---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Backup/
title: Cloud Firestore Admin V1 API - Class Google::Cloud::Firestore::Admin::V1::Backup (v1.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:46.622247+00:00
---

# Cloud Firestore Admin V1 API - Class Google::Cloud::Firestore::Admin::V1::Backup (v1.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore Admin V1 API - Class Google::Cloud::Firestore::Admin::V1::Backup (v1.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.2 (latest)  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.18.0  0.17.1  0.16.0  0.15.0  0.14.3  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Cloud Firestore Admin V1 API class Google::Cloud::Firestore::Admin::V1::Backup.

A Backup of a Cloud Firestore Database.

The backup contains all documents and index configurations for the given database at a specific point in time.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #database
    
    
    def database() -> ::String

**Returns**

  * (::String) — Output only. Name of the Firestore database that the backup is from.

Format is `projects/{project}/databases/{database}`. 




### #database_uid
    
    
    def database_uid() -> ::String

**Returns**

  * (::String) — Output only. The system-generated UUID4 for the Firestore database that the backup is from. 



### #expire_time
    
    
    def expire_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp at which this backup expires. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The unique resource name of the Backup.

Format is `projects/{project}/locations/{location}/backups/{backup}`.

The location in the name will be the Standard Managed Multi-Region (SMMR) location (e.g. `us`) if the backup was created with an SMMR location, or the Google Managed Multi-Region (GMMR) location (e.g. `nam5`) if the backup was created with a GMMR location. 




### #snapshot_time
    
    
    def snapshot_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Protobuf-Timestamp)) — Output only. The backup contains an externally consistent copy of the database at this time. 



### #state
    
    
    def state() -> ::Google::Cloud::Firestore::Admin::V1::Backup::State

**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Backup::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Backup-State)) — Output only. The current state of the backup. 



### #stats
    
    
    def stats() -> ::Google::Cloud::Firestore::Admin::V1::Backup::Stats

**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Backup::Stats](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Backup-Stats)) — Output only. Statistics about the backup.

This data only becomes available after the backup is fully materialized to secondary storage. This field will be empty till then. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
