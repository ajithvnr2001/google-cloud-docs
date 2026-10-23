---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-text-redaction/
title: Text classification and redaction \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:44.417097+00:00
---

# Text classification and redaction  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-text-redaction/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Text classification and redaction Stay organized with collections  Save and categorize content based on your preferences. 

## When to use text classification and redaction

The following are some common use cases:

  * **Sanitize user input before database persistence** : Redact sensitive PII (such as Social Security numbers, credit card numbers, or driver's licenses) from free-form text before writing records to storage or application databases.
  * **Sanitize customer service transcripts and logs** : Strip identifying personal information from chat histories, support tickets, and email threads before agent review or training data ingestion.
  * **Identify sensitive entities for downstream tagging** : Classify text to extract infoTypes and likelihood ratings and use this information in custom workflows to route or flag high-risk messages.
  * **Mask confidential data in generative AI prompts** : Redact proprietary or regulated information from user prompts before sending content to public or third-party LLMs.



## Text classification

Consider the following text input:
    
    
    Please update my records with the following information:
    Email address: foo@example.com
    
    National Provider Identifier: 1245319599
    
    Driver's license: AC333991

The output is a list of findings, organized into the following categories:

  * [`InfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference "InfoTypes Reference")
  * [`Likelihood`](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood "Likelihood Concept Page")
  * `Offset` (Where in the string the potential `InfoType` was found)



Example output is shown in the table below.

`InfoType` | `Likelihood` | `Offset`  
---|---|---  
`US_HEALTHCARE_NPI` | `VERY_LIKELY` | `122`  
`EMAIL_ADDRESS` | `LIKELY` | `72`  
`US_DRIVERS_LICENSE_NUMBER` | `LIKELY` | `155`  
`CANADA_BC_PHN` | `VERY_UNLIKELY` | `122`  
`UK_TAXPAYER_REFERENCE` | `VERY_UNLIKELY` | `122`  
`CANADA_PASSPORT` | `VERY_UNLIKELY` | `155`  
  
## Automatic text redaction

Automatic redaction produces an output with sensitive data matches removed instead of giving you a list of findings.

The following is an example of automatic redaction input:
    
    
    Please update my records with the following information:
    Email address: foo@example.com
    
    National Provider Identifier: 1245319599
    
    Driver's license: AC333991

The following is an example of output using a placeholder of "***":
    
    
    Please update my records with the following information:
    Email address: ***
    
    National Provider Identifier: ***
    
    Driver's license: ***

## Resources

  * For more information about using Sensitive Data Protection to redact text, see [Redacting Sensitive Data From Text Content](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data).
  * For more information about using Sensitive Data Protection to de-identify sensitive data in text content—which includes "masking" sensitive data, replacing sensitive data with a "token" string, and encrypting and replacing sensitive data using a randomly generated or pre-determined key—see [De-identifying sensitive data in text content](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
