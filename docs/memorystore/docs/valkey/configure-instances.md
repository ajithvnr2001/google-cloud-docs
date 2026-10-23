---
url: https://docs.cloud.google.com/memorystore/docs/valkey/configure-instances/
title: Configure an instance \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:57.664806+00:00
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

Memorystore for Valkey supports a subset of the [Valkey configuration parameters](https://github.com/valkey-io/valkey/blob/7.2/valkey.conf) that you can modify to customize the behavior of your instance.

Configuration changes don't require you to restart the instance, and they don't interrupt the service. Memorystore for Valkey saves your changes immediately. If the instance restarts, then the instance retains your configuration changes. After creating an instance, you can update the modifiable configuration parameters. For more information, see [Supported instance configurations](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations).

## Before you begin

Make sure that you install the latest version of the Google Cloud CLI. To update an existing installation, use the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command.

## View configuration parameters

To view configuration parameters, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command.
    
    
    gcloud memorystore instances describe INSTANCE_ID --location=REGION_ID
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance
  * REGION_ID: the region where the instance is located



For example:
    
    
    gcloud memorystore instances describe my-instance --location=us-central1
    

If you don't change any configuration parameters from their default values, then the parameters don't appear in the output.

## Set a configuration parameter when you create an instance

To set a configuration parameter when you create an instance, use the  
[`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command with the `--engine-configs` flag.
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --location=REGION_ID \
    --project=PROJECT_ID \
    --node-type=NODE_TYPE \
    --mode=MODE \
    --shard-count=SHARD_COUNT \
    --engine-configs=CONFIG_NAME=CONFIG_VALUE
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance that you're creating.
  * REGION_ID: the region where you want the instance to be located.
  * PROJECT_ID: your project ID.
  * NODE_TYPE: the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) for the instance.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  * MODE: whether you're creating a Cluster Mode Enabled or Cluster Mode Disabled instance. If you omit this field, then by default, Memorystore for Valkey creates a Cluster Mode Enabled instance. For more information, see [Enable and disable cluster mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

  * SHARD_COUNT: the number of shards in your instance. The shard count determines the total memory capacity for storing instance data.

If the mode that you select is Cluster Mode Disabled, then you can specify only one shard for your instance. For more information, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  * CONFIG_NAME: the name of the configuration parameter that you want to set.

  * CONFIG_VALUE: the value of the parameter that you're setting.




For example:

### Cluster Mode Enabled example
    
    
      gcloud memorystore instances create my-instance --location=us-east1 --project=my-project --node-type=highmem-medium --shard-count=3 --engine-configs=maxmemory-policy=allkeys-lru
      

### Cluster Mode Disabled example
    
    
      gcloud memorystore instances create my-instance --location=us-east1 --project=my-project --node-type=highmem-medium --mode=cluster-disabled --shard-count=1 --engine-configs=maxmemory-policy=allkeys-lru
      

## Update a configuration parameter

To update a configuration parameter for an existing instance, use the  
[`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command with the `--update-engine-configs` flag.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --location=REGION_ID \
    --project=PROJECT_ID \
    --update-engine-configs=CONFIG_NAME=CONFIG_VALUE
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance
  * REGION_ID: the region where the instance is located
  * PROJECT_ID: your project ID
  * CONFIG_NAME: the name of the configuration parameter that you want to update
  * CONFIG_VALUE: the new value of the parameter



For example:
    
    
    gcloud memorystore instances update my-instance --location=us-east1 --project=my-project --update-engine-configs=maxmemory-policy=allkeys-lru
    

For more information about which configuration parameters you can update, see [ Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters).

## Reset a configuration parameter

To reset a configuration parameter to its default value, use the  
[`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command with the `--remove-engine-configs` flag.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --location=REGION_ID \
    --project=PROJECT_ID \
    --remove-engine-configs=CONFIG_NAME
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance
  * REGION_ID: the region where the instance is located
  * PROJECT_ID: your project ID
  * CONFIG_NAME: the name of the configuration parameter that you want to reset to its default value



For example:
    
    
    gcloud memorystore instances update my-instance --location=us-east1 --project=my-project --remove-engine-configs=maxmemory-policy
    

## Reset all configuration parameters

To reset all configuration parameters to their default values, use the  
[`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command with the `--clear-engine-configs` flag.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --location=REGION_ID \
    --project=PROJECT_ID \
    --clear-engine-configs
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance
  * REGION_ID: the region where the instance is located
  * PROJECT_ID: your project ID



For example:
    
    
    gcloud memorystore instances update my-instance --location=us-east1 --project=my-project --clear-engine-configs
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
