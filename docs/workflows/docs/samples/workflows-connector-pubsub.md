---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-pubsub/
title: Connector for Pub/Sub \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:04.290576+00:00
---

# Connector for Pub/Sub  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Pub/Sub within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Pub/Sub API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/pubsub/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Pub/Sub connector:
    # Create a Pub/Sub topic and a subscription to that topic
    # Publish a message to the topic and pull the message from the subscription
    # Delete both the subscription and the topic
    # Expected output: "SUCCESS"
    - init:
        assign:
          - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - topic: "TOPIC_ID"  # replace TOPIC_ID placeholder
          - subscription: "SUBSCRIPTION_ID"  # replace SUBSCRIPTION_ID placeholder
          - message: {"hello": "world"}
          - base64Msg: ${base64.encode(json.encode(message))}  # encodes bytes to Base64 text
    - create_topic:
        call: googleapis.pubsub.v1.projects.topics.create
        args:
          name: ${"projects/" + project + "/topics/" + topic}
    - create_subscription_to_topic:
        call: googleapis.pubsub.v1.projects.subscriptions.create
        args:
          name: ${"projects/" + project + "/subscriptions/" + subscription}
          body:
            name: ${"projects/" + project + "/subscriptions/" + subscription}
            topic: ${"projects/" + project + "/topics/" + topic}
    - publish_message_to_topic:
        call: googleapis.pubsub.v1.projects.topics.publish
        args:
          topic: ${"projects/" + project + "/topics/" + topic}
          body:
            messages:
              - data: ${base64Msg}
    - pull_message:
        call: googleapis.pubsub.v1.projects.subscriptions.pull
        args:
          subscription: ${"projects/" + project + "/subscriptions/" + subscription}
          body:
            maxMessages: 1
        result: m
    - check_message:
        switch:
          - condition: ${m.receivedMessages[0].message.data != base64Msg}
            next: failed
    - delete_subscription:
        call: googleapis.pubsub.v1.projects.subscriptions.delete
        args:
          subscription: ${"projects/" + project + "/subscriptions/" + subscription}
    - delete_topic:
        call: googleapis.pubsub.v1.projects.topics.delete
        args:
          topic: ${"projects/" + project + "/topics/" + topic}
    - the_end:
        return: "SUCCESS"
    - failed:
        raise: ${"Received data:" + m.receivedMessages[0].message.data + " Expected data:" + base64Msg}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
