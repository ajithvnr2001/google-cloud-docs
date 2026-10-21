---
url: https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity/
title: Scale cluster capacity \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:09.112207+00:00
---

# Scale cluster capacity  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Scale cluster capacity Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to scale a cluster in Memorystore for Redis Cluster. Your cluster's capacity is determined by the number of shards in your cluster and your cluster's [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification). To scale your cluster, you must change the shard count or node type. For more information about a cluster's behavior during scaling, see [About scaling cluster capacity](https://docs.cloud.google.com/memorystore/docs/cluster/about-scaling-instance-capacity).

## Scale the shard count

You can increase or decrease the number of shards for a cluster by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click your cluster ID.

  3. In the **Configurations** section, click the pencil icon next to **Shards**.

  4. In the **Shards** field, enter the number of shards to which you want to scale your cluster.

  5. Click **Update cluster**.




### gcloud

To scale the number of shards for a cluster, use the [`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command:
    
    
    gcloud redis clusters update CLUSTER_ID \
    --region=REGION_ID \
    --shard-count=SHARD_COUNT
    

Replace the following:

  * CLUSTER_ID: the ID of your cluster.
  * REGION_ID: the region where your cluster is located.
  * SHARD_COUNT: the number of shards in your cluster. The shard count determines the total memory capacity for storing cluster data. For more information about cluster and node specifications for clusters, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).



For example:
    
    
    gcloud redis clusters update my-cluster \
    --region=us-central1 \
    --shard-count=8
    

## Scale the node type

You can scale the node type for a cluster by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### gcloud

  1. To retrieve information about a cluster, use the [`gcloud redis clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/describe) command:
         
         gcloud redis clusters describe CLUSTER_ID \
         --region=REGION_ID
         

Replace the following:

     * CLUSTER_ID: the ID of your cluster
     * REGION_ID: the region where your cluster is located (for example, `us-central1`)
  2. Check the output to see if the following conditions exist:

     1. The output contains a `redisConfigs` section.

     2. The `maxmemory-clients`, `maxmemory`, or `maxclients` parameters appear in this section.

If any of these parameters appear, then when you scale the node type for the cluster, you must scale the values for the parameters to reflect values that Memorystore for Redis Cluster can accept for the scaled node type. For more information, see [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters).

  3. To scale the node type, use the [`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command:
         
         gcloud redis clusters update CLUSTER_ID \
         --region=REGION_ID \
         --node-type=NODE_TYPE
         

Replace the following:

     * CLUSTER_ID: the ID of your cluster
     * REGION_ID: the region where your cluster is located
     * NODE_TYPE: the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) to which you want to scale your cluster

**Note:** You can't scale your cluster down to the `redis-shared-core-nano` node type.**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.

For this example, you scale the node type of the `my-cluster` cluster to `redis-highmem-medium`. This cluster is located in the `us-central1` region.
    
    gcloud redis clusters update my-cluster \
    --region=us-central1 \
    --node-type=redis-highmem-medium
    

For this example, you change the value of the `maxclients` parameter to `15,000`.
    
    gcloud redis clusters update my-cluster \
    --region=us-central1 \
    --node-type=redis-highmem-medium \
    --update-redis-config=maxclients=15000
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
