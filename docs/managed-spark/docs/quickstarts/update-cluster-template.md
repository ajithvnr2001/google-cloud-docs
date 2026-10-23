---
url: https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-template/
title: Quickstart: Update a cluster by using a template \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:11.802615+00:00
---

# Quickstart: Update a cluster by using a template  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-template/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update a cluster by using a template

This page shows you how to use an [Google APIs Explorer](https://developers.google.com/apis-explorer/#p/) template to update a Managed Service for Apache Spark cluster to change the number of workers in a cluster. [Scaling a cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scaling-clusters) up to include more workers is a common task when additional workers are needed to process larger jobs.

For other ways to update a Managed Service for Apache Spark cluster, see:

  * [Create a cluster by using the Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-console#update_a_cluster)
  * [Create a cluster by using the Google Cloud CLI](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-gcloud#update_a_cluster)
  * [Create a cluster by using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries)



## Before you begin

This quickstart assumes you have already created a Managed Service for Apache Spark cluster. You can use the [APIs Explorer](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-template), the [Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-console#create_a_cluster), the gcloud CLI [gcloud](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-gcloud#create_a_cluster) command-line tool, or the [Quickstarts using Cloud Client Libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries) to create a cluster. 

## Update a cluster

To update the number of workers in your cluster, fill in and execute the Google APIs Explorer **Try this API** template.

**Note:** The `region`, `clusterName` and `updateMask` and `config.workerConfig.numInstances` parameter values are filled in for you. Confirm or replace the `region` and`clusterName` parameter values to match your cluster's region and name. The `updateMask` parameter value is required to update the number of workers in your cluster. You can accept or change the `config.workerConfig.numInstances` parameter value.

  1. **Request parameters:**

     1. Insert your [**projectId**](https://console.cloud.google.com/).
     2. Specify the [**region**](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) where your cluster is located (confirm or replace "us-central1"). Your cluster's region is listed on the Managed Service for Apache Spark [**Clusters**](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console.
     3. Specify the [**clusterName**](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/patch#body.PATH_PARAMETERS.cluster_name) of the existing cluster that you are updating (confirm or replace "example-cluster").
     4. [**updateMask**](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/patch): "config.worker_config.num_instances". This is the JSON PATH relative to the [Cluster](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#resource:-cluster) resource to the `numInstances` parameter to be updated (see the Request body instructions).
  2. **Request body:**

     1. [**config.workerConfig.numInstances**](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#InstanceGroupConfig.FIELDS.num_instances): ("3": the new number of workers). You can change this value to add fewer or more workers. For example, if your standard cluster has the default number of 2 workers, specifying "3" will add 1 worker; specifying "4 will add 2). A standard Managed Service for Apache Spark cluster must have at least 2 workers.
  3. Click **EXECUTE**. The first time you run the API template, you may be asked to choose and sign into your Google account, then authorize the Google APIs Explorer to access your account. If the request is successful, the JSON response shows that cluster update is pending.

  4. To confirm that the number of workers in the cluster has been updated, open the Managed Service for Apache Spark [Clusters](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console and view the cluster's **Total worker nodes** column. You may need to click REFRESH at the top of the page to view the updated value after the cluster update completes.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. If you don't need the cluster to explore the other quickstarts or to run other jobs, use the [APIs Explorer](https://docs.cloud.google.com/managed-spark/docs/quickstarts/quickstart-explorer-delete), the [Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-console#delete_a_cluster), the gcloud CLI [gcloud](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-gcloud#delete_a_cluster) command-line tool, or the [Quickstarts using Cloud Client Libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries) to delete the cluster.



## What's next

  * You can use this quickstart template to restore the cluster to its previous `workerConfig.numInstances` value.

  * Learn how to [write and run a Spark Scala job](https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-scala). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
