---
url: https://docs.cloud.google.com/tasks/docs/comp-pub-sub/
title: Choose Cloud Tasks or Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:23.530856+00:00
---

# Choose Cloud Tasks or Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/comp-pub-sub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Choose Cloud Tasks or Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

Both [Cloud Tasks](https://docs.cloud.google.com/tasks/docs/dual-overview) and [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) can be used to implement message passing and asynchronous integration, but while they function in similar ways, they are not identical. This guide helps you choose the right product for your use case.

## Key differences

Pub/Sub and Cloud Tasks differ primarily in whether they use _implicit_ or _explicit_ invocation.

Pub/Sub decouples event publishers from their subscribers. Publishers don't need to know anything about their subscribers. As a result, Pub/Sub offers no control over message delivery beyond guaranteeing it. This supports **implicit** invocation: a publisher triggers subscriber execution just by publishing an event.

In contrast, Cloud Tasks aims for **explicit** invocation. The publisher retains full control of execution. In particular, a publisher specifies an endpoint where each message is to be delivered.

In addition, Cloud Tasks provides tools for queue and task management unavailable to Pub/Sub publishers, including:

  * Specific delivery scheduling
  * Delivery rate controls
  * Precise configurable retries
  * Access and management of individual tasks in a queue
  * Task creation deduplication



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
  
## Configurable retry differences

Cloud Tasks offers precise control of task retries, including firm limits on attempts and duration. Pub/Sub focuses on reliable delivery, using exponential backoff and dead-letter queues (DLQ) to manage retries for unacknowledged messages.

Feature| Cloud Tasks | Pub/Sub  
---|---|---  
Use case focus| Ensuring eventual execution of a specific task | Ensuring message delivery to decoupled subscribers  
Primary control| Queue-level and task-level retry configuration | Subscription-level retry policy and DLQ  
Stopping retries| Maximum attempts, maximum retry duration | Message acknowledgment, message expiration, or DLQ transfer  
Maximum attempts| Explicitly configurable | Indirectly through DLQ maximum delivery attempts  
Backoff tuning| Minimum/maximum backoff, maximum doublings | Minimum/maximum backoff for exponential backoff policy  
Indefinite retries| Possible if configured, but bounded by maximum task retention limit | Default for unacknowledged messages until expiration, mitigated by DLQ  
  
## What's next

  * [Configure queue routing, limits, and retries](https://docs.cloud.google.com/tasks/docs/configuring-queues)
  * [Manage queues and tasks](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks)
  * [Set retry parameters for a task](https://docs.cloud.google.com/tasks/docs/configure-retry-task)
  * [Task deduplication](https://docs.cloud.google.com/tasks/docs/dual-overview#task_deduplication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
