---
url: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks/
title: Troubleshoot bottlenecks in Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:10.537229+00:00
---

# Troubleshoot bottlenecks in Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Troubleshoot bottlenecks in Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

A _bottleneck_ occurs when one step, stage, or worker slows down the overall job. Bottlenecks can lead to idle workers and increased latency.

If Dataflow detects a bottleneck, the job graph shows an alert, and the [**Step Info** panel](https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel) lists the kind of bottleneck and the cause, if known. Dataflow also exports bottleneck detection information to a Monitoring metric, which presents the data as a timeseries. This lets you view bottlenecks over time or in the past.

## Understand bottlenecks

When Dataflow runs a streaming pipeline, the job consists of a series of components, such as [streaming shuffles](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once#streaming-shuffle), user-defined function (`DoFn`) processing threads, and persistent state checkpointing. To facilitate the flow of data, Dataflow uses queues to connect these components. Data is pushed from upstream to downstream.

In many pipelines, the overall throughput capacity is constrained by a single component, creating a _bottleneck_ in the pipeline. The rate at which data can move through a bottleneck limits how quickly the pipeline can accept and process input data.

For example, consider a pipeline where `DoFn` processing occurs downstream of a streaming shuffle. A queue between them buffers the shuffled but unprocessed data. If the `DoFn` processing can't consume data as quickly as the streaming shuffle produces it, then the queue grows. A prolonged bottleneck can cause the queue to reach its capacity. At that point, further shuffling is paused, and the backlog propagates upstream. Queues further upstream also accumulate backlogs, eventually causing a slowdown that extends to the data source, meaning the whole pipeline can't keep pace with the input.

When a bottleneck happens, a substantial portion of the pipeline might appear to be unhealthy, even though a single point in the pipeline is causing the backlog. This behavior can make it hard to debug bottlenecks. The goal of bottleneck detection is to identify the precise location and cause, eliminating guesswork, so that you can fix the root cause.

Dataflow detects a bottleneck when a delay exceeds the threshold of five minutes. If the delay doesn't cross this threshold, Dataflow doesn't detect a bottleneck.

Bottleneck detection doesn't always require you to act and depends on your use case. A pipeline can operate normally with transient delays of more than five minutes. If this is acceptable for your use case, you might not need to resolve the indicated bottlenecks.

## Kinds of bottleneck

When Dataflow detects a bottleneck, the monitoring interface indicates the severity of the problem. Bottlenecks fall into the following categories:

Processing is stuck and not making progress
    The progress of the pipeline is completely halted at this step.
Processing is ongoing but falling behind.
    The pipeline can't process incoming data as quickly as it arrives. The backlog is growing as a result.
Processing is ongoing but the backlog is steady
    The pipeline is making progress, and the processing rate is comparable to the input rate. Processing is fast enough that the backlog is not growing, but the accumulated backlog is also not significantly decreasing.
Processing is ongoing and catching up from a backlog
    The backlog is decreasing, but the current bottleneck prevents the pipeline from catching up any faster. If you start a pipeline with a backlog, this state might be normal and not require any intervention. Monitor progress to see if the backlog continues to decrease.

## Causes of bottlenecks

This section lists the causes of bottlenecks that can be detected. Use this information to resolve the issue. In some cases, multiple causes might be present, and they might be related. For example, if workers are underprovisioned, vCPU utilization might be high. High vCPU utilization can cause operations to slow down, which in turn can create an elevated queue delay. The likely-cause analysis might display all of these as the causes of the bottleneck.

Long processing time operations
    

Some operations in this computation have a long processing time. This occurs whenever an input bundle is sent to the worker executing the `DoFn` and significant time has elapsed without results being available.

This is most often the result of a single long-running operation in user code. Other issues can manifest as long processing time operations. For example, errors thrown and retried inside the `DoFn`, retries for long periods of time, or crashes of the worker harness due to factors such as OOMs can all cause these long processing times.

If the affected computation is in user code, look for ways to optimize the code or bound the execution time. To help with debugging, the worker logs show stack traces for any operations that are stuck for longer than 5 minutes.

Key commit too large
    

See [Key commit too large exception](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#key-commit-too-large-exception).

BigQuery sink permission denied
    

This error indicates that the service account running the pipeline doesn't have the necessary permissions to write to the BigQuery resource.

To validate this issue using worker logs:

  1. In the Google Cloud console, open the Dataflow **Job details** page.
  2. In the bottom panel, click the **Logs** tab and select **Worker Logs**.
  3. Look for error messages that suggest permissions or access are denied (for example, `PERMISSION_DENIED`, `403 Forbidden`, `Access Denied`, or `actuallyForbidden`).
  4. Inspect the log message to identify the destination dataset or table and the specific missing permission (such as `bigquery.tables.updateData`).



To resolve this issue:

  * Confirm that the service account has been granted the **BigQuery Data Editor** (`roles/bigquery.dataEditor`) role on the destination dataset and table.
  * If writing cross-project, ensure that permissions are granted to the service account directly in the destination project that hosts the BigQuery dataset, and that VPC Service Controls (if enabled) permits communication between both projects.



If these steps don't resolve the issue, see [BigQuery predefined roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control) to identify and grant any missing granular permissions required for your specific configuration.

BigQuery sink resource exhausted
    

This error indicates that the pipeline has exceeded a BigQuery quota limit. The most likely cause is insufficient quota in the destination BigQuery project to handle the volume of data being written.

To validate this issue using worker logs:

  1. In the Google Cloud console, open the Dataflow **Job details** page.
  2. In the bottom panel, click the **Logs** tab and select **Worker Logs**.
  3. Look for error messages that suggest resources or quotas are exhausted or rate limits are exceeded (for example, `RESOURCE_EXHAUSTED`, `429 Too Many Requests`, `quotaExceeded`, or `rateLimitExceeded`).
  4. Inspect the log message to confirm which operation and quota limit was exceeded (for example, Storage Write API `AppendRows` throughput or connection limits, or streaming insert rate limits).



To resolve this issue:

  * Determine which BigQuery sink implementation your pipeline is using (for example, the [Storage Write API](https://docs.cloud.google.com/bigquery/quotas#write-api-limits) or [streaming inserts](https://docs.cloud.google.com/bigquery/quotas#streaming_inserts)).
  * Review your BigQuery quota usage in the Google Cloud console. Look specifically for quotas related to your sink type, such as concurrent connections, throughput, or streaming insert rows per second.
  * If you consistently approach or exceed these limits, consider [requesting a quota increase](https://docs.cloud.google.com/bigquery/quotas#requesting_a_quota_increase).



If these steps don't identify the specific limit being exceeded, see [Troubleshoot quota and limit errors](https://docs.cloud.google.com/bigquery/docs/troubleshoot-quotas) to investigate further.

BigQuery sink RPC failure
    

This error indicates that RPC requests from the pipeline to BigQuery are failing. Potential causes include transient network or service issues, invalid request payloads, schema mismatches, or timeout and deadline exceeded errors.

To validate this issue using worker logs:

  1. In the Google Cloud console, open the Dataflow **Job details** page.
  2. In the bottom panel, click the **Logs** tab and select **Worker Logs**.
  3. Look for error messages or exceptions related to BigQuery write operations (for example, `DEADLINE_EXCEEDED`, `UNAVAILABLE`, `INVALID_ARGUMENT`, or schema validation errors).
  4. Inspect the stack trace and error message to determine the specific failure mode returned by the BigQuery API.



To resolve this issue:

  * Once you identify the specific error message or status code in the worker logs, consult the [BigQuery error messages reference](https://docs.cloud.google.com/bigquery/docs/error-messages) for troubleshooting guidance specific to that error.
  * If your pipeline uses the Storage Write API, see [Error handling](https://docs.cloud.google.com/bigquery/docs/write-api-grpc#error-handling) in the BigQuery Storage Write API documentation for information on handling specific write and stream errors.


Long processing time across all operations
    

Operations in this computation are consistently taking a long time, suggesting an issue within the user-provided `DoFn`.

This cause is different from Long processing time operations; whereas that cause affects some operations, this cause indicates that all operations in this computation are affected.

Check worker logs for errors, exceptions, or stack traces indicating slow or stuck threads. If you're using the Apache Beam SDK for Python, and if the operations are inherently long-running by design (for example, slow external API calls or high-latency I/O), consider using an [Async DoFn](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.async_dofn.html#module-apache_beam.transforms.async_dofn). This feature can improve throughput by preventing processing from being blocked on these long-running tasks.

Slow persistent state read
    

The computation is spending a significant amount of time reading persistent state as part of executing the `DoFn`. This may be the result of excessively large persistent state, or too many reads. Consider reducing the persisted state size or frequency of reads. Optimize state access patterns by combining multiple state read operations or using map state instead of value state where appropriate. This may also be a transient issue due to slowness of the underlying persistent state.

Slow persistent state write
    

The computation is spending a significant amount of time writing persistent state during the commit of the results of processing. This may be the result of excessively large persistent state. Consider reducing the persisted state size. Optimize state access patterns by combining multiple state write operations where appropriate. This may also be a transient issue due to slowness of the underlying persistent state.

Rejected commit
    

Data processing cannot be committed to persistent state due to being invalid. This is usually due to exceeding one of the operational [limits](https://docs.cloud.google.com/dataflow/quotas#limits). Check the logs for more details, or [contact support](https://docs.cloud.google.com/dataflow/docs/support/getting-support).

Insufficient Apache Kafka source partitions
    

The Apache Kafka source computation has insufficient partitions. To resolve this problem, try the following:

  * Increase the number of Kafka partitions.
  * Include redistribute using `.withRedistribute()` when configuring Kafka IO read to parallelize the data more efficiently. Include `.withRedistributeNumKeys(N)` where `N > partitions` to provide an upper bound on the total number of keys. Having a limited number of keys provides efficiency through bundling of records.
  * To minimize the cost of the redistribute shuffle, use `.withOffsetDeduplication()`. This mode minimizes the amount of data that needs to be persisted as part of the shuffle, while still providing exactly-once processing.



For more information, see [Parallelism](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka#parallelism) in the page [Read from Apache Kafka to Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka).

Apache Kafka Source Large Volume of Persisted State
    

The Apache Kafka source computation is redistributing a high volume of data that might incur high latency and cost. To resolve this problem, try the following:

  * If exactly-once processing is required for the pipeline, minimize the cost of the redistribute shuffle by utilizing [offset deduplication mode](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withOffsetDeduplication\(java.lang.Boolean\)). This mode minimizes the amount of data that needs to be persisted as part of the shuffle, while still providing exactly-once processing.
  * If at-least-once processing is sufficient for the pipeline, then the [allow duplicates](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withAllowDuplicates\(java.lang.Boolean\)) configuration can be enabled.



For more information, see [Read from Apache Kafka to Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka#parallelism).

Insufficient source parallelism
    

A source computation has insufficient parallelism. If possible, increase the parallelization within the source. If you can't increase parallelization and the job uses [at-least-once mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes), try adding a `Redistribute` transform to the pipeline.

**Note:** For the Apache Beam `KafkaIO` and `PubSubIO` sources, Dataflow shows a more specific warning.
Hot keys or insufficient key parallelism
    

The job has hot keys or insufficient key parallelism.

For each sharding key, Dataflow processes messages serially. While Dataflow is processing a batch of messages for a given key, other incoming messages for that key are queued until the current batch is completed.

If Dataflow can't process enough distinct keys in parallel, it can cause a bottleneck. For example, the data might have too few distinct keys, or certain keys might be overrepresented in the data ("hot keys"). To resolve this, modify your pipeline logic to redistribute data. For example, add a random suffix to the grouping keys to break up hot keys, and aggregate results in a subsequent step. For more details, see [Troubleshoot hot keys](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs#hot-keys).

Underprovisioned vCPUs
    

The job doesn't have enough worker vCPUs. This situation occurs when the job is already scaled to maximum, vCPU utilization is high, and there is still a backlog. You may have to increase the maximum number of workers provisioned for this job. For example, you could increase this number by an [update to the autoscaling range](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling#update-range). Alternatively, look for ways in which vCPU usage can be decreased by changes to pipeline code or workload. You can use the [cloud profiler](https://docs.cloud.google.com/dataflow/docs/guides/profiling-a-pipeline) to look for optimization opportunities.

High vCPU utilization, waiting for upscale
    

The job has a high vCPU utilization, but there is room to upscale. This condition is likely to be transient until upscaling can occur. You can [monitor autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/autoscaling-metrics) to see the autoscaling decisions. If this condition persists for a long time or occurs frequently, you might need to change the autoscaling configuration by setting a different [worker utilization hint](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling#utilization-hint) to allow the job to upscale more proactively.

Unbalanced vCPU load creating bottlenecks on some outlier workers
    

The job has enough worker vCPUs but some workers show very high vCPU utilization. This is often caused by an uneven work distribution. Potential causes include unevenly-loaded source partitions or hot keys.

To resolve this issue, try the following:

  * Determine the cause of the uneven loading and try to correct it. For example, ensure source partitions are evenly distributed.
  * If correcting the uneven load is not feasible, consider changing the worker VM shape to increase per-worker vCPUs to lower peak utilization. For more information on configuring per-worker vCPUs, see [Configure Dataflow worker VMs](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm).


Problem communicating with workers
    

Dataflow cannot communicate with all of the worker VMs. Check the status of the job's worker VMs. Possible causes include:

  * There is a problem provisioning the worker VMs.
  * The worker VM pool is deleted while the job is running.
  * Networking issues.


Pub/Sub source has pull errors.
    

There are errors pulling from the Pub/Sub source. Check that the required topic and subscriptions exist, and verify quota and configuration. You can also check the logs for errors.

Pub/Sub source has insufficient parallelism
    

The Pub/Sub source computation has an insufficient number of Pub/Sub keys. To increase the number of keys, set the `num_pubsub_keys` service option. For more information, see [Pub/Sub source parallelism](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub#parallelism).

Pub/Sub source throttled for unknown reason
    

The Pub/Sub source computation is throttled while reading from Pub/Sub, for an unknown reason. This issue might be transient. Check for Pub/Sub configuration issues, missing IAM permissions, or quota limits. However, if none of the previous areas is the root cause and the issue persists, [contact support](https://docs.cloud.google.com/dataflow/docs/support/getting-support).

Pub/Sub sink publish slow or stuck
    

The Pub/Sub sink computation is slow or stuck. This problem might be caused by a configuration issue or a quota limit.

High work queue time
    

The oldest eligible work age is high, due to a large number of keys and the rate at which keys are processed. In this situation, each operation might not be abnormally long, but the overall queuing delay is high.

Dataflow uses a single processing thread per sharding key, and the number of processing threads is limited. The queueing delay is approximately equal to the ratio of keys to threads, multiplied by the on-thread latency for each processing bundle for a key:

`(key count / total harness threads) * latency per bundle`

Try the following remediations:

  * Increase the number of workers. See [Streaming autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling#streaming).
  * Increase the number of worker harness threads. Set the `numberOfWorkerHarnessThreads` / `number_of_worker_harness_threads` [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#resource_utilization).
  * Decrease the number of keys.
  * Decrease the operation latency.


A transient issue with the Streaming Engine backend
    

There is a configuration or operational issue with the Streaming Engine backend. This issue might be transient. If the issue persists, [contact support](https://docs.cloud.google.com/dataflow/docs/support/getting-support).

An indeterminable cause
    

The cause of the backlog cannot be determined with certainty. This issue might be transient. If the issue persists, [contact support](https://docs.cloud.google.com/dataflow/docs/support/getting-support).

## Bottleneck metrics

The following job metrics provide information about bottlenecks:

  * **[`dataflow.googleapis.com/job/is_bottleneck`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/is_bottleneck)** : A boolean value indicating whether the stage is an active bottleneck, along with labels specifying the kind of bottleneck and the likely cause.
  * **[`dataflow.googleapis.com/job/backlogged_keys`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/backlogged_keys)** : The number of keys backed up in the bottlenecked stage.
  * **[`dataflow.googleapis.com/job/recommended_parallelism`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/recommended_parallelism)** : The recommended parallelism value to alleviate the bottleneck in the affected stage.



## What's next

  * [About the Dataflow bottleneck detector](https://docs.cloud.google.com/dataflow/docs/concepts/about-bottleneck-detector)
  * [Detect and resolve Dataflow pipeline bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/detect-resolve-bottlenecks)
  * [Blog for the bottleneck detector with real-world scenarios of misbehaving jobs](https://medium.com/google-cloud/transforming-dataflow-debugging-with-the-new-bottleneck-detector-feature-b31539c80b4d)
  * [Troubleshoot slow or stuck jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-jobs)
  * [Monitor pipeline performance using Profiler](https://docs.cloud.google.com/dataflow/docs/guides/profiling-a-pipeline)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
