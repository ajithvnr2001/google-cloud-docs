---
url: https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyOperationAttestation/
title: KeyOperationAttestation \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:21.931543+00:00
---

# KeyOperationAttestation  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyOperationAttestation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Reference ](https://docs.cloud.google.com/kms/docs/apis)



Send feedback 

#  KeyOperationAttestation Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AttestationFormat
  * CertificateChains
    * JSON representation



Contains an HSM-generated attestation about a key operation. For more information, see [Verifying attestations](https://cloud.google.com/kms/docs/attest-key).

JSON representation  
---  
      
    
    {
      "format": enum ([AttestationFormat](https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyOperationAttestation#AttestationFormat)),
      "content": string,
      "certChains": {
        object ([CertificateChains](https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyOperationAttestation#CertificateChains))
      }
    }  
  
Fields  
---  
`format` |  `enum (`[AttestationFormat](https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyOperationAttestation#AttestationFormat)`)` Output only. The format of the attestation data.  
`content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The attestation data provided by the HSM when the key operation was performed.A base64-encoded string.  
`certChains` |  `object (`[CertificateChains](https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyOperationAttestation#CertificateChains)`)` Output only. The certificate chains needed to validate the attestation  
  
## AttestationFormat

Attestation formats provided by the HSM.

Enums  
---  
`ATTESTATION_FORMAT_UNSPECIFIED` | Not specified.  
`CAVIUM_V1_COMPRESSED` | Cavium HSM attestation compressed with gzip. Note that this format is defined by Cavium and subject to change at any time.See <https://www.marvell.com/products/security-solutions/nitrox-hs-adapters/software-key-attestation.html>.  
`CAVIUM_V2_COMPRESSED` | Cavium HSM attestation V2 compressed with gzip. This is a new format introduced in Cavium's version 3.2-08.  
  
## CertificateChains

Certificate chains needed to verify the attestation. Certificates in chains are PEM-encoded and are ordered based on <https://tools.ietf.org/html/rfc5246#section-7.4.2>.

JSON representation  
---  
      
    
    {
      "caviumCerts": [
        string
      ],
      "googleCardCerts": [
        string
      ],
      "googlePartitionCerts": [
        string
      ]
    }  
  
Fields  
---  
`caviumCerts[]` |  `string` Cavium certificate chain corresponding to the attestation.  
`googleCardCerts[]` |  `string` Google card certificate chain corresponding to the attestation.  
`googlePartitionCerts[]` |  `string` Google partition certificate chain corresponding to the attestation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
