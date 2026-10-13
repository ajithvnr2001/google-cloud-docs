---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-private_catalog-v1beta1/latest/Google-Cloud-PrivateCatalog-V1beta1-SearchVersionsRequest/
title: Private Catalog V1beta1 API - Class Google::Cloud::PrivateCatalog::V1beta1::SearchVersionsRequest (v0.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:52.737712+00:00
---

# Private Catalog V1beta1 API - Class Google::Cloud::PrivateCatalog::V1beta1::SearchVersionsRequest (v0.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-private_catalog-v1beta1/latest/Google-Cloud-PrivateCatalog-V1beta1-SearchVersionsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Private Catalog V1beta1 API - Class Google::Cloud::PrivateCatalog::V1beta1::SearchVersionsRequest (v0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.14.1  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.1  0.7.1  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Private Catalog V1beta1 API class Google::Cloud::PrivateCatalog::V1beta1::SearchVersionsRequest.

Request message for [PrivateCatalog.SearchVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-private_catalog-v1beta1/latest/Google-Cloud-PrivateCatalog-V1beta1-PrivateCatalog-Client#Google__Cloud__PrivateCatalog__V1beta1__PrivateCatalog__Client_search_versions_instance_ "Google::Cloud::PrivateCatalog::V1beta1::PrivateCatalog::Client#search_versions \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of entries that are requested. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of entries that are requested. 



**Returns**

  * (::Integer) — The maximum number of entries that are requested. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A pagination token returned from a previous call to SearchVersions that indicates where this listing should continue from. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A pagination token returned from a previous call to SearchVersions that indicates where this listing should continue from. 



**Returns**

  * (::String) — A pagination token returned from a previous call to SearchVersions that indicates where this listing should continue from. 



### #query
    
    
    def query() -> ::String

**Returns**

  * (::String) — 

Required. The query to filter the versions.

The supported queries are:

    * List versions under a product: `parent=catalogs/{catalog}/products/{product}`
    * Get a version by name: `name=catalogs/{catalog}/products/{product}/versions/{version}`



### #query=
    
    
    def query=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The query to filter the versions.

The supported queries are:

    * List versions under a product: `parent=catalogs/{catalog}/products/{product}`
    * Get a version by name: `name=catalogs/{catalog}/products/{product}/versions/{version}`



**Returns**

  * (::String) — 

Required. The query to filter the versions.

The supported queries are:

    * List versions under a product: `parent=catalogs/{catalog}/products/{product}`
    * Get a version by name: `name=catalogs/{catalog}/products/{product}/versions/{version}`



### #resource
    
    
    def resource() -> ::String

**Returns**

  * (::String) — Required. The name of the resource context. See [SearchCatalogsRequest.resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-private_catalog-v1beta1/latest/Google-Cloud-PrivateCatalog-V1beta1-SearchCatalogsRequest#Google__Cloud__PrivateCatalog__V1beta1__SearchCatalogsRequest_resource_instance_ "Google::Cloud::PrivateCatalog::V1beta1::SearchCatalogsRequest#resource \(method\)") for details. 



### #resource=
    
    
    def resource=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the resource context. See [SearchCatalogsRequest.resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-private_catalog-v1beta1/latest/Google-Cloud-PrivateCatalog-V1beta1-SearchCatalogsRequest#Google__Cloud__PrivateCatalog__V1beta1__SearchCatalogsRequest_resource_instance_ "Google::Cloud::PrivateCatalog::V1beta1::SearchCatalogsRequest#resource \(method\)") for details. 



**Returns**

  * (::String) — Required. The name of the resource context. See [SearchCatalogsRequest.resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-private_catalog-v1beta1/latest/Google-Cloud-PrivateCatalog-V1beta1-SearchCatalogsRequest#Google__Cloud__PrivateCatalog__V1beta1__SearchCatalogsRequest_resource_instance_ "Google::Cloud::PrivateCatalog::V1beta1::SearchCatalogsRequest#resource \(method\)") for details. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
