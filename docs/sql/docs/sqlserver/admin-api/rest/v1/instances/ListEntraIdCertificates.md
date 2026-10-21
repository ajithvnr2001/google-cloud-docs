---
url: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/ListEntraIdCertificates/
title: Method: instances.ListEntraIdCertificates \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:37.910966+00:00
---

# Method: instances.ListEntraIdCertificates  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/ListEntraIdCertificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  Method: instances.ListEntraIdCertificates Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all versions of EntraID certificates for the specified instance. There can be up to three sets of certificates listed: the certificate that is currently in use, a future that has been added but not yet used to sign a certificate, and a certificate that has been rotated out.

### HTTP request

`GET https://sqladmin.googleapis.com/v1/projects/{project}/instances/{instance}/listEntraIdCertificates`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Required. Project ID of the project that contains the instance.  
`instance` |  `string` Required. Cloud SQL instance ID. This does not include the project ID.  
  
### Request body

The request body must be empty.

### Response body

Instances instances.ListEntraIdCertificates response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "certs": [
        {
          object ([SslCert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/sslCerts#SslCert))
        }
      ],
      "activeVersion": string,
      "kind": string
    }  
  
Fields  
---  
`certs[]` |  `object (`[SslCert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/sslCerts#SslCert)`)` instances.list of Entra ID certificates for the instance.  
`activeVersion` |  `string` The `sha1Fingerprint` of the active certificate from `certs`.  
`kind` |  `string` This is always `sql#instancesListEntraIdCertificates`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
