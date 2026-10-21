---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/MailMessageToMIMEMessage/
title: google.appengine.api.mail.MailMessageToMIMEMessage \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:47:07.284768+00:00
---

# google.appengine.api.mail.MailMessageToMIMEMessage  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/MailMessageToMIMEMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.mail.MailMessageToMIMEMessage Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L505-L580) Generates a `MIMEMultipart` message from a `MailMessage` protocol buffer.

#### View aliases

**Main aliases** `google.appengine.api.mail.mail_message_to_mime_message`
    
    
    google.appengine.api.mail.MailMessageToMIMEMessage(
        protocol_message
    )
    

This function generates a complete `MIMEMultipart` email object from a `MailMessage` protocol buffer. The body fields are sent as individual alternatives if they are both present; otherwise, only one body part is sent. Multiple entry email fields, such as 'To', 'Cc', and 'Bcc' are converted to a list of comma-separated email addresses. | 

## Args  
  
---  
  
`protocol_message` |  Message protocol buffer to convert to a `MIMEMultipart` message.   
  
## Returns  
  
---  
A `MIMEMultipart` message that represents the provided `MailMessage`.   
  
## Raises  
  
---  
  
`InvalidAttachmentTypeError` |  If the file type of the attachment is invalid.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
