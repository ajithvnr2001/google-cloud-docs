---
url: https://docs.cloud.google.com/managed-spark/docs/guides/profiling/
title: Cloud Profiler \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:40.215467+00:00
---

# Cloud Profiler  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/profiling/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Cloud Profiler Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Profiler](https://docs.cloud.google.com/profiler/docs) continuously gathers and reports application CPU usage and memory-allocation information.

**Requirements:**

  * Profiler supports only Managed Service for Apache Spark Hadoop and Spark job types (Spark, PySpark, SparkSql, and SparkR).

  * Jobs must run longer than 3 minutes to allow Profiler to collect and upload data to your project.




Managed Service for Apache Spark recognizes `cloud.profiler.enable` and the other `cloud.profiler.*` properties (see Profiler options), and then appends the relevant profiler JVM options to the following configurations:

  * Spark: `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions`
  * MapReduce: `mapreduce.task.profile` and other `mapreduce.task.profile.*` properties

**Note:** Overriding Spark or MapReduce properties in your job (for example, by manually constructing a SparkConf and setting `spark.executor.extraJavaOptions`), prevents the setting of profiler options. However, if you provide `extraJavaOptions` using the `gcloud dataproc jobs submit (spark|hadoop) --properties` flag, Managed Service for Apache Spark retains and sets profiler options.

## Enable profiling

Complete the following steps to enable and use the Profiler on your Managed Service for Apache Spark and Hadoop jobs.

  1. [Enable the Profiler](https://docs.cloud.google.com/profiler/docs/profiling-java#enabling-profiler).

  2. [Create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster) with [service account scopes](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--scopes) set to `monitoring` to allow the cluster to talk to the profiler service.

  3. If you are using a [custom VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#create_a_cluster_with_a_custom_vm_service_account), grant the [Cloud Profiler Agent](https://docs.cloud.google.com/profiler/docs/iam#cloudprofiler.agent) role to the custom VM service account. This role contains required profiler service permissions.




### gcloud
    
    
    gcloud dataproc clusters create cluster-name \
        --scopes=cloud-platform \
        --region=region \
        other args ...
    

## Submit a Managed Service for Apache Spark job with Profiler options

  1. [Submit a Spark or Hadoop job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#submitting_a_job) with one or more of the following Profiler options: Option | Description | Value | Required/Optional | Default | Notes  
---|---|---|---|---|---  
`cloud.profiler.enable` | Enable profiling of the job | `true` or `false` | Required | `false` |   
`cloud.profiler.name` | Name used to create profile on the Profiler Service | profile-name | Optional | Managed Service for Apache Spark job UUID |   
`cloud.profiler.service.version` | A user-supplied string to identify and distinguish profiler results. | Profiler Service Version | Optional | Managed Service for Apache Spark job UUID |   
`mapreduce.task.profile.maps` | Numeric range of map tasks to profile (example: for up to 100, specify "0-100")  | number range | Optional | 0-10000 | Applies to Hadoop mapreduce jobs only  
`mapreduce.task.profile.reduces` | Numeric range of reducer tasks to profile (example: for up to 100, specify "0-100") | number range | Optional | 0-10000 | Applies to Hadoop mapreduce jobs only  



### PySpark Example

### Google Cloud CLI

PySpark job submit with profiling example:
    
    
    gcloud dataproc jobs submit pyspark python-job-file \
        --cluster=cluster-name \
        --region=region \
        --properties=cloud.profiler.enable=true,cloud.profiler.name=profiler_name,cloud.profiler.service.version=version \
        --  job args
    

Two profiles will be created:

  1. `profiler_name-driver` to profile spark driver tasks
  2. `profiler_name-executor` to profile spark executor tasks



For example, if the `profiler_name` is "spark_word_count_job", `spark_word_count_job-driver` and `spark_word_count_job-executor` profiles are created.

### Hadoop Example

### gcloud CLI

Hadoop (teragen mapreduce) job submit with profiling example:
    
    
    gcloud dataproc jobs submit hadoop \
        --cluster=cluster-name \
        --region=region \
        --jar=jar-file \
        --properties=cloud.profiler.enable=true,cloud.profiler.name=profiler_name,cloud.profiler.service.version=version \
        --  teragen 100000 gs://bucket-name
    

## View profiles

View profiles from the [Profiler](https://console.cloud.google.com/profiler) on the Google Cloud console.

## Whats next

  * See the [Monitoring documentation](https://docs.cloud.google.com/monitoring/docs)
  * See the [Logging documentation](https://docs.cloud.google.com/logging/docs)
  * Explore [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
