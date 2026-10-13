---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts
title: REST Resource: projects.serviceAccounts \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:05.464854+00:00
---

# REST Resource: projects.serviceAccounts  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: projects.serviceAccounts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ServiceAccount
    * JSON representation
  * Methods



## Resource: ServiceAccount

An IAM service account.

A service account is an account for an application or a virtual machine (VM) instance, not a person. You can use a service account to call Google APIs. To learn more, read the [overview of service accounts](https://cloud.google.com/iam/help/service-accounts/overview).

When you create a service account, you specify the project ID that owns the service account, as well as a name that must be unique within the project. IAM uses these values to create an email address that identifies the service account. //

JSON representation  
---  
      
    
    {
      "name": string,
      "projectId": string,
      "uniqueId": string,
      "email": string,
      "displayName": string,
      "etag": string,
      "description": string,
      "oauth2ClientId": string,
      "disabled": boolean
    }  
  
Fields  
---  
`name` |  `string` The resource name of the service account.Use one of the following formats:

  * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/{PROJECT_ID}/serviceAccounts/{UNIQUE_ID}`

As an alternative, you can use the `-` wildcard character instead of the project ID:

  * `projects/-/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/-/serviceAccounts/{UNIQUE_ID}`

When possible, avoid using the `-` wildcard character, because it can cause response messages to contain misleading error codes. For example, if you try to access the service account `projects/-/serviceAccounts/fake@example.com`, which does not exist, the response contains an HTTP `403 Forbidden` error instead of a `404 Not Found` error.  
`projectId` |  `string` Output only. The ID of the project that owns the service account.  
`uniqueId` |  `string` Output only. The unique, stable numeric ID for the service account.Each service account retains its unique ID even if you delete the service account. For example, if you delete a service account, then create a new service account with the same name, the new service account has a different unique ID than the deleted service account.  
`email` |  `string` Output only. The email address of the service account.  
`displayName` |  `string` Optional. A user-specified, human-readable name for the service account. The maximum length is 100 UTF-8 bytes.  
`etag  
**(deprecated)**` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Deprecated. Do not use.A base64-encoded string.  
`description` |  `string` Optional. A user-specified, human-readable description of the service account. The maximum length is 256 UTF-8 bytes.  
`oauth2ClientId` |  `string` Output only. The OAuth 2.0 client ID for the service account.  
`disabled` |  `boolean` Output only. Whether the service account is disabled.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/create)`

|  Creates a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/delete)`

|  Deletes a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[disable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/disable)`

|  Disables a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` immediately.  
  
### `[enable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/enable)`

|  Enables a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` that was disabled by `[DisableServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/disable#google.iam.admin.v1.IAM.DisableServiceAccount)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/get)`

|  Gets a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy)`

|  Gets the IAM policy that is attached to a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/list)`

|  Lists every `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` that belongs to a specific project.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/patch)`

|  Patches a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy)`

|  Sets the IAM policy that is attached to a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[signBlob](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/signBlob)   
**(deprecated)**`

|  Signs a blob using the system-managed private key for a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[signJwt](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/signJwt)   
**(deprecated)**`

|  Signs a JSON Web Token (JWT) using the system-managed private key for a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[testIamPermissions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/testIamPermissions)`

|  Tests whether the caller has the specified permissions on a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/undelete)`

|  Restores a deleted `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
### `[update](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/update)`

|  **Note:** We are in the process of deprecating this method.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
