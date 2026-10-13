---
url: https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deploymentGroups/patch/
title: Method: projects.locations.deploymentGroups.patch \u00a0|\u00a0 Infrastructure\u00a0Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:48.829813+00:00
---

# Method: projects.locations.deploymentGroups.patch  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deploymentGroups/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager)
  * [ Reference ](https://docs.cloud.google.com/infrastructure-manager/docs/apis)



Send feedback 

#  Method: projects.locations.deploymentGroups.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Updates a `[DeploymentGroup](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deploymentGroups#DeploymentGroup)`

### HTTP request

`PATCH https://config.googleapis.com/v1/{deploymentGroup.name=projects/*/locations/*/deploymentGroups/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`deploymentGroup.name` |  `string` Identifier. The name of the deployment group. Format: 'projects/{projectId}/locations/{location}/deploymentGroups/{deploymentGroup}'. It takes the form `projects/{project}/locations/{location}/deploymentGroups/{deploymentgroup}`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Field mask used to specify the fields to be overwritten in the Deployment Group resource by the update.The fields specified in the updateMask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[DeploymentGroup](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deploymentGroups#DeploymentGroup)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `config.googleapis.com/config.deploymentgroups.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-08 UTC."],[],[]] 
