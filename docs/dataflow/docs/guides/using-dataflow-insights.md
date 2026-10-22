---
url: https://docs.cloud.google.com/dataflow/docs/guides/using-dataflow-insights/
title: Use Dataflow Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:39.900007+00:00
---

# Use Dataflow Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/using-dataflow-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Dataflow Insights Stay organized with collections  Save and categorize content based on your preferences. 

You can use Dataflow Insights to help optimize job performance. This topic demonstrates how to interact with Dataflow Insights using `gcloud` or the REST API. You can also review Insights in the Dataflow Console. For more information on reviewing Insights in the Console, see [Recommendations](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview#recommendations).

## Overview

Dataflow Insights provides [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights) on improving job performance, reducing cost, and troubleshooting errors. Dataflow Insights is part of the [Recommender](https://docs.cloud.google.com/recommender/docs) service and is available through the `google.dataflow.diagnostics.Insight` type.

When you're working with Dataflow Insights, keep in mind that some recommendations might not be relevant to your use case.

## Before you begin

Before you can begin using Dataflow Insights, you must complete the following steps.

  1. [Enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling).
  2. Set up authentication.

Select the tab for how you plan to use the samples on this page:

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

  3. Ensure that your account has the following permissions:

     * `recommender.dataflowDiagnosticsInsights.get`
     * `recommender.dataflowDiagnosticsInsights.list`
     * `recommender.dataflowDiagnosticsInsights.update`

You can grant these permissions individually, or you can grant one of the following roles:

     * `roles/recommender.dataflowDiagnosticsViewer`
     * `roles/recommender.dataflowDiagnosticsAdmin`
     * `roles/dataflow.viewer`
     * `roles/dataflow.developer`
     * `roles/dataflow.admin`



## Request Dataflow insights

You can list Dataflow insights as shown below. For other types of insights interactions, see [the insights guide for the Recommender API](https://docs.cloud.google.com/recommender/docs/insights/using-api).

### List Dataflow insights

To list all Dataflow insights for your project in a given region, use one of the following methods:

###  gcloud 

You can use the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command to view all Dataflow insights for your project in a specified region.

Before you run the command, replace the following values:

  * PROJECT_ID: The ID of the project that you want to list insights for.
  * REGION: The region where your Dataflow jobs are running. For example: `us-west1`.


    
    
    gcloud recommender insights list --insight-type=google.dataflow.diagnostics.Insight \
      --project=PROJECT_ID \
      --location=REGION
    

The output lists all of the Dataflow insights for your project in the specified region.

###  REST 

You can use Recommender API's [insights.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method to list all Dataflow insights for your project in a specified region.

Before using any of the request data, make the following replacements:

  * PROJECT_ID: The ID of the project that you want to list insights for.
  * REGION: The region where your Dataflow jobs are running. For example: `us-west1`.



HTTP method and URL:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/insightTypes/google.dataflow.diagnostics.Insight/insights
    

To send your request using curl (Linux, macOS, or Cloud Shell), run the following command:
    
    
    curl -X GET \
      -H "Authorization: Bearer "$(gcloud auth print-access-token) \
      "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/insightTypes/google.dataflow.diagnostics.Insight/insights"
    

### Get a single Dataflow insight

To get more information about a single insight, including the insight's description, status, and any recommendations associated with it, use one of the following methods:

###  gcloud 

Use the [`gcloud recommender insights describe`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/describe) command with your insight ID to view information about a single insight. Before you run the command, replace the following values:

  * INSIGHT_ID: The ID of the insight that you want to view.
  * PROJECT_ID: The ID of the project that you want to list insights for.
  * REGION: The region where your Dataflow jobs are running. For example: `us-west1`.


    
    
    gcloud recommender insights describe INSIGHT_ID \
      --insight-type=google.dataflow.diagnostics.Insight \
      --project=PROJECT_ID \
      --location=REGION
    

The output shows the insight in detail.

###  REST 

The Recommender API's [insights.get](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/get) method gets a single insight. Before using any of the request data, make the following replacements:

  * PROJECT_ID: The ID of the project that you want to list insights for.
  * REGION: The region where your Dataflow jobs are running. For example: `us-west1`.
  * INSIGHT_ID: The ID of the insight that you want to view.



HTTP method and URL:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/insightTypes/google.dataflow.diagnostics.Insight/insights/INSIGHT_ID
    

To send your request using curl (Linux, macOS, or Cloud Shell), run the following command:
    
    
    curl -X GET \
      -H "Authorization: Bearer "$(gcloud auth print-access-token) \
      "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/insightTypes/google.dataflow.diagnostics.Insight/insights/INSIGHT_ID"
    

## Interpret Dataflow insights

After you get an insight, you can review its contents to understand the pattern of resource usage that it highlights. In addition to the [standard insight attributes](https://docs.cloud.google.com/recommender/docs/insights/using-insights), Dataflow Insights provides the following subtypes:

  * `AUTOSCALING_NOT_ENABLED`: [Autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling) could be enabled. The job has high CPU utilization and is using the maximum number of workers set. Enabling autoscaling could improve performance.
  * `HIGH_FAN_OUT`: A [fusion](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#fusion_optimization) break could be inserted after one or more transforms to increase parallelism.
  * `MAX_NUM_WORKERS`: [Autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling): The maximum number of workers could be increased. The job is using autoscaling, has high CPU utilization, and is using the maximum number of workers set. Increasing the maximum number of workers could improve performance.
  * `WORKER_OUT_OF_MEMORY`: Some of the workers for the job failed due to running out of memory, which could slow down the job or cause it to fail.
  * `PREBUILD_NOT_UTILIZED`: Use the worker image [pre-building workflow](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image#prebuild) to improve worker startup time and autoscaling reliability.
  * `ACTIVE_KEYS` ([Preview](https://cloud.google.com/products/#product-launch-stages)): Total number of active keys are less than total number of cores and scaling up won't help.
  * `LONG_WORK_ITEM`: Work in a fused stage is taking too long to process, indicating a slow-running or stuck operation.



To learn more about how to mitigate problems identified by Dataflow Insights, see Insights.

Dataflow Insights also provides a special `content` field that contains subfields with additional information and metadata about an insight. Depending on your use case, the following `content` subfields might be useful:

  * `jobName`: The Dataflow job name.
  * `description`: A description of the insight in English.
  * `title`: The title of the insight in English.



## Insights

### High fan-out detected

When Dataflow detects that a job has one or more transforms with a high fan-out, the following message appears:
    
    
    High fan-out detected
    

This message displays when a ParDo that has a high output-to-input element count ratio is fused with a subsequent ParDo. In this situation, the second ParDo runs sequentially with the first, which forces all the output elements of a given input onto the same worker and reduces parallelism and slowing down performance.

To resolve this issue:

  * Insert a `GroupByKey` and ungroup after your first ParDo. The Dataflow service never fuses ParDo operations across an aggregation. For more information, see [Fusion optimization](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#fusion_optimization)
  * Pass the intermediate PCollection as a side input to another ParDo. The Dataflow service always materializes side inputs.
  * Insert a Reshuffle step. Reshuffle prevents fusion, checkpoints the data, and reconfigures the windowing strategy so that no data is dropped. Reshuffle is supported by Dataflow even though it is marked deprecated in the Apache Beam documentation (note that reshuffling data can increase the cost of running your pipeline).



### Autoscaling: Maximum number of workers could be increased

When Dataflow detects that a job is using the maximum number of allowed workers, [`maxNumWorkers`](https://cloud.google.com/dataflow/docs/reference/pipeline-options) (or `max_num_workers`), and that the job might use more workers if this maximum was increased, the following message appears:
    
    
    maximum number of workers could be increased
    

For example, this recommendation occurs for a batch or streaming job that has `maxNumWorkers` set to 50 when all 50 workers are being used with an average worker CPU utilization above 80%. This recommendation also occurs for streaming jobs that have `maxNumWorkers` set to 50 when all 50 workers are being used with an average worker CPU utilization above 50% and the job has an estimated processing time over 2 minutes.

Typically, increasing `maxNumWorkers` increases pipeline throughput. A batch pipeline could complete in less time, and a streaming pipeline could handle larger spikes in data and process more elements per second. However, this might come at an increased cost. For more information, see [Worker resources pricing](https://cloud.google.com/dataflow/pricing#worker_resources_pricing). For details about how the Autoscaling algorithm works and how to configure it, see the [Autoscaling guide](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling).

To resolve this issue:

  * Increase or remove the `maxNumWorkers` pipeline option. Without the option, Dataflow uses the defaults listed in the [Autoscaling guide](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling).
  * It's okay to do nothing if pipeline performance is adequate. 
    * For batch pipelines, check that the total running time meets your requirements.
    * For streaming pipelines, check the **Data freshness** graph on the **Job Metrics** tab of the job page. Verify that the values in the graph aren't continuously increasing and that they are within acceptable bounds.



### Autoscaling: Setting the initial number of workers could improve the job performance

When Dataflow detects that a job is using a certain number of workers for more than 50% of the running time, setting the initial number of workers to the recommended value could improve the job performance by reducing the running time for batch jobs or preventing the backlog from growing when updating a streaming job.

### Workers are failing with OutOfMemory errors

When Dataflow detects that workers for a job are failing because of Out of Memory errors, the following message appears:
    
    
    Some workers are out of memory
    

Some workers for the job have failed due to being out of memory. Although it is possible the job will finish, it is also possible these errors will prevent the job from completing successfully or otherwise slow down performance.

Try the following suggestions:

  * Manually increase the amount of memory available to workers.
  * Reduce the amount of memory required, by profiling memory usage. For more information, see [Troubleshoot Dataflow out of memory errors](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom).



### Pre-build workflow not utilized

When Dataflow detects a pipeline where the worker image pre-building workflow is not used, the following message appears:
    
    
    pre-build workflow not utilized
    

When the worker image pre-building workflow is not used, the pipeline has dependencies that are repetitively installed at runtime. This configuration slows worker startup time, which degrades the throughput of the job and causes unreliable autoscaling behavior.

To resolve this issue, use the worker image pre-building workflow when launching the pipeline. For more information, see [Pre-build Python dependencies](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image#prebuild).

If a customized, pre-built container is already in use, to avoid unnecessary installations, add the '--sdk_location=container' option, and remove the following options:

  * '--setup_file'
  * '--requirements_file'
  * '--extra_package(s)'



### Active keys are low

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When Dataflow detects that a job is falling behind because the number of active keys is less than the total number of cores and scaling up won't help, the following message appears:
    
    
    Active keys can be increased
    

To run user code in jobs, Dataflow uses workers. Each thread maps to a key that is responsible for a set of data to process and a key can only be run on a single core at a time for correctness reasons.

In some cases, some cores are overworked while others are idle. To resolve this issue, increase the number of keys, which also increases the number of active threads.

Potential solutions to increase keys: \- You can increase the number of keys by using a more specific key type. For example, if the key type is `IP address`, fewer keys are available. However, if you change the key type to `IP + [user identifier]`, more keys are available, which increases parallelism. \- For pipelines that write to BigQuery where sinks could potentially be the bottleneck, refer to [this article](https://cloud.google.com/blog/products/data-analytics/3x-dataflow-throughput-auto-sharding-bigquery). \- For other sources/sinks, check to see if it has have a `numShards` parameter and increase it. In general one shard maps to one key. \- For more general guidance on our execution model, refer to [this article](https://medium.com/google-cloud/streaming-engine-execution-model-1eb2eef69a8e). \- Fanout can be used to take a single input key and add a hash to it to produce multiple output keys. [Reference](https://beam.apache.org/releases/javadoc/2.1.0/org/apache/beam/sdk/transforms/Combine.Globally.html#withFanout-int-)

### Stage spending too long on work

When Dataflow detects that work has frequently taken too long to finish processing, the following message appears:
    
    
    Stage spending too long on work
    

Dataflow sends work to fused stages in bundles of elements to be processed, and each bundle is considered complete once all elements and their outputs have been processed for the stage. Streaming pipelines are optimized around bundles of work that take less than a minute to fully process, so long processing times can cause further performance issues in pipelines.

This issue can be caused by user transforms that are stuck or slow. These transforms can be identified by warnings emitted in Cloud Logging and its Diagnostics tab, with the key phrases "Operation ongoing" or "Processing stuck". To diagnose whether this issue is caused by a user transform, use Cloud Profiler to inspect the performance of user transforms. Then trace what code is causing the slowdown and how frequently. For more information, see [Troubleshooting Common Dataflow Errors](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#processing-stuck).

If investigating reveals that the long processing times are not caused by user transforms, then we recommend contacting Cloud Support and describing the steps taken to investigate.

### Job stuck on work item

When Dataflow detects that a key is stuck because a single work item has repeatedly failed and then been retried, the following message appears:
    
    
    Job is stuck due to failed and retried work item
    

In Dataflow, all messages in a pipeline are processed under a particular key. When an error occurs while processing a message, that message is retried. It's acceptable if a message is retried two or three times. However, if errors occur over and over again, such as ten times in a row, it usually indicates a fundamental problem with the pipeline code. When a particular message on a key gets retried, other messages under the same key can't make progress. If a message fails 10 or more times, the issue will likely not resolve on its own. This message failure can cause pipeline problems such as:

  * delaying the watermark
  * accruing backlog
  * preventing a drain operation from completing



To debug this issue, investigate the stage that the recommendation reported and review the logs to identify the problematic code. Then, update the job with the new pipeline code to get the job unstuck.

### Streaming Engine not enabled

When Dataflow detects that a streaming job doesn't have [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) enabled, the following message appears:
    
    
    This job isn't using Streaming Engine. It might benefit from having Streaming Engine enabled.
    

Using Streaming Engine has various potential benefits, including better horizontal autoscaling, improved supportability, and reduced CPU, memory, and Persistent Disk storage resource usage on the worker VMs. Streaming Engine also supports [resource-based billing](https://docs.cloud.google.com/dataflow/docs/streaming-engine#pricing).

### Kafka partitions low

When Dataflow detects that a streaming job reads from Kafka and the read stage keys are identified as a bottleneck, the following message appears:
    
    
    The partition count provided by the Kafka source is too low, consider increasing
    partitions or redistributing to more keys.
    

We recommended that you increase the number of partitions, or include a Redistribute transform `withRedistribute()` and consider offset deduplication mode `withOffsetDeduplication()`. For additional information about Kafka Read best practices for parallelism, see [Read from Kafka](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka#parallelism).

### Kafka persistence cost

When Dataflow detects that a streaming job reads from Kafka with Redistribute and the cost of persisting outputs is high, the following message appears:
    
    
    Redistribute requires persistence of Kafka outputs as part of the shuffle phase,
    consider reducing latency and cost with offset deduplication mode.
    

To minimize the latency and cost of the shuffle, use offset deduplication mode `withOffsetDeduplication()`. For additional information about Kafka Read best practices for parallelism, see [Read from Kafka](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka#parallelism).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
