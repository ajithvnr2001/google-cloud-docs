---
url: https://docs.cloud.google.com/bigquery/docs/prompt-analytics-opt-out/
title: Opt out from prompt analytics \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:45:32.398559+00:00
---

# Opt out from prompt analytics  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/prompt-analytics-opt-out/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Opt out from prompt analytics

To improve the quality, accuracy, and reliability of conversational analytics, Google analyzes anonymized prompt data across customer interactions. This data helps identify common usage patterns, detect gaps in comprehension, and improve overall product performance. This data isn't used to train or fine tune Google's foundational AI models. This data processing is enabled by default.

To opt out from prompt analytics, do one of the following:

  * To opt out _before_ November 23, 2026, complete the following steps: 
    1. Use the Resource Manager API, CLI, or the Google Cloud console to obtain project numbers, or find your organization ID to opt out all existing BigQuery projects in an organization. 
    2. Submit the [opt-out form](https://docs.google.com/forms/d/e/1FAIpQLSc3Jtc0cM2t2HXcyN_yRQJ0xVm3giGDCXvHft_l1jid_Jp7tw/viewform), including the project IDs that you want to exclude. 
  * To opt out _on or after_ November 23, 2026, apply the custom, hierarchical Organization Policy Service constraint `constraints/gcp.disablePromptAnalytics` to block prompt ingestion at the Organization, Folder, or Project level. 



You can re-enable prompt analytics within the Google Cloud console administrator settings. You must remove the custom Organization Policy Service constraint if you previously applied it.

To learn more, see [ Service Specific Terms](https://cloud.google.com/terms/service-terms) for BigQuery conversational analytics.

## What's next

  * [Learn about conversational analytics in BigQuery](https://docs.cloud.google.com/bigquery/docs/conversational-analytics).
  * [Create data agents](https://docs.cloud.google.com/bigquery/docs/create-data-agents).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
