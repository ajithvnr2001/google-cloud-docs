---
url: https://docs.cloud.google.com/run/docs/triggering/webhooks/
title: Hosting webhooks targets \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:32.750771+00:00
---

# Hosting webhooks targets  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/webhooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Hosting webhooks targets Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows how to host a webhook target in a Cloud Run service.

Cloud Run provides good solutions for hosting your webhook targets. Cloud Run provides more flexibility and is able to handle larger volumes with concurrency.

Hosting webhook targets in a Cloud Run service is ideal for the following scenarios:

  * You want longer request timeouts (up to 60 minutes)
  * You're expecting large volume and need concurrency (up to 1,000 concurrent requests per instance)



## Create a webhook target in Cloud Run

Using Cloud Run, you can define a webhook target in any language you choose. You only need to create an HTTP endpoint that can accept the data. Typically this is done with a `POST`, for example:
    
    
    from flask import Flask, request
    app = Flask(__name__)
    
    @app.route('/', methods=['POST'])
    def index():
        data = request.get_json()
        return ('', 200)
    

In this example, the index page of the URL is configured to accept only `POST` requests and expects data to be delivered through a JSON payload.

## Integrate with the webhook provider

Most services that provide HTTP callbacks require you to verify URL ownership. This is usually done by sending some kind of token, message, or secret and expecting a valid response. You'll need to obtain these requirements from the service provider. Using the preceding example webhook target, this could look like:
    
    
    @app.route('/', methods=['POST'])
    def index():
        data = request.get_json()
        return data['challenge']
    

After the provider verifies your ownership, you'll need to add authorization on your end as well.

## Authorize requests

A webhook target is an open and public URL. Most services provide a token or a secret to ensure that the incoming requests are from authorized services. Because the URL is public, you cannot prevent malicious attempts to send data to the webhook target. However, using tokens or secrets ensures you only process data from authorized sources.

In order to verify the request, you can either [configure secrets](https://docs.cloud.google.com/run/docs/configuring/services/secrets), or store your copy of the secret either as an environment variable or using some kind of key management system.

When storing your copy of the secret as an environment variable, each request should have a secret or token in the request headers or the JSON payload, and you must check it to ensure the source is valid.
    
    
    import os
    from flask import request
    
    @app.route('/', methods=['POST'])
    def index():
        request_secret = request.headers.get('Secret')
        if request_secret != os.environ.get('SECRET'):
            return ('Unauthorized', 401)
        return ('', 200)
    

If the webhook provider does not support a secret or other authentication mechanism, anyone with the URL of your webhook target will be able to send messages. In this case, your webhook implementation should be safe to expose to the public internet.

**Note:** If you're creating webhooks to send data between multiple Cloud Run instances, use the [built in authentication](https://docs.cloud.google.com/run/docs/authenticating/service-to-service) to protect your HTTP Target. When prompted to allow [unauthenticated requests](https://docs.cloud.google.com/run/docs/authenticating/public), respond no.

## Responding to requests

Most services require you to respond to a request within a set amount of time, as specified by the service. Some webhooks have built-in retry methods if there is an error response, such as an HTTP status code of 4xx or 5xx, so you'll need to return a successful status code (2xx) to let the service know the event was processed properly.
    
    
    @app.route('/', methods=['POST'])
    def index():
        data = request.get_json()
        return ('', 200)
    

### Timeouts

Both Cloud Run and the webhooks provider have timeouts. The shorter of the two will apply to your application. If your data processing exceeds the time allotted by either Cloud Run or the webhooks provider, you'll need to use a product that lets you complete your processing asynchronously, such as [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) or [Cloud Tasks](https://docs.cloud.google.com/tasks/docs). These products let you quickly hand off the data, immediately return a success response to the webhooks provider, and continue the processing without the timeout concern. These are also good options for handling failures and retries.

## Common webhooks patterns

Type | Examples  
---|---  
Relaying Data | Sending a notification using Firebase Cloud Messaging whenever the webhook is called.  
Storing Data | Storing the data in BigQuery for later analysis.   
Triggering Actions | Fulfilling actions on Dialogflow, posting replies on Twitter, or pushing to your staging environment whenever new code is committed in GitHub.   
  
## What's next

  * Learn more about webhooks (HTTP Triggers) on [Cloud Run functions](https://docs.cloud.google.com/run/docs/function-triggers)
  * Set up webhooks notifications on [Google Cloud Observability](https://docs.cloud.google.com/monitoring/support/notification-options#webhooks)
  * Send Pub/Sub messages to a webhook using [push subscriptions](https://docs.cloud.google.com/pubsub/docs/push)
  * Fulfill actions on [Dialogflow](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview) with webhooks



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
