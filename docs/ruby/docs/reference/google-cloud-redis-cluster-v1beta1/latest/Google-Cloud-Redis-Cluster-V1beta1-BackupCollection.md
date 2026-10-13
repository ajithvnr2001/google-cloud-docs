---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1beta1/latest/Google-Cloud-Redis-Cluster-V1beta1-BackupCollection/
title: Google Cloud Memorystore for Redis V1BETA1 API - Class Google::Cloud::Redis::Cluster::V1beta1::BackupCollection (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:50.147429+00:00
---

# Google Cloud Memorystore for Redis V1BETA1 API - Class Google::Cloud::Redis::Cluster::V1beta1::BackupCollection (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1beta1/latest/Google-Cloud-Redis-Cluster-V1beta1-BackupCollection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1BETA1 API - Class Google::Cloud::Redis::Cluster::V1beta1::BackupCollection (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.0  0.10.0  0.9.1  0.8.0  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1BETA1 API class Google::Cloud::Redis::Cluster::V1beta1::BackupCollection.

BackupCollection of a cluster.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cluster
    
    
    def cluster() -> ::String

**Returns**

  * (::String) — Output only. The full resource path of the cluster the backup collection belongs to. Example: projects/{project}/locations/{location}/clusters/{cluster} 



### #cluster_uid
    
    
    def cluster_uid() -> ::String

**Returns**

  * (::String) — Output only. The cluster uid of the backup collection. 



### #kms_key
    
    
    def kms_key() -> ::String

**Returns**

  * (::String) — Output only. The KMS key used to encrypt the backups under this backup collection. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. Full resource path of the backup collection. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. Full resource path of the backup collection. 



**Returns**

  * (::String) — Identifier. Full resource path of the backup collection. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. System assigned unique identifier of the backup collection. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
