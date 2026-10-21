---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InboundEmailMessage/
title: google.appengine.api.mail.InboundEmailMessage \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:02:37.399494+00:00
---

# google.appengine.api.mail.InboundEmailMessage  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InboundEmailMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.mail.InboundEmailMessage Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1564-L1726) Receives a parsed email as it is recevied from an external source. Inherits From: [`EmailMessage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EmailMessage), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.mail.InboundEmailMessage(
        mime_message: typing.Optional[typing.Union[typing.Text, bytes, typing.TextIO, email.
            message.Message]] = None,
        **kw
    )
    

This class makes use of a `date` field and can store any number of additional bodies. These additional attributes make the email more flexible as required for incoming mail, where the developer has less control over the content.

#### Example:

# Read mail message from `CGI` input.

message = InboundEmailMessage(sys.stdin.read()) logging.info('Received email message from %s at %s', message.sender, message.date) enriched_body = list(message.bodies('text/enriched'))[0]

# ... Do something with body ...

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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1671-L1707)
    
    
    bodies(
        content_type: typing.Text = None
    )
    

Iterates over all bodies.

Args  
---  
  
`content_type` |  Content type on which to filter. This argument allows you to select only specific types of content. You can use the base type or the content type. For example, `content_type = 'text/html'` matches only HTML content, and `content_type = 'text'` matches text of any kind.   
  
Yields  
---  
A `(content_type, payload)` tuple for all bodies of a message, including the body, HTML, and all `alternate_bodies`, in that order.   
  
### `check_initialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1449-L1460)
    
    
    check_initialized()
    

Provides additional checks to ensure that recipients have been specified.

Raises  
---  
  
`MissingRecipientError` |  If no recipients are specified in 'To', 'Cc', or 'Bcc'.   
  
### `from_environ`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1593-L1623)
    
    
    @classmethod
    from_environ(
        environ
    )
    

Creates an email message by parsing the HTTP request body in `environ`.

Example (WSGI)::

def app(environ, start_response): mail_message = mail.InboundEmailMessage.from_environ(request.environ)
    
    
    # Do something with the message
    logging.info('Received greeting from %s: %s' % (mail_message.sender,
                                                      mail_message.body))
    start_response("200 OK", [])
    return “Success”
    

**Note:** Flask (other web frameworks) can directly use `new InboundEmailMessage(request_bytes)` to create the email message if they have the request bytes of an HTTP request.

Args  
---  
  
`environ` |  a WSGI dict describing the HTTP request (See PEP 333).   
  
Returns  
---  
An InboundEmailMessage object.   
  
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1709-L1726)
    
    
    to_mime_message()
    

Converts a message to a MIME message.

This function adds additional headers from the inbound email.

Returns  
---  
The MIME message instance of a payload.   
  
### `update_from_mime_message`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1625-L1641)
    
    
    update_from_mime_message(
        mime_message
    )
    

Updates the values of a MIME message.

This function copies over date values.

Args  
---  
  
`mime_message` |  The `email.Message` instance from which you want to copy information.   
  
## Class Variables  
  
---  
  
ALLOWED_EMPTY_PROPERTIES | 
    
    
    {
     'amp_html',
     'body',
     'subject'
    }
      
  
ALLOW_BLANK_EMAIL |  `True`  
PROPERTIES | 
    
    
    {
     'alternate_bodies',
     'amp_html',
     'attachments',
     'bcc',
     'body',
     'cc',
     'date',
     'html',
     'message_id',
     'reply_to',
     'sender',
     'subject',
     'to'
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
