---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.jakarta
title: Package com.google.appengine.api.mail.jakarta (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:09:38.363135+00:00
---

# Package com.google.appengine.api.mail.jakarta (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.jakarta

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.mail.jakarta (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides a service to send email messages on behalf of administrators or authenticated users, also accessible via a [JavaMail](http://www.oracle.com/technetwork/java/javamail/index.html) interface. Receiving messages is not supported via the JavaMail API but is supported via [an HTTP interface](http://cloud.google.com/appengine/docs/java/mail/receiving.html).

This low-level API is intended primarily for framework authors. For application developers we provide a custom `javax.mail.Transport` that allows the standard `javax.mail` interface to be used to send emails. No special configuration is required to send emails via this interface.

The [com.google.appengine.api.mail.MailService.Message](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Message) class represents a message, including sender and recipient information, and possibly attachments as [com.google.appengine.api.mail.MailService.Attachment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Attachment) objects. These can be independently created via their respective constructors.

Sending a message requires a [com.google.appengine.api.mail.MailService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService) object, created by the [com.google.appengine.api.mail.MailServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServiceFactory). Messages are sent asynchronously, so the `MailService` methods will always succeed immediately. Any errors in the mail message will be returned to the sender's address as "bounce" messages. See Also: [JavaMail API](http://www.oracle.com/technetwork/java/javamail/index.html), [com.google.appengine.api.mail.MailService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService), [The Mail Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/mail/)

## Classes 

### [BounceNotificationParser](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.jakarta.BounceNotificationParser)

The `BounceNotificationParser` parses an incoming HTTP request into a description of a bounce notification.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
