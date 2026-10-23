---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/hdfs/
title: Hadoop data storage \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:24.245257+00:00
---

# Hadoop data storage  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/hdfs/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Hadoop data storage Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark integrates with Apache Hadoop and the Hadoop Distributed File System (HDFS). The following features and considerations can be important when selecting compute and data storage options for Managed Service for Apache Spark clusters and jobs:

  * HDFS with Cloud Storage: Managed Service for Apache Spark uses the Hadoop Distributed File System (HDFS) for storage. Additionally, Managed Service for Apache Spark automatically installs the HDFS-compatible [Cloud Storage connector](https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/cloud-storage), which enables the use of Cloud Storage in parallel with HDFS. Data can be moved in and out of a cluster through upload and download to HDFS or Cloud Storage.
  * VM disks: 
    * By default, when no local SSDs are provided, HDFS data and intermediate shuffle data is stored on VM boot disks, which are [Persistent Disks](https://cloud.google.com/persistent-disk/).
    * If you use [local SSDs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/dataproc-local-ssds), HDFS data and intermediate shuffle data is stored on the SSDs.
    * Persistent disk (PD) size and type affect performance and VM size, whether using HDFS or Cloud Storage for data storage.
    * **VM Boot disks are deleted when the cluster is deleted.**



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
