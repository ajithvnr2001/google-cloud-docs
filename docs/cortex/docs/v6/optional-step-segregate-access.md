---
url: https://docs.cloud.google.com/cortex/docs/v6/optional-step-segregate-access/
title: Using different projects to segregate access \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:21.091224+00:00
---

# Using different projects to segregate access  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/optional-step-segregate-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using different projects to segregate access

This page describes an optional step to segregate access using different projects within the Cortex Framework Data Foundation, the core of Cortex Framework.

You might choose to have different projects for different functions to keep users from having excessive access to some data. However, using two different projects is optional. A single project can be used to deploy all datasets. The Cortex Framework Data Foundation deployment lets you use [two projects](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-one#projects), one for processing replicated data, where only technical users have access to the raw data, and another for reporting, where business users can query the predefined models or views.

![Segregation of projects ](https://docs.cloud.google.com/cortex/docs/images/segregate-access.png)

**Figure 1**. Segregation of projects flow example.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
