---
url: https://docs.cloud.google.com/trace/docs/troubleshooting/
title: Troubleshoot \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:11.052234+00:00
---

# Troubleshoot  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

You can use this document to resolve common issues when working with Cloud Trace, such as missing span data, query failures in Observability Analytics, and validation errors when creating alerting policies.

## Known issues

This section lists known issues:

  * Spans written to your Google Cloud project by using the [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) aren't accessible to the Cloud Trace API. For example, if you try to list these traces, then the command fails with a `404 Not Found` error.



## Troubleshoot Observability Analytics

This section describes how to resolve failures you might see when using Observability Analytics to query your trace data.

### You can't save your alerting policy because of a validation error

You try to save an alerting policy that monitors your trace data and receive an error similar to the following:
    
    
    The following error occurred when validating your SQL Alert: Error authenticating service account `service-12345@gcp-sa-monitoring-notification.iam.gserviceaccount.com`. BigQuery returned an error.
    

This error message indicates that the [Monitoring Service Account](https://docs.cloud.google.com/iam/docs/service-agents#monitoring-service-account) hasn't been granted the required permissions or that it doesn't exist. This account is automatically created by the system when certain user-initiated actions occur. However, if the Cloud Monitoring API is disabled, then the system can't create the service account.

To resolve the failure, do the following:

  1. In the Google Cloud console, go to the **APIs & Services** page and enable the Cloud Monitoring API: 

[Go to **APIs & Services**](https://console.cloud.google.com/apis/dashboard)

  2. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  3. On the **IAM** page, do the following:

     1. Select **Include Google-provided role grants**.

     2. If the Monitoring Service Account isn't listed, then create a SQL-based alerting policy and try to save the policy.

When you save the policy, the system creates the Monitoring Service Account. The save action fails because this service account doesn't have the required IAM roles.

     3. Grant the Monitoring Service Account the following roles:

        * [Monitoring Service Agent (`roles/monitoring.notificationServiceAgent`)](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.NotificationServiceAgent) on your project.
        * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) on your linked BigQuery dataset.
**Note:** We recommend that you restrict the `BigQuery Data Viewer` role grant to the linked BigQuery dataset for your trace data. Don't grant this role at the project level.



### Error message stating a view does not exist

You enter a SQL query in the query pane of the **Observability Analytics** page, but the SQL parser displays the following error:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/views/OBS_VIEW_ID does not exist
    
    

The previous error is reported when the view specified in the `FROM` statement can't be found.

To resolve this error, verify that your view has the proper syntax:

  * Verify that the fully-qualified name of the view follows the syntax required by the Observability Analytics naming scheme. You can find the required syntax for a view by [displaying its default query](https://docs.cloud.google.com/trace/docs/analytics#query-view).

  * If the Google Cloud project ID, location, bucket ID, dataset ID, or view ID contains period characters, `(.)`, then verify that the field is wrapped by single backquotes, `(`)`.

For example, if the ID of your Google Cloud project is `example.com:bluebird`, then the `FROM` statement is as follows:
        
        FROM `example.com:bluebird`.`us`.`_Trace`.`Spans`.`_AllSpans`
        




### Get started with Observability Analytics message is shown

You open the **Observability Analytics** page and it displays a window with a message similar to the following:
    
    
    Get started with Observability Analytics
    

To use Observability Analytics, on the window, click _close_ **Close**.

The previous message is shown when you don't have any log buckets that are upgraded to use Observability Analytics. However, your trace data isn't stored in a log bucket.

### Join of multiple views fails

You write a query that joins multiple views, but the query is marked as invalid.

Not all views can be joined.

To join views, the following restrictions apply:

  1. The locations of the views satisfy one of the following:

     * All views have the same location.
     * All views are in either the `global` or `us` location.
  2. When storage resources use customer managed encryption keys (CMEK), one of the following is be true:

     * Storage resources that use CMEK use the same Cloud KMS key.
     * Storage resources that use CMEK have a common ancestor, and that ancestor specifies a default Cloud KMS key that is in the same location as the storage resources.

When one or more storage resources uses CMEK, the system encrypts temporary data generated by the join with either the common Cloud KMS key or the ancestor's default Cloud KMS key.




For example, suppose that you have two views that reside in the same location. Then you can join these views when any of the following are true:

  * The storage resources don't use CMEK.
  * One storage resource uses CMEK and the other doesn't.
  * Both storage resources use CMEK and both use the same Cloud KMS key.
  * Both storage resources use CMEK but they use different keys. However, the resources share an ancestor that specifies a default Cloud KMS key that is in the same location as the storage resources.

For example, suppose that the resource hierarchy for a log bucket and observability bucket includes the same organization. You can join views on those buckets when, for that organization, you've configured the [default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/default-settings) and for [observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets) with the same default Cloud KMS key for the storage location.




### Creating a linked BigQuery dataset fails with a permission error

You attempt to create a linked BigQuery dataset, but the operation fails with an error similar to the following:
    
    
    ERROR: (gcloud.beta.observability.buckets.datasets.links.create) {
      "code": 7,
      "message": "The caller does not have permission"
    }
    

To resolve this issue, do the following:

  * Make sure that you have been granted the required IAM roles. For a list of these roles, see [Create a link on a dataset](https://docs.cloud.google.com/trace/docs/storage-manage#create-links-on-dataset).

  * Review your organization's policies to determine whether there are constraints that apply to BigQuery datasets. Suppose that you create a custom constraint that requires BigQuery datasets to be in a specific location. For this case, you can only create a linked BigQuery dataset on an observability dataset that is in that specific location.




### Querying a linked BigQuery dataset fails with dataset not found

You issue a query to a linked BigQuery dataset and the command fails with an error message similar to "Dataset not found".

To resolve this problem, try the following:

  * Make sure that the path to the dataset name is correct.
  * Run the following [`gcloud observability buckets datasets links list`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/datasets/links/list) command and verify that the response lists your linked BigQuery dataset.

If your linked BigQuery dataset isn't listed, then the dataset is orphaned. To resolve this scenario, delete the linked BigQuery dataset.

A project can have an orphaned linked BigQuery dataset if you revoke IAM role grants from a service account that Google Cloud Observability uses to manage data and then delete a link on an observability dataset. In that scenario, Google Cloud Observability can't delete the linked BigQuery dataset.




## No data in the **Trace Explorer** page

You have an application that is sending trace data to your Google Cloud project. However, when you open the **Trace Explorer** page, no data is shown.

There are several possible reasons why you can't view trace data:

  * You aren't granted the permissions required to view the data.
  * Trace spans weren't sent to your project.
  * Your application doesn't have the permissions required to write trace data.
  * Your trace spans aren't being stored.



The following subsections provide information about how to troubleshoot the listed failure scenarios.

### Verify that you have permission to view trace data

To view trace data, make sure that you have been granted the [Cloud Trace User role (`roles/cloudtrace.user`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user).

### Verify that trace spans are sent to your project

To verify that spans are being sent to your project, do the following:

  1. Enable the Cloud Trace and Telemetry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudtrace.googleapis.com,telemetry.googleapis.com)

Both APIs can ingest trace spans. However, the Telemetry API is recommended because it is compatible with the OpenTelemetry ecosystem and because it has more generous limits than the Cloud Trace API.

**Note:** There might be org policies in place that have disabled the Cloud Trace API. These policies prevent you from enabling the API.

  2. Go to the **Enabled APIs and Services** page, find the rows for the Cloud Trace API and Telemetry API.

If the **Requests** count for these two APIs is zero, then no trace data is being sent to your project.




### Verify that your application has the required permissions to write trace spans

To determine whether your application has permission to write trace data to your project, do the following:

  1. Go to the **Enabled APIs and Services** page, find the rows for the Cloud Trace API and Telemetry API, and examine the **Errors** column.

  2. If you see a non-zero value in the **Errors** column for either API, then there are errors reading or writing trace data through that API. To identify the type of error, select the API, select the **Metrics** tab, and view the **Errors by API method** :

If writes are failing, then grant the [service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) that is providing credentials the following roles:

     * Cloud Trace API: [Cloud Trace Agent Role (`roles/cloudtrace.agent`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent).
     * Telemetry API: [Cloud Telemetry Trace Writer (`roles/telemetry.tracesWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.tracesWriter).



### Verify that your trace data is stored

Trace spans are stored in an observability bucket named `_Trace`. That bucket is provisioned automatically when your Google Cloud project receives trace spans. However, there are several scenarios where provisioning fails.

To resolve this failure, try one of the following:

  * Google Cloud console instructions: 
    1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.



  1. If you see a banner similar to the following, then that indicates that storage for your trace data isn't provisioned. `none {: .devsite-disable-click-to-copy} Trace storage is not initialized for this project. Enable trace storage to begin collecting trace data.` To provision an observability bucket for your trace data, go to the banner and click **Enable**. When you click **Enable** , a span is sent to your project. After the system receives the span, it issues the command to create an observability bucket named `_Trace`. This process can take several minutes to complete. After provisioning completes, a notification banner appears, and Cloud Trace ingests any trace data that was sent in the last hour. It might take a few minutes for data to appear in the **Trace Explorer**. If you don't see any data, then refresh the page. 
     1. If the enable command fails, then the following message is shown:
            
            Initializing trace storage has failed for an unexpected reason. Please file a support ticket for assistance.
            

To resolve the failure, contact Google Cloud support by clicking **File a ticket**.



  * API instructions:

    1. [List your observability buckets](https://docs.cloud.google.com/trace/docs/storage-manage#list-buckets).
    2. If your project doesn't have a `_Trace` bucket, then create one.

For more information, see [Create an observability bucket](https://docs.cloud.google.com/trace/docs/create-observability-buckets).




## Search for a specific trace fails

You enter a trace ID into the **Trace Explorer** page. The trace isn't found and a message similar to the following is shown:
    
    
    The selected trace with ID abcde does not exist or is older than 30 days and has been deleted per our retention policy.
    

To resolve this failure, try the following:

  1. Verify that the timestamp associated with the trace ID is within the retention period.

  2. Identify the Google Cloud project that stores the trace, and verify that the resource picker in the Google Cloud console selects this project. By default, the **Trace Explorer** page only has access to trace data stored in the selected project.




## Missing older data in the **Trace Explorer** page

You are using the **Trace Explorer** page and you can view recent data, but when you set the time-range selector to 30 days or to a larger value, the older data isn't shown.

The **Trace Explorer** page doesn't display data for time periods that are larger than the data retention period of Cloud Trace, which is 30 days.

If the time-range selector is 30 days or less, then the missing data indicates that the database queried by the **Trace Explorer** page was created more recently than your time-range setting. For example, if you set this value to 20 days and you can only see the most recent 10 days of data, then the database was created 10 days in the past. Also, this database only contains traces that were sent to your Google Cloud project after the database was created.

## Incomplete trace is shown

You open the **Trace Explorer** page and select a span to view. The **Details** flyout shows the trace, but the trace isn't complete. Some spans aren't shown.

Spans might be missing for the following reasons:

  * The **Trace Explorer** page isn't searching all Google Cloud projects that store span data for the trace.

  * Your IAM role on a Google Cloud project that stores span data for the trace doesn't contain the permissions necessary to view trace data.

  * There is an instrumentation issue. For example, only some spans in a trace were sent to your Google Cloud project.




To resolve these problems, do the following:

  1. In the **Trace Explorer** page, make sure to set the **Scope** element to a trace scope that lists projects that store the spans for the selected trace.

If there isn't a trace scope that includes the projects that you identified in the previous step, then create or modify an existing trace scope. For more information, see [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).

  2. Verify you have the Cloud Trace User role (`roles/cloudtrace.user`) on the projects that store the span data.




## You don't have the required permissions to view trace data

You are viewing the **Trace Explorer** page and see the following notification:
    
    
    You don't have the required permissions to view trace data for one or more projects listed in the trace scope.
    

To resolve this message, in the toolbar, do the following:

  1. Expand the **Scope** element and identify the selected trace scope.
  2. In the **Refine scope** flyout, select **Manage scopes**.
  3. Locate the trace scope you identified in the first step, and then expand the details to view the list of Google Cloud projects.
  4. For each Google Cloud project in the trace scope, verify that you have the role of Cloud Trace User (`roles/cloudtrace.user`). If you don't have that role on a project, then ask an administrator or project owner to grant you that role.



## Cross-regional queries are not supported

You open the **Trace Explorer** page and it displays a message similar to the following:
    
    
    Error loading chart data. Cross-regional queries are not supported. The selected scope comprises buckets residing in multiple locations: list of locations.
    

The error message indicates that the **Trace Explorer** page needs to issue a query for data that is stored in different locations.

To resolve this failure, do one of the following:

  * Restrict trace data to that which is stored by your selected project:

    * Go to the toolbar of the **Trace Explorer** page and expand the **Scope** menu.
    * In the **Refine scope** flyout, select **Current project**.
  * Select a trace scope that lists projects whose data is stored in the same location. To make this change, use the options in the **Scope** menu.

  * Remove from the selected trace scope those projects whose data is stored in a different location than your selected project:

    * Go to the toolbar of the **Trace Explorer** page and expand the **Scope** menu.
    * In the **Refine scope** flyout, select **Manage scopes**.
    * From the **Trace scopes** page, you can edit any trace scope.

To find the storage location of your trace data, run the [List observability buckets](https://docs.cloud.google.com/trace/docs/storage-manage#list-buckets) command. In the path parameter specify your project, and for the LOCATION, set the field to a hyphen, `(-)`, which acts as a wildcard.




## Missing span ID message in trace

Your trace contains a "Missing span ID" message.

In distributed tracing systems, incomplete traces are expected. A trace is incomplete when a sampled span contains a reference to another span that hasn't been received. The unresolved reference can occur for the following reasons:

  * The referenced span wasn't sampled.
  * The referenced span was sampled but hasn't yet been received by Cloud Trace or the span was received but not stored.



When you are viewing an incomplete trace, Cloud Trace displays the message "Missing span ID" on the trace details pane.

If you are consistently seeing the message "Missing span ID", then try the following:

  * For components that you manage, verify that they respect and propagate the header's [`sampled` flag](https://www.w3.org/TR/trace-context/#sampled-flag), when this field is present. This setting is a hint to child components to sample the request. For more information about trace headers, see [Protocols for context propagation](https://docs.cloud.google.com/trace/docs/trace-context#context-propagation-protocols).

Google Cloud services typically respect this hint. However, they also limit the rate at which they write trace data.

  * If you are using Cloud Service Mesh, then verify that you follow the guidance for propagating the trace context for those configurations. For Cloud Service Mesh guidance, see [Trace context propagation](https://docs.cloud.google.com/service-mesh/docs/observability/accessing-traces#trace_context_propagation).




## Unable to correlate log and trace data

You are doing one of the following:

  * You are viewing a trace span and you want to view associated log entries. However, either no log data is listed or, when you open the **Logs Explorer** page, it doesn't show any log entries.

  * You are viewing a log entry and you want to view associated trace spans. However, when you use the options on the log entry to open the **Trace Explorer** page, it doesn't show any trace data.




To resolve these failures, configure the observability scope. This scope specifies which of your trace scopes and log scopes to use when the corresponding explorer pages open. For more information, see [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes).

## No trace data after updating Go app to use OpenTelemetry

Your application relies on the client library to capture traces, and after updating your application to use OpenTelemetry, you no longer see Cloud Trace data.

Because some Cloud Client Libraries for Go are integrated with OpenCensus, you must use an OpenCensus Bridge. For more information about the problem solved by the bridge, see [OpenCensus Bridge](https://github.com/open-telemetry/opentelemetry-go/tree/main/bridge/opencensus).

For information about the update of the Cloud Client Libraries for Go, see [Issue #4237](https://github.com/googleapis/google-cloud-go/issues/4237).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
