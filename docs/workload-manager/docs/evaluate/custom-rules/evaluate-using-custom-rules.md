---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/evaluate-using-custom-rules/
title: Evaluate your workloads using custom rules \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:53.490902+00:00
---

# Evaluate your workloads using custom rules  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/evaluate-using-custom-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Evaluate your workloads using custom rules Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use custom rules in Workload Manager to evaluate your workloads against best practices recommended for your organization.

For more information, see [About custom rules in Workload Manager](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/about-custom-rules).

## Before you begin

  * [Create custom rules using Rego](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/rego-custom-rules) and upload rules to a Cloud Storage bucket.
  * Enable the following APIs in your Google Cloud project where you create and run the evaluation: 
    * Service Usage API
    * Cloud Monitoring API



### Required roles

For more information about the required IAM roles, see [required permissions to create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/roles#summary_of_required_permissions_to_create_and_run_an_evaluation).

## Evaluate workloads using custom rules

To create a workload evaluation using custom rules, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

Go to [Workload Manager](https://console.cloud.google.com/workload-manager)

  2. Select a Google Cloud project.

  3. If prompted, to enable the required API for Workload Manager, click **Enable**.

  4. Click add**New evaluation**.

  5. In the **Name & rules** pane, do the following:

     1. For **Evaluation name** , enter a name for the workload evaluation.
     2. For **Workload type** , select **Custom**.
     3. Optional: Select the Cloud Storage bucket containing the custom rules.

You can use the sample rules available in the [GoogleCloudPlatform/workload-manager](https://github.com/GoogleCloudPlatform/workload-manager) GitHub repository or build your own rules and upload them to the Cloud Storage bucket. For more information, see [Write custom rules using Rego](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/rego-custom-rules).

     4. From the **Rules table** , select the custom rules you want to validate the selected resources against.

  6. In the **Scope & filters** pane, select the resources that you want to include in the evaluation.

     1. Click **Browse scopes** and select the organizations, folders, or projects in which you want to run the evaluation.
     2. Optional: In the **Apply filters to resources** section, use filters to only select specific resources.
     3. In the **Location for evaluation data** section, select the **Regions** where you want Workload Manager to store the evaluation data.
  7. Click **Continue**.

  8. In the **Frequency & notification** section, do the following:

     1. Optional: To export evaluation results to a BigQuery dataset, select **Save to BigQuery dataset** , and then specify the name of the dataset.

**Note:** Ensure that the BigQuery dataset is regional. Workload Manager doesn't support exporting data to multi-region datasets. You must also create and use a dataset in the same region as the one you selected for evaluation in the previous step. If your organization uses a [Resource Location Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) policy, then create a BigQuery dataset in one of the allowed regions and [Workload Manager supported regions](https://docs.cloud.google.com/workload-manager/docs/evaluate/locations).
     2. Optional: To create a separate table for each evaluation, click **Create a new results table for this evaluation**.

     3. Optional: To encrypt evaluation data with customer-managed encryption keys (CMEK), click **Encryption** and provide an encryption key for each region. For more information, see [Enable customer-managed encryption keys for evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/enable-cmek).

  9. Click **Continue**.

  10. In the **Evaluation scope** section, select the resources that you want to include in the evaluation.

     1. Click **Browse scopes** and select the organizations, folders, or projects in which you want to run the evaluation.
     2. Optional: In the **Apply filters to resources** section, use filters to only select specific resources.
  11. Click **Continue**.

  12. In the **Evaluation rules** section, select the custom rules you want to validate the selected resources against.

  13. In the **Scheduling** section, select the frequency at which you want the evaluation to run.

  14. Click **Continue**.

  15. In the **Notifications** section, select the notification channel and select the events for which you want to receive notifications.

  16. Click **Continue**.

  17. Review the evaluation settings, and then click **Create**.




## Run the evaluation

To run a workload evaluation, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

Go to [Workload Manager](https://console.cloud.google.com/workloads?walkthrough_id=workload-manager--create-evaluation).

  2. Click the **Evaluation name**.

  3. On the **Evaluation information** page, click **Run**. A workload evaluation takes a few minutes to complete. There might be evaluations that aren't completely real-time due to the time it takes for an evaluation to complete.




## What's next

  * Learn more [about workload evaluations](https://docs.cloud.google.com/workload-manager/docs/about-evaluations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
