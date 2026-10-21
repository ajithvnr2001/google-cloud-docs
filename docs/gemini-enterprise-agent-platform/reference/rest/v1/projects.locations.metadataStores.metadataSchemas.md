---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas
title: REST Resource: projects.locations.metadataStores.metadataSchemas \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:07:05.564962+00:00
---

# REST Resource: projects.locations.metadataStores.metadataSchemas  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.metadataStores.metadataSchemas Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: MetadataSchema

Instance of a general MetadataSchema.

Fields  
  
`name` `string` Output only. The resource name of the MetadataSchema. | `schemaVersion` `string` The version of the MetadataSchema. The version's format must match the following regular expression: `^[0-9]+[.][0-9]+[.][0-9]+$`, which would allow to order/compare different versions. Example: 1.0.0, 1.0.1, etc. | `schema` `string` Required. The raw YAML string representation of the MetadataSchema. The combination of [MetadataSchema.version] and the schema name given by `title` in [MetadataSchema.schema] must be unique within a MetadataStore.The schema is defined as an OpenAPI 3.0.2 [MetadataSchema Object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#schemaObject) | `schemaType` `enum (`[MetadataSchemaType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas#MetadataSchemaType)`)` The type of the MetadataSchema. This is a property that identifies which metadata types will use the MetadataSchema. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this MetadataSchema was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `description` `string` description of the metadata Schema | JSON representation  
---  
      
    
    {
      "name": string,
      "schemaVersion": string,
      "schema": string,
      "schemaType": enum ([MetadataSchemaType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas#MetadataSchemaType)),
      "createTime": string,
      "description": string
    }  
  
## MetadataSchemaType

Describes the type of the MetadataSchema.

Enums  
---  
`METADATA_SCHEMA_TYPE_UNSPECIFIED` | Unspecified type for the MetadataSchema.  
`ARTIFACT_TYPE` | A type indicating that the MetadataSchema will be used by Artifacts.  
`EXECUTION_TYPE` | A typee indicating that the MetadataSchema will be used by Executions.  
`CONTEXT_TYPE` | A state indicating that the MetadataSchema will be used by Contexts.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas/create)`

|  Creates a MetadataSchema.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas/get)`

|  Retrieves a specific MetadataSchema.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas/list)`

|  Lists MetadataSchemas.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
