---
url: https://docs.cloud.google.com/logging/docs/view/summarize-log-entries-gemini/
title: Summarize log entries with Gemini assistance \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:32.854120+00:00
---

# Summarize log entries with Gemini assistance  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/view/summarize-log-entries-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Summarize log entries with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview), a key product in the Gemini for Google Cloud portfolio, to summarize a log entry in Cloud Logging. When you are investigating an issue, log entry summaries can help you to interpret activity in a log.

This documentation assumes that your Google Cloud project already [collects the log data](https://docs.cloud.google.com/logging/docs/agent-or-library) that you want to explore.

**Note:** Gemini Cloud Assist can store data in any Google Cloud data center globally. Don't enable the [Gemini Cloud Assist API](https://docs.cloud.google.com/gemini/docs/discover/certifications#cloud-assist-security) for projects that have a data residency or [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/cmek) requirement.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

  1. [Ensure that Gemini Cloud Assist is set up for your Google Cloud user account and project](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

  2. In the Google Cloud console, on the project selector page, select your Google Cloud project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)




## Summarize a log entry

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

Logging sends only the text of a log entry to Gemini Cloud Assist, so responses are based only on that text and don't include context from other log entries or other resources in your Google Cloud project.

To have Gemini Cloud Assist generate a summary of a log entry, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Find the log entry that you want to review. To find a specific log entry, try the following:

     * Specify criteria that the log entries must match by selecting from the menus or by writing a [query](https://docs.cloud.google.com/logging/docs/view/building-queries).
     * Adjust the time range by using the time range picker.
     * Select the projects and log views that are searched for log data.

The projects and log views in the default log scope are automatically searched for log data. However, you can [specify which projects and log views are searched](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope).

  3. Select the log entry that you want to summarize.

  4. In the toolbar for the log entry, click **Investigate log**.

Cloud Logging sends the text of the log entry to Gemini Cloud Assist with a prompt to summarize the contents of the log entry. Gemini Cloud Assist responds with a generated summary in the **Cloud Assist** pane. The summary is based only on the text of the log entry without any additional context.




## What's next

  * Read the [Gemini Cloud Assist overview](https://docs.cloud.google.com/cloud-assist/overview).
  * Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

  * Learn about [querying and viewing log data](https://docs.cloud.google.com/logging/docs/log-analytics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
