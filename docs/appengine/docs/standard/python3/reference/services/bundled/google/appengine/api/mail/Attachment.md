---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/Attachment/
title: google.appengine.api.mail.Attachment \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:28:40.410411+00:00
---

# google.appengine.api.mail.Attachment  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/Attachment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.mail.Attachment Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L735-L823) Attachment object. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.mail.Attachment(
        filename, payload, content_id=None
    )
    

An Attachment object is largely interchangeable with a `(filename, payload)` tuple.

#### Note:

The behavior is a bit asymmetric with respect to unpacking and equality comparison. An Attachment object without a content ID will be equivalent to a `(filename, payload)` tuple. An Attachment with a content ID will unpack to a `(filename, payload)` tuple, but will compare unequally to that tuple. Thus, the following comparison will succeed:
    
    
    attachment = mail.Attachment('foo.jpg', 'data')
    filename, payload = attachment
    attachment == filename, payload
    

...while the following will fail:
    
    
    attachment = mail.Attachment('foo.jpg', 'data', content_id='<foo>')
    filename, payload = attachment
    attachment == filename, payload
    

The following comparison will pass: attachment = mail.Attachment('foo.jpg', 'data', content_id='') attachment == (attachment.filename, attachment.payload, attachment.content_id) | 

## Arguments  
  
---  
  
`filename` |  The name of the attachment.   
`payload` |  The attachment data.   
`content_id` |  Optional; the content ID for this attachment.   
  
## Attributes  
  
---  
  
`filename` |  The name of the attachment.   
`payload` |  The attachment data.   
`content_id` |  Optional; the content ID for this attachment. Keyword only.   
  
## Methods

### `__contains__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L819-L820)
    
    
    __contains__(
        val
    )
    

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L788-L802)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__getitem__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L816-L817)
    
    
    __getitem__(
        i
    )
    

### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L813-L814)
    
    
    __iter__()
    

### `__len__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L822-L823)
    
    
    __len__()
    

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L810-L811)
    
    
    __ne__(
        other
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
