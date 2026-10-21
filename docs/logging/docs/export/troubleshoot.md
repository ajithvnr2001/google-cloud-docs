---
url: https://docs.cloud.google.com/logging/docs/export/troubleshoot/
title: Troubleshoot routing and storing logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:41.039184+00:00
---

# Troubleshoot routing and storing logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/export/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Troubleshoot routing and storing logs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains common routing and storage issues and how to use the Google Cloud console to view and troubleshoot configuration mistakes or unexpected results.

For general information about viewing log data, see [View logs in sink destinations](https://docs.cloud.google.com/logging/docs/export/using_exported_logs).

## Troubleshoot log routing

This section describes how to troubleshoot common issues when routing your log entries.

### Creating a sink fails with an unknown service error

You attempt to create a log sink but the command fails with an `INVALID_ARGUMENT (HTTP 400)` error. The error message includes the following:
    
    
    Sink.destination with unknown service name: [SERVICE_DOMAIN]. Supported services are bigquery.googleapis.com,pubsub.googleapis.com,storage.googleapis.com,logging.googleapis.com
    

To resolve this error, use the global endpoint for one of the supported services. A log sink destination can't specify a [regional service endpoint](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) (REP), such as `pubsub.LOCATION.rep.googleapis.com`.

### Sink configuration error message states that a topic region is not allowed

One of the following occurs:

  * You receive an email with the subject `[ACTION REQUIRED] Cloud Logging sink configuration error in [PROJECT_ID]` and the error code `topic_region_not_allowed`. The email includes a message similar to the following:

> The topic's message storage policy requires enforcement in transit, but the Publish request was received by a Pub/Sub server in a non-allowed region. Please either publish via a regional Cloud Logging endpoint corresponding to an allowed region, or update the topic's message storage policy.

  * You notice log entries with a severity level of `ERROR`, an error code of `"topic_region_not_allowed"`, and a text payload similar to the following:
        
        Cloud Logging sink configuration error in [PROJECT_ID], sink [SINK_NAME]: topic_region_not_allowed ()
        




These messages indicate that the sink's destination is a Pub/Sub topic that enforces in-transit restrictions and that Logging routed log entries from a region not permitted by the topic's policy. In-transit restrictions can be configured on an individual topic's message storage policy or enforced organization-wide by using the `constraints/pubsub.enforceInTransitRegions` organization policy constraint.

To resolve these failures, do one of the following:

  * Update the destination Pub/Sub topic's message storage policy to disable in-transit enforcement or expand its allowed persistence regions.
  * If in-transit restrictions are enforced by an organization policy, update the organization policy or request an exemption for the project.
  * Update the sink to route log entries to a different destination.



### Destination contains unwanted log entries

You are viewing the log entries routed to a destination and determine that the destination contains unwanted log entries.

To resolve this condition, update the [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) for your sinks that route log entries to the destination. Exclusion filters let you exclude selected log entries from being routed to a destination.

For example, assume that you create an [aggregated sink](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview) to route log entries in an organization to a destination. To exclude the log entries from a specific project from being routed to the destination, add the following exclusion filter to the sink:
    
    
    logName:projects/PROJECT_ID
    

You can also exclude log entries from multiple projects by using the logical-OR operator to join `logName` clauses.

### Destination is missing log entries

Perhaps the most common sink-related issue is that log entries seem to be missing from the destination of a sink.

**Note:** If the Google Cloud console is reporting an error message or if you see a log entry that is reporting a sink configuration error, then skip section and view the error log to target and fix the underlying issue.

In some cases, an error isn't generated but you might notice that log entries are unavailable when you try to access them in your destination. If you suspect that your sink isn't properly routing log entries, then check your sink's system log-based metrics:

  * `exports/byte_count`: Number of bytes in log entries that were routed.
  * `exports/log_entry_count`: Number of log entries that were routed.
  * `exports/error_count`: Number of log entries that failed to be routed.



The metrics have labels that record the counts by sink name and destination name and let you know whether your sink is routing log entries successfully or or failing. For details about how to view metrics, see [Log-based metrics overview](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

If your sink metrics indicate that your sink isn't performing as you expected, here are some possible reasons and what to do about them:

**Latency**

  * No matching log entries have been received since you created or updated your sink; only new log entries are routed.

Try waiting an hour and check your destination again.

  * Matching log entries are late-arriving.

There can be a delay before you can view your log entries in the destination. Late-arriving log entries are especially common for sinks which have configured Cloud Storage buckets as their destinations. Try waiting a few hours and check your destination again.




**Viewing scope/filter is incorrect**

  * The scope you're using to view log entries stored in a log bucket is incorrect.

Scope your search to one or more [log views](https://docs.cloud.google.com/logging/docs/logs-views) as follows:

    * If you're using the Logs Explorer, then use the [Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope) button.

    * If you're using the gcloud CLI, then use the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command and add a `--view=AllLogs` flag.

  * The time range you're using to [select and view data in your sink destination](https://docs.cloud.google.com/logging/docs/export/using_exported_logs) is too narrow.

Try broadening the time range that you're using when selecting data in your sink destination.




**Error in sink filter**

  * The sink's filter is incorrect and not capturing the log entries you expected to see in your destination.

Edit your sink's filter by using the **Log Router** in the Google Cloud console. To verify you entered the correct filter, select **Preview logs** in the **Edit sink** panel. This opens the Logs Explorer in a new tab with the filter pre-populated. For instructions about viewing and managing your sinks, see [Manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#managing_sinks).




### View errors

For each of the supported sink destinations, Logging provides error messages for improperly configured sinks.

There are several ways to view these sink-related errors; these methods are described in the following sections:

  * View the error logs generated for the sink.
  * Receive sink error notifications by email.

The sender of this email is `logging-noreply@google.com`. The subject line is similar to `[ACTION REQUIRED] Cloud Logging sink configuration error`.


**Note:** Sink-related errors are reported once per day per error group.

#### Error logs

The recommended method for inspecting your sink-related errors in detail is to view the error log entries generated by the sink. For details about viewing log entries, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

You can use the following query in the query-editor pane in the Logs Explorer to review your sink's error logs. The same query works in the Logging API and the gcloud CLI.

Before you copy the query, replace the variable SINK_NAME with the name of the sink you're trying to troubleshoot. You can find your sink's name on the **Log Router** page in the Google Cloud console.
    
    
    logName:"logging.googleapis.com%2Fsink_error"
    resource.type="logging_sink"
    resource.labels.name="SINK_NAME"
    

For example, if your sink's name is `my-sink-123`, then the log entry might look similar to the following:
    
    
    {
       errorGroups: [
       0: {
       id: "COXu96aNws6BiQE"
       }]
       insertId: "170up6jan"
       labels: {
          activity_type_name: "LoggingSinkConfigErrorV2"
          destination: "pubsub.googleapis.com/projects/my-project/topics/my-topic"
          error_code: "topic_not_found"
          error_detail: ""
          sink_id: "my-sink-123"
       }
       logName: "projects/my-project/logs/logging.googleapis.com%2Fsink_error"
       receiveTimestamp: "2024-07-11T14:41:42.578823830Z"
       resource: {
       labels: {
          destination: "pubsub.googleapis.com/projects/my-project/topics/my-topic"
          name: "my-sink-123"
          project_id: "my-project"
       }
       type: "logging_sink"
       }
       severity: "ERROR"
       textPayload: "Cloud Logging sink configuration error in my-project, sink my-sink-123: topic_not_found ()"
       timestamp: "2024-07-11T14:41:41.296157014Z"
    }
    

The [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) field `labels` and its nested key-value information helps you target the source of your sink's error; it contains the affected resource, affected sink, and error code. The `labels.error_code` field contains a shorthand description of the error, letting you know which component of your sink needs reconfiguring.

To resolve this failure, [edit your sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#managing_sinks). For example, you might edit your sink by using the **Log Router** page:

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

**Note:** If you're unable to see permission-related sink errors, then verify that you've [enabled Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for the services to which you're sending logs. Data Access audit logs help Google Support troubleshoot issues with your account. Therefore, we recommend enabling Data Access audit logs when possible.

#### Email notifications

[Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) sends sink configuration error email notifications to contacts assigned to the Technical notification category for a Google Cloud project or its parent resource. If the resource does not have a configured contact for Technical notifications, then users listed as IAM **Project Owner** `roles/owner` for the resource receive the email notification.

For each combination of log sink name and error, the system sends one notification per day.

The email message contains the following information:

  * **Resource ID** : The name of the Google Cloud project or other Google Cloud resource where the sink was configured.
  * **Sink name** : The name of the sink that contains the configuration error.
  * **Sink destination** : The full path of the sink's routing destination; for example, `pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID`
  * **Error code** : Shorthand description of the error category; for example, `topic_not_found`.
  * **Error detail** : Detailed information about the error, including recommendations for troubleshooting the underlying error.



The sender of this email is `logging-noreply@google.com`.

The subject is similar to: `Subject: [ACTION REQUIRED] Cloud Logging sink configuration error in my-project`

To view and manage your sinks, use the **Log Router** page:

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

Any sink configuration errors that apply to the resource appear in the list as a `Cloud Logging sink configuration error`. Each error contains a link to one of the log entries generated by the faulty sink. To examine the underlying errors in detail, see the section Error logs.

### Incorrect sink destination

If you set up a sink but then see a configuration error that the destination couldn't be found when Logging attempted to route log entries, here are some possible reasons:

  * Your sink's configuration contains a misspelling or other formatting error in the specified sink destination.

You need to update the sink's configuration to properly specify the existing destination.

  * The specified destination might have been deleted.

You can either change the sink's configuration to use a different, existing destination or recreate the destination with the same name.




To resolve these types of failure, [edit your sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#managing_sinks). For example, you might edit your sink by using the **Log Router** page:

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

Your sink begins routing log entries when the destination is found and new log entries that match your filter are received by Logging.

### Disabled-sink issues

If you [disabled a sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#stopping_logs_ingestion) to stop storing log entries in a log bucket but still see log entries being routed, then wait a few minutes for changes to the sink to apply.

### Permission issues with sinks

**Note:** If you're unable to see permission-related sink errors in your log entries, then verify that you've [enabled Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for the services to which you're sending log entries. Data Access audit logs help Google Support troubleshoot issues with your account. Therefore, we recommend enabling Data Access audit logs when possible.

When a sink tries to route a log entry but lacks the appropriate IAM permissions for the sink's destination, the sink reports an error, which you can view, and skips the log entry.

When you create a sink, the sink's service account must be granted the appropriate [destination permissions](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-auth). If you create the sink in the Google Cloud console in the same Google Cloud project, then the Google Cloud console typically assigns these permissions automatically. However, if you create the sink in a different Google Cloud project, or by using gcloud CLI or the Logging API, then you must configure the permissions manually.

If you're seeing permission-related errors for your sink, then add the necessary permissions or update your sink to use a different destination. For instructions on how to update these permissions, see [Destination permissions](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-auth).

There is a slight delay between creating the sink and using the sink's new service account to authorize writing to the destination. Your sink begins routing log entries when any permissions are corrected and new log entries that match your filter are received by Logging.

### Organizational policy issues with sinks

If you're trying to route a log entry but encounter an [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) that constrains Logging from writing to the sink's destination, then the sink can't route to the selected destination and reports an error.

If you're seeing errors related to organization policies, then you can do the following:

  * Update the organization policy for the destination to remove the constraints blocking the sink from routing log entries; this presupposes that you have the appropriate permissions to update the organization policy.

You might examine whether a Resource Location Restriction (`constraints/gcp.resourceLocations`) exists. This constraint determines the locations where data can be stored. Also, some services support constraints that might affect a log sink. For example, there are several restrictions that might apply when a Pub/Sub destination is selected. For a list of possible constraints, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

For instructions, see [Creating and editing policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies).

  * If you can't update the organization policy, then update your sink in the **Log Router** page to use a compliant destination.

[Go to **Log Router**](https://console.cloud.google.com/logs/router)




Your sink begins routing log entries when the organization policy no longer blocks the sink from writing to the destination and new log entries that match your filter are received by Logging.

### Encryption key issues with sinks

If you're using encryption keys, whether managed with Cloud Key Management Service or by you, to encrypt the data in the sink's destination, then you might see related errors. Here are some possible issues and ways to fix them:

  * Billing isn't being enabled for the Google Cloud project that contains the Cloud KMS key.

    * Even if the sink was successfully created with the correct destination, this error message displays if there isn't a valid billing account associated with the Google Cloud project that contains the key.

    * Make sure there is a valid [billing account linked to the Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/view-linked#view_the_billing_account_linked_to_each_of_your_projects) that contains the key. If a billing account isn't linked to the Google Cloud project, enable billing for that Google Cloud project or use a Cloud KMS key contained by a Google Cloud project that has a valid billing account linked to it.



  * The Cloud KMS key can't be found.

    * The Google Cloud project that contains the Cloud KMS key configured to encrypt the data isn't found.

    * Use a valid Cloud KMS key from an existing Google Cloud project.

  * The location of the Cloud KMS key doesn't match the location of the destination.

    * If the Google Cloud project that contains the Cloud KMS key is located in a region that differs from the region of the destination, then encryption fails and the sink can't route data to that destination.

    * Use a Cloud KMS key contained by a Google Cloud project whose region matches the sink's destination.

  * Encryption key access is denied to the sink's service account.

    * Even if the sink was successfully created with the correct service account permissions, this error message displays if the sink destination uses an encryption key that doesn't give the service account sufficient permissions to encrypt or decrypt the data.

    * Grant the Cloud KMS [CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) for the service account specified in the sink's `writerIdentity` field for the key used in the destination. Also verify that the Cloud KMS API is enabled.




### Quota issues with sinks

When sinks write log entries, export and destination quotas apply. Depending on the destination, quotas are enforced on the resource where the sink was created, such as for Pub/Sub, or on the destination itself, such as for BigQuery. If quota is exhausted, then a sink stops routing log entries to its destination.

  * Sinks that route log entries to a Pub/Sub topic are restricted to 60 GB/min. If the volume of log entries exceeds the export-rate quota, then a log entry with a `topic_over_quota` error code is written.


  * Sinks that route data to BigQuery are restricted to the per-table streaming insert quota. When this quota is exhausted, then a log entry with a `table_resource_exhausted` error code is written.



Quotas also apply to aggregated sinks. These sinks route log entries for the folder or organization in which they were created, and for child resources.

For project-level sinks, the following metric types can help you monitor your quota usage and identify when errors occur:

  * `logging.googleapis.com/exports/byte_count`: Volume, in bytes, of log entries exported to a destination.
  * `logging.googleapis.com/exports/log_entry_count`: Number of log entries exported to a destination.
  * `logging.googleapis.com/exports/error_count`: Number of log entries that failed to export.



To chart a metric type, use the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) and filter the data for a specific destination. These metric types aren't available for folder- or organization-level sinks.

To fix the quota exhaustion issues, try the following:

  * Decrease the amount of log data being routed by updating your sink's filter to match fewer log entries. You might use the [`sample` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#functions) in your filter to select a fraction of the total number of log entries.

  * File a support request to raise your quota.




For details on the limits that might apply when you route log entries, review the appropriate destination's quota information:

  * [Cloud Logging: Quotas & limits](https://docs.cloud.google.com/logging/quotas)


  * [Cloud Storage: Quotas & limits](https://docs.cloud.google.com/storage/quotas)


  * [BigQuery: Quotas & limits](https://docs.cloud.google.com/bigquery/quota-policy#streaminginserts)


  * [Pub/Sub: Quotas & limits](https://docs.cloud.google.com/pubsub/quotas)



### Errors routing to Cloud Storage

The following are the most common errors when routing log entries to Cloud Storage:

  * Late-arriving log entries:

    * Routed log entries are saved to Cloud Storage buckets in hourly batches. It might take from 2 to 3 hours before the first entries begin to appear.

    * Routed log file shards with the suffix `An` ("Append") hold log entries that arrived late. If the Cloud Storage destination experiences an outage, then Cloud Logging buffers the data until the outage is over.

  * Unable to grant correct permissions to the destination:

To resolve this failure, verify that the service account for the log sink has the correct permissions. For more information, see the Permissions issues section of this document.

  * You receive an email notification or see a log entry that indicates an error in the configuration of a log sink. The error code is `bucket_changed_parent_project`.

This error code indicates that the log sink listed in the notification is configured to route log entries to a Cloud Storage bucket and that the parent project of the Cloud Storage bucket has changed. In this scenario, Cloud Logging marks the log sink as misconfigured, which prevents the sink from routing log entries to the Cloud Storage bucket.

To resolve this configuration error, do one of the following:

    * Delete the existing log sink and create a new log sink that routes log entries to the Cloud Storage bucket.

    * Move the Cloud Storage bucket back to the original Google Cloud project.




### Errors routing to BigQuery

The following are the most common errors when routing log entries to BigQuery:

  * Invalid table schema:

    * Log entries streamed to the table in your BigQuery dataset don't match the current table's schema. Common issues include trying to route log entries with different data types, which causes a schema mismatch. For example, one of the fields in the log entry is an integer, while a corresponding column in the schema has a string type.

    * Make sure that your log entries match the table's schema. After you fix the source of the error, you can rename your current table and let Logging create the table again.

    * BigQuery supports loading [nested data](https://docs.cloud.google.com/bigquery/docs/nested-repeated) into its tables. However, when loading data from Logging, the maximum nested depth limit for a column is 13 levels.

When BigQuery identifies a schema mismatch, it creates a table within the corresponding dataset to store the error information. A table's type determines the table name. For date-sharded tables, the naming format is `export_errors_YYYYMMDD`. For partitioned tables, the naming format is `export_errors`. For information about the schema of the error tables and about how to prevent future field-type mismatches, see [Mismatches in schema](https://docs.cloud.google.com/logging/docs/export/bigquery#mismatch).

  * Log entries are outside of the permitted time boundaries:

    * Log entries streamed to the partitioned BigQuery table are outside the permitted time boundaries. BigQuery doesn't accept log entries that are too far in the past or future.

    * You can update your sink to route those log entries to Cloud Storage and use a BigQuery load job. See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/streaming-data-into-bigquery#streaming_into_partitioned_tables) for further instructions.

  * Dataset doesn't allow the service account associated with the log sink to write to it:

    * Even if the sink was successfully created with the correct service account permissions, this error message displays if there isn't a valid billing account associated with the Google Cloud project that contains the sink destination.

    * Make sure there is a [billing account linked to your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/view-linked#view_the_billing_account_linked_to_each_of_your_projects). If a billing account isn't linked to the sink destination Google Cloud project, enable billing for that Google Cloud project or update the sink destination so that it's located in a Google Cloud project that has a valid billing account linked to it.

  * Dataset contains duplicate log entries:

    * Duplicate log entries can occur when there are failures in streaming log entries to BigQuery, including due to retries or misconfigurations. Cloud Logging deduplicates log entries with the same `timestamp` and `insertId` at query time. BigQuery doesn't eliminate duplicate log entries.

    * To ignore duplicate log entries in BigQuery, include the [`SELECT DISTINCT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#select_distinct) clause in your query. For example:
    
    SELECT DISTINCT insertId, timestamp FROM TABLE_NAME
    

  * Log entries are backfilled after a Cloud Logging alert:

Logging automatically generate tables with a `backfill_` prefix as part of a backfill operation that occurs when a Cloud Logging alert prevents routing of log data to BigQuery.

Tables with a `backfill_` prefix contain all log entries that were to be routed to BigQuery during the time range of the alert. These tables might contain some log entries that were successfully routed to the table specified by the sink.

To prevent duplicate data, we recommend merging data from backfill tables into the original tables and then deleting the backfill tables.




### Errors routing to Cloud Logging buckets

You might encounter a situation where you can see log entries in the Logs Explorer that you excluded with your sink. You can still see these log entries if any of following conditions are true:

  * You're running your query in the Google Cloud project that generated the log entries.

To fix this, verify you're running your query in the correct Google Cloud project.

  * The excluded log entries were sent to multiple log buckets; you're seeing a copy of the same log you meant to exclude.

To fix this, check your sinks in the **Log Router** page to verify you aren't including the log entries in other sinks' filters.

  * You have access to [views](https://docs.cloud.google.com/logging/docs/logs-views) in the log bucket where the log entries were sent. In this case, you can see those log entries by default.

To avoid seeing these log entries in the Logs Explorer, you can [refine the scope of your search](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope) to your source Google Cloud project or bucket.




## Troubleshoot storing logs

### Why can't I delete this bucket?

If you're trying to delete a bucket, do the following:

  * Verify that you have the correct permissions to delete the bucket. For the list of the permissions that you need, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

  * Determine whether the bucket is locked by listing the bucket's attributes. If the bucket is locked, check the bucket's retention period. You can't delete a locked bucket until all of the logs in the bucket have fulfilled the bucket's retention period.



  * Verify that the log bucket doesn't have any links. You can't delete a log buckets that contains links.

The following error is shown in response to a `delete` command on a log bucket that has a linked BigQuery dataset:
        
        FAILED_PRECONDITION: This bucket is used for advanced analytics and has an active link. The link must be deleted first before deleting the bucket
        

To list the links associated with a log bucket, run the [`gcloud logging links list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/links/list) command or run the [`projects.locations.buckets.links.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links/list) API method.

To delete links, use the [`gcloud logging links delete`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/links/list) command.




### Which service accounts are routing logs to my bucket?

To determine if any service accounts have IAM permissions to route logs to your bucket, do the following:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. From the **Permissions** tab, view by **Roles**. You see a table with all the IAM roles and principals associated with your Google Cloud project.

  3. In the table's **Filter** **text box** _filter_list_ , enter **Logs Bucket Writer**.

You see any principals with the **Logs Bucket Writer** role. If a principal is a service account, its ID contains the string `gserviceaccount.com`.

  4. Optional: If you want to remove a service account from being able to route logs to your Google Cloud project, select the **check box** _check_box_outline_blank_ for the service account and click **Remove**.




### Why do I see logs for a Google Cloud project even though I excluded them from my `_Default` sink?

You might be viewing logs in a log bucket in a [centralized Google Cloud project](https://docs.cloud.google.com/logging/docs/central-log-storage), which aggregates logs from across your organization.

If you're using the Logs Explorer to access these logs and see logs that you excluded from the `_Default` sink, then your view might be set to the Google Cloud project level.

To fix this issue, select **Log view** in the [Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope) menu and then select the log view associated with the `_Default` bucket in your Google Cloud project. You shouldn't see the excluded logs anymore.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
