---
url: https://docs.cloud.google.com/certificate-authority-service/docs/using-grpc/
title: Using gRPC with Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:54:04.552323+00:00
---

# Using gRPC with Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/using-grpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Reference ](https://docs.cloud.google.com/certificate-authority-service/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using gRPC with Certificate Authority Service

If you are using manually created [gRPC](https://grpc.io/) libraries to make API calls to Certificate Authority Service, you must add `x-goog-request-params: '<request-field>:<resource-name>'` as a header. The proper use of `x-goog-request-params` ensures that the request is routed to the appropriate region for your CA Service resources.

Given below are a few examples of methods with their respective request field and sample header. 

**Method** : [CreateCertificateAuthority](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1beta1#createcertificateauthorityrequest)  
**Request field** : [CreateCertificateAuthority.parent](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1beta1#google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest.FIELDS.string.google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest.parent)  

    
    
    x-goog-request-params: 'parent: projects/PROJECT_ID/locations/LOCATION_ID'  
  
---  
**Method** : [GetCertificateAuthority](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1beta1#getcertificateauthorityrequest)  
**Request field** : [GetCertificateAuthority.name](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1beta1#google.cloud.security.privateca.v1beta1.GetCertificateAuthorityRequest.FIELDS.string.google.cloud.security.privateca.v1beta1.GetCertificateAuthorityRequest.name)  

    
    
    x-goog-request-params: 'name: projects/PROJECT_ID/locations/LOCATION_ID/certificateAuthorities/CA_NAME'  
  
**Method** : [UpdateCertificateAuthority](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1beta1#updatecertificateauthorityrequest)  
**Request field** : [UpdateCertificateAuthority.certificate_authority.name](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1beta1#google.cloud.security.privateca.v1beta1.UpdateCertificateAuthorityRequest.FIELDS.google.cloud.security.privateca.v1beta1.CertificateAuthority.google.cloud.security.privateca.v1beta1.UpdateCertificateAuthorityRequest.certificate_authority)  

    
    
    x-goog-request-params: 'CertificateAuthority.name: projects/PROJECT_ID/locations/LOCATION_ID/certificateAuthorities/CA_NAME'  
  
For the complete list of RPC methods and their respective request fields, see [Package google.cloud.security.privateca.v1beta1](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1beta1).

## What's next

  * [Cloud APIs: gRPC APIs](https://docs.cloud.google.com/apis/docs/client-libraries-explained#grpc_apis)
  * [RPC Reference](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
