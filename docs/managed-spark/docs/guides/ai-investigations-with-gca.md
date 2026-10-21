---
url: https://docs.cloud.google.com/managed-spark/docs/guides/ai-investigations-with-gca/
title: Investigate workloads with AI-powered Gemini Cloud Assist \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:29.280165+00:00
---

# Investigate workloads with AI-powered Gemini Cloud Assist  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/ai-investigations-with-gca/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Investigate workloads with AI-powered Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Overview

The Gemini Cloud Assist Investigations preview feature uses Gemini advanced capabilities to assist in creating and running Managed Service for Apache Spark batch workloads. This feature analyzes failed and slow-running workloads to identify root causes and recommend fixes. It creates persistent analysis that you can review, save, and share with Google Cloud support to facilitate collaboration and accelerate issue resolution. 

## Features

Use this feature to create investigations from the Google Cloud console:

  * Add a natural language context description to an issue before creating an investigation. 
  * Analyze failed and slow batch workloads.
  * Get insights into issue root causes with recommended fixes.
  * Create Google Cloud support cases with the full investigation context attached.



## Before you begin

Enable the Gemini Cloud Assist API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=geminicloudassist.googleapis.com)

## Start an investigation

To start an investigation, do one of the following:

  * Option 1: In the Google Cloud console, go to the [**Batches List Page**](https://console.cloud.google.com/dataproc/batches). For any batch with a `Failed` status, an **INVESTIGATE** button appears in the **Insights by Gemini** column. Click the button to start an investigation.

![Batches list page showing the INVESTIGATE button.](https://docs.cloud.google.com/static/managed-spark/docs/images/investigate-button-batches-list.png)
  * Option 2: Open the **Batch Details Page** of the batch workload to investigate. For both `Succeeded` and `Failed` batch workloads, in the **Health overview** section of the **Summary** tab, an **INVESTIGATE** button appears in the **Insights by Gemini** panel. Click the button to start an investigation.

![Batch details page showing the INVESTIGATE button in the Insights by Gemini column for failed jobs.](https://docs.cloud.google.com/static/managed-spark/docs/images/investigate-from-batch-details.png)

The investigation button text indicates the status of the investigation:

    * **INVESTIGATE:** No investigation has been run for this batch. Click the button to start an investigation.
    * **VIEW INVESTIGATION:** An investigation has been completed. Click the button ` to view the results.
    * **INVESTIGATING:** An investigation is in progress.



## View investigation results

Once an investigation is complete, the **Investigation details** page opens. This page contains the full Gemini analysis, which is organized into the following sections:

  * **Issue** : A collapsed section containing auto-populated details of the batch workload being investigated
  * **Relevant Observations** : A collapsed section that lists key data points and anomalies that Gemini found during its analysis of logs and metrics
  * **Hypotheses** : This is the primary section, which is expanded by default. It presents a list of potential root causes for the observed issue. Each hypothesis includes: 
    * **Overview** : A description of the possible cause, such as "High Shuffle Write Time and Potential Task Skew."
    * **Recommended Fixes** : A list of actionable steps to address the potential issue.



## Take action

After reviewing the hypotheses and recommendations, you can take the following actions:

  * Apply one or more of the suggested fixes to the job configuration or code, and then rerun the job.

  * Provide feedback on the helpfulness of the investigation by clicking the thumbs-up or thumbs-down icons at the top of the panel.




## Review and escalate investigations

The results of a previously run investigation can be reviewed by clicking the investigation name on the **Cloud Assist Investigations** page to open the **Investigation details** page.

If you need further assistance, you can open a Google Cloud support case. This process provides the support engineer with the complete context of the previously performed investigation, including the observations and hypotheses generated by Gemini. This context sharing significantly reduces the need for clarifying communications with the support team, and leads to faster case resolution.

To create a support case from an investigation, in the **Investigation details** page, click **Request support**.

**Note:** You can click **Open chat** to start a conversation and ask clarifying questions about investigation results before opening a support case.

### Preview status and pricing

There is no charge for Gemini Cloud Assist investigations during public preview. Charges will apply to the feature when it becomes [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

For more information about pricing after general availability, see [Gemini Cloud Assist Pricing](https://cloud.google.com/products/gemini/pricing#gemini-cloud-assist-pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
