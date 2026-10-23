---
url: https://docs.cloud.google.com/appengine/docs/standard/services/mail/bounce/
title: Receiving bounce notification \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:38.300530+00:00
---

# Receiving bounce notification  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/mail/bounce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Receiving bounce notification Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

In order to receive email bounce notifications, you need to configure your app to enable email notification and you need to create a handler to handle those incoming notifications.

## Configuring your application for email bounce notification

There are two parts to the configuration. First, you need to enable notification. Second, you need to set the mapping between `/_ah/bounce` and your bounce handler, so App Engine knows where to POST the notification data. To configure your app to receive bounced email notifications:

  * Add the following to your `app.yaml` file to enable notification:
        
        inbound_services:
            - mail_bounce
        

  * Also in `app.yaml`, declare a mapping between `/_ah/bounce` and the bounce notification handler in your code, for example:
        
        - url: /_ah/bounce
          script: handle_bounced_email.app
          login: admin




## Handling bounce notifications

A [bounce notification](http://en.wikipedia.org/wiki/Bounce_message) is an automated message from an email system that there's been a problem with message delivery. In your app, you'll need to create bounce handler code to receive and process these notifications.

One way to write a bounce handler is to use the [`BounceNotificationHandler`](https://docs.cloud.google.com/appengine/docs/standard/python3/services/mail#receiving_bounce_notifications) convenience class. If you go this route, you'll need to override its `receive()` method, which is called with an argument of the [`BounceNotification`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/BounceNotification) class. Whether you use the `BounceNotificationHandler` convenience class or not, you do need to use `BounceNotification` to parse the bounce notifications.

Here is a sample bounce handler that uses the `BounceNotificationHandler` convenience class:
    
    
    @app.route("/_ah/bounce", methods=["POST"])
    def receive_bounce():
        bounce_message = mail.BounceNotification(dict(request.form.lists()))
    
        # Do something with the message
        print("Bounce original: ", bounce_message.original)
        print("Bounce notification: ", bounce_message.notification)
    
        return "OK", 200
    
    

Learn more about the migration considerations for Mail API in the [Mail handlers](https://docs.cloud.google.com/appengine/docs/standard/python3/services/mail) guide.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
