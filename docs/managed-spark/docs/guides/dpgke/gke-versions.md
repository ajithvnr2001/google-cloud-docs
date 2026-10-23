---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-versions/
title: Managed Service for Apache Spark on GKE release versions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:10.473339+00:00
---

# Managed Service for Apache Spark on GKE release versions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-versions/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark on GKE release versions Stay organized with collections  Save and categorize content based on your preferences. 

## Spark Engine 3.5

Component | 3.5-dataproc-28 | 3.5-dataproc-22 (Deprecated) | 3.5-dataproc-17 (Deprecated)  
---|---|---|---  
Apache Spark | 3.5.1 | 3.5.0 | 3.5.0  
Hadoop Libraries | 3.3.6 | 3.3.6 | 3.3.6  
Cloud Storage Connector | 3.0.0 | 3.0.0 | 3.0.0  
Java | 11 | 11 | 11  
Python | 3.8.5 | 3.8.5 | 3.8.5  
Conda | - | 4.9.2 | 4.9.2  
R | 4.3.0 | 4.3.0 | 4.3.0  
  
## Spark Engine 3.1(Deprecated)

Component | 3.1-dataproc-17 | 3.1-dataproc-16 | 3.1-dataproc-15 | 3.1-dataproc-14  
---|---|---|---|---  
Apache Spark | 3.1.3 | 3.1.3 | 3.1.3 | 3.1.3  
Hadoop Libraries | 3.2.3 | 3.2.3 | 3.2.3 | 3.2.3  
Cloud Storage Connector | hadoop3-2.2.13 | hadoop3-2.2.13 | hadoop3-2.2.11 | hadoop3-2.2.11  
Java | 8 | 8 | 8 | 8  
Python | 3.8.5 | 3.8.5 | 3.8.5 | 3.8.5  
Conda | 4.9.2 | 23.5.0 | 4.9.2 | 4.9.2  
R | 4.3.0 | 4.3.0 | 4.2.3 | 4.2.3  
  
## Spark Engine 2.4(Deprecated)

Spark 2.4 has reached EOL for support in DPGKE. The public image continues to be available with no further support.

Component | 2.4-dataproc-17 | 2.4-dataproc-16 | 2.4-dataproc-15 | 2.4-dataproc-14  
---|---|---|---|---  
Apache Spark | 2.4.8 | 2.4.8 | 2.4.8 | 2.4.8  
Hadoop Libraries | 2.10.2 | 2.10.2 | 2.10.2 | 2.10.2  
Cloud Storage Connector | hadoop2-2.1.9 | hadoop2-2.1.9 | hadoop2-2.1.9 | hadoop2-2.1.9  
Java | 8 | 8 | 8 | 8  
Python | 3.7.4 | 3.7.4 | 3.7.4 | 3.7.4  
Conda | 4.7.12 | 22.11.1 | 22.11.1 | 22.1.0  
R | 3.6.3 | 3.6.3 | 3.6.3 | 3.6.3  
  
## Spark version formats on Managed Service for Apache Spark on GKE 

A fully qualified Spark engine release version is expressed as: `3.1-dataproc-[NUMBER]` or `3.5-dataproc-[NUMBER]`, for example, `3.1-dataproc-17` or `3.5-dataproc-17`.

Spark version formats can also be expressed in alias form, as shown in the following examples:

  * `3` \- Most recent version of Spark engine with a Spark major version of 3.
  * `3.5` \- Most recent version of Spark engine with a Spark major.minor version of 3.5.
  * `dataproc-2.2` \- Most recent version of Spark engine that is compatible with Managed Service for Apache Spark `2.2` images.
  * `latest` \- Most recent version of Spark engine.

**Note:** Because version aliases are dereferenced at cluster creation time, multiple clusters created using the same alias are not guaranteed to have the same concrete version. Therefore, although aliases are useful to ensure that the cluster is built with the most up-to-date version, they should not be used if exact consistency is required.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
