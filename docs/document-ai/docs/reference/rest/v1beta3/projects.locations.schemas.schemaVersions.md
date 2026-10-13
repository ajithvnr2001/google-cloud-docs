---
url: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.schemas.schemaVersions
title: REST Resource: projects.locations.schemas.schemaVersions \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:45.842372+00:00
---

# REST Resource: projects.locations.schemas.schemaVersions  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.schemas.schemaVersions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  REST Resource: projects.locations.schemas.schemaVersions Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: SchemaVersion

SchemaVersion is a version of the Schema which is created in SchemaGroup.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "schema": {
        object ([DocumentSchema](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/DocumentSchema))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the SchemaVersion. Format: `projects/{project}/locations/{location}/schemas/{schema}/schemaVersions/{schemaVersion}`  
`displayName` |  `string` Required. The user-defined name of the SchemaVersion.  
`labels` |  `map (key: string, value: string)` Optional. The Google Cloud labels for the SchemaVersion.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the SchemaVersion was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`schema` |  `object (`[DocumentSchema](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/DocumentSchema)`)` Required. The schema of the SchemaVersion.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.schemas.schemaVersions/create)`

|  Creates a schema version.  
  
### `[delete](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.schemas.schemaVersions/delete)`

|  Deletes a schema version.  
  
### `[generate](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.schemas.schemaVersions/generate)`

|  Generates a schema version.  
  
### `[get](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.schemas.schemaVersions/get)`

|  Gets a schema version.  
  
### `[list](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.schemas.schemaVersions/list)`

|  Lists SchemaVersions.  
  
### `[patch](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.schemas.schemaVersions/patch)`

|  Updates a schema version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
