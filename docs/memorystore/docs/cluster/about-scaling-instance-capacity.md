---
url: https://docs.cloud.google.com/memorystore/docs/cluster/about-scaling-instance-capacity/
title: About scaling cluster capacity \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:24.938574+00:00
---

# About scaling cluster capacity  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/about-scaling-instance-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  About scaling cluster capacity Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how your cluster in Memorystore for Redis Cluster behaves during scaling.

You can scale the capacity for your cluster in the following ways:

  * You can change the number of shards for your cluster. This is _horizontal scaling_. You can scale a cluster horizontally in one of the following ways:

    * **Scale out** : increase the capacity of your cluster, which gives the cluster more memory and processing power to handle a larger volume of data or traffic. Your cluster's capacity is determined by the number of shards in your cluster.

By scaling your cluster out, your application can handle an increased demand without performance degradation. To scale a cluster out, add shards to the cluster.

    * **Scale in** : reduce the capacity of your cluster, which decreases both the processing power and the amount of memory available to store data. This occurs when your application's data demands decrease and you need to lower your resource usage to save costs. To scale a cluster in, reduce the number of shards in the cluster.

  * You can change the node type for your cluster. This is _vertical scaling_. You can scale a cluster vertically in one of the following ways:

    * **Scale up** : increase the capacity of your cluster. Your cluster's capacity is determined by your cluster's node type. To scale a cluster up, change the node type to a larger node type. For example, scale your cluster up from a `redis-standard-small` node type to a `redis-highmem-medium` node type.
    * **Scale down** : reduce the capacity of your cluster. To scale a cluster down, change the node type to a smaller node type. For example, scale your cluster down from a `redis-highmem-medium` node type to a `redis-standard-small` node type.

**Important:** If you want to scale the node type for your cluster down, and you haven't overwritten the default settings for the original node type, then Memorystore for Redis Cluster modifies the default settings to those of the scaled node type.

**Note:** For more information about the different types and sizes of shards and nodes, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification). To learn more about scaling a cluster, see [Scale cluster capacity](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity).

## Impact of scaling

During a scaling operation, the availability of your cluster isn't impacted. However, when you change the number of shards in your cluster, Memorystore for Redis Cluster rebalances the cluster's keyspace. This might cause increased latency during the scaling operation.

Also, the impact of scaling your cluster vertically by changing the node type is similar to what happens with a [maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance) operation.

## Failure scenarios

If you encounter an error during the scaling operation, then it's likely because of one of the following scenarios:

  * You want to update the shard count for your cluster, but you don't have enough free memory for the `redis-shared-core-nano` node type for your cluster.

To resolve this issue, you can either [scale your cluster up](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity#scale_the_node_type) or free memory from the nodes of your cluster. To free memory, do the following:

    1. [Connect to a cluster](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance).
    2. To get details about the cluster, including the IP address and port number, use the [`gcloud redis clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/describe) command.
    3. Make a note of the IP address and port number of the cluster.
    4. To get information about the nodes of the cluster, use the following command:
           
           redis-cli -h IP_ADDRESS -p PORT_NUMBER cluster nodes
           

Replace IP_ADDRESS and PORT_NUMBER with the values that you noted in the previous step.

    5. Make a note of the IP address and port number of a node that doesn't have enough free space. This node's ID matches an ID that appears in the error.

    6. To connect to this node, use the following command:
           
           redis-cli -h IP_ADDRESS -p PORT_NUMBER
           

Replace IP_ADDRESS and PORT_NUMBER with the values that you noted in the previous step.

    7. At the prompt, enter the `info memory` command.

In the output, values for the `used_memory` and `maxmemory` parameters appear. `used_memory` is how much memory the node uses and `maxmemory` is how much memory is available for the node.

    8. Divide the value of the `used_memory` parameter by the value of the `maxmemory` parameter, and verify that the quotient is greater than 98%.

    9. To free up space for the node, [delete some of the node's keys](https://redis.io/docs/latest/commands/del/).

    10. Enter the `info memory` command again. In the output, the value of the `used_memory` parameter is smaller.

    11. Divide the value of the `used_memory` parameter by the value of the `maxmemory` parameter, and verify that the quotient is now less than 98%. If it isn't, then delete more keys.

    12. For any other nodes that don't have enough free space, repeat steps 4 - 11 of this procedure.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type. For more information about these node types, see [Choose a node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type).
  * You scaled to a smaller shard count that doesn't have the capacity to hold all of the keys that Memorystore for Redis Cluster stores in the original cluster. To resolve this, scale to a larger shard count that can hold all of the stored keys. For more information about increasing the number of shards for your cluster, see [Scale the shard count](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity#scale_the_shard_count).

  * You scaled to a smaller node type that doesn't have the capacity to hold all of the data that Memorystore for Redis Cluster stores in the original node type. If this occurs, then Memorystore for Redis Cluster provides you with a recommended node type to scale down vertically.

  * You updated the node type for your cluster and either you overwrite the default [settings](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations) for the original node type or these settings are overwritten already. However, the new, scaled node type either doesn't support the values for the default settings or the settings aren't valid for the node type. If this occurs, then Memorystore for Redis Cluster returns an error. To resolve this, modify the settings manually so that they're valid for the new node type.

  * You scaled your cluster during a period of high write pressure (for example, during load testing). To resolve this, scale during periods of low cluster traffic.

  * You have a slot which contains a large key, and you want to migrate this key to another node. However, this node doesn't have sufficient memory to support the key. You can't update your cluster. To resolve this, reduce the size of the key so that it's less than 128 MB. Then, retry the update operation.

  * The slot number that a node of a cluster owns isn't known, but only the slot range is known. Memorystore for Redis Cluster returns an error message. If this occurs, then reduce the size of the key and retry the update operation.

  * You increased the capacity of your cluster by scaling out to a smaller shard count. However, Memorystore for Redis Cluster doesn't have enough memory to accommodate this request. To resolve this, reduce the capacity of your cluster by scaling in to the original, larger shard count.




## Best practices

To help you scale the capacity for your cluster, we recommend the following best practices:

  * **Choose when to scale** : to increase the speed and reliability of scaling your cluster, scale it during low periods of traffic. To learn how to monitor cluster traffic, see [Monitor clusters](https://docs.cloud.google.com/memorystore/docs/cluster/monitor-instances).
  * **Retry when you can't scale** : resource availability changes frequently. If you can't scale your cluster because of a temporary resource constraint, then try to scale the cluster later.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
