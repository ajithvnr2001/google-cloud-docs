---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/failover/
title: Method: instances.failover \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:07.344312+00:00
---

# Method: instances.failover  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Method: instances.failover Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * InstancesFailoverRequest
    * JSON representation
  * FailoverContext
    * JSON representation
  * Examples
  * Try it!



Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance. Users are then rerouted to the new primary. For more information, see the [Overview of high availability](https://cloud.google.com/sql/docs/mysql/high-availability) page in the Cloud SQL documentation. If using Legacy HA (MySQL only), this causes the instance to failover to its failover replica instance.

### HTTP request

`POST https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/failover`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` ID of the project that contains the read replica.  
`instance` |  `string` Cloud SQL instance ID. This does not include the project ID.  
  
### Request body

The request body contains an instance of `[InstancesFailoverRequest](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/failover#InstancesFailoverRequest)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## InstancesFailoverRequest

Instance failover request.

JSON representation  
---  
      
    
    {
      "failoverContext": {
        object ([FailoverContext](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/failover#FailoverContext))
      }
    }  
  
Fields  
---  
`failoverContext` |  `object (`[FailoverContext](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/failover#FailoverContext)`)` instances.failover Context.  
  
## FailoverContext

Database instance failover context.

JSON representation  
---  
      
    
    {
      "settingsVersion": string,
      "kind": string
    }  
  
Fields  
---  
`settingsVersion` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The current settings version of this instance. Request will be rejected if this version doesn't match the current settings version.  
`kind` |  `string` This is always `sql#failoverContext`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
