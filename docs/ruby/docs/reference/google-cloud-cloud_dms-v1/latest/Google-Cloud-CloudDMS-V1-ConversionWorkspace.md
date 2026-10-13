---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConversionWorkspace/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConversionWorkspace (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:22.328113+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConversionWorkspace (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConversionWorkspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConversionWorkspace (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::ConversionWorkspace.

The main conversion workspace resource entity.

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

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when the workspace resource was created. 



### #destination
    
    
    def destination() -> ::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEngineInfo)) — Required. The destination engine details. 



### #destination=
    
    
    def destination=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEngineInfo)) — Required. The destination engine details. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEngineInfo)) — Required. The destination engine details. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Optional. The display name for the workspace. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The display name for the workspace. 



**Returns**

  * (::String) — Optional. The display name for the workspace. 



### #global_settings
    
    
    def global_settings() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. A generic list of settings for the workspace. The settings are database pair dependant and can indicate default behavior for the mapping rules engine or turn on or off specific features. Such examples can be: convert_foreign_key_to_interleave=true, skip_triggers=false, ignore_non_table_synonyms=true 



### #global_settings=
    
    
    def global_settings=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. A generic list of settings for the workspace. The settings are database pair dependant and can indicate default behavior for the mapping rules engine or turn on or off specific features. Such examples can be: convert_foreign_key_to_interleave=true, skip_triggers=false, ignore_non_table_synonyms=true 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. A generic list of settings for the workspace. The settings are database pair dependant and can indicate default behavior for the mapping rules engine or turn on or off specific features. Such examples can be: convert_foreign_key_to_interleave=true, skip_triggers=false, ignore_non_table_synonyms=true 



### #has_uncommitted_changes
    
    
    def has_uncommitted_changes() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Whether the workspace has uncommitted changes (changes which were made after the workspace was committed). 



### #latest_commit_id
    
    
    def latest_commit_id() -> ::String

**Returns**

  * (::String) — Output only. The latest commit ID. 



### #latest_commit_time
    
    
    def latest_commit_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when the workspace was committed. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Full name of the workspace resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Full name of the workspace resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 



**Returns**

  * (::String) — Full name of the workspace resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 



### #source
    
    
    def source() -> ::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEngineInfo)) — Required. The source engine details. 



### #source=
    
    
    def source=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEngineInfo)) — Required. The source engine details. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEngineInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEngineInfo)) — Required. The source engine details. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when the workspace resource was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
