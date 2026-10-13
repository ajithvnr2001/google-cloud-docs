---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1/latest/Google-Apps-Events-Subscriptions-V1-NotificationEndpoint/
title: Google Workspace Events V1 API - Class Google::Apps::Events::Subscriptions::V1::NotificationEndpoint (v0.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:41.019030+00:00
---

# Google Workspace Events V1 API - Class Google::Apps::Events::Subscriptions::V1::NotificationEndpoint (v0.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1/latest/Google-Apps-Events-Subscriptions-V1-NotificationEndpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Workspace Events V1 API - Class Google::Apps::Events::Subscriptions::V1::NotificationEndpoint (v0.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.0 (latest)  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Google Workspace Events V1 API class Google::Apps::Events::Subscriptions::V1::NotificationEndpoint.

The endpoint where the subscription delivers events.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #pubsub_topic
    
    
    def pubsub_topic() -> ::String

**Returns**

  * (::String) — Immutable. The Cloud Pub/Sub topic that receives events for the subscription.

Format: `projects/{project}/topics/{topic}`

You must create the topic in the same Google Cloud project where you create this subscription.

When the topic receives events, the events are encoded as Cloud Pub/Sub messages. For details, see the [Google Cloud Pub/Sub Protocol Binding for CloudEvents](https://github.com/googleapis/google-cloudevents/blob/main/docs/spec/pubsub.md). 




### #pubsub_topic=
    
    
    def pubsub_topic=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. The Cloud Pub/Sub topic that receives events for the subscription.

Format: `projects/{project}/topics/{topic}`

You must create the topic in the same Google Cloud project where you create this subscription.

When the topic receives events, the events are encoded as Cloud Pub/Sub messages. For details, see the [Google Cloud Pub/Sub Protocol Binding for CloudEvents](https://github.com/googleapis/google-cloudevents/blob/main/docs/spec/pubsub.md). 




**Returns**

  * (::String) — Immutable. The Cloud Pub/Sub topic that receives events for the subscription.

Format: `projects/{project}/topics/{topic}`

You must create the topic in the same Google Cloud project where you create this subscription.

When the topic receives events, the events are encoded as Cloud Pub/Sub messages. For details, see the [Google Cloud Pub/Sub Protocol Binding for CloudEvents](https://github.com/googleapis/google-cloudevents/blob/main/docs/spec/pubsub.md). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
