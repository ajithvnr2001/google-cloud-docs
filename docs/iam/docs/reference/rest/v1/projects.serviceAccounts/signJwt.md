---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/signJwt/
title: Method: projects.serviceAccounts.signJwt \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:08.122494+00:00
---

# Method: projects.serviceAccounts.signJwt  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/signJwt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.serviceAccounts.signJwt Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



This method is deprecated. Use the [signJwt](https://cloud.google.com/iam/help/rest-credentials/v1/projects.serviceAccounts/signJwt) method in the IAM Service Account Credentials API instead. If you currently use this method, see the [migration guide](https://cloud.google.com/iam/help/credentials/migrate-api) for instructions.

Signs a JSON Web Token (JWT) using the system-managed private key for a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.

### HTTP request

`POST https://iam.googleapis.com/v1/{name=projects/*/serviceAccounts/*}:signJwt`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name  
**(deprecated)**` |  `string` Required. Deprecated. [Migrate to Service Account Credentials API](https://cloud.google.com/iam/help/credentials/migrate-api).The resource name of the service account.Use one of the following formats:

  * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/{PROJECT_ID}/serviceAccounts/{UNIQUE_ID}`

As an alternative, you can use the `-` wildcard character instead of the project ID:

  * `projects/-/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/-/serviceAccounts/{UNIQUE_ID}`

When possible, avoid using the `-` wildcard character, because it can cause response messages to contain misleading error codes. For example, if you try to access the service account `projects/-/serviceAccounts/fake@example.com`, which does not exist, the response contains an HTTP `403 Forbidden` error instead of a `404 Not Found` error. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `iam.serviceAccounts.signJwt`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "payload": string
    }  
  
Fields  
---  
`payload  
**(deprecated)**` |  `string` Required. Deprecated. [Migrate to Service Account Credentials API](https://cloud.google.com/iam/help/credentials/migrate-api).The JWT payload to sign. Must be a serialized JSON object that contains a JWT Claims Set. For example: `{"sub": "user@example.com", "iat": 313435}`If the JWT Claims Set contains an expiration time (`exp`) claim, it must be an integer timestamp that is not in the past and no more than 12 hours in the future.If the JWT Claims Set does not contain an expiration time (`exp`) claim, this claim is added automatically, with a timestamp that is 1 hour in the future.  
  
### Response body

Deprecated. [Migrate to Service Account Credentials API](https://cloud.google.com/iam/help/credentials/migrate-api).

The service account sign JWT response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "keyId": string,
      "signedJwt": string
    }  
  
Fields  
---  
`keyId  
**(deprecated)**` |  `string` This item is deprecated!Deprecated. [Migrate to Service Account Credentials API](https://cloud.google.com/iam/help/credentials/migrate-api).The id of the key used to sign the JWT.  
`signedJwt  
**(deprecated)**` |  `string` This item is deprecated!Deprecated. [Migrate to Service Account Credentials API](https://cloud.google.com/iam/help/credentials/migrate-api).The signed JWT.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
