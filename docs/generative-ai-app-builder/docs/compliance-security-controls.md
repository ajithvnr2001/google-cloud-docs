---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/compliance-security-controls/
title: Compliance and security controls \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:32.072700+00:00
---

# Compliance and security controls  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/compliance-security-controls/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Resources ](https://docs.cloud.google.com/generative-ai-app-builder/docs/resources)



Send feedback 

#  Compliance and security controls Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a high-level view of the compliance certifications and security controls that are supported by Agent Search.

## Certifications

Agent Search has various compliance certifications.

To find out if a product has a compliance certification, search for the product name in the security pages; for example, the following:

  * [FedRAMP](https://cloud.google.com/security/compliance/fedramp)
  * [ISO 27001](https://cloud.google.com/security/compliance/iso-27001)
  * [ISO 27017](https://cloud.google.com/security/compliance/iso-27017)
  * [ISO 27018](https://cloud.google.com/security/compliance/iso-27018)
  * [ISO 27701](https://cloud.google.com/security/compliance/iso-27701)
  * [SOC 1](https://cloud.google.com/security/compliance/soc-1)
  * [SOC 2](https://cloud.google.com/security/compliance/soc-2)
  * [SOC 3](https://cloud.google.com/security/compliance/soc-3)
  * [PCI DSS](https://cloud.google.com/security/compliance/pci-dss)
  * [BSI C5:2020](https://cloud.google.com/security/compliance/bsi-c5)
  * [HIPAA](https://cloud.google.com/security/compliance/hipaa)—Agent Search Pre-GA offerings are included in the Google Cloud Business Associate Agreement (BAA). If you will be using Agent Search to store or process Protected Health Information in a manner subject to the Health Insurance Portability and Accountability Act (HIPAA) of 1996 and/or any amendments or regulations under HIPAA, you must enter into an appropriate BAA with Google. For more information, see [HIPAA Compliance on Google Cloud](https://cloud.google.com/security/compliance/hipaa).



## Security controls

Agent Search provides security horizontals. The CMEK controls are only available in the Enterprise Edition.

Security controls compliance | Standard Edition | Enterprise Edition  
---|---|---  
[Data Residency (DRZ)](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations) | ✔ US and EU multi-region APIs only | ✔ US and EU multi-region APIs only  
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek) | ✘ | ✔   
US and EU multi-region APIs only *  
[ VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) | ✔ | ✔  
[Access Transparency](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-transparency) | ✔ US and EU multi-regions only | ✔ US and EU multi-regions only  
  
* Using external key manager (EKM) or hardware security module (HSM) with CMEK is in GA with allowlist. 

The following table identifies security controls for RAG APIs.

Security controls compliance | Ranking API | Grounded generation API | Check grounding API  
---|---|---|---  
[Data Residency (DRZ)](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations) | N/A | N/A | N/A  
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek) | N/A | N/A | N/A  
[ VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) | ✔ | ✔ | ✔  
[ Access Transparency](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-transparency) | ✔ | ✔ | ✔  
  
## What's next

Learn more about [Google Cloud compliance](https://docs.cloud.google.com/security/compliance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
