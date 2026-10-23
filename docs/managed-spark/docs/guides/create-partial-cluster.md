---
url: https://docs.cloud.google.com/managed-spark/docs/guides/create-partial-cluster/
title: Create a Managed Service for Apache Spark partial cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:04.503838+00:00
---

# Create a Managed Service for Apache Spark partial cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/create-partial-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create a Managed Service for Apache Spark partial cluster Stay organized with collections  Save and categorize content based on your preferences. 

To mitigate the effects of the unavailability of user-specified VMs in specific regions at specific times ([stockouts](https://en.wikipedia.org/wiki/Stockout)), Managed Service for Apache Spark lets you request the creation of a `partial cluster` by specifying a **minimum number** of primary workers that is acceptable to allow cluster creation.

**Note:** See [Managed Service for Apache Spark secondary workers](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms) to understand the difference between primary and secondary workers.Standard cluster | Partial cluster  
---|---  
If one or more primary workers cannot be created and initialized, cluster creation fails. Workers that are created continue to run and incur charges until deleted by the user. | If the specified minimum number of workers can be created, the cluster is created. Failed (uninitialized) workers are deleted and don't incur charges. If the specified minimum number of workers can't be created and initialized, the cluster is not created. Workers that are created aren't deleted to allow for debugging.  
Cluster creation time is optimized. | Longer cluster creation time can occur since all nodes must report provisioning status.  
[Single node clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters) are available for creation. | [Single node clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters) are not available for creation.  
  
### Autoscaling

Use [autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling) with partial cluster creation to make sure that the target (full) number of primary workers is created. Autoscaling will try to acquire failed workers in the background if the workload requires them.

The following is a sample autoscaling policy that retries until the total number of primary worker instances reaches a target size of 10. The policy's `minInstances` and `maxInstances` match the minimum and total number of primary workers specified at cluster creation time (see Create a partial cluster). Setting the `scaleDownFactor` to 0 prevents the cluster from scaling down from 10 to 8, and will help keep the number of workers at the maximum 10-worker limit.
    
    
    workerConfig:
      minInstances: 8
      maxInstances: 10
    basicAlgorithm:
      cooldownPeriod: 2m
      yarnConfig:
        scaleUpFactor: 1
        scaleDownFactor: 0
        gracefulDecommissionTimeout: 1h
    

## Create a partial cluster

You can use the Google Cloud CLI or the Dataproc API to create a Managed Service for Apache Spark partial cluster.

**Note:** Managed Service for Apache Spark partial cluster creation is not available in the Google Cloud console.

### gcloud

To create a Managed Service for Apache Spark partial cluster on the command line, run the following [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--min-num-workers) command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true).
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --project=PROJECT \
        --region=REGION \
        --num-workers=NUM_WORKERS \
        --min-num-workers=MIN_NUM_WORKERS \
        other args ...
    

Replace the following:

  * CLUSTER_NAME: The cluster name must start with a lowercase letter followed by up to 51 lowercase letters, numbers, and hyphens, and cannot end with a hyphen.
  * PROJECT: Specify the project associated with the job cluster.
  * REGION: Specify the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the job cluster will be located.
  * NUM_WORKERS: The total number of primary workers in the cluster to create if available.
  * MIN_NUM_WORKERS: The minimum number of primary workers to create if the specified total number of workers (`NUM_WORKERS`) cannot be created. Cluster creation fails if this minimum number of primary workers cannot be created (workers that are created are not deleted to allow for debugging). If this flag is omitted, standard cluster creation with the total number of primary workers (`NUM_WORKERS`) is attempted. 



### REST

To create a Dataproc partial cluster, specify the minimum number of primary workers in the [`workerConfig.minNumInstances`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#FIELDS.min_num_instances) field as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

**Note:** You can click the **Equivalent command line** or **Equivalent REST** links at the bottom of the page of the Managed Service for Apache Spark Google Cloud console [Create a cluster](https://console.cloud.google.com/dataproc/clusters/create) page to have the Console construct an equivalent API REST request or gcloud CLI command to use in your code or from the command line to create a cluster.

## Display the number of provisioned workers

After creating a cluster, you can run the following gcloud CLI command to list the number of workers, including any secondary workers, provisioned in your cluster.
    
    
    gcloud dataproc clusters list \
        --project=PROJECT \
        --region=REGION \
        --filter=clusterName=CLUSTER_NAME
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
