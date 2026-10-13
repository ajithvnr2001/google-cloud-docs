---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AggregatedListNodeTypesRequest/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AggregatedListNodeTypesRequest (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:51.213402+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AggregatedListNodeTypesRequest (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AggregatedListNodeTypesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AggregatedListNodeTypesRequest (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::AggregatedListNodeTypesRequest.

A request message for NodeTypes.AggregatedList. See the method description for details.

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

  * (::String) — A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal AIP-160. These two types of filter expressions cannot be mixed in one request.

If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.

For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.

The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use: ` labels.owner:* `

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based onresource labels.

To filter on multiple expressions, provide each separate expression within parentheses. For example: ` (scheduling.automaticRestart = true) (cpuPlatform = "Intel Skylake") ` By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example: ` (cpuPlatform = "Intel Skylake") OR (cpuPlatform = "Intel Broadwell") AND (scheduling.automaticRestart = true) `

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:

`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`

The literal value is interpreted as a regular expression using GoogleRE2 library syntax. The literal value must match the entire field.

For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.

You cannot combine constraints on multiple fields using regular expressions. 




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal AIP-160. These two types of filter expressions cannot be mixed in one request.

If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.

For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.

The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use: ` labels.owner:* `

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based onresource labels.

To filter on multiple expressions, provide each separate expression within parentheses. For example: ` (scheduling.automaticRestart = true) (cpuPlatform = "Intel Skylake") ` By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example: ` (cpuPlatform = "Intel Skylake") OR (cpuPlatform = "Intel Broadwell") AND (scheduling.automaticRestart = true) `

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:

`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`

The literal value is interpreted as a regular expression using GoogleRE2 library syntax. The literal value must match the entire field.

For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.

You cannot combine constraints on multiple fields using regular expressions. 




**Returns**

  * (::String) — A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal AIP-160. These two types of filter expressions cannot be mixed in one request.

If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.

For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.

The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use: ` labels.owner:* `

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based onresource labels.

To filter on multiple expressions, provide each separate expression within parentheses. For example: ` (scheduling.automaticRestart = true) (cpuPlatform = "Intel Skylake") ` By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example: ` (cpuPlatform = "Intel Skylake") OR (cpuPlatform = "Intel Broadwell") AND (scheduling.automaticRestart = true) `

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:

`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`

The literal value is interpreted as a regular expression using GoogleRE2 library syntax. The literal value must match the entire field.

For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.

You cannot combine constraints on multiple fields using regular expressions. 




### #include_all_scopes
    
    
    def include_all_scopes() -> ::Boolean

**Returns**

  * (::Boolean) — Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included. 



### #include_all_scopes=
    
    
    def include_all_scopes=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included. 



**Returns**

  * (::Boolean) — Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included. 



### #max_results
    
    
    def max_results() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`) 



### #max_results=
    
    
    def max_results=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`) 



**Returns**

  * (::Integer) — The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`) 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.

You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.

Currently, only sorting by `name` or `creationTimestamp desc` is supported. 




### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.

You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.

Currently, only sorting by `name` or `creationTimestamp desc` is supported. 




**Returns**

  * (::String) — Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.

You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.

Currently, only sorting by `name` or `creationTimestamp desc` is supported. 




### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results. 



**Returns**

  * (::String) — Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results. 



### #project
    
    
    def project() -> ::String

**Returns**

  * (::String) — Project ID for this request. 



### #project=
    
    
    def project=(value) -> ::String

**Parameter**

  * **value** (::String) — Project ID for this request. 



**Returns**

  * (::String) — Project ID for this request. 



### #service_project_number
    
    
    def service_project_number() -> ::Integer

**Returns**

  * (::Integer) — The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api. 



### #service_project_number=
    
    
    def service_project_number=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api. 



**Returns**

  * (::Integer) — The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
