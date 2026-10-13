---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/patch/
title: Method: projects.serviceAccounts.patch \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:07.606350+00:00
---

# Method: projects.serviceAccounts.patch  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.serviceAccounts.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Patches a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.

### HTTP request

`PATCH https://iam.googleapis.com/v1/{serviceAccount.name=projects/*/serviceAccounts/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`serviceAccount.name` |  `string` The resource name of the service account.Use one of the following formats:

  * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/{PROJECT_ID}/serviceAccounts/{UNIQUE_ID}`

As an alternative, you can use the `-` wildcard character instead of the project ID:

  * `projects/-/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/-/serviceAccounts/{UNIQUE_ID}`

When possible, avoid using the `-` wildcard character, because it can cause response messages to contain misleading error codes. For example, if you try to access the service account `projects/-/serviceAccounts/fake@example.com`, which does not exist, the response contains an HTTP `403 Forbidden` error instead of a `404 Not Found` error.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "serviceAccount": {
        "name": string,
        "projectId": string,
        "uniqueId": string,
        "email": string,
        "displayName": string,
        "etag": string,
        "description": string,
        "oauth2ClientId": string,
        "disabled": boolean
      },
      "updateMask": string
    }  
  
Fields  
---  
`serviceAccount.projectId` |  `string` Output only. The ID of the project that owns the service account.  
`serviceAccount.uniqueId` |  `string` Output only. The unique, stable numeric ID for the service account.Each service account retains its unique ID even if you delete the service account. For example, if you delete a service account, then create a new service account with the same name, the new service account has a different unique ID than the deleted service account.  
`serviceAccount.email` |  `string` Output only. The email address of the service account.  
`serviceAccount.displayName` |  `string` Optional. A user-specified, human-readable name for the service account. The maximum length is 100 UTF-8 bytes.  
`serviceAccount.etag  
**(deprecated)**` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Deprecated. Do not use.A base64-encoded string.  
`serviceAccount.description` |  `string` Optional. A user-specified, human-readable description of the service account. The maximum length is 256 UTF-8 bytes.  
`serviceAccount.oauth2ClientId` |  `string` Output only. The OAuth 2.0 client ID for the service account.  
`serviceAccount.disabled` |  `boolean` Output only. Whether the service account is disabled.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

If successful, the response body contains an instance of `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
