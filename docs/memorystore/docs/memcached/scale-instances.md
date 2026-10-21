---
url: https://docs.cloud.google.com/memorystore/docs/memcached/scale-instances/
title: Scale Memcached instances \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:48.975155+00:00
---

# Scale Memcached instances  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/scale-instances/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Scale Memcached instances Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to scale instances, and how scaling works for Memorystore for Memcached.

You can scale the number of nodes in a cluster down to a minimum of 1 node or up to a maximum of 20 nodes. You cannot scale a node's memory capacity or number of vCPUs.

### Scaling out

When you scale out your cluster, unless you use [Auto Discovery](https://docs.cloud.google.com/memorystore/docs/memcached/auto-discovery-overview) you must manually add the IP addresses of the new nodes to your application so the application can access them. Also, Memorystore for Memcached does not rebalance the data in your nodes. You must manage any data rebalancing you wish to perform.

### Scaling in

If you scale in your instance, you will lose the data that is stored in the nodes that are deleted from your cluster.

During a scale in operation, Memorystore removes nodes from the end of the node list. For example, if you are scaling from 12 nodes to 8 nodes, nodes 9-12 will be deleted from the instance.

You can view the node list on your Memcached instance's **node list** tab in the Google Cloud console.

You can also view the node list by running the following command, replacing variables with appropriate values:
    
    
    gcloud memcache instances describe instance-id --region=us-region
    

#### Managing nodes when scaling in

Your application's node management strategy affects what actions you need to take when scaling in your cluster.

If you manually manage the addition and removal of Memcached nodes in your application, you must adjust your code by removing references to the nodes that will be deleted before scaling in the cluster.

If you use [Auto Discovery](https://docs.cloud.google.com/memorystore/docs/memcached/auto-discovery-overview), node addition and removal is handled for you automatically.

## Scaling the number of nodes in your cluster

### Console

  1. Go to the Memorystore for Memcached page in the Google Cloud console.

  
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)

  2. Click the Instance ID of the instance you want to resize.

  3. Click **Edit**.

  4. In the **Nodes** field, enter your desired number of nodes.

  5. Click **Save**.




### Gcloud

Enter the following command, replacing the variables with the appropriate values:
    
    
    gcloud memcache instances update instance-id --region=region --node-count=desired-number-of-nodes
    

For example:
    
    
    gcloud memcache instances update myinstance --region=us-central1 --node-count=6
    

## What's next

  * View available [Memcached configurations](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).
  * [Monitor your Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
