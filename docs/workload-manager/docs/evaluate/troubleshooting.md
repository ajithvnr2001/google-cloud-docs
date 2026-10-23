---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/troubleshooting/
title: Troubleshooting evaluations \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:52.655400+00:00
---

# Troubleshooting evaluations  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Troubleshooting evaluations Stay organized with collections  Save and categorize content based on your preferences. 

Troubleshooting evaluation issues, such as missing IAM permissions or disabled notifications, helps ensure that you receive alerts about workload deviations from security and compliance best practices.

This document describes how to resolve common issues that might occur with Workload Manager evaluations.

## Notifications are disabled for the first evaluation in a project

When you create the first evaluation in a Google Cloud project using Workload Manager, you might notice that the event notification checkboxes are disabled in the **Notifications** section. You can also see the following message:
    
    
    Selection unavailable until metrics exist in the current project.
    

This issue occurs because the Workload Manager service account does not have the required permissions to send metrics to Cloud Monitoring in the project from where you run the evaluation.

If you're creating the first evaluation in a project, then create the evaluation without event notifications. If you have at least one evaluation in the project, then do the following:

  1. Authorize the Workload Manager service account to send metrics to your project.

     1. In the navigation panel of the Google Cloud console, click **IAM & Admin** and then select **IAM** :

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Select the project in which you're creating the evaluation.

     3. To see the Google-managed service accounts on the **Permissions** page, select the **Include Google-provided role grants** checkbox.

     4. Search for the Workload Manager service account that has the following format:
            
            service-PROJECT_NUMBER@gcp-sa-workloadmanager.iam.gserviceaccount.com

You can find the `PROJECT_NUMBER` of your Google Cloud project on the **Project settings** page. For more information, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

     5. To modify roles for the service account, click edit **Edit principal** in the row that contains the service account name, and click add **Add another role**.

     6. If the service account is not listed on the **Permissions** page, manually enter the service account name:

        1. Click person_add **Grant Access** , and then enter the email address of the Workload Manager service account in the following format:
               
               service-PROJECT_NUMBER@gcp-sa-workloadmanager.iam.gserviceaccount.com"

        2. Click **Select a role**.

  2. Assign the following roles to the service account:

     * Service Usage Consumer ([`roles/serviceusage.serviceUsageConsumer`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer))
     * Monitoring Metric Writer ([`roles/monitoring.metricWriter`](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter))
  3. Run an evaluation and wait for completion.

After successful completion of the evaluation, Workload Manager sends metrics to the project, and then you can [set alerts for the evaluations](https://docs.cloud.google.com/workload-manager/docs/create-evaluation#notifications).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
