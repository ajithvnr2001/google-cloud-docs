---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageObjectDetection/
title: AutoMlImageObjectDetection \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:20:29.307228+00:00
---

# AutoMlImageObjectDetection  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageObjectDetection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  AutoMlImageObjectDetection Stay organized with collections  Save and categorize content based on your preferences. 

A TrainingJob that trains and uploads an AutoML Image Object Detection Model.

Fields  
  
`inputs` `object (`[AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageObjectDetection#AutoMlImageObjectDetectionInputs)`)` The input parameters of this TrainingJob. | `metadata` `object (`[AutoMlImageObjectDetectionMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageObjectDetection#AutoMlImageObjectDetectionMetadata)`)` The metadata information | JSON representation  
---  
      
    
    {
      "inputs": {
        object ([AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageObjectDetection#AutoMlImageObjectDetectionInputs))
      },
      "metadata": {
        object ([AutoMlImageObjectDetectionMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageObjectDetection#AutoMlImageObjectDetectionMetadata))
      }
    }  
  
## AutoMlImageObjectDetectionInputs

Fields  
  
`modelType` `enum (`ModelType`)` | `budgetMilliNodeHours` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be `model-converged`. Note, node_hour = actual_hour * number_of_nodes_involved. For modelType `cloud`(default), the budget must be between 20,000 and 900,000 milli node hours, inclusive. The default value is 216,000 which represents one day in wall time, considering 9 nodes are used. For model types `mobile-tf-low-latency-1`, `mobile-tf-versatile-1`, `mobile-tf-high-accuracy-1` the training budget must be between 1,000 and 100,000 milli node hours, inclusive. The default value is 24,000 which represents one day in wall time on a single node that is used. | `disableEarlyStopping` `boolean` Use the entire training budget. This disables the early stopping feature. When false the early stopping feature is enabled, which means that AutoML Image Object Detection might stop training before the entire training budget has been used. | `uptrainBaseModelId` `string` The id of `base` model for upTraining. If it is specified, the new model will be upTrained based on the `base` model for upTraining. Otherwise, the new model will be trained from scratch. The `base` model for upTraining must be in the same Project and Location as the new Model to train, and have the same modelType. | JSON representation  
---  
      
    
    {
      "modelType": enum (ModelType),
      "budgetMilliNodeHours": string,
      "disableEarlyStopping": boolean,
      "uptrainBaseModelId": string
    }  
  
## AutoMlImageObjectDetectionMetadata

Fields  
  
`costMilliNodeHours` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The actual training cost of creating this model, expressed in milli node hours, i.e. 1,000 value in this field means 1 node hour. Guaranteed to not exceed inputs.budgetMilliNodeHours. | `successfulStopReason` `enum (`SuccessfulStopReason`)` For successful job completions, this is the reason why the job has finished. | JSON representation  
---  
      
    
    {
      "costMilliNodeHours": string,
      "successfulStopReason": enum (SuccessfulStopReason)
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
