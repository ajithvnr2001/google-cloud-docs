---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-Backup/
title: Google Cloud Memorystore for Redis V1 API - Class Google::Cloud::Redis::Cluster::V1::Backup (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:49.685007+00:00
---

# Google Cloud Memorystore for Redis V1 API - Class Google::Cloud::Redis::Cluster::V1::Backup (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-Backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1 API - Class Google::Cloud::Redis::Cluster::V1::Backup (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.6.0  0.5.0  0.4.2  0.3.0  0.2.2  0.1.0 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1 API class Google::Cloud::Redis::Cluster::V1::Backup.

Backup of a cluster.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_files
    
    
    def backup_files() -> ::Array<::Google::Cloud::Redis::Cluster::V1::BackupFile>

**Returns**

  * (::Array<[::Google::Cloud::Redis::Cluster::V1::BackupFile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-BackupFile)>) — Output only. List of backup files of the backup. 



### #backup_type
    
    
    def backup_type() -> ::Google::Cloud::Redis::Cluster::V1::Backup::BackupType

**Returns**

  * ([::Google::Cloud::Redis::Cluster::V1::Backup::BackupType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-Backup-BackupType)) — Output only. Type of the backup. 



### #cluster
    
    
    def cluster() -> ::String

**Returns**

  * (::String) — Output only. Cluster resource path of this backup. 



### #cluster_uid
    
    
    def cluster_uid() -> ::String

**Returns**

  * (::String) — Output only. Cluster uid of this backup. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the backup was created. 



### #encryption_info
    
    
    def encryption_info() -> ::Google::Cloud::Redis::Cluster::V1::EncryptionInfo

**Returns**

  * ([::Google::Cloud::Redis::Cluster::V1::EncryptionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-EncryptionInfo)) — Output only. Encryption information of the backup. 



### #engine_version
    
    
    def engine_version() -> ::String

**Returns**

  * (::String) — Output only. redis-7.2, valkey-7.5 



### #expire_time
    
    
    def expire_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the backup will expire. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Cluster UID] OR customer specified while backup cluster. Example: 20240515123000_1234 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Cluster UID] OR customer specified while backup cluster. Example: 20240515123000_1234 



**Returns**

  * (::String) — Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Cluster UID] OR customer specified while backup cluster. Example: 20240515123000_1234 



### #node_type
    
    
    def node_type() -> ::Google::Cloud::Redis::Cluster::V1::NodeType

**Returns**

  * ([::Google::Cloud::Redis::Cluster::V1::NodeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-NodeType)) — Output only. Node type of the cluster. 



### #replica_count
    
    
    def replica_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of replicas for the cluster. 



### #shard_count
    
    
    def shard_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of shards for the cluster. 



### #state
    
    
    def state() -> ::Google::Cloud::Redis::Cluster::V1::Backup::State

**Returns**

  * ([::Google::Cloud::Redis::Cluster::V1::Backup::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-Backup-State)) — Output only. State of the backup. 



### #total_size_bytes
    
    
    def total_size_bytes() -> ::Integer

**Returns**

  * (::Integer) — Output only. Total size of the backup in bytes. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. System assigned unique identifier of the backup. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
