---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-ListNetworkPoliciesRequest/
title: Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::ListNetworkPoliciesRequest (v1.5.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:32.671065+00:00
---

# Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::ListNetworkPoliciesRequest (v1.5.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-ListNetworkPoliciesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::ListNetworkPoliciesRequest (v1.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.2 (latest)  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.1  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud VMware Engine V1 API class Google::Cloud::VmwareEngine::V1::ListNetworkPoliciesRequest.

Request message for [VmwareEngine.ListNetworkPolicies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-VmwareEngine-Client#Google__Cloud__VmwareEngine__V1__VmwareEngine__Client_list_network_policies_instance_ "Google::Cloud::VmwareEngine::V1::VmwareEngine::Client#list_network_policies \(method\)")

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

  * (::String) — A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be `=`, `!=`, `>`, or `<`.

For example, if you are filtering a list of network policies, you can exclude the ones named `example-policy` by specifying `name != "example-policy"`.

To filter on multiple expressions, provide each separate expression within parentheses. For example: ` (name = "example-policy") (createTime > "2021-04-12T08:15:10.40Z") `

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example: ` (name = "example-policy-1") AND (createTime > "2021-04-12T08:15:10.40Z") OR (name = "example-policy-2") `




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be `=`, `!=`, `>`, or `<`.

For example, if you are filtering a list of network policies, you can exclude the ones named `example-policy` by specifying `name != "example-policy"`.

To filter on multiple expressions, provide each separate expression within parentheses. For example: ` (name = "example-policy") (createTime > "2021-04-12T08:15:10.40Z") `

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example: ` (name = "example-policy-1") AND (createTime > "2021-04-12T08:15:10.40Z") OR (name = "example-policy-2") `




**Returns**

  * (::String) — A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be `=`, `!=`, `>`, or `<`.

For example, if you are filtering a list of network policies, you can exclude the ones named `example-policy` by specifying `name != "example-policy"`.

To filter on multiple expressions, provide each separate expression within parentheses. For example: ` (name = "example-policy") (createTime > "2021-04-12T08:15:10.40Z") `

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example: ` (name = "example-policy-1") AND (createTime > "2021-04-12T08:15:10.40Z") OR (name = "example-policy-2") `




### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Sorts list results by a certain order. By default, returned results are ordered by `name` in ascending order. You can also sort results in descending order based on the `name` value using `orderBy="name desc"`. Currently, only ordering by `name` is supported. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Sorts list results by a certain order. By default, returned results are ordered by `name` in ascending order. You can also sort results in descending order based on the `name` value using `orderBy="name desc"`. Currently, only ordering by `name` is supported. 



**Returns**

  * (::String) — Sorts list results by a certain order. By default, returned results are ordered by `name` in ascending order. You can also sort results in descending order based on the `name` value using `orderBy="name desc"`. Currently, only ordering by `name` is supported. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of network policies to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of network policies to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500. 



**Returns**

  * (::Integer) — The maximum number of network policies to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A page token, received from a previous `ListNetworkPolicies` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListNetworkPolicies` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A page token, received from a previous `ListNetworkPolicies` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListNetworkPolicies` must match the call that provided the page token. 




**Returns**

  * (::String) — A page token, received from a previous `ListNetworkPolicies` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListNetworkPolicies` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the location (region) to query for network policies. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the location (region) to query for network policies. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1`



**Returns**

  * (::String) — Required. The resource name of the location (region) to query for network policies. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
