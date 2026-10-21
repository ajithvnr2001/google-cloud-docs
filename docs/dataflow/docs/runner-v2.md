---
url: https://docs.cloud.google.com/dataflow/docs/runner-v2/
title: Use the Dataflow Portable Runner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:24:45.000813+00:00
---

# Use the Dataflow Portable Runner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/runner-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use the Dataflow Portable Runner Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Dataflow Portable Runner was previously called _Runner v2_. The standard JVM-based runner is called the _Non-Portable Runner_ for batch workloads, or the _Streaming Java Runner_ for streaming workloads.

When you use Dataflow to run your pipeline, the Dataflow runner uploads your pipeline code and dependencies to a Cloud Storage bucket and creates a Dataflow job. This Dataflow job runs your pipeline on managed resources in Google Cloud.

  * For batch pipelines that use the Apache Beam Java SDK versions 2.54.0 or later, the Portable Runner is enabled by default.
  * For pipelines that use the Apache Beam Java SDK, the Portable Runner is required when running multi-language pipelines, using custom containers, or using Spanner or Bigtable change stream pipelines. For high-scale Java streaming pipelines, use the Streaming Java (default) Runner.
  * For pipelines that use the Apache Beam Python SDK versions 2.21.0 or later, the Portable Runner is enabled by default. For pipelines that use the Apache Beam Python SDK versions 2.45.0 and later, the Dataflow Portable Runner is the only Dataflow runner available.
  * For the Apache Beam SDK for Go, the Portable Runner is the only Dataflow runner available.



The Portable Runner uses a services-based architecture that benefits many pipelines:

  * The Dataflow Portable Runner lets you pre-build your Python container, which can improve VM startup times and Horizontal Autoscaling performance. For more information, see [Pre-build Python dependencies](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image#prebuild).

  * The Dataflow Portable Runner supports [multi-language pipelines](https://beam.apache.org/documentation/programming-guide/#multi-language-pipelines), a feature that enables your Apache Beam pipeline to use transforms defined in other Apache Beam SDKs. The Dataflow Portable Runner supports [using Java transforms from a Python SDK pipeline](https://beam.apache.org/documentation/sdks/python-multi-language-pipelines/) and [using Python transforms from a Java SDK pipeline](https://beam.apache.org/documentation/sdks/java-multi-language-pipelines/). When you run Apache Beam pipelines without the Portable Runner, the Dataflow runner uses language-specific workers.




## Usage recommendations

Unless your pipeline is affected by one of the limits described in this document, use the following guidance to help select the appropriate runner based on your pipeline requirements:

**Select the Portable Runner for:**

  * All batch pipelines.
  * Streaming pipelines that use the Apache Beam Python SDK or the Apache Beam SDK for Go.
  * Streaming pipelines that require GPU support for machine learning processing.
  * Pipelines that use any of the portable runner-only features.



**Select the Streaming Java Runner for:**

  * Streaming pipelines that use the Apache Beam Java SDK.



## Limitations and restrictions

The Dataflow Portable Runner has the following requirements and limitations:

  * **Portable Runner-only features:** The following features are only supported on the Portable Runner: 
    * [Managed transforms](https://docs.cloud.google.com/dataflow/docs/guides/managed-io) and `RunInference` in Java.
    * Custom containers.
    * ARM-based worker VMs.
    * Splittable DoFns. Support for the Non-Portable runner is being explored.
  * The Dataflow Portable Runner requires [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) for streaming jobs.
  * Because the Dataflow Portable Runner requires Streaming Engine for streaming jobs, any Apache Beam transform that requires the Dataflow Portable Runner also requires the use of Streaming Engine for streaming jobs. For example, the [Pub/Sub Lite I/O connector](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsublite.html) for the Apache Beam SDK for Python is a cross-language transform that requires the Dataflow Portable Runner. If you try to disable Streaming Engine for a job or template that uses this transform, the job fails.
  * While the Portable Runner scales better than the Non-Portable runner in many batch cases, the memory usage might be higher for fixed sharding.
  * Dataflow [classic templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates) can't be run with a different version of the Dataflow runner than they were built with. This means that Google-provided classic templates can't enable the Portable Runner. To enable the Portable Runner for custom templates, set the appropriate flag when you build the template. This flag depends on the SDK version you're using: 
    * Beam SDK versions 2.74 and later: `--experiments=enable_portable_runner`.
    * Beam SDK versions 2.73 and earlier: `--experiments=use_runner_v2`.
  * Due to a known autoscaling issue, the Portable Runner is disabled by default for batch Java pipelines that require [stateful processing](https://beam.apache.org/documentation/programming-guide/#state-and-timers). You can still enable the Portable Runner for those pipelines (see [Enable the Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner#enable)), but pipeline performance might be severely bottlenecked.

  * In some pipelines, the Portable Runner can increase the frequency of consistency failures. You might see the following error in the log files: "Internal consistency check failed, the output is likely incorrect. Please retry the job". A possible mitigation is to add a `Reshuffle` transform after the `Join`/`GroupByKey` step. If the failure rate is not tolerable and the mitigation does not solve the issue, try [disabling the Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner#disable).




## Enable the Portable Runner

To enable the Dataflow Portable Runner, follow the configuration instructions for your Apache Beam SDK.

### Java

The Dataflow Portable Runner requires the Apache Beam Java SDK versions 2.30.0 or later, with version 2.44.0 or later being recommended.

For batch pipelines that use the Apache Beam Java SDK versions 2.54.0 or later, the Portable Runner is enabled by default.

To enable the Portable Runner, run your job with the experiment value that corresponds with your Beam SDK version and pipeline type:

  * Beam SDK versions 2.74 and later: `enable_portable_runner`. **Note:** Beam SDK version 2.74 log messages still refer to the Portable Runner as _Runner v2_. 
  * Beam SDK versions 2.73 and earlier: `use_runner_v2`.



For more information, see [Set experimental pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#experimental).

### Python

For pipelines that use the Apache Beam Python SDK versions 2.21.0 or later, the Portable Runner is enabled by default.

The Dataflow Portable Runner isn't supported with the Apache Beam Python SDK versions 2.20.0 and earlier.

In some cases, your pipeline might not use the Portable Runner even though the pipeline runs on a supported SDK version. To run the job with the Portable Runner, set the experiment value that corresponds with your Beam SDK version:

  * Beam SDK versions 2.74 and later: `enable_portable_runner`. **Note:** Beam SDK version 2.74 log messages still refer to the Portable Runner as _Runner v2_. 
  * Beam SDK versions 2.73 and earlier: `use_runner_v2`.



For more information, see [Set experimental pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#experimental).

### Go

The Dataflow Portable Runner is the only Dataflow runner available for the Apache Beam SDK for Go. The Portable Runner is enabled by default.

## Disable the Portable Runner

To disable the Dataflow Portable Runner, follow the configuration instructions for your Apache Beam SDK.

### Java

To disable the Portable Runner, set the experiment value that corresponds with your Beam SDK version:

  * Beam SDK versions 2.74 and later: 
    * For batch, use `disable_portable_runner`.
    * For streaming, use `enable_streaming_java_runner`.
  * Beam SDK versions 2.73 and earlier: `disable_runner_v2`.



This will default the job to the Non-Portable Runner, or the Streaming Java Runner for streaming. For more information, see [Set experimental pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#experimental).

### Python

Disabling the Portable Runner is not supported with the Apache Beam Python SDK versions 2.45.0 and later.

For earlier versions of the Python SDK, if your job is identified as using the `auto_runner_v2` experiment, you can disable the Portable Runner by setting the `disable_runner_v2` experiment. For more information, see [Set experimental pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#experimental).

### Go

The Dataflow Portable Runner can't be disabled in Go. The Portable Runner is the only Dataflow runner available for the Apache Beam SDK for Go.

## Monitor your job

Use the monitoring interface to view [Dataflow job metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf), such as memory utilization, CPU utilization, and more.

Worker VM logs are available through the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) and the [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview). Worker VM logs include logs from the runner harness process and logs from the SDK processes. You can use the VM logs to troubleshoot your job.

## Troubleshoot the Portable Runner

To troubleshoot jobs using the Dataflow Portable Runner, follow [standard pipeline troubleshooting steps](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline). The following list provides additional information about how the Dataflow Portable Runner works:

  * Dataflow Portable Runner jobs run two types of processes on the worker VM: SDK process and the runner harness process. Depending on the pipeline and VM type, there might be one or more SDK processes, but there is only one runner harness process per VM.
  * SDK processes run user code and other language-specific functions. The runner harness process manages everything else.
  * The runner harness process waits for all SDK processes to connect to it before starting to request work from Dataflow.
  * Jobs might be delayed if the worker VM downloads and installs dependencies during the SDK process startup. If issues occur during an SDK process, such as when starting up or installing libraries, the worker reports its status as unhealthy. If the startup times increase, enable the Cloud Build API on your project and submit your pipeline with the following parameter: `--prebuild_sdk_container_engine=cloud_build`.
  * Because Dataflow Portable Runner uses checkpointing, each worker might wait for up to five seconds while buffering changes before sending the changes for further processing. As a result, latency of approximately six seconds is expected.

**Note:** The pre-build feature requires the Apache Beam SDK for Python, version 2.25.0 or later.

  * To diagnose problems in your user code, examine the worker logs from the SDK processes. If you find any errors in the runner harness logs, [contact Support](https://console.cloud.google.com/support) to file a bug.
  * To debug common errors related to Dataflow multi-language pipelines, see the [Multi-language Pipelines Tips](https://cwiki.apache.org/confluence/display/BEAM/Multi-language+Pipelines+Tips) guide.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
