---
url: https://docs.cloud.google.com/logging/docs/audit/best-practices/
title: Best practices for Cloud Audit Logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:24.462256+00:00
---

# Best practices for Cloud Audit Logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/audit/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Best practices for Cloud Audit Logs Stay organized with collections  Save and categorize content based on your preferences. 

Following best practices for Cloud Audit Logs helps your organization maintain security, control access to sensitive log data, and minimize risk. Although not exhaustive, the recommended sequence of tasks in this document helps you understand the scope of audit logging activities and plan your logging configuration.

## Understand Cloud Audit Logs

Audit logs are available for most Google Cloud services. Cloud Audit Logs provides the following types of audit logs for each Google Cloud project, billing account, folder, and organization:

Audit log type | Configurable | Chargeable  
---|---|---  
[Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) | No; always written | No  
[Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) | Yes | Yes  
[Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied) | Yes; you can exclude these logs from being written to log buckets | Yes  
[System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event) | No; always written | No  
  
Data Access audit logs—except for BigQuery—are disabled by default. If you want Data Access audit logs to be written for Google Cloud services, then you must explicitly enable them; for details, see Configure Data Access audit logs on this page.

For information about the overall landscape for audit logging with Google Cloud, see [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit).

## Control access to logs

Due to the sensitivity of audit logging data, it is especially important to configure the appropriate access controls for your organization's users.

Depending on your compliance and usage requirements, set these access controls as follows:

  * Set IAM permissions
  * Configure log views
  * Set log entry field-level access controls



### Set IAM permissions

IAM [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions) and [roles](https://docs.cloud.google.com/iam/docs/overview#roles) determine users' ability to access audit logs data in the [Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest), the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), and the [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging). Use IAM to grant granular access to specific Google Cloud buckets and prevent unwanted access to other resources.

The permission-based roles that you grant to your users depend on their auditing-related functions within your organization. For example, you might grant your CTO broad administrative permissions whereas your developer team members might require logs-viewing permissions. For guidance on which roles to grant to your organization's users, see [configuring roles for audit logging](https://docs.cloud.google.com/iam/docs/roles-audit-logging).

When setting IAM permissions, apply the security principle of least privilege, so you grant users only the necessary access to your resources:

  * Remove all nonessential users.
  * Grant essential users the correct and minimal permissions.



For instructions on setting IAM permissions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Configure log views

All logs, including audit logs, received by Logging are written into storage containers called [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries). [Log views](https://docs.cloud.google.com/logging/docs/logs-views) let you control who has access to the logs within your log buckets.

Because log buckets can contain logs from multiple Google Cloud projects, you might need to control which Google Cloud projects different users can view logs from. Create custom log views, which give you more granular access control for those buckets.

You can query log views with the Logs Explorer or with Observability Analytics. For more information, see [Query and view logs overview](https://docs.cloud.google.com/logging/docs/log-analytics).

For instructions on creating and managing log views, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

### Set log field-level access controls

Field-level access controls let you hide individual `LogEntry` fields from users of a Google Cloud project, providing you a more granular way to control the logs data a user can access. Compared to logs views, which hide the entire `LogEntry`, field-level access controls hide individual fields of the `LogEntry`. For example, you might want to redact external user PII, such as an email address contained in the log entry payload, from the majority of your organization's users.

If you plan to use [Observability Analytics](https://docs.cloud.google.com/logging/docs/log-analytics#analytics) to analyze your audit logs, then don't configure field-level access controls on the log bucket that stores those logs. You can't use Observability Analytics on log buckets that have field-level access controls configured.

For instructions on configuring field-level access controls, see [Configure field-level access](https://docs.cloud.google.com/logging/docs/field-level-acl).

## Configure Data Access audit logs

When enabling new Google Cloud services, evaluate whether or not to enable [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access).

Data Access audit logs help Google Support troubleshoot issues with your account. Therefore, we recommend enabling Data Access audit logs when possible.

**Note:** Data Access audit logs can be large and that you might incur additional costs for storage. For pricing information, see the Cloud Logging sections of the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

To enable all audit logs for all services, follow the [instructions to update the Identity and Access Management (IAM) policy](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#example) with the configuration listed in the [audit policy](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#policy-objects).

After you define your organization-level data access policy and enable Data Access audit logs, use a test Google Cloud project to validate the configuration of your audit logs collection before creating developer and production Google Cloud projects in the organization.

For instructions on enabling Data Access audit logs, see [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## Control how your logs are stored

You can configure aspects of your organization's buckets and also create user-defined buckets to centralize or subdivide your log storage. Depending on your compliance and usage requirements, you might want to customize your logs storage as follows:

  * Choose where your logs are stored.
  * Define the data retention period.
  * Protect your logs with customer-managed encryption keys (CMEK).



### Choose where your logs are stored

In Logging buckets are regional resources: the infrastructure that stores, indexes, and searches your logs is located in a specific geographical location.

Your organization might be required to store its logs data in specific regions. The primary factors in selecting the region where your logs are stored include meeting your organization's latency, availability, or compliance requirements.

To automatically apply a particular storage region to the new `_Default` and `_Required` buckets created in your organization, you can configure a default resource location.

For instructions on configuring default resource locations, see [Configure default settings for organizations](https://docs.cloud.google.com/logging/docs/default-settings#specify-region).

### Define data retention periods

Cloud Logging retains logs according to retention rules applying to the log bucket type where the logs are held.

To meet your compliance needs, configure Cloud Logging to retain logs between 1 day and 3650 days. Custom retention rules apply to all the logs in a bucket, regardless of the log type or whether that log has been copied from another location.

For instructions on setting retention rules for a log bucket, see [Configure custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention).

### Protect your audit logs with customer-managed encryption keys

By default, Cloud Logging encrypts customer content stored at rest. Your organization might have advanced encryption requirements that the default encryption at rest doesn't provide. To meet your organization's requirements, instead of Google managing the key encryption keys that protect your data, configure customer-managed encryption keys (CMEK) to control and manage your own encryption.

For instructions on configuring CMEK, see [Configure CMEK for logs storage](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage).

## Pricing

For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page. If you route log data to other Google Cloud services, then see the following documents:

  * [Cloud Storage pricing](https://cloud.google.com/storage/pricing)
  * [BigQuery pricing](https://cloud.google.com/bigquery/pricing#data_ingestion_pricing)
  * [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing)



As you configure and use your audit logs, we recommend the following pricing-related best practices:

  * [Estimate your bills](https://docs.cloud.google.com/stackdriver/estimating-bills) by viewing your usage data and configuring alerting policies.

  * Be aware that Data Access audit logs can be large and that you might incur additional costs for storage.

  * Manage your costs by [excluding audit logs](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) that aren't useful. For example, you can probably exclude Data Access audit logs in development projects.




## Query and view audit logs

If you need to troubleshoot, being able to quickly look at logs is a requirement. In the Google Cloud console, use the Logs Explorer to retrieve your audit log entries for your organization:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select your organization.

  3. In the **Query** pane, do the following:

     * In **Resource type** , select the Google Cloud resource whose audit logs you want to see.

     * In **Log name** , select the audit log type that you want to see:

       * For Admin Activity audit logs, select **activity**.
       * For Data Access audit logs, select **data_access**.
       * For System Event audit logs, select **system_event**.
       * For Policy Denied audit logs, select **policy**.

If you don't see these options, then there aren't any audit logs of that type available in the organization.

     * In the query editor, further specify the audit log entries that you want to see. For examples of common queries, see [Sample queries using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/query-library).

  4. Click **Run query**.




For more information about querying by using the Logs Explorer, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).

## Monitor your audit logs

You can use Cloud Monitoring to notify you when conditions you describe occur. To provide Cloud Monitoring with data from your logs, Logging lets you create log-based alerting policies, which notify you anytime that a specific event appears in a log.

Configure alerting policies to distinguish between events that require immediate investigation versus low-priority events. For example, if you want to know when an audit log records a particular data-access message, you can create a log-based alerting policy that matches the message and notifies you when the message appears.

For instructions about configuring log-based alerting policies, see [Managing log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

## Route logs to supported destinations

Your organization may face requirements for creating and preserving audit logs. Using [sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks), you can route some or all of your logs to these supported destinations:

  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/creating-buckets)


  * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/create-topic-console#create_a_topic), including third parties such as [Splunk](https://docs.cloud.google.com/architecture/exporting-stackdriver-logging-for-splunk)


  * [BigQuery](https://docs.cloud.google.com/bigquery/quickstart-command-line#createtable)


  * Another Cloud Logging bucket

**Tip:** For longer term retention, configure sinks prior to your organization receiving logs data.

Determine whether you need folder-level or organization-level sinks, and route logs from all the Google Cloud projects inside the organization or folder using [aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview). For example, you might consider these routing use cases:

  * Organization-level sink: If your organization uses a SIEM to manage multiple audit logs, you might want to route all of your organization's audit logs. Thus, an organization-level sink makes sense.

  * Folder-level sink: Sometimes, you might want to only route departmental audit logs. For example, if you have a "Finance" folder and an "IT" folder, you might find value in only routing the audit logs belonging to the "Finance" folder, or the other way around.

For more information on folders and organizations, see [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).




Apply the same access policies to the Google Cloud destination that you use to route logs as you applied to the Logs Explorer.

For instructions on creating and managing aggregated sinks, see [Collate and route organization-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks).

### Understand data format in sink destinations

When routing audit logs to destinations outside of Cloud Logging, understand the format of the data that has been sent.

For example, if routing logs to BigQuery, Cloud Logging applies rules to shorten BigQuery schema field names for [audit logs](https://docs.cloud.google.com/logging/docs/export/bigquery#audit-logs) and for certain structured payload fields.

To understand and find log entries that you routed from Cloud Logging to supported destinations, see [View logs in sink destinations](https://docs.cloud.google.com/logging/docs/export/using_exported_logs).

### Copy log entries

Depending on your organization's compliance needs, you might need to share audit log entries with auditors outside of Logging. If you need to share log entries that are already stored in Cloud Logging buckets, you can manually copy them to Cloud Storage buckets.

When you copy log entries to Cloud Storage, the log entries also remain in the log bucket they were copied from.

Note that copy operations don't replace sinks, which automatically send all incoming log entries to a pre-selected supported storage destination, including Cloud Storage.

For instructions on routing logs to Cloud Storage retroactively, see [Copy log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
