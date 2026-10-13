---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-BigQueryDiscoveryTarget/
title: Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::BigQueryDiscoveryTarget (v1.19.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:38.542804+00:00
---

# Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::BigQueryDiscoveryTarget (v1.19.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-BigQueryDiscoveryTarget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::BigQueryDiscoveryTarget (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.1  1.17.0  1.16.1  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.2  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1 

Reference documentation and code samples for the Cloud Data Loss Prevention (DLP) V2 API class Google::Cloud::Dlp::V2::BigQueryDiscoveryTarget.

Target used to match against for discovery with BigQuery tables

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cadence
    
    
    def cadence() -> ::Google::Cloud::Dlp::V2::DiscoveryGenerationCadence

**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryGenerationCadence](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryGenerationCadence)) — How often and when to update profiles. New tables that match both the filter and conditions are scanned as quickly as possible depending on system capacity.

Note: The following fields are mutually exclusive: `cadence`, `disabled`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cadence=
    
    
    def cadence=(value) -> ::Google::Cloud::Dlp::V2::DiscoveryGenerationCadence

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::DiscoveryGenerationCadence](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryGenerationCadence)) — How often and when to update profiles. New tables that match both the filter and conditions are scanned as quickly as possible depending on system capacity.

Note: The following fields are mutually exclusive: `cadence`, `disabled`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryGenerationCadence](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryGenerationCadence)) — How often and when to update profiles. New tables that match both the filter and conditions are scanned as quickly as possible depending on system capacity.

Note: The following fields are mutually exclusive: `cadence`, `disabled`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #conditions
    
    
    def conditions() -> ::Google::Cloud::Dlp::V2::DiscoveryBigQueryConditions

**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryBigQueryConditions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryBigQueryConditions)) — In addition to matching the filter, these conditions must be true before a profile is generated. 



### #conditions=
    
    
    def conditions=(value) -> ::Google::Cloud::Dlp::V2::DiscoveryBigQueryConditions

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::DiscoveryBigQueryConditions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryBigQueryConditions)) — In addition to matching the filter, these conditions must be true before a profile is generated. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryBigQueryConditions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryBigQueryConditions)) — In addition to matching the filter, these conditions must be true before a profile is generated. 



### #disabled
    
    
    def disabled() -> ::Google::Cloud::Dlp::V2::Disabled

**Returns**

  * ([::Google::Cloud::Dlp::V2::Disabled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-Disabled)) — Tables that match this filter will not have profiles created.

Note: The following fields are mutually exclusive: `disabled`, `cadence`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #disabled=
    
    
    def disabled=(value) -> ::Google::Cloud::Dlp::V2::Disabled

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::Disabled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-Disabled)) — Tables that match this filter will not have profiles created.

Note: The following fields are mutually exclusive: `disabled`, `cadence`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dlp::V2::Disabled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-Disabled)) — Tables that match this filter will not have profiles created.

Note: The following fields are mutually exclusive: `disabled`, `cadence`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #filter
    
    
    def filter() -> ::Google::Cloud::Dlp::V2::DiscoveryBigQueryFilter

**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryBigQueryFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryBigQueryFilter)) — Required. The tables the discovery cadence applies to. The first target with a matching filter will be the one to apply to a table. 



### #filter=
    
    
    def filter=(value) -> ::Google::Cloud::Dlp::V2::DiscoveryBigQueryFilter

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::DiscoveryBigQueryFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryBigQueryFilter)) — Required. The tables the discovery cadence applies to. The first target with a matching filter will be the one to apply to a table. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryBigQueryFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryBigQueryFilter)) — Required. The tables the discovery cadence applies to. The first target with a matching filter will be the one to apply to a table. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
