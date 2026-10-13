---
url: https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/CertificateConfig/
title: CertificateConfig \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:40.157368+00:00
---

# CertificateConfig  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/CertificateConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Reference ](https://docs.cloud.google.com/certificate-authority-service/docs/apis)



Send feedback 

#  CertificateConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SubjectConfig
    * JSON representation



A `[CertificateConfig](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/CertificateConfig)` describes an X.509 certificate or CSR that is to be created, as an alternative to using ASN.1.

JSON representation  
---  
      
    
    {
      "subjectConfig": {
        object ([SubjectConfig](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/CertificateConfig#SubjectConfig))
      },
      "reusableConfig": {
        object ([ReusableConfigWrapper](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/ReusableConfigWrapper))
      },
      "publicKey": {
        object ([PublicKey](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/PublicKey))
      }
    }  
  
Fields  
---  
`subjectConfig` |  `object (`[SubjectConfig](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/CertificateConfig#SubjectConfig)`)` Required. Specifies some of the values in a certificate that are related to the subject.  
`reusableConfig` |  `object (`[ReusableConfigWrapper](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/ReusableConfigWrapper)`)` Required. Describes how some of the technical fields in a certificate should be populated.  
`publicKey` |  `object (`[PublicKey](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/PublicKey)`)` Optional. The public key that corresponds to this config. This is, for example, used when issuing `[Certificates](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/projects.locations.certificateAuthorities.certificates#Certificate)`, but not when creating a self-signed `[CertificateAuthority](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/projects.locations.certificateAuthorities#CertificateAuthority)` or `[CertificateAuthority](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/projects.locations.certificateAuthorities#CertificateAuthority)` CSR.  
  
## SubjectConfig

These values are used to create the distinguished name and subject alternative name fields in an X.509 certificate.

JSON representation  
---  
      
    
    {
      "subject": {
        object ([Subject](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/Subject))
      },
      "commonName": string,
      "subjectAltName": {
        object ([SubjectAltNames](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/SubjectAltNames))
      }
    }  
  
Fields  
---  
`subject` |  `object (`[Subject](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/Subject)`)` Required. Contains distinguished name fields such as the location and organization.  
`commonName` |  `string` Optional. The "common name" of the distinguished name.  
`subjectAltName` |  `object (`[SubjectAltNames](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/SubjectAltNames)`)` Optional. The subject alternative name fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
