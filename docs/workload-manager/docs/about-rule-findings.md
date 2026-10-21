---
url: https://docs.cloud.google.com/workload-manager/docs/about-rule-findings/
title: About Workload Manager rule findings \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:09:41.140479+00:00
---

# About Workload Manager rule findings  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/about-rule-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  About Workload Manager rule findings Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use rule findings in Workload Manager to identify configuration risks and best practice violations across your cloud resources. By reviewing aggregated findings from your workload evaluations across Google Cloud projects, you can proactively resolve issues to maintain the reliability, security, and performance of your workloads.

This page provides an overview of Workload Manager rule findings, explains how Workload Manager aggregates findings across projects, and describes their severity levels and impact categories.

## Key benefits

  * **Fleet-wide visibility** : aggregate findings across multiple projects in a centralized view without needing to inspect evaluations individually.
  * **Contextual integration** : access rule findings directly within daily workflows, such as on the Compute Engine **Overview** page.
  * **Actionable remediation** : review detailed descriptions, affected resources, and recommended steps to remediate misconfigurations before they cause system outages or security issues.
  * **Cross-project sharing** : share rule findings across projects so that resource owners can view compliance data without requiring access to the central consumer project.



## Rule-based evaluation and findings

When you create and run an evaluation in Workload Manager, the service scans specified resources in target projects against curated Google best practices or custom rules.

When an evaluation detects deviations from best practices, Workload Manager generates rule findings, aggregates them across projects, and categorizes them by severity level and impact category.

### Multi-project aggregation

In complex environments with multiple Google Cloud projects, managing evaluations project-by-project can lead to fragmented visibility. Workload Manager rule findings support multi-project aggregation:

  * **Consumer project** : the project where you configure, store, and execute the evaluation.
  * **Target projects** : the projects containing the resources that the evaluation scans.



For more information about consumer and target project concepts, see [Consumer and target projects](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles#wlm-projects).

### Cross-project sharing

When configuring a workload evaluation in a consumer project, you can enable the **Share findings** option.

Enabling **Share findings** propagates rule findings to all target projects in the evaluation scope. This feature lets resource owners and DevOps teams view configuration findings for their specific resources in their local project consoles, eliminating the need to grant them direct IAM access to the consumer project.

For instructions on configuring this option, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation).

## Rule findings in the Google Cloud console

In the Google Cloud console, rule findings appear across multiple pages to make compliance and reliability data available where you manage your infrastructure:

  * **Rule findings** tab in Workload Manager: displays a comprehensive, filterable table of all rule findings. You can filter findings by category, severity, or rule name, and click a specific finding to view affected resources and remediation guidance. For instructions, see [View rule findings](https://docs.cloud.google.com/workload-manager/docs/evaluate/view-rule-findings).
  * **Workload Manager findings** tile on the Compute Engine **Overview** page: summarizes top configuration risks across your VM fleet. You can click any severity count to drill down directly into the **Rule findings** tab in Workload Manager.



To learn how to view findings in Compute Engine, see [View Workload Manager rule findings](https://docs.cloud.google.com/compute/docs/view-wlm-findings).

## Severity levels and impact categories

Rule findings categorize each finding by severity level and impact category to help you prioritize remediation efforts.

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
  
## Limitations

The following limitations apply to Workload Manager rule findings:

  * Workload Manager rule findings are only available at the project scope. Workload Manager does not support viewing or aggregating rule findings at the organization and folder levels.
  * If you disable the **Share findings** option for an evaluation, existing rule findings from earlier evaluation runs remain visible in target projects until their default time to live (TTL) retention period expires. Subsequent evaluation runs don't generate or share new rule findings with target projects.



## What's next

  * Learn how to [view Workload Manager rule findings in Workload Manager](https://docs.cloud.google.com/workload-manager/docs/evaluate/view-rule-findings).
  * Learn how to [view Workload Manager rule findings in Compute Engine](https://docs.cloud.google.com/compute/docs/view-wlm-findings).
  * Learn how to [create and run a Workload Manager evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation).
  * Review [Identity and Access Management (IAM) roles and permissions for evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles).
  * Review [Workload Manager best practices](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
