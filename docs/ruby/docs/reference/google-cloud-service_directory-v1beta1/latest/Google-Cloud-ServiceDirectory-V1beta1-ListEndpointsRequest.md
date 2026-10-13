---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Cloud-ServiceDirectory-V1beta1-ListEndpointsRequest/
title: Service Directory V1beta1 API - Class Google::Cloud::ServiceDirectory::V1beta1::ListEndpointsRequest (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:44.044326+00:00
---

# Service Directory V1beta1 API - Class Google::Cloud::ServiceDirectory::V1beta1::ListEndpointsRequest (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Cloud-ServiceDirectory-V1beta1-ListEndpointsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Directory V1beta1 API - Class Google::Cloud::ServiceDirectory::V1beta1::ListEndpointsRequest (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.1  0.20.0  0.19.1  0.18.0  0.17.1  0.16.0  0.15.2  0.14.2  0.13.0  0.12.1  0.11.1  0.10.0  0.9.0  0.8.0  0.7.4 

Reference documentation and code samples for the Service Directory V1beta1 API class Google::Cloud::ServiceDirectory::V1beta1::ListEndpointsRequest.

The request message for [RegistrationService.ListEndpoints](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Cloud-ServiceDirectory-V1beta1-RegistrationService-Client#Google__Cloud__ServiceDirectory__V1beta1__RegistrationService__Client_list_endpoints_instance_ "Google::Cloud::ServiceDirectory::V1beta1::RegistrationService::Client#list_endpoints \(method\)").

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

  * (::String) — Optional. The filter to list results by.

General `filter` string syntax: `<field> <operator> <value> (<logical connector>)`

    * `<field>` can be `name`, `address`, `port`, `metadata.<key>` for map field, or `attributes.<field>` for attributes field
    * `<operator>` can be `<`, `>`, `<=`, `>=`, `!=`, `=`, `:`. Of which `:` means `HAS`, and is roughly the same as `=`
    * `<value>` must be the same data type as field
    * `<logical connector>` can be `AND`, `OR`, `NOT`

Examples of valid filters:

    * `metadata.owner` returns endpoints that have a metadata with the key `owner`, this is the same as `metadata:owner`
    * `metadata.protocol=gRPC` returns endpoints that have key/value `protocol=gRPC`
    * `address=192.108.1.105` returns endpoints that have this address
    * `port>8080` returns endpoints that have port number larger than 8080 * `name>projects/my-project/locations/us-east1/namespaces/my-namespace/services/my-service/endpoints/endpoint-c` returns endpoints that have name that is alphabetically later than the string, so "endpoint-e" is returned but "endpoint-a" is not
    * `metadata.owner!=sd AND metadata.foo=bar` returns endpoints that have `owner` in metadata key but value is not `sd` AND have key/value `foo=bar`
    * `doesnotexist.foo=bar` returns an empty list. Note that endpoint doesn't have a field called "doesnotexist". Since the filter does not match any endpoints, it returns no results
    * `attributes.kubernetes_resource_type=KUBERNETES_RESOURCE_TYPE_CLUSTER_ IP` returns endpoints with the corresponding kubernetes_resource_type

For more information about filtering, see [API Filtering](https://aip.dev/160). 




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The filter to list results by.

General `filter` string syntax: `<field> <operator> <value> (<logical connector>)`

    * `<field>` can be `name`, `address`, `port`, `metadata.<key>` for map field, or `attributes.<field>` for attributes field
    * `<operator>` can be `<`, `>`, `<=`, `>=`, `!=`, `=`, `:`. Of which `:` means `HAS`, and is roughly the same as `=`
    * `<value>` must be the same data type as field
    * `<logical connector>` can be `AND`, `OR`, `NOT`

Examples of valid filters:

    * `metadata.owner` returns endpoints that have a metadata with the key `owner`, this is the same as `metadata:owner`
    * `metadata.protocol=gRPC` returns endpoints that have key/value `protocol=gRPC`
    * `address=192.108.1.105` returns endpoints that have this address
    * `port>8080` returns endpoints that have port number larger than 8080 * `name>projects/my-project/locations/us-east1/namespaces/my-namespace/services/my-service/endpoints/endpoint-c` returns endpoints that have name that is alphabetically later than the string, so "endpoint-e" is returned but "endpoint-a" is not
    * `metadata.owner!=sd AND metadata.foo=bar` returns endpoints that have `owner` in metadata key but value is not `sd` AND have key/value `foo=bar`
    * `doesnotexist.foo=bar` returns an empty list. Note that endpoint doesn't have a field called "doesnotexist". Since the filter does not match any endpoints, it returns no results
    * `attributes.kubernetes_resource_type=KUBERNETES_RESOURCE_TYPE_CLUSTER_ IP` returns endpoints with the corresponding kubernetes_resource_type

For more information about filtering, see [API Filtering](https://aip.dev/160). 




**Returns**

  * (::String) — Optional. The filter to list results by.

General `filter` string syntax: `<field> <operator> <value> (<logical connector>)`

    * `<field>` can be `name`, `address`, `port`, `metadata.<key>` for map field, or `attributes.<field>` for attributes field
    * `<operator>` can be `<`, `>`, `<=`, `>=`, `!=`, `=`, `:`. Of which `:` means `HAS`, and is roughly the same as `=`
    * `<value>` must be the same data type as field
    * `<logical connector>` can be `AND`, `OR`, `NOT`

Examples of valid filters:

    * `metadata.owner` returns endpoints that have a metadata with the key `owner`, this is the same as `metadata:owner`
    * `metadata.protocol=gRPC` returns endpoints that have key/value `protocol=gRPC`
    * `address=192.108.1.105` returns endpoints that have this address
    * `port>8080` returns endpoints that have port number larger than 8080 * `name>projects/my-project/locations/us-east1/namespaces/my-namespace/services/my-service/endpoints/endpoint-c` returns endpoints that have name that is alphabetically later than the string, so "endpoint-e" is returned but "endpoint-a" is not
    * `metadata.owner!=sd AND metadata.foo=bar` returns endpoints that have `owner` in metadata key but value is not `sd` AND have key/value `foo=bar`
    * `doesnotexist.foo=bar` returns an empty list. Note that endpoint doesn't have a field called "doesnotexist". Since the filter does not match any endpoints, it returns no results
    * `attributes.kubernetes_resource_type=KUBERNETES_RESOURCE_TYPE_CLUSTER_ IP` returns endpoints with the corresponding kubernetes_resource_type

For more information about filtering, see [API Filtering](https://aip.dev/160). 




### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. The order to list results by.

General `order_by` string syntax: `<field> (<asc|desc>) (,)`

    * `<field>` allows values: `name`, `address`, `port`
    * `<asc|desc>` ascending or descending order by `<field>`. If this is left blank, `asc` is used

Note that an empty `order_by` string results in default order, which is order by `name` in ascending order. 




### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The order to list results by.

General `order_by` string syntax: `<field> (<asc|desc>) (,)`

    * `<field>` allows values: `name`, `address`, `port`
    * `<asc|desc>` ascending or descending order by `<field>`. If this is left blank, `asc` is used

Note that an empty `order_by` string results in default order, which is order by `name` in ascending order. 




**Returns**

  * (::String) — Optional. The order to list results by.

General `order_by` string syntax: `<field> (<asc|desc>) (,)`

    * `<field>` allows values: `name`, `address`, `port`
    * `<asc|desc>` ascending or descending order by `<field>`. If this is left blank, `asc` is used

Note that an empty `order_by` string results in default order, which is order by `name` in ascending order. 




### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of items to return. The default value is 100. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of items to return. The default value is 100. 



**Returns**

  * (::Integer) — Optional. The maximum number of items to return. The default value is 100. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. The next_page_token value returned from a previous List request, if any. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The next_page_token value returned from a previous List request, if any. 



**Returns**

  * (::String) — Optional. The next_page_token value returned from a previous List request, if any. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the service whose endpoints you'd like to list. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the service whose endpoints you'd like to list. 



**Returns**

  * (::String) — Required. The resource name of the service whose endpoints you'd like to list. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
