---
url: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails
title: REST Resource: projects.locations.reportConfigs.reportDetails \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:08.151543+00:00
---

# REST Resource: projects.locations.reportConfigs.reportDetails  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  REST Resource: projects.locations.reportConfigs.reportDetails Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: ReportDetail

Message describing the `ReportDetail` object. `ReportDetail` represents the metadata of the generated inventory report for a report configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "snapshotTime": string,
      "reportPathPrefix": string,
      "shardsCount": string,
      "status": {
        object ([Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status))
      },
      "labels": {
        string: string,
        ...
      },
      "targetDatetime": {
        object ([DateTime](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails#DateTime))
      },
      "reportMetrics": {
        object ([Metrics](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails#Metrics))
      }
    }  
  
Fields  
---  
`name` |  `string` Name of resource. Format: `projects/{projectNumber}/locations/{location}/reportConfigs/{report-config-id}/reportDetails/{report-detail-id}`.  
`snapshotTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The snapshot time. All the inventory report data is referenced at this point of time.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`reportPathPrefix` |  `string` Prefix of the object name of each report's shard. This has the full prefix except the `extension` and `shard_id`. For example, if the `destinationPath` is `{report-config-id}/dt={datetime}`, then the shard object name is `gs://my-insights/1A34-F2E456-12B456-1C3D/dt=2022-05-20T06:35/1A34-F2E456-12B456-1C3D_2022-05-20T06:35_5.csv` and the value of `reportPathPrefix` field is `gs://my-insights/1A34-F2E456-12B456-1C3D/dt=2022-05-20T06:35/1A34-F2E456-12B456-1C3D_2022-05-20T06:35_`.  
`shardsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total shards generated for the inventory report.  
`status` |  `object (`[Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status)`)` Status of the inventory report.  
`labels` |  `map (key: string, value: string)` Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`targetDatetime` |  `object (`[DateTime](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails#DateTime)`)` The date and time of the inventory report generation. This field is auto-populated. The time part of `targetDatetime` is always `0`.  
`reportMetrics` |  `object (`[Metrics](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails#Metrics)`)` Metrics of the inventory report.  
  
## DateTime

Represents civil time (or occasionally physical time).

This type can represent a civil time in one of a few possible ways:

  * When utcOffset is set and timeZone is unset: a civil time on a calendar day with a particular offset from UTC.
  * When timeZone is set and utcOffset is unset: a civil time on a calendar day in a particular time zone.
  * When neither timeZone nor utcOffset is set: a civil time on a calendar day in local time.



The date is relative to the Proleptic Gregorian Calendar.

If year, month, or day are 0, the DateTime is considered not to have a specific year, month, or day respectively.

This type may also be used to represent a physical time if all the date and time fields are set and either case of the `time_offset` oneof is set. Consider using `Timestamp` message for physical time instead. If your use case also would like to store the user's timezone, that can be done in another field.

This type is more flexible than some applications may want. Make sure to document and validate your application's limitations.

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer,
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer,
    
      // Union field time_offset can be only one of the following:
      "utcOffset": string,
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails#TimeZone))
      }
      // End of list of possible types for union field time_offset.
    }  
  
Fields  
---  
`year` |  `integer` Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.  
`month` |  `integer` Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.  
`day` |  `integer` Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.  
`hours` |  `integer` Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.  
`seconds` |  `integer` Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.  
Union field `time_offset`. Optional. Specifies either the UTC offset or the time zone of the DateTime. Choose carefully between them, considering that time zone data may change in the future (for example, a country modifies their DST start/end dates, and future DateTimes in the affected range had already been stored). If omitted, the DateTime is considered to be in local time. `time_offset` can be only one of the following:  
`utcOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails#TimeZone)`)` Time zone.  
  
## TimeZone

Represents a time zone from the [IANA Time Zone Database](https://www.iana.org/time-zones).

JSON representation  
---  
      
    
    {
      "id": string,
      "version": string
    }  
  
Fields  
---  
`id` |  `string` IANA Time Zone Database time zone. For example "America/New_York".  
`version` |  `string` Optional. IANA Time Zone Database version number. For example "2019a".  
  
## Metrics

Metrics associated with the generated report.

JSON representation  
---  
      
    
    {
      "processedRecordsCount": string
    }  
  
Fields  
---  
`processedRecordsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Count of Cloud Storage objects that are part of the inventory report.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails/get)`

|  Gets an existing inventory report in a given project for a given location.  
  
### `[list](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails/list)`

|  Lists the inventory reports in a given project for a given location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
