---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/rotateServerCa/
title: Method: instances.rotateServerCa \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:09.639842+00:00
---

# Method: instances.rotateServerCa  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/rotateServerCa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Method: instances.rotateServerCa Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * InstancesRotateServerCaRequest
    * JSON representation
  * RotateServerCaContext
    * JSON representation
  * Examples
  * Try it!



Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method. For instances that have enabled Certificate Authority Service (CAS) based server CA, use instances.RotateServerCertificate to rotate the server certificate.

### HTTP request

`POST https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/rotateServerCa`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID of the project that contains the instance.  
`instance` |  `string` Cloud SQL instance ID. This does not include the project ID.  
  
### Request body

The request body contains an instance of `[InstancesRotateServerCaRequest](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/rotateServerCa#InstancesRotateServerCaRequest)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## InstancesRotateServerCaRequest

Rotate Server CA request.

JSON representation  
---  
      
    
    {
      "rotateServerCaContext": {
        object ([RotateServerCaContext](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/rotateServerCa#RotateServerCaContext))
      }
    }  
  
Fields  
---  
`rotateServerCaContext` |  `object (`[RotateServerCaContext](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/rotateServerCa#RotateServerCaContext)`)` Contains details about the rotate server CA operation.  
  
## RotateServerCaContext

Instance rotate server CA context.

JSON representation  
---  
      
    
    {
      "kind": string,
      "nextVersion": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#rotateServerCaContext`.  
`nextVersion` |  `string` The fingerprint of the next version to be rotated to. If left unspecified, will be rotated to the most recently added server CA version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
