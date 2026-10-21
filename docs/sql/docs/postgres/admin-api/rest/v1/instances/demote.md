---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/demote/
title: Method: instances.demote \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:17.846877+00:00
---

# Method: instances.demote  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/demote/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  Method: instances.demote Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * InstancesDemoteRequest
    * JSON representation
  * DemoteContext
    * JSON representation
  * Examples
  * Try it!



Demotes an existing standalone instance to be a Cloud SQL read replica for an external database server.

### HTTP request

`POST https://sqladmin.googleapis.com/v1/projects/{project}/instances/{instance}/demote`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Required. ID of the project that contains the instance.  
`instance` |  `string` Required. Cloud SQL instance name.  
  
### Request body

The request body contains an instance of `[InstancesDemoteRequest](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/demote#InstancesDemoteRequest)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## InstancesDemoteRequest

This request is used to demote an existing standalone instance to be a Cloud SQL read replica for an external database server.

JSON representation  
---  
      
    
    {
      "demoteContext": {
        object ([DemoteContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/demote#DemoteContext))
      }
    }  
  
Fields  
---  
`demoteContext` |  `object (`[DemoteContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/demote#DemoteContext)`)` Required. Contains details about the demote operation.  
  
## DemoteContext

This context is used to demote an existing standalone instance to be a Cloud SQL read replica for an external database server.

JSON representation  
---  
      
    
    {
      "kind": string,
      "sourceRepresentativeInstanceName": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#demoteContext`.  
`sourceRepresentativeInstanceName` |  `string` Required. The name of the instance which acts as the on-premises primary instance in the replication setup.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
