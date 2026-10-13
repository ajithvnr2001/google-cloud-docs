---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/batchReadFeatureValues/
title: Method: featurestores.batchReadFeatureValues \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:36.913873+00:00
---

# Method: featurestores.batchReadFeatureValues  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/batchReadFeatureValues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: featurestores.batchReadFeatureValues Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featurestores.batchReadFeatureValues

Batch reads feature values from a Featurestore.

This API enables batch reading feature values, where each read instance in the batch may read feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for feature values of each read instance as of each instance's read timestamp.

### Endpoint

post  `https://{service-endpoint}/v1/{featurestore}:batchReadFeatureValues`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`featurestore` `string` Required. The resource name of the Featurestore from which to query feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`

### Request body

The request body contains data with the following structure: | Fields  
  
`destination` `object (`[FeatureValueDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValueDestination)`)` Required. Specifies output location and format. | `passThroughFields[]` `object (`[PassThroughField](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/batchReadFeatureValues#PassThroughField)`)` When not empty, the specified fields in the *_read_instances source will be joined as-is in the output, in addition to those fields from the Featurestore Entity.For BigQuery source, the type of the pass-through values will be automatically inferred. For CSV source, the pass-through values will be passed as opaque bytes. | `entityTypeSpecs[]` `object (`[EntityTypeSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/batchReadFeatureValues#EntityTypeSpec)`)` Required. Specifies EntityType grouping Features to read values of and settings. | `startTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Excludes feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in feature Store. timestamp, if present, must not have higher than millisecond precision.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `read_option` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`csvReadInstances` `object (`[CsvSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/CsvSource)`)` Each read instance consists of exactly one read timestamp and one or more entity IDs identifying entities of the corresponding EntityTypes whose Features are requested.Each output instance contains feature values of requested entities concatenated together as of the read time.An example read instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z`.An example output instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z, foo_entity_feature1_value, bar_entity_feature2_value`.timestamp in each read instance must be millisecond-aligned.`csvReadInstances` are read instances stored in a plain-text CSV file. The header should be: [ENTITY_TYPE_ID1], [ENTITY_TYPE_ID2], ..., timestampThe columns can be in any order.Values in the timestamp column must use the RFC 3339 format, e.g. `2012-07-30T10:43:17.123Z`. | `bigqueryReadInstances` `object (`[BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/BigQuerySource)`)` Similar to csvReadInstances, but from BigQuery source. End of mutually exclusive fields.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

## PassThroughField

Describe pass-through fields in read_instance source. | Fields  
  
`fieldName` `string` Required. The name of the field in the CSV header or the name of the column in BigQuery table. The naming restriction is the same as `[feature.name](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups.features#Feature.FIELDS.name)`. | JSON representation  
---  
      
    
    {
      "fieldName": string
    }  
  
## EntityTypeSpec

Selects Features of an EntityType to read values of and specifies read settings.

Fields  
  
`entityTypeId` `string` Required. id of the EntityType to select Features. The EntityType id is the `[entityTypeId](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/create#body.QUERY_PARAMETERS.entity_type_id)` specified during EntityType creation. | `featureSelector` `object (`[FeatureSelector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureSelector)`)` Required. Selectors choosing which feature values to read from the EntityType. | `settings[]` `object (`[DestinationFeatureSetting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DestinationFeatureSetting)`)` Per-feature settings for the batch read. | JSON representation  
---  
      
    
    {
      "entityTypeId": string,
      "featureSelector": {
        object ([FeatureSelector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureSelector))
      },
      "settings": [
        {
          object ([DestinationFeatureSetting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DestinationFeatureSetting))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
