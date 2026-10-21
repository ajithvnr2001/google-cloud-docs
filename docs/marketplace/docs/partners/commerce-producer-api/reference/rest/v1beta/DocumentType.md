---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/DocumentType/
title: DocumentType \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:16.939798+00:00
---

# DocumentType  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/DocumentType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  DocumentType Stay organized with collections  Save and categorize content based on your preferences. 

Supported types of documents. Additional document types may be added in future. Further editions of the Google Cloud Marketplace Standard EULA may be published in future, which may result in changes to the subset of Standard EULA versions permitted to be used in new offers.

Enums  
---  
`DOCUMENT_TYPE_UNSPECIFIED` | The default / unset value. Do not use.  
`CUSTOM_END_USER_LICENSE_AGREEMENT` | The document is a custom EULA used in place of the standard product EULA. A private offer may not have more than one custom EULA document, and may not have both a custom EULA and a standard EULA.If this enum value is set, then mimeType and inlineContent must be set.  
`STATEMENT_OF_WORK` | The document is the statement of work described by the [Cloud Marketplace Product Specific Terms](https://cloud.google.com/terms/marketplace-product-terms). A private offer may not have more than one statement of work document.Whether this document type is required, optional, or not permitted depends on the service; see `Service.document_requirement`.The mimeType and inlineContent fields must be set.  
`STANDARD_END_USER_LICENSE_AGREEMENT_V1` | The document is the Marketplace standard EULA, with the following link: <https://cloud.google.com/terms/marketplace/eula-standard-v1-12102020>.This edition has been superseded by STANDARD_END_USER_LICENSE_AGREEMENT_V2. Offers created before that edition was published may have this document type, but it is not permitted on any service for new offers.  
`STANDARD_END_USER_LICENSE_AGREEMENT_V2` | The document is the Marketplace standard EULA, with the following link: <https://cloud.google.com/terms/marketplace/eula-standard-v2-01272021>New offers using Standard EULAs should set this enum value. A private offer may not have more than one standard EULA document, and may not have both a standard EULA and a custom EULA.Whether this document type is required, optional, or not permitted depends on the service; see `Service.document_requirement`.The mimeType and inlineContent fields must not be set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
