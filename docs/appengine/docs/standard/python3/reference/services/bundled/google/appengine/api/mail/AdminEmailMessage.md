---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/AdminEmailMessage/
title: google.appengine.api.mail.AdminEmailMessage \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:46:54.069883+00:00
---

# google.appengine.api.mail.AdminEmailMessage  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/AdminEmailMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.mail.AdminEmailMessage Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1526-L1561) Interface that sends email messages to all administrators via the Mail API. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.mail.AdminEmailMessage(
        mime_message=None, **kw
    )
    

This class is used to programmatically build an administrator email message to be sent via the Mail API. To use the class, construct an instance, populate its fields, and call `Send()`. Unlike normal email messages, addresses in the recipient fields are ignored and not used to send the message. An `AdminEmailMessage` can be built completely by the constructor:
    
    
    AdminEmailMessage(sender='sender@nowhere.com',
                      subject='a subject',
                      body='This is an email to you').Send()
    

You might want your application to build an administrator email in different places throughout the code. For this, `AdminEmailMessage` is mutable:
    
    
    message = AdminEmailMessage()
    message.sender = 'sender@nowhere.com'
    message.subject = 'a subject'
    message.body = 'This is an email to you'
    message.check_initialized()
    message.send()
    

| 

## Args  
  
---  
  
`mime_message` |  The MIME message to initialize from. If the message is an instance of `email.message.Message`, `mime_message` will take ownership as specified the original message.   
`**kw` |  List of keyword properties as defined by `PROPERTIES`.   
  
## Attributes  
  
---  
  
`original` |  Gets the original MIME message from which values were set.   
  
## Methods

### `CheckInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1103-L1105)
    
    
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1124-L1175)
    
    
    ToProto()
    

Converts an email message to a protocol message.

Unicode strings are converted to UTF-8 for all fields.

This method is overridden by `EmailMessage` to support the sender field.

Returns  
---  
The `MailMessage` protocol version of the mail message.   
  
Raises  
---  
Decoding errors when using `EncodedPayload` objects.   
  
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1028-L1100)
    
    
    check_initialized()
    

Checks if `EmailMessage` is properly initialized.

This function tests if `EmailMessage` meets the basic requirements to be used with the Mail API. To function properly, this function requires that the following fields must be set or have at least one value in the case of multi-value fields:
    
    
    - A subject must be set.
    - A recipient must be specified.
    - The message must contain a body.
    - All bodies and attachments must decode properly.
    

This test does not include determining if the sender is actually authorized to send email for the application.

Raises  
---  
  
`InvalidAttachmentTypeError` |  The attachment type is invalid.   
`MissingRecipientsError` |  No recipients were specified in the 'To', 'Cc', or 'Bcc' fields.   
`MissingSenderError` |  A sender was not specified.   
`MissingSubjectError` |  A subject was not specified.   
`MissingBodyError` |  A body was not specified.   
`PayloadEncodingError` |  The payload was not properly encoded.   
`UnknownEncodingError` |  The payload encoding could not be determined.   
`UnknownCharsetError` |  The character set of the payload could not be determined.   
  
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1340-L1370)
    
    
    update_from_mime_message(
        mime_message
    )
    

Copies information from a MIME message.

Information from the `email.Message` instance is set to the values of the MIME message. This function will only copy values that it finds. Missing values will not be copied, nor will those values overwrite old values with blank values.

This object is not guaranteed to be initialized after this call.

Args  
---  
  
`mime_message` |  The `email.Message` instance from which to copy information.   
  
Returns  
---  
A MIME message instance of the `mime_message`.   
  
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
