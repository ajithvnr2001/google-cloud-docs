---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_risk-v1beta1/latest/Google-Cloud-WebRisk-V1beta1-ComputeThreatListDiffRequest-Constraints/
title: Web Risk V1beta1 API - Class Google::Cloud::WebRisk::V1beta1::ComputeThreatListDiffRequest::Constraints (v0.16.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:03.389931+00:00
---

# Web Risk V1beta1 API - Class Google::Cloud::WebRisk::V1beta1::ComputeThreatListDiffRequest::Constraints (v0.16.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_risk-v1beta1/latest/Google-Cloud-WebRisk-V1beta1-ComputeThreatListDiffRequest-Constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Web Risk V1beta1 API - Class Google::Cloud::WebRisk::V1beta1::ComputeThreatListDiffRequest::Constraints (v0.16.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.1 (latest)  0.16.0  0.15.1  0.14.1  0.13.0  0.12.1  0.11.0  0.10.1  0.9.2  0.8.0  0.7.1  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Web Risk V1beta1 API class Google::Cloud::WebRisk::V1beta1::ComputeThreatListDiffRequest::Constraints.

The constraints for this diff.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #max_database_entries
    
    
    def max_database_entries() -> ::Integer

**Returns**

  * (::Integer) — Sets the maximum number of entries that the client is willing to have in the local database. This should be a power of 2 between 2*_10 and 2_ *20. If zero, no database size limit is set. 



### #max_database_entries=
    
    
    def max_database_entries=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Sets the maximum number of entries that the client is willing to have in the local database. This should be a power of 2 between 2*_10 and 2_ *20. If zero, no database size limit is set. 



**Returns**

  * (::Integer) — Sets the maximum number of entries that the client is willing to have in the local database. This should be a power of 2 between 2*_10 and 2_ *20. If zero, no database size limit is set. 



### #max_diff_entries
    
    
    def max_diff_entries() -> ::Integer

**Returns**

  * (::Integer) — The maximum size in number of entries. The diff will not contain more entries than this value. This should be a power of 2 between 2*_10 and 2_ *20. If zero, no diff size limit is set. 



### #max_diff_entries=
    
    
    def max_diff_entries=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum size in number of entries. The diff will not contain more entries than this value. This should be a power of 2 between 2*_10 and 2_ *20. If zero, no diff size limit is set. 



**Returns**

  * (::Integer) — The maximum size in number of entries. The diff will not contain more entries than this value. This should be a power of 2 between 2*_10 and 2_ *20. If zero, no diff size limit is set. 



### #supported_compressions
    
    
    def supported_compressions() -> ::Array<::Google::Cloud::WebRisk::V1beta1::CompressionType>

**Returns**

  * (::Array<[::Google::Cloud::WebRisk::V1beta1::CompressionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_risk-v1beta1/latest/Google-Cloud-WebRisk-V1beta1-CompressionType)>) — The compression types supported by the client. 



### #supported_compressions=
    
    
    def supported_compressions=(value) -> ::Array<::Google::Cloud::WebRisk::V1beta1::CompressionType>

**Parameter**

  * **value** (::Array<[::Google::Cloud::WebRisk::V1beta1::CompressionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_risk-v1beta1/latest/Google-Cloud-WebRisk-V1beta1-CompressionType)>) — The compression types supported by the client. 



**Returns**

  * (::Array<[::Google::Cloud::WebRisk::V1beta1::CompressionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_risk-v1beta1/latest/Google-Cloud-WebRisk-V1beta1-CompressionType)>) — The compression types supported by the client. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
