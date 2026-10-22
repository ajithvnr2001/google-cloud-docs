---
url: https://docs.cloud.google.com/cloud-assist/proactive-cost-optimization/
title: Proactive cost optimization \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:47.855393+00:00
---

# Proactive cost optimization  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/proactive-cost-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Proactive cost optimization Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Proactive cost optimization is in private preview, and is only available to users that have a [Premium Support contract](https://cloud.google.com/support/premium).   
  
Use of this private preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805).

You can use Proactive Mode in Gemini Cloud Assist to automatically identify cost anomalies and gain actionable insights into your cloud spending.

## Before you begin

Before Proactive Mode can analyze cost data, you must [set up Proactive Mode](https://docs.cloud.google.com/cloud-assist/proactive-agents-setup).

## How proactive cost optimization works

Proactive Mode monitors your billing data in the background. When a [cost anomaly is detected](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies) by Cloud Billing, the agent automatically starts an investigation to determine the root cause. This investigation can happen at most once a day per project.

The agent correlates the cost spike to changes in your infrastructure, such as:

  * Significant changes in spending patterns over time.
  * Specific resources responsible for a spike.
  * Resources that are underutilized but represent high spending.



## View investigation results

Once an investigation is complete, you can review the root-cause analysis and remediation suggestions.

To view results, go to the **Cloud Hub Optimization** page in the Google Cloud console:

[Go to Cloud Hub Optimization](https://console.cloud.google.com/cloud-hub/optimization)

## Automate cost notifications

You can build automated workflows that react when a cost investigation is complete by using Eventarc. 

To isolate cost-specific notifications from other agent activities, you must configure your destination service, such as a Cloud Run functions, to filter the delivered event payload.

  1. Create an Eventarc trigger with the attribute `proactive=true` and the event type `google.cloud.geminicloudassist.task.v1.completed`.
  2. Configure your code to inspect the `title` field in the delivered event data. Cost investigations include the string "Cost Anomaly" or "Cost Optimization" in the title.



For a technical integration guide, see [Automate Proactive Agent activities](https://docs.cloud.google.com/cloud-assist/proactive-agents-tasks).

## What's next

  * Learn about [agent identity](https://docs.cloud.google.com/cloud-assist/proactive-agents-concepts).
  * Learn how to [set up Proactive Mode](https://docs.cloud.google.com/cloud-assist/proactive-agents-setup).
  * Review [IAM requirements](https://docs.cloud.google.com/cloud-assist/iam-requirements) for optimization.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
