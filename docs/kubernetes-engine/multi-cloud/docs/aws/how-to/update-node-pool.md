---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool/
title: Update a node pool \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:06.192844+00:00
---

# Update a node pool  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Update a node pool Stay organized with collections  Save and categorize content based on your preferences. 

After you have created a cluster, you can modify its node pools. Only certain parameters of a node pool can be updated, such as its size, encryption key, and security groups. This document explains how to perform these and other common updates to a node pool.

However, this document doesn't provide an exhaustive list of update commands. If you need to update a parameter that isn't described in this document, see [`gcloud container aws node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update) and the [`projects.locations.awsNodePools.patch`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.awsClusters.awsNodePools/patch) documentation.

## Before you begin

To update a node pool, you must have the following Identity and Access Management permission: `gkemulticloud.googleapis.com/awsNodePools.update`.

For instructions about how to manage permissions, see [Grant IAM roles to users](https://docs.cloud.google.com/anthos/multicluster-management/gateway/setup#grant_iam_roles_to_users).

## Update a node pool

The following sections explain how to make various updates to a node pool. A [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) is a group of nodes within a cluster that have the same configuration. All the nodes in a cluster must belong to a node pool.

You can update multiple parameters of a node pool at the same time by specifying them all in the same command. However, for the sake of clarity, this document shows how to update a single parameter at a time.

### Change node pool version

In GKE on AWS, changing a node pool version means changing the GKE version that is running on the nodes in that node pool.

To change the node pool version, specify the new version using the `node-version` flag in the following command:
    
    
    gcloud container aws node-pools update NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION \
        --node-version NODE_POOL_VERSION
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool to update.
  * `CLUSTER_NAME`: the name of the cluster to attach the node pool to.
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster. For example, `us-west1`.
  * `NODE_POOL_VERSION`: the new [supported node pool version](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/versioning).



### Update node pool instance type

A node pool instance type is the type of AWS EC2 instance that is used to create the nodes in a node pool. For example, the `m5.xlarge` instance type has 4 vCPUs, 16GB of memory, and 32GB of SSD storage.

To change the instance type of your node pool, specify the new instance type using the `instance-type` flag in the following command:
    
    
    gcloud container aws node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=GOOGLE_CLOUD_LOCATION \
        --instance-type=INSTANCE_TYPE
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster.
  * `INSTANCE_TYPE`: the new AWS machine instance type for this node pool. For example, `m5.xlarge`.



Updates to the node pool instance type must not change the underlying CPU architecture of the EC2 instance. For example, if your original node pool uses instances with x86 CPUs, then your updated instance type needs to continue to use x86 CPUs, rather than some other architecture.

For a complete list of supported instances and their underlying architectures, see [supported AWS instance types](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-instance-types).

### Rotate a node pool's encryption key

For information about how to update your node pool's KMS encryption keys, see [Key rotation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/key-rotation#node_pool_configuration_key).

### Replace node pool security groups

To update the security groups attached to a node pool, run the following command:
    
    
    gcloud container aws node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=GOOGLE_CLOUD_LOCATION \
        --security-group-ids=SECURITY_GROUP_IDS
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool to update.
  * `CLUSTER_NAME`: the name of your cluster.
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster.
  * `SECURITY_GROUP_IDS`: a comma-separated list of security groups to attach to the node pool.



For clusters running GKE version 1.25 or later, the update can be performed dynamically without restarting the nodes. This is the recommended approach for clusters that use GKE v1.25 or later.

To perform dynamic updates, your API service agent role must have the following AWS IAM permissions:

  * `ec2:ModifyInstanceAttribute`
  * `ec2:DescribeInstances`



These permissions are automatically assigned to the API service agent role if you choose the [default API service agent role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_service_agent_role) when you create your cluster.

For clusters running earlier versions of GKE, or clusters running versions 1.25 or later but the API service agent doesn't have the permissions to perform a dynamic update, the update is performed using a rolling update. Rolling updates are more disruptive than dynamic updates because rolling updates restart nodes, while dynamic updates don't. For more information about rolling updates, see [Surge updates](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/about-surge-updates).

### Remove node pool security groups

You can remove all the non-default security groups attached to your node pool by running the following command. For more information about default security groups, see [Node pool security groups](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/security-groups#node_pool_security_groups).
    
    
    gcloud container aws node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=GOOGLE_CLOUD_LOCATION \
        --clear-security-group-ids
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool to update.
  * `CLUSTER_NAME`: the name of your cluster.
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster.



## Resize a node pool

To change the size of your node pool (that is, the number of nodes in the node pool), assign new values to the `min-nodes` and `max-nodes` flags in the following command:
    
    
    gcloud container aws node-pools update NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION \
        --min-nodes MIN_NODES \
        --max-nodes MAX_NODES
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool to update.
  * `CLUSTER_NAME`: the name of the cluster to attach the node pool to.
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster. For example, `us-west1`.
  * `MIN_NODES`: the minimum number of nodes the node pool can contain. Value can be `0` or greater.
  * `MAX_NODES`: the maximum number of nodes the node pool can contain. Value must be at least `1`, and greater than or equal to the value of `MIN_NODES`.



### Further details about resizing node pools

Before resizing a node pool, it's important to evaluate the potential repercussions on your workloads.

#### Resizing actions and their consequences

When resizing node pools, different actions are triggered based on the new configuration and the current state of the nodes. It's essential to understand these actions and their implications:

  * **No change** : If the current node count already aligns with the new specified range, GKE on AWS makes no adjustments to the number of nodes.
  * **Increasing the minimum** : If the new minimum number of nodes is set higher than the existing count, GKE on AWS incrementally adds nodes until the newly defined minimum size is reached.
  * **Decreasing the maximum** : If you change the maximum node count to a value that's lower than the existing count, GKE on AWS performs the following actions: 
    * Disables the cluster autoscaler.
    * Sets the Auto Scaling group for the node pool to the specified minimum size.
    * Selects individual nodes for removal. Each node is cordoned off, drained of its tasks, and then terminated. This procedure continues until the specified maximum size is reached.
    * Modifies the Auto Scaling group of the node pool to align with the new maximum size.
    * Re-enables the cluster autoscaler once the maximum size is reached.



For more information about the cluster autoscaler, see [About cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/cluster-autoscaler).

#### Workload protection during resizing

To ensure the continued availability of workloads during node pool resizing, GKE on AWS provides the following safeguards:

  * During a node drain, GKE on AWS respects the `PodDisruptionBudget` configuration for up to one hour. Pods remaining on the node after this period are deleted.

  * When nodes are set to be restarted or removed, GKE on AWS ensures their graceful shutdown and waits up to two hours. If Pods remain on the node after this period, the underlying virtual machine instance is deleted.




## Check the status of your node pool

To verify that your update was successful, you can check the status of the node pool by running the following command:
    
    
    gcloud container aws node-pools describe NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster.



GKE on AWS tries to perform the requested updates to the node pool and then performs a health check. If any of the update steps fail, the node pool status is marked as `DEGRADED`.

## Cancel an update operation

Before you can cancel an ongoing node pool update, you need to determine the name of the operation in progress. To list the ongoing operations and their respective names, run the following command:
    
    
    gcloud container aws operations list--filter="status=PENDING OR status=RUNNING"
        --location GOOGLE_CLOUD_LOCATION
    

Replace `GOOGLE_CLOUD_LOCATION` with the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster. For example, `us-west1`.

Look for the `OPERATION_NAME` of the update you want to cancel in the output of the command. For a list of operations, see [gcloud container aws operations list](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/operations/list).

Once you have identified the `OPERATION_NAME`, you can cancel the operation with the following command:
    
    
    gcloud container aws operations cancel OPERATION_NAME
        --location GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `OPERATION_NAME`: the name of the update operation.
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster. For example, `us-west1`.



Note that cancelling an ongoing node pool update doesn't revert node updates that have already completed. This can result in a partially updated node pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
