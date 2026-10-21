---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/getCertificateAuthority/
title: Method: projects.locations.instances.getCertificateAuthority \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:29.332392+00:00
---

# Method: projects.locations.instances.getCertificateAuthority  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/getCertificateAuthority/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  Method: projects.locations.instances.getCertificateAuthority Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * ManagedCertificateAuthority
    * JSON representation
  * CertChain
    * JSON representation



Gets details about the certificate authority for an Instance.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west15europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`GET https://memorystore.googleapis.com/v1/{name=projects/*/locations/*/instances/*}/certificateAuthority`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the certificate authority. Format: projects/{project}/locations/{location}/instances/{instance}/certificateAuthority  
  
### Request body

The request body must be empty.

### Response body

A certificate authority for an instance.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "managedServerCa": {
        object ([ManagedCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/getCertificateAuthority#ManagedCertificateAuthority))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique name of the certificate authority. Format: projects/{project}/locations/{location}/instances/{instance}  
Information about the server certificate authority. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`managedServerCa` |  `object (`[ManagedCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/getCertificateAuthority#ManagedCertificateAuthority)`)` A managed server certificate authority.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/memorystore.read-write`
  * `https://www.googleapis.com/auth/memorystore.read-only`



### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `memorystore.instances.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ManagedCertificateAuthority

A managed certificate authority.

JSON representation  
---  
      
    
    {
      "caCerts": [
        {
          object ([CertChain](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/getCertificateAuthority#CertChain))
        }
      ]
    }  
  
Fields  
---  
`caCerts[]` |  `object (`[CertChain](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/getCertificateAuthority#CertChain)`)` PEM encoded CA certificate chains for managed server authentication.  
  
## CertChain

A certificate chain.

JSON representation  
---  
      
    
    {
      "certificates": [
        string
      ]
    }  
  
Fields  
---  
`certificates[]` |  `string` The certificates that form the CA chain in order of leaf to root.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
