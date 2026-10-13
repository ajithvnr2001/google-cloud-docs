---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchResponse-Facet-FacetValue/
title: Retail V2 API - Class Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue (v2.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:31.352804+00:00
---

# Retail V2 API - Class Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue (v2.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchResponse-Facet-FacetValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Retail V2 API - Class Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue (v2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.0 (latest)  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.0  1.0.1  0.21.0  0.20.0  0.19.0  0.18.2  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Retail V2 API class Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue.

A facet value which contains value names and their count.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #count
    
    
    def count() -> ::Integer

**Returns**

  * (::Integer) — Number of items that have this facet value. 



### #count=
    
    
    def count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of items that have this facet value. 



**Returns**

  * (::Integer) — Number of items that have this facet value. 



### #interval
    
    
    def interval() -> ::Google::Cloud::Retail::V2::Interval

**Returns**

  * ([::Google::Cloud::Retail::V2::Interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-Interval)) — Interval value for a facet, such as [10, 20) for facet "price".

Note: The following fields are mutually exclusive: `interval`, `value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #interval=
    
    
    def interval=(value) -> ::Google::Cloud::Retail::V2::Interval

**Parameter**

  * **value** ([::Google::Cloud::Retail::V2::Interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-Interval)) — Interval value for a facet, such as [10, 20) for facet "price".

Note: The following fields are mutually exclusive: `interval`, `value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Retail::V2::Interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-Interval)) — Interval value for a facet, such as [10, 20) for facet "price".

Note: The following fields are mutually exclusive: `interval`, `value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #max_value
    
    
    def max_value() -> ::Float

**Returns**

  * (::Float) — The maximum value in the [FacetValue.interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchResponse-Facet-FacetValue#Google__Cloud__Retail__V2__SearchResponse__Facet__FacetValue_interval_instance_ "Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue#interval \(method\)"). Only supported on numerical facets and returned if [SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-FacetSpec-FacetKey#Google__Cloud__Retail__V2__SearchRequest__FacetSpec__FacetKey_return_min_max_instance_ "Google::Cloud::Retail::V2::SearchRequest::FacetSpec::FacetKey#return_min_max \(method\)") is true. 



### #max_value=
    
    
    def max_value=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The maximum value in the [FacetValue.interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchResponse-Facet-FacetValue#Google__Cloud__Retail__V2__SearchResponse__Facet__FacetValue_interval_instance_ "Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue#interval \(method\)"). Only supported on numerical facets and returned if [SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-FacetSpec-FacetKey#Google__Cloud__Retail__V2__SearchRequest__FacetSpec__FacetKey_return_min_max_instance_ "Google::Cloud::Retail::V2::SearchRequest::FacetSpec::FacetKey#return_min_max \(method\)") is true. 



**Returns**

  * (::Float) — The maximum value in the [FacetValue.interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchResponse-Facet-FacetValue#Google__Cloud__Retail__V2__SearchResponse__Facet__FacetValue_interval_instance_ "Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue#interval \(method\)"). Only supported on numerical facets and returned if [SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-FacetSpec-FacetKey#Google__Cloud__Retail__V2__SearchRequest__FacetSpec__FacetKey_return_min_max_instance_ "Google::Cloud::Retail::V2::SearchRequest::FacetSpec::FacetKey#return_min_max \(method\)") is true. 



### #min_value
    
    
    def min_value() -> ::Float

**Returns**

  * (::Float) — The minimum value in the [FacetValue.interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchResponse-Facet-FacetValue#Google__Cloud__Retail__V2__SearchResponse__Facet__FacetValue_interval_instance_ "Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue#interval \(method\)"). Only supported on numerical facets and returned if [SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-FacetSpec-FacetKey#Google__Cloud__Retail__V2__SearchRequest__FacetSpec__FacetKey_return_min_max_instance_ "Google::Cloud::Retail::V2::SearchRequest::FacetSpec::FacetKey#return_min_max \(method\)") is true. 



### #min_value=
    
    
    def min_value=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The minimum value in the [FacetValue.interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchResponse-Facet-FacetValue#Google__Cloud__Retail__V2__SearchResponse__Facet__FacetValue_interval_instance_ "Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue#interval \(method\)"). Only supported on numerical facets and returned if [SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-FacetSpec-FacetKey#Google__Cloud__Retail__V2__SearchRequest__FacetSpec__FacetKey_return_min_max_instance_ "Google::Cloud::Retail::V2::SearchRequest::FacetSpec::FacetKey#return_min_max \(method\)") is true. 



**Returns**

  * (::Float) — The minimum value in the [FacetValue.interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchResponse-Facet-FacetValue#Google__Cloud__Retail__V2__SearchResponse__Facet__FacetValue_interval_instance_ "Google::Cloud::Retail::V2::SearchResponse::Facet::FacetValue#interval \(method\)"). Only supported on numerical facets and returned if [SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-FacetSpec-FacetKey#Google__Cloud__Retail__V2__SearchRequest__FacetSpec__FacetKey_return_min_max_instance_ "Google::Cloud::Retail::V2::SearchRequest::FacetSpec::FacetKey#return_min_max \(method\)") is true. 



### #value
    
    
    def value() -> ::String

**Returns**

  * (::String) — Text value of a facet, such as "Black" for facet "colorFamilies".

Note: The following fields are mutually exclusive: `value`, `interval`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #value=
    
    
    def value=(value) -> ::String

**Parameter**

  * **value** (::String) — Text value of a facet, such as "Black" for facet "colorFamilies".

Note: The following fields are mutually exclusive: `value`, `interval`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Text value of a facet, such as "Black" for facet "colorFamilies".

Note: The following fields are mutually exclusive: `value`, `interval`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
