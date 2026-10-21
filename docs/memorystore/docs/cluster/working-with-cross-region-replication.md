---
url: https://docs.cloud.google.com/memorystore/docs/cluster/working-with-cross-region-replication/
title: Work with cross-region replication \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:09.319024+00:00
---

# Work with cross-region replication  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/working-with-cross-region-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Work with cross-region replication Stay organized with collections  Save and categorize content based on your preferences. 

Cross-region replication lets you create secondary clusters from a primary cluster to make the cluster available in different regions. If the primary cluster's region becomes unavailable, then you can detach or switch over to a secondary cluster in another region to serve read and write requests. Secondary clusters serve read requests without detaching or switching over to the primary cluster. Distributing data geographically brings the data closer to you and decreases read latency. If slow or overloaded connections occur in one region, then you can route traffic to another region.

[Access control list (ACL) policies](https://docs.cloud.google.com/memorystore/docs/cluster/use-acl-policies) aren't replicated across regions in Memorystore for Redis Cluster. If you assign an ACL policy to a cross-region replication cluster, then you must manage the consistency for the policy in the different regions that are associated with the cluster.

To maintain consistency, update and delete each policy that's assigned to the primary and secondary clusters separately, and ensure that the rules for each policy are consistent. ACL policies aren't linked to one another so you can modify and delete policies in any order.

**Note** : To create a secondary cluster, you must have a service network policy in the region where you want the cluster to be located. For more information about service network policies, see [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking).

Also, for a conceptual overview of cross-region replication, see [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication).

## Create a secondary cluster

When you create a secondary cluster, Memorystore for Redis Cluster copies and applies some of the primary cluster settings as secondary cluster settings. For more information, see [Cluster settings](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication#cluster_settings).

You can create a secondary cluster in Memorystore for Redis Cluster by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click a primary cluster. The primary cluster is the parent of the secondary cluster that you're creating.

**Note** : Don't click a secondary cluster because Memorystore for Redis Cluster doesn't support cascading replicas. Also, don't click a primary cluster if it already has two secondary clusters because a primary cluster can have no more than two secondary clusters.

If no primary clusters appear, then [create a cluster](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances). After you create it, you can click it.

  3. In the side panel, click the **Secondary clusters** tab.

  4. Click **Add secondary cluster**.

  5. In the **Add secondary clusters** window, make the following changes:

     1. In the **Cluster ID** field, enter the ID of the secondary cluster that you're creating. The ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter, end with a lowercase letter or number, and be unique in its region.

     2. From the **Region** menu, select the region where you want the secondary cluster to be located.

     3. In the **Zonal availability** section, select one of the following options:

        * If you want all of the shards and replicas of the cluster to be distributed across three zones of the region where Memorystore for Redis Cluster creates the cluster, then select the **Multi-zone** option.

For example, if the region that you select is `us-central1`, and you select the **Multi-zone** option, then Memorystore for Redis Cluster distributes the cluster's shards and replicas across the `us-central1-a`, `us-central1-b`, and `us-central1-c` zones. In case of a zonal failure, the nodes in the cluster failover to the replicas.

        * If you want all of the shards and replicas of the cluster to be located in one zone of the region where Memorystore for Redis Cluster creates the cluster, select the **Single zone** option, and then select the zone from the **Zone** menu.

By using a single zone, you reduce network costs. However, in case of a zonal failure, failover doesn't occur.

     4. From the **Replicas** menu, select the number of replicas (per shard) for the cluster. You can have zero, one, or two replicas.

     5. From the **Network** menu, select a network for the cluster. For more information about networking for Memorystore for Redis Cluster, see [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking).

  6. Click **Add secondary cluster**.




### gcloud

**Note** : If you installed the gcloud CLI, then make sure that you have the latest version by running [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update). To manage cross-region replication for Memorystore for Redis Cluster, you need at least gcloud CLI version 488.0.0.

To create a secondary cluster, use the [`gcloud redis clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/create) command.
    
    
    gcloud redis clusters create CLUSTER_ID \
    --project=PROJECT_ID \
    --region=REGION_ID \
    --cross-cluster-replication-role=secondary \
    --network=NETWORK \
    --primary-cluster=PRIMARY_CLUSTER_PATH
    

Make the following replacements:

  * CLUSTER_ID: the ID of the secondary cluster that you're creating. The ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter, end with a lowercase letter or number, and be unique in its region.
  * PROJECT_ID: the ID of the project where you want to create the secondary cluster. This is the same project where the primary cluster is located.
  * REGION_ID: the ID of the region where you want the secondary cluster to be located.
  * NETWORK: the network used to create the cluster. It must use this format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID that you use must match the network ID that the [service connection policy](https://docs.cloud.google.com/memorystore/docs/cluster/networking#prerequisites_required_for_using_service_connection_policy_networking) uses. Otherwise, you can't create the secondary cluster.
  * PRIMARY_CLUSTER_PATH: the path of the primary cluster. For example: `projects/my-project/locations/us-central1/clusters/my-primary-cluster`. You can choose any cluster in your project to be the primary cluster, as long as it's not a secondary cluster.



For example:
    
    
    gcloud redis clusters create my-secondary-cluster \
    --project=my-project \
    --region=asia-east1 \
    --cross-cluster-replication-role=secondary \
    --network=projects/my-project/global/networks/default
    --primary-cluster=projects/my-project/locations/us-central1/clusters/my-primary-cluster
    

## View a secondary cluster

You can view summary information about a secondary cluster by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the expander arrow next to a primary cluster. This cluster is the parent of the secondary cluster about which you want to view information.

  3. Click the secondary cluster. Summary information about the cluster appears.




### gcloud

To view information about a secondary cluster, including a membership field that lists the primary and secondary clusters in the replication group, use the [`gcloud redis clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/describe) command.
    
    
    gcloud redis clusters describe CLUSTER_ID \
    --region=REGION_ID \
    

Make the following replacements:

  * CLUSTER_ID: the ID of the secondary cluster
  * REGION_ID: the ID of the region where the secondary cluster is located



## Perform a switchover

A switchover lets you reverse the roles of the primary and secondary clusters by promoting a secondary cluster to a primary cluster for disaster recovery purposes.

You can perform a switchover by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** Before you perform a switchover, follow the instructions in [Switchover best practices](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication#switchover_best_practices). Using these instructions, your application can keep track of the writes that it makes, and send the writes to the appropriate cluster.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the expander arrow next to a primary cluster. This cluster is the parent of the secondary cluster that you want to switchover.

  3. Click the secondary cluster.

  4. Click **Promote to Primary**.

  5. In the **Promote secondary cluster to primary?** dialog, enter the ID of the secondary cluster, and then click **Promote**.




After the switchover is complete, you must reconnect your applications to the new primary cluster.

### gcloud

To perform a switchover, use the [`gcloud redis clusters switchover`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/switchover) command.
    
    
    gcloud redis clusters switchover CLUSTER_ID \
    --project=PROJECT_ID \
    --region=REGION_ID \
    

Make the following replacements:

  * CLUSTER_ID: the ID of the secondary cluster that you want to switchover
  * PROJECT_ID: your project ID
  * REGION_ID: the ID of the region where the secondary cluster is located



After the switchover is complete, you must reconnect your applications to the new primary cluster.

## Detach secondary clusters

Detaching one or more secondary clusters from their primary cluster makes them fully functional independent clusters that allow both reads and writes. For more information, see [How to work with cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication#how_to_work_with_cross-region_replication).

You can detach secondary clusters by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Detach a secondary cluster

This section explains how to detach a secondary cluster from its primary cluster.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click a primary cluster. This is the parent of the secondary cluster that you're detaching from the primary cluster.

  3. In the side panel, click the **Secondary clusters** tab.

  4. Select the checkbox next to the ID of the secondary cluster that you're detaching from the primary cluster.

  5. Click **Detach from Primary**.

  6. In the **Detach secondary cluster?** dialog, enter the ID of the secondary cluster, and then click **Detach**.




### gcloud

To detach a secondary cluster, use the [`gcloud redis clusters detach`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/detach) command.
    
    
    gcloud redis clusters detach CLUSTER_ID \
    --project=PROJECT_ID \
    --region=REGION_ID
    

Make the following replacements:

  * CLUSTER_ID: the ID of the secondary cluster that you want to detach
  * PROJECT_ID: your project ID
  * REGION_ID: the ID of the region where the secondary cluster is located



### Detach multiple secondary clusters

This section explains how to detach multiple secondary clusters from their primary cluster. You can also use the procedure in this section to detach an unavailable secondary cluster from its primary cluster.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click a primary cluster. This is the parent of the secondary clusters that you're detaching from the primary cluster.

  3. In the side panel, click the **Secondary clusters** tab.

  4. Select the checkboxes next to the IDs of the secondary clusters that you're detaching from the primary cluster.

  5. Click **Detach from Primary**.

  6. In the **Detach secondary clusters?** dialog, do the following:

     1. Enter the IDs of the secondary clusters. Use commas to separate the IDs.

     2. Click **Detach**.




### gcloud

To detach multiple secondary clusters, use the [`gcloud redis clusters detach-secondaries`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/detach-secondaries) command.
    
    
    gcloud redis clusters detach-secondaries PRIMARY_CLUSTER_ID \
    --clusters-to-detach=SECONDARY_CLUSTERS \
    --project=PROJECT_ID \
    --region=PRIMARY_CLUSTER_REGION_ID
    

Make the following replacements:

  * PRIMARY_CLUSTER_ID: the ID of the primary cluster.
  * SECONDARY_CLUSTERS: the secondary clusters that you want to detach. Use commas to separate the cluster IDs. Each secondary cluster must have this format: `projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID`.
  * PROJECT_ID: your project ID.
  * PRIMARY_CLUSTER_REGION: the ID of the region where your primary cluster is located.



For example:
    
    
    gcloud redis clusters detach-secondaries my-primary-cluster \
    --clusters-to-detach=projects/my-project/locations/us-west4/clusters/my-secondary-cluster-1,projects/my-project/locations/asia-southeast2/clusters/my-secondary-cluster-2  \
    --project=my-project \
    --region=us-central1
    

## Update cluster settings

This section provides links to update cluster settings. The process for updating cluster settings is different, depending on whether you change settings on the primary cluster or secondary cluster. For more information about how to update settings, see [Cluster settings](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication#cluster_settings).

### Update settings on the primary cluster

You must change the following settings on the primary cluster. After you do, Memorystore for Redis Cluster synchronizes the changes to the secondary clusters.

  * [Scale the cluster's capacity](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity)
  * [Configure the cluster](https://docs.cloud.google.com/memorystore/docs/cluster/configure-instances)
  * [Prevent the deletion of the cluster](https://docs.cloud.google.com/memorystore/docs/cluster/deletion-protection)
  * [Manage persistence for the cluster](https://docs.cloud.google.com/memorystore/docs/cluster/manage-persistence)



### Update settings on the secondary cluster

You must change the following settings on the secondary cluster:

  * [Configure whether the cluster is single-zone or multi-zone](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances)
  * [Scale the cluster's replica count](https://docs.cloud.google.com/memorystore/docs/cluster/scale-replica-count)
  * [Set maintenance windows for the cluster](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows)



## Delete clusters that use cross-region replication

This section explains how to delete primary and secondary clusters that use cross-region replication.

### Delete a primary cluster

To delete a primary cluster, do the following:

  1. Detach or delete all secondary clusters.
  2. To delete the primary cluster, follow the instructions at [Delete clusters](https://docs.cloud.google.com/memorystore/docs/cluster/delete-instances).



To protect against accidental deletion, you can't delete primary and secondary clusters simultaneously.

### Delete a secondary cluster

To delete a secondary cluster, follow the instructions at [Delete clusters](https://docs.cloud.google.com/memorystore/docs/cluster/delete-instances). For the cluster ID, use the ID of the secondary cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
