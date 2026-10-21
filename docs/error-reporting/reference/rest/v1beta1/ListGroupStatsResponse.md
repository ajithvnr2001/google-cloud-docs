---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse/
title: ListGroupStatsResponse \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:41.374177+00:00
---

# ListGroupStatsResponse  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  ListGroupStatsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ErrorGroupStats
    * JSON representation
  * TimedCount
    * JSON representation



Contains a set of requested error group stats.

JSON representation  
---  
      
    
    {
      "errorGroupStats": [
        {
          object ([ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#ErrorGroupStats))
        }
      ],
      "nextPageToken": string,
      "timeRangeBegin": string
    }  
  
Fields  
---  
`errorGroupStats[]` |  `object (`[ErrorGroupStats](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#ErrorGroupStats)`)` The error group stats which match the given request.  
`nextPageToken` |  `string` If non-empty, more results are available. Pass this token, along with the same query parameters as the first request, to view the next page of results.  
`timeRangeBegin` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp specifies the start time to which the request was restricted. The start time is set based on the requested time range. It may be adjusted to a later time if a project has exceeded the storage quota and older data has been deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ErrorGroupStats

Data extracted for a specific group based on certain filter criteria, such as a given time period and/or service filter.

JSON representation  
---  
      
    
    {
      "group": {
        object ([ErrorGroup](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups#ErrorGroup))
      },
      "count": string,
      "affectedUsersCount": string,
      "timedCounts": [
        {
          object ([TimedCount](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#TimedCount))
        }
      ],
      "firstSeenTime": string,
      "lastSeenTime": string,
      "affectedServices": [
        {
          object ([ServiceContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext))
        }
      ],
      "numAffectedServices": integer,
      "representative": {
        object ([ErrorEvent](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorEvent))
      }
    }  
  
Fields  
---  
`group` |  `object (`[ErrorGroup](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups#ErrorGroup)`)` Group data that is independent of the filter criteria.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Approximate total number of events in the given group that match the filter criteria.  
`affectedUsersCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Approximate number of affected users in the given group that match the filter criteria. Users are distinguished by data in the `[ErrorContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext)` of the individual error events, such as their login name or their remote IP address in case of HTTP requests. The number of affected users can be zero even if the number of errors is non-zero if no data was provided from which the affected user could be deduced. Users are counted based on data in the request context that was provided in the error report. If more users are implicitly affected, such as due to a crash of the whole service, this is not reflected here.  
`timedCounts[]` |  `object (`[TimedCount](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListGroupStatsResponse#TimedCount)`)` Approximate number of occurrences over time. Timed counts returned by ListGroups are guaranteed to be:

  * Inside the requested time interval
  * Non-overlapping, and
  * Ordered by ascending time.

  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Approximate first occurrence that was ever seen for this group and which matches the given filter criteria, ignoring the timeRange that was specified in the request.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Approximate last occurrence that was ever seen for this group and which matches the given filter criteria, ignoring the timeRange that was specified in the request.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`affectedServices[]` |  `object (`[ServiceContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext)`)` Service contexts with a non-zero error count for the given filter criteria. This list can be truncated if multiple services are affected. Refer to `numAffectedServices` for the total count.  
`numAffectedServices` |  `integer` The total number of services with a non-zero error count for the given filter criteria.  
`representative` |  `object (`[ErrorEvent](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorEvent)`)` An arbitrary event that is chosen as representative for the whole group. The representative event is intended to be used as a quick preview for the whole group. Events in the group are usually sufficiently similar to each other such that showing an arbitrary representative provides insight into the characteristics of the group as a whole.  
  
## TimedCount

The number of errors in a given time period. All numbers are approximate since the error events are sampled before counting them.

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-12 UTC."],[],[]] 
