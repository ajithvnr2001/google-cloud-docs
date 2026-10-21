---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/assess/
title: Method: datasets.assess \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:16:02.091952+00:00
---

# Method: datasets.assess  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/assess/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: datasets.assess Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.assess

Assesses the state or validity of the dataset with respect to a given use case.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{name}:assess`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`name` `string` Required. The name of the Dataset resource. Used only for MULTIMODAL datasets. Format: `projects/{project}/locations/{location}/datasets/{dataset}`

### Request body

The request body contains data with the following structure: | Fields  
  
`geminiRequestReadConfig` `object (`[GeminiRequestReadConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiRequestReadConfig)`)` Optional. The Gemini request read config for the dataset. | `assessment_config` `Union type`  
  
The assessment type. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`tuningValidationAssessmentConfig` `object (`[TuningValidationAssessmentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/assess#TuningValidationAssessmentConfig)`)` Optional. Configuration for the tuning validation assessment. | `tuningResourceUsageAssessmentConfig` `object (`[TuningResourceUsageAssessmentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/assess#TuningResourceUsageAssessmentConfig)`)` Optional. Configuration for the tuning resource usage assessment. | `batchPredictionValidationAssessmentConfig` `object (`[BatchPredictionValidationAssessmentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/assess#BatchPredictionValidationAssessmentConfig)`)` Optional. Configuration for the batch prediction validation assessment. | `batchPredictionResourceUsageAssessmentConfig` `object (`[BatchPredictionResourceUsageAssessmentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/assess#BatchPredictionResourceUsageAssessmentConfig)`)` Optional. Configuration for the batch prediction resource usage assessment. End of mutually exclusive fields.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

## TuningValidationAssessmentConfig

Configuration for the tuning validation assessment. | Fields  
  
`modelName` `string` Required. The name of the model used for tuning. | `datasetUsage` `enum (`[DatasetUsage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/assess#DatasetUsage)`)` Required. The dataset usage (e.g. training/validation). | JSON representation  
---  
      
    
    {
      "modelName": string,
      "datasetUsage": enum ([DatasetUsage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/assess#DatasetUsage))
    }  
  
## DatasetUsage

The dataset usage (e.g. training/validation).

Enums  
---  
`DATASET_USAGE_UNSPECIFIED` | Default value. Should not be used.  
`SFT_TRAINING` | Supervised fine-tuning training dataset.  
`SFT_VALIDATION` | Supervised fine-tuning validation dataset.  
  
## TuningResourceUsageAssessmentConfig

Configuration for the tuning resource usage assessment.

Fields  
  
`modelName` `string` Required. The name of the model used for tuning. | JSON representation  
---  
      
    
    {
      "modelName": string
    }  
  
## BatchPredictionValidationAssessmentConfig

Configuration for the batch prediction validation assessment.

Fields  
  
`modelName` `string` Required. The name of the model used for batch prediction. | JSON representation  
---  
      
    
    {
      "modelName": string
    }  
  
## BatchPredictionResourceUsageAssessmentConfig

Configuration for the batch prediction resource usage assessment.

Fields  
  
`modelName` `string` Required. The name of the model used for batch prediction. | JSON representation  
---  
      
    
    {
      "modelName": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
