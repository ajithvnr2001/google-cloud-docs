---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-MaintenanceSummary-Stats/
title: Maintenance V1 API - Class Google::Cloud::Maintenance::Api::V1::MaintenanceSummary::Stats (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:47.913228+00:00
---

# Maintenance V1 API - Class Google::Cloud::Maintenance::Api::V1::MaintenanceSummary::Stats (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-MaintenanceSummary-Stats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Maintenance V1 API - Class Google::Cloud::Maintenance::Api::V1::MaintenanceSummary::Stats (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Maintenance V1 API class Google::Cloud::Maintenance::Api::V1::MaintenanceSummary::Stats.

Stats indicates the type of aggregate and the corresponding aggregates.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #aggregates
    
    
    def aggregates() -> ::Array<::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary::Aggregate>

**Returns**

  * (::Array<[::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary::Aggregate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-MaintenanceSummary-Aggregate)>) — Aggregates is a list 



### #aggregates=
    
    
    def aggregates=(value) -> ::Array<::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary::Aggregate>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary::Aggregate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-MaintenanceSummary-Aggregate)>) — Aggregates is a list 



**Returns**

  * (::Array<[::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary::Aggregate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-MaintenanceSummary-Aggregate)>) — Aggregates is a list 



### #group_by
    
    
    def group_by() -> ::String

**Returns**

  * (::String) — groupBy specifies the type of aggregate. For example a group_by might be `"state"`



### #group_by=
    
    
    def group_by=(value) -> ::String

**Parameter**

  * **value** (::String) — groupBy specifies the type of aggregate. For example a group_by might be `"state"`



**Returns**

  * (::String) — groupBy specifies the type of aggregate. For example a group_by might be `"state"`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
