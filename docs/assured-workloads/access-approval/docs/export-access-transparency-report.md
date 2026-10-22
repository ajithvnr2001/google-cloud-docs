---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/export-access-transparency-report/
title: Generate or download an Access Transparency report \u00a0|\u00a0 Access Approval \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:22.122972+00:00
---

# Generate or download an Access Transparency report  |  Access Approval  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/export-access-transparency-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Generate or download an Access Transparency report

You can generate and download Access Transparency reports using [access insights](https://docs.cloud.google.com/assured-workloads/access-approval/docs/access-insights).

## Before you begin

  * To generate and download Access Transparency reports, [enable Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys#enrolling) for your organization. To enable Access Approval in an audit-only mode, select the **Transparency** [enrollment mode](https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys#enrollment-mode) for your policy.



### Required roles

To get the permission that you need to generate and download Access Transparency reports, ask your administrator to grant you the [Access Approval Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.viewer) (`roles/accessapproval.viewer`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `accessapproval.settings.get` permission, which is required to generate and download Access Transparency reports. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Generate an Access Transparency report

  1. In the Google Cloud console, go to the **Access Approval** page.

[Go to Access Approval](https://console.cloud.google.com/security/access-approval)

  2. On the **Home** tab, select the start date, the end date, the products, and the reason type to include in your report.

  3. Click **Queue export**.




## Download an Access Transparency report

You can download a generated report from the **Reports** tab for up to 30 days.

  1. In the Google Cloud console, go to the **Access Approval** page.

[Go to Access Approval](https://console.cloud.google.com/security/access-approval)

  2. Click the **Reports** tab.

  3. Locate the report that you want to download, and then click **Download**.




## What's next

  * Learn more about [access insights](https://docs.cloud.google.com/assured-workloads/access-approval/docs/access-insights).

  * Learn more about [Access Transparency log entries and how to view and use them](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
