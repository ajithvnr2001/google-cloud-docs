---
url: https://docs.cloud.google.com/compute/vm-manager/docs/best-practices/
title: Best practices for using VM Manager across an organization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:58.231552+00:00
---

# Best practices for using VM Manager across an organization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Best practices for using VM Manager across an organization Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a consolidated overview of organization-level how-to guides and best practices for configuring, orchestrating, and monitoring VM Manager across your Google Cloud organization or folders. You can use these guides to automate fleet-wide operating system management, enforce compliance, and centralize reporting across projects. Each entry in the following table links to detailed documentation for specific tasks: 

Select a category: Compliance and custom dataMonitoring and governancePatch and vulnerability managementPolicy orchestrationSetup and enablement

Category | Best practices | Summary  
---|---|---  
Setup and enablement | [Enable VM Manager across a folder or organization](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-api-hierarchical) | Enable the OS Config API across all existing and future projects in an organization or folder by using hierarchical service activation and organization policy constraints.  
Setup and enablement | [Set up VM Manager across an organization by using Terraform](https://docs.cloud.google.com/compute/vm-manager/docs/vm-manager-org-terraform) | Automate organization-wide VM Manager enablement, custom IAM role creation, instance metadata configuration, and OS policy assignments by using Terraform.  
Policy orchestration | [About policy orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/about-policy-orchestrator) | Understand how organization-level and folder-level policy orchestrators automate progressive rollouts of OS policy assignments across projects and zones.  
Policy orchestration | [Prerequisites for using policy orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites) | Configure the service agents, IAM permissions, and VPC Service Controls ingress rules that are required for organization-level and folder-level policy orchestration.  
Policy orchestration | [Manage OS policy assignments using policy orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/use-policy-orchestrator) | Create organization-level or folder-level policy orchestrators to progressively roll out, update, or delete OS policy assignments across multiple projects and zones.  
Policy orchestration | [View, edit, and delete policy orchestrators](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-edit-policy-orchestrator) | Inspect rollout status across your organization or folders, modify orchestration scopes, or delete existing policy orchestrators.  
Compliance and custom data | [View OS policy compliance summary for an organization or folder](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-compliance#policy-summary) | Review aggregated OS policy compliance states across all projects in your organization or folder in the Google Cloud console, and filter results by using the query builder.  
Compliance and custom data Monitoring and governance | [View custom data from OS policies for your organization](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-custom-data) | Export VM Manager and Cloud Asset Inventory data to BigQuery to query custom script outputs (strings or JSON) and enforcement error messages across all VMs in your organization.  
Patch and vulnerability management | [View vulnerability reports for your organization](https://docs.cloud.google.com/compute/vm-manager/docs/patch/view-org-vulnerability-reports) | Export OS inventory and vulnerability data to BigQuery by using Cloud Asset Inventory to identify and query Common Vulnerabilities and Exposures (CVEs) across your organization.  
Patch and vulnerability management | [View patch summary for VMs in an organization or folder](https://docs.cloud.google.com/compute/vm-manager/docs/patch/view-patch-summary#patch-summary) | Monitor organization-wide or folder-wide patch compliance, available OS updates, and reboot requirements across all projects in the Google Cloud console.  
Monitoring and governance | [View VM Manager status for your organization](https://docs.cloud.google.com/compute/vm-manager/docs/view-org-status) | Export Cloud Asset Inventory resource and OS inventory snapshots to BigQuery to verify VM Manager enablement, check OS Config agent versions, and audit operating system distributions across your organization.  
Monitoring and governance | [VM Manager audit logs](https://docs.cloud.google.com/compute/vm-manager/docs/audit-logging) | Monitor Admin Activity and Data Access audit logs for VM Manager operations, including organization-level and folder-level policy orchestrator actions.  
Monitoring and governance Policy orchestration | [Quotas and limits](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas) | Track and manage folder-level and organization-level quotas for policy orchestrators across large VM fleets.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
