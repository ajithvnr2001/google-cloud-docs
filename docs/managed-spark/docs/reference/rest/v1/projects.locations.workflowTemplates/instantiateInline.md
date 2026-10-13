---
url: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/instantiateInline/
title: Method: projects.locations.workflowTemplates.instantiateInline \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:44.420703+00:00
---

# Method: projects.locations.workflowTemplates.instantiateInline  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/instantiateInline/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-spark/docs/reference)



Send feedback 

#  Method: projects.locations.workflowTemplates.instantiateInline Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Instantiates a template and begins execution.

This method is equivalent to executing the sequence `[workflowTemplates.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/create#google.cloud.dataproc.v1.WorkflowTemplateService.CreateWorkflowTemplate)`, `[workflowTemplates.instantiate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/instantiate#google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateWorkflowTemplate)`, `[workflowTemplates.delete](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/delete#google.cloud.dataproc.v1.WorkflowTemplateService.DeleteWorkflowTemplate)`.

The returned Operation can be used to track execution of workflow by polling `[operations.get](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.operations/get#google.longrunning.Operations.GetOperation)`. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via `[operations.cancel](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.operations/cancel#google.longrunning.Operations.CancelOperation)`. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The `[Operation.metadata](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.operations#Operation.FIELDS.metadata)` will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, `[Operation.response](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.operations#Operation.FIELDS.response)` will be `[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`.

### HTTP request

`POST https://dataproc.googleapis.com/v1/{parent=projects/*/locations/*}/workflowTemplates:instantiateInline`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>.

  * For `projects.regions.workflowTemplates,instantiateinline`, the resource name of the region has the following format: `projects/{projectId}/regions/{region}`
  * For `projects.locations.workflowTemplates.instantiateinline`, the resource name of the location has the following format: `projects/{projectId}/locations/{location}`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dataproc.workflowTemplates.instantiateInline`

  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` Optional. A tag that prevents multiple concurrent workflow instances with the same tag from running. This mitigates risk of concurrent instances started due to retries.It is recommended to always set this value to a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier).The tag must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters.  
  
### Request body

The request body contains an instance of `[WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#WorkflowTemplate)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dataproc`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
