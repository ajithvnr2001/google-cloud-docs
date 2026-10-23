---
url: https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity/
title: Scale instance capacity \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:39.241079+00:00
---

# Scale instance capacity  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Scale instance capacity Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to scale a Memorystore for Valkey instance. Your instance's capacity is determined by the number of shards in your instance and your instance's [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification). To scale your instance, you must change the shard count or node type. For more information about an instance's behavior during scaling, see [About scaling instance capacity](https://docs.cloud.google.com/memorystore/docs/valkey/about-scaling-instance-capacity).

## Scale the shard count

You can increase or decrease the number of shards for an instance by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** If you specify **Cluster Mode Enabled** when you [create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#create_a_multi-zone_instance), then you can scale the shard count for the instance. If you specify **Cluster Mode Disabled** , then Memorystore for Valkey doesn't partition the instance, but hosts it on a single shard. Therefore, you can't scale the number of the shards for the instance.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click your instance ID.

  3. In the **Configurations** section, click the pencil icon next to **Shards**.

  4. In the **Shards** field, enter the number of shards to which you want to scale your instance.

  5. Click **Update instance**.




### gcloud

To scale the number of shards for an instance, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command:
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --location=REGION_ID \
    --shard-count=SHARD_COUNT
    

Replace the following:

  * INSTANCE_ID: the ID of your instance.
  * REGION_ID: the region where your instance is located.
  * SHARD_COUNT: the number of shards in your instance. The shard count determines the total memory capacity for storing instance data. For more information about instance and node specifications for Memorystore for Valkey instances, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).



For example:
    
    
    gcloud memorystore instances update my-instance \
    --location=us-central1 \
    --shard-count=8
    

## Scale the node type

You can scale the node type for an instance by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### gcloud

  1. To retrieve information about an instance, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command:
         
         gcloud memorystore instances describe INSTANCE_ID \
         --location=REGION_ID
         

Replace the following:

     * INSTANCE_ID: the ID of your instance
     * REGION_ID: the region where your instance is located (for example, `us-central1`)
  2. Check the output to see if the following conditions exist:

     1. The output contains an `engineConfigs` section.

     2. The `maxmemory-clients`, `maxmemory`, or `maxclients` parameters appear in this section.

If any of these parameters appear, then when you scale the node type for the instance, you must scale the values for the parameters to reflect values that Memorystore for Valkey can accept for the scaled node type. For more information, see [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters).

  3. To scale the node type, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command:
         
         gcloud memorystore instances update INSTANCE_ID \
         --location=REGION_ID \
         --node-type=NODE_TYPE
         

Replace the following:

     * INSTANCE_ID: the ID of your instance.
     * REGION_ID: the region where your instance is located.
     * NODE_TYPE: the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) to which you want to scale your instance.

**Note:** You can't scale your instance down to the `shared-core-nano` node type.**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.

For this example, you scale the node type of the `my-instance` instance to `highmem-medium`. This instance is located in the `us-central1` region.
    
    gcloud memorystore instances update my-instance \
    --location=us-central1 \
    --node-type=highmem-medium
    

For this example, you change the value of the `maxclients` parameter to `15,000`.
    
    gcloud memorystore instances update my-instance \
    --location=us-central1 \
    --node-type=highmem-medium \
    --update-engine-configs=maxclients=15000
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
