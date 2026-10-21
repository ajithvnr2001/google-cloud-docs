---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/services/mail/
title: Mail API for Python \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:57:16.910055+00:00
---

# Mail API for Python  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/services/mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Mail API for Python Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To improve email security and ensure reliable, high-volume email delivery, we recommend that you [migrate from the legacy Mail API to an SMTP-based email service](https://docs.cloud.google.com/appengine/migration-center/standard/python/mail-to-smtp), such as SendGrid, Mailgun, or Mailjet.

This page describes how to use the Mail API, one of the legacy bundled services, with the [Python runtime](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime) for the standard environment. Your app can access the bundled services through the [**App Engine services SDK for Python**](https://github.com/GoogleCloudPlatform/appengine-python-standard).

## Overview

In Python, the mail handling functionality is included in the [`google.appengine.api.mail`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail) module. This is different from Python 2, where the `mail_handlers` module was provided by webapp. The Mail API for Python can be used to receive emails and bounce notifications.

## Using the Mail API

Your app receives mail when an email is sent as the request body in an HTTP POST request. For the app to handle incoming emails, the app needs to match the URL with the path `/_ah/mail/[ADDRESS]`. The `[ADDRESS]` part of the path is usually an email address with the suffix `@<Cloud-Project-ID>.appspotmail.com`. Emails sent to the app in this format will be routed to the function.

Python doesn't require the app to specify a handler script in the `app.yaml` file, so you can remove all `handler` sections in `app.yaml`.

Your `app.yaml` file should keep the following lines:
    
    
    inbound_services:
    - mail
    - mail_bounce
    

## Sending mail

You do not need to make changes to your app's configuration when upgrading to Python. The behavior, features, and setup instructions for sending mail remains the same. Refer to the [Mail API reference for Python](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail) for more details.

## Receiving mail

To receive mail, you need to import the `google.appengine.api.mail` module and use the [`InboundEmailMessage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/InboundEmailMessage) class to represent an email. This class needs to be instantiated to retrieve the email content from the incoming HTTP request.

Previously in Python 2, apps could access the `InboundEmailMessage` class by overriding the `receive()` method in the webapp handler `InboundEmailHandler`. This is not needed in Python; instead, the app needs to instantiate a new object.

### Web frameworks

When using Python web frameworks, the `InboundEmailMessage` constructor takes in the bytes of the HTTP request body. There are multiple ways to create the `InboundEmailMessage` object in Python. The following are examples for Flask and Djago apps:

### Python 3 (Flask)

In Flask, `request.get_data()` gives the request bytes.
    
    
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
    
    

### Python 3 (Django)

In Django, `request.body` gives the bytes of the HTTP request body.
    
    
    def receive_mail(request):
        message = mail.InboundEmailMessage(request.body)
    
        print(f"Received greeting for {message.to} at {message.date} from {message.sender}")
        for _, payload in message.bodies("text/plain"):
            print(f"Text/plain body: {payload.decode()}")
            break
    
        return HttpResponse("OK")
    
    

To view the complete code samples from this guide, see [GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/appengine/standard_python3/bundled-services).

### Other WSGI-compliant frameworks

For other WSGI-compliant frameworks, we recommend using the same method as the Flask and Django examples to create the `InboundEmailMessage`. This method works when the bytes of the HTTP request body are directly available.

### WSGI app without a web framework

If your app is a WSGI app that does not use a web framework, it is possible that the bytes of the HTTP request body is not directly available. If the bytes of the HTTP request body are directly available, we recommend that you use a Python web framework.

In Python, a factory method named `from_environ` is defined for `InboundEmailMessage`. This method is a class method that takes the [WSGI `environ` dictionary](https://www.python.org/dev/peps/pep-0333/#environ-variables) as the input, and can be used for any WSGI application.

In the following example, notice how `environ` is taken in as an input to get the `mail_message`:

### Python 3 (WSGI app)
    
    
    def HelloReceiver(environ, start_response):
        if environ["REQUEST_METHOD"] != "POST":
            return ("", http.HTTPStatus.METHOD_NOT_ALLOWED, [("Allow", "POST")])
    
        message = mail.InboundEmailMessage.from_environ(environ)
    
        print(f"Received greeting for {message.to} at {message.date} from {message.sender}")
        for content_type, payload in message.bodies("text/plain"):
            print(f"Text/plain body: {payload.decode()}")
            break
    
        response = http.HTTPStatus.OK
        start_response(f"{response.value} {response.phrase}", [])
        return ["success".encode("utf-8")]
    
    

## Receiving bounce notifications

A bounce notification is an automated message from an email system that indicates a problem with your app's message delivery. To process bounce notifications, your app needs to match incoming URL paths with the `/_ah/bounce` path.

Like `InboundEmailMessage`, the `BounceNotification` class for Python 2 was accessible by overriding the `receive()` method in the webapp handler `BounceNotificationHandler`.

In Python, the app needs to instantiate the `BounceNotification` object, which can be created in multiple ways depending on the Python web framework used.

### Web frameworks

The `BounceNotification` object is initialized with the values that are retrieved by calling `post_vars.get(key)`.

When using a Python web framework, like Flask or Django, the `BounceNotification` constructor takes in a dictionary named `post_vars`, which contains the POST request of the form data. To retrieve the data, the method `get()` needs to be defined on the input object. The `key` is a list of input values that can be read and retrieved by `BounceNotification` and can be any of the following:
    
    
    original-to, original-cc, original-bcc, original-subject, original-text, notification-from, notification-to, notification-cc, notification-bcc, notification-subject, notification-text, raw-message

In most web frameworks, this data is available as a multi dictionary in the request object. Most of these types can be converted into a dictionary keyed by strings.

For all keys except `raw-message`, the value can be anything. Usually, the value is either a single value such as a string, or a list of values, such as `{'to': ['bob@example.com', 'alice@example.com']}`. The default value for all fields is an empty string. These values will populate the `original` and `notification` properties.

For the `raw-message` key, the value needs to be a valid input to the constructor of [`EmailMessage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/EmailMessage). It can either be a single value or a single valued list. The `raw-message` key is used to initialize the `original_raw_message` property of the object.

### Python 2 (webapp2)
    
    
    class LogBounceHandler(BounceNotificationHandler):
        def receive(self, bounce_message):
            logging.info('Received bounce post ... [%s]', self.request)
            logging.info('Bounce original: %s', bounce_message.original)
            logging.info('Bounce notification: %s', bounce_message.notification)
    

### Python 3 (Flask)

In Flask, [`request.form`](https://werkzeug.palletsprojects.com/en/2.0.x/wrappers/?highlight=request#werkzeug.wrappers.Request.form) of type [`werkzeug.datastructures.MultiDict`](https://werkzeug.palletsprojects.com/en/2.0.x/datastructures/#werkzeug.datastructures.MultiDict) gives the POST variables. However, the `get()` method for this type only returns a value, even if there are multiple values for the key is present.

To get all values corresponding to a key, the app needs to call [`dict(request.form.lists())`](https://werkzeug.palletsprojects.com/en/2.0.x/datastructures/#werkzeug.datastructures.MultiDict.lists), which results in a dictionary where each value is a list.
    
    
    @app.route("/_ah/bounce", methods=["POST"])
    def receive_bounce():
        bounce_message = mail.BounceNotification(dict(request.form.lists()))
    
        # Do something with the message
        print("Bounce original: ", bounce_message.original)
        print("Bounce notification: ", bounce_message.notification)
    
        return "OK", 200
    
    

### Python 3 (Django)

In Django, [`request.POST`](https://docs.djangoproject.com/en/3.2/ref/request-response/#django.http.HttpRequest.POST) of type [`django.http.QueryDict`](https://docs.djangoproject.com/en/3.2/ref/request-response/#querydict-objects) gives the POST variables. However, the `get()` method for this type only returns a value, even if there are multiple values for the key is present.

To get all values corresponding to a key, the app needs to call [`dict(request.POST.lists())`](https://docs.djangoproject.com/en/3.2/ref/request-response/#django.http.QueryDict.lists), which results in a dictionary where each value is a list.
    
    
    def receive_bounce(request):
        bounce_message = mail.BounceNotification(dict(request.POST.lists()))
    
        # Do something with the message
        print(f"Bounce original: {bounce_message.original}")
        print(f"Bounce notification: {bounce_message.notification}")
    
        return HttpResponse("OK")
    
    

**Note:** To maintain similar behavior as Python 2, use `request.form` (in Flask) or `request.POST` (in Django) to initialize each key in `BounceNotification` to a single value even if there are multiple values present. To populate `BounceNotification` with multiple values for each key from a Bounce Notification, `dict(request.form.list())` for Flask or `dict(request.POST.list())` for Django can be passed in as an argument. The `to`, `cc`, and `bcc` fields will be initialized to strings or list of strings, depending on the input dict.

### WSGI app without a web framework

If your app is a WSGI app that does not use a web framework, it is possible that the form variables of the HTTP POST request are not directly available in a dictionary.

In Python, a factory method named `from_environ` is defined for `BounceNotification`. This method is a class method that takes the WSGI `environ` dictionary as the input, and can be used for any WSGI application.

In the following example, notice how `environ` is taken in as an input to get the `bounce_message`:

### Python 3
    
    
    def BounceReceiver(environ, start_response):
        if environ["REQUEST_METHOD"] != "POST":
            return ("", http.HTTPStatus.METHOD_NOT_ALLOWED, [("Allow", "POST")])
    
        bounce_message = mail.BounceNotification.from_environ(environ)
    
        # Do something with the message
        print("Bounce original: ", bounce_message.original)
        print("Bounce notification: ", bounce_message.notification)
    
        # Return suitable response
        response = http.HTTPStatus.OK
        start_response(f"{response.value} {response.phrase}", [])
        return ["success".encode("utf-8")]
    
    

## Code samples

To view the complete code samples from this guide, see [GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/appengine/standard_python3/bundled-services).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
