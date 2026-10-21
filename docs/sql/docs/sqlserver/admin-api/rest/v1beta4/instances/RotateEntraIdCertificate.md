---
url: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/RotateEntraIdCertificate/
title: Method: instances.RotateEntraIdCertificate \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:50.108845+00:00
---

# Method: instances.RotateEntraIdCertificate  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/RotateEntraIdCertificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  Method: instances.RotateEntraIdCertificate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * InstancesRotateEntraIdCertificateRequest
    * JSON representation
  * RotateEntraIdCertificateContext
    * JSON representation
  * Examples
  * Try it!



Rotates the Entra Id certificate version to one previously added with the addEntraIdCertificate method.

### HTTP request

`POST https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/rotateEntraIdCertificate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Required. Project ID of the project that contains the instance.  
`instance` |  `string` Required. Cloud SQL instance ID. This does not include the project ID.  
  
### Request body

The request body contains an instance of `[InstancesRotateEntraIdCertificateRequest](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/RotateEntraIdCertificate#InstancesRotateEntraIdCertificateRequest)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## InstancesRotateEntraIdCertificateRequest

Rotate Entra ID Certificate request.

JSON representation  
---  
      
    
    {
      "rotateEntraIdCertificateContext": {
        object ([RotateEntraIdCertificateContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/RotateEntraIdCertificate#RotateEntraIdCertificateContext))
      }
    }  
  
Fields  
---  
`rotateEntraIdCertificateContext` |  `object (`[RotateEntraIdCertificateContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/RotateEntraIdCertificate#RotateEntraIdCertificateContext)`)` Optional. Contains details about the rotate Entra ID certificate operation.  
  
## RotateEntraIdCertificateContext

Instance rotate Entra ID certificate context.

JSON representation  
---  
      
    
    {
      "kind": string,
      "nextVersion": string
    }  
  
Fields  
---  
`kind` |  `string` Optional. This is always `sql#rotateEntraIdCertificateContext`.  
`nextVersion` |  `string` Optional. The fingerprint of the next version to be rotated to. If left unspecified, will be rotated to the most recently added Entra ID certificate version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
