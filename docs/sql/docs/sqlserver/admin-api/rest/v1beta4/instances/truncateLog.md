---
url: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/truncateLog/
title: Method: instances.truncateLog \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:53.202965+00:00
---

# Method: instances.truncateLog  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/truncateLog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  Method: instances.truncateLog Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * InstancesTruncateLogRequest
    * JSON representation
  * TruncateLogContext
    * JSON representation
  * Examples
  * Try it!



Truncate MySQL general and slow query log tables MySQL only.

### HTTP request

`POST https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/truncateLog`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID of the Cloud SQL project.  
`instance` |  `string` Cloud SQL instance ID. This does not include the project ID.  
  
### Request body

The request body contains an instance of `[InstancesTruncateLogRequest](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/truncateLog#InstancesTruncateLogRequest)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## InstancesTruncateLogRequest

Instance truncate log request.

JSON representation  
---  
      
    
    {
      "truncateLogContext": {
        object ([TruncateLogContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/truncateLog#TruncateLogContext))
      }
    }  
  
Fields  
---  
`truncateLogContext` |  `object (`[TruncateLogContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/truncateLog#TruncateLogContext)`)` Contains details about the truncate log operation.  
  
## TruncateLogContext

Database Instance truncate log context.

JSON representation  
---  
      
    
    {
      "kind": string,
      "logType": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#truncateLogContext`.  
`logType` |  `string` The type of log to truncate. Valid values are `MYSQL_GENERAL_TABLE` and `MYSQL_SLOW_TABLE`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
