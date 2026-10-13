---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/updateApiProxyRevision/
title: Method: organizations.apis.revisions.updateApiProxyRevision \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:25.413454+00:00
---

# Method: organizations.apis.revisions.updateApiProxyRevision  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/updateApiProxyRevision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.apis.revisions.updateApiProxyRevision Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates an existing API proxy revision by uploading the API proxy configuration bundle as a zip file from your local machine.

You can update only API proxy revisions that have never been deployed. After deployment, an API proxy revision becomes immutable, even if it is undeployed.

Set the `Content-Type` header to either `multipart/form-data` or `application/octet-stream`.

### HTTP request

`POST https://apigee.googleapis.com/v1/{name=organizations/*/apis/*/revisions/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. API proxy revision to update in the following format: `organizations/{org}/apis/{api}/revisions/{rev}`If the API Proxy resource has the `space` attribute set, IAM permissions are checked against the Space resource path. To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.proxyrevisions.update`

  
  
### Query parameters

Parameters  
---  
`validate` |  `boolean` Ignored. All uploads are validated regardless of the value of this field. Maintained for compatibility with Apigee Edge API.  
  
### Request body

The request body contains an instance of `[HttpBody](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases#HttpBody)`.

### Response body

If successful, the response body contains an instance of `[ApiProxyRevision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions#ApiProxyRevision)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
