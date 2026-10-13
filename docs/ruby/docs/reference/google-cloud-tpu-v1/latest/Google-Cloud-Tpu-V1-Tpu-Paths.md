---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Tpu-Paths/
title: Cloud TPU V1 API - Module Google::Cloud::Tpu::V1::Tpu::Paths (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:14.557747+00:00
---

# Cloud TPU V1 API - Module Google::Cloud::Tpu::V1::Tpu::Paths (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Tpu-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud TPU V1 API - Module Google::Cloud::Tpu::V1::Tpu::Paths (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Cloud TPU V1 API module Google::Cloud::Tpu::V1::Tpu::Paths.

Path helper methods for the Tpu API.

## Extended By

  * [Google::Cloud::Tpu::V1::Tpu::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Tpu-Paths)



## Included In

  * [Google::Cloud::Tpu::V1::Tpu::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Tpu-Client)
  * [Google::Cloud::Tpu::V1::Tpu::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Tpu-Paths)



## Methods 

### #accelerator_type_path
    
    
    def accelerator_type_path(project:, location:, accelerator_type:) -> ::String

Create a fully-qualified AcceleratorType resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/acceleratorTypes/{accelerator_type}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **accelerator_type** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #node_path
    
    
    def node_path(project:, location:, node:) -> ::String

Create a fully-qualified Node resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/nodes/{node}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **node** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #tensor_flow_version_path
    
    
    def tensor_flow_version_path(project:, location:, tensor_flow_version:) -> ::String

Create a fully-qualified TensorFlowVersion resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/tensorFlowVersions/{tensor_flow_version}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **tensor_flow_version** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
