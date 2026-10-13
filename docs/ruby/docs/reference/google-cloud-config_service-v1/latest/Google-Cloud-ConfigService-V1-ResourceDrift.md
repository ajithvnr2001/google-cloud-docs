---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceDrift/
title: Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::ResourceDrift (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:23.309485+00:00
---

# Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::ResourceDrift (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceDrift/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::ResourceDrift (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.1  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.3.0  1.2.1  1.1.0  1.0.2  0.6.0  0.5.0  0.4.0  0.3.1  0.2.1  0.1.0 

Reference documentation and code samples for the Infrastructure Manager V1 API class Google::Cloud::ConfigService::V1::ResourceDrift.

A resource drift represents a drift to a resource in the state file.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The name of the resource drift. Format: 'projects/{project_id}/locations/{location}/previews/{preview}/resourceDrifts/{resource_drift}'. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The name of the resource drift. Format: 'projects/{project_id}/locations/{location}/previews/{preview}/resourceDrifts/{resource_drift}'. 



**Returns**

  * (::String) — Identifier. The name of the resource drift. Format: 'projects/{project_id}/locations/{location}/previews/{preview}/resourceDrifts/{resource_drift}'. 



### #property_drifts
    
    
    def property_drifts() -> ::Array<::Google::Cloud::ConfigService::V1::PropertyDrift>

**Returns**

  * (::Array<[::Google::Cloud::ConfigService::V1::PropertyDrift](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-PropertyDrift)>) — Output only. The property drifts of the resource drift. 



### #terraform_info
    
    
    def terraform_info() -> ::Google::Cloud::ConfigService::V1::ResourceDriftTerraformInfo

**Returns**

  * ([::Google::Cloud::ConfigService::V1::ResourceDriftTerraformInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceDriftTerraformInfo)) — Output only. Terraform info of the resource drift. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
