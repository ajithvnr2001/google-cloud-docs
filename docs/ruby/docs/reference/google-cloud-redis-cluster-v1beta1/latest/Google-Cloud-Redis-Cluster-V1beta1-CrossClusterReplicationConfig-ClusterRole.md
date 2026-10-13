---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1beta1/latest/Google-Cloud-Redis-Cluster-V1beta1-CrossClusterReplicationConfig-ClusterRole/
title: Google Cloud Memorystore for Redis V1BETA1 API - Module Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::ClusterRole (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:04.999977+00:00
---

# Google Cloud Memorystore for Redis V1BETA1 API - Module Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::ClusterRole (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1beta1/latest/Google-Cloud-Redis-Cluster-V1beta1-CrossClusterReplicationConfig-ClusterRole/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1BETA1 API - Module Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::ClusterRole (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.0  0.10.0  0.9.1  0.8.0  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1BETA1 API module Google::Cloud::Redis::Cluster::V1beta1::CrossClusterReplicationConfig::ClusterRole.

The role of the cluster in cross cluster replication.

## Constants 

### CLUSTER_ROLE_UNSPECIFIED

**value:** 0  
Cluster role is not set. The behavior is equivalent to NONE.

### NONE

**value:** 1  
This cluster does not participate in cross cluster replication. It is an independent cluster and does not replicate to or from any other clusters.

### PRIMARY

**value:** 2  
A cluster that allows both reads and writes. Any data written to this cluster is also replicated to the attached secondary clusters.

### SECONDARY

**value:** 3  
A cluster that allows only reads and replicates data from a primary cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
