---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DataRiskLevel-DataRiskLevelScore/
title: Cloud Data Loss Prevention (DLP) V2 API - Module Google::Cloud::Dlp::V2::DataRiskLevel::DataRiskLevelScore (v1.19.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:40.521102+00:00
---

# Cloud Data Loss Prevention (DLP) V2 API - Module Google::Cloud::Dlp::V2::DataRiskLevel::DataRiskLevelScore (v1.19.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DataRiskLevel-DataRiskLevelScore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Data Loss Prevention (DLP) V2 API - Module Google::Cloud::Dlp::V2::DataRiskLevel::DataRiskLevelScore (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.1  1.17.0  1.16.1  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.2  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1 

Reference documentation and code samples for the Cloud Data Loss Prevention (DLP) V2 API module Google::Cloud::Dlp::V2::DataRiskLevel::DataRiskLevelScore.

Various score levels for resources.

## Constants 

### RISK_SCORE_UNSPECIFIED

**value:** 0  
Unused.

### RISK_LOW

**value:** 10  
Low risk - Lower indication of sensitive data that appears to have additional access restrictions in place or no indication of sensitive data found.

### RISK_UNKNOWN

**value:** 12  
Unable to determine risk.

### RISK_MODERATE

**value:** 20  
Medium risk - Sensitive data may be present but additional access or fine grain access restrictions appear to be present. Consider limiting access even further or transform data to mask.

### RISK_HIGH

**value:** 30  
High risk – SPII may be present. Access controls may include public ACLs. Exfiltration of data may lead to user data loss. Re-identification of users may be possible. Consider limiting usage and or removing SPII.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
