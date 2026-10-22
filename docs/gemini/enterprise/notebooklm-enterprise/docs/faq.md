---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/faq/
title: FAQs about Gemini Notebook Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:55.180740+00:00
---

# FAQs about Gemini Notebook Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)



Send feedback 

#  FAQs about Gemini Notebook Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

This page provides answers to frequently asked questions (FAQs) about Gemini Notebook Enterprise.

## Can I move my notebooks to a different organization?

No, you can't directly transfer or share notebooks between different Google Cloud organizations. To move your data, you need to manually export your notebooks and sources from one organization and then import them into an account in the other organization. For more information, see [Share notebooks](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks).

## Can I use my Gemini Notebook Plus notebooks with Gemini Notebook Enterprise?

No, Gemini Notebook Plus is designed for Google Workspace and isn't a Google Cloud product. Your existing Gemini Notebook Plus notebooks can't be used or directly accessed in Gemini Notebook Enterprise or Gemini Enterprise.

## Can I enable Nano Banana in Gemini Notebook Enterprise ?

No, Nano Banana isn't supported in Gemini Notebook Enterprise.

## Does Model Armor support data masking or de-identification in Gemini Notebook Enterprise?

No. Model Armor does not support data de-identification or masking in Gemini Notebook Enterprise. If a prompt or response triggers a configured Sensitive Data Protection detector and the enforcement type is **Inspect and block** , Gemini Notebook Enterprise blocks the request or response rather than de-identifying it. For more information, see [Considerations when using Model Armor](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/enable-model-armor#considerations).

## Why can't I add a website URL as a source in Gemini Notebook Enterprise?

If your project is protected by [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), adding public or external website URLs as notebook sources is disabled.

Adding a website URL as a source performs a live crawl of the public web, which generates outbound network traffic outside Google networks. Because VPC Service Controls blocks outbound network traffic to maintain security and compliance, direct website ingestion is blocked for VPC Service Controls-protected projects.

Other source types, such as Google Drive documents and YouTube video links, remain supported. YouTube video links remain supported because YouTube transcripts are retrieved using an internal service rather than live public web crawling.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
