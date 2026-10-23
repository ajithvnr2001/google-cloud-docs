---
url: https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring/
title: Use the code editor for PromQL \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:30.865578+00:00
---

# Use the code editor for PromQL  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Use the code editor for PromQL Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the code editor for PromQL. The editor is available in the Google Cloud console and provides suggestions and other tools for creating valid PromQL queries.

This page doesn't cover the PromQL language; for information about PromQL, we recommend consulting open source documentation. The following resources can help you get started:

  * [Querying Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/)
  * [Query examples](https://prometheus.io/docs/prometheus/latest/querying/examples/)
  * [PromQL cheat sheet](https://promlabs.com/promql-cheat-sheet/)



## Access the code editor

You access PromQL from the following pages in the Google Cloud console:

  * **Metrics Explorer**
  * **Add widget** when creating dashboards



To open the code editor when using Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. After you complete your query, you can configure the legend or change how the data is displayed. For more information, see the following pages:

     * [Set chart display options](https://docs.cloud.google.com/monitoring/charts/chart-view-options)
     * [Configure legends](https://docs.cloud.google.com/monitoring/charts/working-with-legends)



## Use the code editor

To use the code editor, type your query into the text field and click **Run Query**.

### Autocompletion

As you type your query, the editor displays a list of syntactically valid completions. You can manually bring up the autocompletion menu by pressing `Control+Space`, and you can dismiss it by pressing `Escape`.

To navigate the list of options, use the arrow keys. Pressing `Enter` inserts the selected choice.

To insert the prefix common to all available choices, press `Tab`.

### Find and replace

The editor supports a find-and-replace feature. To find, and optionally replace, terms in your query, press `Control+F` (or `Command+F` on Mac). The following screenshot shows the feature:

![code editor supports a find-and-replace feature.](https://docs.cloud.google.com/static/monitoring/images/promql-find-replace.png)

### Editor controls

The editor has two controls that determine how it interacts with your query.

By default, your query is executed only when you click **Run Query**. You can set up the editor to automatically execute your query as you type, but this option is disabled by default.

To enable the auto-run option, use the **Auto-run** toggle. When this option is enabled, the editor works as follows:

  * The **Run Query** button isn't displayed.
  * Errors messages appear continuously as you type.
  * If your cursor is at the end of a query that is incomplete but has no errors, then the editor shows a yellow triangle in the control bar. If there is room, the text **Incomplete query** also appears.

The editor does not attempt to evaluate incomplete queries.




There is also a grab-bar between the code editor and the chart region. Use this bar to change the relative sizes of the two regions.

## Save charts

How you save a chart depends on the context in which you created the chart:

  * From Metrics Explorer.
  * As part of creating or editing a custom dashboard.



### Save charts from Metrics Explorer

From the code editor in Metrics Explorer, you have the option to save your chart to a custom dashboard. To save your chart, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter your query in the editor.
  4. If you do not have the auto-run option for the code editor enabled, then run your query by clicking **Run Query** before saving the chart. By default, custom dashboards periodically save your changes. When you don't run your query first, the code editor saves the last query you ran. 

  5. Click **Save as** and select **Dashboard chart** , and then complete the dialog.




### Save charts on a custom dashboard

To save a new chart to your dashboard, do the following:

  1. Give the chart a descriptive title.

  2. If you do not have the auto-run option for the code editor enabled, then run your query by clicking **Run Query** before saving the chart. By default, custom dashboards periodically save your changes. When you don't run your query first, the code editor saves the last query you ran. 

  3. If you don't have autosave enabled for your dashboard, then click **Save**.




The Google Cloud console supports [page-level filters for custom dashboards](https://docs.cloud.google.com/monitoring/charts/filter-dashboard). These filters are supported for PromQL charts on your custom dashboards.

## Exit the code editor

To exit the code editor without saving your query, click one of the other selector tabs. Any query text in the editor is discarded, but you are given the option to save it to the clipboard.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
