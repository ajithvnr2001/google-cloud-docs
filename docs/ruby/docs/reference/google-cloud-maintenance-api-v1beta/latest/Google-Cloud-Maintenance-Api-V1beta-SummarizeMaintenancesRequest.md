---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1beta/latest/Google-Cloud-Maintenance-Api-V1beta-SummarizeMaintenancesRequest/
title: Maintenance V1BETA API - Class Google::Cloud::Maintenance::Api::V1beta::SummarizeMaintenancesRequest (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:46.293064+00:00
---

# Maintenance V1BETA API - Class Google::Cloud::Maintenance::Api::V1beta::SummarizeMaintenancesRequest (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1beta/latest/Google-Cloud-Maintenance-Api-V1beta-SummarizeMaintenancesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Maintenance V1BETA API - Class Google::Cloud::Maintenance::Api::V1beta::SummarizeMaintenancesRequest (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Maintenance V1BETA API class Google::Cloud::Maintenance::Api::V1beta::SummarizeMaintenancesRequest.

Request message for SummarizeMaintenances custom method.

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

Filter the list as specified in https://google.aip.dev/160. Supported fields include:

    * state
    * resource.location
    * resource.resourceName
    * resource.type
    * maintenance.maintenanceName
    * maintenanceStartTime
    * maintenanceCompleteTime Examples:
    * state="SCHEDULED"
    * resource.location="us-central1-c"
    * resource.resourceName=~"*/instance-20241212-211259"
    * maintenanceStartTime>"2000-10-11T20:44:51Z"
    * state="SCHEDULED" OR resource.type="compute.googleapis.com/Instance"
    * maintenance.maitenanceName="eb3b709c-9ca1-5472-9fb6-800a3849eda1" AND maintenanceCompleteTime>"2000-10-11T20:44:51Z"



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Filter the list as specified in https://google.aip.dev/160. Supported fields include:

    * state
    * resource.location
    * resource.resourceName
    * resource.type
    * maintenance.maintenanceName
    * maintenanceStartTime
    * maintenanceCompleteTime Examples:
    * state="SCHEDULED"
    * resource.location="us-central1-c"
    * resource.resourceName=~"*/instance-20241212-211259"
    * maintenanceStartTime>"2000-10-11T20:44:51Z"
    * state="SCHEDULED" OR resource.type="compute.googleapis.com/Instance"
    * maintenance.maitenanceName="eb3b709c-9ca1-5472-9fb6-800a3849eda1" AND maintenanceCompleteTime>"2000-10-11T20:44:51Z"



**Returns**

  * (::String) — 

Filter the list as specified in https://google.aip.dev/160. Supported fields include:

    * state
    * resource.location
    * resource.resourceName
    * resource.type
    * maintenance.maintenanceName
    * maintenanceStartTime
    * maintenanceCompleteTime Examples:
    * state="SCHEDULED"
    * resource.location="us-central1-c"
    * resource.resourceName=~"*/instance-20241212-211259"
    * maintenanceStartTime>"2000-10-11T20:44:51Z"
    * state="SCHEDULED" OR resource.type="compute.googleapis.com/Instance"
    * maintenance.maitenanceName="eb3b709c-9ca1-5472-9fb6-800a3849eda1" AND maintenanceCompleteTime>"2000-10-11T20:44:51Z"



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Order results as specified in https://google.aip.dev/132. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Order results as specified in https://google.aip.dev/132. 



**Returns**

  * (::String) — Order results as specified in https://google.aip.dev/132. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of resource maintenances to send per page. The default page size is 20 and the maximum is 1000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of resource maintenances to send per page. The default page size is 20 and the maximum is 1000. 



**Returns**

  * (::Integer) — The maximum number of resource maintenances to send per page. The default page size is 20 and the maximum is 1000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page. 



**Returns**

  * (::String) — The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent of the resource maintenance. eg. `projects/123/locations/*`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent of the resource maintenance. eg. `projects/123/locations/*`



**Returns**

  * (::String) — Required. The parent of the resource maintenance. eg. `projects/123/locations/*`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
