---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ListGoldengateDeploymentVersionsRequest/
title: Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::ListGoldengateDeploymentVersionsRequest (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:49.416358+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::ListGoldengateDeploymentVersionsRequest (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ListGoldengateDeploymentVersionsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::ListGoldengateDeploymentVersionsRequest (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Cloud::OracleDatabase::V1::ListGoldengateDeploymentVersionsRequest.

Message for listing GoldengateDeploymentVersions.

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

  * (::String) — Optional. An expression for filtering the results of the request. Either the deployment_id and deployment_type fields must be specified in the format: `deployment_id="id"` or `deployment_type="DATABASE_ORACLE"`. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An expression for filtering the results of the request. Either the deployment_id and deployment_type fields must be specified in the format: `deployment_id="id"` or `deployment_type="DATABASE_ORACLE"`. 



**Returns**

  * (::String) — Optional. An expression for filtering the results of the request. Either the deployment_id and deployment_type fields must be specified in the format: `deployment_id="id"` or `deployment_type="DATABASE_ORACLE"`. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. The maximum value is 1000; values above 1000 will be coerced to 1000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. The maximum value is 1000; values above 1000 will be coerced to 1000. 



**Returns**

  * (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. The maximum value is 1000; values above 1000 will be coerced to 1000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A token identifying a page of results the server should return. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A token identifying a page of results the server should return. 



**Returns**

  * (::String) — Optional. A token identifying a page of results the server should return. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Parent value for ListGoldengateDeploymentVersionsRequest Format: projects/{project}/locations/{location} 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Parent value for ListGoldengateDeploymentVersionsRequest Format: projects/{project}/locations/{location} 



**Returns**

  * (::String) — Required. Parent value for ListGoldengateDeploymentVersionsRequest Format: projects/{project}/locations/{location} 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
