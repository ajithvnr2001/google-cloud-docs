---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/update/
title: Method: organizations.environments.resourcefiles.update \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:08.769176+00:00
---

# Method: organizations.environments.resourcefiles.update  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.resourcefiles.update Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates a resource file.

Specify the `Content-Type` as `application/octet-stream` or `multipart/form-data`.

For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files).

### HTTP request

`PUT https://apigee.googleapis.com/v1/{parent=organizations/*/environments/*}/resourcefiles/{type}/{name}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the environment in the following format: `organizations/{org}/environments/{env}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.resourcefiles.update`

  
`type` |  `string` Required. Resource file type. Valid types include `java`, `js`, `jsc`, `properties`, `py`, `wsdl`, `xsd`, or `xsl`. For more information, see [Resource types](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#resourcetypes).  
`name` |  `string` Required. ID of the resource file to update. Must match the regular expression: [a-zA-Z0-9:/\\!@#$%^&{}[]()+-=,.~'` ]{1,255}  
  
### Request body

The request body contains an instance of `[HttpBody](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases#HttpBody)`.

### Response body

If successful, the response body contains an instance of `[ResourceFile](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ResourceFiles#ResourceFile)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
