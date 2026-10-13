---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Cloud-Workflows-V1-ListWorkflowsRequest/
title: Workflows V1 API - Class Google::Cloud::Workflows::V1::ListWorkflowsRequest (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:43.816362+00:00
---

# Workflows V1 API - Class Google::Cloud::Workflows::V1::ListWorkflowsRequest (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Cloud-Workflows-V1-ListWorkflowsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Workflows V1 API - Class Google::Cloud::Workflows::V1::ListWorkflowsRequest (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.1  2.4.1  2.3.0  2.2.0  2.1.1  2.0.0  1.2.0  1.1.0  1.0.2  0.8.0  0.7.2  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Workflows V1 API class Google::Cloud::Workflows::V1::ListWorkflowsRequest.

Request for the [ListWorkflows](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Cloud-Workflows-V1-Workflows-Client#Google__Cloud__Workflows__V1__Workflows__Client_list_workflows_instance_ "Google::Cloud::Workflows::V1::Workflows::Client#list_workflows \(method\)") method.

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

  * (::String) — Filter to restrict results to specific workflows. For details, see [AIP-160](https://google.aip.dev/160).

For example, if you are using the Google APIs Explorer:

`state="SUCCEEDED"`

or

`createTime>"2023-08-01" AND state="FAILED"`




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Filter to restrict results to specific workflows. For details, see [AIP-160](https://google.aip.dev/160).

For example, if you are using the Google APIs Explorer:

`state="SUCCEEDED"`

or

`createTime>"2023-08-01" AND state="FAILED"`




**Returns**

  * (::String) — Filter to restrict results to specific workflows. For details, see [AIP-160](https://google.aip.dev/160).

For example, if you are using the Google APIs Explorer:

`state="SUCCEEDED"`

or

`createTime>"2023-08-01" AND state="FAILED"`




### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Comma-separated list of fields that specify the order of the results. Default sorting order for a field is ascending. To specify descending order for a field, append a "desc" suffix. If not specified, the results are returned in an unspecified order. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Comma-separated list of fields that specify the order of the results. Default sorting order for a field is ascending. To specify descending order for a field, append a "desc" suffix. If not specified, the results are returned in an unspecified order. 



**Returns**

  * (::String) — Comma-separated list of fields that specify the order of the results. Default sorting order for a field is ascending. To specify descending order for a field, append a "desc" suffix. If not specified, the results are returned in an unspecified order. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Maximum number of workflows to return per call. The service might return fewer than this value even if not at the end of the collection. If a value is not specified, a default value of 500 is used. The maximum permitted value is 1000 and values greater than 1000 are coerced down to 1000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Maximum number of workflows to return per call. The service might return fewer than this value even if not at the end of the collection. If a value is not specified, a default value of 500 is used. The maximum permitted value is 1000 and values greater than 1000 are coerced down to 1000. 



**Returns**

  * (::Integer) — Maximum number of workflows to return per call. The service might return fewer than this value even if not at the end of the collection. If a value is not specified, a default value of 500 is used. The maximum permitted value is 1000 and values greater than 1000 are coerced down to 1000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A page token, received from a previous `ListWorkflows` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListWorkflows` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A page token, received from a previous `ListWorkflows` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListWorkflows` must match the call that provided the page token. 




**Returns**

  * (::String) — A page token, received from a previous `ListWorkflows` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListWorkflows` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Project and location from which the workflows should be listed. Format: projects/{project}/locations/{location} 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Project and location from which the workflows should be listed. Format: projects/{project}/locations/{location} 



**Returns**

  * (::String) — Required. Project and location from which the workflows should be listed. Format: projects/{project}/locations/{location} 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
