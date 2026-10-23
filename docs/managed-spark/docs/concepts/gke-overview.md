---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/gke-overview/
title: Managed Service for Apache Spark on GKE overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:36.587965+00:00
---

# Managed Service for Apache Spark on GKE overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/gke-overview/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark on GKE overview Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark on GKE allows you to execute Big Data applications using the Managed Service for Apache Spark `jobs` API on GKE clusters. Use the Google Cloud console, Google Cloud CLI or the Managed Service for Apache Spark API (HTTP request or Cloud Client Libraries) to [create a Managed Service for Apache Spark on GKE virtual cluster](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/gke-quickstart-create-cluster), then submit a Spark, PySpark, SparkR, or Spark-SQL job to the Managed Service for Apache Spark service.

Managed Service for Apache Spark on GKE supports [Spark 3.5 versions](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-versions).

## How Managed Service for Apache Spark on GKE works

Managed Service for Apache Spark on GKE deploys Managed Service for Apache Spark **virtual** clusters on a GKE cluster. Unlike [Managed Service for Apache Spark on Compute Engine clusters](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster), Managed Service for Apache Spark on GKE virtual clusters do not include separate master and worker VMs. Instead, when you create a Managed Service for Apache Spark on GKE virtual cluster, Managed Service for Apache Spark on GKE creates node pools within a GKE cluster. Managed Service for Apache Spark on GKE jobs are run as pods on these node pools. The node pools and scheduling of pods on the node pools are managed by GKE.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
