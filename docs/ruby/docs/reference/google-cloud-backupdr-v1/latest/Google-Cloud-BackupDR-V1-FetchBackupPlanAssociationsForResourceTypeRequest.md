---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupPlanAssociationsForResourceTypeRequest/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeRequest (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:47.813396+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeRequest (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupPlanAssociationsForResourceTypeRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeRequest (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeRequest.

Request for the FetchBackupPlanAssociationsForResourceType method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — 

Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields:

    * resource
    * backup_plan
    * state
    * data_source
    * cloud_sql_instance_backup_plan_association_properties.instance_create_time



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields:

    * resource
    * backup_plan
    * state
    * data_source
    * cloud_sql_instance_backup_plan_association_properties.instance_create_time



**Returns**

  * (::String) — 

Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields:

    * resource
    * backup_plan
    * state
    * data_source
    * cloud_sql_instance_backup_plan_association_properties.instance_create_time



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — 

Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * name



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * name



**Returns**

  * (::String) — 

Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * name



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of BackupPlanAssociations to return. The service may return fewer than this value. If unspecified, at most 50 BackupPlanAssociations will be returned. The maximum value is 100; values above 100 will be coerced to 100. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of BackupPlanAssociations to return. The service may return fewer than this value. If unspecified, at most 50 BackupPlanAssociations will be returned. The maximum value is 100; values above 100 will be coerced to 100. 



**Returns**

  * (::Integer) — Optional. The maximum number of BackupPlanAssociations to return. The service may return fewer than this value. If unspecified, at most 50 BackupPlanAssociations will be returned. The maximum value is 100; values above 100 will be coerced to 100. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token, received from a previous call of `FetchBackupPlanAssociationsForResourceType`. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `FetchBackupPlanAssociationsForResourceType` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token, received from a previous call of `FetchBackupPlanAssociationsForResourceType`. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `FetchBackupPlanAssociationsForResourceType` must match the call that provided the page token. 




**Returns**

  * (::String) — Optional. A page token, received from a previous call of `FetchBackupPlanAssociationsForResourceType`. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `FetchBackupPlanAssociationsForResourceType` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent resource name. Format: projects/{project}/locations/{location} 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent resource name. Format: projects/{project}/locations/{location} 



**Returns**

  * (::String) — Required. The parent resource name. Format: projects/{project}/locations/{location} 



### #resource_type
    
    
    def resource_type() -> ::String

**Returns**

  * (::String) — Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance 



### #resource_type=
    
    
    def resource_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance 



**Returns**

  * (::String) — Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
