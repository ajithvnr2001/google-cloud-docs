---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/disable/
title: Method: projects.serviceAccounts.disable \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:05.963999+00:00
---

# Method: projects.serviceAccounts.disable  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.serviceAccounts.disable Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Disables a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` immediately.

If an application uses the service account to authenticate, that application can no longer call Google APIs or access Google Cloud resources. Existing access tokens for the service account are rejected, and requests for new access tokens will fail.

To re-enable the service account, use `[serviceAccounts.enable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/enable#google.iam.admin.v1.IAM.EnableServiceAccount)`. After you re-enable the service account, its existing access tokens will be accepted, and you can request new access tokens.

To help avoid unplanned outages, we recommend that you disable the service account before you delete it. Use this method to disable the service account, then wait at least 24 hours and watch for unintended consequences. If there are no unintended consequences, you can delete the service account with `[serviceAccounts.delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/delete#google.iam.admin.v1.IAM.DeleteServiceAccount)`.

### HTTP request

`POST https://iam.googleapis.com/v1/{name=projects/*/serviceAccounts/*}:disable`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The resource name of the service account.Use one of the following formats:

  * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/{PROJECT_ID}/serviceAccounts/{UNIQUE_ID}`

As an alternative, you can use the `-` wildcard character instead of the project ID:

  * `projects/-/serviceAccounts/{EMAIL_ADDRESS}`
  * `projects/-/serviceAccounts/{UNIQUE_ID}`

When possible, avoid using the `-` wildcard character, because it can cause response messages to contain misleading error codes. For example, if you try to access the service account `projects/-/serviceAccounts/fake@example.com`, which does not exist, the response contains an HTTP `403 Forbidden` error instead of a `404 Not Found` error. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `iam.serviceAccounts.disable`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
