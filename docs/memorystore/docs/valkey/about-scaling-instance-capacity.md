---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-scaling-instance-capacity/
title: About scaling instance capacity \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:24.979831+00:00
---

# About scaling instance capacity  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-scaling-instance-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About scaling instance capacity Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how your Memorystore for Valkey instance behaves during scaling.

You can scale the capacity for your instance in the following ways:

  * You can change the number of shards for your instance. This is _horizontal scaling_. You can scale an instance horizontally in one of the following ways:

    * **Scale out** : increase the capacity of your instance, which gives the instance more memory and processing power to handle a larger volume of data or traffic. Your instance's capacity is determined by the number of shards in your instance.

By scaling your instance out, your application can handle an increased demand without performance degradation. To scale an instance out, add shards to the instance.

    * **Scale in** : reduce the capacity of your instance, which decreases both the processing power and the amount of memory available to store data. This occurs when your application's data demands decrease and you need to lower your resource usage to save costs. To scale an instance in, reduce the number of shards in the instance.

**Note:** If you specify **Cluster Mode Disabled** when you [ create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#create_a_multi-zone_instance), then Memorystore for Valkey doesn't partition the instance, but hosts it on a single shard. Therefore, horizontal scaling doesn't apply for the instance.
  * You can change the node type for your instance. This is _vertical scaling_. You can scale an instance vertically in one of the following ways:

    * **Scale up** : increase the capacity of your instance. Your instance's capacity is determined by your instance's node type. To scale an instance up, change the node type to a larger node type. For example, scale your instance up from a `standard-small` node type to a `highmem-medium` node type.
    * **Scale down** : reduce the capacity of your instance. To scale an instance down, change the node type to a smaller node type. For example, scale your instance down from a `highmem-medium` node type to a `standard-small` node type.

**Important:** If you want to scale the node type for your instance down, and you haven't overwritten the default settings for the original node type, then Memorystore for Valkey modifies the default settings to those of the scaled node type.


**Note:** For more information about the different types and sizes of shards and nodes, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification). To learn more about scaling a Memorystore for Valkey instance, see [Scale instance capacity](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity).

## Impact of scaling

During a scaling operation, the availability of your instance isn't impacted. However, when you change the number of shards in your instance, Memorystore for Valkey rebalances the instance's keyspace. This might cause increased latency during the scaling operation.

Also, the impact of scaling your instance vertically by changing the node type is similar to what happens with a [maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance) operation.

## Failure scenarios

If you encounter an error during the scaling operation, then it's likely because of one of the following scenarios:

  * You want to update the shard count for your instance, but you don't have enough free memory for the `shared-core-nano` node type for your instance.

To resolve this issue, you can either [scale your instance up](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_node_type) or free memory from the nodes of your instance. To free memory, do the following:

    1. [Connect to a Memorystore for Valkey instance](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance).
    2. To get details about the instance, including the IP address and port number, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command.
    3. Make a note of the IP address and port number of the instance.
    4. To get information about the nodes of the instance, use the following command:
           
           valkey-cli -h IP_ADDRESS -p PORT_NUMBER cluster nodes
           

Replace IP_ADDRESS and PORT_NUMBER with the values that you noted in the previous step.

    5. Make a note of the IP address and port number of a node that doesn't have enough free space. This node's ID matches an ID that appears in the error.

    6. To connect to this node, use the following command:
           
           valkey-cli -h IP_ADDRESS -p PORT_NUMBER
           

Replace IP_ADDRESS and PORT_NUMBER with the values that you noted in the previous step.

    7. At the prompt, enter the `info memory` command.

In the output, values for the `used_memory` and `maxmemory` parameters appear. `used_memory` is how much memory the node uses and `maxmemory` is how much memory is available for the node.

    8. Divide the value of the `used_memory` parameter by the value of the `maxmemory` parameter, and verify that the quotient is greater than 98%.

    9. To free up space for the node, [delete some of the node's keys](https://valkey.io/commands/del/).

    10. Enter the `info memory` command again. In the output, the value of the `used_memory` parameter is smaller.

    11. Divide the value of the `used_memory` parameter by the value of the `maxmemory` parameter, and verify that the quotient is now less than 98%. If it isn't, then delete more keys.

    12. For any other nodes that don't have enough free space, repeat steps 4 - 11 of this procedure.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type. For more information about these node types, see [Choose a node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type).
  * You scaled to a smaller shard count that doesn't have the capacity to hold all of the keys that Memorystore for Valkey stores in the original instance. To resolve this, scale to a larger shard count that can hold all of the stored keys. For more information about increasing the number of shards for your instance, see [Scale the shard count](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_shard_count).

  * You scaled to a smaller node type that doesn't have the capacity to hold all of the data that Memorystore for Valkey stores in the original node type. If this occurs, then Memorystore for Valkey provides you with a recommended node type to scale down vertically.

  * You updated the node type for your instance, and either you overwrite the default [settings](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations) for the original node type or these settings are overwritten already. However, the new, scaled node type either doesn't support the values for the default settings or the settings aren't valid for the node type. If this occurs, then Memorystore for Valkey returns an error. To resolve this, modify the settings manually so that they're valid for the new node type.

  * You scaled your instance during a period of high write pressure (for example, during load testing). To resolve this, scale during periods of low instance traffic.

  * You have a slot which contains a large key, and you want to migrate this key to another node. However, this node doesn't have sufficient memory to support the key. You can't update your instance. To resolve this, reduce the size of the key so that it's less than 128 MB. Then, retry the update operation.

  * The slot number that a node of an instance owns isn't known, but only the slot range is known. Memorystore for Valkey returns an error message. If this occurs, then reduce the size of the key and retry the update operation.

  * You increased the capacity of your instance by scaling out to a smaller shard count. However, Memorystore for Valkey doesn't have enough memory to accommodate this request. To resolve this, reduce the capacity of your instance by scaling in to the original, larger shard count.




## Best practices

To help you scale the capacity for your instance, we recommend the following best practices:

  * **Choose when to scale** : to increase the speed and reliability of scaling your instance, scale it during low periods of traffic. To learn how to monitor instance traffic, see [Monitor instances](https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances).
  * **Retry when you can't scale** : resource availability changes frequently. If you can't scale your instance because of a temporary resource constraint, then try to scale the instance later.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
