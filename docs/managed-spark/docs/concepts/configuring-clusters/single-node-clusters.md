---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters/
title: Single node clusters \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:49.326840+00:00
---

# Single node clusters  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Single node clusters Stay organized with collections  Save and categorize content based on your preferences. 

Single node clusters are Managed Service for Apache Spark clusters with only one node. This single node acts as the master and worker for your Managed Service for Apache Spark cluster. While single node clusters only have one node, most Managed Service for Apache Spark concepts and features still apply, except those listed below.

There are a number of situations where single node Managed Service for Apache Spark clusters can be useful, including:

  * Trying out new versions of Spark and Hadoop or other open source components
  * Building proof-of-concept (PoC) demonstrations
  * Lightweight data science
  * Small-scale non-critical data processing
  * Education related to the Spark and Hadoop ecosystem



## Single node cluster semantics

The following semantics apply to single node Managed Service for Apache Spark clusters:

  * Single node clusters are configured the same as multi node Managed Service for Apache Spark clusters, and include services such as HDFS and YARN.
  * Single node clusters report as master nodes for [initialization actions](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions).
  * Single node clusters show 0 workers since the single node acts as both master and worker.
  * Single node clusters are given hostnames that follow the pattern `clustername-m`. You can use this hostname to SSH into or connect to a [web UI](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/cluster-web-interfaces) on the node.
  * Single node clusters cannot be upgraded to multi node clusters. Once created, single node clusters are restricted to one node. Similarly, multi node clusters cannot be scaled down to single node clusters.



## Limitations

  * Single node clusters are not recommended for large-scale parallel data processing. If you exceed the resources on a single node cluster, a multi node Managed Service for Apache Spark cluster is recommended.

  * Single node clusters are not available with [high-availability](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability) since there is only one node in the cluster.

  * Single node clusters cannot use [preemptible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/preemptible-vms).




## Create a single node cluster

### Console

  * Open the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  * In the **Define your cluster shape** section, select **Development**.
  * Under **Additional configuration** , edit **Driver node** , clear the checkbox, **Default driver node to the same as primary worker** , then confirm or change driver node settings.



### gcloud command

You can create a single node Managed Service for Apache Spark cluster using the `gcloud` command-line tool. To create a single node cluster, pass the `--single-node` flag to the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command. 
    
    
    gcloud dataproc clusters create cluster-name \
        --region=region \
        --single-node \
        ... other args
    

### REST API

You can create a single node cluster through the [Dataproc REST API](https://docs.cloud.google.com/managed-spark/docs/reference/rest) using a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. When making this request, you must: 

  1. Add the property `"dataproc:dataproc.allow.zero.workers":"true"` to the [SoftwareConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#SoftwareConfig) of the cluster request.
  2. Don't submit values for `workerConfig` and `secondaryWorkerConfig` (see [ClusterConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig)).

To examine and construct the JSON body of a Dataproc API clusters create request, open the Google Cloud console [Create a cluster](https://console.cloud.google.com/dataproc/clusters/create) page in your browser, fill in the applicable fields, then click **Equivalent REST** at the bottom of the page to view the POST request with the completed JSON request body. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
