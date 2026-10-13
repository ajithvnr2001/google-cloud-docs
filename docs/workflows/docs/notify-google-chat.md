---
url: https://docs.cloud.google.com/workflows/docs/notify-google-chat/
title: Send notifications to Google Chat from your workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:18.608483+00:00
---

# Send notifications to Google Chat from your workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/notify-google-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Send notifications to Google Chat from your workflow Stay organized with collections  Save and categorize content based on your preferences. 

You can create a workflow that sends messages to a Google Chat _incoming webhook_. Incoming webhooks let you send asynchronous messages into Google Chat from applications that aren't Chat apps. For example, you can configure a monitoring application to notify on-call personnel on Google Chat when a server goes down.

## Create and register a Google Chat incoming webhook

In the Google Chat space where you want to receive messages, create a webhook. Follow the instructions to [register the incoming webhook](https://developers.google.com/chat/how-tos/webhooks#step_1_register_the_incoming_webhook).

## Make an HTTP call to the webhook URL

[Create a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow) and add a step to the workflow that makes an `HTTP POST` call to the webhook URL. For example:

### YAML
    
    
      - get_message:
          call: http.post
          args:
            url: WEBHOOK_URL
            body:
              text: "Hello world!"
            headers:
              Content-Type: "application/json; charset=UTF-8"
          result: response
      - return_value:
          return: ${response}

### JSON
    
    
      [
        {
          "get_message": {
            "call": "http.post",
            "args": {
              "url": "WEBHOOK_URL",
              "body": {
                "text": "Hello world!"
              },
              "headers": {
                "Content-Type": "application/json; charset=UTF-8"
              }
            },
            "result": "response"
          }
        },
        {
          "return_value": {
            "return": "${response}"
          }
        }
      ]

Replace `WEBHOOK_URL` with the webhook URL that you copied when registering the incoming webhook.

You can confirm that the workflow works as expected by ensuring that a notification is sent to your Google Chat space.

## What's next

  * [Learn more about making HTTP requests](https://docs.cloud.google.com/workflows/docs/http-requests)
  * [Learn more about Workflows](https://docs.cloud.google.com/workflows/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
