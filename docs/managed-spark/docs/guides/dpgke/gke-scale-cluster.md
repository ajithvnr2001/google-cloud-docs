---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-scale-cluster/
title: Scale GKE clusters \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:11.553572+00:00
---

# Scale GKE clusters  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-scale-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Scale GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

To scale a Managed Service for Apache Spark on GKE cluster, update the autoscaler configuration of the [node pool(s)](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-nodepools) associated with the Spark driver or Spark executor roles. You specify Managed Service for Apache Spark on GKE [node pools and their associated roles](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-nodepools#role_to_node_pool_mapping) when you [create a Managed Service for Apache Spark on GKE cluster](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/dataproc-gke-quickstart-create-cluster#create_a_on_cluster).

## Set node pool autoscaling

You can set the bounds for Managed Service for Apache Spark on GKE node pool autoscaling when you [create a Managed Service for Apache Spark on GKE virtual cluster](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/dataproc-gke-quickstart-create-cluster). If not specified, Managed Service for Apache Spark on GKE node pools are autoscaled with default values (at Managed Service for Apache Spark on GKE GA release, defaults set to minimum = 1 and maximum = 10, which are subject to change). To obtain specific minimum and maximum node pool autoscaling values, set them when you create your Managed Service for Apache Spark on GKE virtual cluster.

## Update node pool autoscaling

**Note:** Updating a Managed Service for Apache Spark on GKE node pool configuration to [disable autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_limits) is not recommended.

Use the following GKE [`gcloud container node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update) command to change the autoscaling configuration of a Managed Service for Apache Spark on GKE node pool.
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=GKE_CLUSTER_NAME \
        --region=region \
        --enable-autoscaling \
        --min-nodes=min nodes (must be <= max-nodes) \
        --max-nodes=max nodes (must be >= min-nodes) \
    
    

## How Spark autoscaling works

  1. When a job is submitted, the driver pod is scheduled to run on the node pool associated with the [Spark driver role](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#role).
  2. The driver pod calls the GKE scheduler to create executor pods.
  3. Executor pods are scheduled on the node pool associated with the [Spark executor role](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#role).
  4. If the node pools have capacity for the pods, the pods start running immediately. If there is insufficient capacity, the GKE cluster autoscaler scales up the node pool to provide the requested resources, up to the user-specified limit. When node pools have excess capacity, the GKE cluster autoscaler scales down the node pool to its user-specified limit.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
