---
url: https://docs.cloud.google.com/data-studio/table-reference/
title: Table reference \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:54.824241+00:00
---

# Table reference  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/table-reference/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Table reference Stay organized with collections  Save and categorize content based on your preferences. 

Tables display your data in a grid of rows and columns. Each column represents a dimension or metric, while each row is one record of your data.

[Learn how to add charts to your reports](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report).

## Tables in Data Studio

Tables in Data Studio automatically group your data. Each row in the table displays the unique combination of all the dimensions included in the table definition. Each metric in the table is aggregated according to the aggregation type for that metric (sum, average, count, etc.).

## Table examples

Here is some sales data for a fictional pet store. The store sells items for dogs, cats, and birds, with several products in each category.

**Date** |  **Item** |  **Category** |  **Qty Sold**  
---|---|---|---  
10/1/2016  |  Happy Cat Catnip  |  Cat  |  1   
10/1/2016  |  Healthy Dog Dog Food  |  Dog  |  3   
10/1/2016  |  Pretty Bird Bird Seed  |  Bird  |  5   
10/2/2016  |  Pretty Bird Bird Seed  |  Bird  |  3   
10/2/2016  |  Happy Cat Catnip  |  Cat  |  2   
10/3/2016  |  Playful Puppy Toy  |  Dog  |  6   
10/5/2016  |  Pretty Bird Bird Seed  |  Bird  |  7   
Data continues...  | ...  | ...  | ...   
  
A Data Studio table showing a **Category** dimension and **Qty Sold** metric looks like this:

**Category** |  **Qty Sold**  
---|---  
Bird  |  28   
Dog  |  27   
Cat  |  12   
  
Data Studio has aggregated the quantities sold per category. Since there are only 3 categories in the dataset, the table shows just 3 rows.

This is what the table looks like when an **Item** dimension is added:

**Category** |  Item  |  **Qty Sold**  
---|---|---  
Bird  |  Pretty Bird Bird Seed  |  20   
Dog  |  Healthy Dog Dog Food  |  17   
Dog  |  Playful Puppy Toy  |  10   
Bird  |  Parrot Perch  |  8   
Cat  |  Happy Cat Catnip  |  4   
Cat  |  Hungry Kitty Cat Food  |  3   
  
The table contains 6 rows, 1 for each item. The **Qty Sold** metric is now aggregated per item.

**Tip:** The metric's aggregation type depends on how the data source is configured. [Learn how to change a metric's aggregation type](https://docs.cloud.google.com/data-studio/model-your-data).

## Adjust table column size

To manually change the size of individual columns in the table, click a column divider and drag it. To resize multiple columns at once, hold the Shift key while dragging a column divider.

To apply automated column resizing, right-click the table, then select one of the **Resize columns** option:

  * **Fit to data** sizes each column in the table to the optimum width according to the data.
  * **Distribute evenly** makes all the columns equal width.

**Tip:** You can also double-click on a column divider to apply the **Fit to data** option.

## Watch a demonstration of resizing table columns

## Sort table charts

Viewers of your reports can sort the data by clicking on a column header, even if the editor has defined a different default sort order. To sort by multiple columns, click multiple column headers while holding the Shift key. If the table is sorted by multiple columns, Data Studio numbers each column in the order in which they are sorted.

To remove sorts on multiple columns, click a column header without pressing the Shift key. All sorts will be removed, and the chart will be sorted on the column that you clicked.

To reverse the sort order of a table visualization that is sorted by only one column, click the column header again. To reverse the sort order of a column in a table visualization that is sorted by two or more columns, hold the Shift key and click the column header.

If a viewer changes the sort order of a chart, and that chart was sorted by a metric that was not displayed in the chart, refreshing the page restores the default sorting.

## Limits of table charts

The number of dimensions and metrics you can add depends on the data source used by that table:

  * Tables that are based on "fixed schema" data sources, such as Google Analytics, Google Ads, Display & Video 360, and other Google marketing products' data sources, can have up to 10 dimensions and 20 metrics.
  * Tables that are based on "flexible schema" data sources, such as Google Sheets, BigQuery, and SQL databases, can have up to 100 dimensions and 100 metrics.



## Add the chart

[Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart. Then, use the **Properties** panel to configure the chart's **Setup** tab and **Style** tab properties to set up the chart data and style the chart, respectively.

## Set up the chart data

The options in the **Setup** tab of the **Properties** panel determine how the chart's data is organized and displayed.

### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit data source** icon. (You must have at least [Viewer permission](https://docs.cloud.google.com/data-studio/viewer-user-type) to see this icon.)
  * Click **Blend data** to see data from multiple data sources in the same chart. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).



### Dimension

Dimensions are data categories. Dimension values (the data that is contained by the dimension) are names, descriptions, or other characteristics of a category.

#### Drill down

This option appears on charts that support it.

Drilling down gives viewers a way to reveal additional levels of detail within a chart. When you turn on the **Drill down** switch, each dimension that you add becomes another level of detail that you can drill into. [Learn more about chart drill down](https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts).

### Metric

Metrics measure the things that are contained in dimensions and provide the numeric scale and data series for the chart.

Metrics are aggregations that come from the underlying dataset or that are the result of implicitly or explicitly applying an aggregation function, such as `COUNT()`, `SUM()`, or `AVG()`. The metric itself has no defined set of values, so you can't group by a metric as you can with a [dimension](https://docs.cloud.google.com/data-studio/dimension).

[Learn more about aggregation](https://docs.cloud.google.com/data-studio/aggregation).

#### Optional metrics

You can add [optional metrics](https://docs.cloud.google.com/data-studio/optional-metrics) by turning on the **Optional metrics** switch and selecting metrics from the **Add metric** field selector. You can also click metrics from the fields list on the **Data** panel and place them in the **Optional metrics** selector.

### Filter

Filters restrict the data that is displayed in the component by including or excluding the values that you specify. [Learn more about the filter property](https://docs.cloud.google.com/data-studio/about-filter-properties).

Filter options include the following:

  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it.
  * **Add filter:** Click this option to create a new filter for the chart.



### Date range dimension

This option appears if your data source has a valid date dimension.

**Important:** This option does not appear for Google Ads or Google Analytics data sources, as these automatically select a dimension of type **Date** from the data source.

The date range dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the timeframe.

### Default date range filter

The default date range filter lets you set a timeframe for an individual chart.

Default date range filter options include the following:

  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.
  * **Comparison date range:** Displays comparison data for the selected time period.



[Learn more about working with dates and time](https://docs.cloud.google.com/data-studio/dates-and-times).

### Number of rows

Use the settings in the **Number of rows** section to customize the appearance and number of rows that are displayed in your table chart. **Number of rows** settings include **Pagination** and **Top N.**

When selected, the **Pagination** setting separates large table results into multiple pages on the table chart. You can customize how the page navigation is displayed to users with the **Table Footer** options in the **Style** tab.

Use the **Per page** option to control how many table rows to display per table page.

When selected, the **Top N** setting lets you specify the number of rows to display in the table chart. You can specify the number of rows to display in the **Top rows** field.

When you enable the **Top N** setting, you can also turn on the **Group others** switch to aggregate the results that are outside of the specified row limit into one row that will be labeled **Others**. When enabled, **Group others** lets you compare the top N results against the context of the remaining results.

Keep the following considerations in mind when using the **Number of rows** settings:

  * The **Pagination** setting is enabled by default. If you select the **Top N** setting, **Pagination** is disabled.
  * When **Group others** is not enabled, depending on the chart's configuration, the chart may not display all the data.
  * The **Group others** option is not compatible with [comparison metrics](https://docs.cloud.google.com/data-studio/add-comparison-metrics-and-running-totals#differences_between_running_calculations_and_calculated_fields). To use comparison metrics, disable the **Group others** option.



#### Show summary row

When enabled, the **Show summary row** option displays a row at the bottom of a table that summarizes each metric column.

#### Ignore canvas filters in summary row

When the **Ignore canvas filters in summary row** option is enabled, the summary row displays a complete total, ignoring any viewer-applied filters, such as [controls](https://docs.cloud.google.com/data-studio/about-controls). The total row still includes [filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties).

### Sort

The **Sort** and **Secondary sort** options in the chart's setup panel control the default sorting behavior. You can select any metric or dimension that is in the chart's data source, or that is displayed in the chart, to use as the primary or secondary sorting field.

Click **Add sort** to add up to 10 sorting fields.

**Note:** Sorting by a field that is not selected in the table chart may be confusing for chart viewers.

The **Secondary sort** option only appears when there is an appropriate combination of dimensions and metrics in the chart.

**Tip:** When you specify a metric as a sort field, you can [edit the field's aggregation](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports). For example, you could include a numeric field in the chart as a SUM, but sort on that same field's AVERAGE value.

### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

When the **Open links in new tab** option is enabled on a chart, [hyperlinks that are included in the data](https://docs.cloud.google.com/data-studio/hyperlinks-in-data) will open in a new tab. When the **Open links in new tab** option is _not_ enabled, hyperlinks that are included in the data will open in the same tab.

## Style the chart

The options in the **Style** tab control the overall presentation and appearance of the chart.

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

### Chart title

Turn on the **Show title** switch to add a title to your chart. Data Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.

#### Autogenerate

This option is enabled by default. When **Autogenerate** is enabled, Data Studio generates a title that is based on the chart type and the fields that are used in the chart. The autogenerated title will be updated if you change the chart type or make changes to the fields that are used in the chart.

To add a custom title to your chart, enter it into the **Title** field. This will turn off the **Autogenerate** setting.

#### Title options

When the **Show title** setting is enabled, you can use the following title options:

  * **Title:** Provides a text field where report editors can enter a custom title for the chart.
  * **Font family:** Sets the font type for the title text.
  * **Font size:** Sets the font size for the title text.
  * **Font color:** Sets the font color for the title text.
  * **Font styling options:** Applies bold, italic, or underline styling to the title text.
  * **Top:** Positions the chart title at the top of the chart.
  * **Bottom:** Positions the chart title at the bottom of the chart.
  * **Left:** Aligns the chart title to the left side of the chart.
  * **Center:** Centers the chart title horizontally.
  * **Right:** Aligns the chart title to the right side of the chart.



### Conditional formatting

Click **Add conditional formatting** to apply conditional formatting rules to the chart. [Learn more about conditional formatting in Data Studio charts](https://docs.cloud.google.com/data-studio/use-conditional-formatting-rules).

### Table style

These options control the orientation and header of the table:

  * **Display:** Sets the orientation of the table. By default, the table position is set to ![](https://docs.cloud.google.com/static/data-studio/images/vertical-table.png)**Vertical**. To transpose the table, click the ![](https://docs.cloud.google.com/static/data-studio/images/horizontal-table.png)**Horizontal** button.
  * **Show header:** Shows or hides the table header. Note that viewers can't sort tables with hidden headers.
  * **Font family:** Sets the font family of the table header. This option appears when the **Show header** setting is enabled.
  * **Font size:** Sets the font size of the table header. This option appears when the **Show header** setting is enabled.
  * **Font color:** Sets the font color of the table header. This option appears when the **Show header** setting is enabled.
  * **Wrap text:** Wraps the header text. This option appears when the **Show header** setting is enabled.
  * **Show field descriptions:** Inserts an ![The info icon.](https://docs.cloud.google.com/static/data-studio/images/info-icon.png) info icon in column headers that displays the description for each field in a tooltip. Viewers can put their cursor over the info icon to view the field description. Field descriptions are sourced from the [**Description** column](https://docs.cloud.google.com/data-studio/edit-a-data-source) in the data source. This option appears when the **Show header** setting is enabled.

**Important:** **Show field descriptions** is automatically enabled for charts that are connected to a [Looker](https://docs.cloud.google.com/data-studio/connect-to-looker) or [Search Ads 360](https://docs.cloud.google.com/data-studio/connect-to-search-ads-360-deprecated) data source.



#### Table labels

These options control the appearance of the table data:

  * **Font family:** Sets the font family of the data.
  * **Font size:** Sets the font size of the data.
  * **Font color:** Sets the font color of the data.
  * **Summary row label:** Sets the label for the summary row. This option appears if you have enabled **Show summary row**.



#### Table colors

These options control the colors of the table borders and cells:

  * **Header background color:** Sets the color of the table header background.
  * **Cell border color:** Sets the color of the border between rows.



#### Table body

These options control the appearance of the table body:

  * **Row numbers:** Adds row numbering as the leftmost column of the table.
  * **Auto-height:** Resizes row height to fit the content.
  * **Wrap text:** Wraps long text in the table body.
  * **Horizontal scrolling:** Adds a horizontal scrollbar to the bottom of the table.

**Note:** When Horizontal scrolling is enabled, users can freeze columns while viewing the report.
  * **Freeze all columns up to:** Freeze all columns up to the selected column number.

**Important:** Freezing columns is unavailable when the table is transposed.
  * **Tooltip position:** Determines where a tooltip will appear relative to the table chart.

  * **Missing Data:** This option controls how to display missing values. For example, when data is missing from the table, you can choose to show blanks, hyphens, or the words "no data."

  * **Heatmap text contrast:** Sets the font color automatically when displaying a heatmap. Choose from four levels of contrast: **None** , **Low** , **Medium** , or **High**.




#### Table Footer

These options control the appearance of the table footer:

  * **Footer border color:** Sets the footer border color.
  * **Footer border weight:** Sets the thickness of the footer border.
  * **Footer border style:** Sets the line style of the footer border.
  * **Compact pagination:** Reduces the vertical spacing of the pagination controls.



### Dimensions

Use the **Select dimension** drop-down menu to select a specific dimension to customize, or select **All dimensions** to apply changes to all dimensions at once. Note that this option appears only if you have added more than one dimension to the table.

Styles set for an individual dimension will override styles set for **All dimensions**.

If a setting has different values for different dimensions, then selecting **All dimensions** will indicate that there are multiple values for that setting. The style panel will either display a mixed toggle state, or the word **Mixed** for settings with a text value.

This setting specifies the alignment of dimension text in table columns.

### Metrics

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

Use the **Select metric** drop-down menu to select a specific metric to customize, or select **All metrics** to apply changes to all metrics at once. Note that this option appears only if you have added more than one metric to the table.

Styles set for an individual metric will override styles set for **All metrics**.

If a setting has different values for different metrics, then selecting **All metrics** will indicate that there are multiple values for that setting. The style panel will either display a mixed toggle state, or the word **Mixed** for settings with a text value.

These options control the display of metric columns:

  * **Drop-down menu options:**

    * **Number:** Displays the metric value "as is."
    * **Heatmap:** Displays the metric value with a colored background, the intensity of which shows how that value compares to the other values in that column.

Use the **Heatmap text contrast** option (in the **Table body** section) to set the font color automatically to provide better readability of your data labels. Choose from four levels of contrast: **None** , **Low** , **Medium** , or **High**.

    * **Bar:** Displays the metric value as a horizontal bar. You can change the bar color and include the numeric value.

  * **Alignment:** Aligns the data in the column left, right, or center. This setting appears when **Number** is selected.

  * **Column Color:** Sets the color of the bar or the heatmap. This setting appears when the column type is set to **Bar** or **Heatmap**. 

  * **Compact numbers:** Rounds numbers and displays the unit indicator. For example, 553,939 becomes 553.9K. This setting appears in this position when the column type is **Number** or **Heatmap**.

  * **Decimal precision:** Sets the number of decimal places in metric values.

  * **Show number:** Shows the number of the metric value. This setting appears when the column type is set to **Bar**. When enabled, this setting reveals **Compact numbers** and **Decimal precision** styling options for displaying the number.

  * **Show target:** Shows a target line for the value that is set in the **Target value** field, similar to a bullet chart. This setting appears when the column type is set to **Bar**. When enabled, this setting reveals a **Target value** field to specify the target value, and a **Target color** option to set the color of the target line.

  * **Show axis:** Displays an X-axis for the bar chart. This setting appears when the column type is set to **Bar**. When enabled, this setting reveals **Axis font family** , **Axis font color** , **Axis compact numbers** , and **Axis decimal precision** settings for styling the bar axis and axis values.




### Background and border

These options control the appearance of the chart background container:

  * **Background:** Sets the chart background color.
  * **Opacity:** Sets the chart opacity. 100% opacity completely hides objects behind the chart. 0% opacity makes the chart invisible.
  * **Border color:** Sets the chart border color.
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the chart border line thickness.
  * **Border style:** Sets the chart border line style.
  * **Add border shadow:** Adds a shadow to the chart's lower and right borders.



### Chart header

The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. Chart header options include the following:

  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Header font color:** Sets the color of the chart header options.



### Reset to report theme

Click **Reset to report theme** to reset the chart settings to the report theme settings.

## Related resources

  * [Types of charts in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts)
  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [About filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
