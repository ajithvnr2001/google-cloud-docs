---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-FacetSpec-FacetKey/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::FacetSpec::FacetKey (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:07.262902+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::FacetSpec::FacetKey (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-FacetSpec-FacetKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::FacetSpec::FacetKey (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::FacetSpec::FacetKey.

Specifies how a facet is computed.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #case_insensitive
    
    
    def case_insensitive() -> ::Boolean

**Returns**

  * (::Boolean) — True to make facet keys case insensitive when getting faceting values with prefixes or contains; false otherwise. 



### #case_insensitive=
    
    
    def case_insensitive=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — True to make facet keys case insensitive when getting faceting values with prefixes or contains; false otherwise. 



**Returns**

  * (::Boolean) — True to make facet keys case insensitive when getting faceting values with prefixes or contains; false otherwise. 



### #contains
    
    
    def contains() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Only get facet values that contain the given strings. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "contains" to "2022", the "category" facet only contains "Action > 2022" and "Sci-Fi > 2022". Only supported on textual fields. Maximum is 10. 



### #contains=
    
    
    def contains=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Only get facet values that contain the given strings. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "contains" to "2022", the "category" facet only contains "Action > 2022" and "Sci-Fi > 2022". Only supported on textual fields. Maximum is 10. 



**Returns**

  * (::Array<::String>) — Only get facet values that contain the given strings. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "contains" to "2022", the "category" facet only contains "Action > 2022" and "Sci-Fi > 2022". Only supported on textual fields. Maximum is 10. 



### #intervals
    
    
    def intervals() -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::Interval>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::Interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Interval)>) — Set only if values should be bucketed into intervals. Must be set for facets with numerical values. Must not be set for facet with text values. Maximum number of intervals is 30. 



### #intervals=
    
    
    def intervals=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::Interval>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::Interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Interval)>) — Set only if values should be bucketed into intervals. Must be set for facets with numerical values. Must not be set for facet with text values. Maximum number of intervals is 30. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::Interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Interval)>) — Set only if values should be bucketed into intervals. Must be set for facets with numerical values. Must not be set for facet with text values. Maximum number of intervals is 30. 



### #key
    
    
    def key() -> ::String

**Returns**

  * (::String) — Required. Supported textual and numerical facet keys in [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") object, over which the facet values are computed. Facet key is case-sensitive. 



### #key=
    
    
    def key=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Supported textual and numerical facet keys in [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") object, over which the facet values are computed. Facet key is case-sensitive. 



**Returns**

  * (::String) — Required. Supported textual and numerical facet keys in [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") object, over which the facet values are computed. Facet key is case-sensitive. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — The order in which documents are returned.

Allowed values are:

    * "count desc", which means order by [SearchResponse.Facet.values.count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Facet-FacetValue#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse__Facet__FacetValue_count_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet::FacetValue#count \(method\)") descending.

    * "value desc", which means order by [SearchResponse.Facet.values.value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Facet-FacetValue#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse__Facet__FacetValue_value_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet::FacetValue#value \(method\)") descending. Only applies to textual facets.

If not set, textual values are sorted in [natural order](https://en.wikipedia.org/wiki/Natural_sort_order); numerical intervals are sorted in the order given by [FacetSpec.FacetKey.intervals](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-FacetSpec-FacetKey#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest__FacetSpec__FacetKey_intervals_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::FacetSpec::FacetKey#intervals \(method\)"). 




### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — The order in which documents are returned.

Allowed values are:

    * "count desc", which means order by [SearchResponse.Facet.values.count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Facet-FacetValue#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse__Facet__FacetValue_count_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet::FacetValue#count \(method\)") descending.

    * "value desc", which means order by [SearchResponse.Facet.values.value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Facet-FacetValue#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse__Facet__FacetValue_value_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet::FacetValue#value \(method\)") descending. Only applies to textual facets.

If not set, textual values are sorted in [natural order](https://en.wikipedia.org/wiki/Natural_sort_order); numerical intervals are sorted in the order given by [FacetSpec.FacetKey.intervals](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-FacetSpec-FacetKey#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest__FacetSpec__FacetKey_intervals_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::FacetSpec::FacetKey#intervals \(method\)"). 




**Returns**

  * (::String) — The order in which documents are returned.

Allowed values are:

    * "count desc", which means order by [SearchResponse.Facet.values.count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Facet-FacetValue#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse__Facet__FacetValue_count_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet::FacetValue#count \(method\)") descending.

    * "value desc", which means order by [SearchResponse.Facet.values.value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Facet-FacetValue#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse__Facet__FacetValue_value_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet::FacetValue#value \(method\)") descending. Only applies to textual facets.

If not set, textual values are sorted in [natural order](https://en.wikipedia.org/wiki/Natural_sort_order); numerical intervals are sorted in the order given by [FacetSpec.FacetKey.intervals](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-FacetSpec-FacetKey#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest__FacetSpec__FacetKey_intervals_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::FacetSpec::FacetKey#intervals \(method\)"). 




### #prefixes
    
    
    def prefixes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Only get facet values that start with the given string prefix. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "prefixes" to "Action", the "category" facet only contains "Action > 2022" and "Action > 2021". Only supported on textual fields. Maximum is 10. 



### #prefixes=
    
    
    def prefixes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Only get facet values that start with the given string prefix. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "prefixes" to "Action", the "category" facet only contains "Action > 2022" and "Action > 2021". Only supported on textual fields. Maximum is 10. 



**Returns**

  * (::Array<::String>) — Only get facet values that start with the given string prefix. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "prefixes" to "Action", the "category" facet only contains "Action > 2022" and "Action > 2021". Only supported on textual fields. Maximum is 10. 



### #restricted_values
    
    
    def restricted_values() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Only get facet for the given restricted values. Only supported on textual fields. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "restricted_values" to "Action > 2022", the "category" facet only contains "Action > 2022". Only supported on textual fields. Maximum is 10. 



### #restricted_values=
    
    
    def restricted_values=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Only get facet for the given restricted values. Only supported on textual fields. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "restricted_values" to "Action > 2022", the "category" facet only contains "Action > 2022". Only supported on textual fields. Maximum is 10. 



**Returns**

  * (::Array<::String>) — Only get facet for the given restricted values. Only supported on textual fields. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "restricted_values" to "Action > 2022", the "category" facet only contains "Action > 2022". Only supported on textual fields. Maximum is 10. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
