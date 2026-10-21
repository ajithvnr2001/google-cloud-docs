---
url: https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta
title: Package google.cloud.appoptimize.v1beta \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:41:29.223077+00:00
---

# Package google.cloud.appoptimize.v1beta  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  Package google.cloud.appoptimize.v1beta Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AppOptimize](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.AppOptimize)` (interface)
  * `[Column](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.Column)` (message)
  * `[CreateReportRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.CreateReportRequest)` (message)
  * `[DeleteReportRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.DeleteReportRequest)` (message)
  * `[GetReportRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.GetReportRequest)` (message)
  * `[ListReportsRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.ListReportsRequest)` (message)
  * `[ListReportsResponse](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.ListReportsResponse)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.OperationMetadata)` (message)
  * `[ReadReportRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.ReadReportRequest)` (message)
  * `[ReadReportResponse](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.ReadReportResponse)` (message)
  * `[Report](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.Report)` (message)
  * `[Scope](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.Scope)` (message)



## AppOptimize

Service for managing and querying optimization reports.

CreateReport  
---  
` rpc CreateReport(`[CreateReportRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.CreateReportRequest)`) returns (`[Operation](https://docs.cloud.google.com/app-optimize/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new report.This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/appoptimize`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `appoptimize.reports.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteReport  
---  
` rpc DeleteReport(`[DeleteReportRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.DeleteReportRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified report.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/appoptimize`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `appoptimize.reports.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetReport  
---  
` rpc GetReport(`[GetReportRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.GetReportRequest)`) returns (`[Report](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.Report)`) ` Retrieves the details of a report configuration.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/appoptimize`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `appoptimize.reports.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListReports  
---  
` rpc ListReports(`[ListReportsRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.ListReportsRequest)`) returns (`[ListReportsResponse](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.ListReportsResponse)`) ` Lists reports within a given project.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/appoptimize`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `appoptimize.reports.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ReadReport  
---  
` rpc ReadReport(`[ReadReportRequest](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.ReadReportRequest)`) returns (`[ReadReportResponse](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.ReadReportResponse)`) ` Reads data within a specified report.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/appoptimize`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `appoptimize.reports.getData`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## Column

Describes a single column within `Columns`.

Fields  
---  
`name` |  `string` The name of the column.This field:

  * Contains only letters (a-z, A-Z), numbers (0-9), or underscores (_);
  * Start with a letter or underscore; and
  * Has a maximum length is 128 characters.

  
`type` |  `string` The data type of the column.Supported values include:

  * `STRING`
  * `INT64`
  * `FLOAT64`
  * `BOOLEAN`
  * `TIMESTAMP`
  * `RECORD`

`RECORD` indicates that the field contains a nested schema, described in the `columns` property of this `Column`.  
`mode` |  `string` The mode of the column, indicating if it is nullable, required, or repeated.Possible values:

  * `NULLABLE`: The column allows NULL values.
  * `REQUIRED`: The column does not allow NULL values.
  * `REPEATED`: The column contains an array of values.

  
`columns[]` |  `[Column](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.Column)` If the `type` of this column is `RECORD`, this sub-field describes the nested structure.  
  
## CreateReportRequest

Request message for the `CreateReport` method.

Fields  
---  
`parent` |  `string` Required. The parent Google Cloud project that will own the report.This value does not define the scope of the report data. See `Report.scope` for setting the data scope.Format: `projects/{project}/locations/{location}`.  
`report_id` |  `string` Required. The ID to use for this report. This ID must be unique within the parent project and should comply with RFC 1034 restrictions (letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum).  
`report` |  `[Report](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.Report)` Required. The report resource to create.  
  
## DeleteReportRequest

Request message for the `DeleteReport` method.

Fields  
---  
`name` |  `string` Required. The name of the report to delete.Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`allow_missing` |  `bool` Optional. If set to true, and the report is not found, the request will succeed but no action will be taken on the server.  
  
## GetReportRequest

Request message for the `GetReport` method.

Fields  
---  
`name` |  `string` Required. The name of the report to retrieve.Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
  
## ListReportsRequest

Request message for the `ListReports` method.

Fields  
---  
`parent` |  `string` Required. The parent project whose reports are to be listed.Format: `projects/{project}/locations/{location}`.  
`page_size` |  `int32` Optional. The maximum number of reports to return. The service may return fewer than this value. If unspecified, the server will determine the number of results to return.  
`page_token` |  `string` Optional. A page token, received from a previous `ListReports` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListReports` must match the call that provided the page token.  
  
## ListReportsResponse

Response message for the `ListReports` method.

Fields  
---  
`reports[]` |  `[Report](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.Report)` The list of reports.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is empty, there are no subsequent pages.  
  
## OperationMetadata

This type has no fields.

Represents metadata related to the creation of a Report. This value is embedded in the Operation object returned by `CreateReport`.

## ReadReportRequest

Request message for the `ReadReport` method.

Fields  
---  
`name` |  `string` Required. The resource name of the report to query.Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`page_size` |  `int32` Optional. The maximum number of rows to return. The service may return fewer than this value. If unspecified, at most 10,000 rows will be returned per page. The maximum allowed value is 25,000; values above 25,000 are coerced to 25,000.  
`page_token` |  `string` Optional. A page token, received from a previous `ReadReport` call, to retrieve the subsequent page of results. When `page_token` is specified, `job_reference` must also be provided from the previous response, and the `statement` field must not be set.  
  
## ReadReportResponse

Response message for the `ReadReport` method.

Fields  
---  
`rows[]` |  `[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` A list of rows, where each row represents a record from the report.  
`columns[]` |  `[Column](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.Column)` The columns describing the structure of the data in the `rows` field.  
`next_page_token` |  `string` A token that can be sent as `page_token` in a subsequent `ReadReport` request to retrieve the next page of results. If this field is empty, there are no further pages.  
  
## Report

A configuration that defines the parameters for the data represented by a report.

Fields  
---  
`name` |  `string` Identifier. The name of this report.  
`dimensions[]` |  `string` Required. A list of dimensions to include in the report. Supported values:

  * `project`
  * `application`
  * `service_or_workload`
  * `resource`
  * `resource_type`
  * `location`
  * `product_display_name`
  * `sku`
  * `month`
  * `day`
  * `hour`

To aggregate results by time, specify at least one time dimension (`month`, `day`, or `hour`). All time dimensions use Pacific Time, respect Daylight Saving Time (DST), and follow these ISO 8601 formats:

  * `month`: `YYYY-MM` (e.g., `2024-01`)
  * `day`: `YYYY-MM-DD` (e.g., `2024-01-10`)
  * `hour`: `YYYY-MM-DDTHH` (e.g., `2024-01-10T00`)

If the time range filter does not align with the selected time dimension, the range is expanded to encompass the full period of the finest-grained time dimension.For example, if the filter is `2026-01-10` through `2026-01-12` and the `month` dimension is selected, the effective time range expands to include all of January (`2026-01-01` to `2026-02-01`).  
`metrics[]` |  `string` Required. A list of metrics to include in the report. Supported values:

  * `cost`
  * `resource_cost`
  * `network_cost`
  * `network_cost_standard_internet`
  * `network_cost_premium_internet`
  * `network_cost_inter_region`
  * `network_cost_inter_zone`
  * `network_cost_load_balancing_inbound`
  * `network_cost_load_balancing_outbound`
  * `network_cost_interconnect_inbound`
  * `network_cost_interconnect_outbound`
  * `cpu_mean_utilization`
  * `cpu_usage_core_seconds`
  * `cpu_allocation_core_seconds`
  * `cpu_p95_utilization`
  * `memory_mean_utilization`
  * `memory_usage_byte_seconds`
  * `memory_allocation_byte_seconds`
  * `memory_p95_utilization`

  
`scopes[]` |  `[Scope](https://docs.cloud.google.com/app-optimize/reference/rpc/google.cloud.appoptimize.v1beta#google.cloud.appoptimize.v1beta.Scope)` Optional. The resource containers for which to fetch data. Default is the project specified in the report's parent.No more than one scope is supported.  
`filter` |  `string` Optional. A Common Expression Language (CEL) expression used to filter the data for the report.Predicates may refer to any dimension. Filtering must conform to these constraints:

  * All string field predicates must use exact string matches.
  * Multiple predicates referring to the same string field must be joined using the logical OR operator ('||').
  * All other predicates must be joined using the logical AND operator (`&&`).
  * A predicate on a time dimension (e.g., `day`) specifying the start time must use a greater-than-or-equal-to comparison (`>=`).
  * A predicate on a time dimension specifying the end time must use a less-than comparison (`<`).

Examples:

  1. Filter by a specific resource type: `"resource_type == 'compute.googleapis.com/Instance'"`
  2. Filter data points that fall within a specific absolute time interval: `"hour >= timestamp('2024-01-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')"`
  3. Filter data points that fall within the past 72 hours: `"hour >= now - duration('72h')"`
  4. Combine string predicate with time interval predicate: `"(location == 'us-east1' || location == 'us-west1') && hour >= timestamp('2023-12-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')"`

If the filter omits time dimensions (`month`, `day`, `hour`), the report defaults to a 7-day range ending at the previous Pacific Time midnight, with Daylight Saving Time (DST) applied.For example, if the current Pacific Time is `2026-01-05T12:00:00`, the default range is `2025-12-29T00:00:00` to `2026-01-05T00:00:00` Pacific time.  
Union field `expiration`. Defines this report's expiration time. `expiration` can be only one of the following:  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp in UTC of when this report expires. Once the report expires, it will no longer be accessible and the report's underlying data will be deleted.  
  
## Scope

Specifies the report scope.

Fields  
---  
Union field `scope`.`scope` can be only one of the following:  
`project` |  `string` Required. A Google Cloud Platform project to fetch data from.Format: `"projects/{project}"`.  
`application` |  `string` Required. An App Hub Application to fetch data from.Format: `"projects/{project}/locations/{location}/applications/{application}"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
