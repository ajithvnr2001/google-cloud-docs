---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-assured_workloads-v1/latest/Google-Cloud-AssuredWorkloads-V1-Violation-Remediation-RemediationType/
title: Assured Workloads for Government V1 API - Module Google::Cloud::AssuredWorkloads::V1::Violation::Remediation::RemediationType (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:25.752951+00:00
---

# Assured Workloads for Government V1 API - Module Google::Cloud::AssuredWorkloads::V1::Violation::Remediation::RemediationType (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-assured_workloads-v1/latest/Google-Cloud-AssuredWorkloads-V1-Violation-Remediation-RemediationType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Assured Workloads for Government V1 API - Module Google::Cloud::AssuredWorkloads::V1::Violation::Remediation::RemediationType (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1 

Reference documentation and code samples for the Assured Workloads for Government V1 API module Google::Cloud::AssuredWorkloads::V1::Violation::Remediation::RemediationType.

Classifying remediation into various types based on the kind of violation. For example, violations caused due to changes in boolean org policy requires different remediation instructions compared to violation caused due to changes in allowed values of list org policy.

## Constants 

### REMEDIATION_TYPE_UNSPECIFIED

**value:** 0  
Unspecified remediation type

### REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION

**value:** 1  
Remediation type for boolean org policy

### REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION

**value:** 2  
Remediation type for list org policy which have allowed values in the monitoring rule

### REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION

**value:** 3  
Remediation type for list org policy which have denied values in the monitoring rule

### REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION

**value:** 4  
Remediation type for gcp.restrictCmekCryptoKeyProjects

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
