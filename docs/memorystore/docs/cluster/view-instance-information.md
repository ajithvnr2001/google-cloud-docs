---
url: https://docs.cloud.google.com/memorystore/docs/cluster/view-instance-information/
title: View cluster information \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:21.054706+00:00
---

# View cluster information  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/view-instance-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  View cluster information Stay organized with collections  Save and categorize content based on your preferences. 

Viewing high-level information about clusters in Memorystore for Redis Cluster is essential to obtain a comprehensive snapshot of the cluster's state, configuration, and connectivity.

The following are sample use cases for viewing summary information about clusters:

  * **Retrieve connection endpoints** : retrieve the [discovery endpoint](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#discovery_endpoint), which consists of an IP address and port number.
  * **Verify custom configurations** : view configuration parameters that a user applies to a cluster. For example, you can obtain the value that a user sets for the [`maxmemory-policy`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters) parameter.
  * **Check information about nodes and shards** : obtain information about the nodes and shards associated with a cluster. This includes the number of shards, the node type, and the number of replicas that each shard has.
  * **Confirm data resiliency settings** : verify active [persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview) modes for Redis Database (RDB) snapshots and Append-Only File (AOF) log files, as well as the status of whether a cluster is protected from accidental deletion.



## View summary information about a cluster

You can view summary information about a cluster by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of a cluster about which you want to view summary information.




### gcloud

To view summary information about a cluster, use the [`gcloud redis clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/describe) command:
    
    
    gcloud redis clusters describe CLUSTER_ID \
    --region=REGION_ID
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster about which you want to view summary information
  * REGION_ID: the region where the cluster is located



For example:
    
    
    gcloud redis clusters describe my-cluster \
    --region=us-central1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
