---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/CertificateProvider/
title: CertificateProvider \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:33.079606+00:00
---

# CertificateProvider  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/CertificateProvider/

You are viewing archived v1.26 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)



Send feedback 

#  CertificateProvider Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Specification of certificate provider. Defines the mechanism to obtain the certificate and private key for peer to peer authentication.

JSON representation  
---  
      
    
    {
    
      // Union field type can be only one of the following:
      "grpcEndpoint": {
        object ([GrpcEndpoint](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/GrpcEndpoint))
      },
      "certificateProviderInstance": {
        object ([CertificateProviderInstance](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/CertificateProviderInstance))
      }
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
Union field `type`. The type of certificate provider which provides the certificates and private keys. `type` can be only one of the following:  
`grpcEndpoint` |  `object (`[GrpcEndpoint](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/GrpcEndpoint)`)` gRPC specific configuration to access the gRPC server to obtain the cert and private key.  
`certificateProviderInstance` |  `object (`[CertificateProviderInstance](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/CertificateProviderInstance)`)` The certificate provider instance specification that will be passed to the data plane, which will be used to load necessary credential information.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-23 UTC."],[],[]] 
