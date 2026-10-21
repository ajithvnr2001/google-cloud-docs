---
url: https://docs.cloud.google.com/memorystore/docs/cluster/configure-instances/
title: Configure a cluster \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:08.194287+00:00
---

# Configure a cluster  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/configure-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Configure a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Redis Cluster supports a subset of the [Redis configuration parameters](https://redis.io/topics/config) that you can modify to customize the behavior of your cluster.

Configuration changes don't require you to restart the cluster, and they don't interrupt the service. Memorystore for Redis Cluster saves your changes immediately. If the cluster restarts, then the cluster retains your configuration changes. After creating a cluster, you can update the modifiable configuration parameters. For more information, see [Supported cluster configurations](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations).

## Before you begin

Make sure that you install the latest version of the Google Cloud CLI. To update an existing installation, use the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command.

## View configuration parameters

To view configuration parameters, use the [`gcloud redis clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/describe) command.
    
    
    gcloud redis clusters describe CLUSTER_ID --region=REGION_ID
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster
  * REGION_ID: the region where the cluster is located



For example:
    
    
    gcloud redis clusters describe my-cluster --region=us-central1
    

If you don't change any configuration parameters from their default values, then the parameters don't appear in the output.

## Set a configuration parameter when you create a cluster

To set a configuration parameter when you create a cluster, use the  
[`gcloud redis clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/create) command with the `--redis-config` flag.
    
    
    gcloud redis clusters create CLUSTER_ID \
    --region=REGION_ID \
    --project=PROJECT_ID \
    --network=NETWORK \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --redis-config=CONFIG_NAME=CONFIG_VALUE
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that you're creating.
  * REGION_ID: the region where you want the cluster to be located.
  * PROJECT_ID: your project ID.
  * NETWORK: the name or fully qualified path of the Virtual Private Cloud (VPC) network to which the cluster connects.
  * NODE_TYPE: the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * SHARD_COUNT: the number of shards in your cluster. The shard count determines the total memory capacity for storing cluster data.

  * CONFIG_NAME: the name of the configuration parameter that you want to set.

  * CONFIG_VALUE: the value of the parameter that you're setting.




For example:
    
    
    gcloud redis clusters create my-cluster --region=us-east1 --project=my-project --network=projects/my-project/global/networks/default --node-type=redis-highmem-medium --shard-count=3 --redis-config=maxmemory-policy=allkeys-lru
    

## Update a configuration parameter

To update a configuration parameter for an existing cluster, use the  
[`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command with the `--update-redis-config` flag.
    
    
    gcloud redis clusters update CLUSTER_ID \
    --region=REGION_ID \
    --project=PROJECT_ID \
    --update-redis-config=CONFIG_NAME=CONFIG_VALUE
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster
  * REGION_ID: the region where the cluster is located
  * PROJECT_ID: your project ID
  * CONFIG_NAME: the name of the configuration parameter that you want to update
  * CONFIG_VALUE: the new value of the parameter



For example:
    
    
    gcloud redis clusters update my-cluster --region=us-east1 --project=my-project --update-redis-config=maxmemory-policy=allkeys-lru
    

For more information about which configuration parameters you can update, see [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters).

## Reset a configuration parameter

To reset a configuration parameter to its default value, use the  
[`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command with the `--remove-redis-config` flag.
    
    
    gcloud redis clusters update CLUSTER_ID \
    --region=REGION_ID \
    --project=PROJECT_ID \
    --remove-redis-config=CONFIG_NAME
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster
  * REGION_ID: the region where the cluster is located
  * PROJECT_ID: your project ID
  * CONFIG_NAME: the name of the configuration parameter that you want to reset to its default value



For example:
    
    
    gcloud redis clusters update my-cluster --region=us-east1 --project=my-project --remove-redis-config=maxmemory-policy
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
