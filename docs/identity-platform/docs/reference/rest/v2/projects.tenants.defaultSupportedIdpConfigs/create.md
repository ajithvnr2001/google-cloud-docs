---
url: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants.defaultSupportedIdpConfigs/create/
title: Method: projects.tenants.defaultSupportedIdpConfigs.create \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:06.331795+00:00
---

# Method: projects.tenants.defaultSupportedIdpConfigs.create  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants.defaultSupportedIdpConfigs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback 

#  Method: projects.tenants.defaultSupportedIdpConfigs.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Create a default supported Idp configuration for an Identity Toolkit project.

### HTTP request

`POST https://identitytoolkit.googleapis.com/v2/{parent=projects/*/tenants/*}/defaultSupportedIdpConfigs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The parent resource name where the config to be created, for example: "projects/my-awesome-project" Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `firebaseauth.configs.update`

  
  
### Query parameters

Parameters  
---  
`idpId` |  `string` The id of the Idp to create a config for. Call ListDefaultSupportedIdps for list of all default supported Idps.  
  
### Request body

The request body contains an instance of `[DefaultSupportedIdpConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.defaultSupportedIdpConfigs#DefaultSupportedIdpConfig)`.

### Response body

If successful, the response body contains a newly created instance of `[DefaultSupportedIdpConfig](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.defaultSupportedIdpConfigs#DefaultSupportedIdpConfig)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/identitytoolkit`
  * ` https://www.googleapis.com/auth/firebase`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
