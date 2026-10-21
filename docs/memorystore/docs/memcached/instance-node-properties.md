---
url: https://docs.cloud.google.com/memorystore/docs/memcached/instance-node-properties/
title: Instance and node properties \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:48.385265+00:00
---

# Instance and node properties  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/instance-node-properties/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Instance and node properties Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the properties of Memorystore for Memcached instances and nodes, as well as the possible values for those properties.

## Instance settings

The following table lists the settings that you can modify for your Memorystore for Memcached instances and nodes.

Setting | Possible Values  
---|---  
**Instance ID** | 

  * Compose of lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Cannot exceed 40 characters.

  
**Display name** | Optional. The display name of the instance cannot exceed 80 characters.  
**Labels** | String key/value pairs. Keys must start with a lowercase character and can contain only hyphens (-), underscores (_), lowercase characters, and numbers.   
**Network association** | A network from your project, or a shared VPC network.  
**Number of nodes** | 1-20  
**Cores/vCPUs per node** | Minimum: 1 or 2 vCPUs [depending on the region](https://docs.cloud.google.com/memorystore/docs/memcached/instance-node-properties#minimum_vcpu_according_to_region)   
Maximum: 32 vCPUs   
With the exception of a single vCPU (depending on the region), you must provision vCPUs in even numbers. For example, 1 vCPU, 2 vCPUs, 12 vCPUs, and 26 vCPUs can be acceptable values.   
**Memory per node** | Minimum: 1 GB or (0.9 GB * vCPUs per node), whichever is greater.   
Maximum: 256 GB.   
Note: Memory per node is constrained by the number of vCPUs that the node has. You can provision up to 8 GB of memory for every vCPU and must provision at least 0.9 GB for every vCPU. Therefore, to reach the maximum memory per node of 256 GB, you need to provision 32 vCPUs for each node.  
**Region** | The Google Cloud region in which you want to deploy your instance  
**Zones** | Optional. The zone(s) within a region where you want to deploy your node(s).  
**Memcached version** | The Memcached version your instance uses. Available versions are `1.5.16` and `1.6.15`. For more information, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/memcached/supported-versions).  
  
#### Minimum vCPU according to region

Nodes in your Memcached instances have a minimum vCPU count of 2, except for the following regions whose minimum is 1 vCPU:

Region Name | Region Description | Minimum vCPU count  
---|---|---  
`asia-east1` | Taiwan | 1  
`asia-east2` | Hong Kong  
`asia-northeast1` | Tokyo  
`asia-northeast2` | Osaka  
`asia-northeast3` | Seoul  
`asia-south1` | Mumbai  
`asia-south2` | Delhi  
`asia-southeast1` | Singapore  
`asia-southeast2` | Jakarta  
`australia-southeast1` | Sydney  
`australia-southeast2` | Melbourne  
`europe-central2` | Warsaw  
`europe-north1` | Finland | `europe-west1` | Belgium  
`europe-west2` | London  
`europe-west3` | Frankfurt  
`europe-west4` | Netherlands  
`europe-west6` | Zurich  
`northamerica-northeast1` | Montreal  
`northamerica-northeast2` | Toronto  
`southamerica-east1` | São Paulo  
`us-central1` | Iowa  
`us-east1` | South Carolina  
`us-east4` | Northern Virginia  
`us-west1` | Oregon  
`us-west2` | Los Angeles  
`us-west3` | Salt Lake City  
`us-west4` | Las Vegas  
  
## Output fields

The following tables list the output properties of instances and nodes that you can query to learn about an instance or node. To view these properties, run the following command, replacing the variables with appropriate values: 
    
    
    gcloud memcache instances describe instance-id --region=region
    

Instance property | Description  
---|---  
`memcacheFullVersion:` | Memcached version used in the instance. For a list of available versions, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/memcached/supported-versions).  
`state:`  
  
| Instances can be in the following states:  


  * **Creating** : Instance is being created. 
  * **Ready** : Instance is ready to be used in Memcached clients. 
  * **Deleting** : Instance is being deleted.

  
`zones:`  
| User designated zones in which nodes are provisioned.  
Node property | Description  
---|---  
`memcacheFullVersion:` | Memcached version used by the node. For a list of available versions, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/memcached/supported-versions).  
`nodeID:` | Auto-generated ID of the Memcached node used to view node-level metrics in Cloud Monitoring.  
`state:`  
  
| Nodes can be in the following states:  


  * **Creating** : Node is being created. 
  * **Ready** : Node is ready to be used in Memcached clients. If a node is undergoing a repair by the Memorystore for Memcached system, that state will not be reflected here.
  * **Deleting** : Node is being deleted.

  
`zone:`  
| The Google Cloud zone where the node is located.  
`port:` | Node port. This value is always `11211` for all nodes.  
  
## What's next

  * [Create a Memcached instance](https://docs.cloud.google.com/memorystore/docs/memcached/creating-managing-instances).
  * View the available [Regions and zones](https://docs.cloud.google.com/memorystore/docs/memcached/regions) for Memorystore for Memcached.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
