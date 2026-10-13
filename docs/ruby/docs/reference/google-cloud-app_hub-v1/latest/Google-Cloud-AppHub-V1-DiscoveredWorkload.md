---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_hub-v1/latest/Google-Cloud-AppHub-V1-DiscoveredWorkload/
title: App Hub V1 API - Class Google::Cloud::AppHub::V1::DiscoveredWorkload (v1.7.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:54.242612+00:00
---

# App Hub V1 API - Class Google::Cloud::AppHub::V1::DiscoveredWorkload (v1.7.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_hub-v1/latest/Google-Cloud-AppHub-V1-DiscoveredWorkload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Hub V1 API - Class Google::Cloud::AppHub::V1::DiscoveredWorkload (v1.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.2 (latest)  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the App Hub V1 API class Google::Cloud::AppHub::V1::DiscoveredWorkload.

DiscoveredWorkload is a binary deployment (such as managed instance groups (MIGs) and GKE deployments) that performs the smallest logical subset of business functionality. A discovered workload can be registered to an App Hub Workload.

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

  * (::String) — Identifier. The resource name of the discovered workload. Format: `"projects/{host-project-id}/locations/{location}/discoveredWorkloads/{uuid}"`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The resource name of the discovered workload. Format: `"projects/{host-project-id}/locations/{location}/discoveredWorkloads/{uuid}"`



**Returns**

  * (::String) — Identifier. The resource name of the discovered workload. Format: `"projects/{host-project-id}/locations/{location}/discoveredWorkloads/{uuid}"`



### #workload_properties
    
    
    def workload_properties() -> ::Google::Cloud::AppHub::V1::WorkloadProperties

**Returns**

  * ([::Google::Cloud::AppHub::V1::WorkloadProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_hub-v1/latest/Google-Cloud-AppHub-V1-WorkloadProperties)) — Output only. Properties of an underlying compute resource represented by the Workload. These are immutable. 



### #workload_reference
    
    
    def workload_reference() -> ::Google::Cloud::AppHub::V1::WorkloadReference

**Returns**

  * ([::Google::Cloud::AppHub::V1::WorkloadReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_hub-v1/latest/Google-Cloud-AppHub-V1-WorkloadReference)) — Output only. Reference of an underlying compute resource represented by the Workload. These are immutable. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
