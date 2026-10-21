---
url: https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface/
title: View and analyze log entries \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:03.525878+00:00
---

# View and analyze log entries  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  View and analyze log entries Stay organized with collections  Save and categorize content based on your preferences. 

This document provides you with an overview of the Logs Explorer in the Google Cloud console, which you can use to retrieve, view, and analyze log entries that are stored in [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries). Viewing and analyzing individual log entries and a sequence of log entries can help you troubleshoot problems and improve observability. You can also read log data by using the [Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) and the [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/api/gcloud-logging#reading_log_entries).

To perform aggregate operations on your log entries, like counting the number of log entries that contain a specific pattern, upgrade the log bucket to use Observability Analytics, and then run queries from the **Observability Analytics** page of the Google Cloud console. You can continue to use the Logs Explorer to view log entries that are stored in log buckets that have been upgraded to use Observability Analytics. For more information, see [Observability Analytics overview](https://docs.cloud.google.com/logging/docs/log-analytics#analytics).

The remainder of this document describes how to use the Logs Explorer.

## Before you begin

To get the permissions that you need to use the Logs Explorer to view log entries, ask your administrator to grant you the following IAM roles: 

  * To view log entries in the `_Required` bucket and those in the `_Default` view on the `_Default` bucket, or to select a log scope: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on your project, folder, or organization. 
  * To view all log entries in the `_Required` and `_Default` buckets: [Private Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer) (`roles/logging.privateLogViewer`) on your project, folder, or organization. 
  * To view restricted [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields in a log bucket: [Log Field Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.fieldAccessor) (`roles/logging.fieldAccessor`) on the project, folder, or organization that stores the log bucket. For information about how to restrict access to `LogEntry` fields, see [Configure field-level access](https://docs.cloud.google.com/logging/docs/field-level-acl). 
  * To view and download log entries stored in a [log view](https://docs.cloud.google.com/logging/docs/logs-views) on a log bucket: [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`) on the project, folder, or organization that contains the log bucket. For information about how to get access only to a specific log view, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#about-iam-policies). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Get started

To begin using the Logs Explorer, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select a Google Cloud project, folder, or organization. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

The log entries displayed by the **Logs Explorer** page depend on the following:

     * The resources searched for log entries.
     * The time-range setting.
     * Your Identity and Access Management (IAM) roles on the searched resources.
     * The filters applied to the search results. For example, adding the query `severity>=ERROR` results in the display listing only those log entries with a severity level of at least `ERROR`.

By default, the **Logs Explorer** page searches the resources listed in the default [log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage) for log entries. When the default log scope isn't accessible, the page searches for the log entries that originate in your selected project, folder, or organization. For projects, the search results include the log entries that are routed to the project by a sink in another project, and then stored in a log bucket.

After the **Logs Explorer** page opens, you can select which resources are searched for log entries by the Logs Explorer. However, your selection applies only to your current session.




## Logs Explorer interface

The Logs Explorer interface lets you display log entries, parse and analyze them, and specify query parameters. The Logs Explorer contains the following sections, which are detailed on this page:

  1. Primary toolbar
  2. **Query** pane
  3. **Fields** pane
  4. **Timeline**
  5. **Query results** pane



![User interface for the Logs Explorer.](https://docs.cloud.google.com/static/logging/docs/images/logs-explorer-interface.png)

## Primary toolbar in the Logs Explorer

Using the primary toolbar, you can do the following:

  * _menu_book_ **Query library** : View saved, recent, and suggested queries. For more information, see [Save and share queries](https://docs.cloud.google.com/logging/docs/view/building-queries#saved-queries).
  * _link_ **Share link** : Create a shortened URL of the query and copy it to your clipboard, making it easier to share a query. The copied URL has the corresponding absolute time range represented by the time range of your query; for example, `7:49:37 PM - 8:49:37 PM`.
  * _settings_ **Preferences** : Adjust the view of the Logs Explorer page, and customize the format of your query results. For more information, see Set preferences for viewing log data.
  * **Time-range selector** : Specify a time range for the log entries that you want to view. For more information, see [Use the time-range selector](https://docs.cloud.google.com/logging/docs/view/building-queries#time-range). 
  * **Stream logs** : View log entries as Logging stores them in log buckets. For more information, see Stream log entries. 
  * _school_ **Learn** : View links to relevant documentation and topics.

**Note:** If your data is managed through an [Assured Workloads environment](https://docs.cloud.google.com/assured-workloads/docs/key-concepts), then this feature might be impacted or restricted. For information, see [Restrictions and limitations in Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/eu-sovereign-controls-restrictions-limitations#features_logging).

### View recent, saved, and suggested queries

To view queries that you have recently run, queries that you saved for future use, and suggested queries, click the _menu_book_ **Query library** button.

In the **Query library** tab, you can view the following:

  * Recent queries: View queries that you have recently run. For more information, see [Use recent queries](https://docs.cloud.google.com/logging/docs/view/building-queries#recent-queries).

  * Saved queries: View your saved queries and queries that other users of the Google Cloud project have shared with you. For more information, see [Save and share queries](https://docs.cloud.google.com/logging/docs/view/building-queries#saved-queries).

  * Suggested queries: View suggested queries based on the resources in your Google Cloud project. For more information, see [Use suggested queries](https://docs.cloud.google.com/logging/docs/view/building-queries#suggested_queries).

  * Queries provided by Google Cloud: View queries provided by Google Cloud based on common use cases for various Google Cloud services. For more information, see [Select queries from the library](https://docs.cloud.google.com/logging/docs/view/building-queries#library-queries).




### Set preferences for viewing log data

To customize how your log entries are presented in the query results, click the _settings_ **Preferences** button, and select **View** , **Format** , or **Manage summary fields** :

  * To show or hide the **Timeline** and **Fields** panes, to hide summary chips in your query results, or to change the sorting order of your log entries, select **View**.

  * To configure the **Time** column of your query results, select **Format**. For more information, see Configure the **Time** column.

  * To show up to 10 lines for each log entry, select **Format** and click **Wrap lines**. By default, the content of each log entry is truncated to fit into one line. Blank spaces are preserved in each log entry.

  * To find patterns in your log entries by using summary fields, select **Manage summary fields**. For more information, see Find patterns in your log entries by using summary fields.




#### Configure the **Time** column

The **Time** column in the **Query results** pane displays the timestamps of your log entries. You can customize the **Time** column so that only certain parts of the timestamp are visible. This creates more horizontal space so that you can view more information in the log entry.

To select which parts of the timestamp to display, click the _settings_ **Preferences** menu, select **Format** , and then select one of the following options:

  * Date, time, and timezone

  * Date and time (default)

  * Time only




#### Find patterns in your log entries by using summary fields

Suppose you're looking through the log entries in your query results and want to quickly skim the results by a certain [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) field. Or perhaps you want to group your log entries by a certain field-value pair. You can add summary fields to your results, which appear as chips at the beginning of each log entry line.

The Logs Explorer offers default summary fields and custom summary fields. Default summary fields depend on your current query results, and custom summary fields let you select any field in the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

To show or hide all summary field chips in your query results, click _settings_ **Preferences** , select **View** , and then **Show summary chips**. When this option is enabled, the results are displayed in raw-text format.

To hide specific summary fields, enable **Summary fields** , and then click **Hide summary field**. To modify summary fields, do the following:

  1. Click the _settings_ **Preferences** button, and select **Manage summary fields**.

  2. In the **Manage summary fields** dialog, you can do the following:

     * Add any custom field names to **Custom summary fields**.

The summary field supports auto-completion and field correction for legal characters within quotes. For example, if you type `jsonPayload.id-field`, it gets changed to `jsonPayload."id-field"`.

You can also select any [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) field, regardless of whether it is suggested to you with the autocomplete function.

To remove an existing custom summary field, click the `X` in its chip.

     * Turn truncation on and off for your custom summary fields.

To shorten the display of the summary field values, use the _toggle_off_ toggle next to **Truncate custom summary fields**. You can choose how many characters to display before the field is truncated, and whether the beginning or the end of the field is displayed.

**Tip:** To display a summary field's full value, hold the pointer over a truncated summary field in your query results.
     * Hide or show default summary fields:

To customize which default summary fields are shown in your query results, expand the **Hide or show default summary fields** menu.

  3. Click **Apply**.

Your summary fields are now updated in your query results.




### Filter log entries by time range

To specify a time range for the log entries that you want to view, use the [time-range selector](https://docs.cloud.google.com/logging/docs/view/building-queries#time-range).

To perform a forced refresh of your query results to include the current time, click keyboard_tab **Jump to now**.

### Stream log entries

You can [stream log entries](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) as Logging stores them in log buckets, or you can add a query to stream only those log entries that match the query.

To stream log entries based on a query, add a query in the **Query** pane, and then select the **Stream logs** button in the primary toolbar. As Logging stores the log entries in log buckets, only those log entries that match the query are shown in the **Query results** pane. When a query isn't provided, Logging shows each log entry as it's stored.

To stop streaming, click _stop_ **Stop stream** , or manually scroll to pause the stream.

## **Query** pane

To build a query in the Logs Explorer, use the query pane. In the query pane, you can build and refine queries by using the following features:

  * Select which resources are searched for log entries. Queries that you write filter the log entries returned by the search.

  * Search all fields: Find log entries that match your search terms or phrases. Any search terms added to the **Search all fields** field are added to the query-editor field and are evaluated as part of your query expression. For more information, see [Search for text across log fields](https://docs.cloud.google.com/logging/docs/view/building-queries#query-builder-menus).

  * Filter menus: Build queries by using various menus to select resources, log names, severity levels, and correlation to other log entries. For more information, see [Use filter menus](https://docs.cloud.google.com/logging/docs/view/building-queries#query-builder-menus).

  * Query-editor field: Build advanced queries by using the Logging query language. If you don't see the query-editor field, enable **Show query**. For more information, see [Write advanced queries using the Logging query language](https://docs.cloud.google.com/logging/docs/view/building-queries#queries-by-expression).

**Note:** When a query contains multiple statements, you can either specify how those statements are joined or rely on Cloud Logging implicitly adding the conjunctive restriction, `AND`, between the statements. For example, suppose a query or filter dialog contains two statements, `resource.type = "gce_instance"` and `severity >= "ERROR"`. The actual query is `resource.type = "gce_instance" AND severity >= "ERROR"`. Cloud Logging supports both disjunctive restrictions, `OR`, and conjunctive restrictions, `AND`. When you use `OR` statements, we recommend that you group the clauses with parentheses. For more information, see the [Logging query language documentation](https://docs.cloud.google.com/logging/docs/view/logging-query-language).



After you review your query, click **Run query**. Log entries that match your query are listed under the **Query results** pane. The **Timeline** and **Fields** panes also adjust according to the query expression.

### Select which resources are searched for log entries

This section describes how to view or change which resources are searched for log entries. If you enter a query, then the Logs Explorer displays only the fetched log entries which also match the query. For example, adding the query `severity>=ERROR` results in the display listing only those log entries with a severity level of at least `ERROR`.

To determine which log entries to display, the **Logs Explorer** page searches the resources listed in the default [log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage). When the default log scope isn't accessible, the page searches for the log entries that originate in your selected project, folder, or organization. When projects are searched, the search results include the log entries that are routed to the project by a sink in another project, and then stored in a log bucket.

**Note:** To configure which resources are searched when the **Logs Explorer** page opens, set the default log scope. For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).

For your current session, you can configure which resources the Logs Explorer searches for log entries. For example, when troubleshooting, you might want to examine only those log entries that are included in a [log view](https://docs.cloud.google.com/logging/docs/logs-views) or that originate in a specific Google Cloud project.

The toolbar in the **Query** pane displays the resources searched for log entries:

  * ![](https://docs.cloud.google.com/static/stackdriver/images/gc-project-icon.png)**Project logs** and ![](https://docs.cloud.google.com/static/stackdriver/images/log-scope-icon.png)**_Default** : Log entries that originate in the selected project, folder, or organization are returned. For projects, these log entries include those that are routed to the project by a sink in another project.

  * ![](https://docs.cloud.google.com/static/stackdriver/images/log-view-icon.png)**N log view** : Log entries included in the **N** log views are returned. You can expand the menu to list the log views.

  * ![](https://docs.cloud.google.com/static/stackdriver/images/log-scope-icon.png)**my-custom-scope** , where "my-custom-scope" is the name of a custom log scope: If a log scope lists log views, then the log entries in those log views are returned. If a log scope lists other resources, like projects, then log entries that originate in those resources are returned. For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).




When you want to change which resources are searched for log entries, do the following:

  1. Go to the toolbar of the **Query** pane. This toolbar displays a menu that is labeled like one of the following:

     * ![](https://docs.cloud.google.com/static/stackdriver/images/gc-project-icon.png)**Project logs**
     * ![](https://docs.cloud.google.com/static/stackdriver/images/log-view-icon.png)**N log view**
     * ![](https://docs.cloud.google.com/static/stackdriver/images/log-scope-icon.png)**my-custom-scope**

Select the menu.

  2. In the **Refine scope** flyout, select the storage location, and then complete the dialog.

The following information might help you complete the dialog:

     * When you want to view log entries routed by an [aggregated sink](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview), select ![](https://docs.cloud.google.com/static/stackdriver/images/log-view-icon.png)**Log view** as the storage location. Be sure to then select all log views that store log entries that you want to view.

     * For folders and organizations, the log view menu lists all log views that store log entries that originated in those resources.

     * For projects, the log view menu lists the log views on log buckets stored by the selected project.

     * To modify the log-view menu to include log views on log buckets stored in a specific project, click  _add_circle_ **Import project** , and then select the project.

     * To configure a log scope, select ![](https://docs.cloud.google.com/static/stackdriver/images/log-scope-icon.png)**Log scope** , and then click **Manage scopes**.



## **Fields** pane

The **Fields** pane offers a high-level summary of log entries and provides an efficient way to refine a query. The entries in this pane also list the approximate number of log entries that match the corresponding filter. To get an exact count of the number of log entries received in a time interval, use Observability Analytics or [copy log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs) to a Cloud Storage bucket.

After you execute a query in the query-editor field, the **Fields** pane is populated based on the results of the query. The pane is divided into the following sections:

  * **Pinned** : Shows fields that you pinned for quick access. If this section isn't shown, then you haven't pinned any fields.

  * **System metadata** : Shows log entries broken down by different dimensions, corresponding to fields in the log entries.

  * **Frequent fields** : Shows the most frequent `json_payload` fields in the current query results.




For the **System metadata** section, the following dimensions are always available:

  * Resource type

If you use BindPlane to write on-premise and hybrid cloud log data, then select the resource type [**Generic Node**](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#tag_generic_node).

  * Severity

If you want your query to filter by multiple severity levels, then use the **Severity** menu.




Some dimensions are dynamically populated based on the labels in your log entries. For example, you might see a **Workload / Service** or **Application** dimension:

  * The **Workload / Service** dimension is shown in the following scenarios:

    * You have log entries whose resource type is [**Kubernetes Container**](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#tag_k8s_container) and you haven't filtered your log entries by resource type. The values in the `labels.k8s-pod/app` label contribute to the entries in the **Workload / Service** dimension.

For example, if a log entry similar to the following is displayed as a result of your query, then the service menu includes the service named `myservice`:
          
          {
          ...
          labels: {
              compute.googleapis.com/resource_name: "mycluster1"
              **k8s-pod/app: "myservice"**
              k8s-pod/pod-template-hash: "5ffcd94fdd"
           }
           logName: "projects/my-project/logs/stdout"
           resource: {
              labels: {6}
              type: "k8s_container"
           }
           ...
          }
          

    * You have log data with labels for an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) service or workload. These labels are of the form `apphub.workload.id` or `apphub.service.id`. In your log entry, they are shown in the `apphub` entry. For example, a log entry might contain something like the following:
          
          apphub: {
           application: {3}
           workload: {
              criticalityType: "MEDIUM"
              environmentType: "STAGING"
              **id: "my-workload-id"**
           }
          }
          

    * You filter your log data by the resource type of [**Audited Resource**](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#tag_audited_resource). The values in the `resource.labels.service` label contribute to the entries in the **Workload / Service** dimension.

    * You have log data that contains the `resource.labels.namespace_name` or the `labels.service.name` label.

  * The **Application** dimension is shown when your log data contains an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application ID label, which is of the form `apphub.application.id`. In your log entry, this label is shown in the `apphub` entry:
        
        apphub: {
          application: {
             container: "projects/my-project"
             **id: "my-app"**
             location: "my-app-location"
          }
          workload: {3}
        }
        




Other dimensions, like **Project ID** , are listed based on your selections. For example, the **Project ID** dimension is listed when your query restricts the log entries to those whose resource type is **Kubernetes Container** , or when you've selected a log view.

### Refine your query

To refine your query, select a value from the **Fields** pane. For example, if you select **Error** in the **Severity** heading, then the query pane is updated to include `severity=ERROR`.

To remove a selection, click the **Clear** button.

### Add fields to the **Fields** pane

You can add certain [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) key-value pairs to the **Logs field** pane from the log entries populated in the **Query results** pane. For example, if you frequently filter by the value of the `jsonPayload.message` field, then add it to the **Fields** pane.

To add a field to the **Fields** pane, do the following:

  1. Select a log entry and click _chevron_right_ **Expand**.

  2. Find the field that you want to add to the panel, select the value, and in the menu, select **Pin to Fields pane**.

The custom field appears in the **Fields** pane as a list of key-value pairs.

If the **Pin to Fields pane** entry isn't listed in the menu, then you can't add the field to the **Fields** pane. For example, you can't add the `insertID` field to the **Fields** pane.




To remove a custom field from the **Fields** pane, click **Remove** next to the field.

Note that the following types of fields can't be added to the **Fields** pane:

  * Fields related to time; for example, `receiveTimestamp` and `protoPayload.startTime`.
  * Fields with high cardinality; for example, `insertId` and `protoPayload.latency`.
  * Fields with array indexes in their path; for example, `protoPayload.authorizationInfo[0].resource`.



## Timeline

**Note:** Each element of the timeline displays the approximate number of log entries received in the time interval associated with the element. To get an exact count of the number of log entries received in a time interval, use Observability Analytics or [copy log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs) to a Cloud Storage bucket.

With the **Timeline** pane, you can visualize the distribution of log entries over time. The timeline regenerates when you run a query, making it easier to see trends in your log entries and troubleshoot problems.

To show or hide the **Timeline** pane, click keyboard_capslock **Collapse timeline**.

### **Timeline** features

  1. Timeline bars: Each timeline bar represents a time range. Each bar contains a three-color breakdown for the log-severity levels captured in each bar's time range. The colors represent the following log severities:

     * Blue: Low severities such as **Default** , **Debug** , **Info** , and **Notice**.
     * Yellow: Medium severities such as **Warning**.
     * Red: High severities such as **Error** , **Critical** , **Alert** , and **Emergency**.

Each bar in the **Timeline** features a menu with options to analyze your log entries.

  2. Time controls: Let you adjust the time range of the log entries you see in the **Query results** pane. For details on these options, see Analyze log entries using time controls.

  3. Time range: Shows you the time range of the log entries, represented by histogram bars. The timeline helps to orient you to the log entries you're viewing within the larger time range of your query.




### Analyze log entries using time controls

You can use time controls in the timeline to help you investigate and analyze your log entries.

**Tip:** When you adjust the timeline's time controls, the log entries in the **Query results** and **Fields** panes adjusts according to the time range captured by the timeline. Adjusting the timeline's time controls doesn't alter the query expression in the **Query** pane.

#### Adjust time controls

The timeline provides time controls that let you adjust the data that you see in the Logs Explorer:

  * Time handles: Drag the timeline's handles inward to narrow the data or outward to widen the data in the timeline. Click **Run**.

  * Slide the timeline forward and backward: Click _chevron_right_ **Forward arrow** to slide the timeline to a later time. Click _chevron_left_ **Backward arrow** to slide the timeline to an earlier time.

  * Zoom in and out: Click _zoom_out_ **Zoom-out** to broaden the data shown in the timeline. Click _zoom_in_ **Zoom-in** to narrow the data shown in the timeline.

  * Hide timeline: Click keyboard_capslock **Collapse timeline** to hide the timeline.




Timeline modifications are constrained to be between the current time ("now") and up to 30 days in the past.

#### Scroll or zoom to time

In addition to the time controls previously listed, the timeline provides the **Scroll to time** and **Zoom to time** features to give you more in-depth control of the timeline and the data that you see in other panes in the Logs Explorer. Perhaps a particular bar in the timeline interests you based on its relative size or severity levels. You can select that bar to adjust the log entries you see in the Logs Explorer.

You can use the **Scroll to time** feature to browse your log entries without changing the values in the **Timeline** and **Fields** panes. When you select the **Scroll to time** feature, the following happens:

  * The log entries that you see in the **Query results** pane adjusts according to the time range captured by the selected timeline bar.

The query isn't run, but a partial reload of the data might occur to ensure you're seeing log entries in the **Query results** pane that correspond with the selected timeline bar's time range.

  * The console URL updates to contain the `timestamp` of the most recent log captured by the time range of the selected timeline bar.




To select the **Scroll to time** feature, do the following:

  1. Hold the pointer over a bar in the timeline. A pane containing summary information about the log entries for the specified time range appears.

  2. In the pane, select **Scroll to time**.

Alternatively, clicking on a timeline bar is equivalent to selecting **Scroll to time**.




The **Zoom to time** feature is similar to **Scroll to time** , but it runs a query on your log entries based on the time range captured by a selected timeline bar. When you select the **Zoom to time** feature, the following happens:

  * The log entries that you see in the **Query results** pane reloads and narrows according to the time-range restriction of the selected timeline bar.
  * The console URL updates to contain the `timestamp` of the most recent log captured by the time range of the selected timeline bar.
  * The timeline changes to show only log entries that have a `timestamp` value that falls within the time range of the selected timeline bar.
  * The data in the **Fields** pane adjusts according to the time range captured by the selected timeline bar.



To select the **Zoom to time** feature, do the following:

  1. Hold the pointer over a bar in the timeline. A pane containing summary information about the log entries for the specified time range appears.

  2. In the pane, select **Zoom to time**.




## View your query results

The **Query results** pane displays the result of your query. This pane also includes features that help you troubleshoot your applications. For example, you can view more details for each log entry, and search for patterns and strings in your log entries.

### Highlight search terms, monitor and download your log entries

There are various options to analyze your log entries by selecting the **Actions** menu of the **Query results** toolbar:

  * ink_highlighter **Highlight in results** : Enter text to be highlighted in your query results.


  * _add_chart_ **Create metric** : Set up a [log-based metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics).


  * _call_merge_ **Create sink** : Create a log sink that auto-populates the sink's inclusion filter with the current query expression.


  * _add_alert_ **Create log alert** : Set up a [log-based alerting policy](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

  * _edit_ **Manage alerts** : View and manage alerting policies.



  * _download_ **Download** : Download your log entries in CSV or JSON format. For more information, see Download log entries.



#### Download log entries

**Note:** This feature doesn't support the bulk download of log entries. You can download up to 10,000 log entries, provided the time to query the log entries and perform the download can complete within the timeout for the command. You can [copy log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs) in bulk to a Cloud Storage bucket.

To get the permissions that you need to download log entries, ask your administrator to grant you the [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This role contains the `logging.logEntries.download` permission. You can also grant a role that contains the `logging.logEntries.list` permission, which lets a principal view and download log entries. 

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To download your log entries, do the following:

  1. In the **Actions** menu of the **Query results** pane, click **Download**.

  2. In the **Download logs** dialog, select CSV or JSON format, and then click **Download**.

  3. Select what to do with the log entries. You have the following options:

     * Download the data to your computer.
     * Download the data to Google Drive.
     * View the data in a new tab.

When you save a CSV and select Google Drive, you can open the file in Google Sheets.




For troubleshooting information, see Download of log entries fails.

### Analyze results by using Observability Analytics

You can aggregate, analyze, and chart your log data by using SQL queries in the **Observability Analytics** page when your project contains log buckets that are upgraded to use Observability Analytics. To go to the Observability Analytics page from the Logs Explorer, in the **Query results** toolbar, click _manage_search_ **Analyze results**.

The _manage_search_ **Analyze results** button is visible only when the log bucket that contains the log view you are querying has been upgraded to use Observability Analytics. For example, if the toolbar displays ![](https://docs.cloud.google.com/static/stackdriver/images/log-view-icon.png)**N log view** , then the _manage_search_ **Analyze results** button is shown when the log bucket for at least one of the selected log views is upgraded to use Observability Analytics. For more information, see [Upgrade a log bucket to use Observability Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket).

The following occurs when you click _manage_search_ **Analyze results** :

  * The time range in the Logs Explorer might be automatically adjusted so that there is meaningful log data in the **Observability Analytics** page.

  * The **Observability Analytics** page opens in a new tab and automatically translates the current Logging query language query into a SQL query.

  * The resource selected by the Google Cloud project picker and a toolbar setting determine how the `FROM` clause in the SQL query is constructed. The selected resource can be a project, folder, or organization:

    * If the toolbar displays ![](https://docs.cloud.google.com/static/stackdriver/images/gc-project-icon.png)**Project logs** or ![](https://docs.cloud.google.com/static/stackdriver/images/log-scope-icon.png)**_Default** , then the resource's `_Required` and `_Default` buckets are queried.

    * If the toolbar displays ![](https://docs.cloud.google.com/static/stackdriver/images/log-view-icon.png)**N log view** , then log views on log buckets in the current project are queried. Log views on log buckets stored by different resources are ignored.

    * If the toolbar displays ![](https://docs.cloud.google.com/static/stackdriver/images/log-scope-icon.png)**myscope** , where "myscope" is the name of a custom log scope, then the previous rules are applied to the resources listed in the selected [log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage). For example, if the log scope contains log views, then only those log views on log buckets stored by the resource are queried.

**Note:** Observability Analytics doesn't support querying across projects or regions. If resources in multiple projects or regions are searched for log entries, then the **Observability Analytics** might show different log entries than the **Logs Explorer** page.



In the Observability Analytics page, you can view your results in tabular form, or as a chart. In the **Chart** tab, you can select the data that is charted, customize the chart configuration, or save a chart to a custom dashboard. For information about creating charts from your query results and saving charts to a custom dashboard, see [Chart query results with Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/charts).

For information about using SQL to write queries, see [Query and view logs in Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).

### Investigate a log entry by using Gemini Cloud Assist

**Note:** Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/service-terms), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview).**Caution:** Gemini Cloud Assist can store data in any Google Cloud data center globally. Don't enable the [Gemini Cloud Assist API](https://docs.cloud.google.com/gemini/docs/discover/certifications#cloud-assist-security) for projects that have data residency or [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/cmek) requirements.

You can use Gemini Cloud Assist to convert a log entry into natural language. For example, for an audit log, Gemini Cloud Assist displays a summary, information about who initiated the action, the action they attempted, whether the action was allowed, and when the action was performed. For a log entry with a severity of at least `ERROR`, Gemini Cloud Assist might summarize the issue, provide a list of potential causes, and suggest remediation steps.

To have Gemini Cloud Assist generate a summary of a log entry, do the following:

  1. Select the log entry you want to summarize, and click _chevron_right_ **Expand**.

  2. In the toolbar for the log entry, click **Investigate log**.

Cloud Logging sends the text of the log entry to Gemini Cloud Assist with a prompt to summarize the contents of the log entry. Gemini Cloud Assist responds with a generated summary in the **Cloud Assist** pane. The summary is based only on the text of the log entry without any additional context.




For more information about using Gemini Cloud Assist investigations, see the following documents:

  * [Troubleshoot issues with Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations)
  * [Create a Gemini Cloud Assist investigation](https://docs.cloud.google.com/cloud-assist/create-investigation)
  * [Manage Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/manage-investigations)
  * [Summarize log entries with Gemini assistance](https://docs.cloud.google.com/logging/docs/view/summarize-log-entries-gemini)



### View or hide log entries that match a field

You can view or hide log entries that match a field in a log entry, which lets you focus on entries that contain the same field content.

To view or hide log entries that match a specific field in a log entry, do the following:

  1. Select a log entry and click _chevron_right_ **Expand**.

  2. Click a field's value within the log entry, such as `compute.googleapis.com`, which is a `serviceName`.

  3. From the menu, select **Show matching entries** or **Hide matching entries**.

The query updates with a query that shows or hides similar entries, and the **Query results** reload with new results.




### Pin log entries

After you run a query, you can highlight a log entry by pinning it. The pinned log entry stays centered in the **Query results** pane. If you run a new query and the pinned log entry isn't included, then you are prompted to unpin the log entry.

To pin a log entry, do the following:

  1. Hold the pointer over the log entry that you want to pin.
  2. Click _push_pin_ **Pin**.



After you pin a log entry, its background is darkened, and a _push_pin_ **Pin** icon is shown. A pin icon also appears on the **Timeline** pane based on the pinned log entry's `timestamp`.

To unpin a log entry, click the pin icon again.

#### Show log entries that match the resource of a pinned log entry

After you pin a log entry, you can run a new query that displays log entries that match the resource type or resource labels of the pinned log.

To pin a log entry and display log entries that match the same resource type or resource labels, do the following:

  1. Click _arrow_drop_down_ **Down arrow** next to the pinned log to expand the pin menu.

  2. Make a selection from the pin menu:

     * To rerun the query with the same [`resource.type`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) as the pinned log, select **Same resource.type**.

For example, suppose you pin a log entry with a `resource.type` of `k8s_node`. If you select **Same resource.type** , then the query is rerun to display all log entries with `resource.type="k8s_node"`.

     * To rerun the query with the same [`resource.labels`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) as the pinned log, select **Same resource.labels**.

     * To rerun the query with the same [`trace`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) as the pinned log, select **Same trace**.
     * To clear the query and show all log entries, select **Show all**.



#### View a pinned log entry in the **Timeline**

You can use the **Timeline** to highlight, scroll to, and further examine a pinned log entry.

Using the **Timeline** , click _push_pin_ **Pin** , and then choose from the following menu options:

  * **Scroll to log entry** : Bring the log entry into the current **Query results** pane and view the pinned log entry in the context of nearby log entries.
  * **Zoom to log entry** : Narrow the time range that the **Timeline** pane displays and refine your query to isolate the log entries near the pinned log.
  * **Unpin** : Unpin a log entry.



### View trace data

When a log entry contains both the `trace` and the latency-related field, both the latency and trace icons appear.

![Log entry display that contains trace data.](https://docs.cloud.google.com/static/logging/docs/images/trace-latency-chip.png)

When a log entry contains only the `trace` field, then only the trace icon appears.

![Log entry display that contains only the trace field has a trace icon.](https://docs.cloud.google.com/static/logging/docs/images/trace-icon-only.png)

To view the trace data related to the log entry, click the trace icon. You have the following options:

  * **View trace details** : Shows the parent span and child traces along with details about the trace. To view more details about the trace, navigate to Cloud Trace by clicking **View in Trace**. For more information about the content in the details panel, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

**Note:** The **View trace details** button is only available when `traceSampled` is true.

  * **Show all logs for this trace** : Refines and runs the query by adding the `trace` field set to the identifier of the trace associated with the log entry.

  * **Show only traced requests** : Refines and runs the query by adding the `traceSampled` field set to `True`. For more information on sampling, see [Sampling rate](https://docs.cloud.google.com/trace/docs/setup#force-trace).




### View Monitoring data

For certain log entries, such as those for GKE and Compute Engine, you can select the resource type from the log entry's summary line to display a menu with the following options:

  * **View monitoring details** : opens a details panel for a GKE resource. For information on the details panel, see [View resource details](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/observing#alerting-details).
  * **View in Monitoring** : opens to a **Monitoring** page for the resource.
  * **View in GKE** or **View in Compute Engine** : opens the **Details** page for the resource within the GKE or Compute Engine user interface.



![Display of Logs Explorer menu for GKE resources.](https://docs.cloud.google.com/static/logging/docs/images/k8s_explorer_menu.png)

### Copy a link to a log entry

To share a link to a log, expand a log entry, and then select _content_copy_ **Copy**. You can choose to copy a log in JSON, or a link to the log. The link is copied to your clipboard. You can send the link to users who have access to the Google Cloud project. When a user pastes the link into a browser or selects it, Logging pins the log entry in their **Query results** pane.

## Example Logs Explorer queries

For suggested queries, arranged by Google Cloud product and use case, see [Sample queries using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/query-library). For example, you can run [Kubernetes-related queries](https://docs.cloud.google.com/logging/docs/view/query-library#kubernetes-filters) to find Google Kubernetes Engine log entries.

## View Compute Engine log entries

For certain Compute Engine resource types, such as `gce_instance` and `gce_network`, you see the resource name with the resource ID as subtext in several places in the Logs Explorer. For example, for the `gce_instance` resource type, you see the VM name alongside the VM ID. The resource names help you identify the correct resource ID, on which you can build queries.

You might see Compute Engine resource names in the following places:

  * **Query** pane filter menus: Compute Engine resource types show resource names, with their corresponding resource IDs as subtext.
  * Fields: Compute Engine resource types show the resource name, rather than the resource ID, in the field dimensions.
  * Query results: For Compute Engine VM instance log entries, the `resource.labels` field shows metadata with the corresponding resource name.
  * Summary fields: For Compute Engine VM instance log entries, the chip shows the resource name instead of the resource ID.



## Troubleshoot logging issues

This section provides instructions for troubleshooting common issues when using the Logs Explorer.

If you're experiencing issues when trying to view log entries in sink destinations, see [Troubleshoot routing and sinks](https://docs.cloud.google.com/logging/docs/export/troubleshoot).

### The all resources and all log name menus are disabled

You open the Logs Explorer page, and the **All resources** and **All log names** menus are disabled.

This is expected behavior when the Logs Explorer page is searching a log view that contains a [flexible filter](https://docs.cloud.google.com/logging/docs/logs-views#view-filter). These filters use an extended set of [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) such as disjunctive clauses.

### Download of logs fails

You are using the Logs Explorer and click _download_ **Download**. The command starts but then fails to complete or reports an error.

To resolve this issue, reduce the time it takes for the command to execute by trying the following:

  * In the **Download logs** dialog, reduce the value of **Maximum log entries**.
  * Reduce the time period over which logs are queried.
  * In the query results toolbar, click **Hide similar entries** before you begin the download.


  * Modify your query to use [indexed fields](https://docs.cloud.google.com/logging/docs/analyze/custom-index).

**Note:** The download feature isn't intended for the bulk download of logs. You can [copy logs](https://docs.cloud.google.com/logging/docs/routing/copy-logs) to a Cloud Storage bucket.

### Can't find console logs for a VM instance

Logs written to the console of a Compute Engine instance might not be available in the Logs Explorer. To view these logs, do the following:

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Select the instance, and then select **Serial port 1 (console)** in the **Logs** section of the page.




You can configure your instances such that their serial port output is sent to Cloud Logging. For more information, see [Enabling and disabling serial port output logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver).

### Get Google Cloud project or organization ID

To get a Google Cloud project or organization ID from anywhere in the Google Cloud console, expand the list of Google Cloud projects from the Google Cloud project and organization selector and find the Google Cloud project ID in the **ID** column.

### Can't see log entries

If you don't see any log entries, check the following:

  * Verify that the correct Google Cloud project is selected.

  * Verify that your Google Cloud project is using resources that generate logs and that there is activity on those resources. Even if the Google Cloud project is new, it should have audit logs recording the fact that it was created. For information about how to verify that you're using a resource that generates logs, see [Mapping services to resource types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-mappings).

  * Ensure that the time range isn't too narrow.

  * View your [current exclusion queries](https://docs.cloud.google.com/logging/docs/exclusions#viewing-exclusion-filters) to ensure that the logs you're looking for aren't accidentally excluded.

  * Ensure that you have permission to view the log entries in the projects and log views referenced by setting of the **Refine scope** menu. For information about how to adjust the scope of your search, see [Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope).




### My query is correct but I still don't see log entries

  * You can't see log entries that are older than the Logging retention period. See [Log retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) for the logs retention period in effect.

  * During periods of heavy load, there could be delays in sending logs to Logging or in receiving and displaying the logs.

  * The Logs Explorer doesn't show log entries that have timestamps in the future until the current time has "caught up" with them. This is an unusual situation, probably caused by a time skew in the application sending the logs.

  * The query scope was set too large and couldn't complete within a reasonable amount of time. You might see this as "deadline expired before operation could complete". Try making your query more specific or reducing the time range.




### Query returns an error

If you issue a query over a resource without specifying a bucket, then Cloud Logging uses the history of the sinks in the Google Cloud project to determine where entries might have been written for that resource. If Cloud Logging identifies more than 200 buckets where entries might have been written, then the query fails with the message `Error: Invalid query`.

To resolve this issue, refine the scope of your query to a subset of the storage. For more information, see [Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope).

### Query results time range doesn't match query

The logs data you see in the **Query results** and **Fields** pane adjusts according to the time range captured by the histogram timeline. You adjust the histogram timeline using the histogram's time controls or the [time-range selector](https://docs.cloud.google.com/logging/docs/view/building-queries#time-range). Adjusting these time controls doesn't alter the query expression in the **Query** pane.

When you have a query with a timestamp, the time-range selector is disabled. The query uses the timestamp expression as its time-range restriction. If a query doesn't use a timestamp expression, then the query uses the time-range selector as its time-range restriction.

## Get support

For information on getting support, see the [Google Cloud Observability support page](https://docs.cloud.google.com/stackdriver/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
