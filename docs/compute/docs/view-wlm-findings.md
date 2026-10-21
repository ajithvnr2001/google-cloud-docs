---
url: https://docs.cloud.google.com/compute/docs/view-wlm-findings/
title: View Workload Manager rule findings \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:50:53.787943+00:00
---

# View Workload Manager rule findings  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/view-wlm-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View Workload Manager rule findings Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Viewing Workload Manager rule findings in Compute Engine lets you identify configuration risks and best practice violations across your virtual machine (VM) fleet directly within your daily infrastructure management workflows.

This page describes how to view Workload Manager rule findings on the Compute Engine **Overview** page.

To learn more about Workload Manager rule findings, see [About Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings).

## Before you begin

Before you view Workload Manager rule findings, ensure that you meet the following prerequisites:

  * You have the required roles and permissions.
  * You have enabled Workload Manager for your project.
  * You have created and run at least one evaluation with the **Share findings** option enabled. For more information, see Create an evaluation.



### Required roles

To get the permissions that you need to view Workload Manager rule findings in Compute Engine, ask your administrator to grant you the following IAM roles on your project: 

  * View the Compute Engine Overview page: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * View Workload Manager findings: [Workload Manager Evaluation Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationViewer) (`roles/workloadmanager.evaluationViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view Workload Manager rule findings in Compute Engine. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view Workload Manager rule findings in Compute Engine:

  * View the Compute Engine Overview page: `compute.projects.get`
  * View Workload Manager findings: `workloadmanager.findings.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Workload Manager roles, see [Workload Manager IAM roles and permissions](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles).

### Enable Workload Manager

If you haven't enabled Workload Manager for your project, the **Workload Manager findings** tile on the Compute Engine **Overview** page prompts you to enable the service. Activating the service lets you view configuration risks and compliance violations directly on the **Overview** page.

To enable Workload Manager from the Compute Engine **Overview** page, do the following:

  1. In the Google Cloud console, go to the Compute Engine **Overview** page.

[Go to Overview](https://console.cloud.google.com/compute/overview)

  2. Locate the **Workload Manager findings** tile.

  3. Click **Activate Workload Manager**.




Alternatively, you can enable the Workload Manager API directly. For more information, see [Enable Workload Manager](https://docs.cloud.google.com/workload-manager/docs/enable).

### Create an evaluation

If you haven't created or received shared evaluations in Workload Manager for your project, the **Workload Manager findings** tile prompts you to create an evaluation. To generate rule findings for your resources, you must create and run an evaluation.

To create an evaluation from the Compute Engine **Overview** page, do the following:

  1. In the Google Cloud console, go to the Compute Engine **Overview** page.

[Go to Overview](https://console.cloud.google.com/compute/overview)

  2. Locate the **Workload Manager findings** tile.

  3. Click **Create evaluation**.

  4. Follow the prompts to configure and run your evaluation. For detailed instructions, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation).




## Interpret rule findings

The **Workload Manager findings** tile displays aggregated rule findings for your resources. The tile categorizes findings by severity level and impact category to help you prioritize remediation efforts.

### Severity levels

When you run an evaluation, Workload Manager evaluates resources by comparing their current state with best practices. If a resource doesn't comply with a selected best practice, Workload Manager assigns it a severity level that indicates how far the resource is out of compliance. The Google Cloud console marks each non-compliant resource with an icon. The following table explains these icons, their corresponding severity levels, how the current resource setting might impact your workload, and recommendations for modifying the resource to adhere to best practices. Icon | Severity level | Impacts | Recommendation  
---|---|---|---  
![](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg) | Critical | System Reliability, Unplanned Outages, Unsupported Configuration |  Resolve as soon as possible to prevent an impact on system availability and data integrity due to a high risk of an unplanned outage.  
![](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg) | High | Degraded Performance, System Stability | Resolve during the next planned maintenance window.  
![](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg) | Medium | Suboptimal Performance, Supportability | Resolve at your earliest convenience.  
![](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg) | Low | Informational, Non-essential Behavior | Although there's no resolution needed, reviewing this best practice can provide useful insights.  
  
### Impact categories

The following table describes the impact categories used to classify Workload Manager findings: Category | Description  
---|---  
Reliability | Findings related to workload availability, fault tolerance, and backup configurations.  
Security | Findings related to access controls, encryption, and compliance with best practices for security.  
Performance | Findings related to resource utilization, latency, and system optimization.  
Cost | Findings related to underutilized resources and opportunities to optimize operational expenses.  
  
## View detailed findings

To view details of specific rule findings, you can navigate from the **Workload Manager findings** tile on the Compute Engine **Overview** page directly to the Workload Manager dashboard.

To view detailed rule findings in Workload Manager:

  1. In the Google Cloud console, go to the **Overview** page.

[Go to Overview](https://console.cloud.google.com/compute/overview)

  2. Click **View all findings** or select a specific severity level to open the Workload Manager **Rule findings** tab.

  3. In the findings table, click the name of a specific finding to view its description, affected resources, and recommended remediation steps.




## Troubleshoot

For help with diagnosing and resolving issues related to Workload Manager evaluations, see [Troubleshoot Workload Manager evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/troubleshooting).

## What's next

  * Learn more about [Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings).
  * Learn how to [create and run a Workload Manager evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation).
  * Review [Workload Manager best practices](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
