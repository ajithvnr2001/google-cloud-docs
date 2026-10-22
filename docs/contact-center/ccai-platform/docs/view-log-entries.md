---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/view-log-entries/
title: View log entries \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:04.042488+00:00
---

# View log entries  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/view-log-entries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  View log entries Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Cloud Logging](https://docs.cloud.google.com/logging/docs) to capture logging data and events for your Google Cloud project. The [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) displays log entries for your project. You can use the `contactcenteraiplatform.googleapis.com/ContactCenter` resource type to filter your results to view only the log entries for CCAI Platform.

## Before you begin

Before you can use the Logs Explorer, your administrator needs to grant you the right IAM role. The role you require depends on your use case. For more information, see [Before you begin](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#before-you-begin) in the Cloud Logging documentation.

## View CCAI Platform log entries

You can filter the results that appear in the Logs Explorer to display only CCAI Platform log entries.

To view CCAI Platform log entries, follow these steps:

  1. In the Google Cloud console, go to the project selector dashboard and select the project that contains your instance.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the navigation menu, click **Logging > Logs explorer**.

[Logs Explorer](https://console.cloud.google.com/logs)

The **Logs Explorer** page appears.

  3. For ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-project.png)**Project logs** , enter `resource.type="contactcenteraiplatform.googleapis.com/ContactCenter"` in the query field, and then click **Run query**. Your CCAI Platform log entries appear.

**Note:** To get query results, you might need to click **Edit time** to adjust the time window.



For more information about using the Logs Explorer, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). For information about CCAI Platform events available in the logs, see [Understanding log entries](https://docs.cloud.google.com/contact-center/ccai-platform/docs/understanding-log-entries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
