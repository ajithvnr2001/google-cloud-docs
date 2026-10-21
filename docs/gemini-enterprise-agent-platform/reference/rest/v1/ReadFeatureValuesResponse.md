---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse/
title: ReadFeatureValuesResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:05:18.941649+00:00
---

# ReadFeatureValuesResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ReadFeatureValuesResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for `[FeaturestoreOnlineServingService.ReadFeatureValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/readFeatureValues#google.cloud.aiplatform.v1.FeaturestoreOnlineServingService.ReadFeatureValues)`.

Fields  
  
`header` `object (`[Header](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#Header)`)` Response header. | `entityView` `object (`[EntityView](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#EntityView)`)` Entity view with feature values. This may be the entity in the Featurestore if values for all Features were requested, or a projection of the entity in the Featurestore if values for only some Features were requested. | JSON representation  
---  
      
    
    {
      "header": {
        object ([Header](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#Header))
      },
      "entityView": {
        object ([EntityView](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#EntityView))
      }
    }  
  
## Header

Response header with metadata for the requested `[ReadFeatureValuesRequest.entity_type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/readFeatureValues#body.PATH_PARAMETERS.entity_type)` and Features.

Fields  
  
`entityType` `string` The resource name of the EntityType from the `ReadFeatureValuesRequest`. value format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`. | `featureDescriptors[]` `object (`[FeatureDescriptor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#FeatureDescriptor)`)` List of feature metadata corresponding to each piece of `[ReadFeatureValuesResponse.EntityView.data](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#EntityView.FIELDS.data)`. | JSON representation  
---  
      
    
    {
      "entityType": string,
      "featureDescriptors": [
        {
          object ([FeatureDescriptor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#FeatureDescriptor))
        }
      ]
    }  
  
## FeatureDescriptor

metadata for requested Features.

Fields  
  
`id` `string` feature id. | JSON representation  
---  
      
    
    {
      "id": string
    }  
  
## EntityView

Entity view with feature values.

Fields  
  
`entityId` `string` id of the requested entity. | `data[]` `object (`[Data](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#Data)`)` Each piece of data holds the k requested values for one requested feature. If no values for the requested feature exist, the corresponding cell will be empty. This has the same size and is in the same order as the features from the header `[ReadFeatureValuesResponse.header](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#FIELDS.header)`. | JSON representation  
---  
      
    
    {
      "entityId": string,
      "data": [
        {
          object ([Data](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#Data))
        }
      ]
    }  
  
## Data

Container to hold value(s), successive in time, for one feature from the request.

Fields  
  
`data` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`value` `object (`[FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValue)`)` feature value if a single value is requested. | `values` `object (`[FeatureValueList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#FeatureValueList)`)` feature values list if values, successive in time, are requested. If the requested number of values is greater than the number of existing feature values, nonexistent values are omitted instead of being returned as empty. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // data
      "value": {
        object ([FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValue))
      },
      "values": {
        object ([FeatureValueList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ReadFeatureValuesResponse#FeatureValueList))
      }
      // Union type
    }  
  
## FeatureValueList

Container for list of values.

Fields  
  
`values[]` `object (`[FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValue)`)` A list of feature values. All of them should be the same data type. | JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValue))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
