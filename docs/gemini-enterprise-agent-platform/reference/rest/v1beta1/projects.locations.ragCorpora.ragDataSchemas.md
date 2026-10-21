---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas
title: REST Resource: projects.locations.ragCorpora.ragDataSchemas \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:56:48.095665+00:00
---

# REST Resource: projects.locations.ragCorpora.ragDataSchemas  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.ragCorpora.ragDataSchemas Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: RagDataSchema

The schema of the user specified metadata.

Fields  
  
`name` `string` Identifier. Resource name of the data schema in the form of: `projects/{projectNumber}/locations/{location}/ragCorpora/{ragCorpus}/ragDataSchemas/{ragDataSchema}` where the {ragDataSchema} part should be the same as the `key` field below. | `key` `string` Required. The key of this data schema. This key should be matching the key of user specified metadata and unique inside corpus. This value can be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number. | `schemaDetails` `object (`[RagMetadataSchemaDetails](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#RagMetadataSchemaDetails)`)` The schema details mapping to the key. | JSON representation  
---  
      
    
    {
      "name": string,
      "key": string,
      "schemaDetails": {
        object ([RagMetadataSchemaDetails](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#RagMetadataSchemaDetails))
      }
    }  
  
## RagMetadataSchemaDetails

data schema details indicates the data type and the data struct corresponding to the key of user specified metadata.

Fields  
  
`listConfig` `object (`[ListConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#ListConfig)`)` Config for List data type. | `type` `enum (`[DataType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#DataType)`)` type of the metadata. | `granularity` `enum (`[Granularity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#Granularity)`)` The granularity associated with this RagMetadataSchema. | `searchStrategy` `object (`[SearchStrategy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#SearchStrategy)`)` The search strategy for the metadata value of the `key`. | JSON representation  
---  
      
    
    {
      "listConfig": {
        object ([ListConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#ListConfig))
      },
      "type": enum ([DataType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#DataType)),
      "granularity": enum ([Granularity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#Granularity)),
      "searchStrategy": {
        object ([SearchStrategy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#SearchStrategy))
      }
    }  
  
## DataType

data type of the metadata.

Enums  
---  
`DATA_TYPE_UNSPECIFIED` | Unspecified type.  
`INTEGER` | Integer type.  
`FLOAT` | Float type.  
`STRING` | String type.  
`DATETIME` | Supported formats: %Y-%m-%dT%H:%M:%E*S%E*z (absl::RFC3339_full) %Y-%m-%dT%H:%M:%E*S %Y-%m-%dT%H:%M%E*z %Y-%m-%dT%H:%M %Y-%m-%dT%H%E*z %Y-%m-%dT%H %Y-%m-%d%E*z %Y-%m-%d %Y-%m %Y  
`BOOLEAN` | Boolean type.  
`LIST` | List type. - Each element in the list must be of the exact same data schema; otherwise, they are invalid arguments. - Elements cannot be another list (no list of list).  
  
## ListConfig

Config for List data type.

Fields  
  
`valueSchema` `object (`[RagMetadataSchemaDetails](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#RagMetadataSchemaDetails)`)` The value's data type in the list. | JSON representation  
---  
      
    
    {
      "valueSchema": {
        object ([RagMetadataSchemaDetails](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#RagMetadataSchemaDetails))
      }
    }  
  
## Granularity

The granularity of metadata under this DataSchema.

Enums  
---  
`GRANULARITY_UNSPECIFIED` | Unspecified granularity.  
`GRANULARITY_FILE_LEVEL` | RagFile-level granularity.  
  
## SearchStrategy

The search strategy for the metadata value of the `key`.

Fields  
  
`searchStrategyType` `enum (`[SearchStrategyType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#SearchStrategyType)`)` The search strategy type to be applied on the metadata key. | JSON representation  
---  
      
    
    {
      "searchStrategyType": enum ([SearchStrategyType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#SearchStrategyType))
    }  
  
## SearchStrategyType

The types of search strategies to be applied on the metadata key.

Enums  
---  
`SEARCH_STRATEGY_TYPE_UNSPECIFIED` | Unspecified search strategy type.  
`NO_SEARCH` | metadata values of the `key` above will not be searchable.  
`EXACT_SEARCH` | When searching with `key`, the value must be exactly as the metadata value that has been ingested.  
  
## Methods  
  
---  
  
### `[batchCreate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/batchCreate)`

|  Batch Create one or more RagDataSchemas  
  
### `[batchDelete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/batchDelete)`

|  Batch Deletes one or more RagDataSchemas  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/create)`

|  Creates a RagDataSchema.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/delete)`

|  Deletes a RagDataSchema.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/get)`

|  Gets a RagDataSchema.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/list)`

|  Lists RagDataSchemas in a Location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
