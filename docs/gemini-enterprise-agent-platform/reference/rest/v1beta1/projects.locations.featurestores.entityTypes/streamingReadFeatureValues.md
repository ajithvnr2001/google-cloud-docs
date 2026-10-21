---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/streamingReadFeatureValues/
title: Method: entityTypes.streamingReadFeatureValues \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:10:10.987431+00:00
---

# Method: entityTypes.streamingReadFeatureValues  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/streamingReadFeatureValues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: entityTypes.streamingReadFeatureValues Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featurestores.entityTypes.streamingReadFeatureValues

Reads feature values for multiple entities. Depending on their size, data for different entities may be broken up across multiple responses.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{entityType}:streamingReadFeatureValues`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`entityType` `string` Required. The resource name of the entities' type. value format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`. For example, for a machine learning model predicting user clicks on a website, an EntityType id could be `user`.

### Request body

The request body contains data with the following structure: | Fields  
  
`entityIds[]` `string` Required. IDs of entities to read feature values of. The maximum number of IDs is 100. For example, for a machine learning model predicting user clicks on a website, an entity id could be `user_123`. | `featureSelector` `object (`[FeatureSelector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureSelector)`)` Required. Selector choosing Features of the target EntityType. feature IDs will be deduplicated.

### Response body

If successful, the response body contains a stream of `[ReadFeatureValuesResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ReadFeatureValuesResponse)` instances. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-05-04 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
