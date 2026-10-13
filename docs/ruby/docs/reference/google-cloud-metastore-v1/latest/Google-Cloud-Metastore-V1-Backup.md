---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-Backup/
title: Dataproc Metastore V1 API - Class Google::Cloud::Metastore::V1::Backup (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:41.404087+00:00
---

# Dataproc Metastore V1 API - Class Google::Cloud::Metastore::V1::Backup (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-Backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataproc Metastore V1 API - Class Google::Cloud::Metastore::V1::Backup (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Dataproc Metastore V1 API class Google::Cloud::Metastore::V1::Backup.

The details of a backup resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the backup was started. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — The description of the backup. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — The description of the backup. 



**Returns**

  * (::String) — The description of the backup. 



### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the backup finished creating. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Immutable. The relative resource name of the backup, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. The relative resource name of the backup, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`




**Returns**

  * (::String) — Immutable. The relative resource name of the backup, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`




### #restoring_services
    
    
    def restoring_services() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. Services that are restoring from the backup. 



### #service_revision
    
    
    def service_revision() -> ::Google::Cloud::Metastore::V1::Service

**Returns**

  * ([::Google::Cloud::Metastore::V1::Service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-Service)) — Output only. The revision of the service at the time of backup. 



### #state
    
    
    def state() -> ::Google::Cloud::Metastore::V1::Backup::State

**Returns**

  * ([::Google::Cloud::Metastore::V1::Backup::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-Backup-State)) — Output only. The current state of the backup. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
