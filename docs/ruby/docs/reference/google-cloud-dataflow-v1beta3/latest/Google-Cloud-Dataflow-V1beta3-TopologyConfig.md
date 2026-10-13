---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-TopologyConfig/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::TopologyConfig (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:31.924686+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::TopologyConfig (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-TopologyConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::TopologyConfig (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::TopologyConfig.

Global topology of the streaming Dataflow job, including all computations and their sharded locations.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #computations
    
    
    def computations() -> ::Array<::Google::Cloud::Dataflow::V1beta3::ComputationTopology>

**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::ComputationTopology](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-ComputationTopology)>) — The computations associated with a streaming Dataflow job. 



### #computations=
    
    
    def computations=(value) -> ::Array<::Google::Cloud::Dataflow::V1beta3::ComputationTopology>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dataflow::V1beta3::ComputationTopology](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-ComputationTopology)>) — The computations associated with a streaming Dataflow job. 



**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::ComputationTopology](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-ComputationTopology)>) — The computations associated with a streaming Dataflow job. 



### #data_disk_assignments
    
    
    def data_disk_assignments() -> ::Array<::Google::Cloud::Dataflow::V1beta3::DataDiskAssignment>

**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::DataDiskAssignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-DataDiskAssignment)>) — The disks assigned to a streaming Dataflow job. 



### #data_disk_assignments=
    
    
    def data_disk_assignments=(value) -> ::Array<::Google::Cloud::Dataflow::V1beta3::DataDiskAssignment>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dataflow::V1beta3::DataDiskAssignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-DataDiskAssignment)>) — The disks assigned to a streaming Dataflow job. 



**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::DataDiskAssignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-DataDiskAssignment)>) — The disks assigned to a streaming Dataflow job. 



### #forwarding_key_bits
    
    
    def forwarding_key_bits() -> ::Integer

**Returns**

  * (::Integer) — The size (in bits) of keys that will be assigned to source messages. 



### #forwarding_key_bits=
    
    
    def forwarding_key_bits=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The size (in bits) of keys that will be assigned to source messages. 



**Returns**

  * (::Integer) — The size (in bits) of keys that will be assigned to source messages. 



### #persistent_state_version
    
    
    def persistent_state_version() -> ::Integer

**Returns**

  * (::Integer) — Version number for persistent state. 



### #persistent_state_version=
    
    
    def persistent_state_version=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Version number for persistent state. 



**Returns**

  * (::Integer) — Version number for persistent state. 



### #user_stage_to_computation_name_map
    
    
    def user_stage_to_computation_name_map() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Maps user stage names to stable computation names. 



### #user_stage_to_computation_name_map=
    
    
    def user_stage_to_computation_name_map=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Maps user stage names to stable computation names. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Maps user stage names to stable computation names. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
