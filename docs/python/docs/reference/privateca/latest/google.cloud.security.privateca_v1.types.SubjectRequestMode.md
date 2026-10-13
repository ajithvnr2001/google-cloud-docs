---
url: https://docs.cloud.google.com/python/docs/reference/privateca/latest/google.cloud.security.privateca_v1.types.SubjectRequestMode
title: Class SubjectRequestMode (1.20.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:52.921223+00:00
---

# Class SubjectRequestMode (1.20.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/privateca/latest/google.cloud.security.privateca_v1.types.SubjectRequestMode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SubjectRequestMode (1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.3  1.13.1  1.12.2  1.11.0  1.10.3  1.9.0  1.8.1  1.7.1  1.6.1  1.5.0  1.4.3  1.3.2  1.2.4  1.1.0  1.0.6  0.4.0  0.3.0  0.1.1 
    
    
    SubjectRequestMode(value)

Describes the way in which a Certificate's Subject and/or SubjectAltNames will be resolved.

## Enums  
  
---  
**Name** | **Description**  
`SUBJECT_REQUEST_MODE_UNSPECIFIED` | Not specified.  
`DEFAULT` | The default mode used in most cases. Indicates that the certificate's Subject and/or SubjectAltNames are specified in the certificate request. This mode requires the caller to have the `privateca.certificates.create` permission.  
`RDN_SEQUENCE` | A mode used to get an accurate representation of the Subject field's distinguished name. Indicates that the certificate's Subject and/or SubjectAltNames are specified in the certificate request. When parsing a PEM CSR this mode will maintain the sequence of RDNs found in the CSR's subject field in the issued Certificate. This mode requires the caller to have the `privateca.certificates.create` permission.  
`REFLECTED_SPIFFE` | A mode reserved for special cases. Indicates that the certificate should have one SPIFFE SubjectAltNames set by the service based on the caller's identity. This mode will ignore any explicitly specified Subject and/or SubjectAltNames in the certificate request. This mode requires the caller to have the `privateca.certificates.createForSelf` permission.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
