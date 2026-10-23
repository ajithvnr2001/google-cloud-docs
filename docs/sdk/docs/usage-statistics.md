---
url: https://docs.cloud.google.com/sdk/docs/usage-statistics/
title: Usage statistics \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:24.772515+00:00
---

# Usage statistics  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/usage-statistics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Resources ](https://docs.cloud.google.com/sdk/docs/resources)



Send feedback 

#  Usage statistics Stay organized with collections  Save and categorize content based on your preferences. 

Unless you opt-in during Google Cloud CLI installation, gcloud CLI software **does not** collect usage statistics. You can help Google to prioritize gcloud CLI features and improvements by permitting gcloud CLI to send usage statistics to Google. 

Usage statistics contain anonymized [Google Cloud CLI](https://docs.cloud.google.com/sdk/cloudplatform) tool executions, including e.g. the command that was invoked, the time taken, whether an error was raised, and other such metrics. Usage statistics don't include argument values or any personal information. 

You can change whether usage statistics are sent to Google at any time. To _disable_ sending usage statistics, run the following command after you've installed gcloud CLI: 
    
    
    gcloud config set disable_usage_reporting true

To _enable_ sending usage statistics, run the following command: 
    
    
    gcloud config set disable_usage_reporting false

For more information about `gcloud config`, see the [gcloud CLI guide](https://docs.cloud.google.com/sdk/gcloud#configurations). 

Usage statistics are handled in accordance with Google's [privacy policy](https://policies.google.com/privacy). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
