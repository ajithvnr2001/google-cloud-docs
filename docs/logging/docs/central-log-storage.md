---
url: https://docs.cloud.google.com/logging/docs/central-log-storage/
title: Aggregate and store your organization's logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:59.049285+00:00
---

# Aggregate and store your organization's logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/central-log-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Aggregate and store your organization's logs Stay organized with collections  Save and categorize content based on your preferences. 

A non-intercepting aggregated sink lets you route log entries from across your Google Cloud organization to a central location while allowing child resources to route and store their own copies of those logs. In this tutorial, you create an organization-level, non-intercepting aggregated sink that routes your organization's audit logs to a Google Cloud project, where a project-level sink routes them to a central log bucket. You then configure read access to a log view on that bucket and query your aggregated audit logs in the Logs Explorer.

You can also configure an aggregated sink to be intercepting if you want to control which log entries can be queried or routed in child resources. For more information, see [Aggregated sinks overview](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview). If you're setting up a new organization, you can also configure centralized log storage as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

## Before you begin

Ensure the following:

  * To get the permissions that you need to centralize storage by creating an organization-level aggregated sink that routes log entries to a project, ask your administrator to grant you the following IAM roles: 

    * To create the aggregated sink: [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) on your organization 
    * To grant a service account IAM roles and to create a log bucket: [Owner ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`) on your project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 




## Create a log bucket

**Note:** You can skip this step if you use a log bucket that already exists. However, we recommend that you create a log bucket for this use case.

Log buckets store the log entries that are routed from other Google Cloud projects, folders, or organizations. For more information, see [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets).

To create the log bucket in the Google Cloud project that you want to aggregate log entries into, complete the following steps:

  1. Open a shell.

For example, to use the Cloud Shell, do the following:

     1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/)

     2. In the toolbar, click _terminal_ **Activate Cloud Shell**.
  2. In the shell, run the [`gcloud logging buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/create) command.

Before running the following command, make the following replacements:

     * BUCKET_NAME: The name of the log bucket.
     * LOCATION: The location of the log bucket. After you create your log bucket, you can't change its location.
     * PROJECT_ID: The identifier of the project in which to create the log bucket.

Run the `gcloud logging buckets create` command:
    
    gcloud logging buckets create BUCKET_NAME \
      --location=LOCATION --project=PROJECT_ID
    

  3. Verify that the log bucket was created:
         
         gcloud logging buckets list --project=PROJECT_ID
         

The response of the command is a list of the log buckets in your project.

  4. Log buckets have configurable retention periods. If you want to set the retention period of the log entries in your log bucket, then use the `gcloud logging buckets update` command. For example, the following command extends the retention of log entries stored in the log bucket to 365 days:
         
         gcloud logging buckets update BUCKET_NAME \
            --location=LOCATION --project=PROJECT_ID \
            --retention-days=365
         

For more information about flags, see [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update).




## Create the project-level log sink

You route log entries to a log bucket by creating a sink. A sink includes an inclusion filter, exclusion filters, and a destination. In this tutorial, you configure an inclusion filter and the destination to your new log bucket. Your sink doesn't contain any exclusion filters. For more information about sinks, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

To create a sink that routes log entries to the log bucket you just created, run the [`gcloud logging sinks create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create) command.

Before running the following command, make the following replacements:

  * PROJECT_LEVEL_SINK_NAME: The name of the project-level log sink.
  * SINK_DESTINATION: The log bucket where your log entries are routed. Sink destinations must use the global endpoint (`logging.googleapis.com`); [regional endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) (REP) aren't supported. The destination path format for a log bucket is the following:
        
        logging.googleapis.com/projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_NAME
        

  * PROJECT_ID: The identifier of the project in which to create the log sink. Set this flag to the same project where you created the log bucket.

  * Include the following flags:

    * `--log-filter`: Use this flag to set a [filter](https://docs.cloud.google.com/logging/docs/view/logging-query-language) that matches the log entries you want to include in your sink. In this tutorial, the filter is set to select all audit log entries. If you don't set a filter, then all log entries from your Google Cloud project are routed to the destination.
    * `--description`: Use this flag to describe the purpose or use case for the sink.



Run the `gcloud logging sinks create` command:
    
    
    gcloud logging sinks create PROJECT_LEVEL_SINK_NAME SINK_DESTINATION \
      --project=PROJECT_ID \
      --log-filter='logName:cloudaudit.googleapis.com' \
      --description="Audit logs from my organization"
    

## Create the aggregated sink

Aggregated sinks combine and route log entries from the resources contained by an organization or folder to a destination.

In this tutorial, you create an aggregated sink that is non-intercepting. This means every log entry that is routed by the aggregated sink is also routed by the sinks in the resource in which the log entry originates. For example, an audit log that originates in a project is routed by the aggregated sink and the sinks in that project. Therefore, it's possible for you to store multiple copies of a log entry.

You can also create intercepting sinks. For more information, see [Aggregated sinks overview](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview).

### Set up the sink at the organization level

To create an aggregated sink that is non-intercepting and that routes log entries to a project, complete the following steps:

  1. Run the [`gcloud logging sinks create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create) command.

Before running the following command, make the following replacements:

     * SINK_NAME: The name of the log sink. You can't change the name of a sink after you create it.
     * PROJECT_ID: The identifier of the project that stores the log bucket.
     * ORGANIZATION_ID: The identifier of the organization.

Run the `gcloud logging sinks create` command:
    
    gcloud logging sinks create SINK_NAME \
      logging.googleapis.com/projects/PROJECT_ID  \
      --log-filter='logName:cloudaudit.googleapis.com' \
      --description="Audit logs from my organization" \
      --organization=ORGANIZATION_ID \
      --include-children
    

The `--include-children` flag is important. This flag ensures that log entries from all the Google Cloud projects and folders within your organization are routed. For more information, see [Collate and route organization-level and folder-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks).

  2. Verify that the sink was created:
         
         gcloud logging sinks list --organization=ORGANIZATION_ID
         

  3. Get the name of the service account:
         
         gcloud logging sinks describe SINK_NAME --organization=ORGANIZATION_ID
         

The output looks similar to the following:
         
         writerIdentity: serviceAccount:o1234567890-ORGANIZATION_ID@gcp-sa-logging.iam.gserviceaccount.com
         

  4. Copy the value of the `serviceAccount` field into your clipboard.




### Grant access to the sink

After creating the aggregated sink, you must grant permission for the sink to write log entries to the project that you set as the destination. You can grant permission by using the Google Cloud console or by editing the Identity and Access Management (IAM) policy, as described in [Set destination permissions](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-auth).

If the destination Google Cloud project is protected by a VPC Service Controls [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#about-perimeters), then you must also add an ingress rule to the destination perimeter that allows access from the sink's service account. You don't need to configure an ingress rule for non-aggregated sinks. For more information, see [Collate and route organization- and folder-level logs to supported destinations: Limitations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks#limitations).

To grant your sink permission to write log entries, do the following:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Select the Google Cloud project that contains your log bucket.

  3. Click person_add **Grant access** and add the service account as a new principal. Don't include the `serviceAccount:` prefix.

  4. In the **Select a role** menu, select **Logs Writer**.

  5. Click **Save**.




### Generate log entries to assist in sink verification

To verify that your aggregated sink is properly configured, try the following:

  1. Generate audit log entries that should be routed to your log bucket.

     * If you have many Google Cloud projects in your organization, then you might have enough audit log traffic that you don't need to create any for validation purposes. Go to the next step.

     * Otherwise, go to a different project, create a Compute Engine VM instance, and then delete the instance you created. Audit logs are written when a VM is created, started, and deleted.

  2. Follow the steps in View log entries in the Logs Explorer page to view your audit logs. Be sure that you select the `_AllLogs` view.




## Configure read access to a log view on a log bucket

When you create a log bucket, Cloud Logging automatically creates a [log view](https://docs.cloud.google.com/logging/docs/logs-views) named `_AllLogs`. This view includes every log entry stored in the log bucket.

To restrict a principal to having access only to specific log entries, create a log view, and then do one of the following:

  * Grant them the Logs Views Accessor role (`roles/logging.viewAccessor`) along with an IAM condition that restricts the grant to the log view.

  * On the IAM policy associated with the log view, grant a principal access. We recommend this approach when you create a large number of log views.




For more information about these two approaches, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#about-iam-policies).

In the following steps, you grant a principal the Logs Views Accessor role (`roles/logging.viewAccessor`) along with an IAM condition that restricts the grant to the view named `_AllLogs`:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Select the Google Cloud project that contains the log bucket.

  3. Click person_add **Add**.

  4. In the **New principal** field, add a principal.

  5. In the **Select a role** menu, select **Logs Views Accessor**.

If you don't add a condition to this role, then the principal has access to all log views on all user-defined log buckets in the Google Cloud project.

  6. Add an IAM condition to the binding:

     1. Click **Add condition** , and then enter a title and description.
     2. In the **Condition type** menu, go to **Resource** , and then select **Name**.
     3. In the **Operator** menu, select **Ends with**.
     4. In the **Value** field, enter the full name of the log view:
            
            locations/LOCATION/buckets/BUCKET_NAME/views/_AllLogs
            

     5. Click **Save** to save the condition.

  7. Click **Save** to save the binding.




## View log entries in the Logs Explorer page

To view the log entries in your log bucket, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select **Refine Scope**.

  3. On the **Refine scope** panel, select **Log view**.

  4. Select the log view, or log views, whose log entries you want to see. For example, to view all log entries, select the view named `_AllLogs`.

  5. Click **Apply**.

The **Logs Explorer** page refreshes to show log entries from your log bucket. For more information about using the Logs Explorer, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
