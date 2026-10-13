---
url: https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deploymentGroups/delete/
title: Method: projects.locations.deploymentGroups.delete \u00a0|\u00a0 Infrastructure\u00a0Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:37.977576+00:00
---

# Method: projects.locations.deploymentGroups.delete  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deploymentGroups/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager)
  * [ Reference ](https://docs.cloud.google.com/infrastructure-manager/docs/apis)



Send feedback 

#  Method: projects.locations.deploymentGroups.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * DeploymentReferencePolicy
  * Try it!



Deletes a `[DeploymentGroup](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deploymentGroups#DeploymentGroup)`

### HTTP request

`DELETE https://config.googleapis.com/v1/{name=projects/*/locations/*/deploymentGroups/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of DeploymentGroup in the format projects/{projectId}/locations/{locationId}/deploymentGroups/{deploymentGroup} It takes the form `projects/{project}/locations/{location}/deploymentGroups/{deploymentgroup}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `config.deploymentgroups.delete`

  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
`force` |  `boolean` Optional. If set to true, any revisions for this deployment group will also be deleted. (Otherwise, the request will only work if the deployment group has no revisions.)  
`deploymentReferencePolicy` |  `enum (`[DeploymentReferencePolicy](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deploymentGroups/delete#DeploymentReferencePolicy)`)` Optional. Policy on how to handle referenced deployments when deleting the DeploymentGroup. If unspecified, the default behavior is to fail the deletion if any deployments currently referenced in the `deploymentUnits` of the DeploymentGroup or in the latest revision are not deleted.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `config.googleapis.com/config.deploymentgroups.delete`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## DeploymentReferencePolicy

Policy on how to handle referenced deployments when deleting the DeploymentGroup.

Enums  
---  
`DEPLOYMENT_REFERENCE_POLICY_UNSPECIFIED` | The default behavior. If unspecified, the system will act as if `FAIL_IF_ANY_REFERENCES_EXIST` is specified.  
`FAIL_IF_ANY_REFERENCES_EXIST` | Fail the deletion if any deployments currently referenced in the `deploymentUnits` of the DeploymentGroup or in the latest revision are not deleted.  
`FAIL_IF_METADATA_REFERENCES_EXIST` | Fail the deletion only if any deployments currently referenced in the `deploymentUnits` of the DeploymentGroup are not deleted. The deletion will proceed even if the deployments in the latest revision of the DeploymentGroup are not deleted.  
`IGNORE_DEPLOYMENT_REFERENCES` | Ignore any deployments currently referenced in the `deploymentUnits` of the DeploymentGroup or in the latest revision.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-08 UTC."],[],[]] 
