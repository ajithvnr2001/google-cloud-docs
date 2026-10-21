---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/BounceNotification/
title: google.appengine.api.mail.BounceNotification \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:44.225744+00:00
---

# google.appengine.api.mail.BounceNotification  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/mail/BounceNotification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.mail.BounceNotification Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1840-L1955) Encapsulates a bounce notification received by the application. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.mail.BounceNotification(
        post_vars: typing.Mapping[str, typing.Any]
    )
    

| 

## Args  
  
---  
  
`post_vars` |  a dictionary with keys as strings. This should contain bounce information, and the following keys are handled: original-from original-to original-cc original-bcc original-subject original-text notification-from notification-to notification-cc notification-bcc notification-subject notification-text raw-message For all keys except 'raw-message', the value can be anything. The Bounce Notification object just assigns these values to the `original` and `notification` properties of this instance, which are dictionaries. For example, original["to"] = post_vars.get("original-to") The `raw-message` value is used to create an `InboundEmailMessage` object. This value should be a valid input to the `EmailMessage` constructor (inherited by 'InboundEmailMessage'). Flask- This is typically the `flask.request.form` field (if the user wants to pass single (non-list) values for each key), or 'dict(flask.request.form.lists())' if the user wants to store a list for each key (example use case is multiple `to` and `cc` recipients). Webob- `webob.Request.POST` can be used for single values, and `webob.Request.POST.dict_of_lists()` for multiple values. Django- `request.POST` can be used for single values, and `dict(request.POST.lists())` can be used for multiple values.   
  
## Attributes  
  
---  
  
`notification` |   
`original` |   
`original_raw_message` |   
  
## Methods

### `from_environ`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/mail.py#L1912-L1943)
    
    
    @classmethod
    from_environ(
        environ
    )
    

Transforms the HTTP request body to a bounce notification object.

Example(WSGI)::

def BounceReceiver(environ, start_response): bounce_msg = mail.BounceNotification.from_environ(environ)
    
    
    # Add logic for what to do with the bounce notification
    print('Bounce original: %s', bounce_msg.original)
    print('Bounce notification: %s', bounce_msg.notification)
    
    # Return suitable response
    response = http.HTTPStatus.OK
    start_response(f'{response.value} {response.phrase}', [])
    return ['success'.encode('utf-8')]
    

Args  
---  
  
`environ` |  a WSGI dict describing the HTTP request (See PEP 333).   
  
Returns  
---  
A BounceNotification object.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
