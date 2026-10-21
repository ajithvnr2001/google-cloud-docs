---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1
title: Package google.monitoring.metricsscope.v1 \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:21.742159+00:00
---

# Package google.monitoring.metricsscope.v1  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Package google.monitoring.metricsscope.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[MetricsScopes](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MetricsScopes)` (interface)
  * `[CreateMonitoredProjectRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.CreateMonitoredProjectRequest)` (message)
  * `[DeleteMonitoredProjectRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.DeleteMonitoredProjectRequest)` (message)
  * `[GetMetricsScopeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.GetMetricsScopeRequest)` (message)
  * `[ListMetricsScopesByMonitoredProjectRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.ListMetricsScopesByMonitoredProjectRequest)` (message)
  * `[ListMetricsScopesByMonitoredProjectResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.ListMetricsScopesByMonitoredProjectResponse)` (message)
  * `[MetricsScope](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MetricsScope)` (message)
  * `[MonitoredProject](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MonitoredProject)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.OperationMetadata)` (message)
  * `[OperationMetadata.State](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.OperationMetadata.State)` (enum)



## MetricsScopes

Manages Cloud Monitoring Metrics Scopes, and the monitoring of Google Cloud projects and AWS accounts.

CreateMonitoredProject  
---  
` rpc CreateMonitoredProject(`[CreateMonitoredProjectRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.CreateMonitoredProjectRequest)`) returns (`[Operation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.longrunning#google.longrunning.Operation)`) ` Adds a `MonitoredProject` with the given project ID to the specified `Metrics Scope`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `monitoring.metricsScopes.link`

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `monitoring.metricsScopes.link`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteMonitoredProject  
---  
` rpc DeleteMonitoredProject(`[DeleteMonitoredProjectRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.DeleteMonitoredProjectRequest)`) returns (`[Operation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a `MonitoredProject` from the specified `Metrics Scope`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetMetricsScope  
---  
` rpc GetMetricsScope(`[GetMetricsScopeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.GetMetricsScopeRequest)`) returns (`[MetricsScope](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MetricsScope)`) ` Returns a specific `Metrics Scope`, including the list of projects monitored by the specified `Metrics Scope`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListMetricsScopesByMonitoredProject  
---  
` rpc ListMetricsScopesByMonitoredProject(`[ListMetricsScopesByMonitoredProjectRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.ListMetricsScopesByMonitoredProjectRequest)`) returns (`[ListMetricsScopesByMonitoredProjectResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.ListMetricsScopesByMonitoredProjectResponse)`) ` Returns a list of every `Metrics Scope` that a specific `MonitoredProject` has been added to. The metrics scope representing the specified monitored project will always be the first entry in the response.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## CreateMonitoredProjectRequest

Request for the `CreateMonitoredProject` method.

Fields  
---  
`parent` |  `string` Required. The resource name of the existing `Metrics Scope` that will monitor this project. Example: `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}`  
`monitored_project` |  `[MonitoredProject](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MonitoredProject)` Required. The initial `MonitoredProject` configuration. Specify only the `monitored_project.name` field. All other fields are ignored. The `monitored_project.name` must be in the format: `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}`  
  
## DeleteMonitoredProjectRequest

Request for the `DeleteMonitoredProject` method.

Fields  
---  
`name` |  `string` Required. The resource name of the `MonitoredProject`. Example: `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}`Authorization requires the following [Google IAM](https://cloud.google.com/iam) permissions on both the `Metrics Scope` and on the `MonitoredProject`: `monitoring.metricsScopes.link`  
  
## GetMetricsScopeRequest

Request for the `GetMetricsScope` method.

Fields  
---  
`name` |  `string` Required. The resource name of the `Metrics Scope`. Example: `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `resourcemanager.projects.get`

  
  
## ListMetricsScopesByMonitoredProjectRequest

Request for the `ListMetricsScopesByMonitoredProject` method.

Fields  
---  
`monitored_resource_container` |  `string` Required. The resource name of the `Monitored Project` being requested. Example: `projects/{MONITORED_PROJECT_ID_OR_NUMBER}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `monitoredResourceContainer`:

  * `resourcemanager.projects.get`

  
  
## ListMetricsScopesByMonitoredProjectResponse

Response for the `ListMetricsScopesByMonitoredProject` method.

Fields  
---  
`metrics_scopes[]` |  `[MetricsScope](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MetricsScope)` A set of all metrics scopes that the specified monitored project has been added to.  
  
## MetricsScope

Represents a [Metrics Scope](https://cloud.google.com/monitoring/settings#concept-scope) in Cloud Monitoring, which specifies one or more Google projects and zero or more AWS accounts to monitor together.

Fields  
---  
`name` |  `string` Immutable. The resource name of the Monitoring Metrics Scope. On input, the resource name can be specified with the scoping project ID or number. On output, the resource name is specified with the scoping project number. Example: `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}`  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time when this `Metrics Scope` was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time when this `Metrics Scope` record was last updated.  
`monitored_projects[]` |  `[MonitoredProject](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MonitoredProject)` Output only. The list of projects monitored by this `Metrics Scope`.  
  
## MonitoredProject

A [project being monitored](https://cloud.google.com/monitoring/settings/multiple-projects#create-multi) by a `Metrics Scope`.

Fields  
---  
`name` |  `string` Immutable. The resource name of the `MonitoredProject`. On input, the resource name includes the scoping project ID and monitored project ID. On output, it contains the equivalent project numbers. Example: `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}`  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time when this `MonitoredProject` was created.  
`is_tombstoned` |  `bool` Output only. Set if the project has been tombstoned by the user.  
  
## OperationMetadata

Contains metadata for longrunning operation for the edit Metrics Scope endpoints.

Fields  
---  
`state` |  `[State](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.OperationMetadata.State)` Current state of the batch operation.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time when the batch request was received.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time when the operation result was last updated.  
  
## State

Batch operation states.

Enums  
---  
`STATE_UNSPECIFIED` | Invalid.  
`CREATED` | Request has been received.  
`RUNNING` | Request is actively being processed.  
`DONE` | The batch processing is done.  
`CANCELLED` | The batch processing was cancelled.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
