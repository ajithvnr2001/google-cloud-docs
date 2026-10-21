---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EmailMessage/
title: google.appengine.api.mail.EmailMessage \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:25:23.075783+00:00
---

# google.appengine.api.mail.EmailMessage  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EmailMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.mail.EmailMessage Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1405-L1523) Main interface to the Mail API service. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.mail.EmailMessage(
        mime_message: typing.Optional[typing.Union[typing.Text, bytes, typing.TextIO, email.
            message.Message]] = None,
        **kw
    )
    

This class is used to programmatically build an email message to send via the Mail API. To use this class, construct an instance, populate its fields and call `Send()`. An `EmailMessage` can be built completely by the constructor:
    
    
    EmailMessage(sender='sender@nowhere.com',
                 to='recipient@nowhere.com',
                 subject='a subject',
                 body='This is an email to you').Send()
    

You might want your application to build an email in different places throughout the code. For this usage, `EmailMessage` is mutable:
    
    
      message = EmailMessage()
      message.sender = 'sender@nowhere.com'
      message.to = ['recipient1@nowhere.com', 'recipient2@nowhere.com']
      message.subject = 'a subject'
      message.body = 'This is an email to you'
      message.check_initialized()
      message.send()
    

| 

## Attributes  
  
---  
  
`original` |  Gets the original MIME message from which values were set.   
  
## Methods

### `CheckInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1463-L1465)
    
    
    CheckInitialized()
    

Ensures that recipients have been specified.

### `Initialize`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1025-L1026)
    
    
    Initialize(
        **kw
    )
    

### `IsInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1120-L1122)
    
    
    IsInitialized()
    

Determines if `EmailMessage` is properly initialized.

### `Send`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1216-L1217)
    
    
    Send(
        *args, **kwds
    )
    

### `ToMIMEMessage`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1196-L1197)
    
    
    ToMIMEMessage()
    

### `ToProto`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1467-L1486)
    
    
    ToProto()
    

Performs more conversion of recipient fields to the protocol buffer.

Returns  
---  
The `MailMessage` protocol version of the mail message, including sender fields.   
  
### `bodies`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1372-L1402)
    
    
    bodies(
        content_type: typing.Text = None
    )
    

Iterates over all bodies.

Args  
---  
  
`content_type` |  Content type on which to filter. This argument allows you to select only specific types of content. You can use the base type or the content type. For example:
    
    
    content_type = 'text/html'  # Matches only HTML content.
    content_type = 'text'       # Matches text of any kind.
      
  
Yields  
---  
A `(content_type, payload)` tuple for HTML and body in that order.   
  
### `check_initialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1449-L1460)
    
    
    check_initialized()
    

Provides additional checks to ensure that recipients have been specified.

Raises  
---  
  
`MissingRecipientError` |  If no recipients are specified in 'To', 'Cc', or 'Bcc'.   
  
### `initialize`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1012-L1022)
    
    
    initialize(
        **kw
    )
    

Keyword initialization.

This function sets all fields of the email message using the keyword arguments.

Args  
---  
  
`**kw` |  List of keyword properties as defined by `PROPERTIES`.   
  
### `is_initialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1107-L1117)
    
    
    is_initialized()
    

Determines if `EmailMessage` is properly initialized.

Returns  
---  
`True` if the message is properly initialized; otherwise returns `False`.   
  
### `send`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1199-L1213)
    
    
    send(
        make_sync_call=[google.appengine.api.apiproxy_stub_map.MakeSyncCall](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub_map/MakeSyncCall)
    )
    

Sends an email message via the Mail API.

Args  
---  
  
`make_sync_call` |  Method that will make a synchronous call to the API proxy.   
  
### `to_mime_message`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1177-L1193)
    
    
    to_mime_message()
    

Generates a `MIMEMultipart` message from `EmailMessage`.

This function calls `MailMessageToMessage` after converting `self` to the protocol buffer. The protocol buffer is better at handing corner cases than the `EmailMessage` class.

Returns  
---  
A `MIMEMultipart` message that represents the provided `MailMessage`.   
  
Raises  
---  
  
`InvalidAttachmentTypeError` |  The attachment type was invalid.   
`MissingSenderError` |  A sender was not specified.   
`MissingSubjectError` |  A subject was not specified.   
`MissingBodyError` |  A body was not specified.   
  
### `update_from_mime_message`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1504-L1523)
    
    
    update_from_mime_message(
        mime_message
    )
    

Copies information for recipients from a MIME message.

Args  
---  
  
`mime_message` |  The `email.Message` instance from which to copy information.   
  
## Class Variables  
  
---  
  
ALLOWED_EMPTY_PROPERTIES | 
    
    
    {
     'amp_html',
     'body',
     'subject'
    }
      
  
PROPERTIES | 
    
    
    {
     'amp_html',
     'attachments',
     'bcc',
     'body',
     'cc',
     'headers',
     'html',
     'reply_to',
     'sender',
     'subject',
     'to'
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
