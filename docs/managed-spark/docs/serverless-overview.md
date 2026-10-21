---
url: https://docs.cloud.google.com/managed-spark/docs/serverless-overview/
title: Managed Service for Apache Spark serverless overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:54.822658+00:00
---

# Managed Service for Apache Spark serverless overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/serverless-overview/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark serverless overview Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark serverless lets you run Spark workloads without requiring you to provision and manage your own cluster. There are two ways to run Managed Service for Apache Spark workloads: batch workloads and interactive sessions.

## Batch workloads

Submit a batch workload using the Google Cloud console, Google Cloud CLI, or REST API. Managed Service for Apache Spark runs the workload on a managed compute infrastructure, autoscaling resources as needed. [Charges](https://cloud.google.com/products/managed-service-for-apache-spark/pricing) apply only to the time when the workload is executing.

### Batch workload capabilities

You can run the following batch workload types:

  * PySpark
  * Spark SQL
  * Spark R
  * Spark (Java or Scala)



You can specify [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties) when you submit a batch workload.

### Schedule batch workloads

You can schedule a Spark batch workload as part of an [Airflow](https://airflow.apache.org/) or [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer) workflow using an [Airflow batch operator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/dataproc.html#create-a-batch). For more information, see [Run Managed Service for Apache Spark serverless workloads with Managed Airflow](https://docs.cloud.google.com/composer/docs/composer-2/run-dataproc-workloads).

### Get started

To get started, see [Run an Apache Spark batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch).

## Interactive sessions

Write and run code in Jupyter notebooks during an interactive session. You can create a notebook session in the following ways:

  * [Run PySpark code in BigQuery Studio notebooks](https://docs.cloud.google.com/bigquery/docs/use-spark). Open a BigQuery Python notebook to create a [Spark-Connect-based](https://spark.apache.org/docs/latest/spark-connect-overview.html) interactive session. Each BigQuery notebook can have only one active session associated with it.

  * [Use the JupyterLab plugin](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions) to create multiple Jupyter notebook sessions from templates that you create and manage. When you install the plugin on a local machine or Compute Engine VM, different cards that correspond to different Spark kernel configurations appear on the JupyterLab launcher page. Click a card to create a Managed Service for Apache Spark notebook session, then start writing and testing your code in the notebook.

The JupyterLab plugin also lets you use the JupyterLab launcher page to take the following actions:

    * Create Managed Service for Apache Spark clusters.
    * Submit jobs to clusters.
    * View Google Cloud and Spark logs.
  * [Use Google Cloud Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview) to manage your entire data workload lifecycle within your IDE. Data Agent Kit provides support for Managed Service for Apache Spark, letting you develop code, create interactive sessions, and [build pipelines](https://docs.cloud.google.com/data-cloud-extension/vs-code/build-pipelines) directly from VS Code or using a supported agentic CLI.




## Security compliance

Managed Service for Apache Spark adheres to all [data residency](https://cloud.google.com/terms/data-residency), [CMEK](https://docs.cloud.google.com/managed-spark/docs/guides/cmek-serverless), [VPC-SC](https://docs.cloud.google.com/managed-spark/docs/concepts/network#s8s-and-vpc-sc-networks), and other security requirements that Managed Service for Apache Spark is compliant with.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
