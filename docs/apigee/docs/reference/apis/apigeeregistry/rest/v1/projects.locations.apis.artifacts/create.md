---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis.artifacts/create/
title: Method: projects.locations.apis.artifacts.create \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:42.788783+00:00
---

# Method: projects.locations.apis.artifacts.create  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis.artifacts/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Method: projects.locations.apis.artifacts.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!

**Note:** You are viewing the legacy Apigee Registry API documentation which is no longer supported. For the latest API hub functionality, it's recommended to use the [Apigee API hub APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest).

Creates a specified artifact.

### HTTP request

`POST https://apigeeregistry.googleapis.com/v1/{parent=projects/*/locations/*/apis/*}/artifacts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of artifacts. Format: `{parent}`  
  
### Query parameters

Parameters  
---  
`artifactId` |  `string` Required. The ID to use for the artifact, which will become the final component of the artifact's resource name.This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.Following AIP-162, IDs must not have the form of a UUID.  
  
### Request body

The request body contains an instance of `[Artifact](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis.artifacts#Artifact)`.

### Response body

If successful, the response body contains a newly created instance of `[Artifact](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis.artifacts#Artifact)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
