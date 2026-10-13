---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.integrations.versions/download/
title: Method: projects.locations.products.integrations.versions.download \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:18.063050+00:00
---

# Method: projects.locations.products.integrations.versions.download  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.integrations.versions/download/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Method: projects.locations.products.integrations.versions.download Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * IAM Permissions



Downloads an integration. Retrieves the `IntegrationVersion` for a given `integration_id` and returns the response as a string.

### HTTP request

`GET https://integrations.googleapis.com/v1/{name=projects/*/locations/*/products/*/integrations/*/versions/*}:download`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The version to download. Format: projects/{project}/locations/{location}/integrations/{integration}/versions/{version}  
  
### Query parameters

Parameters  
---  
`fileFormat` |  `enum (`[FileFormat](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/FileFormat)`)` File format for download request.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[DownloadIntegrationVersionResponse](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/DownloadIntegrationVersionResponse)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `integrations.apigeeIntegrationVers.get`
  * `integrations.integrationVersions.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
