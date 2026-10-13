---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel/
title: DataRiskLevel \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:43.924687+00:00
---

# DataRiskLevel  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  DataRiskLevel Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DataRiskLevelScore



Score is a summary of all elements in the data profile. A higher number means more risk.

JSON representation  
---  
      
    
    {
      "score": enum ([DataRiskLevelScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel#DataRiskLevelScore))
    }  
  
Fields  
---  
`score` |  `enum (`[DataRiskLevelScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel#DataRiskLevelScore)`)` The score applied to the resource.  
  
## DataRiskLevelScore

Various score levels for resources.

Enums  
---  
`RISK_SCORE_UNSPECIFIED` | Unused.  
`RISK_LOW` | Low risk - Lower indication of sensitive data that appears to have additional access restrictions in place or no indication of sensitive data found.  
`RISK_UNKNOWN` | Unable to determine risk.  
`RISK_MODERATE` | Medium risk - Sensitive data may be present but additional access or fine grain access restrictions appear to be present. Consider limiting access even further or transform data to mask.  
`RISK_HIGH` | High risk – SPII may be present. Access controls may include public ACLs. Exfiltration of data may lead to user data loss. Re-identification of users may be possible. Consider limiting usage and or removing SPII.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
