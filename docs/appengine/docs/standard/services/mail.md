---
url: https://docs.cloud.google.com/appengine/docs/standard/services/mail/
title: Mail API for legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:21.088946+00:00
---

# Mail API for legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Mail API for legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

**Note:** To improve email security and ensure reliable, high-volume email delivery, we recommend that you [migrate from the legacy Mail API to an SMTP-based email service](https://docs.cloud.google.com/appengine/migration-center/standard/python/mail-to-smtp), such as SendGrid, Mailgun, or Mailjet.

App Engine applications can send email messages on behalf of the app's email receiving addresses and on behalf of some users with Google Accounts. Apps can receive email at various addresses. Apps send messages using the Mail service and receive messages in the form of HTTP requests initiated by App Engine and posted to the app.

## Sending mail

The Mail service can send email messages to one or more recipients. A message contains a subject, a plaintext body, and an optional HTML body. It can also contain file attachments and a limited set of headers.

You can use any email address for a recipient. A recipient can be in the message's "to" field, in the "cc" field, or hidden from the message recipients (a "blind carbon copy" or "bcc").

When an application calls the Mail service to send a message, the message is queued, and the call returns immediately. The Mail service uses standard procedures for contacting each recipient's mail server, delivering the message, and retrying if the mail server cannot be contacted.

## Who can send mail

For security purposes, the sender address of a message must be one of the following:

  * The Gmail or Google Workspace Account of the user who is currently signed in
  * Any email address of the form `anything@[MY_PROJECT_ID].appspotmail.com` or `anything@[MY_PROJECT_NUMBER].appspotmail.com`
  * Any email address listed in the Google Cloud console under [Email API Authorized Senders](https://console.cloud.google.com/appengine/settings)



All email addresses on the [Email API Authorized Senders](https://console.cloud.google.com/appengine/settings) list need to be valid Gmail or Google-hosted domain accounts. App Administrators can add the following accounts to the list of Authorized Senders:

  * Their own email address
  * Any group for which they are an Owner or Manager
  * Applications hosted in a Google Workspace domain: `noreply@[DOMAIN].com`, as long as `noreply@[DOMAIN].com` is a valid account (user or group).



In addition, domain administrators of domains managed by Google Workspace can add any user in their domain to the list of authorized senders.

You are limited to a maximum of 50 authorized senders.

## Mail from Google Workspace

If you will be sending email from a domain managed by Google Workspace, you should set the DNS `SPF` records for your domain to indicate that Google is a trusted source for your email. For instructions on how to do this, see [SPF records](http://www.google.com/support/a/bin/answer.py?answer=33786) in the Google Workspace Help Center.

Note that if you use aliases set up for your Google Workspace domain, you cannot send email from email addresses that use the domain alias.

## Bounce notifications when mail is not delivered

Mail that matches a known signature for spam, viruses, or other malicious content may not be accepted for delivery.

If the Mail service cannot deliver a message, or if a recipient's mail server returns a bounce message (for example, because there is no account for that address on that system), an error message can be sent by email to the address of the sender for the message. The application itself does not receive any notification about whether delivery succeeded or failed.

By default, email bounce notifications are not enabled. In order to receive email bounce notifications, you need to configure your application. For more details, see [Receiving Bounce Notification](https://docs.cloud.google.com/appengine/docs/standard/services/mail/bounce). 

## Mail and the development server

The development server can be configured to send email messages directly from your computer when you test a feature of your app that sends messages. You can configure the development server to use an SMTP server of your choice. Alternatively, you can tell the development server to use Sendmail, if Sendmail is installed on your computer and set up for sending email.

If you do not configure an SMTP server or enable Sendmail, when your app calls the Mail service, the development server will log the contents of the message. The message will not actually be sent.

## Authentication with DomainKeys Identified Mail (DKIM)

When you send mail, App Engine uses the DomainKeys Identified Mail (DKIM) standard to authenticate the domain. If your application sends messages from an email address that is part of a Google Workspace domain, App Engine can cryptographically sign the emails it sends. This signature says that an email that purports to be from `emma@example.com` really came from `example.com`. The recipient can check this signature; if the signature is correct, the recipient knows that the sender's domain wasn't spoofed.

To enable DKIM authentication for messages sent from Google Workspace email addresses, follow [these instructions](http://support.google.com/a/bin/answer.py?answer=174124) in the Google Workspace Help Center. Note that it can take up to 48 hours before DKIM authentication is active for your Google Workspace domain.

You must also ensure that your application is [using a custom domain](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains) and is the same as your Google Workspace domain. Also note that Google Workspace domains with subdomains such as `subdomain.example.com` are not permitted.

App Engine will sign the application's outgoing mails if the sender address is part of a Google Workspace domain with DKIM enabled. Additionally, the sender address must be formatted such that the domain part of the email address only consists of lowercase letters.

## Quotas and limits

To see the current quota usage of your application, go to the Quota Details page in the Google Cloud console.

[Go to the Quota Details page](https://console.cloud.google.com/appengine/quotadetails)

Each Mail service request counts toward the **Mail API Calls** quota. There are also quotas for the number of messages you can send, the number of Admin messages you can send, and the amount of data and attachments you can send. For more details, see [Mail quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas#Mail).

**Note:** Data sent in the body of an email message or as an attachment also counts towards the **Outgoing Bandwidth (billable) quota**.

The quota is reset daily. If you exceed the daily quota, you will get an [over quota exception](https://docs.cloud.google.com/appengine/docs/quotas#When_a_Resource_is_Depleted). If you need to send more mail than the quota allows, you can use a third-party mail provider, such as [SendGrid](https://sendgrid.com/) or [Mailgun](https://www.mailgun.com/).

In addition to quotas, the following limits apply to the Mail service:

Limit | Amount  
---|---  
Maximum size of outgoing mail messages, including attachments | 31.5 MB  
Maximum size of incoming mail messages, including attachments | 31.5 MB  
Maximum size of message when an administrator is a recipient | 16 KB  
Maximum number of authorized senders | 50  
  
## What's next

  * Read the [bulk mail guidelines](https://docs.cloud.google.com/appengine/docs/standard/services/mail/bulk-mail).
  * Learn how to use the Mail API to [send mail](https://docs.cloud.google.com/appengine/docs/standard/services/mail/sending-mail-with-mail-api) and [receive mail](https://docs.cloud.google.com/appengine/docs/standard/services/mail/receiving-mail-with-mail-api).
  * Refer to the [`google.appengine.api.mail` module reference](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail) . 
  * Learn more about the migration considerations for Mail API in the [Mail handlers](https://docs.cloud.google.com/appengine/docs/standard/python3/services/access#mail) guide. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
