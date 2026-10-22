---
url: https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes/
title: Set the pipeline streaming mode \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:10.678873+00:00
---

# Set the pipeline streaming mode  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Set the pipeline streaming mode Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow supports two modes for streaming jobs:

  * **Exactly-once mode**. This mode is the default for all Dataflow streaming jobs. In this mode, Dataflow ensures that records are not dropped or duplicated as the data moves through the pipeline.
  * **At-least-once mode**. This mode guarantees that records are processed at least once (that is, no input records are lost). However, duplicate records are possible in this mode. For use cases that can tolerate duplicates, at-least-once mode can significantly lower the cost and latency of your job.



## Choose which streaming mode to use

Choose exactly-once mode if you need to ensure exact results from the pipeline and predictable semantics. For example:

  * Pipelines with [aggregations](https://beam.apache.org/documentation/basics/#aggregation), such as count, sum, or mean.
  * Business-critical use cases that rely on records being processed once and only once. Examples include fraud detection, network threat detection, and ecommerce inventory dashboards.



Choose at-least-once streaming mode if your workload can tolerate duplicated records and might benefit from reduced cost or latency. For example:

  * Workloads where deduplication is performed downstream from Dataflow. For example, pipelines that write to BigQuery or a SQL datastore.
  * Map-only pipelines with no aggregations. Examples include log processing, change data capture, or extract, transform, and load (ETL) jobs, in which the pipeline performs only per-element transforms, such as schema translation.
  * Pipelines where the output sink can't guarantee exactly-once delivery, such as Pub/Sub. In that case, deduplication _within_ the pipeline might be unnecessary, and you can benefit from the reduced cost and latency of at-least-once streaming mode.
  * Pipelines that read from Pub/Sub. Reading from Pub/Sub is significantly optimized when using at-least-once mode.



### Additional considerations

  * At-least-once mode can significantly reduce the cost and latency of a pipeline. The exact impact depends on the specifics of the pipeline. Test at-least-once streaming under realistic loads to evaluate the impact.

  * When using at-least-once mode, the rate of duplicate records depends on the number of retries. The baseline rate is typically low (<1%). However, spikes can occur if worker nodes fail or other conditions cause repeated RPC calls.

  * The streaming mode affects how Streaming Engine processes records, but does not change the semantics of I/O connectors. It is recommended to align your I/O semantics with the streaming mode. For example, if you use at-least-once streaming mode with the [BigQuery I/O connector](https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigquery), set the write mode to `STORAGE_API_AT_LEAST_ONCE`. [Google-provided Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) automatically enable this option when you use at-least-once streaming.

**Note:** At-least-once streaming mode is incompatible with the `BigQueryIO` `FILE_LOADS` write method. Instead, use the `STORAGE_API_AT_LEAST_ONCE` write method or run the pipeline in exactly-once streaming mode.
  * Element-wise transforms such as `Map` are not always idempotent. For example, consider a function that receives a message and appends the current timestamp to it. In that case, a duplicate record can produce several distinct outputs. At-least-once mode might not be appropriate for that pipeline.




## Set the streaming mode

Exactly-once processing is the default setting for all Dataflow jobs. To enable at-least-once streaming mode, set the `streaming_mode_at_least_once` [service option](https://docs.cloud.google.com/dataflow/docs/reference/service-options).

###  Java 
    
    
    --dataflowServiceOptions=streaming_mode_at_least_once
    

###  Python 
    
    
    --dataflow_service_options=streaming_mode_at_least_once
    

###  Go 
    
    
    --dataflow_service_options=streaming_mode_at_least_once
    

If you don't specify the `streaming_mode_at_least_once` option, then Dataflow uses exactly-once streaming mode.

If you set the `streaming_mode_at_least_once` option, Dataflow automatically enables [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) with [resource-based billing](https://docs.cloud.google.com/dataflow/docs/streaming-engine#compute-unit-pricing).

To update the streaming mode on a running job, [launch a replacement job](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline#Launching).

## Select the streaming mode for a template

To select the streaming mode when you run a Dataflow streaming template, perform the following steps:

###  Console 

  1. In the Google Cloud console, go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Click **Create job from template**.

  3. Select the template that you want to run from the **Dataflow template** drop-down menu.

  4. For **Streaming mode** , select the streaming mode. If the template supports only one mode, then this option is disabled.




###  gcloud 

To enable at-least-once mode, set the `streaming_mode_at_least_once` option in the `additional-experiments` flag:
    
    
    --additional-experiments=streaming_mode_at_least_once
    

To enable exactly-once mode, set the `streaming_mode_exactly_once` option in the `additional-experiments` flag:
    
    
    --additional-experiments=streaming_mode_exactly_once
    

These two options are mutually exclusive. If you don't set one of these options, then the template defaults to a streaming mode that is determined by the template metadata. For more information, see Custom templates.

###  REST 

Use the `additionalExperiments` field in the [`FlexTemplateRuntimeEnvironment`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch#FlexTemplateRuntimeEnvironment) (Flex templates) or [`RuntimeEnvironment`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/RuntimeEnvironment) (classic templates) object.
    
    
    {
      additionalExperiments : ["streaming_mode_at_least_once"]
      ...
    }
    

### Custom templates

If you create a custom template that supports at-least-once processing, add the following top-level fields to the template metadata file:
    
    
    {
      "streaming": true,
      "supportsAtLeastOnce": true,
      "supportsExactlyOnce": true,
      "defaultStreamingMode": "AT_LEAST_ONCE"
    }
    

These metadata fields enable users to select the streaming mode when deploying the template in the Google Cloud console. The `defaultStreamingMode` field is optional and specifies the default streaming mode for the template. If you don't specify `defaultStreamingMode` and the template supports both modes, then exactly-once mode is the default.

For more information, see the following sections in the Dataflow templates documentation:

  * Flex templates: [Metadata](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#metadata)
  * Classic templates: [Use metadata in your pipeline code](https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates#use-metadata-in-your-pipeline-code)



## View a job's streaming mode

To view the streaming mode for a job, go to the **Jobs** page in the Google Cloud console.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

The streaming mode is also listed on the job details page, in the **Job info** panel.

## Limitations

At-least-once streaming mode requires [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) with [resource-based billing](https://docs.cloud.google.com/dataflow/docs/streaming-engine#compute-unit-pricing).

## Pricing

At-least-once mode always uses [resource-based billing](https://docs.cloud.google.com/dataflow/docs/streaming-engine#compute-unit-pricing), where you're billed for the total resources that are consumed by your job.

The per-unit cost of [Streaming Engine Compute Units](https://cloud.google.com/dataflow/pricing#streaming-compute-units) is the same regardless of the streaming mode. However, in most cases a pipeline consumes significantly fewer total resources when using at-least-once mode.

## What's next

  * Learn more about [exactly-once processing](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
