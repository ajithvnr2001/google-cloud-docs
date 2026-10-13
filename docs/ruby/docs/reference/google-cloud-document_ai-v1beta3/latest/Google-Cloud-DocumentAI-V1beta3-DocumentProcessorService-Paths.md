---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Paths/
title: Document AI V1beta3 API - Module Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Paths (v0.49.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:20.005809+00:00
---

# Document AI V1beta3 API - Module Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Paths (v0.49.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Document AI V1beta3 API - Module Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Paths (v0.49.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.49.1 (latest)  0.49.0  0.48.1  0.47.0  0.46.2  0.45.0  0.44.0  0.43.1  0.42.0  0.41.0  0.40.0  0.39.1  0.38.0  0.37.0  0.36.1  0.35.0  0.34.0  0.33.1  0.32.0  0.31.0  0.30.2  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.4 

Reference documentation and code samples for the Document AI V1beta3 API module Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Paths.

Path helper methods for the DocumentProcessorService API.

## Extended By

  * [Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Paths)



## Included In

  * [Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Client)
  * [Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Paths)
  * [Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Rest-Client)



## Methods 

### #evaluation_path
    
    
    def evaluation_path(project:, location:, processor:, processor_version:, evaluation:) -> ::String

Create a fully-qualified Evaluation resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}/evaluations/{evaluation}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **processor** (String) 
  * **processor_version** (String) 
  * **evaluation** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #human_review_config_path
    
    
    def human_review_config_path(project:, location:, processor:) -> ::String

Create a fully-qualified HumanReviewConfig resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/processors/{processor}/humanReviewConfig`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **processor** (String) 



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



### #processor_path
    
    
    def processor_path(project:, location:, processor:) -> ::String

Create a fully-qualified Processor resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/processors/{processor}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **processor** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #processor_type_path
    
    
    def processor_type_path(project:, location:, processor_type:) -> ::String

Create a fully-qualified ProcessorType resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/processorTypes/{processor_type}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **processor_type** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #processor_version_path
    
    
    def processor_version_path(project:, location:, processor:, processor_version:) -> ::String

Create a fully-qualified ProcessorVersion resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **processor** (String) 
  * **processor_version** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
