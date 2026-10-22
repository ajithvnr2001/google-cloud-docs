---
url: https://docs.cloud.google.com/logging/docs/export/aggregated_sinks/
title: Collate and route organization- and folder-level logs to supported destinations \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:05.101194+00:00
---

# Collate and route organization- and folder-level logs to supported destinations  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/export/aggregated_sinks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Collate and route organization- and folder-level logs to supported destinations Stay organized with collections  Save and categorize content based on your preferences. 

Aggregated [sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) in Cloud Logging let you combine and route log entries from all resources in a folder or organization to a central destination. You can configure an aggregated sink as intercepting or non-intercepting, define filters to control which log entries are routed, and grant the sink permission to write to its destination.

**Note:** If your data is managed through an [Assured Workloads environment](https://docs.cloud.google.com/assured-workloads/docs/key-concepts), then this feature might be impacted or restricted. For information, see [Restrictions and limitations in Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/eu-sovereign-controls-restrictions-limitations#features_logging).

## Limitations

When you configure an aggregated sink, the following limitations apply:

  * A destination path can only include a global service endpoint, such as `pubsub.googleapis.com`. You **can't include** a [regional service endpoint](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) (REP) such as `pubsub.LOCATION.rep.googleapis.com`. For a list of supported destination paths, see [Destination path formats](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#destination-paths).

  * Routing log data to Pub/Sub topics with [in-transit restrictions](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) isn't supported. If you configure a log sink to a Pub/Sub topic with in-transit restrictions, then you might see [`topic_region_not_allowed`](https://docs.cloud.google.com/logging/docs/export/troubleshoot#topic_region_not_allowed) configuration errors and dropped logs.



  * Routing log entries to a resource protected by a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#about-perimeters) requires that you add an ingress rule to the perimeter that allows access from the sink's service account:

    * [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules)
    * [Manage service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters)

If you use an aggregated log sink to route log entries to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs) that is in a perimeter, then use `ANY_IDENTITY` as the identity type in the ingress rule. You can't use `ANY_SERVICE_ACCOUNT` or `ANY_USER_ACCOUNT` as the identity type for this destination.

You don't need to configure an ingress rule for non-aggregated sinks.




## Before you begin

Before you create a sink, ensure the following:

  * You are familiar with the behavior of aggregated sinks. For more information, see [Aggregated sinks overview](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview).

  * You have a Google Cloud folder or organization with log entries that you can see in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  * You have one of the following Identity and Access Management roles for the Google Cloud organization or folder from which you're routing log entries:

    * **Owner** (`roles/owner`)
    * **Logging Admin** (`roles/logging.admin`)
    * **Logs Configuration Writer** (`roles/logging.configWriter`)

The permissions contained in these roles let you create, delete, or modify sinks. For information about setting IAM roles, see the Logging [Access control guide](https://docs.cloud.google.com/logging/docs/access-control).

  * The destination of the aggregated sink exists or you have the ability to create it. The destination can be in any Google Cloud project and in any organization. For a list of supported destinations and their limitations, see [Supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#supported_destinations).

  * Select the interface you plan to use:

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




## Create an aggregated sink

To configure an aggregated sink, create the sink and then grant the sink the permissions to write to the destination. This section describes how to create an aggregated sink. For information about granting permissions to the sink, see Set destination permissions.

You can create up to 200 sinks per folder or organization.

###  Console 

To create an aggregated sink for your folder or organization, do the following:

  1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select an existing folder or organization.

  3. Select **Create sink**.

  4. In the **Sink details** panel, enter the following details:

     * **Sink name** : Provide an identifier for the sink. After you create the sink, you can't rename it, but you can delete it and create a new one.

     * **Sink description** (optional): Describe the purpose or use case for the sink.

  5. In the **Select sink service** menu, select the type of destination, and then complete the dialog to specify the destination. You can select an existing destination or create the destination.

     * For an intercepting sink, select **Google Cloud project** , and then enter the fully qualified name of the destination Google Cloud project:
           
           logging.googleapis.com/projects/DESTINATION_PROJECT_ID
           

     * For a non-intercepting sink, select the destination, and then enter the fully qualified name of the destination. The following destinations are supported:

       * **Google Cloud project**
             
             logging.googleapis.com/projects/DESTINATION_PROJECT_ID
             

       * **Logging bucket**
             
             logging.googleapis.com/projects/DESTINATION_PROJECT_ID/locations/LOCATION/buckets/BUCKET_NAME
             

       * **BigQuery dataset**

Enter the name of a write-enabled dataset. Don't enter the name of a linked BigQuery dataset; these datasets are read-only. You can use [partitioned tables](https://docs.cloud.google.com/logging/docs/export/bigquery#partition-tables).
             
             bigquery.googleapis.com/projects/DESTINATION_PROJECT_ID/datasets/DATASET_ID
             

       * **Cloud Storage bucket**
             
             storage.googleapis.com/BUCKET_NAME
             

       * **Pub/Sub topic**

Don't enter the name of a Pub/Sub topic that enforces [in-transit restrictions](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).
             
             pubsub.googleapis.com/projects/DESTINATION_PROJECT_ID/topics/TOPIC_ID
             

       * **Splunk**

Enter the Pub/Sub topic for your [Splunk](https://docs.cloud.google.com/architecture/exporting-stackdriver-logging-for-splunk) service.

  6. In the **Choose logs to include in sink** panel, select the resources to include in the sink.

     * For an intercepting sink, select **Intercept logs ingested by this organization and all child resources**.

     * For a non-intercepting sink, select **Include logs ingested by this resource and all child resources**.

  7. In the **Build inclusion filter** field, [enter a filter expression](https://docs.cloud.google.com/logging/docs/view/logging-query-language) that matches the log entries that you want to include. If you don't set a filter, all log entries from your selected resource are routed to the destination.

For example, you might want to build a filter to route all Data Access audit logs to a single Logging bucket. This filter looks like the following:
         
         LOG_ID("cloudaudit.googleapis.com/data_access") OR LOG_ID("externalaudit.googleapis.com/data_access")
         

For examples, see Filters for aggregated sinks.

Note that the length of a filter can't exceed 20,000 characters.

  8. Optional: To verify that you entered the correct filter, select **Preview logs**. This opens the Logs Explorer in a new tab with the filter pre-populated.

  9. Optional: In the **Choose logs to exclude from the sink** panel, do the following:

     1. In the **Exclusion filter name** field, enter a name.

     2. In the **Build an exclusion filter** field, enter a [filter expression](https://docs.cloud.google.com/logging/docs/view/logging-query-language) that matches the log entries that you want to exclude. You can also use the [`sample` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#functions) to select a portion of the log entries to exclude.

**Key Point:** If you want your exclusion filter to be disabled when the sink is created, then select **Disable** after you enter your filter expression. You can update the sink later to enable the exclusion filter.

For example, to exclude the log entries from a specific project from being routed to the destination, add the following exclusion filter:
            
            logName:projects/PROJECT_ID
            

To exclude log entries from multiple projects, use the logical-OR operator to join `logName` clauses.

You can create up to 50 exclusion filters per sink. Note that the length of a filter can't exceed 20,000 characters.

  10. Select **Create sink**.

  11. To complete the configuration of your aggregated sink, grant the service account for the sink the permission to write log entries to your sink's destination. For more information, see Set destination permissions.




###  gcloud 

To create an aggregated sink, use the [`logging sinks create`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#creating_sinks) command:

  1. To create a sink, run the `gcloud logging sinks create` command, and include the `--include-children` flag.

Before using the following command, make the following replacements:

     * SINK_NAME: The name of the log sink. You can't change the name of a sink after you create it.
     * SINK_DESTINATION: The service or project to where you want your log entries routed. For information about the format of these destinations, see [Destination path formats](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#destination-paths).
     * INCLUSION_FILTER: The inclusion filter for a sink. For examples, see Filters for aggregated sinks.
     * FOLDER_ID: The ID of the folder. If you want to create a sink at the organization level, then replace `--folder=FOLDER_ID` with `--organization=ORGANIZATION_ID`.

Run the [`gcloud logging sinks create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create) command:
    
    gcloud logging sinks create SINK_NAME \
      SINK_DESTINATION  --include-children \
      --folder=FOLDER_ID --log-filter="INCLUSION_FILTER"
    

To create an intercepting sink, also include the `--intercept-children` flag.

For example, if you're creating a folder-level aggregated sink whose destination is a Pub/Sub topic, then your command might look like the following:
    
    gcloud logging sinks create SINK_NAME \
      pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID --include-children \
      --folder=FOLDER_ID --log-filter="logName:activity"

  2. Grant the service account for the sink permission to write to your sink destination. For more information, see Set destination permissions.




###  REST 

To create an aggregated sink, use the [`organizations.sinks.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/organizations.sinks/create) or [`folders.sinks.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/folders.sinks/create) Logging API method. Prepare the arguments to the method as follows:

  1. Set the `parent` field to be the Google Cloud organization or folder in which to create the sink. The parent must be one of the following:

     * `organizations/ORGANIZATION_ID`
     * `folders/FOLDER_ID`
  2. In the [`LogSink`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks#LogSink) object in the method request body, do one of the following:

     * Set `includeChildren` to `true`.

     * To create an intercepting sink, also set the `interceptChildren` field to `true`.

  3. Set the `filter` field to match the log entries that you want to include.

For examples, see Filters for aggregated sinks.

The length of a filter can't exceed 20,000 characters.

  4. Set the remaining [`LogSink`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks#LogSink) fields as you would for any sink. For more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

  5. Call [`organizations.sinks.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/organizations.sinks/create) or [`folders.sinks.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/folders.sinks/create) to create the sink.

  6. Grant the service account for the sink permission to write to your sink destination. For more information, see Set destination permissions.




Any changes made to a sink might take a few minutes to apply.

## Set destination permissions

This section describes how to grant the **writer identity** of a log sink the IAM permissions it needs so that the sink can write log entries to the sink's destination. The writer identity is the ID of the service account associated with the sink; this identity includes an email address that identifies the principal that must have access to write data to the destination.

You don't need to set destination permissions when a log sink routes log entries to a log bucket in the same project. For this configuration, a service account isn't required. For all other configurations, Logging automatically creates and manages the service account for a log sink, and you must set the destination permissions:

  * As of May 22, 2023, Logging uses the same service account for all sinks in the underlying resource. Resources can be a Google Cloud project, an organization, a folder, or a billing account.
  * Before May 22, 2023, Logging created a service account for each sink.



If the sink's destination is protected by a VPC Service Controls [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#about-perimeters), then you must also add an ingress rule to the destination perimeter that allows access from the sink's writer identity. For more information, see Limitations.

**Note:** To set the destination permissions, you must have **Owner** access on the Google Cloud project that contains the destination.

To set permissions for your sink to route to its destination, do the following:

###  Console 

**Note:** If you created your sink in the Google Cloud console and you have **Owner** access to the destination, then Logging should have set up the necessary permissions on your behalf. If it did so, you're done. If not, complete the following steps:

  1. To get information about the service account for your sink, do the following:

     1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     2. Select _more_vert_ **Menu** and then select **View sink details**. The writer identity appears in the **Sink details** panel.

     3. If the value of the `writerIdentity` field contains an email address, then proceed to the next step. When the value is `None`, you don't need to configure destination permissions.

     4. Copy the sink's writer identity into your clipboard. Writer identities might look different depending on what resource your sink belongs to, but are always prefixed by `serviceAccount:`. The following is an example of a writer identity:
            
            serviceAccount:service-123456789012@gcp-sa-logging.iam.gserviceaccount.com
            

  2. Grant the principal specified by the sink's writer identity the permission to write log data to the destination:

     1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

     2. In the toolbar of the Google Cloud console, select the project that stores the destination of the aggregated sink. When the destination is a project, select that project.

     3. Click person_add **Grant access**.

     4. Enter the principal specified by the sink's writer identity and then grant an IAM role:

        * For all destinations, grant the [Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.logWriter`). Specifically, a principal needs the `logging.logEntries.route` permission. 
        * Grant one of the following roles based on the destination: 
          * Log bucket: Grant the [Logs Bucket Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.bucketWriter`). 
          * Cloud Storage bucket: Grant the [Storage Object Creator role](https://docs.cloud.google.com/iam/docs/understanding-roles#storage) (`roles/storage.objectCreator`). 
          * BigQuery dataset: Grant the [BigQuery Data Editor role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) (`roles/bigquery.dataEditor`). 
          * Pub/Sub topic, including Splunk: Grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/pubsub/docs/access-control#roles) (`roles/pubsub.publisher`). 



###  gcloud 

  1. Ensure that you have **Owner** access on the Google Cloud project that contains the destination. If you don't have **Owner** access to the destination of the sink, then ask a project owner to add the writer identity as a principal.

  2. To get information about the service account for your sink, run the `gcloud logging sinks describe` command.

Before using the following command, make the following replacements:

     * SINK_NAME: The name of the log sink. You can't change the name of a sink after you create it.

Run the [`gcloud logging sinks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/describe) command:
    
    gcloud logging sinks describe SINK_NAME
    

  3. If the sink details contain a field labeled `writerIdentity`, then proceed to the next step. When the details don't include a `writerIdentity` field, you don't need to configure destination permissions for the sink.

  4. Copy the sink's writer identity into your clipboard. The following illustrates a writer identity:
         
         serviceAccount:service-123456789012@gcp-sa-logging.iam.gserviceaccount.com
         

  5. Grant the sink's writer identity the permission to write log data to the destination by running the `gcloud projects add-iam-policy-binding` command.

Before using the following command, make the following replacements:

     * PROJECT_ID: The identifier of the project. Select the project that stores the destination of the aggregated sink. When the destination is a project, select that project.
     * PRINCIPAL: An identifier for the principal that you want to grant the role to. Principal identifiers usually have the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com`. For a full list of the formats that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).
     * ROLE: An IAM role. Grant the sink's writer identity an IAM role based on the destination of the log sink:

       * For all destinations, grant the [Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.logWriter`). Specifically, a principal needs the `logging.logEntries.route` permission. 
       * Grant one of the following roles based on the destination: 
         * Log bucket: Grant the [Logs Bucket Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.bucketWriter`). 
         * Cloud Storage bucket: Grant the [Storage Object Creator role](https://docs.cloud.google.com/iam/docs/understanding-roles#storage) (`roles/storage.objectCreator`). 
         * BigQuery dataset: Grant the [BigQuery Data Editor role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) (`roles/bigquery.dataEditor`). 
         * Pub/Sub topic, including Splunk: Grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/pubsub/docs/access-control#roles) (`roles/pubsub.publisher`). 

Run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member=PRINCIPAL --role=ROLE
    




###  REST 

We recommend that you use the Google Cloud console or the Google Cloud CLI to grant a role to the service account.

## Filters for aggregated sinks

This section provides examples of filters that you might use in an aggregated sink. For more examples, see [Sample queries using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/query-library).

Some examples use the following notation:

  * `:` is the substring operator. Don't substitute the `=` operator.
  * `...` represents any additional filter comparisons.
  * Variables are indicated by colored text. Replace them with valid values.



The length of a filter is restricted to 20,000 characters.

For more details about the filtering syntax, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

### Select the log source

To route log entries from all child resources, don't specify a project, folder, or organization in your sink's inclusion and exclusion filters. For example, suppose you configure an aggregated sink for an organization with the following filter:
    
    
    resource.type="gce_instance"

With this filter, the aggregated sink routes log entries from Compute Engine instances in any child resource of that organization to the destination.

However, there might be situations where you want to use an aggregated sink to route log entries only from specific child resources. For example, for compliance reasons, you might want to store audit logs from specific folders or projects in their own Cloud Storage bucket. In these situations, configure your inclusion filter to specify _each_ child resource whose log entries you want routed. If you want to route log entries from a folder and all projects within that folder, then the filter must list the folder and each of the projects contained by that folder, and also join the statements with an `OR` clause.

The following filters restrict log entries to **specific** Google Cloud projects, folders, or organizations:
    
    
    logName:"projects/PROJECT_ID/logs/" AND ... 
    
    
    logName:("projects/PROJECT_A_ID/logs/" OR "projects/PROJECT_B_ID/logs/") AND ... 
    
    
    logName:"folders/FOLDER_ID/logs/" AND ... 
    
    
    logName:"organizations/ORGANIZATION_ID/logs/" AND ... 

For example, to route only log entries that were generated by Compute Engine instances and that originated in the folder `my-folder`, use the following filter:
    
    
    logName:"folders/my-folder/logs/" AND resource.type="gce_instance"

With this filter, log entries that originate in any resource other than `my-folder`, including log entries that originate in Google Cloud projects that are children of `my-folder`, aren't routed to the destination.

### Select the monitored resource

To route log entries from only a specific monitored resource in a Google Cloud project, use multiple comparisons to specify the resource exactly:
    
    
    logName:"projects/PROJECT_ID/logs" AND
    resource.type=RESOURCE_TYPE AND
    resource.labels.instance_id=INSTANCE_ID

For a list of resource types, see [Monitored resource types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types).

### Select a sample of log entries

To route a random sample of log entries, add the `sample` built-in function. For example, to route only ten percent of the log entries matching your current filter, use this addition:
    
    
    sample(insertId, 0.10) AND ...
    

For more information, see the [`sample` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#functions).

For information about Logging filters, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

## What's next

  * [Create log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views): Log views let you grant principals read access to a subset of the log entries stored in a log bucket.

  * [Route logs to supported destinations: Manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#managing_sinks)

  * [Troubleshoot routing and sinks](https://docs.cloud.google.com/logging/docs/export/troubleshoot)

  * [View logs in sink destinations](https://docs.cloud.google.com/logging/docs/export/using_exported_logs)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
