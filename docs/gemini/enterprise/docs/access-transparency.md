---
url: https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency/
title: Enable Access Transparency \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:43.691596+00:00
---

# Enable Access Transparency  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Enable Access Transparency Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the support that [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) provides for Gemini Enterprise.

## Overview

Access Transparency provides you with logs that capture the actions that Google personnel take when accessing your content.

Similar to the way audit logs show when members of your organization access content in your Google Cloud projects, Access Transparency [logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs) show when Google personnel take action.

## Limitations of Access Transparency in Gemini Enterprise

All access to your data in Gemini Enterprise by Google personnel is logged, except for the following:

  * **Multi-region data stores:** You must use multi-region data stores and apps (not global ones). For more information about multi-regions, including limits associated with using non-global locations, see [Gemini Enterprise locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

  * **Data associated with preview features:** In the documentation, preview features are marked with disclaimers. In the Google Cloud console, preview features have preview labels.

  * **Search analytics:** Access Transparency logs do not record when Google personnel view or take action on your analytics data. For general information about analytics, including how to create a search app where analytics is disabled, see [View analytics](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics).




## Enable Access Transparency

To enable Access Transparency for a Google Cloud project, do the following:

  1. Confirm that the project resides in an organization. Only projects in organizations can use Access Transparency.

  2. Follow the instructions in [Enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable).




## What's next

  * Learn about the [content of Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs).

  * Learn [when you might want to use Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview#when-to-use).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
