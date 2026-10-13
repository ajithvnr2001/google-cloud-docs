---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Api-SelectiveGapicGeneration/
title: Memorystore V1BETA API - Class Google::Api::SelectiveGapicGeneration (v0.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:05.383469+00:00
---

# Memorystore V1BETA API - Class Google::Api::SelectiveGapicGeneration (v0.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Api-SelectiveGapicGeneration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Memorystore V1BETA API - Class Google::Api::SelectiveGapicGeneration (v0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Memorystore V1BETA API class Google::Api::SelectiveGapicGeneration.

This message is used to configure the generation of a subset of the RPCs in a service for client libraries.

Note: This feature should not be used in most cases.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #generate_omitted_as_internal
    
    
    def generate_omitted_as_internal() -> ::Boolean

**Returns**

  * (::Boolean) — Setting this to true indicates to the client generators that methods that would be excluded from the generation should instead be generated in a way that indicates these methods should not be consumed by end users. How this is expressed is up to individual language implementations to decide. Some examples may be: added annotations, obfuscated identifiers, or other language idiomatic patterns. 



### #generate_omitted_as_internal=
    
    
    def generate_omitted_as_internal=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Setting this to true indicates to the client generators that methods that would be excluded from the generation should instead be generated in a way that indicates these methods should not be consumed by end users. How this is expressed is up to individual language implementations to decide. Some examples may be: added annotations, obfuscated identifiers, or other language idiomatic patterns. 



**Returns**

  * (::Boolean) — Setting this to true indicates to the client generators that methods that would be excluded from the generation should instead be generated in a way that indicates these methods should not be consumed by end users. How this is expressed is up to individual language implementations to decide. Some examples may be: added annotations, obfuscated identifiers, or other language idiomatic patterns. 



### #methods
    
    
    def methods() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — An allowlist of the fully qualified names of RPCs that should be included on public client surfaces. 



### #methods=
    
    
    def methods=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — An allowlist of the fully qualified names of RPCs that should be included on public client surfaces. 



**Returns**

  * (::Array<::String>) — An allowlist of the fully qualified names of RPCs that should be included on public client surfaces. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
