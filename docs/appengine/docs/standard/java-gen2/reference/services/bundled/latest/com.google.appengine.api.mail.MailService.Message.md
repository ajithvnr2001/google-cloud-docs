---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Message
title: Class MailService.Message (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:13:57.986253+00:00
---

# Class MailService.Message (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Message

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class MailService.Message (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static class MailService.Message

Messages are prepared by the caller, and then submitted to the Mail service for sending. Different fields are subject to different constraints, as enumerated in the `send` and `sendToAdmins` methods.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MailService.Message

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### Message()
    
    
    public Message()

### Message(String sender, String to, String subject, String textBody)
    
    
    public Message(String sender, String to, String subject, String textBody)

Convenience constructor for simple messages

**Parameters**  
---  
**Name** | **Description**  
`sender` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The sender's email address.  
`to` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The recipient's email address or null for empty to address.  
`subject` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The message subject.  
`textBody` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The text body of the message.  
  
## Methods 

### getAmpHtmlBody()
    
    
    public String getAmpHtmlBody()

Gets the AMP HTML body of this message. See [#setAmpHtmlBody](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Message#com_google_appengine_api_mail_MailService_Message_setAmpHtmlBody_) for more details.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The AMP HTML body.  
  
### getAttachments()
    
    
    public Collection<MailService.Attachment> getAttachments()

Gets the attachments of this message.

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Attachment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Attachment)>` | A collection containing the attachments of this message.  
  
### getBcc()
    
    
    public Collection<String> getBcc()

Gets the recipients in the 'bcc' field of this message.

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A collection containing the 'bcc' field recipients.  
  
### getCc()
    
    
    public Collection<String> getCc()

Gets the recipients in the 'cc' field of this message.

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A collection containing the 'cc' field recipients.  
  
### getHeaders()
    
    
    public Collection<MailService.Header> getHeaders()

Gets the headers of this message.

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Header)>` | A collection containing the headers of this message.  
  
### getHtmlBody()
    
    
    public String getHtmlBody()

Gets the html body of this message.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The html body.  
  
### getReplyTo()
    
    
    public String getReplyTo()

Gets the reply to field of this message.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The reply to field of this message.  
  
### getSender()
    
    
    public String getSender()

Gets the sender of this message.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sender of this message.  
  
### getSubject()
    
    
    public String getSubject()

Gets the subject of this message.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subject of this message.  
  
### getTextBody()
    
    
    public String getTextBody()

Gets the text body of this message.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text body.  
  
### getTo()
    
    
    public Collection<String> getTo()

Gets the recipients in the 'to' field of this message.

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A collection containing the 'to' field recipients.  
  
### setAmpHtmlBody(String ampHtmlBody)
    
    
    public void setAmpHtmlBody(String ampHtmlBody)

Sets the AMP HTML body of this message. This field is optional. Setting AMP HTML body makes the email an AMP Email. Plain text or HTML may become fallback content depending on the email client used.

**Parameter**  
---  
**Name** | **Description**  
`ampHtmlBody` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A string containing the new AMP HTML body of this message.  
  
### setAttachments(MailService.Attachment[] attachments)
    
    
    public void setAttachments(MailService.Attachment[] attachments)

Sets the attachments of this message. `attachments` may be `null`, otherwise each attachment must have a corresponding file name with an extension not on the block list.

**Parameter**  
---  
**Name** | **Description**  
`attachments` | `[Attachment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Attachment)[]`  
Attachments to attach to this message.  
  
### setAttachments(Collection<MailService.Attachment> attachments)
    
    
    public void setAttachments(Collection<MailService.Attachment> attachments)

Sets the attachments of this message. `attachments` may be `null`, otherwise each attachment must have a corresponding file name with an extension not on the block list.

**Parameter**  
---  
**Name** | **Description**  
`attachments` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Attachment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Attachment)>`  
A collection of attachments.  
  
### setBcc(String[] bcc)
    
    
    public void setBcc(String[] bcc)

Sets the 'bcc' field of this message. Each string represents exactly one email address. Having null (or invalid addresses) will lead bcc eventual failure during the send process.

**Parameter**  
---  
**Name** | **Description**  
`bcc` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
The email addresses bcc set as the 'bcc' field.  
  
### setBcc(Collection<String> bcc)
    
    
    public void setBcc(Collection<String> bcc)

Sets the 'bcc' field of this message. Each string in the collection represents exactly one email address. Having null (or invalid addresses) will lead bcc eventual failure during the send process.

**Parameter**  
---  
**Name** | **Description**  
`bcc` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
A collection containing the email addresses bcc set as the 'bcc' field.  
  
### setCc(String[] cc)
    
    
    public void setCc(String[] cc)

Sets the 'cc' field of this message. Each string represents exactly one email address. Having null (or invalid addresses) will lead cc eventual failure during the send process.

**Parameter**  
---  
**Name** | **Description**  
`cc` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
The email addresses cc set as the 'cc' field.  
  
### setCc(Collection<String> cc)
    
    
    public void setCc(Collection<String> cc)

Sets the 'cc' field of this message. Each string in the collection represents exactly one email address. Having null (or invalid addresses) will lead cc eventual failure during the send process.

**Parameter**  
---  
**Name** | **Description**  
`cc` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
A collection containing the email addresses cc set as the 'cc' field.  
  
### setHeaders(MailService.Header[] headers)
    
    
    public void setHeaders(MailService.Header[] headers)

Sets the headers of this message. `headers` may be `null`, otherwise each header name must be one of the allowed names.

**Parameter**  
---  
**Name** | **Description**  
`headers` | `[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Header)[]`  
A collection of headers.  
  
### setHeaders(Collection<MailService.Header> headers)
    
    
    public void setHeaders(Collection<MailService.Header> headers)

Sets the headers of this message. `headers` may be `null`, otherwise each header name must be one of the allowed names.

**Parameter**  
---  
**Name** | **Description**  
`headers` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Header)>`  
A collection of headers.  
  
### setHtmlBody(String htmlBody)
    
    
    public void setHtmlBody(String htmlBody)

Sets the html body of this message. At least one of `textBody` and `htmlBody` must not be `null`.

**Parameter**  
---  
**Name** | **Description**  
`htmlBody` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A string containing the new html body of this message.  
  
### setReplyTo(String replyTo)
    
    
    public void setReplyTo(String replyTo)

`replyTo` may be `null`, or must be a valid email address otherwise.

**Parameter**  
---  
**Name** | **Description**  
`replyTo` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setSender(String sender)
    
    
    public void setSender(String sender)

`sender` must correspond to the valid email address of one of the admins for this application, or to the email address of the currently logged-in user. Sender is really the From: field of the email.

**Parameter**  
---  
**Name** | **Description**  
`sender` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setSubject(String subject)
    
    
    public void setSubject(String subject)

Sets the subject of this message. A null or empty subject will lead to eventual failure during the send process.

**Parameter**  
---  
**Name** | **Description**  
`subject` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A string containing the new subject of this message.  
  
### setTextBody(String textBody)
    
    
    public void setTextBody(String textBody)

Sets the text body of this message. At least one of `textBody` and `htmlBody` must not be `null`.

**Parameter**  
---  
**Name** | **Description**  
`textBody` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A string containing the new text body of this message.  
  
### setTo(String[] to)
    
    
    public void setTo(String[] to)

Sets the 'to' field of this message. Each string represents exactly one email address. Having null (or invalid addresses) will lead to eventual failure during the send process.

**Parameter**  
---  
**Name** | **Description**  
`to` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
The email addresses to set as the 'to' field.  
  
### setTo(Collection<String> to)
    
    
    public void setTo(Collection<String> to)

Sets the 'to' field of this message. Each string in the collection represents exactly one email address. Having null (or invalid addresses) will lead to eventual failure during the send process.

**Parameter**  
---  
**Name** | **Description**  
`to` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
A collection containing the email addresses to set as the 'to' field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
