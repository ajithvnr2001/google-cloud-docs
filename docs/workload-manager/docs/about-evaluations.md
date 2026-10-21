---
url: https://docs.cloud.google.com/workload-manager/docs/about-evaluations/
title: About Workload Manager Evaluation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:20.731134+00:00
---

# About Workload Manager Evaluation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/about-evaluations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  About Workload Manager Evaluation Stay organized with collections  Save and categorize content based on your preferences. 

Workload Manager uses a rule-based evaluation service to scan your workloads and to detect deviations from standards, rules, and best practices to improve system quality, reliability, and performance.

Workload Manager checks the state of your resources against up-to-date best practices for infrastructure, operating systems, and critical high-availability configurations. For identified issues, Workload Manager provides guidance to help you understand and resolve issues.

You can use Workload Manager to perform a one-time check or for ongoing evaluation of workloads that might drift after system upgrades or other operational activities.

## Summary of benefits

  * **Improve system quality:** Workload Manager provides initial and ongoing evaluation of infrastructure configuration, high-availability setup, and operating system configurations to help you improve workload reliability and prevent issues before they impact your business-critical applications.

  * **Lower operational overhead:** Workload Manager provides at scale validation to provide confidence in your deployments and automate operational processes for detecting configuration drift.

  * **Save time during troubleshooting:** Workload Manager automates configuration checks to help you identify causes of issues affecting workload performance or reliability.




## Supported workloads

Workload Manager supports evaluating the following workloads:

  * SAP
  * Microsoft SQL Server
  * Oracle
  * MySQL
  * Redis
  * Red Hat OpenShift ([Preview](https://cloud.google.com/products#product-launch-stages))
  * Custom (evaluate using custom rules)



### Evaluate other workload types using custom rules

You can define organizational best practices for your workloads using _custom rules_ written in the Rego policy language. Workload Manager evaluates your workloads against these rules and creates reports for any violation and helps you prioritize remediation. For more information, see [About custom rules](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/about-custom-rules).

## How to evaluate a workload

Before you can evaluate a workload against best practices, you must specify the projects that contain the resources to evaluate, and specify the best practices to evaluate the workload against.

To evaluate different sets of resources against different best practices, such as resources from different business units or from different applications, create multiple workload evaluations.

After you create a workload evaluation, you can run it. When you run a workload evaluation, Workload Manager uses data from Cloud Asset Inventory and Cloud Monitoring to analyze the resources that you specified in the workload evaluation against selected best practices.

When you run an evaluation, Workload Manager evaluates resources by comparing their current state with best practices. If a resource doesn't comply with a selected best practice, Workload Manager assigns it a severity level that indicates how far the resource is out of compliance. The Google Cloud console marks each non-compliant resource with an icon. The following table explains these icons, their corresponding severity levels, how the current resource setting might impact your workload, and recommendations for modifying the resource to adhere to best practices. Icon | Severity level | Impacts | Recommendation  
---|---|---|---  
![](https://docs.cloud.google.com/static/workload-manager/images/status-critical.svg) | Critical | System Reliability, Unplanned Outages, Unsupported Configuration |  Resolve as soon as possible to prevent an impact on system availability and data integrity due to a high risk of an unplanned outage.  
![](https://docs.cloud.google.com/static/workload-manager/images/status-high.svg) | High | Degraded Performance, System Stability | Resolve during the next planned maintenance window.  
![](https://docs.cloud.google.com/static/workload-manager/images/status-medium.svg) | Medium | Suboptimal Performance, Supportability | Resolve at your earliest convenience.  
![](https://docs.cloud.google.com/static/workload-manager/images/status-low.svg) | Low | Informational, Non-essential Behavior | Although there's no resolution needed, reviewing this best practice can provide useful insights.  
  
## Rule findings

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When you run an evaluation, Workload Manager generates rule findings that aggregate configuration issues across your projects. You can share these findings across projects so that resource owners can view compliance data for their resources directly in their local consoles.

Rule findings appear in the Workload Manager **Rule findings** tab and on integrated pages such as the Compute Engine **Overview** page.

For more information, see [About Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings).

## What's next

  * [Learn about Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * [View Workload Manager rule findings in Compute Engine](https://docs.cloud.google.com/compute/docs/view-wlm-findings) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * [Set up the agent for SAP workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sap)
  * [Set up the agent for SQL Server workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sql-server)
  * [Set up the agent for Oracle workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-oracle)
  * [Set up the agent for MySQL workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-mysql)
  * [Set up the agent for Redis workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-redis)
  * [Set up the Cluster Services for OpenShift Telemetry operator](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-operator-for-openshift) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation)
  * Review the [best practices for evaluating workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
