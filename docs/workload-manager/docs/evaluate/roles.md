---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/roles/
title: IAM roles in consumer and target projects for evaluations \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:30.121489+00:00
---

# IAM roles in consumer and target projects for evaluations  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  IAM roles in consumer and target projects for evaluations Stay organized with collections  Save and categorize content based on your preferences. 

When you evaluate workloads using Workload Manager, you inspect infrastructure resources that might span multiple Google Cloud projects. Understanding how IAM roles are split between your central evaluation project and the projects hosting your workloads ensures that you grant the minimum permissions required to run evaluations securely.

This document explains consumer and target projects and lists the roles and permissions that you need to create and run Workload Manager evaluations.

## Consumer and target projects

Workload Manager evaluations scan resources across multiple projects which are called _target projects_ , but the evaluation is stored in only one project called a _consumer project_.

You use the consumer project to access Workload Manager in the Google Cloud console, and to create and run evaluations. When you create an evaluation using the Google Cloud console, in the **Evaluation scope** section of the workflow, you specify the target projects that hold the resources you want to evaluate.

If the resources to evaluate are present in the same project where you create a Workload Manager evaluation, then the consumer project is also considered as one of your target projects.

## Summary of required permissions to create and run an evaluation

The following table summarizes the permissions required for users in the consumer and target projects to create and run evaluations using Workload Manager. To get the permission that you need, ask your administrator to grant you a role that includes the required permission or create a custom role.

Action | Consumer project | Target project  
---|---|---  
Enable Workload Manager API |  Permission:   
`serviceusage.services.enable`  
  
Predefined role that includes the permission:   
`roles/serviceusage.serviceUsageAdmin` | None  
Create an evaluation |  Permission to create a service account:   
`resourcemanager.projects.setIamPolicy`  
  
Predefined role that includes the permission:   
`roles/resourcemanager.projectIamAdmin` Required only when you create the first evaluation. Predefined role that grants permission to create an evaluation:   
`roles/workloadmanager.evaluationAdmin` Predefined role that grants permission to create alert notifications:   
`roles/monitoring.metricWriter` To create an evaluation using custom rules, you need the following additional permissions: Predefined role that grants permission to read Cloud Asset Inventory data:   
`roles/cloudasset.owner` Predefined role that grants permission to read rules stored in a Cloud Storage bucket:   
`roles/storage.objectViewer` Predefined role that grants permission to write evaluation results to a BigQuery dataset:   
`roles/bigquery.admin` |  Permission to create a service account:   
`resourcemanager.projects.setIamPolicy`  
  
Predefined role that includes the permission:   
`roles/resourcemanager.projectIamAdmin` Required only when you create the first evaluation.  
Run an evaluation |  Permission:   
`workloadmanager.evaluations.run`  
  
Predefined role that includes the permission:   
`roles/workloadmanager.evaluationAdmin` | None  
View evaluation results |  Permission:   
`workloadmanager.results.list`  
  
Predefined role that includes the permission:   
`roles/workloadmanager.evaluationAdmin`  
or  
`roles/workloadmanager.evaluationViewer` | None  
View rule findings and shared findings ([Preview](https://cloud.google.com/products#product-launch-stages)) |  Permission:   
`workloadmanager.findings.list`  
  
Predefined role that includes the permission:   
`roles/workloadmanager.evaluationViewer`  
or  
`roles/workloadmanager.evaluationAdmin` |  Permission:   
`workloadmanager.findings.list`  
  
Predefined role that includes the permission:   
`roles/workloadmanager.evaluationViewer`  
or  
`roles/workloadmanager.evaluationAdmin` Required to view shared rule findings on the Compute Engine Overview page or in Workload Manager.  
Share evaluation findings ([Preview](https://cloud.google.com/products#product-launch-stages)) |  Permission:   
`workloadmanager.evaluations.create`  
or  
`workloadmanager.evaluations.update`  
  
Predefined role that includes the permission:   
`roles/workloadmanager.evaluationAdmin` |  Permission:   
`workloadmanager.findings.create`  
  
Predefined role that includes the permission:   
`roles/workloadmanager.evaluationAdmin` Required on the target project, folder, or organization scope where findings are shared.  
  
## Service agents for evaluations

Workload Manager uses service agents (`roles/workloadmanager.serviceAgent` and `roles/workloadmanager.worker`) to scan resources in target projects and execute evaluations from consumer projects.

To learn how Workload Manager creates service agents automatically or how to create them manually using the Workload Manager API, see [Workload Manager service agents](https://docs.cloud.google.com/workload-manager/docs/access-control/service-accounts).

## Additional roles and permissions

For the complete reference of all Workload Manager roles and permissions across all APIs, see [Workload Manager IAM roles and permissions](https://docs.cloud.google.com/workload-manager/docs/access-control/roles-permissions).

For an overview of IAM allow policies and conditional access in Workload Manager, see [Access control with IAM](https://docs.cloud.google.com/workload-manager/docs/access-control/access-control-iam).

## What's next

  * [About Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings)
  * [View Workload Manager rule findings in Compute Engine](https://docs.cloud.google.com/compute/docs/view-wlm-findings)
  * [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
