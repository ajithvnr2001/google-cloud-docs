---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-nodepools/
title: Create node pools \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:45.977053+00:00
---

# Create node pools  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-nodepools/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create node pools Stay organized with collections  Save and categorize content based on your preferences. 

When you [create](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/dataproc-gke-quickstart-create-cluster) or [update](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/dataproc-gke-recreate-cluster) a Managed Service for Apache Spark on GKE virtual cluster, you specify one or more node pools that the virtual cluster will use to run jobs (this cluster is referred to as the cluster "used by" or "associated" with the specified node pools). If a specified node pool does not exist on your GKE cluster, Managed Service for Apache Spark on GKE will create the node pool on the GKE cluster with settings you specify. If the node pool exists and was created by Managed Service for Apache Spark, it will be validated to confirm that its settings match the specified settings.

### Managed Service for Apache Spark on GKE node pool settings

You can specify the following [settings](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#gkenodeconfig) on node pools used by your Managed Service for Apache Spark on GKE virtual clusters (these settings are a subset of [GKE node pool settings](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig)):

  * `accelerators`
  * `acceleratorCount`
  * `acceleratorType`
  * `gpuPartitionSize`*
  * `localSsdCount`
  * `machineType`
  * `minCpuPlatform`
  * `minNodeCount`
  * `maxNodeCount`
  * `preemptible`
  * `spot`*



Notes:

  * `gpuPartitionSize` can be set in the Managed Service for Apache Spark API [`GkeNodePoolAcceleratorConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#gkenodepoolacceleratorconfig).
  * `spot` can be set in the Managed Service for Apache Spark API [GkeNodeConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#gkenodeconfig).



## Node pool deletion

When a Managed Service for Apache Spark on GKE cluster is deleted, the node pools used by the cluster are not deleted. See [Delete a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool) to delete node pools no longer in use by Managed Service for Apache Spark on GKE clusters.

## Node pool location

You can specify the [zone](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#GkeNodePoolConfig.FIELDS.locations) location of node pools associated with your Managed Service for Apache Spark on GKE virtual cluster when you create or update the virtual cluster. The node pool zones must be located in the region of the associated virtual cluster.

## Role to node pool mapping

Node pool [roles](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#Role) are defined for Spark driver and executor work, with a default role defined for all types of work by a node pool. Managed Service for Apache Spark on GKE clusters must have at least one a node pool that is assigned the `default` role. Assigning other roles is optional.

**Recommendation:** Create separate node pools for each role type, with node type and size based on role requirements.

gcloud CLI virtual cluster creation example:
    
    
    gcloud dataproc clusters gke create "${DP_CLUSTER}" \
      --region=${REGION} \
      --gke-cluster=${GKE_CLUSTER} \
      --spark-engine-version=latest \
      --staging-bucket=${BUCKET} \
      --pools="name=${DP_POOLNAME},roles=default \
      --setup-workload-identity
      --pools="name=${DP_CTRL_POOLNAME},roles=default,machineType=e2-standard-4" \
      --pools="name=${DP_DRIVER_POOLNAME},min=1,max=3,roles=spark-driver,machineType=n2-standard-4" \
      --pools="name=${DP_EXEC_POOLNAME},min=1,max=10,roles=spark-executor,machineType=n2-standard-8"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
