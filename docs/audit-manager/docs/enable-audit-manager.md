---
url: https://docs.cloud.google.com/audit-manager/docs/enable-audit-manager/
title: Enable Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:16.006902+00:00
---

# Enable Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/enable-audit-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Enable Audit Manager Stay organized with collections  Save and categorize content based on your preferences. 

Enable Audit Manager so that you can audit Google Cloud folders and projects using built-in or custom frameworks.

## Before you begin

To enable APIs, you need the Service Usage Admin IAM role (`roles/serviceusage.serviceUsageAdmin`), which contains the `serviceusage.services.enable` permission. To learn how to grant roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Enable Audit Manager

  1. If required, update the [Restrict service usage organization policy constraint](https://docs.cloud.google.com/organization-policy/restrict-services) to include the Audit Manager API (`auditmanager.googleapis.com`).

  2. To enable Audit Manager, complete one of the following:

     * To enable Audit Manager on a project, enable the Audit Manager API.

[Go to Enable access to API](https://console.cloud.google.com/apis/enableflow;apiid=auditmanager.googleapis.com)

     * To enable Audit Manager on your organization, run the following command:
           
           gcloud beta services enable auditmanager.googleapis.com \
              --organization=ORGANIZATION_ID
           

Replace `ORGANIZATION_ID` with your [Google Cloud organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

For more information, see [Enable services](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-enablement#enable).

The Audit Manager service agent is created when you enable Audit Manager. When you enable Audit Manager at the project level, the service agent is `service-`PROJECT_NUMBER`@gcp-sa-audit-manager.iam.gserviceaccount.com`. When you enable Audit Manager at the organization level, the service agent is `service-org-`ORGANIZATION_ID`@gcp-sa-audit-manager.iam.gserviceaccount.com`.

  3. Configure Audit Manager to support [VPC Service Controls service perimeters](https://docs.cloud.google.com/audit-manager/docs/configure-vpcsc).




Audit Manager doesn't support the [jurisdictional console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console).

## What's next

  * [Set up permissions for your auditors](https://docs.cloud.google.com/audit-manager/docs/access-control).
  * [Enroll resources for audit](https://docs.cloud.google.com/audit-manager/docs/enroll-resource).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
