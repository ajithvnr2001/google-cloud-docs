---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EncodedPayload/
title: google.appengine.api.mail.EncodedPayload \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:19:01.420450+00:00
---

# google.appengine.api.mail.EncodedPayload  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EncodedPayload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.mail.EncodedPayload Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L826-L955) Wrapper for a payload that contains encoding information. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.mail.EncodedPayload(
        payload: bytes, charset=None, encoding=None
    )
    

When an email is received, it is usually encoded using a certain character set, then possibly further encoded using a transfer encoding in that character set. Most of the time, it is possible to decode the encoded payload as-is; however, in the case where it is not, the encoded payload and the original encoding information must be preserved. | 

## Args  
  
---  
  
`payload` |  Maps to an attribute of the same name.   
`charset` |  Maps to an attribute of the same name.   
`encoding` |  Maps to an attribute of the same name.   
  
## Attributes  
  
---  
  
`payload` |  The original encoded payload.   
`charset` |  The character set of the encoded payload. To specify that you want to use the default character set, set this argument to `None`.   
`encoding` |  The transfer encoding of the encoded payload. To specify that you do not want the content to be encoded, set this argument to `None`.   
  
## Methods

### `copy_to`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L912-L923)
    
    
    copy_to(
        mime_message
    )
    

Copies the contents of a message to a MIME message payload.

If no content transfer encoding is specified and the character set does not equal the overall message encoding, the payload will be base64-encoded.

Args  
---  
  
`mime_message` |  Message instance that will receive the new payload.   
  
### `decode`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L858-L889)
    
    
    decode()
    

Attempts to decode the encoded data.

This function attempts to use `Python's codec library`_ to decode the payload. All exceptions are passed back to the caller.

Returns  
---  
The binary or Unicode version of the payload content.   
  
.. _Python's codec library: https://docs.python.org/2/library/codecs.html

### `to_mime_message`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L925-L933)
    
    
    to_mime_message()
    

Converts a message to a MIME message.

Returns  
---  
The MIME message instance of the payload.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L891-L906)
    
    
    __eq__(
        other
    )
    

Equality operator.

Args  
---  
  
`other` |  The other `EncodedPayload` object with which to compare. Comparison with other object types are not implemented.   
  
Returns  
---  
`True` if the payload and encodings are equal; otherwise returns `False`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
