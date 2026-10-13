---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/create/
title: Method: projects.locations.oauthClients.credentials.create \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:55.156217+00:00
---

# Method: projects.locations.oauthClients.credentials.create  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.oauthClients.credentials.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Creates a new `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.

### HTTP request

`POST https://iam.googleapis.com/v1/{parent=projects/*/locations/*/oauthClients/*}/credentials`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource to create the `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)` in.  
  
### Query parameters

Parameters  
---  
`oauthClientCredentialId` |  `string` Required. The ID to use for the `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`, which becomes the final component of the resource name. This value should be 4-32 characters, and may contain the characters [a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may not be specified.  
  
### Request body

The request body contains an instance of `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.

### Response body

If successful, the response body contains a newly created instance of `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
