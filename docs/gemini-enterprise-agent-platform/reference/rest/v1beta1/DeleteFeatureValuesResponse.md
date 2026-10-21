---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeleteFeatureValuesResponse/
title: DeleteFeatureValuesResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:48:59.763648+00:00
---

# DeleteFeatureValuesResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeleteFeatureValuesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  DeleteFeatureValuesResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for `[FeaturestoreService.DeleteFeatureValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/deleteFeatureValues#google.cloud.aiplatform.v1beta1.FeaturestoreService.DeleteFeatureValues)`.

Fields  
  
`response` `Union type`  
  
Response based on which delete option is specified in the request The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`selectEntity` `object (`[SelectEntity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeleteFeatureValuesResponse#SelectEntity)`)` Response for request specifying the entities to delete | `selectTimeRangeAndFeature` `object (`[SelectTimeRangeAndFeature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeleteFeatureValuesResponse#SelectTimeRangeAndFeature)`)` Response for request specifying time range and feature End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // response
      "selectEntity": {
        object ([SelectEntity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeleteFeatureValuesResponse#SelectEntity))
      },
      "selectTimeRangeAndFeature": {
        object ([SelectTimeRangeAndFeature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeleteFeatureValuesResponse#SelectTimeRangeAndFeature))
      }
      // Union type
    }  
  
## SelectEntity

Response message if the request uses the SelectEntity option.

Fields  
  
`offlineStorageDeletedEntityRowCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The count of deleted entity rows in the offline storage. Each row corresponds to the combination of an entity id and a timestamp. One entity id can have multiple rows in the offline storage. | `onlineStorageDeletedEntityCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The count of deleted entities in the online storage. Each entity id corresponds to one entity. | JSON representation  
---  
      
    
    {
      "offlineStorageDeletedEntityRowCount": string,
      "onlineStorageDeletedEntityCount": string
    }  
  
## SelectTimeRangeAndFeature

Response message if the request uses the SelectTimeRangeAndFeature option.

Fields  
  
`impactedFeatureCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The count of the features or columns impacted. This is the same as the feature count in the request. | `offlineStorageModifiedEntityRowCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The count of modified entity rows in the offline storage. Each row corresponds to the combination of an entity id and a timestamp. One entity id can have multiple rows in the offline storage. Within each row, only the features specified in the request are deleted. | `onlineStorageModifiedEntityCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The count of modified entities in the online storage. Each entity id corresponds to one entity. Within each entity, only the features specified in the request are deleted. | JSON representation  
---  
      
    
    {
      "impactedFeatureCount": string,
      "offlineStorageModifiedEntityRowCount": string,
      "onlineStorageModifiedEntityCount": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
