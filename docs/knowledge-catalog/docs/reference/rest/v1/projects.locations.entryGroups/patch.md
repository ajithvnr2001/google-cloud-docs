---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/patch/
title: Method: projects.locations.entryGroups.patch \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:22.794295+00:00
---

# Method: projects.locations.entryGroups.patch  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/patch/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  Method: projects.locations.entryGroups.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Updates an EntryGroup.

### HTTP request

`PATCH https://dataplex.googleapis.com/v1/{entryGroup.name=projects/*/locations/*/entryGroups/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`entryGroup.name` |  `string` Output only. The relative resource name of the EntryGroup, in the format projects/{project_id_or_number}/locations/{locationId}/entryGroups/{entryGroupId}.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Mask of fields to update.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`validateOnly` |  `boolean` Optional. The service validates the request, without performing any mutations. The default is false.  
  
### Request body

The request body contains an instance of `[EntryGroup](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups#EntryGroup)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/organizations.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dataplex.read-write`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `dataplex.entryGroups.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
