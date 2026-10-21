---
url: https://docs.cloud.google.com/managed-spark/docs/guides/gca-clusters/
title: AI-powered Investigations with Gemini Cloud Assist (Preview) \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:57.160517+00:00
---

# AI-powered Investigations with Gemini Cloud Assist (Preview)  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/gca-clusters/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  AI-powered Investigations with Gemini Cloud Assist (Preview) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Overview

The Gemini Cloud Assist Investigations preview feature uses Gemini advanced capabilities to assist in creating and running Managed Service for Apache Spark clusters and jobs. This feature analyzes failed clusters and failed and slow-running jobs to identify root causes and recommend fixes. It creates persistent analysis that you can review, save, and share with Google Cloud support to facilitating collaboration and accelerate issue resolution.

## Features

Use this feature to create investigations from the Google Cloud console:

  * Add a natural language context description to an issue before creating an investigation.
  * Analyse failed clusters and slow and failed jobs.
  * Get insights into issue root causes with recommended fixes.
  * Create Google Cloud support cases with the full investigation context attached.



## Before you begin

To get started using the Investigation feature, in your Google Cloud project, enable the [Gemini Cloud Assist API](https://console.cloud.google.com/troubleshooting/investigations/list).

## Create an investigation

To create an investigation, do the following:

  1. In the Google Cloud console, go to the **Cloud Assist Investigations** page.

[Cloud Assist Investigations](https://console.cloud.google.com/troubleshooting/investigations/list)

  2. Click add**Create**.

  3. **Describe the issue** : Provide a description of the cluster or job issue.

  4. **Select time range** : Prove a time range when the issue occurred (default is 30 minutes).

  5. **Select resources** :

     1. Click add**Add resource**. 
        1. In the **Quick filters** field, type "dataproc", and then select one or more of `dataproc.Batch`, `dataproc.Job`, or `dataproc.Cluster` as filters.  You can also filter by **Location**.
        2. Select the listed batch, job, or cluster to investigate. You can add multiple resources that are affected by the issue.
  6. Click **Create**.


**Tip:** Gemini Cloud Assist is also accessible through [direct API](https://docs.cloud.google.com/cloud-assist/investigations#entry-points) and other interfaces. You can create investigations for any job from these interfaces.

## Interpret investigation results

Once an investigation is complete, the **Investigation details** page opens. This page contains the full Gemini analysis, which is organized into the following sections:

  * **Issue** : A collapsed section containing auto-populated details of the job being investigated.
  * **Relevant Observations** : A collapsed section that lists key data points and anomalies that Gemini found during its analysis of logs and metrics.
  * **Hypotheses** : This is the primary section, which is expanded by default. It presents a list of potential root causes for the observed issue. Each hypothesis includes: 
    * **Overview** : A description of the possible cause, such as "High Shuffle Write Time and Potential Task Skew."
    * **Recommended Fixes** : A list of actionable steps to address the potential issue.



## Take action

After reviewing the hypotheses and recommendations:

  * Apply one or more of the suggested fixes to the job configuration or code, and then rerun the job.

  * Provide feedback on the helpfulness of the investigation by clicking the thumbs-up or thumbs-down icons at the top of the panel.




## Review and escalate investigations

The results of a previously run investigation can be reviewed by clicking the investigation name on the **Cloud Assist Investigations** page to open the **Investigation details** page.

If further assistance is needed, you can use open a Google Cloud support case. This process provides the support engineer with the complete context of the previously performed investigation, including the observations and hypotheses generated by Gemini. This context sharing significantly reduces the back-and-forth communication required with the support team, and leads to faster case resolution.

To create a support case from an investigation:

In the **Investigation details** page, click **Request support**.

**Note:** You can lick **Open chat** to start a conversation and ask clarifying questions about investigation results before opening a support case.

## Preview status and pricing

There is no charge for Gemini Cloud Assist investigations during public preview. Charges will apply to the feature when it becomes [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

For more information about pricing after general availability, see [ Gemini Cloud Assist Pricing](https://cloud.google.com/products/gemini/pricing#gemini-cloud-assist-pricing).

## What's next

  * [Monitor clusters and jobs](https://docs.cloud.google.com/managed-spark/docs/guides/monitor-clusters-jobs).
  * [Troubleshoot cluster creation issues](https://docs.cloud.google.com/managed-spark/docs/support/troubleshoot-errors).
  * [View cluster diagnostic data](https://docs.cloud.google.com/managed-spark/docs/support/diagnose-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
