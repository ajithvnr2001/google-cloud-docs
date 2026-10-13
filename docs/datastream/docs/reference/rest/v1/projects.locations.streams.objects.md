---
url: https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects
title: REST Resource: projects.locations.streams.objects \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:28.465819+00:00
---

# REST Resource: projects.locations.streams.objects  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Reference ](https://docs.cloud.google.com/datastream/docs/reference/rest)



Send feedback 

#  REST Resource: projects.locations.streams.objects Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: StreamObject
    * JSON representation
  * BackfillJob
    * JSON representation
  * State
  * Trigger
  * EventFilter
    * JSON representation
  * Methods



## Resource: StreamObject

A specific stream object (e.g a specific DB table).

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "displayName": string,
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/Error))
        }
      ],
      "backfillJob": {
        object ([BackfillJob](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects#BackfillJob))
      },
      "sourceObject": {
        object ([SourceObjectIdentifier](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/SourceObjectIdentifier))
      },
      "customizationRules": [
        {
          object ([CustomizationRule](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/CustomizationRule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The object resource's name.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the object.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update time of the object.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Required. Display name.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/Error)`)` Output only. Active errors on the object.  
`backfillJob` |  `object (`[BackfillJob](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects#BackfillJob)`)` The latest backfill job that was initiated for the stream object.  
`sourceObject` |  `object (`[SourceObjectIdentifier](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/SourceObjectIdentifier)`)` The object identifier in the data source.  
`customizationRules[]` |  `object (`[CustomizationRule](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/CustomizationRule)`)` Output only. The customization rules for the object. These rules are derived from the parent Stream's `ruleSets` and represent the intended configuration for the object.  
  
## BackfillJob

Represents a backfill job on a specific stream object.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects#State)),
      "trigger": enum ([Trigger](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects#Trigger)),
      "lastStartTime": string,
      "lastEndTime": string,
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/Error))
        }
      ],
      "eventFilter": {
        object ([EventFilter](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects#EventFilter))
      }
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects#State)`)` Output only. Backfill job state.  
`trigger` |  `enum (`[Trigger](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects#Trigger)`)` Backfill job's triggering reason.  
`lastStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Backfill job's start time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Backfill job's end time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/Error)`)` Output only. Errors which caused the backfill job to fail.  
`eventFilter` |  `object (`[EventFilter](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects#EventFilter)`)` Output only. The filter for performing a partial backfill.  
  
## State

State of the stream object's backfill job.

Enums  
---  
`STATE_UNSPECIFIED` | Default value.  
`NOT_STARTED` | Backfill job was never started for the stream object (stream has backfill strategy defined as manual or object was explicitly excluded from automatic backfill).  
`PENDING` | Backfill job will start pending available resources.  
`ACTIVE` | Backfill job is running.  
`STOPPED` | Backfill job stopped (next job run will start from beginning).  
`FAILED` | Backfill job failed (due to an error).  
`COMPLETED` | Backfill completed successfully.  
`UNSUPPORTED` | Backfill job failed since the table structure is currently unsupported for backfill.  
  
## Trigger

Triggering reason for a backfill job.

Enums  
---  
`TRIGGER_UNSPECIFIED` | Default value.  
`AUTOMATIC` | Object backfill job was triggered automatically according to the stream's backfill strategy.  
`MANUAL` | Object backfill job was triggered manually using the dedicated API.  
  
## EventFilter

Represents a filter for included data on a stream object.

JSON representation  
---  
      
    
    {
    
      // Union field filter can be only one of the following:
      "sqlWhereClause": string
      // End of list of possible types for union field filter.
    }  
  
Fields  
---  
Union field `filter`. A filter type. `filter` can be only one of the following:  
`sqlWhereClause` |  `string` An SQL-query Where clause selecting which data should be included, not including the "WHERE" keyword. e.g., `t.key1 = 'value1' AND t.key2 = 'value2'`  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/get)`

|  Use this method to get details about a stream object.  
  
### `[list](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/list)`

|  Use this method to list the objects of a specific stream.  
  
### `[lookup](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/lookup)`

|  Use this method to look up a stream object by its source object identifier.  
  
### `[startBackfillJob](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/startBackfillJob)`

|  Use this method to start a backfill job for the specified stream object.  
  
### `[stopBackfillJob](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/stopBackfillJob)`

|  Use this method to stop a backfill job for the specified stream object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
