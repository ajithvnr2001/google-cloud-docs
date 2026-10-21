---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail
title: Package com.google.appengine.api.mail (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:02:23.435204+00:00
---

# Package com.google.appengine.api.mail (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.mail (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides a service to send email messages on behalf of administrators or authenticated users, also accessible via a [JavaMail](http://www.oracle.com/technetwork/java/javamail/index.html) interface. Receiving messages is not supported via the JavaMail API but is supported via [an HTTP interface](http://cloud.google.com/appengine/docs/java/mail/receiving.html).

This low-level API is intended primarily for framework authors. For application developers we provide a custom `javax.mail.Transport` that allows the standard `javax.mail` interface to be used to send emails. No special configuration is required to send emails via this interface.

The MailService.Message class represents a message, including sender and recipient information, and possibly attachments as MailService.Attachment objects. These can be independently created via their respective constructors.

Sending a message requires a MailService object, created by the MailServiceFactory. Messages are sent asynchronously, so the `MailService` methods will always succeed immediately. Any errors in the mail message will be returned to the sender's address as "bounce" messages. See Also: [JavaMail API](http://www.oracle.com/technetwork/java/javamail/index.html), [com.google.appengine.api.mail.MailService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService), [The Mail Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/mail/)

## Classes 

### [BounceNotification](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification)

The `BounceNotification` object represents an incoming bounce notification.

### [BounceNotification.BounceNotificationBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.BounceNotificationBuilder)

### [BounceNotification.Details](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.Details)

The `BounceNotification.Details` class describes either the original message that caused a bounce, or the notification message describing the bounce.

### [BounceNotification.DetailsBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.DetailsBuilder)

### [BounceNotificationParser](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotificationParser)

The `BounceNotificationParser` parses an incoming HTTP request into a description of a bounce notification.

### [IMailServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.IMailServiceFactoryProvider)

Factory provider for [IMailServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.IMailServiceFactory).

**Note:** This class is not intended for end users.

### [MailService.Attachment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Attachment)

### [MailService.Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Header)

### [MailService.Message](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Message)

Messages are prepared by the caller, and then submitted to the Mail service for sending. Different fields are subject to different constraints, as enumerated in the `send` and `sendToAdmins` methods.

### [MailServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServiceFactory)

Factory for creating a [MailService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService).

### [MailServicePb](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb)

### [MailServicePb.MailAttachment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailAttachment)

### [MailServicePb.MailAttachment.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailAttachment.Builder)

### [MailServicePb.MailHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailHeader)

### [MailServicePb.MailHeader.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailHeader.Builder)

### [MailServicePb.MailMessage](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailMessage)

### [MailServicePb.MailMessage.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailMessage.Builder)

### [MailServicePb.MailServiceError](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailServiceError)

### [MailServicePb.MailServiceError.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailServiceError.Builder)

### [MailStubServicePb](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb)

### [MailStubServicePb.ClearSentMessagesResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.ClearSentMessagesResponse)

### [MailStubServicePb.ClearSentMessagesResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.ClearSentMessagesResponse.Builder)

### [MailStubServicePb.GetLogMailBodyResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetLogMailBodyResponse)

### [MailStubServicePb.GetLogMailBodyResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetLogMailBodyResponse.Builder)

### [MailStubServicePb.GetLogMailLevelResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetLogMailLevelResponse)

### [MailStubServicePb.GetLogMailLevelResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetLogMailLevelResponse.Builder)

### [MailStubServicePb.GetSentMessagesResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetSentMessagesResponse)

### [MailStubServicePb.GetSentMessagesResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetSentMessagesResponse.Builder)

### [MailStubServicePb.SetLogMailBodyRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.SetLogMailBodyRequest)

### [MailStubServicePb.SetLogMailBodyRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.SetLogMailBodyRequest.Builder)

### [MailStubServicePb.SetLogMailLevelRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.SetLogMailLevelRequest)

### [MailStubServicePb.SetLogMailLevelRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.SetLogMailLevelRequest.Builder)

## Interfaces 

### [IMailServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.IMailServiceFactory)

Factory for creating a [MailService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService).

### [MailService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService)

The `MailService` provides a way for user code to send emails to arbitrary destinations.

### [MailServicePb.MailAttachmentOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailAttachmentOrBuilder)

### [MailServicePb.MailHeaderOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailHeaderOrBuilder)

### [MailServicePb.MailMessageOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailMessageOrBuilder)

### [MailServicePb.MailServiceErrorOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailServiceErrorOrBuilder)

### [MailStubServicePb.ClearSentMessagesResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.ClearSentMessagesResponseOrBuilder)

### [MailStubServicePb.GetLogMailBodyResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetLogMailBodyResponseOrBuilder)

### [MailStubServicePb.GetLogMailLevelResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetLogMailLevelResponseOrBuilder)

### [MailStubServicePb.GetSentMessagesResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetSentMessagesResponseOrBuilder)

### [MailStubServicePb.SetLogMailBodyRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.SetLogMailBodyRequestOrBuilder)

### [MailStubServicePb.SetLogMailLevelRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.SetLogMailLevelRequestOrBuilder)

## Enums 

### [MailServicePb.MailServiceError.ErrorCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailServiceError.ErrorCode)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
