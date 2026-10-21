---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageSegmentation/
title: AutoMlImageSegmentation \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:33:32.846701+00:00
---

# AutoMlImageSegmentation  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageSegmentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  AutoMlImageSegmentation Stay organized with collections  Save and categorize content based on your preferences. 

A TrainingJob that trains and uploads an AutoML Image Segmentation Model.

Fields  
  
`inputs` `object (`[AutoMlImageSegmentationInputs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageSegmentation#AutoMlImageSegmentationInputs)`)` The input parameters of this TrainingJob. | `metadata` `object (`[AutoMlImageSegmentationMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageSegmentation#AutoMlImageSegmentationMetadata)`)` The metadata information. | JSON representation  
---  
      
    
    {
      "inputs": {
        object ([AutoMlImageSegmentationInputs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageSegmentation#AutoMlImageSegmentationInputs))
      },
      "metadata": {
        object ([AutoMlImageSegmentationMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AutoMlImageSegmentation#AutoMlImageSegmentationMetadata))
      }
    }  
  
## AutoMlImageSegmentationInputs

Fields  
  
`modelType` `enum (`ModelType`)` | `budgetMilliNodeHours` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be `model-converged`. Note, node_hour = actual_hour * number_of_nodes_involved. Or actual_wall_clock_hours = trainBudgetMilliNodeHours / (number_of_nodes_involved * 1000) For modelType `cloud-high-accuracy-1`(default), the budget must be between 20,000 and 2,000,000 milli node hours, inclusive. The default value is 192,000 which represents one day in wall time (1000 milli * 24 hours * 8 nodes). | `baseModelId` `string` The id of the `base` model. If it is specified, the new model will be trained based on the `base` model. Otherwise, the new model will be trained from scratch. The `base` model must be in the same Project and Location as the new Model to train, and have the same modelType. | JSON representation  
---  
      
    
    {
      "modelType": enum (ModelType),
      "budgetMilliNodeHours": string,
      "baseModelId": string
    }  
  
## AutoMlImageSegmentationMetadata

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
