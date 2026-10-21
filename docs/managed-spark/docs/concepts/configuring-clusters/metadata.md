---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/metadata/
title: Cluster metadata \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:30.400104+00:00
---

# Cluster metadata  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/metadata/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Cluster metadata Stay organized with collections  Save and categorize content based on your preferences. 

**Metadata compared to Labels**

  * Custom metadata is available to processes running on your cluster, and can be used by initialization actions.
  * Labels are not readily available to processes running on your cluster, but can be used when searching through resources with the Dataproc API. 

If you need a piece of data to be available to your cluster and also used as an API search parameter, then add it both as metadata and as a label to your cluster. 

Managed Service for Apache Spark sets special metadata values for the instances that run in your cluster:

Metadata key| Value | `dataproc-bucket`| Name of the cluster's [staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket)  
---|---  
`dataproc-region`| [Region](https://docs.cloud.google.com/managed-spark/docs/concepts/regional-endpoints) of the cluster's endpoint  
`dataproc-worker-count`| Number of worker nodes in the cluster. The value is `0` for [single node clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters).  
`dataproc-cluster-name`| Name of the cluster  
`dataproc-cluster-uuid`| UUID of the cluster  
`dataproc-role`| Instance's role, either `Master` or `Worker`  
`dataproc-master`| Hostname of the first master node. The value is either `[CLUSTER_NAME]-m` in a standard or single node cluster, or `[CLUSTER_NAME]-m-0` in a [high-availability cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability), where `[CLUSTER_NAME]` is the name of your cluster.  
`dataproc-master-additional`| Comma-separated list of hostnames for the additional master nodes in a high-availability cluster, for example, `[CLUSTER_NAME]-m-1,[CLUSTER_NAME]-m-2` in a cluster that has 3 master nodes.  
`SPARK_BQ_CONNECTOR_VERSION or SPARK_BQ_CONNECTOR_URL`| The version or URL that points to a Spark BigQuery connector version to use in Spark applications, for example, `0.42.1` or `gs://spark-lib/bigquery/spark-3.5-bigquery-0.42.1.jar`. A default Spark BigQuery connector version is pre-installed in Managed Service for Apache Spark `2.1` and later image version clusters. For more information, see [Use the Spark BigQuery connector](https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-connector-spark-example).  
  
You can use these values to customize the behavior of [initialization actions](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions).

You can use the `--metadata` flag in the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command to provide your own metadata:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --metadata=name1=value1,name2=value2... \
        ... other flags ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
