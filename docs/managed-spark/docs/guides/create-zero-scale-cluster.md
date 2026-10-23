---
url: https://docs.cloud.google.com/managed-spark/docs/guides/create-zero-scale-cluster/
title: Create a Managed Service for Apache Spark zero-scale cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:36.319471+00:00
---

# Create a Managed Service for Apache Spark zero-scale cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/create-zero-scale-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create a Managed Service for Apache Spark zero-scale cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a Managed Service for Apache Spark zero-scale cluster.

Managed Service for Apache Spark zero-scale clusters provide a cost-effective way to use Managed Service for Apache Spark clusters. Unlike [standard Managed Service for Apache Spark clusters](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster) that require at least two primary workers, Managed Service for Apache Spark zero-scale clusters use only [secondary workers](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms) that can be scaled down to zero.

Managed Service for Apache Spark zero-scale clusters are ideal for use as long-running clusters that experience idle periods, such as a cluster that hosts a Jupiter notebook. They provide improved resource utilization through the use of zero-scale autoscaling policies.

## Characteristics and limitations

A Managed Service for Apache Spark zero-scale cluster shares similarities with a standard cluster, but has the following unique characteristics and limitations:

  * Requires image version `2.2.53` or later.
  * Supports only secondary workers, not primary workers.
  * Includes services such as YARN, but doesn't support the HDFS file system.

    * To use Cloud Storage as the default file system, set the `core:fs.defaultFS` cluster property to a Cloud Storage bucket location (`gs://BUCKET_NAME`).
    * If you disable a component during cluster creation, also disable HDFS.
  * Can't be converted to or from a standard cluster.

  * Requires an autoscaling policy for `ZERO_SCALE` cluster types.

  * Requires selecting [flexible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms#how_to_request_flexible_vms) as machine type.

  * Doesn't support the Oozie component.

  * Can't be created from the Google Cloud console.




## Optional: Configure an autoscaling policy

You can configure an autoscaling policy to define secondary working scaling for a zero-scale cluster. When doing so, note the following:

  * Set the cluster type to `ZERO_SCALE`.
  * Configure an autoscaling policy to the secondary worker config only.



For more information, see [Create an autoscaling policy](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling#create_an_autoscaling_policy).

## Create a Managed Service for Apache Spark zero-scale cluster

Create a zero-scale cluster using the gcloud CLI or the Dataproc API.

**Note:** When selecting a machine type for zero-scale clusters, use [flexible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms#how_to_request_flexible_vms).

###  gcloud 

Run [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true%22).
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --cluster-type=zero-scale \
        --autoscaling-policy=AUTOSCALING_POLICY \
        --properties=core:fs.defaultFS=gs://BUCKET_NAME \
        --secondary-worker-machine-types="type=MACHINE_TYPE1[,type=MACHINE_TYPE2...][,rank=RANK]"
        ...other args
    

Replace the following:

  * CLUSTER_NAME: name of the Managed Service for Apache Spark zero-scale cluster.
  * REGION: an [available Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * AUTOSCALING_POLICY: the ID or resource URI of the autoscaling policy.
  * BUCKET_NAME: name of your Cloud Storage bucket.
  * MACHINE_TYPE: specific Compute Engine machine type, such as `n1-standard-4`, `e2-standard-8`.
  * RANK: defines the priority of a list of machine types.



###  REST 

Create a zero-scale cluster using a Managed Service for Apache Spark REST API [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request:

  * Set [`ClusterConfig.ClusterType`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#ClusterType.ENUM_VALUES.ZERO_SCALE) for the `secondaryWorkerConfig` to `ZERO_SCALE`.
  * Set the [`AutoscalingConfig.policyUri`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#AutoscalingConfig.FIELDS.policy_uri) with the `ZERO_SCALE` autoscaling policy ID.
  * Add the `core:fs.defaultFS:gs://BUCKET_NAME` [SoftwareConfig.property](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/ClusterConfig#SoftwareConfig.FIELDS.properties). Replace BUCKET_NAME with the name of your Cloud Storage bucket.



## What's next

  * Learn more about [Managed Service for Apache Spark autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
