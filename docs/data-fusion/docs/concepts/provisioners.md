---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/provisioners/
title: Provisioners in Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:31.494582+00:00
---

# Provisioners in Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/provisioners/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Provisioners in Cloud Data Fusion Stay organized with collections  Save and categorize content based on your preferences. 

A provisioner is responsible for creating and tearing down the cloud cluster where the pipeline is executed. Different provisioners are capable of creating different types of clusters on various clouds.

Each provisioner exposes a set of configuration settings that control the type of cluster that's created for a run. For example, the Managed Service for Apache Spark and Amazon EMR provisioners have cluster size settings. Provisioners also have settings for the credentials required to talk to their respective clouds and provision the required compute nodes.

## Supported provisioners in Cloud Data Fusion

Cloud Data Fusion supports the following provisioners:

[Managed Service for Apache Spark](https://docs.cloud.google.com/data-fusion/docs/concepts/dataproc)
    A fast, easy-to-use, and fully-managed cloud service for running Apache Spark and Apache Hadoop clusters.
Amazon Elastic MapReduce (EMR)
    Provides a managed Hadoop framework that processes vast amounts of data across dynamically scalable Amazon EC2 instances.
Remote Hadoop
    Runs jobs on a pre-existing Hadoop cluster, either on-premises or in the cloud.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
