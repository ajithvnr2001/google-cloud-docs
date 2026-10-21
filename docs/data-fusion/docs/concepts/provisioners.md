---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/provisioners/
title: Provisioners in Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:19.195743+00:00
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

Provisioners let you automate cluster lifecycle management when running pipelines across different cloud environments. They create the required compute cluster before a run begins and tear it down after the pipeline finishes.

Each provisioner provides configuration settings to control cluster properties and authenticate with target cloud platforms. For example, provisioners for Managed Service for Apache Spark and Amazon EMR configure cluster size and the credentials required to provision compute nodes.

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

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
