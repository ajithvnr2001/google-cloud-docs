---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata
title: REST Resource: projects.locations.ragCorpora.ragFiles.ragMetadata \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:15:06.967973+00:00
---

# REST Resource: projects.locations.ragCorpora.ragFiles.ragMetadata  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.ragCorpora.ragFiles.ragMetadata Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: RagMetadata

metadata for RagFile provided by users.

Fields  
  
`name` `string` Identifier. Resource name of the RagMetadata. Format: `projects/{project}/locations/{location}/ragCorpora/{ragCorpus}/ragFiles/{ragFile}/ragMetadata/{ragMetadata}` | `userSpecifiedMetadata` `object (`[UserSpecifiedMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata#UserSpecifiedMetadata)`)` user provided metadata. | JSON representation  
---  
      
    
    {
      "name": string,
      "userSpecifiedMetadata": {
        object ([UserSpecifiedMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata#UserSpecifiedMetadata))
      }
    }  
  
## UserSpecifiedMetadata

metadata provided by users.

Fields  
  
`key` `string` Required. Key of the metadata. The key must be set with type by CreateRagDataSchema. | `value` `object (`[MetadataValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata#MetadataValue)`)` value of the metadata. The value must be able to convert to the type according to the data schema. | JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([MetadataValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata#MetadataValue))
      }
    }  
  
## MetadataValue

value of metadata, including all types available in data schema.

Fields  
  
`value` `Union type`  
  
The value of the metadata. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`intValue` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` value of int type metadata. | `floatValue` `number` value of float type metadata. | `strValue` `string` value of string type metadata. | `datetimeValue` `string` value of date time type metadata. | `boolValue` `boolean` value of boolean type metadata. | `listValue` `object (`[MetadataList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata#MetadataList)`)` value of list type metadata. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // value
      "intValue": string,
      "floatValue": number,
      "strValue": string,
      "datetimeValue": string,
      "boolValue": boolean,
      "listValue": {
        object ([MetadataList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata#MetadataList))
      }
      // Union type
    }  
  
## MetadataList

List representation in metadata.

Fields  
  
`values[]` `object (`[MetadataValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata#MetadataValue)`)` The values of `LIST` data type metadata. | JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([MetadataValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata#MetadataValue))
        }
      ]
    }  
  
## Methods  
  
---  
  
### `[batchCreate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata/batchCreate)`

|  Batch Create one or more RagMetadatas  
  
### `[batchDelete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata/batchDelete)`

|  Batch Deletes one or more RagMetadata.  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata/create)`

|  Creates a RagMetadata.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata/delete)`

|  Deletes a RagMetadata.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata/get)`

|  Gets a RagMetadata.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata/list)`

|  Lists RagMetadata in a RagFile.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles.ragMetadata/patch)`

|  Updates a RagMetadata.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
