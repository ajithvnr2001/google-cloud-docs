---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/view-historical-requests/
title: Viewing historical Access Approval requests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:20.130380+00:00
---

# Viewing historical Access Approval requests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/view-historical-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Viewing historical Access Approval requests

This document explains how you can view all historical access requests for a project. Access request logs are retained for a period of 400 days in accordance with the [Cloud Logging retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).

## Before you begin

  * Ensure that you have set up Access Approval by following the instructions in the [Quickstart](https://docs.cloud.google.com/assured-workloads/access-approval/docs/quickstart).

  * Ensure that you have the **Access Approval Viewer** (`roles/accessapproval.viewer`) Identity and Access Management (IAM) role. For more information about IAM roles for Access Approval, see [Access Approval roles](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval).




## View historical access requests

### Console

  1. Go to the **Access Approval** page in the Google Cloud console.

[Go to Access Approval](https://console.cloud.google.com/security/access-approval)

  2. Click **History**.

A table appears that includes all approved, auto-approved, dismissed, and expired requests.

![](https://docs.cloud.google.com/static/assured-workloads/access-approval/docs/images/access-approval-historical.png)![List of approved, auto-approved, dismissed, and expired access requests.](https://docs.cloud.google.com/static/assured-workloads/access-approval/docs/images/access-approval-historical.png)

  3. Optional: If you want to see the details of any access request, click **Details** in the **Details & logs** column.

  4. Optional: If you want to view the Cloud Audit Logs or the Access Transparency logs, click **Logs**.

Cloud Audit Logs provide information about the approval and dismissal actions taken by members within your organization. For more information, see [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit).

Access Transparency logs provide information about the actions taken by Google personnel when accessing Customer Data. For more information, see [Access Transparency overview](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview).




You can also see historical approvals using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary).

[Go to Cloud Logging](https://console.cloud.google.com/logs/query)

If you enable Cloud Audit Logs in your Google Cloud project, you can filter by the Audited Resource `accessapproval.googleapis.com`.

### cURL
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      https://accessapproval.googleapis.com/v1/projects/PROJECT_ID/approvalRequests?filter=ALL
    

By default, the API lists all unapproved, approved, auto-approved, and non-expired requests. There is a filter parameter to do tasks such as listing all dismissed requests. For more information, see [Access Approval API](https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest).

You receive a list of historical access approvals with their status.
    
    
    {
      "approvalRequests": [
        {
          "name": "projects/123456/approvalRequests/xyzabc123",
          "requestedResourceName": "projects/123456",
    
          "requestedReason": {
            "detail":  "Case number: bar123",
            "type":  "CUSTOMER_INITIATED_SUPPORT"
          },
          "requestedLocations": {
            "principalOfficeCountry": "US",
            "principalPhysicalLocationCountry": "US"
          },
          "requestTime": "2018-08-30T17:49:13.712Z",
    
          "requestedExpiration": "2018-09-04T17:49:13.540Z",
          "approve": {
            "approveTime": "2018-08-30T17:49:15.737Z",
            "expireTime": "2018-09-04T17:49:13.540Z"
          }
        }
      ]
    }
    

## What's next

  * Learn more about the [anatomy of an approval request](https://docs.cloud.google.com/assured-workloads/access-approval/docs/approval-request-details).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
