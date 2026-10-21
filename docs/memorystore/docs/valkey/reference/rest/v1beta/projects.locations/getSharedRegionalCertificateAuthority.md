---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations/getSharedRegionalCertificateAuthority/
title: Method: projects.locations.getSharedRegionalCertificateAuthority \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:39.869584+00:00
---

# Method: projects.locations.getSharedRegionalCertificateAuthority  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations/getSharedRegionalCertificateAuthority/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  Method: projects.locations.getSharedRegionalCertificateAuthority Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * RegionalManagedCertificateAuthority
    * JSON representation
  * RegionalCertChain
    * JSON representation



Gets the details of shared regional certificate authority information for Memorystore instance.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west15europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`GET https://memorystore.googleapis.com/v1beta/{name=projects/*/locations/*/sharedRegionalCertificateAuthority}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Regional certificate authority resource name using the form: `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority` where `locationId` refers to a Google Cloud region.  
  
### Request body

The request body must be empty.

### Response body

Shared regional certificate authority for an instance.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "managedServerCa": {
        object ([RegionalManagedCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations/getSharedRegionalCertificateAuthority#RegionalManagedCertificateAuthority))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique name of the resource in this scope including project and location using the form: `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`  
Server ca information. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`managedServerCa` |  `object (`[RegionalManagedCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations/getSharedRegionalCertificateAuthority#RegionalManagedCertificateAuthority)`)` CA certificate chains for memorystore managed server authentication.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/memorystore.read-write`



## RegionalManagedCertificateAuthority

CA certificate chains for memorystore managed server authentication.

JSON representation  
---  
      
    
    {
      "caCerts": [
        {
          object ([RegionalCertChain](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations/getSharedRegionalCertificateAuthority#RegionalCertChain))
        }
      ]
    }  
  
Fields  
---  
`caCerts[]` |  `object (`[RegionalCertChain](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations/getSharedRegionalCertificateAuthority#RegionalCertChain)`)` The PEM encoded CA certificate chains for memorystore managed server authentication  
  
## RegionalCertChain

The certificates that form the CA chain, from leaf to root order.

JSON representation  
---  
      
    
    {
      "certificates": [
        string
      ]
    }  
  
Fields  
---  
`certificates[]` |  `string` The certificates that form the CA chain, from leaf to root order.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
