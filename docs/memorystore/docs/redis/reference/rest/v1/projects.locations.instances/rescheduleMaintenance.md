---
url: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/rescheduleMaintenance/
title: Method: projects.locations.instances.rescheduleMaintenance \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:48.317812+00:00
---

# Method: projects.locations.instances.rescheduleMaintenance  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/rescheduleMaintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  Method: projects.locations.instances.rescheduleMaintenance Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * RescheduleType
  * Examples
  * Try it!



Reschedule maintenance for a given instance in a given project and location.

### HTTP request

`POST https://redis.googleapis.com/v1/{name=projects/*/locations/*/instances/*}:rescheduleMaintenance`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Redis instance resource name using the form: `projects/{projectId}/locations/{locationId}/instances/{instanceId}` where `locationId` refers to a GCP region.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rescheduleType": enum ([RescheduleType](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/rescheduleMaintenance#RescheduleType)),
      "scheduleTime": string
    }  
  
Fields  
---  
`rescheduleType` |  `enum (`[RescheduleType](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/rescheduleMaintenance#RescheduleType)`)` Required. If reschedule type is SPECIFIC_TIME, must set up scheduleTime as well.  
`scheduleTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when the maintenance shall be rescheduled to if rescheduleType=SPECIFIC_TIME, in RFC 3339 format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## RescheduleType

Reschedule options.

Enums  
---  
`RESCHEDULE_TYPE_UNSPECIFIED` | Not set.  
`IMMEDIATE` | If the user wants to schedule the maintenance to happen now.  
`NEXT_AVAILABLE_WINDOW` | If the user wants to use the existing maintenance policy to find the next available window.  
`SPECIFIC_TIME` | If the user wants to reschedule the maintenance to a specific time.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
