---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-GeolocationConstraint/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::GeolocationConstraint (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:20.081904+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::GeolocationConstraint (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-GeolocationConstraint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::GeolocationConstraint (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::GeolocationConstraint.

Constraint of a geolocation field. Name of the geolocation field as defined in the schema.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #address
    
    
    def address() -> ::String

**Returns**

  * (::String) — The reference address that was inferred from the input query. The proximity of the reference address to the geolocation field will be used to filter the results. 



### #address=
    
    
    def address=(value) -> ::String

**Parameter**

  * **value** (::String) — The reference address that was inferred from the input query. The proximity of the reference address to the geolocation field will be used to filter the results. 



**Returns**

  * (::String) — The reference address that was inferred from the input query. The proximity of the reference address to the geolocation field will be used to filter the results. 



### #field_name
    
    
    def field_name() -> ::String

**Returns**

  * (::String) — The name of the geolocation field as defined in the schema. 



### #field_name=
    
    
    def field_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the geolocation field as defined in the schema. 



**Returns**

  * (::String) — The name of the geolocation field as defined in the schema. 



### #latitude
    
    
    def latitude() -> ::Float

**Returns**

  * (::Float) — The latitude of the geolocation inferred from the input query. 



### #latitude=
    
    
    def latitude=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The latitude of the geolocation inferred from the input query. 



**Returns**

  * (::Float) — The latitude of the geolocation inferred from the input query. 



### #longitude
    
    
    def longitude() -> ::Float

**Returns**

  * (::Float) — The longitude of the geolocation inferred from the input query. 



### #longitude=
    
    
    def longitude=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The longitude of the geolocation inferred from the input query. 



**Returns**

  * (::Float) — The longitude of the geolocation inferred from the input query. 



### #radius_in_meters
    
    
    def radius_in_meters() -> ::Float

**Returns**

  * (::Float) — The radius in meters around the address. The record is returned if the location of the geolocation field is within the radius. 



### #radius_in_meters=
    
    
    def radius_in_meters=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The radius in meters around the address. The record is returned if the location of the geolocation field is within the radius. 



**Returns**

  * (::Float) — The radius in meters around the address. The record is returned if the location of the geolocation field is within the radius. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
