---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/manage-pipeline-configurations/
title: Manage pipeline configurations \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:18.576036+00:00
---

# Manage pipeline configurations  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/manage-pipeline-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage pipeline configurations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes ways you can manage configurations for deployed pipelines.

## Before you begin

This page requires some background knowledge about [Compute profiles](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-compute-profiles) and [pipeline performance](https://docs.cloud.google.com/data-fusion/docs/concepts/performance-tuning-overview).

## Compute profile configuration

You can change the compute profile or customize the parameters of the default compute profile that runs the pipeline. For more information, see [Manage compute profiles](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-compute-profiles) and [Managed Service for Apache Spark provisioner properties](https://docs.cloud.google.com/data-fusion/docs/concepts/dataproc).

## Pipeline configuration

For each pipeline, you can enable or disable instrumentation, such as timing metrics. By default, instrumentation is on. If instrumentation is enabled, when you run the pipeline, Cloud Data Fusion generates metrics for each pipeline node. The following metrics display on the **Metrics** tab of each node. The source, transformation, and sink metrics vary slightly.

  * Records out
  * Records in
  * Total number of errors
  * Records out per second
  * Min process time (one record)
  * Max process time (one record)
  * Standard deviation
  * Average processing time



We recommend you always turn on Instrumentation, unless the environment is short on resources.

For streaming pipelines, you can also set the **Batch interval** (seconds/minutes) for streaming data.

## Engine configuration

Apache Spark is the default execution engine. You can pass custom parameters for Spark. For more information, see [Parallel processing](https://docs.cloud.google.com/data-fusion/docs/concepts/parallel-processing).

## Resources

You can specify the memory and number of CPUs for the Spark driver and executor. The driver orchestrates the Spark job. The executor handles the data processing in Spark. For more information, see [Resource management](https://docs.cloud.google.com/data-fusion/docs/concepts/resource-management).

## Pipeline alert

You can configure the pipeline to send alerts and start post processing tasks after the pipeline run finishes. You create pipeline alerts when you design the pipeline. After you deploy the pipeline, you can view the alerts. You can edit the pipeline to change alert settings. For more information, see [Create alerts](https://docs.cloud.google.com/data-fusion/docs/how-to/create-alerts).

## Transformation pushdown

You can enable Transformation pushdown if you want a pipeline to execute certain transformations in BigQuery. For more information, see the [Transformation Pushdown overview](https://docs.cloud.google.com/data-fusion/docs/concepts/transformation-pushdown).

## What's next

  * Learn more about [viewing and downloading pipeline logs in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/how-to/view-and-download-pipeline-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
