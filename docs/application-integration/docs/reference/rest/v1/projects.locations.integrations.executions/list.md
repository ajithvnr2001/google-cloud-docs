---
url: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions/list/
title: Method: projects.locations.integrations.executions.list \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:34.898001+00:00
---

# Method: projects.locations.integrations.executions.list  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback 

#  Method: projects.locations.integrations.executions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI.

### HTTP request

`GET https://integrations.googleapis.com/v1/{parent=projects/*/locations/*/integrations/*}/executions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name of the integration execution.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. Standard filter field, we support filtering on following fields: workflowName: the name of the integration. CreateTimestamp: the execution created time. eventExecutionState: the state of the executions. executionId: the id of the execution. triggerId: the id of the trigger. parameterType: the type of the parameters involved in the execution.All fields support for EQUALS, in additional: CreateTimestamp support for LESS_THAN, GREATER_THAN ParameterType support for HASFor example: "parameterType" HAS "string"Also supports operators like AND, OR, NOT For example, triggerId="id1" AND workflowName="testWorkflow"  
`pageSize` |  `integer` Optional. The size of entries in the response.  
`pageToken` |  `string` Optional. The token returned in the previous response.  
`orderBy` |  `string` Optional. The results would be returned in order you specified here. Currently supporting "createTime".  
`readMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. View mask for the response data. If set, only the field specified will be returned as part of the result. If not set, all fields in Execution will be filled and returned. Supported fields: triggerId executionMethod createTime updateTime executionDetails executionDetails.state executionDetails.execution_snapshots executionDetails.attempt_stats executionDetails.event_execution_snapshots_size requestParameters cloudLoggingDetails snapshotNumber replayInfoThis is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`truncateParams  
**(deprecated)**` |  `boolean` Optional. If true, the service will truncate the params to only keep the first 1000 characters of string params and empty the executions in order to make response smaller. Only works for UI and when the params fields are not filtered out.  
`snapshotMetadataWithoutParams` |  `boolean` Optional. If true, the service will provide execution info with snapshot metadata only i.e. without event parameters.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListExecutionsResponse](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ListExecutionsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `integrations.executions.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-22 UTC."],[],[]] 
