---
url: https://docs.cloud.google.com/workflows/docs/publish-pubsub-message/
title: Publish a message to a Pub/Sub topic \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:10.254663+00:00
---

# Publish a message to a Pub/Sub topic  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/publish-pubsub-message/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Publish a message to a Pub/Sub topic Stay organized with collections  Save and categorize content based on your preferences. 

You can use a [Workflows connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/pubsub/Overview) to support Pub/Sub operations, including publishing messages to a Pub/Sub topic.

A Pub/Sub topic is a resource to which messages are sent by publishers. A subscription represents the stream of messages from a topic that are to be delivered to the subscribing application. [Learn more about Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview).

## Publishing messages

Once a Pub/Sub topic and a subscription to that topic has been created, you can [create a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow) that publishes a message to that topic:

### YAML
    
    
    - init:
        assign:
          - project: '${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}'
          - topic: TOPIC_ID
          - subscription: SUBSCRIPTION_ID
          - message:
              hello: world
          - base64Msg: '${base64.encode(json.encode(message))}'
    - publish_message_to_topic:
        call: googleapis.pubsub.v1.projects.topics.publish
        args:
          topic: '${"projects/" + project + "/topics/" + topic}'
          body:
            messages:
              - data: '${base64Msg}'

### JSON
    
    
    [
    {
      "init": {
        "assign": [
          {
            "project": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}"
          },
          {
            "topic": "TOPIC_ID"
          },
          {
            "subscription": "SUBSCRIPTION_ID"
          },
          {
            "message": {
              "hello": "world"
            }
          },
          {
            "base64Msg": "${base64.encode(json.encode(message))}"
          }
        ]
      }
    },
    {
      "publish_message_to_topic": {
        "call": "googleapis.pubsub.v1.projects.topics.publish",
        "args": {
          "topic": "${\"projects/\" + project + \"/topics/\" + topic}",
          "body": {
            "messages": [
              {
                "data": "${base64Msg}"
              }
            ]
          }
        }
      }
    }
    ]

Replace the following:

  * `TOPIC_ID`: the ID or fully qualified identifier for the Pub/Sub topic.

  * `SUBSCRIPTION_ID`: the ID or fully qualified identifier for the Pub/Sub subscription.




## Pulling messages

You can create an Eventarc trigger that connects a Pub/Sub topic to a Workflows event receiver. A message is published to a Pub/Sub topic to generate an event, and the event is passed as a runtime argument to the destination workflow. For more information, see [Trigger a workflow with events or Pub/Sub messages](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc).

You can also create a workflow that pulls the Pub/Sub message. In the following example, the workflow waits for the message to be published using [polling](https://docs.cloud.google.com/workflows/docs/sleeping).

### YAML
    
    
    - pullMessage:
        call: googleapis.pubsub.v1.projects.subscriptions.pull
        args:
            subscription: '${"projects/" + project + "/subscriptions/" + subscription}'
            body:
                maxMessages: 1
        result: m
    - checkState:
        switch:
        - condition: ${m.receivedMessages[0].message.data != ""}
          next: outputMessage
    - wait:
        call: sys.sleep
        args:
            seconds: 60
        next: pullMessage
    - outputMessage:
        return: '${json.decode(base64.decode(m.receivedMessages[0].message.data))}'

### JSON
    
    
      [
        {
          "pullMessage": {
            "call": "googleapis.pubsub.v1.projects.subscriptions.pull",
            "args": {
              "subscription": "${\"projects/\" + project + \"/subscriptions/\" + subscription}",
              "body": {
                "maxMessages": 1
              }
            },
            "result": "m"
          }
        },
        {
          "checkState": {
            "switch": [
              {
                "condition": "${m.receivedMessages[0].message.data != \"\"}",
                "next": "outputMessage"
              }
            ]
          }
        },
        {
          "wait": {
            "call": "sys.sleep",
            "args": {
              "seconds": 60
            },
            "next": "pullMessage"
          }
        },
        {
          "outputMessage": {
            "return": "${json.decode(base64.decode(m.receivedMessages[0].message.data))}"
          }
        }
      ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
