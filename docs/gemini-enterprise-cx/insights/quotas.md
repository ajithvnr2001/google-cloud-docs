---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/quotas/
title: Quotas & limits \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:55.614548+00:00
---

# Quotas & limits  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Quotas & limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains the current API restrictions and usage limits for Customer Experience Insights. This page will be updated to reflect any changes to these restrictions and usage limits. We reserve the right to change these limits.

For more information about requesting a quota increase, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

[Google Cloud console CX Insights quotas](https://console.cloud.google.com/apis/api/contactcenterinsights.googleapis.com/quotas)

After submitting your request, Google might contact you for more information and inform you whether your request is approved or denied.

## Request quota

The current API usage quota for CX Insights are as follows (and are subject to change):

Type of Quota | Usage Quota  
---|---  
Total number of requests per minute | 3000  
`CreateConversation` requests per minute | 300  
`CreateAnalysis` requests per minute | 300  
`ExportInsightsData` requests per minute | 60  
`UploadConversation` requests per minute | 300  
`DiagnoseConversations` requests per day per project | 50  
  
The current API resource limits for CX Insights are as follows (and are subject to change):

Type of Quota | Quota  
---|---  
Conversations per region | 2,000,000  
Analyses per region | 2,000,000  
Issue models per region | 10  
Deployed issue model per region | 5  
  
## Training operations

Type of Quota | Quota  
---|---  
Concurrent issue model creation operations per region | 1  
Concurrent faq model creation operations per region | 1  
  
## Bulk Operations

Type of Quota | Quota  
---|---  
Concurrent bulk analyze conversation operations per region | 1  
Concurrent bulk ingest creation operations per region | 1  
**Note:** Bulk analyze operations are queued up one after the other if quota is not available and will be resumed once the running operations complete.

## Summarization

Customer Experience Insights uses [Agent Assist](https://docs.cloud.google.com/agent-assist) to generate conversation summaries. When you run summarization for Customer Experience Insights analyses, you will see an additional line item on your bill for Agent Assist API usage. You may have to request additional Agent Assist quota.

## Speech to Text

Customer Experience Insights uses Speech to Text to generate transcriptions. You may have to [request additional quota as specified here](https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api#stt-quota).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
