---
url: https://docs.cloud.google.com/cloud-assist/deprecations/permissions/
title: Deprecated IAM permissions \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:31.954598+00:00
---

# Deprecated IAM permissions  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/deprecations/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Resources ](https://docs.cloud.google.com/cloud-assist/resources)



Send feedback 

#  Deprecated IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

The following Identity and Access Management (IAM) permission is deprecated and shut down for Gemini Cloud Assist as of April 8, 2026:

  * `cloudaicompanion.instances.completeTask`

**Important:** This permission is deprecated for Gemini Cloud Assist only. Other products, such as [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview) and [Gemini in BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-overview) might still require the use of this permission.

If you have any [custom IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom) that contain this permission for controlling access to Gemini Cloud Assist, you should add the following permission to those custom roles:

  * `geminicloudassist.agents.invoke`



For information about updating custom roles, see [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

If your custom IAM roles use the `cloudaicompanion.instances.completeTask` permission for controlling access to other Gemini products in Google Cloud, you should retain this permission in your custom role. If your custom IAM roles are only used to control access to Gemini Cloud Assist, you can remove the `cloudaicompanion.instances.completeTask` permission from those IAM roles.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
