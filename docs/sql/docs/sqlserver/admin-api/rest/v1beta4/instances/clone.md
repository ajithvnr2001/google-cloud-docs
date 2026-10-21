---
url: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone/
title: Method: instances.clone \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:50.730105+00:00
---

# Method: instances.clone  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  Method: instances.clone Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * InstancesCloneRequest
    * JSON representation
  * CloneContext
    * JSON representation
  * BinLogCoordinates
    * JSON representation
  * Examples
  * Try it!



Creates a Cloud SQL instance as a clone of the source instance. Using this operation might cause your instance to restart.

### HTTP request

`POST https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/clone`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID of the source Cloud SQL instance.  
`instance` |  `string` The ID of the Cloud SQL instance to be cloned (source). This does not include the project ID.  
  
### Request body

The request body contains an instance of `[InstancesCloneRequest](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone#InstancesCloneRequest)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## InstancesCloneRequest

Database instance clone request.

JSON representation  
---  
      
    
    {
      "cloneContext": {
        object ([CloneContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone#CloneContext))
      }
    }  
  
Fields  
---  
`cloneContext` |  `object (`[CloneContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone#CloneContext)`)` Contains details about the clone operation.  
  
## CloneContext

Database instance clone context.

JSON representation  
---  
      
    
    {
      "kind": string,
      "pitrTimestampMs": string,
      "destinationInstanceName": string,
      "binLogCoordinates": {
        object ([BinLogCoordinates](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone#BinLogCoordinates))
      },
      "pointInTime": string,
      "allocatedIpRange": string,
      "databaseNames": [
        string
      ],
      "preferredZone": string,
      "preferredSecondaryZone": string,
      "sourceInstanceDeletionTime": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#cloneContext`.  
`pitrTimestampMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Reserved for future use.  
`destinationInstanceName` |  `string` Name of the Cloud SQL instance to be created as a clone.  
`binLogCoordinates` |  `object (`[BinLogCoordinates](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone#BinLogCoordinates)`)` Binary log coordinates, if specified, identify the position up to which the source instance is cloned. If not specified, the source instance is cloned up to the most recent binary log coordinates.  
`pointInTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp, if specified, identifies the time to which the source instance is cloned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`allocatedIpRange` |  `string` The name of the allocated ip range for the private ip Cloud SQL instance. For example: "google-managed-services-default". If set, the cloned instance ip will be created in the allocated range. The range name must comply with [RFC 1035](https://tools.ietf.org/html/rfc1035). Specifically, the name must be 1-63 characters long and match the regular expression [a-z](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/\[-a-z0-9\]*\[a-z0-9\])?. Reserved for future use.  
`databaseNames[]` |  `string` (SQL Server only) instances.clone only the specified databases from the source instance. instances.clone all databases if empty.  
`preferredZone` |  `string` Optional. Copy clone and point-in-time recovery clone of an instance to the specified zone. If no zone is specified, clone to the same primary zone as the source instance.  
`preferredSecondaryZone` |  `string` Optional. Copy clone and point-in-time recovery clone of a regional instance in the specified zones. If not specified, clone to the same secondary zone as the source instance. This value cannot be the same as the preferredZone field.  
`sourceInstanceDeletionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp used to identify the time when the source instance is deleted. If this instance is deleted, then you must set the timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## BinLogCoordinates

Binary log coordinates.

JSON representation  
---  
      
    
    {
      "binLogFileName": string,
      "binLogPosition": string,
      "kind": string
    }  
  
Fields  
---  
`binLogFileName` |  `string` Name of the binary log file for a Cloud SQL instance.  
`binLogPosition` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Position (offset) within the binary log file.  
`kind` |  `string` This is always `sql#binLogCoordinates`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
