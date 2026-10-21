---
url: https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter/
title: Diagnose an access denial and view the classic report \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:55.592728+00:00
---

# Diagnose an access denial and view the classic report  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Diagnose an access denial and view the classic report Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can use the VPC Service Controls violation analyzer to understand and diagnose issues that VPC Service Controls logs.

VPC Service Controls logs include details about requests to protected resources and the reason why VPC Service Controls denied the request. However, these details aren't always easily apparent and you might spend considerable time understanding the logs. You can use the VPC Service Controls violation analyzer to diagnose denials from a service perimeter. For information about violation reasons, see [Debugging requests blocked by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#debugging).

You can also use the violation analyzer to diagnose denials from a service perimeter that uses a dry-run configuration.

You can also diagnose an access denial and [view its comprehensive evaluation report in the violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer).

## Before you begin

To troubleshoot a VPC Service Controls violation, make sure that you have the VPC Service Controls Troubleshooter Viewer IAM role (`roles/accesscontextmanager.vpcScTroubleshooterViewer`) at the organization level. This role doesn't let you modify perimeters or access levels.

## Troubleshoot an access denial event

When VPC Service Controls denies an access request, it generates a unique ID and logs an encrypted troubleshooting token in Cloud Audit Logs. The error returned by the Google Cloud CLI for a VPC Service Controls denial includes the event's [unique ID](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors#unique-id).

Before you begin, [obtain the unique ID](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors#unique-id) for the denial that you want to troubleshoot.

### Access the violation analyzer

The violation analyzer is available only in the Google Cloud console. You can access the violation analyzer using either the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary) or the VPC Service Controls page.

#### Use the Logs Explorer

By using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary), you can move directly from a log entry for a VPC Service Controls denial to the violation analyzer.

To access the violation analyzer from a log entry, do the following:

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. On the **Logs Explorer** page, use the denial's [unique ID to access the log entry](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors#unique-id).
  3. In the **Query Results** box, in the row for the denial that you want to troubleshoot, click **VPC Service Controls** , and then click **Troubleshoot denial**.
  4. On the troubleshooting result page, click **Switch to classic view**.



#### Use the VPC Service Controls page

To access the violation analyzer from the **VPC Service Controls** page, do the following:

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you're prompted, select your organization. You can access the **VPC Service Controls** page only at the organization level.

  3. On the **VPC Service Controls** page, click **Violation analyzer**.

  4. On the **Violation analyzer** page, in the **Troubleshooting token (or unique ID)** field, enter the unique ID of the denial that you want to troubleshoot.

  5. Click **Continue**.

  6. On the troubleshooting result page, click **Switch to classic view**.



If you want to switch back and [view the comprehensive evaluation report](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer), click **Analyze full details** in the classic troubleshooting result page.

## What's next

  * [Understanding VPC Service Controls audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging)
  * Learn how the [VPC Service Controls unique identifier helps troubleshoot issues related to service perimeters](https://cloud.google.com/blog/products/identity-security/unique-identifier-helps-troubleshooting-vpc-service-controls-perimeter).
  * Learn how to [diagnose an access denial in violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer) and view its comprehensive evaluation report.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
