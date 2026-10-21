---
url: https://docs.cloud.google.com/appengine/docs/standard/services/mail/sending-mail-with-mail-api/
title: Sending mail with the Mail API \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:49.780608+00:00
---

# Sending mail with the Mail API  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/mail/sending-mail-with-mail-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Sending mail with the Mail API Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This guide describes how to use the Mail API to send mail.

The Mail API provides two ways to send an email message: the [`mail.send_mail()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/SendMail) function and the [`EmailMessage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EmailMessage) class.

Sending is asynchronous: the `mail.send_mail()` function and the `EmailMessage.send()` method transmit the message data to the mail service, then return. The mail service queues the message, then attempts to send it, retrying if the destination mail server is unavailable. Errors and bounce messages are sent to the sender address for the email message.

## Before you begin

Register your sender emails as authorized senders. For more information, see [who can send email](https://docs.cloud.google.com/appengine/docs/standard/services/mail#who_can_send_mail).

## Sending mail with `mail.send_mail()`

To send mail using the [`mail.send_mail()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/SendMail) function, use the fields of the email message as parameters, including the sender, the recipients, the subject and the body of the message. For example:
    
    
        mail.send_mail(sender=sender_address,
                       to="Albert Johnson <Albert.Johnson@example.com>",
                       subject="Your account has been approved",
                       body="""Dear Albert:
    
    Your example.com account has been approved.  You can now visit
    http://www.example.com/ and sign in using your Google Account to
    access new features.
    
    Please let us know if you have any questions.
    
    The example.com Team
    """)

## Sending mail with `EmailMessage`

To send mail using objects with the [`EmailMessage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EmailMessage) class, pass the fields of the email message to the `EmailMessage` constructor and use attributes of the instance to update message.

The [`EmailMessage.send()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EmailMessage#Send) method sends the email message represented by the instance's attributes. An application can re-use an `EmailMessage` instance by modifying attributes and calling the `send()` method again.
    
    
        message = mail.EmailMessage(
            sender=sender_address,
            subject="Your account has been approved")
    
        message.to = "Albert Johnson <Albert.Johnson@example.com>"
        message.body = """Dear Albert:
    
    Your example.com account has been approved.  You can now visit
    http://www.example.com/ and sign in using your Google Account to
    access new features.
    
    Please let us know if you have any questions.
    
    The example.com Team
    """
        message.send()

## Sending bulk mail

See the [Bulk mail guidelines](https://docs.cloud.google.com/appengine/docs/standard/services/mail/bulk-mail) for considerations around sending bulk email.

Learn more about the migration considerations for Mail API in the [Mail handlers](https://docs.cloud.google.com/appengine/docs/standard/python3/services/mail) guide.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
