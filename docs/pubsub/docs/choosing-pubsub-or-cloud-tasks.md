---
url: https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-cloud-tasks/
title: Choosing Pub/Sub or Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:47.309839+00:00
---

# Choosing Pub/Sub or Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-cloud-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Choosing Pub/Sub or Cloud Tasks Stay organized with collections  Save and categorize content based on your preferences. 

Both [Cloud Tasks](https://docs.cloud.google.com/tasks/docs/dual-overview) and [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) can be used to implement message passing and asynchronous integration. Although they are conceptually similar, each is designed for a different set of use cases. This page helps you choose the right product for your use case.

## Key Differences

The core difference between Pub/Sub and Cloud Tasks is in the notion of implicit vs. explicit invocation.

Pub/Sub aims to decouple publishers of events and subscribers to those events. Publishers do not need to know anything about their subscribers. Therefore, Pub/Sub gives publishers no control over the delivery of the messages save for the guarantee of delivery. In this way, Pub/Sub supports **implicit** invocation: a publisher implicitly causes the subscribers to execute by publishing an event.

By contrast, Cloud Tasks is aimed at **explicit** invocation where the publisher retains full control of execution. In particular, a publisher specifies an endpoint where each message is to be delivered.

Overall, Cloud Tasks is appropriate for use cases where a task producer needs to defer or control the execution timing of a specific webhook or remote procedure call. Pub/Sub is optimal for more general event data ingestion and distribution patterns where some degree of control over execution can be sacrificed.

## Detailed feature comparison

Feature | Cloud Tasks | Pub/Sub  
---|---|---  
Push using webhooks | Yes | Yes  
At-least-once delivery guarantee | Yes | Yes  
Configurable retries | Yes | Yes  
Task/message creation deduplication | Yes | No  
Scheduled delivery | Yes | No  
Ordered delivery | No, enqueued task order is preserved on a best‑effort basis | Yes, with ordering keys  
Explicit rate controls | Yes | Pull subscriber clients can implement [flow control](https://docs.cloud.google.com/pubsub/docs/flow-control-messages)  
Pull using API | No | Yes  
Batch insert | Yes | Yes  
Multiple handlers/subscribers per message | No | Yes  
Task/message retention | 31 days | Up to 31 days  
Maximum size of task/message | 1MB | 10MB  
Maximum delivery rate | 500 QPS/queue | No upper limit, subject to regional throughput quotas  
Geographic availability | Regional | Global  
Maximum push handler/subscriber processing duration | 30 minutes (HTTP)  
10 minutes (App Engine Standard automatic scaling)  
24 hours (App Engine Standard manual or basic scaling)  
60 minutes (App Engine Flexible) | 10 minutes for push operations  
Number of queues/subscriptions  | 1,000 per project per region, more available through quota increase request | 10,000 per project  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
