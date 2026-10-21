---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions/
title: Managed Service for Apache Spark serverless runtime versions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:42.551299+00:00
---

# Managed Service for Apache Spark serverless runtime versions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark serverless runtime versions Stay organized with collections  Save and categorize content based on your preferences. 

This document lists supported and unsupported Managed Service for Apache Spark runtime versions and describes their characteristics.

**Note:** Weekly Managed Service for Apache Spark releases are fully backward compatible and may include subminor version upgrades of Spark, Java libraries, and Python packages.

## Runtime node location

This section describes how Managed Service for Apache Spark runtime versions allocate nodes within a region to execute batch workloads and interactive sessions.

  * **Runtime versions`3.0+`**: To help with obtainability and avoid zonal stockouts, Managed Service for Apache Spark might allocate nodes to execute a batch workload or interactive session in multiple zones within the workload or session region. There is no additional cost for cross-zonal network traffic between nodes in a region.

**Runtimes versions prior to`3.0`**, Managed Service for Apache Spark allocates nodes to execute a batch workload or interactive session in a single zone within the workload or session region.




## Runtime availability and support

  * Managed Service for Apache Spark LTS (Long-Time-Support) runtime versions are supported for 30 months. Managed Service for Apache Spark non-LTS runtime versions are supported for 12 months.

  * Managed Service for Apache Spark runtime versions continue to be available for two years after their end-of-support date.

  * Runtime subminor version pinning is not supported.




## Supported Managed Service for Apache Spark runtime versions

Version | Last updated | Released on | Supported until | Available until | Notes  
---|---|---|---|---|---  
[Spark runtime 3.0](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-3.0) | [2026/08/25](https://docs.cloud.google.com/managed-spark/docs/release-notes#August_25_2026) | [2025/12/04](https://docs.cloud.google.com/dataproc/docs/release-notes#December_04_2025) | 2027/01/31 | 2029/01/31 | General Availability release  
[Spark runtime 2.3 LTS](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-2.3) | [2026/09/23](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_23_2026) | [2025/05/28](https://docs.cloud.google.com/dataproc/docs/release-notes#May_28_2025) | 2027/11/26 | 2029/11/26 | General Availability release  
[Spark runtime 2.2 LTS](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-2.2) | [2026/09/23](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_23_2026) | [2024/03/27](https://docs.cloud.google.com/dataproc/docs/release-notes#December_06_2023) | 2027/03/31 | 2029/03/31 | General Availability release. This is the **default version**.  
[Spark runtime 1.2 LTS](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-1.2) | [2026/09/23](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_23_2026) | [2024/03/27](https://docs.cloud.google.com/dataproc/docs/release-notes#March_20_2024) | 2027/03/31 | 2029/03/31 | General Availability release  
  
### How to choose a Managed Service for Apache Spark runtime version

The current default Managed Service for Apache Spark runtime version is listed in Supported Managed Service for Apache Spark runtime versions. You can choose a different `major.minor` runtime version when you [submit a batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch#submit_a_spark_batch_workload) or [create a interactive session](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates#create-an-interactive-session) or [session template](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates#create-a-session-template).

## Unsupported Managed Service for Apache Spark runtime versions

The following Managed Service for Apache Spark versions are unsupported.

Version | Includes | Released On | Last Updated | Available Until | Notes  
---|---|---|---|---|---  
Spark runtime 2.1 | Apache Spark 3.4.0  
Cloud Storage connector 2.2.20  
BigQuery connector 0.28.1  
Java 17  
Conda 23.3  
Python 3.11  
R 4.2  
Scala 2.13 | [2022/01/19](https://docs.cloud.google.com/dataproc/docs/release-notes#January_19_2022) | 2024/5/30 | 2027/03/31 | Unsupported as of 2024/05/30. 2.1.50 was the final released version.  
Spark runtime 2.0 | Apache Spark 3.3.4  
Cloud Storage connector 2.2.20  
Java 17  
Conda 22.9  
Python 3.10  
R 4.1  
Scala 2.13 | [2022/10/21](https://docs.cloud.google.com/dataproc/docs/release-notes#August_22_2022) | 2024/08/22 | 2027/03/31 | Unsupported as of 2024/08/22. 2.0.85 was the final released version.  
Spark runtime 1.1 | Apache Spark 3.3.4  
Cloud Storage connector 2.2.28  
BigQuery connector 0.28.1  
Java 11  
Conda 22.11  
Python 3.10  
R 4.2  
Scala 2.12 | [2023/01/27](https://docs.cloud.google.com/dataproc/docs/release-notes#January_27_2023) | 2025/07/31 | 2027/07/31 | Unsupported as of 2025/07/31. 1.1.111 was the final released version.  
Spark runtime 1.0 | Apache Spark 3.2.3  
Cloud Storage connector 2.2.11  
Conda 4.11  
Java 11  
Python 3.9  
R 4.1  
Scala 2.12.17 | [2022/01/19](https://docs.cloud.google.com/dataproc/docs/release-notes#January_19_2022) | 2023/2/03 | 2025/05/30 | Unsupported as of 2023/02/03. 1.0.29 was the final released version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
