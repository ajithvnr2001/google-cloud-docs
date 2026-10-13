---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeDatabaseEntitiesRequest/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:28.220179+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeDatabaseEntitiesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest.

Request message for 'DescribeDatabaseEntities' request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #commit_id
    
    
    def commit_id() -> ::String

**Returns**

  * (::String) — Optional. Request a specific commit ID. If not specified, the entities from the latest commit are returned. 



### #commit_id=
    
    
    def commit_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Request a specific commit ID. If not specified, the entities from the latest commit are returned. 



**Returns**

  * (::String) — Optional. Request a specific commit ID. If not specified, the entities from the latest commit are returned. 



### #conversion_workspace
    
    
    def conversion_workspace() -> ::String

**Returns**

  * (::String) — Required. Name of the conversion workspace resource whose database entities are described. Must be in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 



### #conversion_workspace=
    
    
    def conversion_workspace=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the conversion workspace resource whose database entities are described. Must be in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 



**Returns**

  * (::String) — Required. Name of the conversion workspace resource whose database entities are described. Must be in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 



### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. Filter the returned entities based on AIP-160 standard. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Filter the returned entities based on AIP-160 standard. 



**Returns**

  * (::String) — Optional. Filter the returned entities based on AIP-160 standard. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of entities to return. The service may return fewer entities than the value specifies. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of entities to return. The service may return fewer entities than the value specifies. 



**Returns**

  * (::Integer) — Optional. The maximum number of entities to return. The service may return fewer entities than the value specifies. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. The nextPageToken value received in the previous call to conversionWorkspace.describeDatabaseEntities, used in the subsequent request to retrieve the next page of results. On first call this should be left blank. When paginating, all other parameters provided to conversionWorkspace.describeDatabaseEntities must match the call that provided the page token. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The nextPageToken value received in the previous call to conversionWorkspace.describeDatabaseEntities, used in the subsequent request to retrieve the next page of results. On first call this should be left blank. When paginating, all other parameters provided to conversionWorkspace.describeDatabaseEntities must match the call that provided the page token. 



**Returns**

  * (::String) — Optional. The nextPageToken value received in the previous call to conversionWorkspace.describeDatabaseEntities, used in the subsequent request to retrieve the next page of results. On first call this should be left blank. When paginating, all other parameters provided to conversionWorkspace.describeDatabaseEntities must match the call that provided the page token. 



### #tree
    
    
    def tree() -> ::Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest::DBTreeType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest::DBTreeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeDatabaseEntitiesRequest-DBTreeType)) — Required. The tree to fetch. 



### #tree=
    
    
    def tree=(value) -> ::Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest::DBTreeType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest::DBTreeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeDatabaseEntitiesRequest-DBTreeType)) — Required. The tree to fetch. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest::DBTreeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeDatabaseEntitiesRequest-DBTreeType)) — Required. The tree to fetch. 



### #uncommitted
    
    
    def uncommitted() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to retrieve the latest committed version of the entities or the latest version. This field is ignored if a specific commit_id is specified. 



### #uncommitted=
    
    
    def uncommitted=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to retrieve the latest committed version of the entities or the latest version. This field is ignored if a specific commit_id is specified. 



**Returns**

  * (::Boolean) — Optional. Whether to retrieve the latest committed version of the entities or the latest version. This field is ignored if a specific commit_id is specified. 



### #view
    
    
    def view() -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityView

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityView)) — Optional. Results view based on AIP-157 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityView

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEntityView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityView)) — Optional. Results view based on AIP-157 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityView)) — Optional. Results view based on AIP-157 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
