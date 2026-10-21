---
url: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/understanding-workspace-logs/
title: Viewing Access Transparency logs for Google Workspace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:56.180737+00:00
---

# Viewing Access Transparency logs for Google Workspace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/understanding-workspace-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Transparency ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Viewing Access Transparency logs for Google Workspace

This document explains how you can view and understand the Access Transparency logs generated when Google personnel access Customer Data in Google Workspace resources. Customer Data in Google Workspace includes text that you have entered into Gmail, Google Docs, Google Sheets, Google Slides, and other Google Workspace apps.

## Before you begin

  * Make sure that you have the Logs Viewer (`roles/logging.viewer`) Identity and Access Management (IAM) role. For information about granting an IAM role, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).


  * To use Access Transparency with Google Workspace, you must enable sharing of Google Workspace content with Google Cloud. For information about sharing Google Workspace content with Google Cloud, see [Sharing data with Google Cloud](https://support.google.com/a/answer/9320190).



## View Access Transparency logs for Google Workspace

You can use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary) in the Google Cloud console to retrieve, view, and analyze Access Transparency logs. For information about using the Logs Explorer, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

To view Access Transparency logs for Google Workspace using the Logs Explorer, do the following:

  1. Go to the **Logs Explorer** page in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query in the Logs Explorer:
         
         logName="organizations/ORG_ID/logs/cloudaudit.googleapis.com%2Faccess_transparency"
         jsonPayload.@type="type.googleapis.com/ccc_hosted_reporting.ActivityProto"
         

Replace ORG_ID with the unique identifier of your Google Cloud organization.

  3. Click **Run query** to execute the query.

![](https://docs.cloud.google.com/static/assured-workloads/access-transparency/docs/images/logs-explorer-workspace-axt.png)![](https://docs.cloud.google.com/static/assured-workloads/access-transparency/docs/images/logs-explorer-workspace-axt.png)




## Sample Access Transparency log for Google Workspace

The following sample is an example of the Access Transparency log for Google Workspace.
    
    
    {
      "insertId": "-6x8cuqc3rk",
      "jsonPayload": {
        "activityId": {
          "uniqQualifier": "1720950322606095479",
          "timeUsec": "1621441673703908"
        },
        "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
        "event": [
          {
            "status": {
              "success": true
            },
            "eventType": "GSUITE_RESOURCE",
            "parameter": [
              {
                "multiStrValue": [
                  "GMAIL"
                ],
                "name": "GSUITE_PRODUCT_NAME",
              },
              {
                "name": "RESOURCE_NAME",
                "multiStrValue": [
                  "//googleapis.com/gmail/users/owner@example.com"
                ],
              },
              {
                "name": "LOG_ID",
                "value": "Qt8v90c0fAEy_SyaOplDvJc",
              },
              {
                "multiStrValue": [
                  "Google Initiated Service - For details, please refer to the documentation."
                ],
                "name": "JUSTIFICATIONS",
              },
              {
                "name": "ACTOR_HOME_OFFICE",
                "value": "US",
              },
              {
                "value": "owner@example.net",
                "name": "OWNER_EMAIL",
              }
            ],
            "eventName": "ACCESS"
          }
        ]
      },
      "resource": {
        "type": "organization",
        "labels": {
          "organization_id": "12345"
        }
      },
      "timestamp": "2021-05-19T16:27:53.703908Z",
      "severity": "NOTICE",
      "logName": "organizations/12345/logs/cloudaudit.googleapis.com%2Faccess_transparency",
      "receiveTimestamp": "2021-05-19T16:28:52.867650088Z"
    }
    

For information about the event and parameters that can appear in the `jsonPayload` field of the Access Transparency logs generated when Google personnel access Google Workspace resources, see [Access Transparency Activity Events](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/access-transparency).

For information about all the other fields in the Access Transparency logs for Google Workspace, see [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

## What's next

  * Learn more about [Access Transparency audit logs](https://support.google.com/a/answer/9230979).


  * Learn more about [Google Workspace audit logs](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
