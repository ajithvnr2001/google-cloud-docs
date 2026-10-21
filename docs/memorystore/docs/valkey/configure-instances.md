---
url: https://docs.cloud.google.com/memorystore/docs/valkey/configure-instances/
title: Configure an instance \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:19.851936+00:00
---

# Configure an instance  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/configure-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Configure an instance Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Valkey supports a subset of the [OSS Valkey configuration parameters](https://github.com/valkey-io/valkey/blob/7.2/valkey.conf) that you can modify to customize the behavior of your instance.

Configuration changes don't require a restart of the nodes, and are saved if a node restarts. After creating an instance, you can update the modifiable configuration parameters.

For more information about the modifiable configuration parameters, see [Supported instance configurations](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations).

## Before you begin

Ensure that you have installed the latest version of the Google Cloud CLI by running `gcloud components update`.

## View configuration parameters

To view configuration parameters using the Google Cloud CLI, run the `gcloud memorystore instances describe` command, replacing variables with appropriate values.

You can't see configuration parameters when running the `gcloud memorystore instances describe` command unless you change a configuration parameter from its default value.
    
    
    gcloud memorystore instances describe instance-id --location=region-id
    

Example:
    
    
    gcloud memorystore instances describe my-instance --location=us-central1
    

## Set a configuration parameter during instance creation

To set a configuration parameter while creating an instance, run the `gcloud memorystore instances create` command with `--engine-configs` flag, replacing variables with appropriate values.
    
    
    gcloud memorystore instances create instance-id \
    --location=region-id \
    --project=project-id \
    --node-type=node-type \
    --shard-count=shard-count \
    --mode=MODE
    --engine-configs=config-name=config-value \
    

Replace the following:

  * instance-id is the ID of the Memorystore for Valkey instance you're creating.
  * region-id is the region where you want the instance placed.
  * project-id is your project ID.
  * node-type is the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) for the instance.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  * shard-count determines the number of shards in your instance. Shard count determines the total memory capacity for storing instance data. If the mode that you select is Cluster Mode Disabled, then you can specify only one shard for your instance. For more information, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  * mode determines if the instance is Cluster Mode Enabled or Cluster Mode Disabled. If this field is omitted, then the instance defaults to Cluster Mode Enabled. For more information, see [Enable and disable Cluster Mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

  * config-name is the configuration parameter to modify.

  * config-value is your chosen setting corresponding to the parameter you're configuring.




For example:

### Cluster Mode Enabled example
    
    
      gcloud memorystore instances create foo --location=us-east1 --project=test-proj --node-type=highmem-medium --shard-count=3 --engine-configs=maxmemory-policy=allkeys-lru
      

### Cluster Mode Disabled example
    
    
      gcloud memorystore instances create foo --location=us-east1 --project=test-proj --node-type=highmem-medium --shard-count=1 --mode=cluster-disabled --engine-configs=maxmemory-policy=allkeys-lru
      

## Update a configuration parameter

To update a configuration parameter for an existing instance, run the `gcloud memorystore instances update` command with the `--update-engine-configs` flag, replacing variables with appropriate values.
    
    
    gcloud memorystore instances update instance-id \
    --location=region-id \
    --project=project-id \
    --update-engine-configs=config-name=config-value
    

Example:
    
    
    gcloud memorystore instances update foo --location=us-east1 --project=test-proj --update-engine-configs=maxmemory-policy=allkeys-lru
    

**Note** : For more information about which configuration parameters you can update, see [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters).

## Reset a configuration parameter

To reset a configuration parameter to its default value, run the `gcloud memorystore instances update` command with the `--remove-engine-configs` flag, replacing variables with appropriate values.
    
    
    gcloud memorystore instances update instance-id \
    --location=region-id \
    --project=project-id \
    --remove-engine-configs=config-name
    

Example:
    
    
    gcloud memorystore instances update foo --location=us-east1 --project=test-proj --remove-engine-configs=maxmemory-policy
    

## Clear configuration parameters

To clear all configuration parameters to their default values, run the `gcloud memorystore instances update` command with the `--clear-engine-configs` flag, replacing variables with appropriate values.
    
    
    gcloud memorystore instances update instance-id \
    --location=region-id \
    --project=project-id \
    --clear-engine-configs
    

Example:
    
    
    gcloud memorystore instances update foo --location=us-east1 --project=test-proj --clear-engine-configs
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
