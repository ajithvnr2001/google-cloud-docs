---
url: https://docs.cloud.google.com/logging/docs/export/configure_export_v2/
title: Route logs to supported destinations \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:58.782566+00:00
---

# Route logs to supported destinations  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/export/configure_export_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Route logs to supported destinations Stay organized with collections  Save and categorize content based on your preferences. 

You can use log [sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) in Cloud Logging to route log entries from your Google Cloud project to supported destinations for long-term storage, analytics, or streaming.

A [sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) performs a write action, and therefore it must be authorized to write to the destination. When the destination is a log bucket in the same project as the sink, the sink is automatically authorized. For all other destinations, the sink must be attached to a [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) that has been given the permissions required to write data to the destination.

When a service account is required, Cloud Logging automatically creates and manages it. However, you might need to modify the permissions given to the service account. You don't have to use the service account created by Logging. You can create and manage a service account that is used by sinks in multiple projects. For more information, see [Configure log sinks with user-managed service accounts](https://docs.cloud.google.com/logging/docs/routing/user-managed-service-accounts).

**Note:** If your data is managed through an [Assured Workloads environment](https://docs.cloud.google.com/assured-workloads/docs/key-concepts), then this feature might be impacted or restricted. For information, see [Restrictions and limitations in Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/eu-sovereign-controls-restrictions-limitations#features_logging).

## Overview

This document describes how to create a sink and how to configure the options you might see when using the Google Cloud console, the Google Cloud CLI, or the API.

Sinks belong to a given Google Cloud resource: a Google Cloud project, a billing account, a folder, or an organization. When the resource receives a log entry, every sink in the resource processes the log entry. When a log entry matches the filters of the sink, then the log entry is routed to the sink's destination.

Typically, sinks route only the log entries that originate in a resource. However, for folders and organizations you can create _aggregated sinks_. These sinks route log entries that originate in the folder or organization and that originate in its [child resources](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). This document doesn't discuss aggregated sinks. For more information, see [Aggregated sinks overview](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview).

To create and manage sinks, you can use the Google Cloud console, the Cloud Logging API, and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). We recommend that you use the Google Cloud console for the following reasons:

  * You can configure sink destinations as part of the flow to create a sink.
  * You can preview which log entries match the sink's filters.
  * Some authorization steps are simplified.



We recommend that you review your log sink configuration when you make any changes to your log storage. For example, if you delete the destination of a log sink, then delete the corresponding log sink.

For information about viewing and managing your log sinks, see the Manage sinks section of this document.

## Supported destinations

**Note:** To use the visualization and analysis tools of Cloud Logging or to use Error Reporting, you must store your log entries in log buckets. These log buckets don't have to be in the same resource where the log entries originate. For example, you might configure an aggregated sink to route log entries to a Google Cloud project, and then configure the sinks in that project to reroute the log entries to local log buckets.

The destination of a sink can be in a different resource from the sink. For example, you can use a log sink to route log entries from one project to a log bucket stored in a different project.

The following destinations are supported:

Google Cloud project
    

Select this destination when you want the log sinks in the destination project to reroute your log entries, or when you have created an intercepting aggregated sink. The log sinks in the destination project can reroute the log entries to any supported destination except a project.

The system-created log sinks in the destination project exclude log entries that are routed to the `_Required` log bucket in the source project. For example, if you route Admin Activity logs to another project, then both the `_Required` and `_Default` log sinks in the destination project exclude those log entries. To store those log entries, in the destination project update the [`_Default` log sink](https://docs.cloud.google.com/logging/docs/routing/overview#default-sink) or create a custom log sink.

**Note:** This is the only type of destination where log entries are rerouted. For example, if you route log entries from one project to a log bucket in another project, then those log entries aren't rerouted by the log sinks in the project that stores the log bucket.

Log bucket
    

Select this destination when you want to store your log data in resources managed by Cloud Logging. Log data stored in log buckets can be viewed and analyzed using services like the Logs Explorer and Observability Analytics.

If you want to join your log data with other business data, then you can store your log data in a log bucket and create a linked BigQuery dataset. A linked BigQuery dataset is read-only, but you can query it like any other BigQuery dataset.

BigQuery dataset
    Select this destination when you want to join your log data with other business data. The dataset you specify must be write-enabled. **Don't set the destination of a sink to be a linked BigQuery dataset**. Linked BigQuery datasets are read-only.

Cloud Storage bucket
    Select this destination when you want long-term storage of your log data. The Cloud Storage bucket can be in the project where the log entries originate, or in a different project. Log entries are stored as JSON files.

Pub/Sub topic
    Select this destination when you want to export your log data from Google Cloud and then use third-party integrations like Splunk or Datadog. Log entries are formatted as JSON and then routed to a Pub/Sub topic.

### Destination limitations

This section describes destination-specific limitations:

  * When you configure a sink destination, provide the fully qualified path and use the service's global endpoint. [Regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) (REPs), such as `pubsub.LOCATION.rep.googleapis.com`, aren't supported.


  * If you route log entries to a log bucket in a different Google Cloud project, then Error Reporting doesn't analyze those log entries. For more information, see [Error Reporting overview](https://docs.cloud.google.com/error-reporting/docs/grouping-errors).


  * The following limitations apply when the destination of a log sink is a BigQuery dataset:

    * The BigQuery dataset must be write-enabled. Don't set the destination to a linked BigQuery dataset. Linked datasets are read-only.
    * Logging creates a table inside the dataset for each log name. You can't rename a table while a sink is streaming data into it.


  * New sinks that route log entries to Cloud Storage buckets might take several hours to start routing log entries. These sinks are processed hourly.


  * Routing logs to a Pub/Sub topic that enforces [in-transit restrictions](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) isn't supported. Logging can't guarantee that publish requests originate from an allowed region, which causes [`topic_region_not_allowed`](https://docs.cloud.google.com/logging/docs/export/troubleshoot#topic_region_not_allowed) configuration errors and dropped logs.

  * The following limitations apply when the destination of a log sink is a Google Cloud project:

    * There is a one-hop limit.
    * The [`_Required` log sink](https://docs.cloud.google.com/logging/docs/routing/overview#required-sink) in the destination project routes log entries to the project's `_Required` log bucket **when the log entries match the sink's filter and originate in the destination project**.
    * The [`_Default` log sink](https://docs.cloud.google.com/logging/docs/routing/overview#default-sink) in the destination project routes log entries that match its inclusion filter and don't match any exclusion filter. **The`_Default` log sink excludes some log entries**. For example, this sink doesn't route Admin Activity and System Event log entries. You can modify this sink.
    * Only aggregated sinks that are in the resource hierarchy of a log entry process the entry.

For example, assume the destination of a log sink in project `A` is project `B`. In this case, the following rules apply:

    * Due to the one-hop limit, the log sinks in project `B` can't reroute log entries to another Google Cloud project.
    * The `_Required` log bucket of project `B` only stores log entries that originate in project `B`. This log bucket doesn't store any log entries that originate in any other resource, including those that originate in project `A`.
    * If project `A` and project `B` have different resource hierarchies, then a log entry that a log sink in project `A` routes to project `B` isn't sent to the aggregated sinks in the resource hierarchy of project `B`.
    * If project `A` and project `B` have the same resource hierarchy, then log entries are sent to the aggregated sinks in that hierarchy. If a log entry isn't intercepted by an aggregated sink, then the Log Router sends the entry to the sinks in project `A`.



## Before you begin

The instructions in this document describe creating and managing sinks at the Google Cloud project level. You can use the same procedure to create a sink that routes log entries that originate in an organization, folder, or billing account.

To get started, do the following:

  1. Enable the Cloud Logging API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com)

  2. Make sure that your Google Cloud project contains log entries that you can see in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  3. To get the permissions that you need to create, modify, or delete a sink, ask your administrator to grant you the [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information about granting IAM roles, see the Logging [Access control guide](https://docs.cloud.google.com/logging/docs/access-control).

  4. Ensure that you have a resource in a supported destination or have the ability to create one.

To route log entries to a destination, the destination must exist before you create the sink. You can create the destination in any Google Cloud project in any organization.

  5. Before you create a sink, review the limitations that apply to the sink destination. For more information, see the Destination limitations section in this document.

  6. Select the interface you plan to use:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Create a sink

This section describes how to create a sink in a Google Cloud project. You can create up to 200 sinks per Google Cloud project. To view the number and volume of log entries that are routed, view the [`logging.googleapis.com/exports/` metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-logging).

You use the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) to create a filter expression that matches the log entries you want to include. Don't put sensitive information in sink filters. Sink filters are treated as service data.

When a query contains multiple statements, you can either specify how those statements are joined or rely on Cloud Logging implicitly adding the conjunctive restriction, `AND`, between the statements. For example, suppose a query or filter dialog contains two statements, `resource.type = "gce_instance"` and `severity >= "ERROR"`. The actual query is `resource.type = "gce_instance" AND severity >= "ERROR"`. Cloud Logging supports both disjunctive restrictions, `OR`, and conjunctive restrictions, `AND`. When you use `OR` statements, we recommend that you group the clauses with parentheses. 

**Note:** Log entries sent to your project don't contain error group information. This means that log sinks can't filter by error group. It also means that the log data sent to destinations doesn't contain error group information. If you route logs to the log-bucket destination, then that destination adds error group information to log entries when it stores them in a log bucket.

To create a sink, do the following:

### Console

  1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select the Google Cloud project in which the log entries that you want to route originate.

For example, if you want to route your Data Access log entries from the project named `Project-A` to a log bucket in the project named `Project-B`, then select `Project-A`.

  3. Select **Create sink**.

  4. In the **Sink details** panel, enter the following details:

     * **Sink name** : Enter an identifier for the sink. After you create the sink, you can't rename it, but you can delete it and create a new sink.

     * **Sink description** (optional): Describe the purpose or use case for the sink.

  5. In the **Sink destination** panel, select the sink service and destination by using the **Select sink service** menu. Do one of the following:

     * To route log entries to a service that is in the same Google Cloud project, select one of the following options:

       * **Cloud Logging bucket** : Select or create a [Logging bucket](https://docs.cloud.google.com/logging/docs/store-log-entries).
       * **BigQuery dataset** : Select or create the write-enabled dataset to receive the routed log entries. You also have the option to use [partitioned tables](https://docs.cloud.google.com/logging/docs/export/bigquery#partition-tables).
**Note:** Don't select a linked BigQuery dataset for your destination. These datasets are read-only and can't be the destination for a log sink.
       * **Cloud Storage bucket** : Select or create the Cloud Storage bucket to receive the routed log entries.
       * **Pub/Sub topic** : Select or create the topic to receive the routed log entries.
**Note:** Don't select a Pub/Sub topic that enforces [in-transit restrictions](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction). Because log sinks must use global endpoints, Logging can't guarantee that publish requests originate from an allowed region, which causes [`topic_region_not_allowed`](https://docs.cloud.google.com/logging/docs/export/troubleshoot#topic_region_not_allowed) configuration errors and dropped logs.
       * **Splunk** : Select the Pub/Sub topic for your [Splunk](https://docs.cloud.google.com/architecture/exporting-stackdriver-logging-for-splunk) service.
     * To route log entries to a different Google Cloud project, select **Google Cloud project** , and then enter the fully qualified name for the destination:
           
           logging.googleapis.com/projects/DESTINATION_PROJECT_ID
           

     * To route log entries to a service that is in a different Google Cloud project, do the following:

       1. Select **Other resource**.
       2. Enter the fully qualified name for the destination. For information about the syntax, see the Destination path formats.
  6. Specify the log entries to include:

     1. Go to the **Choose logs to include in sink** panel.

     2. In the **Build inclusion filter** field, enter a filter expression that matches the log entries you want to include. For syntax information, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

If you don't set a filter, all log entries from your selected resource are routed to the destination.

For example, to route all Data Access log entries to a Logging bucket, you can use the following filter:
            
            log_id("cloudaudit.googleapis.com/data_access") OR log_id("externalaudit.googleapis.com/data_access")
            

The length of a filter can't exceed 20,000 characters.

     3. To verify that you entered the correct filter, select **Preview logs**. The Logs Explorer opens in a new tab with the filter pre-populated.

  7. (Optional) Configure an exclusion filter to eliminate some of the included log entries:

     1. Go to the **Choose logs to filter out of sink** panel.

     2. In the **Exclusion filter name** field, enter a name.

     3. In the **Build an exclusion filter** field, enter a [filter expression](https://docs.cloud.google.com/logging/docs/view/logging-query-language) that matches the log entries you want to exclude. You can also use the [`sample` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#functions) to select a portion of the log entries to exclude.

**Note:** If you want your exclusion filter to be disabled when the sink is created, then select **Disable** after you enter your filter expression. You can update the sink later to enable the exclusion filter.

You can create up to 50 exclusion filters per sink. Note that the length of a filter can't exceed 20,000 characters.

  8. Select **Create sink**.

  9. Grant the sink's service account permission to write log entries to your sink's destination. For more information, see Set destination permissions.




### gcloud

To create a sink, do the following:

  1. Run the following [`gcloud logging sinks create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create) command:
         
         gcloud logging sinks create SINK_NAME SINK_DESTINATION
         

Before running the command, make the following replacements:

     * SINK_NAME: The name of the log sink. You can't change the name of a sink after you create it.
     * SINK_DESTINATION: The service or project to where you want your log entries routed. Set SINK_DESTINATION to the appropriate path, as described in Destination path formats.

For example, if your sink destination is a Pub/Sub topic, then SINK_DESTINATION looks like the following:
           
           pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID
           

You can also provide the following options:

     * `--log-filter` : Use this option to set a [filter](https://docs.cloud.google.com/logging/docs/view/logging-query-language) that matches the log entries you want to include in your sink. If you don't provide a value for the inclusion filter, then this filter matches all log entries.
     * `--exclusion`: Use this option to set an exclusion filter for log entries that you don't want your sink to route. You can also use the [`sample` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#functions) to select a portion of the log entries to exclude. This option can be repeated; you can create up to 50 exclusion filters per sink.
     * `--description`: Use this option to describe the purpose or use case for the sink.

For example, to create a sink to a Logging bucket, your command might look like this:
    
    gcloud logging sinks create my-sink logging.googleapis.com/projects/myproject123/locations/global/buckets/my-bucket \
     --log-filter='logName="projects/myproject123/logs/matched"' --description="My first sink"
    

For more information about creating sinks by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), see the [`gcloud logging sinks`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks) reference.

  2. If the command response contains a JSON key labeled `"writerIdentity"`, then grant the sink's service account permission to write to the sink destination. For more information, see Set destination permissions.

You don't need to set destination permissions when the response doesn't contain a JSON key labeled `"writerIdentity"`.




### REST

  1. To create a logging sink in your Google Cloud project, use [`projects.sinks.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/create) in the Logging API. In the [`LogSink`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks#LogSink) object, provide the appropriate required values in the method request body:

     * `name`: An identifier for the sink. After you create the sink, you can't rename it, but you can delete it and create a new sink.
     * `destination`: The service and destination where you want your log entries routed. To route log entries to a different project, or to a destination that is in another project, set the `destination` field to the appropriate path, as described in Destination path formats.

For example, if your sink destination is a Pub/Sub topic, then the `destination` looks like the following:
           
           pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID
           

  2. In the [`LogSink`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks#LogSink) object, provide the appropriate optional information:

     * `filter` : Set the [`filter`](https://docs.cloud.google.com/logging/docs/view/logging-query-language) field to match the log entries you want to include in your sink. If you don't set a filter, all log entries from your Google Cloud project are routed to the destination. Note that the length of a filter can't exceed 20,000 characters.
     * `exclusions`: Set this field to match the log entries that you want to exclude from your sink. You can also use the [`sample` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#functions) to select a portion of the log entries to exclude. You can create up to 50 exclusion filters per sink.
     * `description`: Set this field to describe the purpose or use case for the sink.
  3. Call [`projects.sinks.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/create) to create the sink.

  4. If the API response contains a JSON key labeled `"writerIdentity"`, then grant the sink's service account permission to write to the sink destination. For more information, see Set destination permissions.

You don't need to set destination permissions when the API response doesn't contain a JSON key labeled `"writerIdentity"`.




For more information about creating sinks by using the Logging API, see the [`LogSink`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks#LogSink) reference.

If you receive error notifications, then see [Troubleshoot routing and sinks](https://docs.cloud.google.com/logging/docs/export/troubleshoot).

### Destination path formats

When you configure a sink destination, provide the fully qualified path and use the service's global endpoint. [Regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) (REPs), such as `pubsub.LOCATION.rep.googleapis.com`, aren't supported.

In the following path formats, DESTINATION_PROJECT_ID refers to the ID or number of the destination project:

  * Cloud Logging log bucket:
        
        logging.googleapis.com/projects/DESTINATION_PROJECT_ID/locations/LOCATION/buckets/BUCKET_NAME
        

  * Another Google Cloud project:
        
        logging.googleapis.com/projects/DESTINATION_PROJECT_ID
        



  * BigQuery dataset:
        
        bigquery.googleapis.com/projects/DESTINATION_PROJECT_ID/datasets/DATASET_ID
        

**Note:** To be a valid sink destination, DATASET_ID must be write-enabled. Don't select a linked BigQuery dataset; these datasets are read-only.


  * Cloud Storage bucket:
        
        storage.googleapis.com/BUCKET_NAME
        



  * Pub/Sub topic:
        
        pubsub.googleapis.com/projects/DESTINATION_PROJECT_ID/topics/TOPIC_ID
        




## Set destination permissions

This section describes how to grant Logging the Identity and Access Management permissions to write log entries to your sink's destination. For the full list of Logging roles and permissions, see [Access control](https://docs.cloud.google.com/logging/docs/access-control).

**Note:** To secure routed log entries from unauthorized access, you must use the access control features of the destination. Sinks can route any log entries, including Access Transparency log entries and Data Access audit log entries. If the routed log entries produce [Error Reporting data](https://docs.cloud.google.com/error-reporting/docs/grouping-errors) in the destination, then you must also configure Error Reporting access control features. For more information about Error Reporting access control, see [Control access with IAM](https://docs.cloud.google.com/error-reporting/docs/iam).

Cloud Logging creates a shared service account for a resource when a sink is created, unless the required service account already exists. The service account might exist because the same service account is used for all sinks in the underlying resource. A resource can be a Google Cloud project, an organization, a folder, or a billing account.

The **writer identity** of a sink is the identifier of the service account associated with that sink. All sinks have a writer identity except for sinks that write to a log bucket in the same Google Cloud project in which the log entries originate. For the latter configuration, a service account isn't required, and therefore the sink's **writer identity** field is listed as `None` in the console. The API and the Google Cloud CLI commands don't report a writer identity.

The following instructions apply to projects, folders, organizations, and billing accounts:

### Console

**Note:** If you created your sink in the Google Cloud console and you have **Owner** access to the destination, then Cloud Logging should have set up the necessary permissions on your behalf. If not, then complete the following steps:

  1. Make sure that you have **Owner** access to the Google Cloud project that contains the destination. If you don't have **Owner** access to the destination of the sink, then ask a project owner to add the writer identity as a principal.

  2. To get the sink's writer identity—an email address—from the new sink, do the following:

     1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     2. In the toolbar, select the project that contains the sink.
     3. Select _more_vert_ **Menu** and then select **View sink details**. The writer identity appears in the **Sink details** panel.
  3. If the value of the `writerIdentity` field contains an email address, then proceed to the next step. When the value is `None`, you don't need to configure destination permissions for the sink.

  4. Copy the sink's writer identity to your clipboard.

The email address identifies the principal. The prefix, `serviceAccount:`, specifies the account type.

  5. Grant the principal specified in the sink's writer identity permission to write log data to the destination:

     1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

     2. In the toolbar, make sure that the selected project is either the project that stores the destination or is the sink destination. For example, if the destination is a log bucket, then make sure that the toolbar displays the project that stores the log bucket.

     3. Select person_add **Grant access**.

     4. Grant the principal specified in the sink's writer identity an IAM role based on the destination of the log sink:

        * For all destinations, grant the [Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.logWriter`). Specifically, a principal needs the `logging.logEntries.route` permission. 
        * Grant one of the following roles based on the destination: 
          * Log bucket: Grant the [Logs Bucket Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.bucketWriter`). 
          * Cloud Storage bucket: Grant the [Storage Object Creator role](https://docs.cloud.google.com/iam/docs/understanding-roles#storage) (`roles/storage.objectCreator`). 
          * BigQuery dataset: Grant the [BigQuery Data Editor role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) (`roles/bigquery.dataEditor`). 
          * Pub/Sub topic, including Splunk: Grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/pubsub/docs/access-control#roles) (`roles/pubsub.publisher`). 



### gcloud

  1. Make sure that you have **Owner** access to the Google Cloud project that contains the destination. If you don't have **Owner** access to the destination of the sink, then ask a project owner to add the writer identity as a principal.

  2. Get the service account from the `writerIdentity` field in your sink:
         
         gcloud logging sinks describe SINK_NAME
         

  3. Locate the sink whose permissions you want to modify, and if the sink details contain a line with `writerIdentity`, then proceed to the next step. When the details don't include a `writerIdentity` field, you don't need to configure destination permissions for the sink.

The writer identity for the service account looks similar to the following:
         
         serviceAccount:service-123456789012@gcp-sa-logging.iam.gserviceaccount.com
         

  4. Grant the sink's writer identity permission to write log data to the destination by calling the `gcloud projects add-iam-policy-binding` command.

Before using the following command, make the following replacements:

     * PROJECT_ID: The identifier of the project. Specify the project that stores the destination of the log sink. When the destination is a project, specify that project.
     * PRINCIPAL: An identifier for the principal that you want to grant the role to. Principal identifiers usually have the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com`. For a full list of the formats that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).
     * ROLE: An IAM role. Grant the sink's writer identity an IAM role based on the destination of the log sink:

       * For all destinations, grant the [Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.logWriter`). Specifically, a principal needs the `logging.logEntries.route` permission. 
       * Grant one of the following roles based on the destination: 
         * Log bucket: Grant the [Logs Bucket Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.bucketWriter`). 
         * Cloud Storage bucket: Grant the [Storage Object Creator role](https://docs.cloud.google.com/iam/docs/understanding-roles#storage) (`roles/storage.objectCreator`). 
         * BigQuery dataset: Grant the [BigQuery Data Editor role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) (`roles/bigquery.dataEditor`). 
         * Pub/Sub topic, including Splunk: Grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/pubsub/docs/access-control#roles) (`roles/pubsub.publisher`). 

Execute the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member=PRINCIPAL --role=ROLE
    




### REST

We recommend that you use the Google Cloud console or the Google Cloud CLI to grant a role to the service account.

## Manage sinks

We recommend that you review your log sink configuration when you make any changes to your log storage. For example, if you delete the destination of a log sink, then delete the corresponding log sink.

After your sinks are created, you can perform the following actions on them. Any changes made to a sink might take a few minutes to apply:

  * View details
  * Update
  * Disable

    * You can't disable the `_Required` sink.
    * You can disable the `_Default` sink to stop it from routing log entries to the `_Default` Logging bucket.

You can disable the `_Default` sink for any new Google Cloud projects or folders you create in your organization or folder by configuring [default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/default-settings).

**Note:** Log sinks route log entries in real time. Disabling a log sink stops routing new log entries but doesn't affect log entries that were previously routed. If you re-enable a log sink, the sink only routes new log entries. Previously received log entries aren't backfilled.
  * Delete

    * You can't delete the `_Default` or the `_Required` sinks.
    * When you delete a sink, it no longer routes log entries.
    * If the sink has a dedicated service account, then deleting that sink also deletes the service account. Sinks created before May 22, 2023 have dedicated service accounts. Sinks created on or after May 22, 2023 have a shared service account. Deleting the sink doesn't delete the shared service account.
  * Troubleshoot failures



  * View log volume and error rates



The following are the instructions for managing a sink in a Google Cloud project. Instead of a Google Cloud project, you can specify a billing account, folder, or organization:

### Console

  1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the toolbar, select the resource that contains your sink. The resource can be a project, folder, organization, or billing account.




The **Log Router** page displays the sinks in the selected resource. Each table row contains information about a sink's properties:

  * **Enabled** : Indicates if the sink's state is enabled or disabled.
  * **Type** : The sink's destination service; for example, `Cloud Logging bucket`.
  * **Name** : The sink's identifier, as provided when the sink was created; for example, `_Default`.
  * **Description** : The sink's description, as provided when the sink was created.
  * **Destination** : Full name of the destination to which the routed log entries are sent.
  * **Created** : The date and time that the sink was created.
  * **Last updated** : The date and time that the sink was last edited.
  * **Volume** : Reports the total volume of logs routed to the log sink. The value includes the volume routed to log buckets, projects, or to other destinations.



For each table row, the _more_vert_ **More actions** menu provides the following options:

  * **View sink details** : Displays the sink's name, description, destination service, destination, and inclusion and exclusion filters. Selecting **Edit** opens the **Edit Sink** panel.
  * **Edit sink** : Opens the **Edit Sink** panel where you can update the sink's parameters.
  * **Disable sink** : Lets you disable the sink and stop routing log entries to the sink's destination. For more information about disabling sinks, see Stop storing logs in log buckets.
  * **Enable sink** : Lets you enable a disabled sink and restart routing log entries to the sink's destination.
  * **Delete sink** : Lets you delete the sink and stop routing log entries to the sink's destination.
  * **Troubleshoot sink** : Opens the Logs Explorer where you can troubleshoot errors with the sink.
  * **View sink log volume and error rates** : Opens the Metrics Explorer where you can view and analyze data from the sink.



To sort the table by a column, select the column name.

### gcloud

  * To view your list of sinks for your Google Cloud project, use the [`gcloud logging sinks list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/list) command, which corresponds to the Logging API method [`projects.sinks.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/list):
        
        gcloud logging sinks list
        

To view your list of [aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview), use the appropriate option to specify the resource that contains the sink. For example, if you created the sink at the organization level, use the `--organization=ORGANIZATION_ID` option to list the sinks for the organization.

  * To describe a sink, use the [`gcloud logging sinks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/describe) command, which corresponds to the Logging API method [`projects.sinks.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/get):
        
        gcloud logging sinks describe SINK_NAME
        

  * To update a sink, use the [`gcloud logging sinks update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update) command, which corresponds to the API method [`projects.sinks.update`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/update).

You can update a sink to change the destination, filters, and description, or to disable or re-enable the sink:
        
        gcloud logging sinks update SINK_NAME NEW_DESTINATION --log-filter=NEW_FILTER

Omit the NEW_DESTINATION or `--log-filter` if those parts don't change.

For example, to update the destination of your sink named `my-project-sink` to a new Cloud Storage bucket destination named `my-second-gcs-bucket`, your command looks like this:
        
        gcloud logging sinks update my-project-sink storage.googleapis.com/my-second-gcs-bucket
        

  * To disable a sink, use the [`gcloud logging sinks update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update) command, which corresponds to the API method [`projects.sinks.update`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/update), and include the `--disabled` option:
        
        gcloud logging sinks update SINK_NAME --disabled
        

To re-enable the sink, use the [`gcloud logging sinks update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update) command, remove the `--disabled` option, and include the `--no-disabled` option:
        
        gcloud logging sinks update SINK_NAME --no-disabled
        

  * To delete a sink, use the [`gcloud logging sinks delete`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/delete) command, which corresponds to the API method [`projects.sinks.delete`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/delete):
        
        gcloud logging sinks delete SINK_NAME
        

For more information about managing sinks by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), see the [`gcloud logging sinks`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks) reference.




### REST

  * To view the sinks for your Google Cloud project, call [`projects.sinks.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/list).

  * To view a sink's details, call [`projects.sinks.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/get).

  * To update a sink, call [`projects.sinks.update`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/update).

You can update a sink's destination, filters, and description. You can also disable or re-enable the sink.

  * To disable a sink, set the `disabled` field in the `LogSink` object to `true`, and then call [`projects.sinks.update`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/update).

To re-enable the sink, set the `disabled` field in the `LogSink` object to `false`, and then call [`projects.sinks.update`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/update).

  * To delete a sink, call [`projects.sinks.delete`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/delete).

For more information about managing sinks by using the Logging API, see the [`LogSink`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks#LogSink) reference.




## Stop storing log entries in log buckets

**Note:** If you want to disable the `_Default` sinks created in your organization, then configure the [default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/default-settings).

You can disable the `_Default` sink and any user-defined sinks. When you disable a sink, the sink stops routing new log entries to its destination. For example, if you disable the `_Default` sink, then no log entries are routed to the [`_Default` bucket](https://docs.cloud.google.com/logging/docs/routing/overview). The `_Default` bucket becomes empty when all of the previously stored log entries have reached the end of the bucket's [retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).

The following instructions illustrate how to disable a Google Cloud project's `_Default` sink so that it doesn't route log entries to the `_Default` log bucket:

### Console

  1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. To find all the sinks that route log entries to the `_Default` log bucket, filter the sinks by destination, and then enter `_Default`.
  3. For each sink, select _more_vert_ **Menu** and then select **Disable sink**.

The sinks are now disabled and no longer route log entries to the `_Default` bucket.




To re-enable a disabled sink and restart routing log entries to the sink's destination, do the following:

  1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. To find all the sinks that route log entries to the `_Default` log bucket, filter the sinks by destination, and then enter `_Default`.
  3. For each sink, select _more_vert_ **Menu** and then select **Enable sink**.



### gcloud

  1. To view your list of sinks for your Google Cloud project, use the [`gcloud logging sinks list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/list) command, which corresponds to the Logging API method [`projects.sinks.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/list):
         
         gcloud logging sinks list
         

  2. Identify any sinks that are routing to the `_Default` log bucket. To describe a sink, including seeing the destination name, use the [`gcloud logging sinks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/describe) command, which corresponds to the Logging API method [`projects.sinks.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/get):
         
         gcloud logging sinks describe SINK_NAME
         

  3. Run the [`gcloud logging sinks update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update) command and include the `--disabled` option. For example, to disable the `_Default` sink, use the following command:
         
         gcloud logging sinks update _Default --disabled
         

The `_Default` sink is now disabled; it no longer routes log entries to the `_Default` log bucket.




To disable the other sinks in your Google Cloud project that are routing to the `_Default` bucket, repeat the previous steps.

To re-enable a sink, use the [`gcloud logging sinks update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update) command, remove the `--disabled` option, and include the `--no-disabled` option:
    
    
    gcloud logging sinks update _Default --no-disabled
    

### REST

  1. To view the sinks for your Google Cloud project, call the Logging API method [`projects.sinks.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/list).

Identify any sinks that are routing to the `_Default` bucket.

  2. For example, to disable the `_Default` sink, set the `disabled` field in the `LogSink` object to `true`, and then call [`projects.sinks.update`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/update).

The `_Default` sink is now disabled; it no longer routes log entries to the `_Default` bucket.




To disable the other sinks in your Google Cloud project that are routing to the `_Default` bucket, repeat the previous steps.

To re-enable a sink, set the `disabled` field in the `LogSink` object to `false`, and then call [`projects.sinks.update`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/update).

## Code samples

To use client library code to configure sinks in your chosen languages, see [Code samples](https://docs.cloud.google.com/logging/docs/samples).

## Filter examples

The following are some filter examples that are particularly useful when creating sinks. For additional examples that might be useful as you build your inclusion filters and exclusion filters, see [Sample queries](https://docs.cloud.google.com/logging/docs/view/query-library).

### Restore the `_Default` sink filter

If you edited the filter for the `_Default` sink, then you might want to restore this sink to its original configuration. When created, the `_Default` sink is configured with the following inclusion filter and an empty exclusion filter:
    
    
      NOT log_id("cloudaudit.googleapis.com/activity") AND NOT \
      log_id("externalaudit.googleapis.com/activity") AND NOT \
      log_id("cloudaudit.googleapis.com/system_event") AND NOT \
      log_id("externalaudit.googleapis.com/system_event") AND NOT \
      log_id("cloudaudit.googleapis.com/access_transparency") AND NOT \
      log_id("externalaudit.googleapis.com/access_transparency")
    

### Exclude Google Kubernetes Engine container and pod logs

**Note:** Excluding some Google Kubernetes Engine log entries might prevent you from identifying and resolving problems with an application. For more information, see Supportability.

To exclude Google Kubernetes Engine container and pod log entries for GKE system `namespaces`, use the following filter:
    
    
    resource.type = ("k8s_container" OR "k8s_pod")
    resource.labels.namespace_name = (
    "cnrm-system" OR
    "config-management-system" OR
    "gatekeeper-system" OR
    "gke-connect" OR
    "gke-system" OR
    "istio-system" OR
    "knative-serving" OR
    "monitoring-system" OR
    "kube-system")
    

To exclude Google Kubernetes Engine node log entries for GKE system `log_id` values, use the following filter:
    
    
    resource.type = "k8s_node"
    (log_id("container-runtime") OR
     log_id("docker") OR
     log_id("kube-container-runtime-monitor") OR
     log_id("kube-logrotate") OR
     log_id("kube-node-configuration") OR
     log_id("kube-node-installation") OR
     log_id("kubelet") OR
     log_id("kubelet-monitor") OR
     log_id("node-journal") OR
     log_id("node-problem-detector"))
    

To view the volume of Google Kubernetes Engine node, pod, and container log entries stored in log buckets, use Metrics Explorer:

  * [View node log entry volume](https://console.cloud.google.com/monitoring/metrics-explorer?pageState=%7B%22xyChart%22:%7B%22dataSets%22:%5B%7B%22timeSeriesQuery%22:%22fetch%20k8s_node%5Cn%7C%20metric%20%27logging.googleapis.com%2Fbyte_count%27%5Cn%7C%20filter%5Cn%20%20%20%20\(metric.log%20%3D%3D%20%27container-runtime%27\)%20%5Cn%20%20%20%20%7C%7C%20\(metric.log%20%3D%20%27docker%27\)%5Cn%20%20%20%20%7C%7C%20\(metric.log%20%3D%3D%20%27kube-container-runtime-monitor%27\)%5Cn%20%20%20%20%7C%7C%20\(metric.log%20%3D%3D%20%27kube-logrotate%27\)%5Cn%20%20%20%20%7C%7C%20\(metric.log%20%3D%3D%20%27kube-node-configuration%27\)%5Cn%20%20%20%20%7C%7C%20\(metric.log%20%3D%3D%20%27kube-node-installation%27\)%20%7C%7C%20\(metric.log%20%3D%3D%20%27kubelet%27\)%5Cn%20%20%20%20%7C%7C%20\(metric.log%20%3D%3D%20%27kubelet-monitor%27\)%20%5Cn%20%20%20%20%7C%7C%20\(metric.log%20%3D%3D%20%27node-journal%27\)%5Cn%20%20%20%20%7C%7C%20\(metric.log%20%3D%3D%20%27node-problem-detector%27\)%5Cn%7C%20group_by%20%5Bproject_id%5D,%20sum\(value.byte_count\)%5Cn%7C%20every%201d%22,%22targetAxis%22:%22Y1%22,%22plotType%22:%22STACKED_AREA%22%7D%5D,%22options%22:%7B%22mode%22:%22COLOR%22%7D,%22constantLines%22:%5B%5D,%22timeshiftDuration%22:%220s%22,%22y1Axis%22:%7B%22label%22:%22y1Axis%22,%22scale%22:%22LINEAR%22%7D%7D,%22isAutoRefresh%22:true,%22timeSelection%22:%7B%22timeRange%22:%221w%22%7D%7D)
  * [View pod log entry volume](https://console.cloud.google.com/monitoring/metrics-explorer?pageState=%7B%22xyChart%22:%7B%22dataSets%22:%5B%7B%22timeSeriesQuery%22:%22fetch%20k8s_pod%5Cn%7C%20metric%20%27logging.googleapis.com%2Fbyte_count%27%5Cn%7C%20filter%5Cn%20%20%20%20\(resource.namespace_name%20%3D%3D%20%27cnrm-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27docker%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27config-management-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27gatekeeper-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27gke-connect%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27gke-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27istio-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27knative-serving%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27monitoring-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27kube-system%27\)%5Cn%7C%20group_by%20%5Bproject_id%5D,%20sum\(value.byte_count\)%5Cn%7C%20every%201d%22,%22targetAxis%22:%22Y1%22,%22plotType%22:%22STACKED_AREA%22%7D%5D,%22options%22:%7B%22mode%22:%22COLOR%22%7D,%22constantLines%22:%5B%5D,%22timeshiftDuration%22:%220s%22,%22y1Axis%22:%7B%22label%22:%22y1Axis%22,%22scale%22:%22LINEAR%22%7D%7D,%22isAutoRefresh%22:true,%22timeSelection%22:%7B%22timeRange%22:%221w%22%7D%7D)
  * [View container log entry volume](https://console.cloud.google.com/monitoring/metrics-explorer?pageState=%7B%22xyChart%22:%7B%22dataSets%22:%5B%7B%22timeSeriesQuery%22:%22fetch%20k8s_container%5Cn%7C%20metric%20%27logging.googleapis.com%2Fbyte_count%27%5Cn%7C%20filter%5Cn%20%20%20%20\(resource.namespace_name%20%3D%3D%20%27cnrm-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27docker%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27config-management-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27gatekeeper-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27gke-connect%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27gke-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27istio-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27knative-serving%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27monitoring-system%27\)%5Cn%20%20%20%20%7C%7C%20\(resource.namespace_name%20%3D%3D%20%27kube-system%27\)%5Cn%7C%20group_by%20%5Bproject_id%5D,%20sum\(value.byte_count\)%5Cn%7C%20every%201d%22,%22targetAxis%22:%22Y1%22,%22plotType%22:%22STACKED_AREA%22%7D%5D,%22options%22:%7B%22mode%22:%22COLOR%22%7D,%22constantLines%22:%5B%5D,%22timeshiftDuration%22:%220s%22,%22y1Axis%22:%7B%22label%22:%22y1Axis%22,%22scale%22:%22LINEAR%22%7D%7D,%22isAutoRefresh%22:true,%22timeSelection%22:%7B%22timeRange%22:%221w%22%7D%7D)



### Exclude Dataflow logs not required for supportability

To exclude Dataflow log entries that aren't required for supportability, use the following filter:
    
    
    resource.type="dataflow_step"
    labels."dataflow.googleapis.com/log_type"!="system" AND labels."dataflow.googleapis.com/log_type"!="supportability"
    

To view the volume of Dataflow logs stored in log buckets, use Metrics Explorer. For more information, see [View Dataflow log entry volume](https://console.cloud.google.com/monitoring/metrics-explorer?pageState=%7B%22xyChart%22:%7B%22dataSets%22:%5B%7B%22timeSeriesFilter%22:%7B%22filter%22:%22metric.type%3D%5C%22logging.googleapis.com%2Fbyte_count%5C%22%20resource.type%3D%5C%22dataflow_job%5C%22%22,%22minAlignmentPeriod%22:%2260s%22,%22aggregations%22:%5B%7B%22perSeriesAligner%22:%22ALIGN_RATE%22,%22crossSeriesReducer%22:%22REDUCE_NONE%22,%22groupByFields%22:%5B%5D%7D,%7B%22crossSeriesReducer%22:%22REDUCE_NONE%22%7D%5D%7D,%22targetAxis%22:%22Y1%22,%22plotType%22:%22LINE%22%7D%5D,%22options%22:%7B%22mode%22:%22COLOR%22%7D,%22constantLines%22:%5B%5D,%22timeshiftDuration%22:%220s%22,%22y1Axis%22:%7B%22label%22:%22y1Axis%22,%22scale%22:%22LINEAR%22%7D%7D,%22isAutoRefresh%22:true,%22timeSelection%22:%7B%22timeRange%22:%221h%22%7D%7D).

### Exclude Storage Transfer Service log entries that record successful actions

To exclude [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) log entries that record successful actions, use the following exclusion filter:
    
    
    resource.type="storage_transfer_job" AND
    jsonPayload.status.statusCode="OK"
    

An alternative is to modify the log data that a Storage Transfer Service job writes. For more information, see [Enable logging for Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs).

## Supportability

Although Cloud Logging lets you exclude log entries and prevent them from being stored in a log bucket, you might want to consider keeping log entries that help with supportability. Using these log entries can help you troubleshoot and identify issues with your applications.

For example, GKE system log entries are useful for troubleshooting your GKE applications and clusters because they are generated for events that happen in your cluster. These log entries can help you determine if your application code or the underlying GKE cluster is causing an application error. GKE system logs also include Kubernetes Audit Logging generated by the Kubernetes API Server component, which includes changes made by using the `kubectl` command and Kubernetes events.

For Dataflow, we recommend that you, at a minimum, write your system logs (`labels."dataflow.googleapis.com/log_type"="system"`) and supportability logs (`labels."dataflow.googleapis.com/log_type"="supportability"`) to log buckets. These logs are essential for developers to observe and troubleshoot their Dataflow pipelines. Without these logs, users might not be able to use the Dataflow **Job details** page to view job logs.

## What's next

  * [Troubleshoot routing logs](https://docs.cloud.google.com/logging/docs/export/troubleshoot)

  * [View logs in sink destinations](https://docs.cloud.google.com/logging/docs/export/using_exported_logs)

  * [Build queries with the Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
