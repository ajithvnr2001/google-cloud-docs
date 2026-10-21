---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/
title: Module: google.appengine.api.mail \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:59:51.753392+00:00
---

# Module: google.appengine.api.mail  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.mail Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py) Sends email on behalf of the application. This module provides functions for application developers to provide email services for their applications. The module also provides a few utility methods.

## Classes

[`class AdminEmailMessage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/AdminEmailMessage): Interface that sends email messages to all administrators via the Mail API. [`class Attachment`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/Attachment): Attachment object. [`class BounceNotification`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/BounceNotification): Encapsulates a bounce notification received by the application. [`class EmailMessage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EmailMessage): Main interface to the Mail API service. [`class EncodedPayload`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EncodedPayload): Wrapper for a payload that contains encoding information. [`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/Error): Base Mail error type. [`class InboundEmailMessage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InboundEmailMessage): Receives a parsed email as it is recevied from an external source. [`class InvalidAttachmentTypeError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InvalidAttachmentTypeError): The file type of the attachment is invalid. [`class InvalidEmailError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InvalidEmailError): The specified email is invalid. [`class InvalidHeaderNameError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InvalidHeaderNameError): The header name is invalid. [`class InvalidSenderError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InvalidSenderError): The sender is not permitted to send mail for this application. [`class MissingBodyError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/MissingBodyError): A body was not specified in the message. [`class MissingRecipientsError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/MissingRecipientsError): A recipient was not specified in the message. [`class MissingSenderError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/MissingSenderError): A sender was not specified in the message. [`class MissingSubjectError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/MissingSubjectError): The subject was not specified in the message. [`class PayloadEncodingError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/PayloadEncodingError): The payload encoding is unknown. [`class UnknownCharsetError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/UnknownCharsetError): The character set is unknown. [`class UnknownEncodingError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/UnknownEncodingError): The encoding is unknown.

## Functions

[`CheckEmailValid(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/CheckEmailValid): Verifies whether an email is valid. [`InvalidEmailReason(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InvalidEmailReason): Determines the reason why an email is invalid. [`IsEmailValid(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/IsEmailValid): Determines whether an email address is invalid. [`MailMessageToMIMEMessage(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/MailMessageToMIMEMessage): Generates a `MIMEMultipart` message from a `MailMessage` protocol buffer. [`SendMail(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/SendMail): Sends mail on behalf of the application. [`SendMailToAdmins(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/SendMailToAdmins): Sends email to administrators on behalf of the application. [`check_email_valid(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/CheckEmailValid): Verifies whether an email is valid. [`check_headers_valid(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/check_headers_valid): Checks that `headers` is a valid dictionary for a header. [`invalid_email_reason(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InvalidEmailReason): Determines the reason why an email is invalid. [`invalid_headers_reason(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/invalid_headers_reason): Determines the reason why a header is invalid. [`is_ascii(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/is_ascii): Returns whether a string is in ASCII. [`is_email_valid(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/IsEmailValid): Determines whether an email address is invalid. [`mail_message_to_mime_message(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/MailMessageToMIMEMessage): Generates a `MIMEMultipart` message from a `MailMessage` protocol buffer. [`send_mail(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/SendMail): Sends mail on behalf of the application. [`send_mail_to_admins(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/SendMailToAdmins): Sends email to administrators on behalf of the application. | 

## Other Members  
  
---  
  
BOUNCE_NOTIFICATION_URL_PATH |  `'/_ah/bounce'`  
ERROR_MAP | 
    
    
    {
     2: <class 'google.appengine.api.mail_errors.BadRequestError'>,
     3: <class 'google.appengine.api.mail_errors.InvalidSenderError'>,
     4: <class 'google.appengine.api.mail_errors.InvalidAttachmentTypeError'>,
     5: <class 'google.appengine.api.mail_errors.InvalidHeaderNameError'>
    }
      
  
EXTENSION_BLACKLIST |  `['ade', 'adp', 'bat', 'chm', 'cmd', 'com', 'cpl', 'exe', 'hta', 'ins', 'isp', 'jse', 'lib', 'mde', 'msc', 'msp', 'mst', 'pif', 'scr', 'sct', 'shb', 'sys', 'vb', 'vbe', 'vbs', 'vxd', 'wsc', 'wsf', 'wsh']`  
EXTENSION_MIME_MAP | 
    
    
    {
     'aif': 'audio/x-aiff',
     'aifc': 'audio/x-aiff',
     'aiff': 'audio/x-aiff',
     'asc': 'text/plain',
     'au': 'audio/basic',
     'avi': 'video/x-msvideo',
     'bmp': 'image/x-ms-bmp',
     'c': 'text/plain',
     'css': 'text/css',
     'csv': 'text/csv',
     'diff': 'text/plain',
     'doc': 'application/msword',
     'docx': 'application/msword',
     'flac': 'audio/flac',
     'gif': 'image/gif',
     'gzip': 'application/x-gzip',
     'htm': 'text/html',
     'html': 'text/html',
     'ics': 'text/calendar',
     'jpe': 'image/jpeg',
     'jpeg': 'image/jpeg',
     'jpg': 'image/jpeg',
     'kml': 'application/vnd.google-earth.kml+xml',
     'kmz': 'application/vnd.google-earth.kmz',
     'log': 'text/plain',
     'm4a': 'audio/mp4',
     'mid': 'audio/mid',
     'mov': 'video/quicktime',
     'mp3': 'audio/mpeg',
     'mp4': 'video/mp4',
     'mpe': 'video/mpeg',
     'mpeg': 'video/mpeg',
     'mpg': 'video/mpeg',
     'odp': 'application/vnd.oasis.opendocument.presentation',
     'ods': 'application/vnd.oasis.opendocument.spreadsheet',
     'odt': 'application/vnd.oasis.opendocument.text',
     'oga': 'audio/ogg',
     'ogg': 'audio/ogg',
     'ogv': 'video/ogg',
     'patch': 'text/plain',
     'pdf': 'application/pdf',
     'png': 'image/png',
     'pot': 'text/plain',
     'pps': 'application/vnd.ms-powerpoint',
     'ppt': 'application/vnd.ms-powerpoint',
     'pptx': 'application/vnd.ms-powerpoint',
     'qt': 'video/quicktime',
     'rmi': 'audio/mid',
     'rss': 'text/rss+xml',
     'snd': 'audio/basic',
     'sxc': 'application/vnd.sun.xml.calc',
     'sxw': 'application/vnd.sun.xml.writer',
     'text': 'text/plain',
     'tif': 'image/tiff',
     'tiff': 'image/tiff',
     'txt': 'text/plain',
     'vcf': 'text/directory',
     'wav': 'audio/x-wav',
     'wbmp': 'image/vnd.wap.wbmp',
     'webm': 'video/webm',
     'webp': 'image/webp',
     'xls': 'application/vnd.ms-excel',
     'xlsx': 'application/vnd.ms-excel',
     'zip': 'application/zip'
    }
      
  
HEADER_WHITELIST | 
    
    
    {
     'Auto-Submitted',
     'In-Reply-To',
     'List-Id',
     'List-Unsubscribe',
     'On-Behalf-Of',
     'References',
     'Resent-Date',
     'Resent-From',
     'Resent-To'
    }
      
  
INCOMING_MAIL_URL_PATTERN |  `'/_ah/mail/.+'`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
