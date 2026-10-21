---
url: https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime/
title: Use Dataflow Prime \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:43.246858+00:00
---

# Use Dataflow Prime  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Dataflow Prime Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow Prime is a serverless data processing platform for Apache Beam pipelines. Based on Dataflow, Dataflow Prime uses a compute and state-separated architecture. In the following cases, Dataflow Prime might improve pipeline efficiency:

  * Your pipeline would benefit from [Vertical Autoscaling](https://docs.cloud.google.com/dataflow/docs/vertical-autoscaling).



Dataflow Prime supports both batch and streaming pipelines. By default, Dataflow Prime uses [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch) and the [Dataflow Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner) for batch pipelines.

## SDK version support

Dataflow Prime supports the following Apache Beam SDKs:

  * Apache Beam Python SDK version 2.21.0 or later

  * Apache Beam Java SDK version 2.30.0 or later

  * Apache Beam Go SDK version 2.44.0 or later




To download the SDK package or to read the Release Notes, see [Apache Beam Downloads](https://beam.apache.org/get-started/downloads/).

## Dataflow Prime features

The following is the list of supported Dataflow Prime features for different kinds of pipelines:

  * **Vertical Autoscaling (memory).** Supports streaming pipelines in Python, Java, and Go.
  * **Job Visualizer.** Supports batch pipelines in Python and Java.
  * **Smart Recommendations.** Supports both streaming and batch pipelines in Python and Java.
  * **Data Pipelines.** Supports both streaming and batch pipelines in Python and Java.



The features Job Visualizer, Smart Recommendations, and Data Pipelines are also supported for non-Dataflow Prime jobs.

### Vertical Autoscaling

This feature automatically adjusts the memory available to the Dataflow worker VMs to fit the needs of the pipeline and help prevent out-of-memory errors. In Dataflow Prime, Vertical Autoscaling works alongside Horizontal Autoscaling to scale resources dynamically.

For more information, see [Vertical Autoscaling](https://docs.cloud.google.com/dataflow/docs/vertical-autoscaling).

### Job Visualizer

This feature lets you see the performance of a Dataflow job and optimize the performance of the job by finding inefficient code, including parallelization bottlenecks. In the Google Cloud console, you can click any Dataflow job in the **Jobs** page to view details about the job. You can also see the list of steps associated with each stage of the pipeline.

For more information, see [Execution details](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details).

### Smart Recommendations

This feature lets you optimize and troubleshoot the pipeline based on the recommendations provided in the **Diagnostics** tab of the job details page. In the Google Cloud console, you can click any Dataflow job in the **Jobs** page to view details about the job.

For more information, see [Diagnostics](https://docs.cloud.google.com/dataflow/docs/guides/logging#diagnostics).

### Data Pipelines

This feature lets you schedule jobs, observe resource utilizations, track data freshness objectives for streaming data, and optimize pipelines.

For more information, see [Working with Data Pipelines](https://docs.cloud.google.com/dataflow/docs/guides/data-pipelines).

## Quota and limit requirements

Quotas and limits are the same for Dataflow and Dataflow Prime. For more information, see [Quotas and limits](https://cloud.google.com/dataflow/quotas).

If you opt for Data Pipelines, there are additional implications for [quotas and regions](https://docs.cloud.google.com/dataflow/docs/guides/data-pipelines#overview).

## Unsupported features

Dataflow Prime doesn't support the following:

  * Designating specific VM types by using the flag `--worker_machine_type` or `--machine_type` for Python pipelines and `--workerMachineType` for Java pipelines.
  * Designating specific VM types or CPU platforms by using experimental parameters, such as `--additional-experiments=min_cpu_platform=...` or `--experiments=min_cpu_platform=...`. Attempting to set a minimum CPU platform with Dataflow Prime might result in an error such as: `Setting minimum CPU platform is not supported for the selected machine type e2-standard-2.`
  * Viewing or using SSH to log into worker VMs.
  * [Flexible Resource Scheduling (FlexRS)](https://docs.cloud.google.com/dataflow/docs/guides/flexrs).
  * [Auto VM Selection](https://docs.cloud.google.com/dataflow/docs/guides/auto-vm-selection) isn't supported when you use Dataflow Prime.
  * Using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) with Vertical Autoscaling. If you enable Dataflow Prime and launch a new job within a VPC Service Controls perimeter, the job uses Dataflow Prime without Vertical Autoscaling.
  * [NVIDIA Multi-Process Service (MPS)](https://docs.cloud.google.com/dataflow/docs/gpu/use-nvidia-mps).
  * Java pipelines that meet the following requirements can use the [`MapState`](https://beam.apache.org/releases/javadoc/current/index.html?org/apache/beam/sdk/state/MapState.html) and [`SetState`](https://beam.apache.org/releases/javadoc/current/index.html?org/apache/beam/sdk/state/SetState.html) classes: 
    * use Streaming Engine
    * use Apache Beam SDK versions 2.58.0 and later
    * don't use the Portable Runner



All [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options) not explicitly mentioned previously or in the feature comparison table work the same for Dataflow and Dataflow Prime.

## Before using Dataflow Prime

To use Dataflow Prime, you can reuse your existing pipeline code and also enable the Dataflow Prime option either through Cloud Shell or programmatically.

Dataflow Prime is backward compatible with batch jobs that use Dataflow Shuffle and streaming jobs that use Streaming Engine. However, we recommend testing your pipelines with Dataflow Prime before you use them in a production environment.

If your streaming pipeline is running in production, to use Dataflow Prime, perform the following steps:

  1. [Stop](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline) the pipeline.

  2. Enable Dataflow Prime.

  3. Rerun the pipeline.




## Enable Dataflow Prime

To enable Dataflow Prime for a pipeline:

  1. Enable the Cloud Autoscaling API.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=autoscaling.googleapis.com)

Dataflow Prime uses the Cloud Autoscaling API to dynamically adjust memory.

  2. Enable Prime in your pipeline options.

You can set the [pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options) either programmatically or by using the command line. For [supported Apache Beam SDK versions](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime#sdk_version_support), enable the following flag:




### Java
    
    
    --dataflowServiceOptions=enable_prime
    

### Python

Apache Beam Python SDK version 2.29.0 or later:
    
    
    --dataflow_service_options=enable_prime
    

Apache Beam Python SDK version 2.21.0 to 2.28.0:
    
    
    --experiments=enable_prime
    

### Go
    
    
    --dataflow_service_options=enable_prime
    

## Disable Dataflow Prime

Sometimes, such as with certain Google-provided templates, Dataflow Prime might be enabled by default. To explicitly disable Dataflow Prime and use standard Dataflow, set the `enable_prime` pipeline option to `false`.

### Java
    
    
    --dataflowServiceOptions=enable_prime=false
    

### Python

Apache Beam Python SDK version 2.29.0 or later:
    
    
    --dataflow_service_options=enable_prime=false
    

Apache Beam Python SDK version 2.21.0 to 2.28.0:
    
    
    --experiments=enable_prime=false
    

### Go
    
    
    --dataflow_service_options=enable_prime=false
    

## Use Dataflow Prime with templates

If you're using Dataflow templates, you can choose to enable Dataflow Prime in one of the following ways:

  1. For jobs launched from the **Create job from template** page:

     1. Go to the **Create job from template** page.

[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)

     2. In the **Additional experiment** field, enter `enable_prime`.

  2. For jobs launched from a template through the command line interface, pass the `--additional-experiments=enable_prime` flag.

  3. To enable Dataflow Prime when you create a template, set the `--experiments=enable_prime` flag.




## Use Dataflow Prime in Apache Beam notebooks

If you're using an [Apache Beam notebook](https://docs.cloud.google.com/dataflow/docs/guides/interactive-pipeline-development), you can enable Dataflow Prime [programmatically](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#setting_pipeline_options_programmatically) using `PipelineOptions`:
    
    
    options = pipeline_options.PipelineOptions(
        flags=[],
        dataflow_service_options=['enable_prime'],
    )
    

To learn more about setting Dataflow options in a notebook, see [Launch Dataflow jobs from a pipeline created in your notebook](https://docs.cloud.google.com/dataflow/docs/guides/interactive-pipeline-development#launch-jobs-from-pipeline).

## Feature comparison between Dataflow and Dataflow Prime

The following table compares the available features for both variants of Dataflow.

Feature | Dataflow Prime | Dataflow  
---|---|---  
[Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner) | Default feature with no option to turn off for batch jobs and optional for streaming jobs | Default feature with an option to turn off for batch jobs and optional for streaming jobs  
[Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch) for batch jobs | Default feature with an option to turn off | Default feature with an option to turn off  
[Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) for streaming jobs | Optional feature for Java pipelines and always on for Python pipelines | Optional feature for Java pipelines and always on for Python pipelines since 2.45.0  
[Horizontal Autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling) | Default feature with option to turn off | Default feature with option to turn off  
[Vertical Autoscaling](https://docs.cloud.google.com/dataflow/docs/vertical-autoscaling) | Default feature with option to turn off | Not applicable  
[Right fitting](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting) | Optional feature | Optional feature  
[Billing](https://cloud.google.com/dataflow/pricing) | Serverless billing | Standard billing  
  
## What's next

  * Read about Dataflow [quotas](https://cloud.google.com/dataflow/quotas).
  * Learn how to set [pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options).
  * See available [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#worker-level_options) for Java and Python pipelines.
  * Learn more about [autotuning features](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#autotuning-features) for Dataflow Prime.
  * Learn more about Dataflow [GPUs](https://docs.cloud.google.com/dataflow/docs/gpu).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
