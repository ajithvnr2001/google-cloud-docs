---
url: https://docs.cloud.google.com/trace/docs/analytics-migrate/
title: Migrate to Observability Analytics \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:29.756899+00:00
---

# Migrate to Observability Analytics  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/analytics-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Migrate to Observability Analytics Stay organized with collections  Save and categorize content based on your preferences. 

If you use trace sinks to export Cloud Trace data to [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction), then migrate to Observability Analytics. Trace sinks are [deprecated](https://docs.cloud.google.com/stackdriver/docs/deprecations) and will be removed on or after February 18, 2027. Observability Analytics lets you query your trace data directly using the same [SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) query language as BigQuery without managing export sinks.

If you want to use BigQuery services to join datasets, [manage tables](https://docs.cloud.google.com/bigquery/docs/managing-tables), or [export data](https://docs.cloud.google.com/bigquery/docs/export-intro), then you can create a linked BigQuery dataset. You can create the linked BigQuery dataset when you migrate or at a later date. To get started with Observability Analytics, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  8. To get the permissions that you need to load the **Observability Analytics** page, run queries, and create a linked BigQuery dataset, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Trace Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.admin) (`roles/cloudtrace.admin`)
     * [Observability Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)
     * [BigQuery User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  9. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 




## Migrate to Observability Analytics

  1. Complete the actions listed in the Before you begin section of this document. Those actions include enabling the Observability API.

  2. Verify that you have access to your trace data by using Observability Analytics:

     1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     2. In the **Views** menu, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Traces** section, and then select `_Trace.Spans._AllSpans`.

The **Schema** pane is updated and displays the schema.

If you don't see a view named `_Trace.Spans._AllSpans`, then your Google Cloud project doesn't contain an observability bucket named `_Trace`. For information about how to resolve this situation, see [Trace storage initialization fails](https://docs.cloud.google.com/trace/docs/troubleshooting#storage-failed).

     3. In the **Schema** pane, select **Query**.

The query editor field is updated. The `FROM` clause lists an entry similar to the following:
            
            `PROJECT_ID.us._Trace.Spans._AllSpans`
            

     4. In the toolbar, select **Run Query**.

If the toolbar displays **Run in BigQuery** , then click _settings_ **Settings** and select **Analytics (default)**.

You have verified that you can query your trace data by using the **Observability Analytics** page.

  3. Optional: If you want to join your trace data with other business data that is available to BigQuery, then create a linked BigQuery dataset. For more information, see [Query a linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset).

  4. Delete trace sinks and unnecessary datasets:

     1. To list existing trace sinks, execute the [`gcloud alpha trace sinks list`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/trace/sinks/list) command:
            
            gcloud alpha trace sinks list
            

     2. For each sink, execute the [`gcloud alpha trace sinks delete`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/trace/sinks/delete) command:
            
            gcloud alpha trace sinks delete SINK_NAME
            

     3. Optional: Delete any unnecessary BigQuery datasets. For information about how to delete a BigQuery dataset, see [Delete datasets](https://docs.cloud.google.com/bigquery/docs/managing-datasets#delete-datasets).




## Schema comparison

This section provides information about the differences between Observability Analytics and sink-based export schemas.

Name | Analytics | Legacy | Trace ID | `trace_id` | `extendedFields.traceId`  
---|---|---  
Span ID | `span_id` | `span.spanId`  
Parent span ID | `parent_span_id` | `span.parentSpanId`  
Span name | `name` | `span.displayName.value`  
Span kind | `kind`  
For values, see [OpenTelemetry: `SpanKind`](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.0.0/opentelemetry/proto/trace/v1/trace.proto#L119-L147).  | `span.spanKind`  
For values, see the Cloud Trace API reference [`SpanKind`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/SpanKind) page.  
Span start time | `start_time` | `span.startTime`  
Span end time | `end_time` | `span.endTime`  
Attributes | Span, resource, and instrumentation attributes each have a unique format. These fields have the BigQuery [JSON data type](https://docs.cloud.google.com/bigquery/docs/json-data). Examples:

  * `attributes["somekey"]`
  * `resource.attributes["somekey"]`
  * `instrumentation_scope.attributes["somekey"]`

| All attributes use the same format: `span.attributes.attributeMap.ATTRIBUTE_KEY` Examples:

  * `span.attributes.attributeMap._http_method`
  * `span.attributes.attributeMap.g_co_agent`
  * `span.attributes.attributeMap.rpc_service`
  * `span.attributes.attributeMap.rpc_method`

  
  
## What's next

  * [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics)
  * [Sample queries](https://docs.cloud.google.com/trace/docs/analytics-samples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
