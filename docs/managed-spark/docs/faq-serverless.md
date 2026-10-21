---
url: https://docs.cloud.google.com/managed-spark/docs/faq-serverless/
title: Managed Service for Apache Spark serverless FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:51.790876+00:00
---

# Managed Service for Apache Spark serverless FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/faq-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-spark/docs/resources)



Send feedback 

#  Managed Service for Apache Spark serverless FAQ Stay organized with collections  Save and categorize content based on your preferences. 

This page contains frequently asked Managed Service for Apache Spark serverless deployment questions with answers. Unless otherwise stated, this information applies only to Managed Service for Apache Spark serverless, not cluster, deployments.

### When should I use Managed Service for Apache Spark serverless deployment instead of Managed Service for Apache Spark cluster deployment?

  * Managed Service for Apache Spark serverless deployment:

    * Supports Spark batch workloads and interactive sessions in PySpark kernel Jupyter notebooks.
    * Creates and manages your workload and interactive session infrastructure.
  * Managed Service for Apache Spark cluster deployment:

    * Supports the submission of different types Spark jobs, and jobs based on other open source components, such as Flink, Hadoop, Hive, Pig, Presto, and others.

    * Does not create and manage infrastructure. You create and manage your Managed Service for Apache Spark clusters.




### What can I do with Managed Service for Apache Spark serverless deployment?

  * [Run batch jobs](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch).

  * [Use the Managed Service for Apache Spark JupyterLab plugin for serverless batch and interactive notebook sessions](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions).

  * Run streaming jobs using Spark streaming libraries. Note: Streaming is not a managed service, so you must manage checkpointing and restarts.

  * Train models using Spark MLlib.

  * Use interactive SQL notebooks for data exploration, graph, time series, and geospatial analytics.

  * Orchestrate Managed Service for Apache Spark workloads with Managed Service for Apache Airflow, a managed Apache Airflow service.




### How should I set up a workload execution plan?

You can run workloads concurrently or sequentially. Your execution plan impacts your Google Cloud resource quota. You can run as many workloads in parallel as your [batch resource](https://docs.cloud.google.com/managed-spark/quotas#default_batch_resources) quotas allow.

## Can I use a custom image with Managed Service for Apache Spark serverless deployment?

  * Yes. You can use a custom container image instead of the default container image. See [Use custom containers with Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers).



## Can I specify memory and disk resources for Managed Service for Apache Spark workloads?

Yes. You can specify premium executor and driver compute and disk tiers and the amount of driver and executor compute and disk resources to allocate when you submit a workload (see [Resource allocation properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties)).

## How can I specify the IP address range for my Managed Service for Apache Spark VPC network?

Managed Service for Apache Spark workloads run within your environment. Each Spark driver and Spark executor in a Serverless Spark workload consumes one internal IP address in your [Managed Service for Apache Spark VPC network](https://docs.cloud.google.com/managed-spark/docs/concepts/network). `/16` is a typical user-specified [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) address range for a [Managed Service for Apache Spark VPC network](https://docs.cloud.google.com/managed-spark/docs/concepts/network). You can limit your network's IP address range based on the number of concurrent workloads you plan to run.

## Does Managed Service for Apache Spark support data residency?

Yes. You specify the region where your workload is processed. Locate you input and output datasets in the specified region.

## How does Managed Service for Apache Spark select a zone within your specified region to run the workload?

Managed Service for Apache Spark selects the Compute Engine zone where it executes a workload based on capacity and availability. If a zone becomes unavailable after a workload starts, the workload fails, and you must resubmit the failed workload.

## How do Managed Service for Apache Spark workloads use compute resources?

Each workload executes on its own compute resources. Multiple batch submissions don't share or reuse compute resources.

**Best Practices:**

  * Optimize your workload for medium-running jobs, not short-running jobs.

  * Persist data that is accessed by multiple workloads in Cloud Storage.




## Where can I find information on Managed Service for Apache Spark announcements, features, bug fixes, known issues, and deprecations?

See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes).

## Do concurrent workloads compete for resources?

Managed Service for Apache Spark workloads only compete for resources if your resource quota is insufficient to run all concurrently running workloads. Otherwise, workloads are fully isolated from each other.

## How is Managed Service for Apache Spark quota allocated?

Managed Service for Apache Spark batches consume Google Cloud resources. See [Dataproc Serverless quotas](https://docs.cloud.google.com/managed-spark/quotas) for more information.

## Do I need to set up a Managed Service for Apache Spark Persistent History Server?

Setting up a [Persistent History Server (PHS)](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/history-server) to use with Managed Service for Apache Spark is optional.You can use the PHS to view Spark event and other logs in a specified Cloud Storage bucket up to and after the standard [Managed Service for Apache Spark staging and temp bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/buckets) 90-day retention (TTL) period.

**Note:** The PHS must be located in the region where you run batch workloads. 

## What Managed Service for Apache Spark logs are available?

Spark executors and driver logs are available in Cloud Logging during and after Spark workload execution. Also, Spark applications are visible in the [Persistent History Server (PHS)](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/history-server) web interface while the workload is running (select **PHS** > **Incomplete Applications** in the PHS UI).

If you set up a Managed Service for Apache Spark PHS, it provides persistent access to Spark event logs saved in Cloud Storage, which provide insight into Spark app execution, such DAG and executor events.

**Note:** The PHS must be located in the region where you run batch workloads. 

## Can I set the number of executors for my Spark workload?

Yes. You can set the number of executors for a Spark workload using the [`spark.executor.instances`](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties) property. However, the total number of cores that a workload can use is more important than the number of executors because Spark runs 1 task per core. For example, if a workload has four executors with two cores each, it will run `4 * 2 = 8` tasks at the same time. And it will also run the same number of tasks for a workload that has two executors with four cores each. Since the number of cores for each workload is the same, they will run the same number of tasks. You can use the [`spark.executor.cores`](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties) property to set the number cores per executor for your Managed Service for Apache Spark workload.

## What Spark metrics does Managed Service for Apache Spark use for autoscaling?

Managed Service for Apache Spark looks at the `maximum-needed` and `running` Spark's dynamic allocation metrics to determine whether to scale up or down. See [Managed Service for Apache Spark autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling).

## Can I configure Managed Service for Apache Spark autoscaling behavior using Spark properties?

Yes. Managed Service for Apache Spark autoscaling is based on Spark dynamic allocation, and is enabled by default. You can adjust the following [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#supported_spark_properties) and [Spark dynamic allocation properties](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling#spark_dynamic_allocation_properties):

  * `spark.executor.instances`
  * `spark.dynamicAllocation.initialExecutors`
  * `spark.dynamicAllocation.minExecutors`
  * `spark.dynamicAllocation.maxExecutors`



## Why do I need to package my code in a JAR file to submit my Spark workload?

Spark is written in Scala, which means that both the driver and the worker processes operate as JVM processes. In JVM languages, the JAR file is the primary way to package code. You pass the JAR file to Managed Service for Apache Spark when you submit a workload.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
