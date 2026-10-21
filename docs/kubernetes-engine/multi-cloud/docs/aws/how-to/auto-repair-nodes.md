---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/auto-repair-nodes/
title: Automatic Node Repair \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:06.918105+00:00
---

# Automatic Node Repair  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/auto-repair-nodes/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Automatic Node Repair Stay organized with collections  Save and categorize content based on your preferences. 

The node auto repair feature continuously monitors the health of each node in a node pool. If a node becomes unhealthy, the node auto repair feature repairs it automatically. This feature decreases the likelihood of cluster outages and performance degradation, and it minimizes the need for manual maintenance of your clusters.

You can enable node auto repair when creating or updating a node pool. Note that you enable or disable this feature on node pools rather than on individual nodes.

## Unhealthy node conditions

Node auto repair examines the health status of each node to determine if it requires repair. A node is considered healthy if it reports a `Ready` status. Otherwise, if it consecutively reports an unhealthy status for a specific duration, repairs are initiated.

An unhealthy status can arise from a `NotReady` state, detected in consecutive checks over approximately 15 minutes. Alternatively, an unhealthy status may result from depleted boot disk space, identified over a period of approximately 30 minutes.

You can manually check your node's health signals at any time by running the `kubectl get nodes` command.

## Node repair strategies

Node auto repair follows certain strategies to ensure both the overall health of the cluster and the availability of applications during the repair process. This section describes how the node auto repair feature honors `PodDisruptionBudget` configurations, respects the `Pod Termination Grace Period`, and takes other measures that minimize cluster disruption when repairing nodes.

### Honor `PodDisruptionBudget` for 30 minutes

If a node requires repair, it isn't instantly drained and re-created. Instead, the node auto repair feature honors [PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) (PDB) configurations for up to 30 minutes, after which all the Pods on the node are deleted. (A PDB configuration defines, among other things, the minimum number of replicas of a particular Pod that must be available at any given time).

By honoring the `PodDisruptionBudget` for approximately 30 minutes, the node auto repair feature provides a window of opportunity for Pods to be safely rescheduled and redistributed across other healthy nodes in the cluster. This helps maintain the desired level of application availability during the repair process.

After the 30 minute time limit, node auto repair proceeds with the repair process, even if it means violating the `PodDisruptionBudget`. Without a time limit, the repair process could stall indefinitely if the `PodDisruptionBudget` configuration prevents the evictions necessary for a repair.

### Honor the Pod Termination Grace Period

The node auto repair feature also honors a [Pod Termination Grace Period](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-terminating-with-grace) of approximately 30 minutes. The Pod Termination Grace Period provides Pods with a window of time for a graceful shutdown during termination. During the grace period, the kubelet on a Node is responsible for executing cleanup tasks and freeing resources associated with the Pods on that Node. The node auto repair feature allows up to 30 minutes for the kubelet to complete this cleanup. If the allotted 30 minutes elapse, the Node is forced to terminate, regardless of whether the Pods have gracefully terminated.

### Additional node repair strategies

Node auto repair also implements the following strategies:

  * If multiple nodes require repair, they are repaired one at a time to limit cluster disruption and to protect workloads.
  * If you disable node auto-repair during the repair process, in-progress repairs nonetheless continue until the repair operation succeeds or fails.



## How to enable and disable automatic node repair

You can enable or disable node auto repair when creating or updating a node pool. You enable or disable this feature on node pools rather than on individual nodes.

### Enable auto repair for a new node pool
    
    
    gcloud container aws node-pools create NODE_POOL_NAME \
       --cluster CLUSTER_NAME \
       --instance-type INSTANCE_TYPE \
       --root-volume-size ROOT_VOLUME_SIZE \
       --iam-instance-profile NODEPOOL_PROFILE \
       --node-version NODE_VERSION \
       --min-nodes MIN_NODES \
       --max-nodes MAX_NODES \
       --max-pods-per-node MAX_PODS_PER_NODE \
       --location GOOGLE_CLOUD_LOCATION \
       --subnet-id NODEPOOL_SUBNET \
       --ssh-ec2-key-pair SSH_KEY_PAIR_NAME \
       --config-encryption-kms-key-arn CONFIG_KMS_KEY_ARN \
       --tags "Name=CLUSTER_NAME-NODE_POOL_NAME" \
       --enable-autorepair
    

Replace the following:

  * `NODE_POOL_NAME`: a name you choose for your node pool. To get the names of your node pools, run the command `gcloud container aws node-pools list --cluster CLUSTER_NAME --location GOOGLE_CLOUD_LOCATION`
  * `CLUSTER_NAME`: the name of the cluster to attach the node pool to
  * `INSTANCE_TYPE`: the desired AWS machine instance type for this node pool— for example, `m5.large`
  * `ROOT_VOLUME_SIZE`: the desired size for each node's root volume, in Gb
  * `NODEPOOL_PROFILE`: the IAM instance profile for node pool VMs
  * `NODE_VERSION`: the Kubernetes version to install on each node in the node pool (e.g., "1.35.3-gke.300")
  * `MIN_NODES`: the minimum number of nodes the node pool can contain
  * `MAX_NODES`: the maximum number of nodes the node pool can contain
  * `MAX_PODS_PER_NODE`: the maximum number of pods that can be created on any single node in the pool
  * `GOOGLE_CLOUD_LOCATION`: the name of the Google Cloud location from which this node pool will be managed
  * `NODEPOOL_SUBNET`: the ID of the subnet the node pool will run on. 
    * There must not be any overlap between the cluster's Pod/Service IP ranges and the node pool subnet network. For more information on selecting Pod and Service IP ranges for your cluster, see [Select CIDR ranges for your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster#cidr_ranges)
    * If this subnet is outside of the VPC primary CIDR block, some additional steps are needed. For more information, see [security groups](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/security-groups).
  * `SSH_KEY_PAIR_NAME`: the name of the AWS SSH key pair created for SSH access (optional)
  * `CONFIG_KMS_KEY_ARN`: the Amazon Resource Name (ARN) of the AWS KMS key that encrypts user data



### Enable auto repair for an existing node pool

To enable node auto repair on an existing node pool, run the following command:
    
    
    gcloud container aws node-pools update NODE_POOL_NAME \
       --cluster CLUSTER_NAME \
       --location GOOGLE_CLOUD_LOCATION \
       --enable-autorepair
    

Replace the following:

  * `NODE_POOL_NAME`: a unique name for your node pool — for example, `node-pool-1`
  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster



### Disable auto repair for an existing node pool
    
    
    gcloud container aws node-pools update NODE_POOL_NAME \
       --cluster CLUSTER_NAME \
       --location GOOGLE_CLOUD_LOCATION \
       --no-enable-autorepair
    

Replace the following:

  * `NODE_POOL_NAME`: a unique name for your node pool — for example, `node-pool-1`
  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster



Note that GKE on AWS performs graceful node auto repair disablement. When disabling node auto repair for an existing node pool, GKE on AWS launches an update node pool operation. The operation waits for any existing node repairs to complete before it proceeds.

## Check whether node auto repair is enabled

Run the following command to check whether or not node auto repair is enabled:
    
    
    gcloud container aws node-pools describe NODE_POOL_NAME \
       --cluster CLUSTER_NAME \
       --location GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `NODE_POOL_NAME`: a unique name for your node pool — for example, `node-pool-1`
  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster



## Node repair history

You can view the history of repairs performed on a node pool by running the following command:
    
    
    gcloud container aws operations list \
       --location GOOGLE_CLOUD_LOCATION \
       --filter="metadata.verb=repair AND metadata.target=projects/PROJECT_ID/locations/GOOGLE_CLOUD_LOCATION/awsClusters/CLUSTER_NAME/awsNodePools/NODEPOOL_NAME
    
    

Replace the following:

  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster — for example, `us-west1`
  * `PROJECT_ID`: your Google Cloud project
  * `CLUSTER_NAME`: the name of your cluster
  * `NODE_POOL_NAME`: a unique name for your node pool — for example, `node-pool-1`



## Node pool health summary

Once you've enabled node auto repair, you can generate a node pool health summary by running the following command:
    
    
    gcloud container aws node-pools describe NODE_POOL_NAME \
       --cluster CLUSTER_NAME \
       --location GOOGLE_CLOUD_LOCATION
    

A node pool healthy summary looks similar to this sample:
    
    
    {
      "name": "some-np-name",
      "version": "some-version",
      "state": "RUNNING",
    
      ...
    
      "errors": [
        {
          "message": "1 node(s) is/are identified as unhealthy among 2 total node(s) in the node pool. No node is under repair."
        }
      ],
    }
    
    

The node pool health summary helps you understand the current state of the node pool. In this example, the summary contains an error message which states that one of the two nodes in the node pool is unhealthy. It also reports that no nodes are currently undergoing the repair process.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
