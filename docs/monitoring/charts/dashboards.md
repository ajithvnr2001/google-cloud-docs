---
url: https://docs.cloud.google.com/monitoring/charts/dashboards/
title: Create and manage custom dashboards \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:26.569540+00:00
---

# Create and manage custom dashboards  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create and manage custom dashboards Stay organized with collections  Save and categorize content based on your preferences. 

Custom dashboards in Cloud Monitoring let you organize and view the metrics, logs, traces, alerts, and service-level objectives (SLOs) that matter most to your applications in a single place. Using the Google Cloud console, you can build dashboards from scratch, import Grafana dashboards, or copy, modify, and share existing dashboards across projects.

To manage custom dashboards by using the Cloud Monitoring API or the Google Cloud CLI, see [Create and manage dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard). To view preconfigured dashboards for Google Cloud services, see [View and copy Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards).

## About custom dashboards

Custom dashboards support a variety of widget types, so you can choose the best way to display your data. By default, dashboards display all metric data that is available to your Google Cloud project. If you [configure a metrics scope](https://docs.cloud.google.com/monitoring/settings/multiple-projects), then your dashboard can display metric data for multiple Google Cloud projects.

A custom dashboard can display all of the following:

  * [Charts and indicators](https://docs.cloud.google.com/monitoring/dashboards#create_a_new_chart).
  * [Log entries from multiple Google Cloud projects or log views](https://docs.cloud.google.com/monitoring/charts/view-logs).
  * [Alerts and charts for alerting policies](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents).
  * [Service level objectives (SLOs)](https://docs.cloud.google.com/monitoring/dashboards/slos).
  * [Text](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping).
  * [Trace data](https://docs.cloud.google.com/monitoring/dashboards/display-traces-on-dashboards).



You can improve the load time or usability of a dashboard by [grouping widgets](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping#organize_widgets). For example, you might add sections to a dashboard. Alternatively, you might add widgets to a container that is either expanded or collapsed.

After you create a dashboard, you can add filters, variables, events, or user-defined labels:

  * Dashboard-wide filters apply to all widgets on the dashboard. These filters can be helpful when you are troubleshooting. For example, you can use these filters to display data only for a specific zone. For more information, see Add or remove filters.

  * Variables apply to selected widgets. For example, you can use a variable to modify the query issued by the widget, or to control the visibility of a widget. For more information, see [Create and manage variables and pinned filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent).

  * [Events](https://docs.cloud.google.com/monitoring/dashboards/event-types), such as the crash of a Google Kubernetes Engine Pod, can help you correlate data from different sources when you're troubleshooting an issue. For more information, see [Show events on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/show-events).

  * [Labels](https://docs.cloud.google.com/monitoring/charts/dashboards#add-remove-labels) can help you locate dashboards based on the type of content they display. For example, you might add the label `prod` to dashboards that display information about production systems. Similarly, you might add the label `staging` to indicate the dashboard displays information about staging systems.


**Note:** By default, dashboards automatically refresh their display when new data is available, and they automatically save your configuration changes. For information about how to change these settings, see Disable data refresh and Disable automatic saving of configuration changes.

## Before you begin

Complete the following in the Google Cloud project where you want to create and manage dashboards:

  * To get the permissions that you need to create and modify custom dashboards by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).




## Add a custom dashboard to your project

There are different approaches that you can use to add a custom dashboard to your Google Cloud project:

  * You can create a dashboard.
  * You can copy, or duplicate, a dashboard.
  * You can copy a dashboard from project to project.
  * You can upload or install dashboards from a shared location.
  * You can import a dashboard from Grafana.



For example, suppose you have multiple Google Cloud projects and you want them to define the same custom dashboard. For this situation, you might create the dashboard in one project and then [download a template for the dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards#download-dashboard) to your local system. Next, you can install that template in other Google Cloud projects.

### Create a new dashboard

To create a custom dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the **Dashboards** page, click **Create custom dashboard**.
  4. To add widgets to your dashboard, do the following:

     1. In the dashboard toolbar, click _add_ **Add widget**.
     2. In the **Add widget** pane, select a widget to add to your dashboard.

You can select a widget based on the type of data to display or how you want to display the data. In all cases, a configuration pane is opened. For example, you can select the **Metric** widget and then set the visualization to **Stacked area**. Or, you can select the **Stacked area** widget and then select the metric.

     3. Configure the widget.

     4. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.

After the widget is added to your dashboard, you can change the widget's configuration.

  5. To save your modified dashboard, in the toolbar, click **Save**.

  6. Optional: Add user-defined labels to your dashboard:

     1. In the list of dashboards, locate the dashboard and then click sell **Add labels to dashboard**.
     2. Do one of the following: 
        * To create a label and add it to your dashboard, in the **Create a new label** section, enter the name of the label in the textbox and then click **Create and apply**.

        * To configure which labels are added to your dashboard, click _arrow_drop_down_ **Select labels to apply** , select the labels, and then click **Ok**.
     3. To save your changes, click **Confirm**.



### Copy a dashboard

When you want to experiment with different metrics or different aggregation options, you can copy a dashboard and then use the new dashboard for experimentation purposes.

To copy a dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the **Dashboards Overview** page, identify the dashboard to copy, and then click _content_copy_ **Copy dashboard**.
  4. Optional: Update the dashboard's name.
  5. Click **Copy** in the confirmation dialog.



### Copy a dashboard into another project

**Note:** When you copy a dashboard, you copy the template for the dashboard, not the data it displays.

To copy a dashboard from one project to another, your IAM role for the destination Google Cloud projects must include the Monitoring editor permission. For more information about roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

To copy a dashboard to another Google Cloud project, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Copy the dashboard's JSON into your clipboard:

     1. In the dashboard toolbar, click _settings_ **Settings** , then **JSON** , and then **JSON Editor**.
     2. In the editor's toolbar, click _content_copy_ **Copy**.
  4. Paste the JSON in your clipboard into a new dashboard created in a different project:

     1. Use the Google Cloud console project picker to select the project where you want to create the copy.
     2. Click **Create dashboard**.
     3. In the dashboard toolbar, click _settings_ **Settings** , click **JSON** , and then click **JSON Editor**.
     4. Paste the content of your clipboard into the editor.
     5. Click **Apply changes**.
     6. To save your modified dashboard, in the toolbar, click **Save**.



### Install a dashboard template

You can upload a dashboard template to your Google Cloud project when that template is stored in a shared location. Cloud Monitoring, for example, provides a curated set of dashboard templates on GitHub that are specific to various Google Cloud services. The charts on these dashboards present a selection of metrics relevant to a specific service.

After you upload a dashboard template, you can customize it. For example, you might add charts, [add labels](https://docs.cloud.google.com/monitoring/charts/dashboards#add-remove-labels), or [configure which events to display](https://docs.cloud.google.com/monitoring/dashboards/show-events).

For more information, see [Install a dashboard template](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates).

### Import a dashboard from Grafana

Cloud Monitoring provides an importer that you can use to import dashboard files in the [Grafana](https://grafana.com/) JSON format into Cloud Monitoring. For more information, see [Import Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/monitoring/dashboards/import-grafana-dashboards).

## Find and view a dashboard

Custom dashboards are displayed in the same list as the [service-specific dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards) that Cloud Monitoring creates as you add resources to your Google Cloud project.

To view a dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 

The **Dashboards** page lists all dashboards in your Google Cloud project.

  3. To find a dashboard, do any of the following:

     * Use the **Recently Viewed** and **Favorites** options to restrict which dashboards are listed.

     * Use the **Integrations** menu to list only those dashboards that are associated with a specific integration.

     * Use the **Type** menu to list only those dashboards that have a specific type. For example, to list the dashboards that are created automatically by Google Cloud based on your usage of Google Cloud services, in the **Type** menu, select **Google Services**. To further refine the list, use the _filter_list_ **Filter** bar.

     * Use the **Labels** menu to list only those dashboards that have a specific user-defined label. For example, suppose you created a label named `Staging` and then applied that label to your dashboards that display information about your staging resources. To list these dashboards, select the label **Staging**. To further refine the list, use the _filter_list_ **Filter** bar.

     * Add filters to the _filter_list_ **Filter** bar:

       * To list dashboards whose name or description contains specific text, enter that text into the _filter_list_ **Filter** bar.

       * To list dashboards after filtering by the value of a dashboard field, do the following:

         1. Select **Search your dashboards** and then select a field to filter by. You can filter by the following dashboard fields: name, description, type, and user-defined label.

         2. Either enter a value for the filter or make a selection from the menu.

       * To list dashboards that don't have any charts, select **Search your dashboards** , select **Labels** , and then select **(Empty)**.

When you add multiple filters and don't include the **OR** operator between two filters, an `AND` operator joins the filters.

  4. After you locate the dashboard, select it.




## View dashboard version history

You can determine what changes were made to a dashboard by viewing the version history, which lists the user who made a change and how many changes were made. You can also revert to a previous version of the dashboard, or compare a previous version to the current version by viewing the diff. Revisions to an existing dashboard are retained for 90 days, but the latest revision is retained indefinitely.

To view the version history for a dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 

  3. In the dashboard toolbar, go to _settings_ **Settings** , and then select **View Version History**. The version history panel opens.

  4. Optional: To restore a previous version of a dashboard, select a version from the list and click the **Revert** button. The dashboard reloads and displays the previous version.




## Modify a dashboard

After you create a dashboard, you might determine that it needs modification to be more useful to you. For example, you might want to add or remove widgets, change the layout, or change how a widget displays data. Additionally, you might want to add labels to a dashboard, either to make it easier to find or to indicate the type of content on the dashboard.

**Note:** If you create a dashboard by using Terraform, then you can view the dashboard with the Google Cloud console. However, don't edit the dashboard in the Google Cloud console. For more information, see [Troubleshoot: Terraform-created dashboard is rescaled](https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts#dashboard-rescaled).

### Add or remove labels

Labels can help you locate dashboards based on the type of content they display. For example, you might add the label `prod` to dashboards that display information about production systems. Similarly, you might add the label `staging` to indicate the dashboard displays information about staging systems. Next, when you are listing your dashboards, you can select a label to filter the list to those dashboards that contain the selected label.

To add or remove user-defined labels on a dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the list of dashboards, locate the dashboard and then click sell **Add labels to dashboard**.
  4. Do one of the following: 
     * To create a label and add it to your dashboard, in the **Create a new label** section, enter the name of the label in the textbox and then click **Create and apply**.

     * To configure which labels are added to your dashboard, click _arrow_drop_down_ **Select labels to apply** , select the labels, and then click **Ok**.
  5. To save your changes, click **Confirm**.



To list, edit, and delete your labels, click _settings_ **Manage labels**.

### Add or remove filters and variables

After you create a dashboard, you can add filters and variables. Filters apply to all widgets on a dashboard. Variables apply to some widgets on the dashboard. Filters and variables can be helpful when you are troubleshooting. For example, you can use a filter so that the dashboard displays data only for a specific zone.

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Locate and select the dashboard.

     * To add a dashboard-wide filter that applies only for your current session, use the dashboard's _filter_list_ filter bar. For more information, see [Temporary filters](https://docs.cloud.google.com/monitoring/charts/filter-dashboard).

     * To add a dashboard-wide filter that is permanent, in the dashboard toolbar, go to _settings_ **Settings** , and then select **Manage Filters**. For more information, see [Create and manage variables and pinned filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent).




### Modify widgets or change layout

To modify the widgets on a dashboard or the layout of the dashboard, do any of the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Locate and select the dashboard.
  4. Optional: To add a widget to your dashboard, in the dashboard toolbar, click _add_ **Add widget** , then select and configure the widget. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.

For more information, see the following pages:

     * [Add charts and tables](https://docs.cloud.google.com/monitoring/charts)
     * [Display alerts and charts for alerting policies](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents)
     * [Display logs](https://docs.cloud.google.com/monitoring/charts/view-logs)
     * [Display SLOs](https://docs.cloud.google.com/monitoring/dashboards/slos)
     * [Add text and groupings](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping)
  5. Optional: To modify a widget, do one of the following:

     * Place your pointer on the widget to activate the toolbar, click _edit_ **Edit widget** , and then update the widget. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.

You can change most settings for the widget, including the widget type. For example, to change a line chart to a stacked area chart, click **Line chart** _arrow_drop_down_ and select **Stacked area chart** from the menu. For more information, see [Change a widget's type](https://docs.cloud.google.com/monitoring/charts/manage-widgets#changing).

     * Click _settings_ **Settings** , click **JSON** , and then click **JSON Editor**. If you modify the JSON, then you must click **Apply changes**.

You can also access the JSON for a widget by editing the widget and then clicking _code_ **View code** in the widget's toolbar.

  6. Optional: To delete a widget, place your pointer on the widget to activate the toolbar, and then do one of the following:

     * If the toolbar of the widget displays a delete **Delete** button, then click that button.
     * Otherwise, click _more_vert_ **More options** , and then select **Delete widget**.

To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.

  7. Optional: To reposition a widget, use your pointer to drag the widget by its header to a new location. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.

You can't reposition widgets when a dashboard is in grid mode.

  8. Optional: To resize a widget, use your pointer to reposition the right-hand corner of the widget. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.

You can't resize widgets when a dashboard is in grid mode.

  9. To save your modified dashboard, in the toolbar, click **Save**.




## Delete a dashboard

Deleting a dashboard that contains a chart for an alerting policy doesn't delete the alerting policies whose data was displayed on those charts. Therefore, you might receive notifications from those policies after the dashboard is deleted. For information about how to manage your policies, which you do from the **Alerting** page in the Google Cloud console, see [Manage alerting policies](https://docs.cloud.google.com/monitoring/alerts/manage-alerts).

To delete a custom dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. To begin the delete action, find the dashboard you want to delete and click delete **Delete**.
  4. In the confirmation dialog, click **Delete**.
  5. To save your modified dashboard, in the toolbar, click **Save**.



## Save a dashboard as a template to a local system

You might have created a custom dashboard that others in your team or organization want to install in their projects. When you want to share a dashboard template, save it to your local system, and then move or copy the template to a shared location. For example, you might copy the template to a shared drive or to a source code repository like GitHub. Any individual with access to the stored location can install the dashboard into their Google Cloud projects.

To save a template of a custom dashboard to a JSON-formatted file that is stored on your local system, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the dashboard toolbar, click _settings_ **Settings** , click **JSON** , and then click **JSON Editor**.
  4. Click download **File Download** :

The created file, which has the same name as the dashboard, contains a JSON representation of the dashboard. This file is only a template; it doesn't store time-series data.




## Share a dashboard

When you are investigating a data anomaly, you might want another individual in your team or your organization to view the same data that you are viewing. For example, you might see an unexpected drop, or spike, in a performance metric and you want to consult with a teammate. In this scenario, you want your teammate to view the dashboard and its data.

For information about how to share a link to a dashboard, see [Share a custom dashboard](https://docs.cloud.google.com/monitoring/charts/share-dashboards).

## Configure data refresh

When you open a dashboard, it is configured with auto refresh disabled. The toolbar displays a toggle, sync_disabled, which indicates this state.

For your current session, to enable auto refresh, go to the toolbar and select sync_disabled **Enable auto refresh**.

To disable auto refresh after you've enabled it, go to the toolbar and select sync **Disable auto refresh**.

**Note:** You can't configure a dashboard to open with auto refresh enabled. You can enable auto refresh for your current session only. When you reload the dashboard, auto refresh is disabled.

## Configure automatic saving of configuration changes

For each Google Cloud project, Monitoring provides a per-user setting that controls whether modifications to custom dashboards are automatically saved. By default, Monitoring automatically saves modifications. That is, as you edit a custom dashboard, Monitoring periodically saves your changes to the dashboard. If you want to discard changes, then you can restore the original dashboard by using its version history.

You can configure Cloud Monitoring so that when you edit a dashboard, you must select the **Save** option before your changes are applied to the dashboard. Until you save the changes, your modifications apply only to the in-memory state. This configuration lets you modify custom dashboards and then choose to keep or discard those modifications.

To disable the auto-save feature, do the following:

  1. Open any custom dashboard in your Google Cloud project.
  2. In the toolbar, click the **Autosave** toggle until it is in the _toggle_off_ **Off** position.



To enable the auto-save feature, do the following:

  1. Open any custom dashboard in your Google Cloud project.
  2. In the toolbar, click the **Autosave** toggle until it is in the ![](https://docs.cloud.google.com/static/monitoring/images/toggle-on.png)**On** position.

The _cloud_done_ **Cloud Done** icon indicates that Monitoring has saved your changes.




## What's next

  * [Add charts and tables](https://docs.cloud.google.com/monitoring/charts)
  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts)
  * [Configure a metrics scope for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
