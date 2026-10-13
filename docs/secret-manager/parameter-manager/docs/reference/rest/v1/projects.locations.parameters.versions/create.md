---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions/create/
title: Method: projects.locations.parameters.versions.create \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:59.385523+00:00
---

# Method: projects.locations.parameters.versions.create  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions/create/

  * [ Reference ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/apis)



#  Method: projects.locations.parameters.versions.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates a new ParameterVersion in a given project, location, and parameter.

### HTTP request

Choose a location:

global us-central1 europe-west1 europe-west4 us-east4 europe-west2 europe-west3 us-east1 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 asia-northeast1 australia-southeast1 australia-southeast2 europe-west6 europe-west8 europe-west9 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 europe-west12 africa-south1 asia-southeast1 asia-southeast2 me-central1 southamerica-east1 asia-south1 europe-west10 europe-north1 europe-central2 europe-southwest1 asia-south2 asia-east1 asia-east2 asia-northeast2 asia-northeast3 northamerica-south1 southamerica-west1 europe-north2 us eu

  
`POST https://parametermanager.googleapis.com/v1/{parent=projects/*/locations/*/parameters/*}/versions`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Value for parent in the format `projects/*/locations/*/parameters/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `parametermanager.parameterVersions.create`

  
  
### Query parameters

Parameters  
---  
`parameterVersionId` |  `string` Required. Id of the ParameterVersion resource  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[ParameterVersion](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion)`.

### Response body

If successful, the response body contains a newly created instance of `[ParameterVersion](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `parametermanager.parameterVersions.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-24 UTC."],[],[]] 
