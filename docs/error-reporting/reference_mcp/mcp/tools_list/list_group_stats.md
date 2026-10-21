---
url: https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats/
title: MCP Tools Reference: clouderrorreporting.googleapis.com \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:42.059240+00:00
---

# MCP Tools Reference: clouderrorreporting.googleapis.com  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  MCP Tools Reference: clouderrorreporting.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_group_stats`

Use this tool ONLY to find and analyze recurring stack traces in your application. It aggregates similar stack traces, providing statistics like the number of occurrences and the number of affected users. DO NOT use this tool for general error searches or to view individual error logs. For queries asking to 'find errors', or 'show me errors', you MUST use list_log_entries tool. CRITICAL: Default to other tooling for generic questions about errors.

The following code sample shows how to use `curl` to call the `list_group_stats` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://clouderrorreporting.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_group_stats",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Specifies a set of `ErrorGroupStats` to return.

Next ID: 19

### ListGroupStatsRequest

JSON representation  
---  
      
    
    {
      "projectName": string,
      "groupId": [
        string
      ],
      "serviceFilter": {
        object ([ServiceContextFilter](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.ServiceContextFilter))
      },
      "timeRange": {
        object ([QueryTimeRange](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.QueryTimeRange))
      },
      "timedCountDuration": string,
      "alignment": enum ([TimedCountAlignment](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.TimedCountAlignment)),
      "alignmentTime": string,
      "order": enum ([ErrorGroupOrder](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.ErrorGroupOrder)),
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`projectName` |  `string` Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectNumber}`, where `{projectID}` and `{projectNumber}` can be found in the [Google Cloud console](https://support.google.com/cloud/answer/6158840). It may also include a location, such as `projects/{projectID}/locations/{location}` where `{location}` is a cloud region.Examples: `projects/my-project-123`, `projects/5551234`, `projects/my-project-123/locations/us-central1`, `projects/5551234/locations/us-central1`.For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified. Use `-` as a wildcard to request group stats from all regions.  
`groupId[]` |  `string` Optional. List all `[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorGroupStats)` with these IDs. The `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).  
`serviceFilter` |  `object (`[ServiceContextFilter](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.ServiceContextFilter)`)` Optional. List only `[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorGroupStats)` which belong to a service context that matches the filter. Data for all service contexts is returned if this field is not specified.  
`timeRange` |  `object (`[QueryTimeRange](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.QueryTimeRange)`)` Optional. List data for the given time range. If not set, a default time range is used. The field `time_range_begin` in the response will specify the beginning of this time range. Only `[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorGroupStats)` with a non-zero count in the given time range are returned, unless the request contains an explicit `group_id` list. If a `group_id` list is given, also `[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorGroupStats)` with zero occurrences are returned.  
`timedCountDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The preferred duration for a single returned `[TimedCount](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.TimedCount)`. If not set, no timed counts are returned.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`alignment` |  `enum (`[TimedCountAlignment](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.TimedCountAlignment)`)` Optional. The alignment of the timed counts to be returned. Default is `ALIGNMENT_EQUAL_AT_END`.  
`alignmentTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Time where the timed counts shall be aligned if rounded alignment is chosen. Default is 00:00 UTC.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`order` |  `enum (`[ErrorGroupOrder](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.ErrorGroupOrder)`)` Optional. The sort order in which the results are returned. Default is `COUNT_DESC`.  
`pageSize` |  `integer` Optional. The maximum number of results to return per response. Default is 20.  
`pageToken` |  `string` Optional. A `next_page_token` provided by a previous response. To view additional results, pass this token along with the identical query parameters as the first request.  
  
### ServiceContextFilter

JSON representation  
---  
      
    
    {
      "service": string,
      "version": string,
      "resourceType": string
    }  
  
Fields  
---  
`service` |  `string` Optional. The exact value to match against [`ServiceContext.service`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext#FIELDS.service).  
`version` |  `string` Optional. The exact value to match against [`ServiceContext.version`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext#FIELDS.version).  
`resourceType` |  `string` Optional. The exact value to match against [`ServiceContext.resource_type`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext#FIELDS.resource_type).  
  
### QueryTimeRange

JSON representation  
---  
      
    
    {
      "period": enum ([Period](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.Period))
    }  
  
Fields  
---  
`period` |  `enum (`[Period](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Input.Schema.Period)`)` Restricts the query to the specified time range.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### Period

The supported time ranges.

Enums  
---  
`PERIOD_UNSPECIFIED` | Do not use.  
`PERIOD_1_HOUR` | Retrieve data for the last hour. Recommended minimum timed count duration: 1 min.  
`PERIOD_6_HOURS` | Retrieve data for the last 6 hours. Recommended minimum timed count duration: 10 min.  
`PERIOD_1_DAY` | Retrieve data for the last day. Recommended minimum timed count duration: 1 hour.  
`PERIOD_1_WEEK` | Retrieve data for the last week. Recommended minimum timed count duration: 6 hours.  
`PERIOD_30_DAYS` | Retrieve data for the last 30 days. Recommended minimum timed count duration: 1 day.  
  
### TimedCountAlignment

Specifies how the time periods of error group counts are aligned.

Enums  
---  
`ERROR_COUNT_ALIGNMENT_UNSPECIFIED` | No alignment specified.  
`ALIGNMENT_EQUAL_ROUNDED` | The time periods shall be consecutive, have width equal to the requested duration, and be aligned at the `alignment_time` provided in the request.The `alignment_time` does not have to be inside the query period but even if it is outside, only time periods are returned which overlap with the query period.A rounded alignment will typically result in a different size of the first or the last time period.  
`ALIGNMENT_EQUAL_AT_END` | The time periods shall be consecutive, have width equal to the requested duration, and be aligned at the end of the requested time period. This can result in a different size of the first time period.  
  
### ErrorGroupOrder

A sorting order of error groups.

Enums  
---  
`GROUP_ORDER_UNSPECIFIED` | No group order specified.  
`COUNT_DESC` | Total count of errors in the given time window in descending order.  
`LAST_SEEN_DESC` | Timestamp when the group was last seen in the given time window in descending order.  
`CREATED_DESC` | Timestamp when the group was created in descending order.  
`AFFECTED_USERS_DESC` | Number of affected users in the given time window in descending order.  
  
## Output Schema

Contains a set of requested error group stats.

### ListGroupStatsResponse

JSON representation  
---  
      
    
    {
      "errorGroupStats": [
        {
          object ([ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorGroupStats))
        }
      ],
      "nextPageToken": string,
      "timeRangeBegin": string
    }  
  
Fields  
---  
`errorGroupStats[]` |  `object (`[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorGroupStats)`)` The error group stats which match the given request.  
`nextPageToken` |  `string` If non-empty, more results are available. Pass this token, along with the same query parameters as the first request, to view the next page of results.  
`timeRangeBegin` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp specifies the start time to which the request was restricted. The start time is set based on the requested time range. It may be adjusted to a later time if a project has exceeded the storage quota and older data has been deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### ErrorGroupStats

JSON representation  
---  
      
    
    {
      "group": {
        object ([ErrorGroup](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorGroup))
      },
      "count": string,
      "affectedUsersCount": string,
      "timedCounts": [
        {
          object ([TimedCount](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.TimedCount))
        }
      ],
      "firstSeenTime": string,
      "lastSeenTime": string,
      "affectedServices": [
        {
          object ([ServiceContext](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ServiceContext))
        }
      ],
      "numAffectedServices": integer,
      "representative": {
        object ([ErrorEvent](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorEvent))
      }
    }  
  
Fields  
---  
`group` |  `object (`[ErrorGroup](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorGroup)`)` Group data that is independent of the filter criteria.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Approximate total number of events in the given group that match the filter criteria.  
`affectedUsersCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Approximate number of affected users in the given group that match the filter criteria. Users are distinguished by data in the `[ErrorContext](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorContext)` of the individual error events, such as their login name or their remote IP address in case of HTTP requests. The number of affected users can be zero even if the number of errors is non-zero if no data was provided from which the affected user could be deduced. Users are counted based on data in the request context that was provided in the error report. If more users are implicitly affected, such as due to a crash of the whole service, this is not reflected here.  
`timedCounts[]` |  `object (`[TimedCount](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.TimedCount)`)` Approximate number of occurrences over time. Timed counts returned by ListGroups are guaranteed to be:

  * Inside the requested time interval
  * Non-overlapping, and
  * Ordered by ascending time.

  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Approximate first occurrence that was ever seen for this group and which matches the given filter criteria, ignoring the time_range that was specified in the request.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Approximate last occurrence that was ever seen for this group and which matches the given filter criteria, ignoring the time_range that was specified in the request.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`affectedServices[]` |  `object (`[ServiceContext](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ServiceContext)`)` Service contexts with a non-zero error count for the given filter criteria. This list can be truncated if multiple services are affected. Refer to `num_affected_services` for the total count.  
`numAffectedServices` |  `integer` The total number of services with a non-zero error count for the given filter criteria.  
`representative` |  `object (`[ErrorEvent](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorEvent)`)` An arbitrary event that is chosen as representative for the whole group. The representative event is intended to be used as a quick preview for the whole group. Events in the group are usually sufficiently similar to each other such that showing an arbitrary representative provides insight into the characteristics of the group as a whole.  
  
### ErrorGroup

JSON representation  
---  
      
    
    {
      "name": string,
      "groupId": string,
      "trackingIssues": [
        {
          object ([TrackingIssue](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.TrackingIssue))
        }
      ],
      "resolutionStatus": enum ([ResolutionStatus](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ResolutionStatus))
    }  
  
Fields  
---  
`name` |  `string` The group resource name. Written as `projects/{projectID}/groups/{group_id}` or `projects/{projectID}/locations/{location}/groups/{group_id}`Examples: `projects/my-project-123/groups/my-group`, `projects/my-project-123/locations/us-central1/groups/my-group`In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified.  
`groupId` |  `string` An opaque identifier of the group. This field is assigned by the Error Reporting system and always populated.In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).  
`trackingIssues[]` |  `object (`[TrackingIssue](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.TrackingIssue)`)` Associated tracking issues.  
`resolutionStatus` |  `enum (`[ResolutionStatus](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ResolutionStatus)`)` Error group's resolution status.An unspecified resolution status will be interpreted as OPEN  
  
### TrackingIssue

JSON representation  
---  
      
    
    {
      "url": string
    }  
  
Fields  
---  
`url` |  `string` A URL pointing to a related entry in an issue tracking system. Example: `https://github.com/user/project/issues/4`  
  
### TimedCount

JSON representation  
---  
      
    
    {
      "count": string,
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Approximate number of occurrences in the given time period.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Start of the time period to which `count` refers (included).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` End of the time period to which `count` refers (excluded).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### ServiceContext

JSON representation  
---  
      
    
    {
      "service": string,
      "version": string,
      "resourceType": string
    }  
  
Fields  
---  
`service` |  `string` An identifier of the service, such as the name of the executable, job, or Google App Engine service name. This field is expected to have a low number of values that are relatively stable over time, as opposed to `version`, which can be changed whenever new code is deployed.Contains the service name for error reports extracted from Google App Engine logs or `default` if the App Engine default service is used.  
`version` |  `string` Represents the source code version that the developer provided, which could represent a version label or a Git SHA-1 hash, for example. For App Engine standard environment, the version is set to the version of the app.  
`resourceType` |  `string` Type of the MonitoredResource. List of possible values: <https://cloud.google.com/monitoring/api/resources>Value is set automatically for incoming errors and must not be set when reporting errors.  
  
### ErrorEvent

JSON representation  
---  
      
    
    {
      "eventTime": string,
      "serviceContext": {
        object ([ServiceContext](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ServiceContext))
      },
      "message": string,
      "context": {
        object ([ErrorContext](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorContext))
      }
    }  
  
Fields  
---  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time when the event occurred as provided in the error report. If the report did not contain a timestamp, the time the error was received by the Error Reporting system is used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`serviceContext` |  `object (`[ServiceContext](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ServiceContext)`)` The `ServiceContext` for which this error was reported.  
`message` |  `string` The stack trace that was reported or logged by the service.  
`context` |  `object (`[ErrorContext](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.ErrorContext)`)` Data about the context in which the error occurred.  
  
### ErrorContext

JSON representation  
---  
      
    
    {
      "httpRequest": {
        object ([HttpRequestContext](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.HttpRequestContext))
      },
      "user": string,
      "reportLocation": {
        object ([SourceLocation](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.SourceLocation))
      },
      "sourceReferences": [
        {
          object ([SourceReference](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.SourceReference))
        }
      ]
    }  
  
Fields  
---  
`httpRequest` |  `object (`[HttpRequestContext](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.HttpRequestContext)`)` The HTTP request which was processed when the error was triggered.  
`user` |  `string` The user who caused or was affected by the crash. This can be a user ID, an email address, or an arbitrary token that uniquely identifies the user. When sending an error report, leave this field empty if the user was not logged in. In this case the Error Reporting system will use other data, such as remote IP address, to distinguish affected users. See `affected_users_count` in `ErrorGroupStats`.  
`reportLocation` |  `object (`[SourceLocation](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.SourceLocation)`)` The location in the source code where the decision was made to report the error, usually the place where it was logged. For a logged exception this would be the source line where the exception is logged, usually close to the place where it was caught.  
`sourceReferences[]` |  `object (`[SourceReference](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp/tools_list/list_group_stats#Output.Schema.SourceReference)`)` Source code that was used to build the executable which has caused the given error message.  
  
### HttpRequestContext

JSON representation  
---  
      
    
    {
      "method": string,
      "url": string,
      "userAgent": string,
      "referrer": string,
      "responseStatusCode": integer,
      "remoteIp": string
    }  
  
Fields  
---  
`method` |  `string` The type of HTTP request, such as `GET`, `POST`, etc.  
`url` |  `string` The URL of the request.  
`userAgent` |  `string` The user agent information that is provided with the request.  
`referrer` |  `string` The referrer information that is provided with the request.  
`responseStatusCode` |  `integer` The HTTP response status code for the request.  
`remoteIp` |  `string` The IP address from which the request originated. This can be IPv4, IPv6, or a token which is derived from the IP address, depending on the data that has been provided in the error report.  
  
### SourceLocation

JSON representation  
---  
      
    
    {
      "filePath": string,
      "lineNumber": integer,
      "functionName": string
    }  
  
Fields  
---  
`filePath` |  `string` The source code filename, which can include a truncated relative path, or a full path from a production machine.  
`lineNumber` |  `integer` 1-based. 0 indicates that the line number is unknown.  
`functionName` |  `string` Human-readable name of a function or method. The value can include optional context like the class or package name. For example, `my.package.MyClass.method` in case of Java.  
  
### SourceReference

JSON representation  
---  
      
    
    {
      "repository": string,
      "revisionId": string
    }  
  
Fields  
---  
`repository` |  `string` Optional. A URI string identifying the repository. Example: "https://github.com/GoogleCloudPlatform/kubernetes.git"  
`revisionId` |  `string` The canonical and persistent identifier of the deployed revision. Example (git): "0035781c50ec7aa23385dc841529ce8a4b70db1b"  
  
### ResolutionStatus

Resolution status of an error group.

Enums  
---  
`RESOLUTION_STATUS_UNSPECIFIED` | Status is unknown. When left unspecified in requests, it is treated like OPEN.  
`OPEN` | The error group is not being addressed. This is the default for new groups. It is also used for errors re-occurring after marked RESOLVED.  
`ACKNOWLEDGED` | Error Group manually acknowledged, it can have an issue link attached.  
`RESOLVED` | Error Group manually resolved, more events for this group are not expected to occur.  
`MUTED` | The error group is muted and excluded by default on group stats requests.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
