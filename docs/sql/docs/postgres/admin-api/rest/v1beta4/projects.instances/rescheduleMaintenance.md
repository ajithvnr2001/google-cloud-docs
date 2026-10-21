---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/projects.instances/rescheduleMaintenance/
title: Method: projects.instances.rescheduleMaintenance \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:36.054381+00:00
---

# Method: projects.instances.rescheduleMaintenance  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/projects.instances/rescheduleMaintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  Method: projects.instances.rescheduleMaintenance Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * SqlInstancesRescheduleMaintenanceRequestBody
    * JSON representation
  * Reschedule
    * JSON representation
  * RescheduleType
  * Examples
  * Try it!



Reschedules the maintenance on the given instance.

### HTTP request

`POST https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/rescheduleMaintenance`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` ID of the project that contains the instance.  
`instance` |  `string` Cloud SQL instance ID. This does not include the project ID.  
  
### Request body

The request body contains an instance of `[SqlInstancesRescheduleMaintenanceRequestBody](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/projects.instances/rescheduleMaintenance#SqlInstancesRescheduleMaintenanceRequestBody)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## SqlInstancesRescheduleMaintenanceRequestBody

Reschedule options for maintenance windows.

JSON representation  
---  
      
    
    {
      "reschedule": {
        object ([Reschedule](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/projects.instances/rescheduleMaintenance#Reschedule))
      }
    }  
  
Fields  
---  
`reschedule` |  `object (`[Reschedule](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/projects.instances/rescheduleMaintenance#Reschedule)`)` Required. The type of the reschedule the user wants.  
  
## Reschedule

JSON representation  
---  
      
    
    {
      "rescheduleType": enum ([RescheduleType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/projects.instances/rescheduleMaintenance#RescheduleType)),
      "scheduleTime": string
    }  
  
Fields  
---  
`rescheduleType` |  `enum (`[RescheduleType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/projects.instances/rescheduleMaintenance#RescheduleType)`)` Required. The type of the reschedule.  
`scheduleTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when the maintenance shall be rescheduled to if rescheduleType=SPECIFIC_TIME, in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## RescheduleType

Enums  
---  
`RESCHEDULE_TYPE_UNSPECIFIED` |   
`IMMEDIATE` | Reschedules maintenance to happen now (within 5 minutes).  
`NEXT_AVAILABLE_WINDOW` | Reschedules maintenance to occur within one week from the originally scheduled day and time.  
`SPECIFIC_TIME` | Reschedules maintenance to a specific time and day.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
