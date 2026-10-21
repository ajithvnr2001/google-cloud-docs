---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs.bucketOperations
title: REST Resource: projects.locations.jobs.bucketOperations \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:40.158132+00:00
---

# REST Resource: projects.locations.jobs.bucketOperations  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs.bucketOperations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  REST Resource: projects.locations.jobs.bucketOperations Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: BucketOperation

BucketOperation represents a bucket-level breakdown of a Job.

JSON representation  
---  
      
    
    {
      "name": string,
      "bucketName": string,
      "createTime": string,
      "startTime": string,
      "completeTime": string,
      "counters": {
        object ([Counters](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Counters))
      },
      "errorSummaries": [
        {
          object ([ErrorSummary](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ErrorSummary))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs.bucketOperations#State)),
    
      // Union field object_configuration can be only one of the following:
      "prefixList": {
        object ([PrefixList](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PrefixList))
      },
      "manifest": {
        object ([Manifest](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Manifest))
      },
      "projectSource": {
        object ([ProjectSource](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource))
      }
      // End of list of possible types for union field object_configuration.
    
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
`name` |  `string` Identifier. The resource name of the BucketOperation. This is defined by the service. Format: `projects/{projectId}/locations/global/jobs/{jobId}/bucketOperations/{bucket_operation}`.  
`bucketName` |  `string` The bucket name of the objects to be transformed in the BucketOperation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that the BucketOperation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that the BucketOperation was started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that the BucketOperation was completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`counters` |  `object (`[Counters](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Counters)`)` Output only. Information about the progress of the bucket operation.  
`errorSummaries[]` |  `object (`[ErrorSummary](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ErrorSummary)`)` Output only. Summarizes errors encountered with sample error log entries.  
`state` |  `enum (`[State](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs.bucketOperations#State)`)` Output only. State of the BucketOperation.  
Union field `object_configuration`. Specifies objects to be transformed in the BucketOperation. `object_configuration` can be only one of the following:  
`prefixList` |  `object (`[PrefixList](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PrefixList)`)` Specifies objects matching a prefix set.  
`manifest` |  `object (`[Manifest](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Manifest)`)` Specifies objects in a manifest file.  
`projectSource` |  `object (`[ProjectSource](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource)`)` Specifies objects matching the object filters in a project source.  
Union field `transformation`. Action to be performed on the objects. `transformation` can be only one of the following:  
`putObjectHold` |  `object (`[PutObjectHold](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutObjectHold)`)` Changes object hold status.  
`deleteObject` |  `object (`[DeleteObject](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/DeleteObject)`)` Delete objects.  
`putMetadata` |  `object (`[PutMetadata](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutMetadata)`)` Updates object metadata. Allows updating fixed-key and custom metadata and fixed-key metadata i.e. Cache-Control, Content-Disposition, Content-Encoding, Content-Language, Content-Type, Custom-Time.  
`rewriteObject` |  `object (`[RewriteObject](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/RewriteObject)`)` Rewrite the object and updates metadata like KMS key.  
`updateObjectCustomContext` |  `object (`[UpdateObjectCustomContext](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/UpdateObjectCustomContext)`)` Update object custom context.  
`setObjectAcls` |  `object (`[SetObjectAcls](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/SetObjectAcls)`)` Updates object ACLs.  
  
## State

Describes state of the BucketOperation.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`QUEUED` | Created but not yet started.  
`RUNNING` | In progress.  
`SUCCEEDED` | Completed successfully.  
`CANCELED` | Cancelled by the user.  
`FAILED` | Terminated due to an unrecoverable failure.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs.bucketOperations/get)`

|  Gets a BucketOperation.  
  
### `[list](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs.bucketOperations/list)`

|  Lists BucketOperations in a given project and job.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
