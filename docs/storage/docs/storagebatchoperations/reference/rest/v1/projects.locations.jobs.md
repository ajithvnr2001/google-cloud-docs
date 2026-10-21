---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs
title: REST Resource: projects.locations.jobs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:20:41.780704+00:00
---

# REST Resource: projects.locations.jobs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  REST Resource: projects.locations.jobs Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Job

The storage batch operations job description.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "loggingConfig": {
        object ([LoggingConfig](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#LoggingConfig))
      },
      "createTime": string,
      "scheduleTime": string,
      "completeTime": string,
      "counters": {
        object ([Counters](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Counters))
      },
      "errorSummaries": [
        {
          object ([ErrorSummary](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ErrorSummary))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#State)),
      "dryRun": boolean,
      "isMultiBucketJob": boolean,
    
      // Union field source can be only one of the following:
      "bucketList": {
        object ([BucketList](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#BucketList))
      },
      "projectSource": {
        object ([ProjectSource](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource))
      }
      // End of list of possible types for union field source.
    
      // Union field transformation can be only one of the following:
      "putObjectHold": {
        object ([PutObjectHold](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutObjectHold))
      },
      "deleteObject": {
        object ([DeleteObject](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/DeleteObject))
      },
      "putMetadata": {
        object ([PutMetadata](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutMetadata))
      },
      "rewriteObject": {
        object ([RewriteObject](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/RewriteObject))
      },
      "updateObjectCustomContext": {
        object ([UpdateObjectCustomContext](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/UpdateObjectCustomContext))
      },
      "setObjectAcls": {
        object ([SetObjectAcls](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/SetObjectAcls))
      }
      // End of list of possible types for union field transformation.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the job.Format: `projects/{projectId}/locations/global/jobs/{jobId}`.For example: `projects/123456/locations/global/jobs/job01`.`jobId` is unique in a given project.  
`description` |  `string` Optional. A user-provided description for the job.Maximum length: 1024 bytes when unicode-encoded.  
`loggingConfig` |  `object (`[LoggingConfig](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#LoggingConfig)`)` Optional. Logging configuration.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that the job was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`scheduleTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that the job was scheduled.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that the job was completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`counters` |  `object (`[Counters](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Counters)`)` Output only. Information about the progress of the job.  
`errorSummaries[]` |  `object (`[ErrorSummary](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ErrorSummary)`)` Output only. Summarizes errors encountered with sample error log entries.  
`state` |  `enum (`[State](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#State)`)` Output only. State of the job.  
`dryRun` |  `boolean` Optional. If true, the job runs in dry run mode, returning the total object count and, if the object configuration is a prefix list, the bytes found from source. No transformations are performed.  
`isMultiBucketJob` |  `boolean` Output only. If true, this job operates on multiple buckets. Multi-bucket jobs are subject to different quota limits than single-bucket jobs.  
Union field `source`. Specifies objects to be transformed. `source` can be only one of the following:  
`bucketList` |  `object (`[BucketList](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#BucketList)`)` Specifies a list of buckets and their objects to be transformed.  
`projectSource` |  `object (`[ProjectSource](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource)`)` Specifies a project source and filters to identify objects to be transformed.  
Union field `transformation`. Operation to be performed on the objects. `transformation` can be only one of the following:  
`putObjectHold` |  `object (`[PutObjectHold](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutObjectHold)`)` Changes object hold status.  
`deleteObject` |  `object (`[DeleteObject](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/DeleteObject)`)` Delete objects.  
`putMetadata` |  `object (`[PutMetadata](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutMetadata)`)` Updates object metadata. Allows updating fixed-key and custom metadata. For example, `Cache-Control`, `Content-Disposition`, `Content-Encoding`, `Content-Language`, `Content-Type`, `Custom-Time`, and `Retention configuration`.  
`rewriteObject` |  `object (`[RewriteObject](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/RewriteObject)`)` Rewrite the object and updates metadata like KMS key.  
`updateObjectCustomContext` |  `object (`[UpdateObjectCustomContext](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/UpdateObjectCustomContext)`)` Update object custom context.  
`setObjectAcls` |  `object (`[SetObjectAcls](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/SetObjectAcls)`)` Updates object ACLs.  
  
## BucketList

Describes list of buckets and their objects to be transformed.

JSON representation  
---  
      
    
    {
      "buckets": [
        {
          object ([Bucket](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#Bucket))
        }
      ]
    }  
  
Fields  
---  
`buckets[]` |  `object (`[Bucket](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#Bucket)`)` Required. List of buckets and their objects to be transformed. You can specify only one bucket per job. If multiple buckets are specified, an error occurs.  
  
## Bucket

Describes configuration of a single bucket and its objects to be transformed.

JSON representation  
---  
      
    
    {
      "bucket": string,
    
      // Union field object_configuration can be only one of the following:
      "prefixList": {
        object ([PrefixList](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PrefixList))
      },
      "manifest": {
        object ([Manifest](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Manifest))
      }
      // End of list of possible types for union field object_configuration.
    }  
  
Fields  
---  
`bucket` |  `string` Required. Bucket name for the objects to be transformed.  
Union field `object_configuration`. Specifies objects to be transformed. `object_configuration` can be only one of the following:  
`prefixList` |  `object (`[PrefixList](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PrefixList)`)` Specifies objects matching a prefix set.  
`manifest` |  `object (`[Manifest](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Manifest)`)` Specifies objects in a manifest file.  
  
## LoggingConfig

Specifies the Cloud Logging behavior.

JSON representation  
---  
      
    
    {
      "logActions": [
        enum ([LoggableAction](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#LoggableAction))
      ],
      "logActionStates": [
        enum ([LoggableActionState](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#LoggableActionState))
      ]
    }  
  
Fields  
---  
`logActions[]` |  `enum (`[LoggableAction](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#LoggableAction)`)` Required. Specifies the actions to be logged.  
`logActionStates[]` |  `enum (`[LoggableActionState](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#LoggableActionState)`)` Required. States in which Action are logged.If empty, no logs are generated.  
  
## LoggableAction

Loggable actions types.

Enums  
---  
`LOGGABLE_ACTION_UNSPECIFIED` | Illegal value, to avoid allowing a default.  
`TRANSFORM` | The corresponding transform action in this job.  
  
## LoggableActionState

Loggable action states filter.

Enums  
---  
`LOGGABLE_ACTION_STATE_UNSPECIFIED` | Illegal value, to avoid allowing a default.  
`SUCCEEDED` | `LoggableAction` completed successfully. `SUCCEEDED` actions are logged as [INFO][google.logging.type.LogSeverity.INFO].  
`FAILED` | `LoggableAction` terminated in an error state. `FAILED` actions are logged as [ERROR][google.logging.type.LogSeverity.ERROR].  
  
## State

Describes state of a job.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`RUNNING` | In progress.  
`SUCCEEDED` | Completed successfully.  
`CANCELED` | Cancelled by the user.  
`FAILED` | Terminated due to an unrecoverable failure.  
`QUEUED` | Queued but not yet started.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/cancel)`

|  Cancels a batch job.  
  
### `[create](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/create)`

|  Creates a batch job.  
  
### `[delete](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/delete)`

|  Deletes a batch job.  
  
### `[get](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/get)`

|  Gets a batch job.  
  
### `[list](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/list)`

|  Lists Jobs in a given project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
