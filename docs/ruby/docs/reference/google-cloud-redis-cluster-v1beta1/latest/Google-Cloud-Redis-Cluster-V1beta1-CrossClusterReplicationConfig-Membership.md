---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1beta1/latest/Google-Cloud-Redis-Cluster-V1beta1-CrossClusterReplicationConfig-Membership/
title: Google Cloud Memorystore for Redis V1BETA1 API - Class Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::Membership (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:56.971843+00:00
---

# Google Cloud Memorystore for Redis V1BETA1 API - Class Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::Membership (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1beta1/latest/Google-Cloud-Redis-Cluster-V1beta1-CrossClusterReplicationConfig-Membership/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1BETA1 API - Class Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::Membership (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.0  0.10.0  0.9.1  0.8.0  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1BETA1 API class Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::Membership.

An output only view of all the member clusters participating in the cross cluster replication.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #primary_cluster
    
    
    def primary_cluster() -> ::Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::RemoteCluster

**Returns**

  * ([::Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::RemoteCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1beta1/latest/Google-Cloud-Redis-Cluster-V1beta1-CrossClusterReplicationConfig-RemoteCluster)) — Output only. The primary cluster that acts as the source of replication for the secondary clusters. 



### #secondary_clusters
    
    
    def secondary_clusters() -> ::Array<::Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::RemoteCluster>

**Returns**

  * (::Array<[::Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::RemoteCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1beta1/latest/Google-Cloud-Redis-Cluster-V1beta1-CrossClusterReplicationConfig-RemoteCluster)>) — Output only. The list of secondary clusters replicating from the primary cluster. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
