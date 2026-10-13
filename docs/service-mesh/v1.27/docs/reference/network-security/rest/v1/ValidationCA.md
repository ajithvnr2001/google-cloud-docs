---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-security/rest/v1/ValidationCA/
title: ValidationCA \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:09.877444+00:00
---

# ValidationCA  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-security/rest/v1/ValidationCA/

You are viewing v1.27 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback 

#  ValidationCA Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Specification of ValidationCA. Defines the mechanism to obtain the Certificate Authority certificate to validate the peer certificate.

JSON representation  
---  
      
    
    {
    
      // Union field type can be only one of the following:
      "grpcEndpoint": {
        object ([GrpcEndpoint](https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-security/rest/v1/GrpcEndpoint))
      },
      "certificateProviderInstance": {
        object ([CertificateProviderInstance](https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-security/rest/v1/CertificateProviderInstance))
      }
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
Union field `type`. The type of certificate provider which provides the CA certificate. `type` can be only one of the following:  
`grpcEndpoint` |  `object (`[GrpcEndpoint](https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-security/rest/v1/GrpcEndpoint)`)` gRPC specific configuration to access the gRPC server to obtain the CA certificate.  
`certificateProviderInstance` |  `object (`[CertificateProviderInstance](https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-security/rest/v1/CertificateProviderInstance)`)` The certificate provider instance specification that will be passed to the data plane, which will be used to load necessary credential information.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
