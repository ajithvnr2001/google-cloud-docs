---
url: https://docs.cloud.google.com/bigtable/docs/investigate-performance-with-ai/
title: Investigate performance issues with AI assistance \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:23.647678+00:00
---

# Investigate performance issues with AI assistance  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/investigate-performance-with-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Investigate performance issues with AI assistance

**Important** : As of April 10, 2026, you can create, run, and edit [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) only if you have a [Premium Support contract](https://cloud.google.com/support/premium). If you ran an investigation prior to April 10, 2026, then the results of the investigation continue to be available to you in the Google Cloud console.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use AI assistance to help you investigate performance anomalies in your Bigtable resources. You can use the AI-assisted troubleshooting tools of Bigtable and [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) to [investigate performance anomalies](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring). 

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Before you begin

[Ensure that Gemini Cloud Assist is set up for your Google Cloud user account and project](https://docs.cloud.google.com/cloud-assist/set-up-gemini). 

After you set up Gemini Cloud Assist, the service can take a few minutes to propagate. Wait for propagation to complete before you enable AI-assisted troubleshooting in Bigtable.

### Required roles and permissions

To get the permissions that you need to observe and troubleshoot using Gemini Cloud Assist, ask your administrator to grant you the following IAM roles on your project: 

  * View monitoring dashboards and metrics: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
  * Read Bigtable data: [Bigtable Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigtable#bigtable.reader) (`roles/bigtable.reader`) 
  * View database performance issues: [Database Insights Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`) 
  * Use Gemini Cloud Assist investigations: [Gemini Cloud Assist Investigation Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationOwner) (`roles/geminicloudassist.investigationOwner`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about required roles and permissions for using Gemini Cloud Assist investigations, see [Troubleshoot issues with Gemini Cloud Assist Investigations](https://docs.cloud.google.com/cloud-assist/investigations#consideration).

## Open Gemini Cloud Assist

To use Gemini Cloud Assist with Bigtable, do the following:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. To open an instance, click the instance name. 
  3. To open the **[Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel)** , click auto_awesome**Open or close Gemini Cloud Assist chat**.
  4. In the **Cloud Assist panel** , enter a prompt that describes the information that you're interested in.
  5. After you enter the prompt, click send **Send prompt**. 

Gemini returns a response to your prompt based on information from the last hour.




## Investigate performance issues

When you observe a spike or increase in metrics such as CPU utilization or latency, you can use investigations to identify the root cause. This process uses AI assistance from Gemini Cloud Assist to analyze your cluster's performance data and provide actionable recommendations.

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

The **Instances** page displays a list of instances.

  2. To open an instance, click the instance name. 

  3. In the navigation menu, click **System insights**.

  4. To troubleshoot your database load, click **Explore Investigations**.

The **Investigation options** pane opens.

  5. In the **Cluster** field, select the cluster for which you want to view the investigation.

  6. From the list of time filters, select the time range for your investigation or provide a custom date and time for your filter.

  7. Click **Investigate**.

  8. After a few minutes, the **Investigation Overview** pane opens with the following sections:

     * **Issue** : a description of the issue being investigated, including the investigation start and stop time.
     * **Findings** : a list of observations about the issue. For example, these can include client misconfiguration details, such as an incorrect channel pool size.
     * **Hypotheses** : a list of AI-recommended actions to take to help address the anomalies.



### How investigations analyze your database

When you start an investigation, Gemini Cloud Assist analyzes performance data for the time period you selected. It compares your baseline aggregated data against the following metrics:

  * Client latencies
  * Server latencies
  * CPU utilization
  * Disk utilization
  * Request count



When Gemini Cloud Assist completes the analysis and detects a significant change, the investigation identifies a possible root cause and lists actionable insights in the **Hypotheses** section of the **Investigation details** pane to help remediate the issue.

For some situations, depending on the analysis, there might not be a recommendation.

## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn how to use the [Gemini Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel).
  * Read [Use Gemini for AI assistance and development](https://docs.cloud.google.com/gemini/docs/overview)
  * Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

  * If you want to continue troubleshooting or get more assistance with system performance, see [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview).
  * [Troubleshoot latency](https://docs.cloud.google.com/bigtable/docs/latency).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
