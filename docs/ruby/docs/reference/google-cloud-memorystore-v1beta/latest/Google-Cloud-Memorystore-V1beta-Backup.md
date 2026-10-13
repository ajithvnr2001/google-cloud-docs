---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-Backup/
title: Memorystore V1BETA API - Class Google::Cloud::Memorystore::V1beta::Backup (v0.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:18.661262+00:00
---

# Memorystore V1BETA API - Class Google::Cloud::Memorystore::V1beta::Backup (v0.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-Backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Memorystore V1BETA API - Class Google::Cloud::Memorystore::V1beta::Backup (v0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Memorystore V1BETA API class Google::Cloud::Memorystore::V1beta::Backup.

Backup of an instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_files
    
    
    def backup_files() -> ::Array<::Google::Cloud::Memorystore::V1beta::BackupFile>

**Returns**

  * (::Array<[::Google::Cloud::Memorystore::V1beta::BackupFile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-BackupFile)>) — Output only. List of backup files of the backup. 



### #backup_type
    
    
    def backup_type() -> ::Google::Cloud::Memorystore::V1beta::Backup::BackupType

**Returns**

  * ([::Google::Cloud::Memorystore::V1beta::Backup::BackupType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-Backup-BackupType)) — Output only. Type of the backup. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Protobuf-Timestamp)) — Output only. The time when the backup was created. 



### #encryption_info
    
    
    def encryption_info() -> ::Google::Cloud::Memorystore::V1beta::EncryptionInfo

**Returns**

  * ([::Google::Cloud::Memorystore::V1beta::EncryptionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-EncryptionInfo)) — Output only. Encryption information of the backup. 



### #engine_version
    
    
    def engine_version() -> ::String

**Returns**

  * (::String) — Output only. valkey-7.5/valkey-8.0, etc. 



### #expire_time
    
    
    def expire_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Protobuf-Timestamp)) — Output only. The time when the backup will expire. 



### #instance
    
    
    def instance() -> ::String

**Returns**

  * (::String) — Output only. Instance resource path of this backup. 



### #instance_uid
    
    
    def instance_uid() -> ::String

**Returns**

  * (::String) — Output only. Instance uid of this backup. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234 



**Returns**

  * (::String) — Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234 



### #node_type
    
    
    def node_type() -> ::Google::Cloud::Memorystore::V1beta::Instance::NodeType

**Returns**

  * ([::Google::Cloud::Memorystore::V1beta::Instance::NodeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-Instance-NodeType)) — Output only. Node type of the instance. 



### #replica_count
    
    
    def replica_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of replicas for the instance. 



### #shard_count
    
    
    def shard_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of shards for the instance. 



### #state
    
    
    def state() -> ::Google::Cloud::Memorystore::V1beta::Backup::State

**Returns**

  * ([::Google::Cloud::Memorystore::V1beta::Backup::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-Backup-State)) — Output only. State of the backup. 



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

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
