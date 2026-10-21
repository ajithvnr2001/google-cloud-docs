---
url: https://docs.cloud.google.com/memorystore/docs/cluster/configure-instances/
title: Configure an instance \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:54:58.489860+00:00
---

# Configure an instance  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/configure-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Configure an instance Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Redis Cluster supports a subset of the [native Redis configuration parameters](https://redis.io/topics/config) that you can modify to customize the behavior of your instance.

Configuration changes don't require you to restart the instance and the service isn't interrupted. If you restart the instance, then Memorystore for Redis Cluster saves the changes. After creating the instance, you can update any configuration parameters that are modifiable.

For more information about the modifiable configuration parameters, see [Supported instance configurations](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations).

## Before you begin

Ensure that you have installed the latest version of the Google Cloud CLI by running `gcloud components update`.

## View configuration parameters

To view configuration parameters using the Google Cloud CLI, run the `gcloud redis clusters describe` command replacing variables with appropriate values.

You can't see configuration parameters when running the `gcloud redis clusters describe` command unless you have changed a configuration parameter from its default value.
    
    
    gcloud redis clusters describe instance-id --region=region-id
    

Example:
    
    
    gcloud redis clusters describe my-instance --region=us-central1
    

## Set a configuration parameter during cluster creation

To set a configuration parameter while creating a cluster, run the `gcloud redis clusters create` command with `--redis-config` flag replacing variables with appropriate values.
    
    
    gcloud redis clusters create instance-id \
    --region=region-id \
    --project=project-id \
    --node-type=node-type \
    --shard-count=shard-count \
    --redis-config=config-name=config-value \
    

Replace the following:

  * instance-id is the ID of the Memorystore for Redis Cluster instance you're creating.
  * region-id is the region where you want the instance placed.
  * project-id is your project ID.
  * node-type is the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * shard-count determines the number of shards in your instance. Shard count determines the total memory capacity for storing cluster data. To see more details about cluster specification, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  * config-name is the configuration parameter to modify.

  * config-value is your chosen setting corresponding to the parameter you're configuring.

**Note** : For more information about modifying configuration parameters for your instance, see [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters).



For example:
    
    
    gcloud redis clusters create foo --region=us-east1 --project=test-proj --node-type=redis-highmem-medium --shard-count=3 --redis-config=maxmemory-policy=allkeys-lru
    

## Update a configuration parameter

To update a configuration parameter for an existing instance, run the `gcloud redis clusters update` command with the `--update-redis-config` flag replacing variables with appropriate values.
    
    
    gcloud redis clusters update instance-id \
    --region=region-id \
    --project=project-id \
    --update-redis-config=config-name=config-value
    

Example:
    
    
    gcloud redis clusters update foo --region=us-east1 --project=test-proj --update-redis-config=maxmemory-policy=allkeys-lru
    

## Reset a configuration parameter

To reset a configuration parameter to its default value, run the `gcloud redis clusters update` command with the `--remove-redis-config` flag replacing variables with appropriate values.
    
    
    gcloud redis clusters update instance-id \
    --region=region-id \
    --project=project-id \
    --remove-redis-config=config-name
    

Example:
    
    
    gcloud redis clusters update foo --region=us-east1 --project=test-proj --remove-redis-config=maxmemory-policy
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
