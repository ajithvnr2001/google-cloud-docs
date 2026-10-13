---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-AutoML-Paths/
title: Cloud AutoML V1 API - Module Google::Cloud::AutoML::V1::AutoML::Paths (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:50.813921+00:00
---

# Cloud AutoML V1 API - Module Google::Cloud::AutoML::V1::AutoML::Paths (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-AutoML-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1 API - Module Google::Cloud::AutoML::V1::AutoML::Paths (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.8 

Reference documentation and code samples for the Cloud AutoML V1 API module Google::Cloud::AutoML::V1::AutoML::Paths.

Path helper methods for the AutoMl API.

## Extended By

  * [Google::Cloud::AutoML::V1::AutoML::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-AutoML-Paths)



## Included In

  * [Google::Cloud::AutoML::V1::AutoML::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-AutoML-Client)
  * [Google::Cloud::AutoML::V1::AutoML::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-AutoML-Paths)
  * [Google::Cloud::AutoML::V1::AutoML::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-AutoML-Rest-Client)



## Methods 

### #annotation_spec_path
    
    
    def annotation_spec_path(project:, location:, dataset:, annotation_spec:) -> ::String

Create a fully-qualified AnnotationSpec resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **dataset** (String) 
  * **annotation_spec** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #dataset_path
    
    
    def dataset_path(project:, location:, dataset:) -> ::String

Create a fully-qualified Dataset resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/datasets/{dataset}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **dataset** (String) 



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



### #model_evaluation_path
    
    
    def model_evaluation_path(project:, location:, model:, model_evaluation:) -> ::String

Create a fully-qualified ModelEvaluation resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **model** (String) 
  * **model_evaluation** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #model_path
    
    
    def model_path(project:, location:, model:) -> ::String

Create a fully-qualified Model resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/models/{model}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **model** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
