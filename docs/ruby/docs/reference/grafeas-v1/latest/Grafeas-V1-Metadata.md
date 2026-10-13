---
url: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Metadata/
title: Grafeas V1 API - Class Grafeas::V1::Metadata (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:24.384136+00:00
---

# Grafeas V1 API - Class Grafeas::V1::Metadata (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Grafeas V1 API - Class Grafeas::V1::Metadata (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.1  1.0.0  0.16.1  0.15.0  0.14.2  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.1 

Reference documentation and code samples for the Grafeas V1 API class Grafeas::V1::Metadata.

Other properties of the build.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #build_finished_on
    
    
    def build_finished_on() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — The timestamp of when the build completed. 



### #build_finished_on=
    
    
    def build_finished_on=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — The timestamp of when the build completed. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — The timestamp of when the build completed. 



### #build_invocation_id
    
    
    def build_invocation_id() -> ::String

**Returns**

  * (::String) — Identifies the particular build invocation, which can be useful for finding associated logs or other ad-hoc analysis. The value SHOULD be globally unique, per in-toto Provenance spec. 



### #build_invocation_id=
    
    
    def build_invocation_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifies the particular build invocation, which can be useful for finding associated logs or other ad-hoc analysis. The value SHOULD be globally unique, per in-toto Provenance spec. 



**Returns**

  * (::String) — Identifies the particular build invocation, which can be useful for finding associated logs or other ad-hoc analysis. The value SHOULD be globally unique, per in-toto Provenance spec. 



### #build_started_on
    
    
    def build_started_on() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — The timestamp of when the build started. 



### #build_started_on=
    
    
    def build_started_on=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — The timestamp of when the build started. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — The timestamp of when the build started. 



### #completeness
    
    
    def completeness() -> ::Grafeas::V1::Completeness

**Returns**

  * ([::Grafeas::V1::Completeness](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Completeness)) — Indicates that the builder claims certain fields in this message to be complete. 



### #completeness=
    
    
    def completeness=(value) -> ::Grafeas::V1::Completeness

**Parameter**

  * **value** ([::Grafeas::V1::Completeness](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Completeness)) — Indicates that the builder claims certain fields in this message to be complete. 



**Returns**

  * ([::Grafeas::V1::Completeness](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Completeness)) — Indicates that the builder claims certain fields in this message to be complete. 



### #reproducible
    
    
    def reproducible() -> ::Boolean

**Returns**

  * (::Boolean) — If true, the builder claims that running the recipe on materials will produce bit-for-bit identical output. 



### #reproducible=
    
    
    def reproducible=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If true, the builder claims that running the recipe on materials will produce bit-for-bit identical output. 



**Returns**

  * (::Boolean) — If true, the builder claims that running the recipe on materials will produce bit-for-bit identical output. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
