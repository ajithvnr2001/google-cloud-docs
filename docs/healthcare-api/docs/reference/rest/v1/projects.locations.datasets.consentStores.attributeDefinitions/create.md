---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.attributeDefinitions/create/
title: Method: attributeDefinitions.create \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:02.588572+00:00
---

# Method: attributeDefinitions.create  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.attributeDefinitions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: attributeDefinitions.create Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.consentStores.attributeDefinitions.create

Creates a new `[Attribute definition](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.attributeDefinitions#AttributeDefinition)` in the parent `[consent store](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore)`.

### HTTP request

`POST https://healthcare.googleapis.com/v1/{parent=projects/*/locations/*/datasets/*/consentStores/*}/attributeDefinitions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the consent store that this Attribute definition belongs to. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.attributeDefinitions.create`

  
  
### Query parameters

Parameters  
---  
`attributeDefinitionId` |  `string` Required. The ID of the Attribute definition to create. The string must match the following regex: `[_a-zA-Z][_a-zA-Z0-9]{0,255}` and must not be a reserved keyword within the Common Expression Language as listed on <https://github.com/google/cel-spec/blob/master/doc/langdef.md>.  
  
### Request body

The request body contains an instance of `[AttributeDefinition](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.attributeDefinitions#AttributeDefinition)`.

### Response body

If successful, the response body contains a newly created instance of `[AttributeDefinition](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.attributeDefinitions#AttributeDefinition)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
