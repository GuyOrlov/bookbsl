const SHEET_ID = '1d6WCbNnUAAww92pNTCCjy4cSrgGivcGmoy5SktwOU7A';
const SHEET_NAME = 'Enquiries';
const NOTIFY_EMAIL = 'bookings@cseeker.co.uk';

function doPost(e) {
  const p = (e && e.parameter) || {};
  const submissionId = clean_(p.submissionId, 120);
  if (!submissionId) return text_('missing_submission_id');

  const lock = LockService.getScriptLock();
  lock.waitLock(15000);
  try {
    const ss = SpreadsheetApp.openById(SHEET_ID);
    const sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) throw new Error('Enquiries sheet not found');

    const existing = findSubmission_(sheet, submissionId);
    if (existing) return text_('duplicate:' + existing);

    const received = new Date();
    const year = received.getFullYear();
    const enquiryId = nextEnquiryId_(sheet, year);
    const bookingDate = parseDate_(p.bookingDate);

    sheet.appendRow([
      enquiryId,
      received,
      clean_(p.senderName, 160),
      clean_(p.senderEmail, 254),
      clean_(p.organisation, 200),
      clean_(p.bookingType, 160),
      bookingDate || clean_(p.bookingDate, 40),
      clean_(p.startTime, 40),
      clean_(p.finishTime, 40),
      clean_(p.format, 80),
      clean_(p.venue, 500),
      clean_(p.deafUsers, 80),
      clean_(p.preference, 80),
      clean_(p.supportType, 200),
      clean_(p.supportCount, 80),
      clean_(p.recording, 120),
      clean_(p.prep, 120),
      clean_(p.notes, 1500),
      'New',
      '',
      '',
      '',
      '',
      submissionId
    ]);

    const subject = 'BookBSL enquiry — ' + clean_(p.bookingType, 120) + ' — ' + formatDate_(bookingDate || p.bookingDate);
    const body = buildEmail_(enquiryId, p);
    const options = {to: NOTIFY_EMAIL, subject: subject, body: body, name: 'BookBSL'};
    const replyTo = clean_(p.senderEmail, 254);
    if (replyTo) options.replyTo = replyTo;
    MailApp.sendEmail(options);

    return text_('saved:' + enquiryId);
  } finally {
    lock.releaseLock();
  }
}

function doGet(e) {
  const p = (e && e.parameter) || {};
  const callback = String(p.callback || '');
  const submissionId = clean_(p.submissionId, 120);
  if (!/^[A-Za-z_$][A-Za-z0-9_$]*$/.test(callback)) return text_('invalid_callback');

  let result = {saved:false};
  if (submissionId) {
    const sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName(SHEET_NAME);
    const enquiryId = findSubmission_(sheet, submissionId);
    if (enquiryId) result = {saved:true,enquiryId:enquiryId};
  }
  return ContentService
    .createTextOutput(callback + '(' + JSON.stringify(result) + ');')
    .setMimeType(ContentService.MimeType.JAVASCRIPT);
}

function findSubmission_(sheet, submissionId) {
  const last = sheet.getLastRow();
  if (last < 2) return '';
  const ids = sheet.getRange(2, 24, last - 1, 1).getDisplayValues();
  for (let i = 0; i < ids.length; i++) {
    if (ids[i][0] === submissionId) return String(sheet.getRange(i + 2, 1).getDisplayValue() || '');
  }
  return '';
}

function nextEnquiryId_(sheet, year) {
  const prefix = 'BSL-' + year + '-';
  const last = sheet.getLastRow();
  let max = 0;
  if (last >= 2) {
    const values = sheet.getRange(2, 1, last - 1, 1).getDisplayValues();
    values.forEach(r => {
      const v = String(r[0] || '');
      if (v.indexOf(prefix) === 0) {
        const n = Number(v.slice(prefix.length));
        if (Number.isFinite(n)) max = Math.max(max, n);
      }
    });
  }
  return prefix + String(max + 1).padStart(3, '0');
}

function parseDate_(value) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(String(value || ''))) return null;
  const parts = String(value).split('-').map(Number);
  return new Date(parts[0], parts[1] - 1, parts[2], 12, 0, 0);
}

function formatDate_(value) {
  if (value instanceof Date && !isNaN(value)) return Utilities.formatDate(value, 'Europe/London', 'd MMMM yyyy');
  return clean_(value, 60);
}

function buildEmail_(id, p) {
  return [
    'Hello cSeeker,',
    '',
    'A new BookBSL booking request has been submitted directly from BookBSL.co.uk.',
    '',
    'REFERENCE',
    id,
    '',
    'CONTACT',
    'Name: ' + clean_(p.senderName, 160),
    'Organisation: ' + (clean_(p.organisation, 200) || 'Not provided'),
    'Email: ' + clean_(p.senderEmail, 254),
    '',
    'BOOKING DETAILS',
    'Type: ' + clean_(p.bookingType, 160),
    'Date: ' + formatDate_(parseDate_(p.bookingDate) || p.bookingDate),
    'Time: ' + clean_(p.startTime, 40) + '–' + clean_(p.finishTime, 40),
    'Format: ' + clean_(p.format, 80),
    'Venue / platform: ' + clean_(p.venue, 500),
    'Deaf people needing support: ' + clean_(p.deafUsers, 80),
    'Communication preference checked: ' + clean_(p.preference, 80),
    'Support requested: ' + clean_(p.supportType, 200),
    'Professionals planned: ' + clean_(p.supportCount, 80),
    'Recording / livestream: ' + clean_(p.recording, 120),
    'Preparation information: ' + clean_(p.prep, 120),
    'Extra notes: ' + clean_(p.notes, 1500),
    '',
    'Status: New'
  ].join('\n');
}

function clean_(value, maxLen) {
  return String(value == null ? '' : value).trim().slice(0, maxLen || 500);
}

function text_(value) {
  return ContentService.createTextOutput(String(value)).setMimeType(ContentService.MimeType.TEXT);
}
