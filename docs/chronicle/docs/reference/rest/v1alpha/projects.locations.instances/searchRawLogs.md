---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs/
title: Method: instances.searchRawLogs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:57.899838+00:00
---

# Method: instances.searchRawLogs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.searchRawLogs Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * RawLogSearchDataView
    * JSON representation
  * EventTimeline
    * JSON representation
  * EventTimelineBucket
    * JSON representation
  * Aggregations
    * JSON representation
  * FieldAggregation
    * JSON representation
  * ValueCount
    * JSON representation
  * FieldValue
    * JSON representation



**Full name** : projects.locations.instances.searchRawLogs

Api to get events, entities, or unparsed raw logs matching the given raw log query. This api also returns the timeline, field aggregations over the results.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}:searchRawLogs`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. Chronicle instance this request is sent to. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "baselineQuery": string,
      "baselineTimeRange": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval))
      },
      "snapshotQuery": string,
      "snapshotTimeRange": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval))
      },
      "caseSensitive": boolean,
      "logTypes": [
        {
          object ([LogType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes#LogType))
        }
      ],
      "maxAggregationsPerField": integer,
      "pageSize": integer,
      "truncationEnabled": boolean,
      "dataView": {
        object ([RawLogSearchDataView](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#RawLogSearchDataView))
      },
      "skipCache": boolean,
      "draftDataAccessScope": {
        object ([DataAccessScope](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataAccessScopes#DataAccessScope))
      }
    }  
  
Fields  
---  
`baselineQuery` |  `string` Required. Query to search for raw logs. Any matches will be returned in the normalized form or raw log snippet if they can't be normalized.  
`baselineTimeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` Required. The time range to search for [inclusive, exclusive).  
`snapshotQuery` |  `string` Optional. Query to filter results. This is applied on top of the baseline query and doesn't fetch results outside of the baseline results restricted to the result limit.  
`snapshotTimeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` Optional. The time range to filter results [inclusive, exclusive). This time range must // be completely within `baselineTimeRange`. If not set, it is assumed to match `baselineTimeRange`.  
`caseSensitive` |  `boolean` Optional. If true, the search should be performed in a case-sensitive manner. This applies to both baseline and snapshot queries.  
`logTypes[]` |  `object (`[LogType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes#LogType)`)` Optional. If present, limit the result to the matching log types.  
`maxAggregationsPerField` |  `integer` Optional. The maximum number of values a UDM field can have before resorting to only show the top and bottom values by prevalence. If the number of values is greater than `maxValuesPerField` the top (`maxValuesPerField`/2) values and the bottom (`maxValuesPerField`/2) values by prevalence will be sent instead.  
`pageSize` |  `integer` Optional. The maximum number of results to return.  
`truncationEnabled` |  `boolean` Optional. Enables truncation of raw log results if `true`.  
`dataView` |  `object (`[RawLogSearchDataView](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#RawLogSearchDataView)`)` Optional. Internal only, not meant to be exposed to direct consumers.  
`skipCache` |  `boolean` Optional. If `true`, bypass reading from cache, executing the search fresh against primary storage. By default (`false`), searches may serve cached results (retained for up to 25 hours, or up to 12 hours for CMEK-enabled instances) for matching query time buckets to improve performance. Setting this to `true` ensures newly ingested logs within the queried time range are returned, but may increase search latency.  
`draftDataAccessScope` |  `object (`[DataAccessScope](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataAccessScopes#DataAccessScope)`)` Optional. Data access scope used to filter events. This is intended to be used by admins to preview in-development scopes. Should only be called by users with global access. If the caller does not have global access, the request will fail.  
  
### Response body

Response to SearchRawLogsRequest. Contains all the matches converted to normalized form when available, histogram of logs over time, field aggregations for top/bottom fields in all result types.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "matches": [
        {
          object ([RawLogResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/RawLogResult))
        }
      ],
      "progress": integer,
      "timeline": {
        object ([EventTimeline](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#EventTimeline))
      },
      "aggregations": {
        object ([Aggregations](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#Aggregations))
      },
      "nextPageToken": string,
      "truncated": boolean,
      "processingComplete": boolean,
      "complete": boolean
    }  
  
Fields  
---  
`matches[]` |  `object (`[RawLogResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/RawLogResult)`)` Results that match the raw log search.  
`progress` |  `integer` Progress of the query represented as a percentage between 0 and 100.  
`timeline` |  `object (`[EventTimeline](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#EventTimeline)`)` Timeline of results counts broken into buckets.  
`aggregations` |  `object (`[Aggregations](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#Aggregations)`)` Result fields with aggregated values.  
`nextPageToken` |  `string` Currently, this field is used only to indicate whether more value matches are available. If it is empty, there are no more value matches.  
`truncated` |  `boolean` If `true`, indicates that some log entries in the response were truncated.  
`processingComplete` |  `boolean` Internal only, not meant to be exposed to direct consumers. Indicates that all raw log results have been processed and the final results have started streaming. Required for raw logs chunking since `complete` is only set on the last chunk when all raw log results streaming is done.  
`complete` |  `boolean` Streaming for the raw log results is done. There will be no additional updates.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.events.searchRawLogs`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## RawLogSearchDataView

Data view options for Raw Log search.

JSON representation  
---  
      
    
    {
      "enableDedupedChunks": boolean
    }  
  
Fields  
---  
`enableDedupedChunks` |  `boolean` Optional. If true, enables deduping and chunking for Raw Log stream results. This prevents duplicate raw logs from being sent repeatedly and splits responses into size-limited chunks sent at regular intervals.  
  
## EventTimeline

Timeline of results counts broken into buckets.

JSON representation  
---  
      
    
    {
      "buckets": [
        {
          object ([EventTimelineBucket](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#EventTimelineBucket))
        }
      ],
      "bucketSize": string
    }  
  
Fields  
---  
`buckets[]` |  `object (`[EventTimelineBucket](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#EventTimelineBucket)`)` Complete list of buckets that represent the entire search window. Each bucket with duration of bucketSize. Time window of each bucket is [inclusive, exclusive).  
`bucketSize` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration of each timeline bucket.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## EventTimelineBucket

Represents a single time bucket containing number of parsed, unparsed logs in baseline and filtered results.

JSON representation  
---  
      
    
    {
      "baselineParsedLogCount": integer,
      "parsedLogCount": integer,
      "baselineUnparsedLogCount": integer,
      "unparsedLogCount": integer,
      "tooManyEvents": boolean,
      "baselineEventCount": integer,
      "eventCount": integer,
      "baselineEntityCount": integer,
      "entityCount": integer
    }  
  
Fields  
---  
`baselineParsedLogCount` |  `integer` Number of parsed logs in the baseline results.  
`parsedLogCount` |  `integer` Number of parsed logs in the filtered results.  
`baselineUnparsedLogCount` |  `integer` Number of unparsed logs in the baseline results.  
`unparsedLogCount` |  `integer` Number of unparsed logs in the filtered results.  
`tooManyEvents` |  `boolean` Indicates that the bucket has events that couldn't be displayed due to event limits. If the flag is true and the other counters are > 0, it indicates that we reached the limit and had to truncate the results. If the counters are 0 and the flag is set, it indicates that there are >0 events in this bucket that couldn't be fetched due to limit being reached by other buckets.  
`baselineEventCount` |  `integer` Number of events in the baseline results.  
`eventCount` |  `integer` Number of events in the filtered results.  
`baselineEntityCount` |  `integer` Number of context events in the baseline results.  
`entityCount` |  `integer` Number of context events in the filtered results.  
  
## Aggregations

Aggregations contains field aggregations for udm, entity, raw log, and grouped fields.

JSON representation  
---  
      
    
    {
      "udmFieldAggregations": [
        {
          object ([FieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldAggregation))
        }
      ],
      "groupFieldAggregations": [
        {
          object ([FieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldAggregation))
        }
      ],
      "entityFieldAggregations": [
        {
          object ([FieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldAggregation))
        }
      ],
      "rawLogAggregations": [
        {
          object ([FieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldAggregation))
        }
      ]
    }  
  
Fields  
---  
`udmFieldAggregations[]` |  `object (`[FieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldAggregation)`)` List of UDM fields with aggregated values.  
`groupFieldAggregations[]` |  `object (`[FieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldAggregation)`)` List of grouped UDM fields with aggregated values.  
`entityFieldAggregations[]` |  `object (`[FieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldAggregation)`)` List of entity fields with aggregated values.  
`rawLogAggregations[]` |  `object (`[FieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldAggregation)`)` List of raw logs with aggregated values.  
  
## FieldAggregation

All of the field values and their counts.

JSON representation  
---  
      
    
    {
      "field": string,
      "baselineCount": integer,
      "count": integer,
      "tooManyValues": boolean,
      "valueCount": integer,
      "allValues": [
        {
          object ([ValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#ValueCount))
        }
      ],
      "topValues": [
        {
          object ([ValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#ValueCount))
        }
      ],
      "bottomValues": [
        {
          object ([ValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#ValueCount))
        }
      ]
    }  
  
Fields  
---  
`field` |  `string` Name of the field being aggregated.  
`baselineCount` |  `integer` Number of baseline results with this field.  
`count` |  `integer` Number of filtered results with this field.  
`tooManyValues` |  `boolean` True, if there are too many values to be returned for this field.  
`valueCount` |  `integer` Number of values with non-zero result count for this field.  
`allValues[]` |  `object (`[ValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#ValueCount)`)` Populated with all events if `tooManyValues` is False.  
`topValues[]` |  `object (`[ValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#ValueCount)`)` Populated with the top N/2 events if `tooManyValues` is True. N is defined by maxAggregationsPerField.  
`bottomValues[]` |  `object (`[ValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#ValueCount)`)` Populated with the bottom N/2 events if `tooManyValues` is True. N is defined by maxAggregationsPerField.  
  
## ValueCount

The number of times a particular field value appears in the results.

JSON representation  
---  
      
    
    {
      "value": {
        object ([FieldValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldValue))
      },
      "baselineResultCount": integer,
      "resultCount": integer
    }  
  
Fields  
---  
`value` |  `object (`[FieldValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/searchRawLogs#FieldValue)`)` Value of the field.  
`baselineResultCount` |  `integer` Number of events with `value` for this field in the baseline results.  
`resultCount` |  `integer` Number of events with `value` for this field in the snapshot results.  
  
## FieldValue

The value of a field.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "stringValue": string,
      "int32Value": integer,
      "uint32Value": integer,
      "int64Value": string,
      "uint64Value": string,
      "floatValue": number,
      "doubleValue": number,
      "enumValue": string,
      "boolValue": boolean,
      "bytesValue": string,
      "isNull": boolean,
      "timestampValue": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The value of the field. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`stringValue` |  `string` The value of a string field.  
`int32Value` |  `integer` The value of a 32-bit integer field.  
`uint32Value` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The value of a 32-bit unsigned integer field.  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The value of a 64-bit integer field.  
`uint64Value` |  `string` The value of a 64-bit unsigned integer field.  
`floatValue` |  `number` The value of a single-precision floating-point field.  
`doubleValue` |  `number` The value of a double-precision floating-point field.  
`enumValue` |  `string` The value of an enum field.  
`boolValue` |  `boolean` The value of a boolean field.  
`bytesValue` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The value of a bytes field.A base64-encoded string.  
`isNull` |  `boolean` If true, the value is NULL.  
`timestampValue` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The value of a timestamp field.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
