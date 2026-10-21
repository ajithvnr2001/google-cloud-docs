---
url: https://docs.cloud.google.com/managed-spark/docs/quickstarts/quickstart-explorer-delete/
title: APIs Explorer Quickstart\u2014Delete a cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:37.318336+00:00
---

# APIs Explorer Quickstart—Delete a cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/quickstarts/quickstart-explorer-delete/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# APIs Explorer Quickstart—Delete a cluster

This page shows you how to use an [Google APIs Explorer](https://developers.google.com/apis-explorer/#p/) template to delete a Managed Service for Apache Spark cluster.

For other ways to submit a job to a Managed Service for Apache Spark cluster, see:

  * [Quickstart Using the Console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-console#clean-up)
  * [Quickstart using the Google Cloud CLI](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-gcloud#clean-up)
  * [Quickstarts using Cloud Client Libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries)



## Before you begin

This quickstart assumes you have already created a Managed Service for Apache Spark cluster. You can use the [APIs Explorer](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-template), the [Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-console#create_a_cluster), the gcloud CLI [gcloud](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-gcloud#create_a_cluster) command-line tool, or the [Quickstarts using Cloud Client Libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries) to create a cluster. 

## Delete a cluster

To delete a cluster, fill in and execute the Google APIs Explorer **Try this API** template.

**Note:** The `region` and `clusterName` parameter values are filled in for you. Confirm or replace these parameter values to match your cluster's region and name.

  1. **Request parameters:**

     1. Insert your [**projectId**](https://console.cloud.google.com/).
     2. Specify the [**region**](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) where your cluster is located (confirm or replace "us-central1"). Your cluster's region is listed on the Managed Service for Apache Spark [**Clusters**](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console.
     3. Specify the [**clusterName**](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/delete#body.PATH_PARAMETERS.cluster_name) of the existing cluster that you are deleting (confirm or replace "example-cluster").
  2. Click **EXECUTE**. The first time you run the API template, you may be asked to choose and sign into your Google account, then authorize the Google APIs Explorer to access your account. If the request is successful, the JSON response shows that cluster update is pending.

  3. To confirm that the cluster is being deleted, open the Managed Service for Apache Spark [Clusters](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console.


![Dataproc cluster page confirms that the cluster is deleted.](https://docs.cloud.google.com/static/managed-spark/images/delete-cluster.png)

## What's next

  * Browse the [Managed Service for Apache Spark tutorials](https://docs.cloud.google.com/managed-spark/docs). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
