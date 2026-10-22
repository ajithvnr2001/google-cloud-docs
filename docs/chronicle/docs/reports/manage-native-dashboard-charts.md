---
url: https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts/
title: Manage charts in dashboards \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:43.192619+00:00
---

# Manage charts in dashboards  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage charts in dashboards

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can manage chart settings in dashboards.

A dashboard is composed of charts that are populated with data using YARA-L queries. Charts on dashboards simplify complex data, revealing trends and patterns through visuals. The chart type used depends on the data and required insights.

**Note:** You must have the `chronicle.nativeDashboards.update` IAM permission to manage charts.

## Add a chart

To add a chart to your dashboard, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click **Add chart**.

  2. In the query editor, enter a YARA-L query to explore and transform your data. You must use the correct YARA-L field prefix for the data source you want to query. For a list of data sources and their required prefixes, see [Dashboard data sources and field prefixes](https://docs.cloud.google.com/chronicle/docs/reports/dashboard-data-sources-prefixes). You can also view and use previous queries from **History** , your saved search, or queries that have been shared with you earlier.

  3. Select an **Absolute** or **Relative** time range. See [Understand Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#relative_time_range) for **Relative time** operator details.

  4. Click **Run Search**. The results display in a tabular format, which serve as the default chart type.

  5. In the **Chart details** , enter a name for the chart.

  6. Optional: Click **Chart type** and select a chart type to change the format of your tabulated search results. For more information about the available chart types, see Chart types.

  7. Change the chart settings according to your requirements.

  8. Review the results and then click **Add to Dashboard**.




### Display zero values in timeline charts

To plot empty time intervals as `0` instead of drawing continuous lines between non-zero data points across timeline charts, follow these guidelines:

  * Keep timestamps as chronological time objects rather than custom string labels. Formatting timestamps as string labels causes the dashboard to treat data points as discrete categories.
  * Use built-in YARA-L granularity constants (for example, `HOUR` or `DAY`) inside the `timestamp.get_timestamp()` function. This lets the dashboard plot continuous timelines and fill inactive intervals with zeros.



For more information and query examples, see [Display zero values in timeline charts](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#zero-value-filling-chart-timelines).

## Add a chart from the chart library

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

The chart library simplifies dashboard creation by allowing you to browse and add pre-existing charts. Instead of building every chart from scratch, you can select from a collection of curated system charts or custom charts created by your organization.

When editing a dashboard, you can access the chart library through a dialog. It provides a searchable (case-insensitive text-based search on name or description), paginated list of charts categorized into two tabs:

  * **Curated charts** : Default charts provided by Google SecOps that cover common security operations and system metrics, for example, ingestion throughput, error counts, and event distributions.
  * **Custom charts** : Charts created by users within your organization.



When you add a chart from the library, Google SecOps duplicates the chart configuration into the target dashboard. The added chart becomes a distinct copy, allowing you to modify it without affecting the original library chart or other dashboards using the chart.

**Note:** This is a one-time copy. Future updates to the original template chart in the library don't automatically propagate to your copy, and your edits don't affect the library template.

To add a chart from the chart library, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click the down arrow next to **Add chart**.
  2. Select **Add from chart library** from the drop-down menu.
  3. In the **Add from chart library** dialog, select the **Curated** or **Custom** tab to filter by chart origin.
  4. Optional: Use the search bar to filter charts by name or description. The search is case-insensitive and matches terms in both fields. 
  5. Select a row in the data table.
  6. Click **Add** to copy the chart to your dashboard. The dialog closes, and the new chart appears on the dashboard.



The charts display in a table with the following columns:

  * **Name** : The display name of the chart.
  * **Description** : A brief explanation of what the chart visualizes.
  * **Data source** : The underlying data sources used by the chart.
  * **Creator** : The user who created the chart, or Google SecOps for curated charts.



### API usage

The chart library functionality is exposed using the `ChartRepository` service.

  * **List charts** : Use `DashboardChartService.ListDashboardCharts` to retrieve available charts. You can filter by `chart_type`, for example, `CURATED` or `CUSTOM`, and apply search queries.
  * **Duplicate charts** : Use `NativeDashboardService.DuplicateChart` to copy a chart from the library to a specific dashboard.



### Chart library limitations

When using the chart library, keep the following restrictions in mind:

  * You can only access the chart library and add charts when the dashboard is in **Edit** mode.
  * The library only supports adding visualization tiles, such as charts. Markdown and link button tiles are not available in the library and must still be created from scratch.
  * You cannot edit, rename, or delete the original charts stored in the library directly from the chart library interface.
  * Custom charts in the library are scoped to your organization. You cannot access custom charts from other Google SecOps customers.
  * If a chart is copied to another dashboard and the original chart is deleted, the chart no longer appears in the list.
  * If a chart is added to a dashboard from its own dashboard, then it is a duplicated chart, and the prefix `Copy of` is added to its name.



## Edit a chart

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click edit**Edit** on a chart to edit it.

  2. In the query editor, modify the YARA-L query to explore and transform your data. You can also view and use previous queries from your history, saved searches, or shared queries.

  3. Modify the time range as required, and then click **Run Query**.

  4. Change the chart settings according to your requirements.

  5. Review the results and click **Save** to save the changes to the chart.




## Delete a chart

To delete a chart, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click more_vert**Menu** on the chart you want to delete, and then click **Delete**.

  2. Click **Confirm** to delete the chart.




## Refresh a chart

You can refresh a chart to clear its cache and display the most recent data.

  * On the **Dashboards** page, click autorenew**Refresh** to refresh the chart.



## View a chart as a table

You can view any chart in table format to see its underlying data.

To view a chart as a table, do the following:

  * On the **Dashboards** page, click more_vert**Menu** next to a chart, and then click **View as table**.



## View a query

You can view a query for any chart in a dashboard to understand how its data is generated and displayed. You can copy, run, or modify the query, as needed.

To view the query, do the following:

  1. On the **Dashboards** page, click more_vert**Menu** next to a chart, and then click **View query**.

  2. Optional: Click **Run in Search** to run the query in [Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search).

  3. Optional: Click content_copy**Copy** to copy the query to clipboard.




## Add a button

You can add buttons to a dashboard, and then use them to open a link. For example, you can add a button that links to a third-party ticketing system.

To add a button, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click **Add** > **Button**.

  2. In the **Create Button** dialog, enter a name for the button in the **Button label** field.

  3. Enter a link that opens when you click the button. Only `http://` and `https://` links are supported.

  4. Optional: Select the **Open the link in new tab** checkbox to open the link in a new tab.

  5. In the **Description** field, enter a button description.

  6. Select **Button style** and **Button color**.

  7. Click **Save**. The button will appear on the dashboard once the changes are saved.




## Edit a button

To edit an existing button, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click edit**Edit** on the button.

  2. In the **Edit button** dialog, make the required changes.

  3. Click **Save**. The button will appear on the dashboard once the changes are saved.




## Make a copy of a button

To make a copy of a button, do the following:

  * On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click content_copy**Copy**.



## Delete a button

To delete an existing button, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, select the button to delete and then click edit**Delete**.

  2. In the **Edit Button** dialog, click **Remove** > **Confirm** to delete the button.




## Add a Markdown widget

You can add a Markdown widget to your dashboard to display additional information about a chart or dashboard.

To add a Markdown widget, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click **Add** > **Markdown**.

  2. In the **New Markdown** dialog, enter text about your widget in the **Markdown content** box.

  3. In the **Background color** list, select a background color for the widget.

  4. Preview the text, and click **Save**.




## Edit a Markdown widget

To edit a Markdown widget, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, select a Markdown widget to edit, and click edit**Edit**.

  2. Modify the text as needed, and then click **Save**.




## Delete a Markdown widget

To delete a Markdown widget, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click more_vert**Menu** on the Markdown widget you want to delete, and then click **Delete**.

  2. Click **Confirm** to delete the Markdown widget.




## Select a chart type

Visualizations help you quickly identify anomalies and trends. Choose the right chart to visualize your data effectively. To create unique charts, consider your audience and choose a chart type that best represents your data. Ensure your data is correctly formatted, and use clear, concise labels for axes and legends.

### Bar chart

Bar charts are useful for comparing categories of data or tracking changes in quantitative data across multiple groups over time. Data points are plotted on two axes with categories on one axis and values on the other. Bars can be oriented vertically (column charts) or horizontally.

### Line chart

Line charts show trends or changes over a continuous interval, such as time, or an area chart to emphasize the volume of change. The horizontal (X) axis represents the continuous interval, and the vertical (Y) axis shows the quantitative variable. Data points are connected by lines, highlighting change patterns. Key features include an emphasis on trends, comparing multiple data series, and analyzing continuous data.

### Sankey chart

Sankey charts visualize flows, relationships, and data pathways. They display nodes that represent data points connected by links that represent the flow between them. The width of each link is proportional to the volume or weight of the flow, which allow you to identify major data paths, bottlenecks, and anomalies. These charts are particularly useful for visualizing security events that involve multi-hop pathways or directional flows, such as network traffic analysis, data exfiltration detection, authentication flows, and SOC workflow monitoring. 

See [Visualize data flows with Sankey charts](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts-sankey) for use case details and examples.

### Area graph

Area graphs similar to line charts, emphasize the magnitude of change over time. They visualize trends and show the cumulative contribution of components to the overall trend. The horizontal (X) axis represents the continuous interval, like time, while the vertical (Y) axis shows the quantitative variable. The area between the line and the X-axis is filled, highlighting value magnitude. Key features include an emphasis on magnitude, the use of stacked area charts to show individual and contributions over time.

### Scatter plot

Scatter plots display the relationship between two quantitative variables, revealing correlations, patterns, and distributions in bivariate data. One quantitative variable is plotted on the horizontal (X) axis, and the other on the vertical (Y) axis. Each data point appears as a dot, positioned according to its values for both the variables. Key features include identifying correlations, detecting patterns, and analyzing data distribution.

#### Chart configuration

The following table describes the common configuration options for bar charts, line charts, area graphs, and scatter plots.

Field | Description  
---|---  
**Name** | Enter a descriptive name for the chart.  
**Description** | Add a brief explanation of the chart's purpose.  
**X-axis** | Choose the data field to display along the X-axis (horizontal axis).  
**Y-axis** | Choose the data field to display along the Y-axis (vertical axis).  
**Threshold coloring** | Click the toggle to activate the threshold coloring. This option automatically adjusts the color of chart elements based on defined numeric conditions. Enter minimum and maximum values. Select a color for the threshold range. Optional: Click add**Add Threshold** to add more thresholds.  
**Display axis in log scale** | Click the toggle to display the X-axis using a logarithmic scale.  
**X-axis label** | Specify the label for the X-axis (horizontal axis).  
**Y-axis label** | Specify the label for the Y-axis (vertical axis).  
**Legend** | Select where to display the chart's legend. For example, Top, Bottom, Left, Right, None.  
**Drill downs** | Click **Customize drill downs** to configure drill downs. For more information, see [Drill down in charts](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts#drill-down).  
  
### Table chart

Table charts display detailed, structured data in rows and columns, providing precise values and enabling comparisons across multiple dimensions. They support sorting, filtering, and pagination to enhance data exploration and usability.

Field | Description  
---|---  
**Name** | Enter a descriptive name for the chart.  
**Description** | Add a brief explanation of the chart's purpose.  
**Table settings** | Add a label for the event variables.  
**Drill downs** | Click **Customize drill downs** to configure drill downs. For more information, see [Drill down in charts](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts#drill-down).  
  
### Pie chart

Pie charts show how a whole is divided into parts, effectively visualizing the relative size of each category within a single dataset. They represent data as slices of a circle, where each slice's size corresponds to its proportion of the whole. You can use pie charts for a quick, visual understanding of part-to-whole relationships, but limit them to datasets with few categories.

Field | Description  
---|---  
**Name** | Enter a descriptive name for the chart.  
**Description** | Add a brief explanation of the chart's purpose.  
**Field of data** | Select an appropriate event variable.  
**Value of data** | Select an appropriate event variable.  
**Donut chart** | Click the **Donut Chart** toggle to display the data in donut shape.  
**Threshold coloring** | Click the toggle to activate the threshold coloring. Threshold coloring in dashboard charts automatically adjusts the color of data elements based on numeric conditions. Enter minimum and maximum values. Select an appropriate color for the threshold. Optional: Click add**Add Threshold** to add more threshold coloring.  
**Legend** | Select where to display the chart's legend. For example, Top, Bottom, Left, Right, None.  
**Drill downs** | Click **Customize drill downs** to configure drill downs. For more information, see [Drill down in charts](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts#drill-down).  
  
### Metric chart

Metric charts provide a quick snapshot of key performance indicators by displaying a single, prominent numerical value, often accompanied by a label and optional trend indicators for context. They highlight a specific data point for immediate insight, focusing on a single value to provide a clear and concise understanding of critical metrics.

Field | Description  
---|---  
**Name** | Enter a descriptive name for the chart.  
**Description** | Add a brief explanation of the chart's purpose.  
**Metrics data type** | Select an appropriate event variable.  
**Metrics label** | Enter a descriptive name for the label.  
**Threshold coloring** | Click the toggle to activate the threshold coloring. Threshold coloring in dashboard charts automatically adjusts the color of data elements based on numeric conditions. Enter minimum and maximum values. Select an appropriate color for the threshold. Optional: Click add**Add Threshold** to add more threshold coloring.  
**Metric format** | Specifies how the metric value is displayed on the chart. **Plain text** : Displays the metric value as raw, unformatted text. **Number** : Displays the metric value as a formatted number with separators.  
**Show trend of data** | Specifies whether to display the data trend. The trend compares the current time range to the immediately preceding period of the same duration. For example, if you select a time range of `last 7 days` (August 12-18), the trend is compared to August 5-11. Similarly, for an absolute time range like May 16-20, the trend is based on May 11-15.  
**Display trend** | Displays the metric trend. **Absolute value** : Displays the actual numerical value of the metric. **Percentage** : Displays the trend value as a percentage. **Both** : Displays both the absolute value and the percentage of the trend.  
**Trend type** | Specifies the type of trend to display. **Regular** : Default. Displays increasing values in green with an up arrow, and decreasing values in red with a down arrow. **Inverse** : Displays increasing values in red with an up arrow, and decreasing values in green with a down arrow.  
**Drill downs** | Click **Customize drill downs** to configure drill downs. For more information, see [Drill down in charts](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts#drill-down).  
  
### Map chart

Map charts visualize geographic data by plotting coordinates to reveal spatial patterns and distributions. With interactive features like zooming and panning, they're ideal for displaying and analyzing location-based information.

Field | Description  
---|---  
**Name** | Enter a descriptive name for the chart.  
**Description** | Add a brief explanation of the chart's purpose.  
**Latitude** | Select an appropriate event variable.  
**Longitude** | Select an appropriate event variable.  
**Field to count** | Select an appropriate event variable.  
**Plot mode** | Select an appropriate plot mode to plot individual geographic points in terms of latitude and longitude. You can select **Heatmap** , **Points** , or **Both**.  
**Map position** | Click the toggle to fit the data. The map automatically adjusts its zoom level and center point to verify all plotted data points are visible within the current view.  
**Point settings** | Select an appropriate option to select the point size either to **Fixed** or **Proportional to size**.  
**Color** | Select an appropriate color for the point settings.  
**Drill downs** | Click **Customize drill downs** to configure drill downs. For more information, see [Drill down in charts](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts#drill-down).  
**Threshold coloring** | Click the toggle to activate the threshold coloring. Threshold coloring automatically adjusts the color of plot points and other data elements in dashboard charts based on numeric conditions. Enter minimum and maximum values. Select an appropriate color for the threshold. Optional: Click add**Add Threshold** to add more threshold coloring.  
  
### Gauge chart

Gauge charts visually represent a single value within a defined range, using dials or bars, to indicate performance or progress towards a target or threshold.

Field | Description  
---|---  
**Name** | Enter a descriptive name for the chart.  
**Description** | Add a brief explanation of the chart's purpose.  
**Field of data** | Select an appropriate event variable.  
**Gauge display value** | Select an appropriate event variable.  
**Display data values** | Click the toggle to display the data values.  
**Gauge configuration** | Enter an appropriate value for **Base value** and **Limit value**. Select an appropriate color for the **Limit value**. Click add**Add Range** to add **Threshold value**.  
  
## Drill down in charts

Drill downs let you click a specific data point or element within a dashboard chart to access more granular or related information. This action moves you from a high-level summary to a more detailed view. You can configure drill downs for all chart types except Gauge charts.

### Customize drill downs

You can configure a drill down to activate with either a left-click or a right-click on the chart element.

To customize drill downs, do the following:

  1. On the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page, click edit**Edit** on a chart.

  2. Click **Customize drill downs**.

  3. In the **Drill downs** window, in the left pane, click add**Add drill down** to create a new drill down.

  4. Under **Drill down configuration** , enter a name for the drill down.

  5. In the **Action** list, select an appropriate action for the drill down. You can select any of the following options:

     * **Run Search**

     * **Apply dashboard filter**

     * **Open external link**

  6. Configure the drill down, and then click **Done**.




#### Run search

You can customize a drill down to run a query in Search.

  1. In the **Drill downs** window, under **Drill down configuration** , enter name in the **Name** field.

  2. In the **Action** list, select **Run search**.

  3. Optional: Select the **Open in new tab** checkbox to open the search in a new tab.

  4. In the **Show fields to copy** list, select an appropriate value for which you want to configure the trigger. The values in the list are the values returned by the original search query.

  5. In the **Search** field, type a query.

  6. Select the appropriate time range.

  7. Click **Test** to test the query in [Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search).

  8. Click **Done**.




#### Open external link

You can customize a drill down to open an external link. For example, you can customize the drill down to open the threat intelligence page for a clicked IP address.

To create an external link for a trigger, do the following:

  1. In the **Drill downs** window, under **Drill down configuration** , enter name in the **Name** field.

  2. In the **Action** list, select **Open external link**.

  3. Optional: Select the **Open in new tab** checkbox to open the link in a new tab.

  4. In the **Show fields to copy** list, select an appropriate value for which you want to configure the drill down. The values in the list are the values returned by the original search query.

  5. In the **Link** field, enter a link that opens when you click the trigger.

  6. Click **Done**.




#### Apply dashboard filter

You can customize a drill down to select and edit existing filters.

**Note:** You cannot preview the filters during configuration.

To apply a dashboard filter to a trigger, do the following:

  1. In the **Drill downs** window, under **Drill down configuration** , enter name in the **Name** field.

  2. In the **Action** list, select **Apply dashboard filter**.

  3. Click add**Add filter**.

  4. In the **Filter** list, select an existing filter.

  5. Modify the filter as per your requirements.

  6. Optional: Click add**Add filter** to add more filters.

  7. Optional: Click delete**Delete** to delete a filter.

  8. Click **Done** to save the changes.




### Make a copy of drill down

To make a copy of a drill down, do the following:

  * In the **Drill downs** window, in the left pane, click the drill down you want to make a copy of, and then click content_copyDuplicate.



### Reorder a drill down

If you have multiple right-click drill downs, you can reorder them to control their display order in the context menu.

To reorder a drill down, do the following:

  * In the **Drill downs** window, in the left pane, drag a drill down to reorder.



### Delete a drill down

To delete a drill down, do the following:

  * In the **Drill downs** window, in the left pane, click the drill down you want to delete, and then click delete Delete.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
