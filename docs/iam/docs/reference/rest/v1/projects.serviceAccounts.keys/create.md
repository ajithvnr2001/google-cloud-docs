---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/create/
title: Method: projects.serviceAccounts.keys.create \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:09.088357+00:00
---

# Method: projects.serviceAccounts.keys.create  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.serviceAccounts.keys.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Creates a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.

### HTTP request

`POST https://iam.googleapis.com/v1/{name=projects/*/serviceAccounts/*}/keys`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the service account.Use one of the following formats:

  * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/{PROJECT_ID}/serviceAccounts/{UNIQUE_ID}`

As an alternative, you can use the `-` wildcard character instead of the project ID:

  * `projects/-/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/-/serviceAccounts/{UNIQUE_ID}`

When possible, avoid using the `-` wildcard character, because it can cause response messages to contain misleading error codes. For example, if you try to access the service account `projects/-/serviceAccounts/fake@example.com`, which does not exist, the response contains an HTTP `403 Forbidden` error instead of a `404 Not Found` error. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `iam.serviceAccountKeys.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "privateKeyType": enum ([ServiceAccountPrivateKeyType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountPrivateKeyType)),
      "keyAlgorithm": enum ([ServiceAccountKeyAlgorithm](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm))
    }  
  
Fields  
---  
`privateKeyType` |  `enum (`[ServiceAccountPrivateKeyType](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountPrivateKeyType)`)` The output format of the private key. The default value is `TYPE_GOOGLE_CREDENTIALS_FILE`, which is the Google Credentials File format.  
`keyAlgorithm` |  `enum (`[ServiceAccountKeyAlgorithm](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)`)` Which type of key and algorithm to use for the key. The default is currently a 2K RSA key. However this may change in the future.  
  
### Response body

If successful, the response body contains a newly created instance of `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
