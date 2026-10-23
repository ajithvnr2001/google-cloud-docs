---
url: https://docs.cloud.google.com/appengine/docs/standard/services/mail/receiving-mail-with-mail-api/
title: Receiving mail with the Mail API \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:08.854578+00:00
---

# Receiving mail with the Mail API  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/mail/receiving-mail-with-mail-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Receiving mail with the Mail API Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This guide describes how to use the Mail API to receive mail.

Email messages sent to your app are implemented as HTTP requests containing MIME data. To process incoming email messages, you associate email addresses with script handlers in your app configuration, then include the handlers in your app's code.

Incoming email generates HTTP requests, which are passed to the appropriate scripts. The scripts that handle the incoming email must reside in your default service.

For more information on the Mail service, see the [Mail API Overview](https://docs.cloud.google.com/appengine/docs/standard/services/mail).

## Before you begin

You must register your sender emails as authorized senders. For more information, see [who can send email](https://docs.cloud.google.com/appengine/docs/standard/services/mail#who_can_send_mail).

## Configuring your application to receive email

When you create a new app, incoming email is disabled by default. To enable the incoming email, you must modify your `app.yaml` file in your default service.

  1. Add an `inbound_services` section that enables the incoming email service. For example:
         
         inbound_services:
         - mail

If you don't enable incoming email by including this section in your configuration file, then incoming email is disabled, and email messages sent to the app are ignored.

  2. Add mappings that associate URL-mapped email addresses with script handlers.

For the [default service](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine#components_of_an_application), the email address for receiving email has the following format:
         
         [STRING]@[Google Cloud project ID].appspotmail.com
         

For non-default services, the email address has the following format:
         
         [STRING]@[servicename]-dot-[Google Cloud project ID].appspotmail.com
         

Email messages are sent to your app as HTTP POST requests using the following URL, where [ADDRESS] is a full email address, including domain name:
         
         /_ah/mail/[ADDRESS]
         

To handle incoming email in your app, map email URLs to handlers in the `app.yaml` file:
         
         - url: /_ah/mail/.+
           script: handle_incoming_email.app
           login: admin

In the above example, `/_ah/mail/.+` matches all email addressed to the app. If you prefer, you can set up multiple handlers for different email addresses, as in the following example:
         
         - url: /_ah/mail/owner@.*your_app_id\.appspotmail\.com
           script: handle_owner.app
           login: admin
         - url: /_ah/mail/support@.*your_app_id\.appspotmail\.com
           script: handle_support.app
           login: admin
         - url: /_ah/mail/.+
           script: handle_catchall.app
           login: admin

URLs of incoming email messages are matched to this list from first to last, so if an email message URL matches more than one pattern, the first matching handler will be the one executed. This allows you to include a "catchall" handler as the last mapping. The handlers run in the default module (or application version).




## Handling incoming email

When using Python web frameworks, the `InboundEmailMessage` constructor takes in the bytes of the HTTP request body. There are multiple ways to create the `InboundEmailMessage` object in Python. In Flask, `request.get_data()` gives the request bytes. The `InboundEmailMessage` object contains the email message. Its `bodies()` method returns the bodies within the message. If you call `bodies()` without arguments, it returns an iterator that yields HTML bodies first, then plain text bodies. If you want just HTML or just plain text, you can pass an argument to `bodies()`:
    
    
    @app.route("/_ah/mail/<path>", methods=["POST"])
    def receive_mail(path):
        message = mail.InboundEmailMessage(request.get_data())
    
        # Do something with the message
        print(
            f"Received greeting for {escape(message.to)} at {escape(message.date)} from {escape(message.sender)}"
        )
        for content_type, payload in message.bodies("text/plain"):
            print(f"Text/plain body: {payload.decode()}")
            break
    
        return "OK", 200
    
    

The `InboundEmailMessage` object includes attributes to access other message fields:

  * `subject` contains the message subject.
  * `sender` is the sender's address e.g. `"Nobody <nobody@example.com>"`.
  * `to` is a comma-separated list of the message's primary recipients e.g. `"Joe <joe@example.com>, Bill <bill@example.com>"`.
  * `cc` contains a comma-separated list of the cc recipients e.g. `"Joe <joe@example.com>, Bill <bill@example.com>"`.
  * `date` returns the message date.
  * `attachments` is a list of [`Attachment`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/Attachment) objects, possibly empty.
  * `original` is the complete message, including data not exposed by the other fields such as email headers, as a Python [`email.message.Message`](http://docs.python.org/library/email.message.html).



## Simulating incoming messages with the local development server

Once you set up your app to handle incoming email, you can use the development server console to simulate incoming email messages:

  1. Access the development server as an administrator by going to <http://localhost:8080/console> and selecting **Sign in as administrator**.
  2. In the development server, click **Inbound Mail** in the navigation.
  3. Fill out the form that appears, and click **Send Email**.

To get the development server running, see [the local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server).




Learn more about the migration considerations for Mail API in the [Mail handlers](https://docs.cloud.google.com/appengine/docs/standard/python3/services/mail) guide.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
