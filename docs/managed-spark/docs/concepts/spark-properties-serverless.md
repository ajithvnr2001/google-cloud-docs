---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/spark-properties-serverless/
title: Spark properties \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:40.073241+00:00
---

# Spark properties  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/spark-properties-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Spark properties Stay organized with collections  Save and categorize content based on your preferences. 

This document describes Spark properties and how to set them. Managed Service for Apache Spark uses Spark properties to determine the compute, memory, and disk resources to allocate to your batch workload. These property settings can affect workload quota consumption and cost. For more information, see [Managed Service for Apache Spark quotas](https://docs.cloud.google.com/managed-spark/quotas) and [Managed Service for Apache Spark pricing](https://cloud.google.com/products/managed-service-for-apache-spark/pricing).

**Note:** Also see [Spark metrics](https://docs.cloud.google.com/managed-spark/docs/concepts/metrics), which describes properties you can set to control the collection of Spark metrics.

## Set Spark batch workload properties

You can specify Spark properties when you [submit a Managed Service for Apache Spark batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch#submit_a_spark_batch_workload) using the Google Cloud console, gcloud CLI, or the Dataproc API.

**Note:** Unlike Managed Service for Apache Spark Spark configuration [cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#examples), Managed Service for Apache Spark workload properties don't require a leading "spark:" file prefix.

### Console

  1. In the Google Cloud console, go to the **Managed Service for Apache Spark create batch** page.

[Go to Managed Service for Apache Spark Create batch](https://console.cloud.google.com/dataproc/batches)

  2. In the **Properties** section, click **Add Property**.

  3. Enter the `Key` (name) and `Value` of a supported Spark property.




### gcloud

The following is a gcloud CLI batch submission example. Multiple [properties](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--properties) are separated with commas.
    
    
    gcloud dataproc batches submit spark \
        --properties=spark.checkpoint.compress=true,spark.driver.cores=8  \
        --region=REGION \
        other args ...
    

### API

Set [RuntimeConfig.properties](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/projects.locations.batches#RuntimeConfig.FIELDS.properties) with supported Spark properties as part of a [batches.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches/create) request.

## Supported Spark properties

Managed Service for Apache Spark supports most Spark properties, but it does not support YARN-related and shuffle-related Spark properties, such as `spark.master=yarn` and `spark.shuffle.service.enabled`. If Spark application code sets a YARN or shuffle property, the application will fail.

### Runtime environment properties

Managed Service for Apache Spark supports the following custom Spark properties for configuring runtime environment:

Property | Description  
---|---  
`spark.dataproc.driverEnv.ENVIRONMENT_VARIABLE_NAME` | Add ENVIRONMENT_VARIABLE_NAME to the driver process. You can specify multiple environment variables.  
`spark.executorEnv.ENVIRONMENT_VARIABLE_NAME` | Add ENVIRONMENT_VARIABLE_NAME to the executor process. You can specify multiple environment variables.  
  
#### Tier property

Property | Description | Default  
---|---|---  
`dataproc.tier` |  The tier on which a batch workload runs, either `standard` or `premium` (see [Managed Service for Apache Spark tiers](https://docs.cloud.google.com/managed-spark/docs/tiers)) Interactive sessions always run at the premium `dataproc.tier`. 

  * Setting this batch tier property to `standard` sets Managed Service for Apache Spark runtime and resource tier properties to the `standard` tier (see [resource allocation properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties)). 
  * Setting this batch tier property to `premium` sets `spark.dataproc.engine` to `lightningEngine`, and sets `spark.dataproc.driver.compute.tier` and `spark.dataproc.executor.compute.tier` to `premium`. You can override most automatically set batch tier settings, but the automatically set **compute** tier settings can't be overridden for batches using runtimes prior to `3.0` (see [resource allocation properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties)).

| `standard`  
  
#### Engine and runtime properties

Property | Description | Default  
---|---|---  
`spark.dataproc.engine` |  The engine to use to run the batch workload or the interactive session: either `lightningEngine` (see [Lightning Engine](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine)) or the `default` engine. 

  * **Batch workloads:** If you select the standard `dataproc.tier` property for your workload, this property is automatically set to `default` and cannot be overridden. If you select the `premium` `dataproc.tier` for your workload, this property is automatically set to `lightningEngine`, but you can change the setting to `default` if needed.
  * **Interactive sessions:** This setting is automatically set to `default`, but you can change this setting to `lightningEngine`. Note that interactive session always run at the `premium` tier.

| 

  * Batches (standard tier): `default`
  * Batches (premium tier): `lightningEngine`
  * Sessions: `default`

  
`spark.dataproc.lightningEngine.runtime` |  The runtime to use when Lightning Engine is selected for a batch workload or interactive session: `default` or `native` ([Native Query Execution](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine#native_query_execution)).  | `default`  
  
### Resource allocation properties

**Note:** Since Spark resource allocation properties must be fully configured before workload executions starts, set Spark resource allocation properties when you [submit a batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch#submit_a_spark_batch_workload) or create a [session or session template](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates), not on the `SparkContext`/`SparkSession` during workload execution.

Managed Service for Apache Spark supports the following Spark properties for configuring resource allocation:

Property | Description | Default | Examples  
---|---|---|---  
`spark.driver.cores` | The number of cores (vCPUs) to allocate to the Spark driver. Valid values: `4`, `8`, `16`. | `4` |   
`spark.driver.memory` | The amount of memory to allocate to the Spark driver process, specified in JVM memory string format with a size unit suffix ("m", "g" or "t"). Total driver memory per driver core, including driver memory overhead, which must be between `1024m` and `7424m` for the Standard compute tier (`24576m` for the Premium compute tier). For example, if `spark.driver.cores = 4`, then `4096m <= spark.driver.memory + spark.driver.memoryOverhead <= 29696m`. |  | `512m`, `2g`  
`spark.driver.memoryOverhead` | The amount of additional JVM memory to allocate to the Spark driver process, specified in JVM memory string format with a size unit suffix ("m", "g" or "t"). This is non-heap memory associated with JVM overheads, internal strings, and other native overheads, and includes memory used by other driver processes, such as PySpark driver processes and memory used by other non-driver processes running in the container. The maximum memory size of the container in which the driver runs is determined by the sum of `spark.driver.memoryOverhead` plus `spark.driver.memory`. Total driver memory per driver core, including driver memory overhead, must be between `1024m` and `7424m` for the Standard compute tier (`24576m` for the Premium compute tier). For example, if `spark.driver.cores = 4`, then `4096m <= spark.driver.memory + spark.driver.memoryOverhead <= 29696m`. | 10% of driver memory, except for PySpark batch workloads, which default to 40% of driver memory | `512m`, `2g`  
`spark.dataproc.driver.compute.tier` | The compute tier to use on the driver. The Premium compute tier offers higher per-core performance, but it is billed at a higher rate. | standard | standard, premium  
`spark.dataproc.driver.disk.size` | The amount of disk space allocated to the driver, specified with a size unit suffix ("k", "m", "g" or "t"). Must be at least `250GiB`. If the Premium disk tier is selected on the driver, valid sizes are 375g, 750g, 1500g, 3000g, 6000g, or 9000g. If the Premium disk tier and 16 driver cores are selected, the minimum disk size is 750g. | `100GiB` per core | `1024g`, `2t`  
`spark.dataproc.driver.disk.tier` | The disk tier to use for local and shuffle storage on the driver. The Premium disk tier offers better performance in IOPS and throughput, but it is billed at a higher rate. If the Premium disk tier is selected on the driver, the Premium compute tier also must be selected using `spark.dataproc.driver.compute.tier=premium`, and the amount of disk space must be specified using `spark.dataproc.executor.disk.size`. If the Premium disk tier is selected, the driver allocates an additional 50GiB of disk space for system storage, which is not usable by user applications. | standard | standard, premium  
`spark.executor.cores` | The number of cores (vCPUs) to allocate to each Spark executor. Valid values: `4`, `8`, `16`. | `4` |   
`spark.executor.memory` | The amount of memory to to allocate to each Spark executor process, specified in JVM memory string format with a size unit suffix ("m", "g" or "t"). Total executor memory per executor core, including executor memory overhead, must be between `1024m` and `7424m` for the Standard compute tier (`24576m` for the Premium compute tier). For example, if `spark.executor.cores = 4`, then `4096m <= spark.executor.memory + spark.executor.memoryOverhead <= 29696m`. |  | `512m`, `2g`  
`spark.executor.memoryOverhead` |  The amount of additional JVM memory to allocate to the Spark executor process, specified in JVM memory string format with a size unit suffix ("m", "g" or "t"). This is non-heap memory used for JVM overheads, internal strings, and other native overheads, and includes PySpark executor memory and memory used by other non-executor processes running in the container. The maximum memory size of the container in which the executor runs is determined by the sum of `spark.executor.memoryOverhead` plus `spark.executor.memory`. Total executor memory per executor core, including executor memory overhead, must be between `1024m` and `7424m` for the Standard compute tier (`24576m` for the Premium compute tier). For example, if `spark.executor.cores = 4`, then `4096m <= spark.executor.memory + spark.executor.memoryOverhead <= 29696m`. | 10% of executor memory, except for PySpark batch workloads, which default to 40% of executor memory | `512m`, `2g`  
`spark.dataproc.executor.compute.tier` | The compute tier to use on the executors. The Premium compute tier offers higher per-core performance, but it is billed at a higher rate. | standard | standard, premium  
`spark.dataproc.executor.disk.size` | The amount of disk space allocated to each executor, specified with a size unit suffix ("k", "m", "g" or "t"). Executor disk space may be used for shuffle data and to stage dependencies. Must be at least `250GiB`. If the Premium disk tier is selected on the executor, valid sizes are 375g, 750g, 1500g, 3000g, 6000g, or 9000g. If the Premium disk tier and 16 executor cores are selected, the minimum disk size is 750g. | `100GiB` per core | `1024g`, `2t`  
`spark.dataproc.executor.disk.tier` | The disk tier to use for local and shuffle storage on executors. The Premium disk tier offers better performance in IOPS and throughput, but it is billed at a higher rate. If the Premium disk tier is selected on the executor, the Premium compute tier also must be selected using `spark.dataproc.executor.compute.tier=premium`, and the amount of disk space must be specified using `spark.dataproc.executor.disk.size`. If the Premium disk tier is selected, each executor is allocated an additional 50GiB of disk space for system storage, which is not usable by user applications. | standard | standard, premium  
`spark.executor.instances` | The initial number of executors to allocate. After a batch workload starts, autoscaling may change the number of active executors. Must be at least `2` and at most `2000`. |  |   
  
### Autoscaling properties

See [Spark dynamic allocation properties](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling#spark_dynamic_allocation_properties) for a list of Spark properties you can use to configure Managed Service for Apache Spark autoscaling.

### Logging properties

Property | Description | Default | Examples  
---|---|---|---  
`spark.log.level` | When set, overrides any user-defined log settings with the effect of a call to `SparkContext.setLogLevel()` at Spark startup. Valid log levels include: `ALL`, `DEBUG`, `ERROR`, `FATAL`, `INFO`, `OFF`, `TRACE`, and `WARN`. |  | `INFO`, `DEBUG`  
`spark.executor.syncLogLevel.enabled` | When set to `true`, the log level applied through the `SparkContext.setLogLevel()` method is propagated to all executors. | `false` | `true`, `false`  
`spark.log.level.PackageName` | When set, overrides any user-defined log settings with the effect of a call to `SparkContext.setLogLevel(PackageName, level)` at Spark startup. Valid log levels include: `ALL`, `DEBUG`, `ERROR`, `FATAL`, `INFO`, `OFF`, `TRACE`, and `WARN`. |  | `spark.log.level.org.apache.spark=error`  
  
### Scheduling properties

Property | Description | Default | Examples  
---|---|---|---  
`spark.scheduler.excludeShuffleSkewExecutors` | Exclude shuffle map skewed executors when scheduling, which can reduce long shuffle fetch wait times caused by shuffle write skew. | `false` | `true`  
`spark.scheduler.shuffleSkew.minFinishedTasks` | Minimum number of finished shuffle map tasks on an executor to treat as skew. | `10` | `100`  
`spark.scheduler.shuffleSkew.maxExecutorsNumber` | Maximum number of executors to treat as skew. Skewed executors are excluded from the current scheduling round. | 5 | `10`  
`spark.scheduler.shuffleSkew.maxExecutorsRatio` | Maximum ratio of total executors to treat as skew. Skewed executors are excluded from scheduling. | 0.05 | `0.1`  
`spark.scheduler.shuffleSkew.ratio` | A multiple of the average finished shuffle map tasks on an executor to treat as skew. | 1.5 | `2.0`  
  
### Other properties

Property | Description  
---|---  
`dataproc.diagnostics.enabled` | **Supported in 2.3 and earlier runtimes only**. Enable this property to run diagnostics on a batch workload failure or cancellation. If diagnostics are enabled, your batch workload continues to use [ compute resources](https://docs.cloud.google.com/managed-spark/quotas#default_batch_resources) after the workload is complete until diagnostics are finished. A URI pointing to the location of the diagnostics tar file is listed in the [Batch.RuntimeInfo.diagnosticOutputUri](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeInfo#FIELDS.diagnostic_output_uri) API field.  
`dataproc.gcsConnector.version` | **Supported in 2.3 and earlier runtimes only**. Use this property to upgrade to a [Cloud Storage connector version](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases) that is different from the version installed with your batch workload's [runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-versions).  
`dataproc.sparkBqConnector.version` | **Supported in 2.3 and earlier runtimes only**. Use this property to upgrade to a [Spark BigQuery connector version](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) that is different from the version installed with your batch workload's [runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-versions) (see [Use the BigQuery connector with Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/guides/bigquery-connector-spark-example)).  
`dataproc.profiling.enabled` | **Supported in 2.3 and earlier runtimes only**. Set this property to `true` to enable profiling for the Managed Service for Apache Spark workload.  
`dataproc.profiling.name` | **Supported in 2.3 and earlier runtimes only** Use this property to set the name used to create a profile on the [Profiler](https://docs.cloud.google.com/profiler/docs/about-profiler) service.  
`spark.jars` | Use this property to set the comma-separated list of jars to include on the driver and executor classpaths  
`spark.archives` | Use this property to set the comma-separated list of archives to be extracted into the working directory of each executor. .jar, .tar.gz, .tgz and .zip are supported. For serverless interactive sessions add this property when creating an interactive session/template  
`dataproc.artifacts.remove` | Use this property to remove default artifacts installed on [Managed Service for Apache Spark runtimes](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions). Supported artifacts are `conscrypt`, `delta-lake`, `iceberg`, `rapids`, and `spark-bigquery-connector`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
