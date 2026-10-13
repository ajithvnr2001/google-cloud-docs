---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-DenyAccessState/
title: Policy Troubleshooter V3 API - Module Google::Cloud::PolicyTroubleshooter::Iam::V3::DenyAccessState (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:57.477561+00:00
---

# Policy Troubleshooter V3 API - Module Google::Cloud::PolicyTroubleshooter::Iam::V3::DenyAccessState (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-DenyAccessState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Troubleshooter V3 API - Module Google::Cloud::PolicyTroubleshooter::Iam::V3::DenyAccessState (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Policy Troubleshooter V3 API module Google::Cloud::PolicyTroubleshooter::Iam::V3::DenyAccessState.

Whether IAM deny policies deny the principal the permission.

## Constants 

### DENY_ACCESS_STATE_UNSPECIFIED

**value:** 0  
Not specified.

### DENY_ACCESS_STATE_DENIED

**value:** 1  
The deny policy denies the principal the permission.

### DENY_ACCESS_STATE_NOT_DENIED

**value:** 2  
The deny policy doesn't deny the principal the permission.

### DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL

**value:** 3  
The deny policy denies the principal the permission if a condition expression evaluates to `true`. However, the sender of the request didn't provide enough context for Policy Troubleshooter to evaluate the condition expression.

### DENY_ACCESS_STATE_UNKNOWN_INFO

**value:** 4  
The sender of the request does not have access to all of the deny policies that Policy Troubleshooter needs to evaluate the principal's access.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
