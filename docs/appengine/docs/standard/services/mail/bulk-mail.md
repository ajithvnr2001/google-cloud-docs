---
url: https://docs.cloud.google.com/appengine/docs/standard/services/mail/bulk-mail/
title: Bulk mail guidelines \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:43.929994+00:00
---

# Bulk mail guidelines  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/mail/bulk-mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Bulk mail guidelines Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

You must follow these guidelines if your application is sending out bulk email, that is, similar messages to numerous recipients. These guidelines will help to improve your inbox delivery rate to Gmail users, by ensuring that all recipients in your distribution list actually want to receive the email. If recipients manually mark your email as spam, then that acts as a strong signal to Gmail to mark future emails from you as spam.

For more information on sending mail, see the [Mail API Overview](https://docs.cloud.google.com/appengine/docs/standard/services/mail).

## Authentication and identification

  * Use the same sender for every bulk email. When calling the Mail API function to send email, the `From` header will be set to match the sender you specify.
  * Your sender address should be an account in a [Google Workspace](https://workspace.google.com/) domain. If the domain is still in the free trial period or has less than six users, Google accounts that send too many emails marked as spam might be temporarily disabled. In these cases, the Mail API will throw an exception with an `Unauthorized sender` error message.
  * Sign your email with [DKIM](https://support.google.com/a/answer/174124), which requires a G Suite domain if you are sending using App Engine.
  * Publish an [SPF record](http://support.google.com/a/bin/answer.py?answer=33786) to prevent spammers from spoofing your envelope sender address. SPF verifies that email is sent from an IP address that is published in the DNS records of the envelope sender. App Engine's envelope sender is in the `apphosting.bounces.google.com` domain, so your SPF record may not be used to determine if email from App Engine should be delivered.



## Subscription

  * Each user in your distribution list should opt-in to receive messages from you in one of the following ways: 
    * By sending you an email asking to subscribe
    * By manually checking a box on a web form or within a piece of software
  * Using an email address list purchased from a third party is not considered opt-in. You also should not set a checkbox on a web form or within a piece of software to subscribe all users by default. Users should not be required to explicitly opt out of mailings.
  * You should verify that the person that signed up by checking the box on the web form or in software is actually receiving emails at the address that was specified in the form. Verify the user by sending an email that requires them to confirm receipt.



## Unsubscribing

  * A user must be able to unsubscribe in one of the following ways: 
    * Through a prominent link in the email with no further user interaction other than confirmation.
    * Via an email unsubscribe response.
  * App Engine can only receive email sent to the `[APP_ID].appspotmail.com` domain. Therefore, you will need to set your sender to an address in this domain if you want to automatically handle email unsubscribe responses within App Engine.
  * Use the `List-Unsubscribe` header, which is supported by the App Engine Mail API.
  * Automatically unsubscribe users whose addresses bounce multiple pieces of email. You can configure your app to receive bounce notifications. 
  * Periodically send email confirmations to users, offering the opportunity to unsubscribe from each list they are signed up for.
  * Explicitly indicate the email address subscribed within your email, because users might forward email from other accounts.



## Format

  * Format to [RFC 2822 SMTP standards](http://www.ietf.org/rfc/rfc2822.txt) and, if using HTML, [w3.org standards](http://www.w3.org/standards/techs/html).
  * Attempts to hide the true sender of the message or the true landing page for any web links in the message may result in non-delivery. For example, we recommend that you do not use URL shortener services in bulk email, because these can mask the real URLs contained in the body of your email.
  * The subject of each message should be relevant to the body's content and should not be misleading.



## Delivery

  * The following factors will help messages arrive in Gmail users' inboxes: 
    * The `From` address is listed in the user's Contacts list.
    * A user clicks "Not Spam" to alert Gmail that messages sent from that address are solicited.
  * If you send both promotional email and transactional email relating to your organization, we recommend separating email by purpose as much as possible. You can do this by: 
    * Using separate email addresses for each function.
    * Sending email from different domains for each function.



## Third-party senders

  * If others use your service to send email, you are responsible for monitoring your users and/or clients' behavior. You must remove, in a timely fashion, all users and/or clients who use your service to send spam email. The [Google Cloud Platform Acceptable Use Policy](https://cloud.google.com/terms/aup) specifically prohibits spam. Your application can be suspended if you violate this policy, as described in the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms/).
  * You must have an email address available for users and/or clients to report abuse, which should normally be `abuse@[YOUR_DOMAIN].com`. You should also monitor `postmaster@[YOUR_DOMAIN].com`.
  * Monitor email sent to app admins. Google may need to urgently contact app admins, for example to notify you of a violation of the Acceptable Use Policy. We can help you to resolve the problems more quickly if you respond promptly to our emails.
  * You must maintain up-to-date contact information in your WHOIS record maintained by your domain registrar, and on [abuse.net](http://abuse.net/).



## Affiliate marketing programs

  * Affiliate marketing programs reward third-parties for bringing visitors to your site. These programs are attractive to spammers and can potentially do more harm than good. Please note the following: 
    * If your brand becomes associated with affiliate marketing spam, it can affect the email sent by you and your other affiliates.
    * It is your responsibility to monitor your affiliates and remove them if they send spam.



## Alternatives to the App Engine Mail API

You can use a third-party email delivery service provider to send email from App Engine. These services may provide additional features that are not available in the Mail API and may be a better solution for some bulk email senders.

## Limits for bulk mail

If you send too many emails in a short burst, some emails might be silently dropped due to Google safety limits. To avoid this, calculate the maximum daily rate of emails sent per second by dividing your daily quota by 86,400, the number of seconds in a day. Do not send bulk email at a rate higher than 50 times the maximum daily rate.

For more information on other quotas around sending mail, see [Quotas and limits](https://docs.cloud.google.com/appengine/docs/standard/services/mail#quotas_and_limits).

## What's next

  * Read the [Mail API Overview](https://docs.cloud.google.com/appengine/docs/standard/services/mail).
  * Learn how to use the Mail API to [send mail](https://docs.cloud.google.com/appengine/docs/standard/services/mail/sending-mail-with-mail-api) and [receive mail](https://docs.cloud.google.com/appengine/docs/standard/services/mail/receiving-mail-with-mail-api). 
  * Learn more about the migration considerations for the Mail API in the [Mail handlers](https://docs.cloud.google.com/appengine/docs/standard/python3/services/mail) guide. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
