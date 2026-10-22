---
url: https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs/
title: View and manage audit logs for Google Workspace \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:03.653417+00:00
---

# View and manage audit logs for Google Workspace  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  View and manage audit logs for Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

You can configure, view, and route audit logs for Google Workspace to Google Cloud to monitor administrative and user activity across your organization. Routing these audit logs to Google Cloud helps you diagnose and resolve issues related to data security and compliance.

For an overview of Google Workspace audit logs, see [Audit logs for Google Workspace](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging).

## Overview

You can share audit logs with your Google Cloud organization using your Google Workspace, Cloud Identity, or Google Drive Enterprise account. You can access the shared audit logs through [Cloud Logging](https://docs.cloud.google.com/logging/docs) in Google Cloud.

You can access the following services' Google Workspace, Cloud Identity, and Google Drive Enterprise audit logs in Google Cloud:

  * Admin Audit logs
  * Enterprise Groups Audit logs
  * Login Audit logs
  * OAuth Token Audit logs
  * SAML Audit logs



For more information about these services' audit logs, see [Service-specific information](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#service-info).

## Before you begin

To view audit logs for Google Workspace in Google Cloud, ensure you have the correct permissions to view audit logs for Google Workspace.

IAM permissions and roles determine your ability to access audit logs data in the [Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest), the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), and the [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging).

For detailed information about the organization-level IAM permissions and roles you might need, see Cloud Logging [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View audit logs in the Google Admin console

You can view audit logs for Google Workspace directly in the Google Admin console. To learn how to view these audit logs, see the following topics:

  * [View Google Workspace Admin Audit logs in the Google Admin console](https://support.google.com/a/answer/4579579).

  * [View Google Workspace Enterprise Groups Audit logs in the Google Admin console](https://support.google.com/a/answer/9667889).

  * [View Google Workspace Login Audit logs in the Google Admin console](https://support.google.com/a/answer/4580120).

  * [View Google Workspace OAuth Token Audit logs in the Google Admin console](https://support.google.com/a/answer/6124308)

  * [View Google Workspace SAML Audit logs in the Google Admin console](https://support.google.com/a/answer/7007375)

  * [View other types of audit logs for Google Workspace in the Google Admin console](https://support.google.com/a/answer/9725452).




## Share audit logs with Google Cloud

To enable sharing Google Workspace data with Google Cloud from your Google Workspace, Cloud Identity, or Google Drive Enterprise account, follow the instructions in [Share data with Google Cloud services](https://support.google.com/a/answer/9320190).

After you enable sharing Google Workspace data with Google Cloud, Google Cloud receives all audit logs for Google Workspace. To exclude certain audit logs from Google Cloud, set up sinks with [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions). You can't use the IAM page in the Google Cloud console to selectively disable sharing the data.

## View audit logs for Google Workspace in Google Cloud

To view audit logs for Google Workspace in Logging, you use the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) to select data. At a minimum, you need to know the [identifier of your Google Cloud organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#console). You can further specify other indexed [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields, like `resource.type`, and filter by event types.

Here are the audit log names that apply to Google Workspace:

  * [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access):
        
        organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fdata_access

  * [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity):
        
        organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity




In the preceding log names, ORGANIZATION_ID refers to the Google Cloud organization for which you want to view audit logs.

You have several options for viewing your audit log entries:

### Console

To get the audit log entries for your Google Cloud organization using the Logs Explorer in the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. From the **Project selector** menu, select an organization.

  3. From the **Resource** drop-down menu, select the resource type whose audit logs you want to see.

  4. In the **Log name** drop-down menu, select `data_access` for Data Access audit logs or `activity` for Admin Activity audit logs.

If you don't see these options, then these audit logs aren't currently available in the organization.

  5. Optional: You can build a filter in the **Query Builder** pane to further specify the logs you want to see. To learn more about querying logs, see [Build queries](https://docs.cloud.google.com/logging/docs/view/building-queries#building-queries).




### API

To read your audit log entries using the Logging API, do the following:

  1. Go to the **Try this API** section in the documentation for the [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method.

  2. Put the following into the **Request body** part of the **Try this API** form. Clicking on this [prepopulated form](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list?apix_params=%7B%22resource%22%3A%7B%22resourceNames%22%3A%5B%22organizations%2F%5Borganization-id%5D%22%5D%2C%22pageSize%22%3A5%2C%22filter%22%3A%22logName%3D\(organizations%2F%5Borganization-id%5D%2Flogs%2Fcloudaudit.googleapis.com%252Factivity%20OR%20organizations%2F%5Borganization-id%5D%2Flogs%2Fcloudaudit.googleapis.com%252Fsystem_events%20OR%20organizations%2F%5Borganization-id%5D%2Flogs%2Fcloudaudit.googleapis.com%252Fdata_access\)%22%7D%7D) automatically fills the request body, but you need to supply a valid ORGANIZATION_ID in each of the log names.
         
         {
                 "resourceNames": [
                   "organizations/ORGANIZATION_ID"
                 ],
                 "pageSize": 5,
                 "filter": "logName : organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com"
               }

  3. Click **Execute**.




For more details about using the Logging API to read logs, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

### gcloud

The Google Cloud CLI provides a command-line interface to the Cloud Logging API. To read your audit log entries, run the following command:
    
    
        gcloud logging read "logName : organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com"

Replace ORGANIZATION_ID in each of the log names with the ID of the Google Cloud organization for which you want to read audit logs.

For more information about this command, see the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) reference.

Each Google Workspace service that provides audit logs captures events specific to the service. If you want to read logs for a particular audited event, such as a successful login or revoked access, add the following to your filter and supply a valid EVENT_NAME:
    
    
    protoPayload.metadata.event.eventName="EVENT_NAME"
    resource.type="audited_resource"

For a list of valid event names and their parameters, see the [Reports API documentation](https://developers.google.com/admin-sdk/reports/reference/rest) and select from the listed services.

For example, if you want to read logs for each time the Login service reports that an [account password was changed](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/login#password_edit), your filter would look like this:
    
    
    protoPayload.metadata.event.eventName="password_edit"
    resource.type="audited_resource"

## Route audit logs from Google Cloud

After audit logs for Google Workspace are in Google Cloud, you can route the logs to supported destinations. For example, you can create a sink to route logs to Splunk or BigQuery. For a conceptual overview of how logs are routed from Cloud Logging, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

Because audit logs for Google Workspace are organization-level logs, you route them using [aggregated sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) at the organizational level to these destinations:

  * [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets)

  * [Pub/Sub topics](https://docs.cloud.google.com/pubsub/docs/create-topic-console#create_a_topic)

  * [BigQuery tables](https://docs.cloud.google.com/bigquery/docs/quickstarts/load-data-bq#createtable)




For instructions about configuring sinks to route logs, see [Collate and route organization-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks).

## Customize data retention period

Cloud Logging retention periods apply to the audit logs that you store in [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries#about_log_buckets).

To keep audit logs longer than the [default retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods), you can configure [custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention).

## What's next

  * [Troubleshoot](https://docs.cloud.google.com/logging/docs/audit/troubleshooting-faq-gsuite) issues with audit logs for Google Workspace.
  * Review [best practices](https://docs.cloud.google.com/logging/docs/audit/best-practices) for Cloud Audit Logs.
  * Learn about [Access Transparency logs for Google Workspace](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/understanding-workspace-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
