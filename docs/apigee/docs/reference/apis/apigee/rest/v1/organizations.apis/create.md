---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/create/
title: Method: organizations.apis.create \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:20.876333+00:00
---

# Method: organizations.apis.create  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.apis.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates an API proxy. The API proxy created will not be accessible at runtime until it is deployed to an environment.

Create a new API proxy by setting the `name` query parameter to the name of the API proxy.

Import an API proxy configuration bundle stored in zip format on your local machine to your organization by doing the following:

  * Set the `name` query parameter to the name of the API proxy.
  * Set the `action` query parameter to `import`.
  * Set the `Content-Type` header to `multipart/form-data`.
  * Pass as a file the name of API proxy configuration bundle stored in zip format on your local machine using the `file` form field.



**Note** : To validate the API proxy configuration bundle only without importing it, set the `action` query parameter to `validate`.

When importing an API proxy configuration bundle, if the API proxy does not exist, it will be created. If the API proxy exists, then a new revision is created. Invalid API proxy configurations are rejected, and a list of validation errors is returned to the client.

### HTTP request

`POST https://apigee.googleapis.com/v1/{parent=organizations/*}/apis`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the organization in the following format: `organizations/{org}`If the API Proxy resource has the `space` attribute set, IAM permissions are checked against the Space resource path. To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.proxies.create`

  
  
### Query parameters

Parameters  
---  
`name` |  `string` Name of the API proxy. Restrict the characters used to: A-Za-z0-9._-  
`action` |  `string` Action to perform when importing an API proxy configuration bundle. Set this parameter to one of the following values:

  * `import` to import the API proxy configuration bundle.
  * `validate` to validate the API proxy configuration bundle without importing it.

  
`validate` |  `boolean` Ignored. All uploads are validated regardless of the value of this field. Maintained for compatibility with Apigee Edge API.  
`space` |  `string` Optional. The ID of the space associated with this proxy. Any IAM policies applied to the space will affect access to this proxy. Note that this field is only respected when creating a new proxy. It has no effect when creating a new revision for an existing proxy.  
  
### Request body

The request body contains an instance of `[HttpBody](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases#HttpBody)`.

### Response body

If successful, the response body contains a newly created instance of `[ApiProxyRevision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions#ApiProxyRevision)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
