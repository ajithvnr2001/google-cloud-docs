---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/view-rule-findings/
title: View Workload Manager rule findings \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:54.469029+00:00
---

# View Workload Manager rule findings  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/view-rule-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  View Workload Manager rule findings Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you evaluate your workloads with Workload Manager, you can view Workload Manager rule findings on the dashboard to identify configuration risks, security vulnerabilities, and best practice deviations across your cloud resources.

This page describes how to view and filter rule findings on the Workload Manager dashboard.

For more information about rule findings, see [About Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings).

## Before you begin

Before you view Workload Manager rule findings, ensure that you meet the following prerequisites:

  * You have [enabled Workload Manager for your project](https://docs.cloud.google.com/workload-manager/docs/enable).
  * You have the required roles and permissions.
  * You have created and run at least one evaluation with the **Share findings** option enabled. For instructions, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation).



### Required roles

To get the permissions that you need to view Workload Manager rule findings, ask your administrator to grant you the following IAM roles on your project: 

  * View rule findings: 
    * [Workload Manager Evaluation Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationViewer) (`roles/workloadmanager.evaluationViewer`)
    * [Workload Manager Evaluation Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view Workload Manager rule findings. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view Workload Manager rule findings:

  * View rule findings: `workloadmanager.findings.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles in consumer and target projects, see [IAM roles in consumer and target projects for evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles).

## View and filter rule findings

To view and filter Workload Manager rule findings in the Google Cloud console:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager/evaluations)

  2. Click the **Rule findings** tab.

  3. Optional: To filter the findings, use any of the following controls above the table:

     * **Category** : filter by [impact category](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings#impact-categories), such as **Reliability** , **Security** , **Performance** , or **Cost**.
     * **Severity** : filter by [severity level](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings#severity-levels), such as Critical, High, Medium, or Low.
     * **Workload type** : filter by workload type, such as SAP or Oracle.
     * **Filter bar** : search by properties or keywords (for example, rule names or resource names).
     * **Reset filters** : clear all active filters.
  4. In the findings table, review the evaluated findings. The table displays the following columns:

     * **Rule name** : the name of the evaluated best practice rule.
     * **Category** : the [impact category](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings#impact-categories) of the rule finding.
     * **Resource** : the cloud resource that the rule evaluated.
     * **Issues** : the number of detected issues for the resource.
     * **Severity** : the [severity level](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings#severity-levels) of the finding.
     * **Evaluation ID** : the name of the evaluation that generated the finding.
     * **Source** : the project that contains the evaluated resource.



## What's next

  * Learn more about [Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings).
  * Learn how to [create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation).
  * Learn how to [view evaluation results and history](https://docs.cloud.google.com/workload-manager/docs/evaluate/view-evaluation-results).
  * Learn how to [view Workload Manager rule findings in Compute Engine](https://docs.cloud.google.com/compute/docs/view-wlm-findings).
  * Review [Identity and Access Management (IAM) roles and permissions for evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles).
  * Review [Workload Manager best practices](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
