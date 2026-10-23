---
url: https://docs.cloud.google.com/managed-spark/docs/guides/profiling-serverless/
title: Profile resource usage \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:33.251105+00:00
---

# Profile resource usage  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/profiling-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)



Send feedback 

#  Profile resource usage Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to profile Managed Service for Apache Spark resource usage. [Cloud Profiler](https://docs.cloud.google.com/profiler/docs) continuously gathers and reports application CPU usage and memory allocation information. You can enable profiling when you submit a batch or create a session workload by using the profiling properties listed in the following table. Managed Service for Apache Spark appends related JVM options to the `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` configurations used for the workload.

Option | Description | Value | Default  
---|---|---|---  
`dataproc.profiling.enabled` | Enable profiling of the workload | `true` or `false` | `false`  
`dataproc.profiling.name` | Profile name on the Profiler service | PROFILE_NAME | spark-WORKLOAD_TYPE-WORKLOAD_ID, where:  


  * WORKLOAD_TYPE is set to `batch` or `session`
  * WORKLOAD_ID is set to [`batchId`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches/create#body.QUERY_PARAMETERS.batch_id) or [`sessionId`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessions/create#body.QUERY_PARAMETERS.session_id)

  
  
Notes:

  * Managed Service for Apache Spark sets the profiler version to either the [batch UUID](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches#Batch.FIELDS.uuid) or the [session UUID](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessions#Session.FIELDS.uuid).
  * Profiler supports the following Spark workload types: `Spark`, `PySpark`, `SparkSql`, and `SparkR`.
  * A workload must run for more than three minutes to allow Profiler to collect and upload data to a project.
  * You can override profiling options submitted with a workload by constructing a `SparkConf`, and then setting `extraJavaOptions` in your code. Note that setting `extraJavaOptions` properties when the workload is submitted doesn't override profiling options submitted with the workload.



For an example of profiler options used with a batch submission, see the PySpark batch workload example.

## Enable profiling

Complete the following steps to enable profiling on a workload:

  1. [Enable the Profiler](https://docs.cloud.google.com/profiler/docs/profiling-java#enabling-profiler).
  2. If you are using a [custom VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account), grant the [Cloud Profiler Agent](https://docs.cloud.google.com/profiler/docs/iam#cloudprofiler.agent) role to the custom VM service account. This role contains required Profiler permissions.
  3. Set profiling properties when you [submit a batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch#submit_a_spark_batch_workload) or [create a session template](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions#create_a_serverless_runtime_template).



### PySpark batch workload example

The following example uses the gcloud CLI to submit a PySpark batch workload with profiling enabled.
    
    
    gcloud dataproc batches submit pyspark PYTHON_WORKLOAD_FILE \
        --region=REGION \
        --properties=dataproc.profiling.enabled=true,dataproc.profiling.name=PROFILE_NAME \
        --  other args
    

Two profiles are created:

  * `PROFILE_NAME-driver` to profile spark driver tasks
  * `PROFILE_NAME-executor` to profile spark executor tasks



## View profiles

You can view profiles from [Profiler](https://console.cloud.google.com/profiler) in the Google Cloud console.

## What's next

  * See [Monitor and troubleshoot Managed Service for Apache Spark workloads](https://docs.cloud.google.com/managed-spark/docs/guides/monitor-troubleshoot-batches).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
