---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats/list/
title: Method: projects.groupStats.list \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:39.508186+00:00
---

# Method: projects.groupStats.list  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  Method: projects.groupStats.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists the specified groups.

### HTTP request

Choose an endpoint:

globalusafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://clouderrorreporting.googleapis.com/v1beta1/{projectName=projects/*}/groupStats`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectName` |  `string` Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectNumber}`, where `{projectID}` and `{projectNumber}` can be found in the [Google Cloud console](https://support.google.com/cloud/answer/6158840). It may also include a location, such as `projects/{projectID}/locations/{location}` where `{location}` is a cloud region.Examples: `projects/my-project-123`, `projects/5551234`, `projects/my-project-123/locations/us-central1`, `projects/5551234/locations/us-central1`.For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified. Use `-` as a wildcard to request group stats from all regions.  
  
### Query parameters

Parameters  
---  
`groupId[]` |  `string` Optional. List all `[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#ErrorGroupStats)` with these IDs. The `groupId` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).  
`serviceFilter` |  `object (`[ServiceContextFilter](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContextFilter)`)` Optional. List only `[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#ErrorGroupStats)` which belong to a service context that matches the filter. Data for all service contexts is returned if this field is not specified.  
`timeRange` |  `object (`[QueryTimeRange](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/QueryTimeRange)`)` Optional. List data for the given time range. If not set, a default time range is used. The field `[timeRangeBegin](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#FIELDS.time_range_begin)` in the response will specify the beginning of this time range. Only `[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#ErrorGroupStats)` with a non-zero count in the given time range are returned, unless the request contains an explicit `[groupId](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats/list#body.QUERY_PARAMETERS.group_id)` list. If a `[groupId](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats/list#body.QUERY_PARAMETERS.group_id)` list is given, also `[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#ErrorGroupStats)` with zero occurrences are returned.  
`timedCountDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The preferred duration for a single returned `[TimedCount](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#TimedCount)`. If not set, no timed counts are returned.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`alignment` |  `enum (`[TimedCountAlignment](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/TimedCountAlignment)`)` Optional. The alignment of the timed counts to be returned. Default is `ALIGNMENT_EQUAL_AT_END`.  
`alignmentTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Time where the timed counts shall be aligned if rounded alignment is chosen. Default is 00:00 UTC.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`order` |  `enum (`[ErrorGroupOrder](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorGroupOrder)`)` Optional. The sort order in which the results are returned. Default is `COUNT_DESC`.  
`pageSize` |  `integer` Optional. The maximum number of results to return per response. Default is 20.  
`pageToken` |  `string` Optional. A `[nextPageToken](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#FIELDS.next_page_token)` provided by a previous response. To view additional results, pass this token along with the identical query parameters as the first request.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListGroupStatsResponse](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/stackdriver-integration`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
