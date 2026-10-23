---
url: https://docs.cloud.google.com/gemini/docs/deprecations/permissions/
title: Deprecated IAM permissions \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:27.650122+00:00
---

# Deprecated IAM permissions  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/deprecations/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Resources ](https://docs.cloud.google.com/gemini/docs/resources)



Send feedback 

#  Deprecated IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

The following Identity and Access Management (IAM) permissions are deprecated as of February 1, 2026:

  * `cloudaicompanion.companions.generateChat`
  * `cloudaicompanion.companions.generateCode`



If you have any [custom IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom) that contain these permissions for controlling access to the Gemini for Google Cloud API, you should replace those permissions with the following permissions:

  * `cloudaicompanion.instances.completeCode`
  * `cloudaicompanion.instances.completeTask`
  * `cloudaicompanion.instances.generateCode`
  * `cloudaicompanion.instances.generateText`



For information about updating custom roles, see [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
