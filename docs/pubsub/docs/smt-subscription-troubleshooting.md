---
url: https://docs.cloud.google.com/pubsub/docs/smt-subscription-troubleshooting/
title: Troubleshooting a subscription with Single Message Transforms (SMTs) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:52.350238+00:00
---

# Troubleshooting a subscription with Single Message Transforms (SMTs)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/smt-subscription-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshooting a subscription with Single Message Transforms (SMTs) Stay organized with collections  Save and categorize content based on your preferences. 

This page provides some common troubleshooting tips for [subscriptions with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt).

## Monitor SMTs

To understand the performance and impact of SMTs on a subscription, use the following monitoring metrics:

The [subscription/message_transform_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/message_transform_latencies) metric measures how long it takes for SMTs to be applied to a message. The metric measures only the SMT latency and does not include other parts of the message delivery time.

The metric provides two key labels:

  * `status`: reports whether the transformation is successful or encountered an issue.

  * `filtered`: indicates if the SMT caused the message to be filtered out. When an SMT filters a message on a subscription, Pub/Sub acknowledges it, and the message is never sent to subscribers. This `filtered` label is true only when an SMT performs the filtering. Messages filtered using Pub/Sub's [built-in filtering capabilities](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter) are not reflected in this specific metric.




The [subscription/byte_cost](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/byte_cost) metric is used to identify messages that are filtered by SMTs or where SMTs failed. Look for these specific values:

  * When an SMT filters a message, the operation_type is `smt_subscribe_filter_drop`.

  * If an SMT fails to transform a message, you see a `response_code` that is not `OK`.




## A backlog is building up

If you see a backlog of messages building up in the subscription, check for `INVALID_ARGUMENT` errors reported in [`subscription/message_transform_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/message_transform_latencies).

To troubleshoot `INVALID_ARGUMENT` errors, add a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) to the subscription of interest. The dead letter topic captures messages that couldn't be delivered to subscribers, along with an attribute called `CloudPubSubDeadLetterSourceSMTErrorMessage` that explains the failure reason.

## What's next

  * If you still have issues with your subscription SMTs, see [Getting support](https://docs.cloud.google.com/pubsub/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
