---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation/
title: Create and run an evaluation \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:14.763017+00:00
---

# Create and run an evaluation  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Create and run an evaluation Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create an evaluation for your workload in Workload Manager.

### Limitations

Workload Manager supports only 25 evaluations per project to run simultaneously every 1 hour. If you have more than 25 evaluations, it is recommended that you limit the total number of evaluations running every 1 hour to 25, or reduce the frequency of evaluation to every 6 hours or less.

### Create a workload evaluation

To create a workload evaluation, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[ Go to Workload Manager](https://console.cloud.google.com/workloads?walkthrough_id=workload-manager--create-evaluation)   
school The remaining steps appear in the Google Cloud console. 

  2. Select a Google Cloud project.
  3. If prompted, to enable the required API for Workload Manager, click **Enable**.
  4. Click **New evaluation**.
  5. In the **Name & rules** pane, do the following: 
     1. For **Evaluation name** , enter a name for the workload evaluation.
     2. For **Description** , enter a description for the workload evaluation.
     3. In the **Workload type** field, select the type of workload evaluation.
     4. From the **Rules table** , select the best practices to include in the workload evaluation.
  6. Click **Continue**.
  7. In the **Scope & filters** pane, do the following: 
     1. In the **Evaluation scope** section, click **Browse projects** to add the projects that contain the resources that you want to evaluate.
     2. Optional: To share rule findings across target projects, select the **Share findings** checkbox.
     3. In the **Apply filters to resources** section, click **Add filter** , and then use the following types of filters to select specific resources from the selected projects: 
        * Service agent
        * Label
        * Name

Multiple filters in a filter type use `OR` logic. Across filter types, `AND` logic is used.

  8. Click **Continue**.
  9. In the **Frequency & notification** pane, do the following: 
     1. In the **Scheduling** section, choose how frequently you want the evaluation to run.
     2. Optional: In the **Notification** section, select the events that you want to receive alerts for.
  10. Click **Continue**.
  11. In the **Review** pane, review the workload evaluation. To make any final changes on any page, click the page name on the left pane.
  12. Click **Create**.



### Run a workload evaluation

To run a workload evaluation, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[ Go to Workload Manager](https://console.cloud.google.com/workloads?walkthrough_id=workload-manager--create-evaluation)   
school The remaining steps appear in the Google Cloud console. 

  2. Click the **Evaluation name**.
  3. On the **Evaluation information** page, click **Run**. 

A workload evaluation takes a few minutes to complete. There might be evaluations that aren't completely real-time due to the time it takes for an evaluation to complete.




### Share evaluation findings

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Sharing evaluation findings lets resource owners in target projects view configuration findings for their resources in their local project consoles and on integrated pages such as Compute Engine, without requiring direct Identity and Access Management (IAM) access to the consumer project.

#### Required roles

To get the permissions that you need to share evaluation findings, ask your administrator to grant you the following IAM roles: 

  * Workload Manager Evaluation Administrator (`roles/workloadmanager.evaluationAdmin`) on the consumer project
  * Workload Manager Evaluation Administrator (`roles/workloadmanager.evaluationAdmin`) on the target project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to share evaluation findings. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to share evaluation findings:

  * `workloadmanager.evaluations.create` on the consumer project
  * `workloadmanager.evaluations.update` on the consumer project
  * `workloadmanager.findings.create` on the target project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Edit an evaluation to share findings

To enable or disable sharing findings for an existing evaluation, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page and then click **Evaluations**.

[ Go to Workload Manager](https://console.cloud.google.com/workloads)

  2. Click the name of the evaluation that you want to edit.
  3. Click **Edit**.
  4. In the **Scope & filters** section, select or clear the **Share findings** checkbox.
  5. Click **Save**.



#### Visibility of shared findings

When you enable **Share findings** , Workload Manager propagates rule findings to all target projects specified in the evaluation scope. Findings are visible in the **Rule findings** tab and on integrated pages like the Compute Engine **Overview** page.

When you disable **Share findings** , rule findings are no longer propagated to target projects and remain visible only within the consumer project.

### Set alerts for evaluations

To set alerts for existing evaluations, do the following:

  1. In the Google Cloud console, go to the **Workload Manager** page and then click **Evaluations**.

[ Go to Workload Manager](https://console.cloud.google.com/workloads?walkthrough_id=workload-manager--create-evaluation)   
school The remaining steps appear in the Google Cloud console. 

  2. click the name of the evaluation for which you want to enable notifications.
  3. Click **Edit**.
  4. Select the **Notification** section. 
  5. Select the events for which you want to receive alerts, and then select [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options#creating_channels).
  6. Click **Save**. 



## What's next

  * [About Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings)
  * [View Workload Manager rule findings in Compute Engine](https://docs.cloud.google.com/compute/docs/view-wlm-findings)
  * [View evaluation results and history](https://docs.cloud.google.com/workload-manager/docs/evaluate/view-evaluation-results)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
