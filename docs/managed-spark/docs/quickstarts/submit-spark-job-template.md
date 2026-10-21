---
url: https://docs.cloud.google.com/managed-spark/docs/quickstarts/submit-spark-job-template/
title: Quickstart: Submit a Spark job by using a template \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:35.898906+00:00
---

# Quickstart: Submit a Spark job by using a template  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/quickstarts/submit-spark-job-template/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Submit a Spark job by using a template

This page shows you how to use an [Google APIs Explorer](https://developers.google.com/apis-explorer/#p/) template to run a simple Spark job on an existing Managed Service for Apache Spark cluster.

For other ways to submit a job to a Managed Service for Apache Spark cluster, see:

  * [Create a cluster by using the Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-console#submit_a_job)
  * [Create a cluster by using the Google Cloud CLI](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-gcloud#submit_a_job)
  * [Create a cluster by using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries)



## Before you begin

Before you can run a Managed Service for Apache Spark job, you must create a cluster of one or more virtual machines (VMs) to run it on. You can use the [APIs Explorer](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-template), the [Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-console#create_a_cluster), the gcloud CLI [gcloud](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-gcloud#create_a_cluster) command-line tool, or the [Quickstarts using Cloud Client Libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries) to create a cluster. 

## Submit a job

To submit a sample [Apache Spark](http://spark.apache.org/) job that calculates a rough value for [pi](https://en.wikipedia.org/wiki/Pi), fill in and execute the Google APIs Explorer **Try this API** template.

**Note:** The `region`, `clusterName` and `job` parameter values are filled in for you. Confirm or replace the `region` and `clusterName` parameter values to match your cluster's region and name. The `job` parameter values are required to run the a Spark job that is pre-installed on the Managed Service for Apache Spark cluster's master node.

  1. **Request parameters:**

     1. Insert your [**projectId**](https://console.cloud.google.com/).
     2. Specify the [**region**](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) where your cluster is located (confirm or replace "us-central1"). Your cluster's region is listed on the Managed Service for Apache Spark [**Clusters**](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console.
  2. **Request body:**

     1. [**job.placement.clusterName**](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkJob#JobPlacement.FIELDS.cluster_name): The name of the cluster where the job will run (confirm or replace "example-cluster").
     2. [**job.sparkJob.args**](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkJob#FIELDS.args): "1000", the number of job tasks.
     3. [**job.sparkJob.jarFileUris**](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkJob#FIELDS.jar_file_uris): "file:///usr/lib/spark/examples/jars/spark-examples.jar". This is the local file path on the Managed Service for Apache Spark cluster's master node where the jar that contains the Spark Scala job code is installed.
     4. [**job.sparkJob.mainClass**](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkJob#FIELDS.main_class): "org.apache.spark.examples.SparkPi". The is the main method of the job's pi calculation Scala application.
  3. Click **EXECUTE**. The first time you run the API template, you may be asked to choose and sign into your Google account, then authorize the Google APIs Explorer to access your account. If the request is successful, the JSON response shows that job submission request is pending.

  4. To view job output, open the [Managed Service for Apache Spark Jobs](https://console.cloud.google.com/dataproc/jobs) page in the Google Cloud console, then click the top (most recent) Job ID. Click "LINE WRAP" to ON to bring lines that exceed the right margin into view.
         
         ...
         Pi is roughly 3.141804711418047
         ...
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. If you don't need the cluster to explore the other quickstarts or to run other jobs, use the [APIs Explorer](https://docs.cloud.google.com/managed-spark/docs/quickstarts/quickstart-explorer-delete), the [Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-console#delete_a_cluster), the gcloud CLI [gcloud](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-gcloud#delete_a_cluster) command-line tool, or the [Cloud Client Libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries) to delete the cluster.



## What's next

  * Learn how to [update a Managed Service for Apache Spark cluster by using a template](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-template).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
