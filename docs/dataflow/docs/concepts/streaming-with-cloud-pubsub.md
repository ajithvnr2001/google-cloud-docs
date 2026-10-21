---
url: https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub/
title: Read from Pub/Sub to Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:32:04.031516+00:00
---

# Read from Pub/Sub to Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Read from Pub/Sub to Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for reading from Pub/Sub in Dataflow.

Apache Beam provides a reference implementation of the Pub/Sub I/O connector for use by non-Dataflow runners. However, the Dataflow runner uses its own custom implementation of the connector. This implementation takes advantage of Google Cloud-internal APIs and services to offer low-latency watermarks, high watermark accuracy, and efficient deduplication for exactly-once message processing. The connector is available for [Java](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.html), [Python](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsub.html), and [Go](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio).

## Exactly-once processing

Pub/Sub decouples event publishers from event consumers. The application publishes messages to a topic, and Pub/Sub asynchronously delivers the messages to subscribers.

Pub/Sub assigns a unique message ID to each message that is successfully published to a topic. By default, Pub/Sub performs _at-least-once_ message delivery. To achieve at-least-once semantics, if Pub/Sub doesn't receive acknowledgment from the subscriber within the acknowledgment deadline, it retries the message delivery. Retries might also occur before the acknowledgment deadline, or after a message has been acknowledged.

Dataflow acknowledges messages after they are successfully processed by the first fused stage and side effects of that processing have been written to persistent storage. To reduce the number of duplicate messages, Dataflow continually extends the acknowledgment deadline while a batch of messages is being processed in this stage.

Because Pub/Sub might re-deliver a message, it is possible for duplicate messages to arrive at the pipeline. If your Dataflow pipeline uses [exactly-once streaming mode](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once), then Dataflow deduplicates these messages to achieve exactly-once semantics.

If your pipeline can tolerate some duplicate records, then consider using [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes) instead. This mode can significantly lower latency and the total cost of your pipeline. The tradeoff is that duplicate messages might be processed twice. For more information, see [Choose which streaming mode to use](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes#choose-streaming-mode).

**Note:** Pub/Sub also supports exactly-once delivery. However, it's not recommended to use exactly-once delivery with Dataflow. For more information, see Pub/Sub exactly-once delivery.

### Deduplicate by message attribute

By default, Dataflow deduplicates based on message ID. However, an application might send the same record twice as two distinct Pub/Sub messages. For example, the original source data might contain duplicate records, or the application might incorrectly publish the same message twice. The latter can happen due to retries, if acknowledgment was dropped due to network issues or other interruptions. In these situations, the duplicate messages have different message IDs.

Depending on your scenario, your data might contain a unique field that can be used to deduplicate. For example, records might contain a unique transaction ID. You can configure the Pub/Sub I/O connector to deduplicate messages based on the value of a message attribute, instead of using the Pub/Sub message ID. As long as the publisher sets this attribute consistently during retries, then Dataflow can detect the duplicates. Messages must be published to Pub/Sub within 10 minutes of each other for deduplication.

For more information about using ID attributes, see the following SDK reference topics:

  * [`withIdAttribute`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.Read.html#withIdAttribute-java.lang.String-) (Java)
  * [`ReadFromPubSub`](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsub.html#apache_beam.io.gcp.pubsub.ReadFromPubSub) (Python)
  * [`ReadOptions`](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio#ReadOptions) (Go)



## Subscriptions

When you configure your pipeline, you specify either a Pub/Sub topic or a Pub/Sub subscription to read from. If you specify a subscription, don't use the same Pub/Sub subscription for multiple pipelines. If two pipelines read from a single subscription, each pipeline receives part of the data in a nondeterministic manner, which might cause duplicate messages, watermark lag, and inefficient autoscaling. Instead, create a separate subscription for each pipeline.

If you specify a topic, the connector creates a new temporary subscription. This subscription is unique per pipeline.

## Timestamps and watermarks

All Pub/Sub messages have a [timestamp](https://docs.cloud.google.com/pubsub/docs/publish-message-overview#about_messages), which represents the time when Pub/Sub receives the message. Your data might also have an _event_ timestamp, which is the time when the record was generated by the source.

You can configure the connector to read the event timestamp from an attribute on the Pub/Sub message. In that case, the connector uses the event timestamp for watermarking. Otherwise, by default it uses the Pub/Sub message timestamp.

For more information about using event timestamps, see the following SDK reference topics:

  * [`withTimestampAttribute`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.Read.html#withTimestampAttribute-java.lang.String-) (Java)
  * [`ReadFromPubSub`](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsub.html#apache_beam.io.gcp.pubsub.ReadFromPubSub) (Python)
  * [`ReadOptions`](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio#ReadOptions) (Go)



The Pub/Sub connector has access to Pub/Sub's private API that provides the age of the oldest unacknowledged message in a subscription. This API provides lower latency than is available in Cloud Monitoring. It enables Dataflow to advance pipeline watermarks and emit windowed computation results with low latencies.

If you configure the connector to use event timestamps, then Dataflow creates a second Pub/Sub subscription, called the _tracking subscription_. Dataflow uses the tracking subscription to inspect the event times of messages that are still in the backlog. This approach allows Dataflow to estimate the event-time backlog accurately. The [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) must have at least the following permissions on the project that contains the tracking subscription:

  * `pubsub.subscriptions.create`
  * `pubsub.subscriptions.consume`
  * `pubsub.subscriptions.delete`



In addition, it needs the `pubsub.topics.attachSubscription` permission on the Pub/Sub topic. It's recommended to create a [custom Identity and Access Management role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that contains just these permissions.

For more information about watermarks, see the StackOverflow page that covers [how Dataflow computes Pub/Sub watermarks](https://stackoverflow.com/questions/42169004/what-is-the-watermark-heuristic-for-pubsubio-running-on-gcd).

If a pipeline has multiple Pub/Sub sources, and one of them has very low volume or is idle, it delays the entire watermark from advancing, increasing overall pipeline latency. If there are timers or window aggregations in the pipeline based on the watermark, these are also delayed.

## Pub/Sub Seek

[Pub/Sub Seek](https://docs.cloud.google.com/pubsub/docs/replay-overview) lets users replay previously acknowledged messages. You can use Pub/Sub Seek with Dataflow to reprocess messages in a pipeline.

However, it's not recommended to use Pub/Sub Seek in a running pipeline. Seeking backwards in a running pipeline can lead to duplicate messages or messages being dropped. It also invalidates Dataflow's watermark logic and conflicts with the state of a pipeline that incorporates processed data.

To reprocess messages by using Pub/Sub Seek, the following workflow is recommended:

  1. Create a [snapshot](https://docs.cloud.google.com/pubsub/docs/replay-overview#snapshot_create) of the subscription.
  2. Create a new subscription for the Pub/Sub topic. The new subscription inherits the snapshot.
  3. Drain or cancel the current Dataflow job.
  4. Resubmit the pipeline using the new subscription.



For more information, see [Message reprocessing with Pub/Sub Snapshot and Seek](https://docs.cloud.google.com/dataflow/docs/guides/upgrade-guide#message-reprocessing).

## Pub/Sub source parallelism

The Pub/Sub source assigns each message a deterministic key for processing and uses those keys to shuffle the messages. For [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) jobs, 1024 keys are used for shuffling. For non-Streaming Engine jobs, the number of keys is the lowest power of 2 greater than `(4 * maximum workers)`.

To override the default number of shuffle keys, set the `num_pubsub_keys` [service option](https://docs.cloud.google.com/dataflow/docs/reference/service-options#num_pubsub_keys):

###  Java 
    
    
    --dataflowServiceOptions=num_pubsub_keys=NUMBER_OF_KEYS
    

###  Python 
    
    
    --dataflow_service_options=num_pubsub_keys=NUMBER_OF_KEYS
    

###  Go 
    
    
    --dataflow_service_options=num_pubsub_keys=NUMBER_OF_KEYS
    

Replace `NUMBER_OF_KEYS` with the number of keys. The next power of 2 greater than or equal to the specified value is used.

For example, you might set this option in the following situations:

  * Your pipeline has a [bottleneck](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks) that is caused by [insufficient parallelism in the Pub/Sub source](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks#pubsub-source-parallelism).

  * Your pipeline has out-of-memory errors due to excessive parallelism.




If you set this option, consider the tradeoffs described in [Parallelization and distribution](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#parallelization_and_distribution).

You can't change the number of keys as part of a [pipeline update](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline). To change the number of keys for an existing pipeline job, you must start a new job.

## Unsupported Pub/Sub features

The following Pub/Sub features aren't supported in the Dataflow runner's implementation of the Pub/Sub I/O connector.

### Exponential backoff

When you create a Pub/Sub subscription, you can configure it to use an exponential backoff retry policy. However, exponential backoff does not work with Dataflow. Instead, create the subscription with the **Retry immediately** retry policy.

Exponential backoff is triggered by a negative acknowledgment or when the acknowledgment deadline expires. However, Dataflow doesn't send negative acknowledgements when pipeline code fails. Instead, it retries message processing indefinitely, while continually extending the acknowledgment deadline for the message.

### Dead-letter topics

Don't use Pub/Sub dead-letter topics with Dataflow, for the following reasons:

  * Dataflow sends negative acknowledgments for various internal reasons (for example, if a worker is shutting down). As a result, messages might be delivered to the dead-letter topic even when no failures occur in the pipeline code.

  * Dataflow acknowledges messages after a bundle of messages is successfully processed by the first fused stage. If the pipeline has multiple fused stages and failures occur at any point after the first stage, the messages are already acknowledged and don't go to the dead-letter topic.




Instead, implement the dead-letter pattern explicitly in the pipeline, by routing failed messages to a destination for later processing. Some I/O sinks have built-in support for dead-letter queues. The following examples implement dead-letter patterns:

  * [E-commerce sample application](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/tree/master/retail/retail-java-applications#queuing-unprocessable-data-for-further-analysis)
  * [Pub/Sub to BigQuery template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-subscription-to-bigquery)



### Pub/Sub exactly-once delivery

Because Dataflow has its own mechanisms for exactly-once processing, it's not recommended to use [Pub/Sub exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery) with Dataflow. Enabling Pub/Sub exactly-once delivery reduces pipeline performance, because it limits the number of messages that are available for parallel processing.

### Pub/Sub message ordering

[Message ordering](https://docs.cloud.google.com/pubsub/docs/ordering) is a feature in Pub/Sub that lets a subscriber receive messages in the order they were published.

It's not recommended to use message ordering with Dataflow, for the following reasons:

  * The Pub/Sub I/O connector might not preserve message ordering.
  * Apache Beam doesn't define strict guidelines regarding the order in which elements are processed. Therefore, ordering might not be preserved in downstream transforms.
  * Using Pub/Sub message ordering with Dataflow can increase latency and decrease performance.



### Pub/Sub single message transforms

[Single message transforms](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview) (SMTs) let you manipulate, validate, and filter messages based on their attributes or data as they stream through the system. Subscriptions that feed into Dataflow shouldn't use SMTs that filter out messages as it can interfere with autoscaling. This happens because subscription SMT filtering can cause the backlog to appear larger than what is delivered to Dataflow until the filtered-out messages are actually processed by the SMT. Topic SMTs that filter messages won't cause issues with autoscaling. 

## What's next

  * [Stream Processing with Pub/Sub and Dataflow: Qwik Start](https://www.cloudskillsboost.google/focuses/18457?parent=catalog) (self-paced lab)
  * [Stream from Pub/Sub to BigQuery](https://docs.cloud.google.com/dataflow/docs/tutorials/dataflow-stream-to-bigquery)
  * [Stream messages from Pub/Sub by using Dataflow](https://docs.cloud.google.com/pubsub/docs/stream-messages-dataflow)
  * [Streaming pipelines](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines)
  * [Exactly-once in Dataflow](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once)
  * [Pub/Sub to BigQuery best practices](https://docs.cloud.google.com/dataflow/docs/guides/pubsub-bigquery-best-practices)
  * After Lambda: Exactly-once processing in Dataflow [Part 1](https://cloud.google.com/blog/products/gcp/after-lambda-exactly-once-processing-in-google-cloud-dataflow-part-1) and [Part 3: Sources and Sinks](https://cloud.google.com/blog/products/gcp/after-lambda-exactly-once-processing-in-cloud-dataflow-part-3-sources-and-sinks) (blog)
  * [Performance characteristics of Pub/Sub to BigQuery pipelines](https://docs.cloud.google.com/dataflow/docs/guides/pubsub-bigquery-performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
