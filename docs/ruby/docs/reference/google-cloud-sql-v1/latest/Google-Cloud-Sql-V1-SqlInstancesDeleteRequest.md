---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesDeleteRequest/
title: Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlInstancesDeleteRequest (v0.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:00.066316+00:00
---

# Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlInstancesDeleteRequest (v0.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesDeleteRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlInstancesDeleteRequest (v0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud SQL Admin V1 API class Google::Cloud::Sql::V1::SqlInstancesDeleteRequest.

Instance delete request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #enable_final_backup
    
    
    def enable_final_backup() -> ::Boolean

**Returns**

  * (::Boolean) — Flag to opt-in for final backup. By default, it is turned off. 



### #enable_final_backup=
    
    
    def enable_final_backup=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Flag to opt-in for final backup. By default, it is turned off. 



**Returns**

  * (::Boolean) — Flag to opt-in for final backup. By default, it is turned off. 



### #final_backup_description
    
    
    def final_backup_description() -> ::String

**Returns**

  * (::String) — Optional. The description of the final backup. 



### #final_backup_description=
    
    
    def final_backup_description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The description of the final backup. 



**Returns**

  * (::String) — Optional. The description of the final backup. 



### #final_backup_expiry_time
    
    
    def final_backup_expiry_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Timestamp)) — Optional. Final Backup expiration time. Timestamp in UTC of when this resource is considered expired.

Note: The following fields are mutually exclusive: `final_backup_expiry_time`, `final_backup_ttl_days`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #final_backup_expiry_time=
    
    
    def final_backup_expiry_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Timestamp)) — Optional. Final Backup expiration time. Timestamp in UTC of when this resource is considered expired.

Note: The following fields are mutually exclusive: `final_backup_expiry_time`, `final_backup_ttl_days`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Timestamp)) — Optional. Final Backup expiration time. Timestamp in UTC of when this resource is considered expired.

Note: The following fields are mutually exclusive: `final_backup_expiry_time`, `final_backup_ttl_days`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #final_backup_ttl_days
    
    
    def final_backup_ttl_days() -> ::Integer

**Returns**

  * (::Integer) — Optional. Retention period of the final backup.

Note: The following fields are mutually exclusive: `final_backup_ttl_days`, `final_backup_expiry_time`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #final_backup_ttl_days=
    
    
    def final_backup_ttl_days=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Retention period of the final backup.

Note: The following fields are mutually exclusive: `final_backup_ttl_days`, `final_backup_expiry_time`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Integer) — Optional. Retention period of the final backup.

Note: The following fields are mutually exclusive: `final_backup_ttl_days`, `final_backup_expiry_time`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #instance
    
    
    def instance() -> ::String

**Returns**

  * (::String) — Cloud SQL instance ID. This does not include the project ID. 



### #instance=
    
    
    def instance=(value) -> ::String

**Parameter**

  * **value** (::String) — Cloud SQL instance ID. This does not include the project ID. 



**Returns**

  * (::String) — Cloud SQL instance ID. This does not include the project ID. 



### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — Optional. Region of the Cloud SQL instance. 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Region of the Cloud SQL instance. 



**Returns**

  * (::String) — Optional. Region of the Cloud SQL instance. 



### #project
    
    
    def project() -> ::String

**Returns**

  * (::String) — Project ID of the project that contains the instance to be deleted. 



### #project=
    
    
    def project=(value) -> ::String

**Parameter**

  * **value** (::String) — Project ID of the project that contains the instance to be deleted. 



**Returns**

  * (::String) — Project ID of the project that contains the instance to be deleted. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
