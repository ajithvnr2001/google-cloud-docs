---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/deleteFeatureValues/
title: Method: entityTypes.deleteFeatureValues \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:58.006363+00:00
---

# Method: entityTypes.deleteFeatureValues  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/deleteFeatureValues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: entityTypes.deleteFeatureValues Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featurestores.entityTypes.deleteFeatureValues

Delete feature values from Featurestore.

The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done.

If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done.

### Endpoint

post  `https://{service-endpoint}/v1/{entityType}:deleteFeatureValues`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`entityType` `string` Required. The resource name of the EntityType grouping the Features for which values are being deleted from. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`

### Request body

The request body contains data with the following structure: | Fields  
  
`DeleteOption` `Union type`  
  
Defines options to select feature values to be deleted. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`selectEntity` `object (`[SelectEntity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/deleteFeatureValues#SelectEntity)`)` Select feature values to be deleted by specifying entities. | `selectTimeRangeAndFeature` `object (`[SelectTimeRangeAndFeature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/deleteFeatureValues#SelectTimeRangeAndFeature)`)` Select feature values to be deleted by specifying time range and features. End of mutually exclusive fields.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `entityType` resource:

  * `aiplatform.entityTypes.deleteFeatureValues`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## SelectEntity

message to select entity. If an entity id is selected, all the feature values corresponding to the entity id will be deleted, including the entityId. | Fields  
  
`entityIdSelector` `object (`[EntityIdSelector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/deleteFeatureValues#EntityIdSelector)`)` Required. Selectors choosing feature values of which entity id to be deleted from the EntityType. | JSON representation  
---  
      
    
    {
      "entityIdSelector": {
        object ([EntityIdSelector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/deleteFeatureValues#EntityIdSelector))
      }
    }  
  
## EntityIdSelector

Selector for entityId. Getting ids from the given source.

Fields  
  
`entityIdField` `string` Source column that holds entity IDs. If not provided, entity IDs are extracted from the column named entity_id. | `EntityIdsSource` `Union type`  
  
Details about the source data, including the location of the storage and the format. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`csvSource` `object (`[CsvSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/CsvSource)`)` Source of Csv End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "entityIdField": string,
    
      // EntityIdsSource
      "csvSource": {
        object ([CsvSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/CsvSource))
      }
      // Union type
    }  
  
## SelectTimeRangeAndFeature

message to select time range and feature. Values of the selected feature generated within an inclusive time range will be deleted. Using this option permanently deletes the feature values from the specified feature IDs within the specified time range. This might include data from the online storage. If you want to retain any deleted historical data in the online storage, you must re-ingest it.

Fields  
  
`timeRange` `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Interval)`)` Required. Select feature generated within a half-inclusive time range. The time range is lower inclusive and upper exclusive. | `featureSelector` `object (`[FeatureSelector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureSelector)`)` Required. Selectors choosing which feature values to be deleted from the EntityType. | `skipOnlineStorageDelete` `boolean` If set, data will not be deleted from online storage. When time range is older than the data in online storage, setting this to be true will make the deletion have no impact on online serving. | JSON representation  
---  
      
    
    {
      "timeRange": {
        object ([Interval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Interval))
      },
      "featureSelector": {
        object ([FeatureSelector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureSelector))
      },
      "skipOnlineStorageDelete": boolean
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
