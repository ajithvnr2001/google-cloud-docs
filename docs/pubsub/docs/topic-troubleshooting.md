---
url: https://docs.cloud.google.com/pubsub/docs/topic-troubleshooting/
title: Troubleshooting a standard topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:56.117900+00:00
---

# Troubleshooting a standard topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/topic-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshooting a standard topic Stay organized with collections  Save and categorize content based on your preferences. 

This document provides some common troubleshooting tips when publishing messages to a standard Pub/Sub topic.

Learn more about how to [Publish messages to topics](https://docs.cloud.google.com/pubsub/docs/publisher) and the different features.

## High publish latency

Publish latency is the amount of time it takes to complete a publish request that is issued by a publisher client. Publish latency is distinct from [end-to-end delivery latency](https://docs.cloud.google.com/pubsub/docs/monitoring#delivery_latency_health), which is the amount of time it takes for a message that is published to Pub/Sub to be delivered to a subscriber client. You might observe high publish latency or end-to-end latency, even when the value of the other latency type is low. High publish latency can be incurred at the Pub/Sub publisher client, in transit between the client and the Pub/Sub backend, or in the Pub/Sub backend. You can inspect the publish latency incurred in the Pub/Sub backend using the [`topic/send_request_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub) metric. High backend publish latency could be related to the following factors:

  * Pub/Sub is designed for low-latency, high-throughput delivery. If the topic has low throughput, the resources associated with the topic could take longer to initialize.

  * If you are using a message storage policy, it could affect the overall latency of the requests to the topic and subscription. Check the [Performance and availability implications](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction#performance_and_availability_implications) of using this configuration.




If your publisher client is observing publish latency significantly higher than what is reflected in the metric, it could be a sign of one of these client-side factors:

  * Ensure you are not creating a new publisher for every publish. It is recommended to use a single publisher client per topic per application to publish all messages. Spinning up new publisher objects and adding new threads has a latency cost. If you are using Cloud Run functions to publish messages, note that invocations can also affect publish latency.

  * If you find that the default retry settings are not sufficient for your use case, make the corresponding adjustments. However, verify that the new values are not too high. See how to configure the [Retry requests](https://docs.cloud.google.com/pubsub/docs/retry-requests).




Note that high publish latency can lead to `DEADLINE_EXCEEDED` errors, which are discussed in the next section.

## Publish operations fail with DEADLINE_EXCEEDED

A `DEADLINE_EXCEEDED` error during a publish request indicates that the request failed to complete within the time allocated. This could be due to various factors, such as the requests not reaching the Pub/Sub service or performance issues affecting the requests.

To verify that publish requests are reaching the Pub/Sub service, monitor the topic using the [`topic/send_request_count`](https://docs.cloud.google.com/pubsub/docs/monitoring#keeping_publishers_healthy) metric, grouped by `response_code`. This metric helps you determine if requests fail before reaching the Pub/Sub topic. If the metric is empty, there is an external factor preventing the messages from reaching the Pub/Sub service. Additionally, to rule out the possibility of an intermittent issue, check the error rate using the `topic/send_request_count` metric graph mentioned earlier, or the [APIs & Services](https://console.cloud.google.com/apis/api/pubsub.googleapis.com/metrics) page in the Google Cloud console. If the error rate is very low, this could be an intermittent issue.

If requests are reaching Pub/Sub, these are some possible causes of publish operations failing with a `DEADLINE_EXCEEDED` error:

### Client-side bottleneck

Publish failures are likely caused by a client-side bottleneck, such as insufficient memory, CPU pressure, bad thread health, or network congestion in the VM hosting the publisher client. If a `Publish` call returns `DEADLINE_EXCEEDED`, it could be that asynchronous `Publish` calls are being enqueued faster than they are sent to the service, which progressively increases the request latency. Additionally, check if any of the following help to determine a possible bottleneck in your system:

  * Check whether you are publishing messages faster than the client can send them. Usually each asynchronous `Publish` call returns a [`Future`](https://en.wikipedia.org/wiki/Futures_and_promises) object. To track the number of messages waiting to be sent, store the number of messages to be sent with each `Publish` call and delete it only in the callback of the `Future` object.

  * Ensure that you have sufficient upload bandwidth between the machine where the publisher is running and Google Cloud. Development Wi-Fi networks typically have bandwidth of 1-10 MBps, or 1000-10000 typical messages per second. Publishing messages in a loop without any rate limiting could create a short burst of high bandwidth over a short time period. To avoid this, you can run the publisher on a machine within Google Cloud or reduce the rate at which you publish the messages to match your available bandwidth.

  * Check whether you see very high latency between your host and Google Cloud for any reasons like startup network congestion or firewalls. [Calculating network throughput](https://github.com/GoogleCloudPlatform/community/blob/master/archived/network-throughput.md) has pointers on finding out your bandwidth and latency for different scenarios.

  * Ultimately, there are limits to how much data a single machine can publish. You may need to try to scale horizontally or run multiple instances of the publisher client on several machines. [Testing Cloud Pub/Sub clients to maximize streaming performance](https://cloud.google.com/blog/products/data-analytics/testing-cloud-pubsub-clients-to-maximize-streaming-performance) demonstrates how Pub/Sub scales on a single Google Cloud VM with increasing number of CPUs. For example, you can achieve 500 MBps to 700 MBps for 1KB messages on a 16 core Compute Engine instance.




### Inadequate publish timeout duration

To reduce the timeout rate for publish calls, ensure you have a long enough timeout defined in the publisher client's retry settings. For the retry settings, set the initial deadline to 10 seconds and the total timeout to 600 seconds. Even if you are not accumulating a large backlog of unsent messages, occasional spikes in request latency can cause publish calls to timeout. However, if your issues are caused by a persistent bottleneck, rather than occasional timeouts, retrying more times could lead to more errors.

### Client library issues

You could be running a version of the client library with a known issue. The following list includes the issue trackers for all client libraries. If you find a known issue affecting the client library version that you are using, upgrade to the latest version of the client library. This ensures that you have picked up any relevant updates, including fixes and performance improvements.

### C++

[Client library issue tracker](https://github.com/googleapis/google-cloud-cpp)

### C#

[Client library issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-dotnet)

### Go

[Client library issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-go)

### Java

[Client library issue tracker](https://github.com/googleapis/google-cloud-java)

### Node.js

[Client library issue tracker](https://github.com/googleapis/nodejs-pubsub/issues)

### PHP

[Client library issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-php)

### Python

[Client library issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-python)

### Ruby

[Client library issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-ruby)

## Schema issues

If your publishes start to return `INVALID_ARGUMENT`, it is possible that someone has [updated the topic to change the associated schema](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic#edit-schema-association), [deleted the schema](https://docs.cloud.google.com/pubsub/docs/delete-schema), or [deleted the schema revisions associated with the topic](https://docs.cloud.google.com/pubsub/docs/delete-schema-revision). In this case, update the topic's schema settings to a schema and set of revisions that match the messages being published, or adjust the message format to match the current schema.

## Message encryption issues

If you have configured your Pub/Sub topic to encrypt published messages using a customer-managed encryption key, publishing could fail with a `FAILED_PRECONDITION` error. This error might occur if the Cloud KMS key is disabled or if externally managed keys through Cloud EKM are no longer accessible. To resume publishing, [restore access to the key](https://docs.cloud.google.com/pubsub/docs/encryption#disabling_and_re-enabling_keys).

## Message storage policy issues

If your subscriptions don't receive published messages, the topic might have a [message storage policy](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) in effect. If so, you might see `FAILED_PRECONDITION` errors in your publish metrics.

These errors typically contain messages such as:
    
    
    Cannot publish messages that contain ordering keys
    to topic projects/...  due a message storage policy on the topic that would
    require the messages to be forwarded to another region. Please either change
    the topic's message storage policy or publish to an allowed region using
    the appropriate regional Cloud Pub/Sub endpoint.
    

or
    
    
    The topic's message storage policy requires enforcement
    in transit, but the Publish request was received by a Pub/Sub server in
    a non-allowed region. Please either publish via a regional Pub/Sub endpoint
    corresponding to an allowed region, or update the topic's message storage policy.
    

To resolve this issue, do one of the following:

  * Update the topic's message storage policy to allow the region.
  * Configure your publisher client to publish to an allowed region using the appropriate [regional Pub/Sub endpoint](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#list_regional_endpoints).



## Single Message Transform (SMT) issues

If you have configured [SMTs](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview) on your Pub/Sub topic, publishing might fail with `INVALID_ARGUMENT` errors when transformations fail to be applied to messages. If any message in a publish batch fails transformation, the entire batch fails to be published. The error returned indicates the failure reason, for example:
    
    
    INVALID_ARGUMENT: Pub/Sub failed to apply a message transformation to one or
    more messages in the publish request. Error: Failed to execute JavaScript UDF:
    `my_function`. Return value is not an object.
    

### Monitor SMTs

To understand the performance and impact of SMTs on a topic, use the following monitoring metrics:

The [topic/message_transform_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/message_transform_latencies) metric measures how long it takes for SMTs to be applied to a message. The metric measures only the SMT latency and does not include other parts of the message delivery time.

The metric provides two key labels:

  * `status`: reports whether the transformation is successful or encountered an issue.

  * `filtered`: indicates if the SMT caused the message to be filtered out. When an SMT filters a message on a topic, Pub/Sub drops the message, and the message is never sent to subscribers. This `filtered` label is true only when an SMT performs the filtering. Messages filtered using Pub/Sub's [built-in filtering capabilities](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter) are not reflected in this specific metric.




The [topic/byte_cost](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/byte_cost) metric is used to identify messages that are filtered by SMTs or where SMTs failed. Look for these specific values:

  * When an SMT filters a message, the operation_type is `smt_publish_filter_drop`.

  * If an SMT fails to transform a message, you see a `response_code` that is not `OK`.




## What's next

Explore [OpenTelemetry tracing](https://docs.cloud.google.com/pubsub/docs/open-telemetry-tracing) to help you debug your publish latency.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
