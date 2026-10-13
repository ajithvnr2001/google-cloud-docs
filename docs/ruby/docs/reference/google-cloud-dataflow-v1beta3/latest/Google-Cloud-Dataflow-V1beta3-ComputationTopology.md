---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-ComputationTopology/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::ComputationTopology (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:58.348962+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::ComputationTopology (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-ComputationTopology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::ComputationTopology (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::ComputationTopology.

All configuration data for a particular Computation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #computation_id
    
    
    def computation_id() -> ::String

**Returns**

  * (::String) — The ID of the computation. 



### #computation_id=
    
    
    def computation_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The ID of the computation. 



**Returns**

  * (::String) — The ID of the computation. 



### #inputs
    
    
    def inputs() -> ::Array<::Google::Cloud::Dataflow::V1beta3::StreamLocation>

**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::StreamLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StreamLocation)>) — The inputs to the computation. 



### #inputs=
    
    
    def inputs=(value) -> ::Array<::Google::Cloud::Dataflow::V1beta3::StreamLocation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dataflow::V1beta3::StreamLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StreamLocation)>) — The inputs to the computation. 



**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::StreamLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StreamLocation)>) — The inputs to the computation. 



### #key_ranges
    
    
    def key_ranges() -> ::Array<::Google::Cloud::Dataflow::V1beta3::KeyRangeLocation>

**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::KeyRangeLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-KeyRangeLocation)>) — The key ranges processed by the computation. 



### #key_ranges=
    
    
    def key_ranges=(value) -> ::Array<::Google::Cloud::Dataflow::V1beta3::KeyRangeLocation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dataflow::V1beta3::KeyRangeLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-KeyRangeLocation)>) — The key ranges processed by the computation. 



**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::KeyRangeLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-KeyRangeLocation)>) — The key ranges processed by the computation. 



### #outputs
    
    
    def outputs() -> ::Array<::Google::Cloud::Dataflow::V1beta3::StreamLocation>

**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::StreamLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StreamLocation)>) — The outputs from the computation. 



### #outputs=
    
    
    def outputs=(value) -> ::Array<::Google::Cloud::Dataflow::V1beta3::StreamLocation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dataflow::V1beta3::StreamLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StreamLocation)>) — The outputs from the computation. 



**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::StreamLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StreamLocation)>) — The outputs from the computation. 



### #state_families
    
    
    def state_families() -> ::Array<::Google::Cloud::Dataflow::V1beta3::StateFamilyConfig>

**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::StateFamilyConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StateFamilyConfig)>) — The state family values. 



### #state_families=
    
    
    def state_families=(value) -> ::Array<::Google::Cloud::Dataflow::V1beta3::StateFamilyConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dataflow::V1beta3::StateFamilyConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StateFamilyConfig)>) — The state family values. 



**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::StateFamilyConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StateFamilyConfig)>) — The state family values. 



### #system_stage_name
    
    
    def system_stage_name() -> ::String

**Returns**

  * (::String) — The system stage name. 



### #system_stage_name=
    
    
    def system_stage_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The system stage name. 



**Returns**

  * (::String) — The system stage name. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
