---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/writeFeatureValues/
title: Method: entityTypes.writeFeatureValues \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:59:38.922809+00:00
---

# Method: entityTypes.writeFeatureValues  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/writeFeatureValues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: entityTypes.writeFeatureValues Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featurestores.entityTypes.writeFeatureValues

Writes feature values of one or more entities of an EntityType.

The feature values are merged into existing entities if any. The feature values to be written must have timestamp within the online storage retention.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{entityType}:writeFeatureValues`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`entityType` `string` Required. The resource name of the EntityType for the entities being written. value format: `projects/{project}/locations/{location}/featurestores/ {featurestore}/entityTypes/{entityType}`. For example, for a machine learning model predicting user clicks on a website, an EntityType id could be `user`.

### Request body

The request body contains data with the following structure: | Fields  
  
`payloads[]` `object (`[WriteFeatureValuesPayload](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/writeFeatureValues#WriteFeatureValuesPayload)`)` Required. The entities to be written. Up to 100,000 feature values can be written across all `payloads`.

### Response body

If successful, the response body is empty.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `entityType` resource:

  * `aiplatform.entityTypes.writeFeatureValues`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## WriteFeatureValuesPayload

Contains feature values to be written for a specific entity. | Fields  
  
`entityId` `string` Required. The id of the entity. | `featureValues` `map (key: string, value: object (`[FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureValue)`))` Required. feature values to be written, mapping from feature id to value. Up to 100,000 `featureValues` entries may be written across all payloads. The feature generation time, aligned by days, must be no older than five years (1825 days) and no later than one year (366 days) in the future. | JSON representation  
---  
      
    
    {
      "entityId": string,
      "featureValues": {
        string: {
          object ([FeatureValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureValue))
        },
        ...
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
