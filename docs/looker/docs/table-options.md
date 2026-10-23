---
url: https://docs.cloud.google.com/looker/docs/table-options/
title: Table chart options \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:27.044952+00:00
---

# Table chart options  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/table-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Table chart options Stay organized with collections  Save and categorize content based on your preferences. 

You can customize table charts in Looker using formatting, conditional styling, and display options to control how your data appears. This helps you present data in a way that meets your analytical requirements.

## Building a table chart

Table charts accept dimensions, measures, pivots, subtotals, table calculations, custom fields, and row or column totals. Table charts support up to 5,000 rows and up to 200 pivoted columns.

To use a table chart, [run your query](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#explores_are_the_starting_point_for_exploration) and select the table icon on the **Visualization** bar.

To edit your table visualization, select **Edit** in the upper right corner of the **Visualization** bar.

The options listed next may be grayed out or hidden when incompatible with the composition of your table or if they conflict with other settings you have chosen.

## Data bar options

Several options on the **Data** bar can affect both your visualization and the data table.

### Subtotals

The option to add subtotals to your table visualization appears on the **Data** bar when your data table contains at least two dimensions. Select the **Subtotals** checkbox and press **Run**. Subtotals appear only in the table visualization. They do not appear in the data table.

The following image shows a table visualization of **Users State** , **Users City** , **Users Zip** , and **Orders Count** with subtotals enabled. In the visualization, the **Orders Count** field shows the count for each zip code and the subtotals for each city and state. When a city contains multiple zip codes, the counts for all of the city's zip codes are added together to get the city's count. The state count is the sum of all the zip code counts in the state.

![](https://docs.cloud.google.com/static/looker/docs/images/vis-table-next-subtotals-box-2608.png)

Subtotals are calculated for all dimensions other than the rightmost dimension. To change the dimensions that are subtotaled, reorder the positions of the dimensions in your data table.

There are some things to keep in mind about how subtotals work:

  * If the same item appears in several categories, subtotals that count unique items might not add up as you expect. In those cases, Looker counts each item once rather than counting every duplicate appearance. Looker calculates column totals in the same way.
  * Subtotals of [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) that perform aggregations, such as calculations using `percentile` or `mean`, might not add up as you expect. This is because table calculations calculate subtotals using the other subtotal values, not using the values in the data column. For example, if you have two **User Count** subtotals of 30,500 and 24,312 and you have a table calculation such as `mean(${users.count})`, the table calculation will return 27,406 for both subtotal rows because it is performing the calculation `(30500 + 24312)/2`.
  * Subtotals are not available when you filter on a measure or when the Explore uses the [`sql_always_having` parameter](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-having).
  * If your data table row limit cuts off your data table partway through a subtotal category, the entire category will be hidden from the table visualization.
  * Sorting occurs within each subtotal category independently.
  * The leftmost subtotal is always sorted. When you sort by multiple columns, subtotal columns are given precedence.
  * If you change the order of your dimensions by dragging and dropping them in the Data section of the Explore, you may need to unselect and reselect the **Subtotals** checkbox.



Subtotals can be collapsed or expanded in the table visualization. See the Collapse Subtotal section for more information.

#### Dialect support for subtotals

The ability to use subtotals depends on the database dialect that your Looker connection is using. In the latest release of Looker, the following dialects support subtotals:

#### Click here to display the table.

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
There are some things to keep in mind about dialect support for subtotals:

  * When you use MySQL, all subtotals must sort ascending.
  * Pivots in MySQL and Snowflake will fail if you are using subtotals and the underlying result set contains more than 30,000 rows (regardless of any row limits you set in the data table).
  * Using subtotals with BigQuery and Redshift may decrease query speeds compared to queries without subtotals.



### Row Totals

If your chart contains [pivots](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions), you can add row totals to your chart by selecting the **Row Totals** checkbox in the **Data** bar. See the [Exploring data in Looker](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals) documentation page for more information, including information on [when totals aren't available](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#when_totals_arent_available) and [things to consider with totals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#things_to_consider_with_totals).

The arrow to the right of the **Row Totals** checkbox lets you toggle the placement of the totals column between the far right default placement and a placement further to the left, after dimensions and dimension table calculations.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-new-table-row-totals-2300.png)

### Totals

You can add column totals for measures and table calculations by selecting **Totals** in the **Data** bar. See the [Exploring data in Looker](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals) documentation page for more information, including information on [when totals aren't available](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#when_totals_arent_available) and [things to consider with totals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#things_to_consider_with_totals).

![](https://docs.cloud.google.com/static/looker/docs/images/explore-new-table-totals-2300.png)

### Column Limit

If your data table contains [pivots](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions), you can add a column limit to your chart by entering any number between 1 and 200 in the **Column Limit** box. Dimensions, dimension table calculations, row total columns, and measure table calculations outside of pivots are not counted toward the column limit. Pivoted groups each count as one column toward the column limit. See the [Filtering and limiting data](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#limiting_data) documentation page for more information.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-new-table-column-limit-2308.png)

### Row Limit

You can add a row limit to your chart by entering any number between 1 and 5,000 into the **Row Limit** box on the **Data** tab. If your query exceeds the row limit you have set, you cannot sort row total or table calculation columns.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-new-table-row-limit-2300.png)

When you add a table chart to a [dashboard](https://docs.cloud.google.com/looker/docs/viewing-dashboards), if the **Row Limit** is left blank, the dashboard imposes a limit of 1,000 rows to the table chart tile. To increase the row limit on a dashboard tile, enter a higher row limit up to 5,000, which is the maximum number of rows that can be presented.

### Calculations

If you have the appropriate permissions, you can add table calculations to your chart by clicking the **Add calculation** button on the **Data** tab. See the [Using table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) documentation page for more information.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-table-calc-button-2218.png)

You can also use the [**Custom Fields** section of the field picker](https://docs.cloud.google.com/looker/docs/table-calculations#creating_table_calculations_in_looker).

## Column menu options

> When column menu options are accessed through a dashboard tile in view mode, changes to settings are not saved. To save changes to settings, enter [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards) on the dashboard, [select **Edit** in the tile's three-dot **Tile actions** menu](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_a_tiles_query_or_look), and change the settings in the edit window that appears.

Table charts have a three-dot **Column Options** icon at the upper right of each column, which appears when you hover over the column header.

![](https://docs.cloud.google.com/static/looker/docs/images/vis-table-column-kabob-2308.png)

Selecting the **Column Options** icon reveals a column menu that provides options for freezing, copying, and resizing table columns as you view them.

![](https://docs.cloud.google.com/static/looker/docs/images/vis-table-column-menu-2112.png)

### Freeze

Selecting the **Freeze** option freezes a table column to the left side of the chart. The frozen column remains visible on the left side during horizontal scrolling. Multiple columns can be frozen. The first time you freeze a column, the row number column will also freeze, if it exists. When you unfreeze the last frozen column, the row number column will also unfreeze, if it exists.

When one or more columns are frozen, a vertical separator line appears between frozen and unfrozen columns.

To unfreeze a column, select the three-dot icon again and select **Unfreeze**.

### Copy Values

Select **Copy Values** to copy the column header and all the values in the column, which you can then paste into a spreadsheet, text file, or Looker filter. You can also select a cell or a range of cells within the visualization and copy the contents using the keyboard shortcuts Command-C (Mac) or Ctrl+C (Windows).

### Autosize All Columns

Selecting **Autosize All Columns** sizes the width of each column to fit its column heading name or its longest data value, whichever is wider.

### Reset All Column Widths

Selecting **Reset All Column Widths** resizes each column to its default width, which is the width that is set when **Size Columns to Fit** is turned on, or the width that is set by **Autosize All Columns** if sizing columns to fit makes columns too narrow.

## Sorting columns

The default sort order is explained on the [Exploring data in Looker](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#sorting_data) documentation page.

You can sort columns in the table visualization by selecting column headers within the visualization. Each time you select a header, its column switches between ascending and descending sort order. A chevron appears in the column header to indicate that the chart is sorted by that column. The chevron points up to indicate an ascending sort and down to indicate a descending sort.

You can sort by multiple columns by holding down the Shift key and then selecting the column headers in the order you would like them sorted.

If subtotals are enabled, the leftmost subtotal is always sorted. Sorting occurs within each subtotal category independently.

If you reach a row limit, you will not be able to sort row totals or [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations#cannot-sort).

## Manually moving and pinning columns

> When columns are rearranged through a dashboard tile in view mode, changes to the column order are not saved. To save changes to column order, enter [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards) on the dashboard, [select **Edit** in the tile's three-dot menu](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_a_tiles_query_or_look), and move the columns in the edit window that appears.

Selecting and dragging column headers in the table visualization lets you move any column, including pivot groups and individual pivot columns, to any other location in the visualization. The order of the columns within the **Data** table will not change.

While you are selecting and dragging a column, if you approach the left edge of the visualization, a pin icon will appear.

![Pin icon appears when dragging a column to the left edge of a table visualization.](https://docs.cloud.google.com/static/looker/docs/images/vis-table-next-pin-icon-2608.png)

If you drop the column while the pin icon is present, the column will be pinned to the side of your visualization. The pinned column remains visible on the side during horizontal scrolling. Multiple columns can be pinned.

If you drag a column outside of the bounds of the visualization, an icon of a crossed-out eye will appear.

![](https://docs.cloud.google.com/static/looker/docs/images/vis-table-next-eye-icon-2608.png)

If you drop the column while the eye icon is present, the column will not move from its original position.

When you download a table with columns that have been rearranged, the columns will appear in their original order (the order in which they appear in the data table) even if the [**With visualization options applied**](https://docs.cloud.google.com/looker/docs/downloading#results) setting is selected.

## Manually resizing columns

To manually resize columns, select the right border of the column header and drag it left or right.

Manually resizing columns overrides **Size Columns to Fit**.

## Plot menu options

### Table Theme

The default theme for table visualizations is **White**. You can change the theme with the **Table Theme** setting.

You can choose table coloring options:

  * **Classic** : The table appears as it does in the Data section, with blue dimensions, orange measures, and green table calculations.
  * **White** : The table header is white, the data rows alternate between white and gray, and the text is black.
  * **Gray** : The table header is gray, the data rows alternate between white and light gray, and the text is dark gray.
  * **Transparent** : The table header is totally transparent, the data rows alternate between totally transparent and translucent gray, and the text adjusts itself in color. This can be useful when using a customized, embedded dashboard so that the tile background color shows through the visualization. On such a dashboard, the text color adapts to the background color, changing from black to white as needed. On the Explore page or in an embedded Look, the background is always white under the transparent visualization.
  * **Unstyled** : The entire table is white, the data rows are separated by gray lines, and the text is black.



### Show Row Numbers

You can toggle whether to show a row number at the beginning of each table row.

**Show Row Numbers** is disabled when you use subtotals in your table chart.

### Show Totals

**Show Totals** toggles whether to show column totals at the bottom of each table column.

**Show Totals** is disabled when [**Totals**](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals) are not added to your table chart.

### Show Row Totals

**Show Row Totals** toggles whether to show row totals at the beginning or end of each table row.

**Show Row Totals** is disabled when [**Row Totals**](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals) are not added to your pivoted table chart.

### Transpose

The **Transpose** option is available for visualizations that contain only one dimension. When **Transpose** is selected, the visualization's rows will switch to columns and the columns will switch to rows.

![](https://docs.cloud.google.com/static/looker/docs/images/vis-table-next-transpose-2608.png)

### Limit Displayed Rows

You can show or hide rows in a visualization, based on their position in the results. For example, if your visualization displays a seven-day rolling average, you may want to hide the first six rows.

Click **Limit Displayed Rows** to enable or disable this feature. When this feature is enabled, you can specify the following options:

  * **Hide** or **Show** : Choose **Hide** to exclude certain rows from the visualization. Choose **Show** to display only a limited number of rows in the visualization.
  * **First** or **Last** : Choose if the rows to hide or show are the first or last rows in the result set.
  * **Number** : Specify the number of rows to hide or show.



In the Data section of the Look or Explore, excluded rows are shaded in a darker color.

![](https://docs.cloud.google.com/static/looker/docs/images/limit-displayed-rows-2106.png)

This option is dependent on the row order. Changing the query's sort order or adding a row limit can change the rows that are shown or hidden in the visualization.

### Pagination

For tables that contain 50 or more rows, you can enable pagination to display table rows in a series of pages at the bottom of the visualization.

To enable pagination, select the **Paginate Rows** checkbox.

When pagination is enabled, you can use the **Rows Per Page** setting to specify the number of rows to display per page. You can select 50, 100, 250, 500, or 1,000 rows per page.

When pagination is enabled for a table visualization on a dashboard, you must enter dashboard [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards) to change the rows per page setting.

## Grouping menu options

**Note:** The **Grouping** menu is part of the [**Table Row Grouping** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#table-row-grouping), and is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

We encourage you to share your feedback to help us improve. To report bugs or issues, send an email to [`looker-viz-preview-external@google.com`](mailto:looker-viz-preview-external@google.com) with the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



By default, table charts display the data for each field in individual columns. When the **Table Row Grouping** preview feature is enabled, you can group rows of data from multiple dimensions into one column. Grouping dimensions hierarchically into one column can make tables more organized and help users understand how data is related. You can expand and collapse data to focus on specific data points, and hide the granular details that you don't want to see.

For example, you can group granular date fields, such as **Orders Created Year** , **Orders Created Quarter** , and **Orders Created Month** in a single column, along with other information such as **Orders Status** and **Orders Average Order Profit** , to provide multiple ways for users to drill into the data in the table chart. Users can see the summary of the data in the top-level rows, and expand rows for more granular insights about orders placed within specific months in a quarter.

![The top-level rows in a grouped column display the years 2026 and 2023, and subsequent expanded rows that provide a breakdown by quarter of order statuses and average profit for each month in the quarter.](https://docs.cloud.google.com/static/looker/docs/images/table-row-grouping-2612.png)

Click the **Enable Row Groups** switch to group dimensions in table charts. When **Enable Row Groups** is enabled, the settings in the **Grouping** menu will appear. These settings let you control the appearance of hierarchical data in the table chart.

**Note:** When you download or schedule a dashboard as a PDF with the [**Expand tables to show all rows**](https://docs.cloud.google.com/looker/docs/downloading#downloading_a_dashboard_as_a_pdf) option selected, table charts with row grouping enabled download as flat data, and the grouping column expands to display all columns.

### Add Fields

The **Add Fields** button lets you choose which dimensions to group. Click the **Add Fields** button to open the **Fields** menu, and then click the checkbox next to each dimension that you want to include in the group.

The order in which the dimensions are selected determines the hierarchy of the group. For example, if you check the box next to a dimension called **Country** , and then check the box next to a dimension called **State** , **Country** will be the dimension at the top of the hierarchy, and the value of the **State** dimension will appear in a separate row underneath the value of the **Country** dimension in the group.

To change the order of a dimension in the group, click and hold the cursor on a dimension's drag_handle drag handle, and move the dimension into a new position in the hierarchy list.

### Default Display Level

You can use the settings in the **Default Display Level** field to set how the values in a group are displayed when you first view the table chart. The options include the following:

  * **All Collapsed** : All hierarchy levels are collapsed.
  * **Top Level Expanded** : The top hierarchy level is expanded, and all other levels are collapsed.
  * **All Expanded** : All of the hierarchy levels are expanded.



Click the arrows next to each row to expand or collapse the levels in a group. Alternatively, click the arrow next to the group column header name to expand or collapse all the levels in a group, or click the group column header name to sort the data.

### Group Column header

By default, the name of the group column is **Group**. Optionally, input a different name for the group column in the **Group Column Header** text field.

Click the arrow next to the group column header to expand or collapse all the levels in a group. Click the group column header name to sort the data.

### Show Group Counts

Click the switch to enable or disable the **Show Group Counts** setting.

When enabled, the **Show Group Counts** setting displays the number of rows that are collapsed in a group in parentheses next to a value in the displayed row. For example, if five rows are hidden under the expanded row value **2026** , the number of hidden rows will be indicated like **2026 (5)**.

### Show Subtotals

Click the switch to enable or disable the **Show Subtotals** setting.

**Caution:** Don't use the **Show Subtotals** setting for non-additive calculations such as averages, percentiles, or relative change. Instead, use the SQL **Subtotals** option in the **Data** pane. Subtotals for table row grouping only support aggregates such as `sum` and `count`.

When enabled, the **Show Subtotals** setting displays the subtotal of numeric data for rows that are collapsed in a group. The subtotal will appear in the numeric field column (for example, in the **Total** column, if there is a measure called **Total** in an Explore) in the top row of each group. Displaying the subtotals for each group provides users with a snapshot or summary of the underlying data.

## Series menu options

The series menu controls how your chart shows each [data series](https://docs.cloud.google.com/looker/docs/creating-visualizations#series-def).

In a table chart, each column is listed in the series menu for customization.

### Truncate Text

When **Truncate Text** is turned on, the text that appears in data cells will be truncated and followed by ellipses. When it is turned off, text inside data cells wraps to subsequent lines.

To view the full version of truncated or wrapped text inside a data cell, double-click the interior of the cell; press Escape or click outside of the cell to return to the truncated or wrapped version.

The default setting for **Truncate Text** is **on**.

### Truncate Column Names

When **Truncate Column Names** is turned on, the text that appears in column headers will be truncated. When it is turned off, text inside column headers wraps to subsequent lines.

To view the full text of a truncated or wrapped column header, hover over the column header. A tooltip will appear with the full text of the column header.

The default setting for **Truncate Column Names** is **off**.

### Show Full Field Name

You can toggle whether to show the view name along with the field name for each column header. When **Show Full Field Name** is off, generally only the field name shows; however, measures of type `count` display only the view name instead.

### Size Columns to Fit

**Size Columns to Fit** sizes the widths of all columns so that the table perfectly fits the width of the pane in which you are viewing it. When this option is toggled **on** , columns can still be manually re-sized, and the manually set widths will override the widths set by **Size Columns to Fit**. Widths set using the **Size Columns to Fit** option are saved when you save your visualization as a Look or add it to a dashboard.

The default setting for **Size Columns to Fit** is **on**. However, if **Size Columns to Fit** results in columns that are too narrow to be readable, Looker will automatically autosize all columns and will size each column based on its longest data value.

### Minimum Column Width

Enter a number to set the minimum column width in pixels for every column in the table visualization. The default minimum column width is 100 pixels. This setting is useful, for example, if you have a table with a large number of columns and you want to create a PDF of the table visualization that does not cut off any table columns. In that case, you could reduce the minimum column width to ensure that all columns are included.

### Customizations

The **Customizations** section lets you customize each column, or _series_ , in the table chart. Click the arrow next to a series to expand its options.

#### Label

You can create a custom label for the column that will appear in the visualization.

#### Width

You can set the width of the column by entering a number from 1 (narrowest) through 1,000 (widest). Widths set using the **Width** field are saved when you save your visualization as a Look or add it to a dashboard.

#### Format

The **Format** option appears for columns that contain numeric data. Using the drop-down menu, you can choose a predefined format or create a custom format for the values in that column. If you choose **Custom** from the drop-down, use Excel-style formatting to create your custom format. Excel-style formatting is described on the [Adding custom formatting to numeric fields](https://docs.cloud.google.com/looker/docs/custom-formatting) documentation page.

#### Cell Text Layout

![](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-table-next-series-formatting-2308.png)

The formatting icons let you apply styling to the data cells for that column, including the following styles:

  * Font style, size, and color
  * Background fill color
  * Bold, italic, or underline font formatting
  * Horizontal alignment



These settings override any formatting options that are applied in the **Row and header formatting** options.

Customizing cell text layout is not available when the **Cell Visualization** option is set to **on**.

Column headers can be styled using the formatting menu.

#### Collapse Subtotal

The **Collapse Subtotal** option appears for columns that have subtotals. Enabling this option will collapse all subtotals for that column. The subtotals will remain collapsed when you save your visualization as a Look or add it to a dashboard.

You can collapse subtotals on individual cells by selecting the arrow on the left side of the cell, but those changes are not saved.

#### Cell Visualization

The **Cell Visualization** option appears for columns that contain numeric data. When this option is turned on, horizontal bar visualizations appear in the column cells, representing the value of the data in each cell. The bar length is plotted from zero (in which case no bar appears) to the maximum data value.

**Note:** In tables with cell visualizations that include both positive and negative values in a column, if the column is too narrow to show the full range of values, the cell contents shift to avoid being cut off.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-table-next-bars-option-2608.png)

A color palette appears when the **Cell Visualization** option is enabled. The default color palette for the bar visualizations comes from the [color collection](https://docs.cloud.google.com/looker/docs/color-collections) selected in the **Collection** menu option. Selecting the palette lets you select a different palette from the collection or create a custom palette by selecting the **Custom** tab on the palette picker that appears. The bar colors reflect the data values from the minimum (left side of the palette) to the maximum (right side of the palette).

The **Value Labels** checkbox also appears when the **Cell Visualization** option is enabled. This checkbox toggles the appearance of value labels for each data point on a chart. The value labels appear to the right of the bar visualizations for columns with only positive values or only negative values. For columns with both positive and negative values, value labels appear to the right of the bar visualizations for negative values and to the left of the bar visualizations for positive values. **Value Labels** defaults to **on**.

If a column is pivoted by another series, bar visualizations are plotted for that column in each pivot group; and the minimum and maximum values are shared across the pivoted columns. If a series is used to pivot columns, bar visualizations are not available for that series, even if it contains numeric data.

The **Cell Visualization** option defaults to **on** for the first measure in the table visualization. For other columns with numeric data, it defaults to **off**.

#### Custom Tooltip

You can click the **Custom Tooltip** switch to configure tooltips within the [Explore visualization editor](https://docs.cloud.google.com/looker/docs/creating-visualizations#quick_guide) by using a combination of UI settings and an HTML editor that supports Liquid templating. [Learn more about **Custom Tooltips**](https://docs.cloud.google.com/looker/docs/custom-tooltips).

## Formatting menu options

### Color collection

Choosing a color collection from the **Collection** drop-down menu determines the palettes available for [conditional formatting rules](https://docs.cloud.google.com/looker/docs/table-options#defining_formatting_rules) or [cell visualizations](https://docs.cloud.google.com/looker/docs/table-options#bars).

A color collection lets you create themed visualizations and dashboards that look good together. You can see all the palettes in each of Looker's built-in color collections on the [Color collections](https://docs.cloud.google.com/looker/docs/color-collections) documentation page. Your Looker admin may also create a custom color collection for your organization.

The palettes for any cell visualizations and the **Palette** section for each conditional formatting rule update with a palette from that collection.

### Row and header formatting

**Rows** let you set the font size for cell text between 1 and 99 points. 

**Header** lets you set the font size, text color, background fill color, and horizontal alignment for column headers. Header font size can range between 1 and 99 points.

#### Show Headers

Click the **Show Headers** switch to show or hide table headers.

#### Borders

Click the **Borders** switch to show or hide table borders. You can also customize border settings, including border width in pixels, border color, and border style (solid, dotted, or dashed).

### Cell Highlighting

Click the **Cell Highlighting** switch to enable row and column highlighting when you hover over a cell in the table. You can also use the **Highlight Color** color picker to select a custom color for cell highlighting.

**Note:** When **Cell Highlighting** is enabled, conditional formatting is not available.

### Enable conditional formatting

You can apply conditional formatting to columns in a table visualization when subtotals are not present and the **Cell Visualization** feature is set to **off** for those columns. Turn on **Enable Conditional Formatting** to define rules that color code your table, either on a scale or by specifying values that are of interest.

**Note:** When [Cell Highlighting](https://docs.cloud.google.com/looker/docs/table-options#cell_highlighting) is enabled, conditional formatting is not available.

For example, you can color all values on a scale from red to yellow to green as the values scale from low to medium to high.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-table-next-conditional-formatting-scale-622.png)

You could also format all values over 5,000 with a yellow cell background and bold text.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-table-next-conditional-formatting-values-622.png)

#### Defining formatting rules

You specify how to color code your visualization in the **Rules** section.

When you first enable conditional formatting, there will be one rule, set to the default of color coding on a scale. Conditional formatting is supported on both numeric and non-numeric (string) fields, and rules can be applied to both dimensions and measures.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-conditional-formatting-rules-2608.png)

  1. To rearrange rules, click and hold on the icon with the three parallel lines and drag the rule up or down.
  2. To delete a rule, click the trash can icon in the top right corner of that rule section.
  3. To add an additional rule, click **Add Rule**.

**Note:** You can define a maximum of three rules for conditional formatting.



You can apply the rule to all numeric fields in the visualization, or apply the rule to one or more fields using the **Apply to** box.

![The Apply to box has two fields: a drop-down field for choosing a field from a list and a search field to search for the field you want.](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-conditional-formatting-select-fields-2308.png)

  * If you choose **All numeric fields** , the conditional formatting rule is applied to every value in all the numeric fields in the visualization. If you are color coding values on a scale, the scale will include all numeric values, even if the values in different columns are unrelated.

If you create multiple rules using **All numeric fields** , the rules higher on the list have precedence over rules lower on the list. To change the precedence of a rule, click on the three horizontal bars at the top left of that rule and drag the rule higher or lower in the list.

  * If you choose **Select fields** , Looker displays a box that lets you select the fields where you want to apply the rule. If you enter text in the box, Looker lists only the fields that include that text.

Select the field or fields to apply the rule. The conditional formatting will be applied only to the values in those fields.

If you create multiple rules on the same field, only the rule highest on the list applies to the visualization and the other rules are inactive. To move a rule higher or lower on the list, click on the three horizontal bars at the top left of that rule and drag the rule higher or lower in the list.




In the **Format** box, choose whether to color code values along a scale or based on a logical condition.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-conditional-formatting-format-64.png)

If you format based on a logical condition, when you enter a value in the **Format** box, do not use thousands separators.

#### Color coding on a scale

If you are color coding values on a scale, click the color palette. Color coding on a scale can be applied only to numeric fields.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-conditional-formatting-rule-scale-2308.png)

Choose an existing palette or create a custom palette by clicking on the **Custom** tab of the palette picker:

  * To add or remove colors from the scale, click the **+** or **-** buttons. You can have a maximum of 5 and a minimum of 2 colors on your scale.
  * To edit all colors of the scale, click **Edit All** and enter RGB [hex strings](https://www.w3schools.com/colors/colors_hexadecimal.asp), such as `#2ca6cd`, or [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`.
  * To choose a custom color for the highlighted part of your color scale, use the color wheel.



![](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-conditional-formatting-colors-62.png)

Use the following options to modify the color coding:

  * Select **Reverse colors** to apply the colors at the left end of the palette to values in the higher end of the data range and colors at the right end of the palette to values in the lower end of the data range.
  * Select **Use X color steps** to limit the number of colors used to the specified step value. When this option is not enabled, the data is colored on a gradient covering the entire palette spectrum. When this option is enabled, the data is then grouped and colored according to the number of color steps. For example, if you specify 5 color steps, the data is grouped into 5 equal buckets and the 5 colors applied, one color to each bucket of data. Valid color step numbers are from 2 to 100, inclusive.
  * Select **Mirror range around center value** to make equal color shifts on either side of the color palette. For example, on a scale from -100 to 0 to 100, values of -20 and a 20 will be the same color distance (10%) from the center color definition — 40% and 60% of the palette gradient respectively.
  * Use the **Range** fields to specify the values that determine the palette gradient start (0%), center (50%), and end (100%) colors. For the start and end colors, you can specify the minimum and maximum values in your data, specific numeric values, or percentile values. For the center value, you can specify the midpoint of the minimum and maximum data values, the data average, the data median, a specific numeric value, or a percentile value. For example, specifying start and end percentile values of 1% and 99% respectively, with a center value of 75%, causes the bottom half of the color gradient to apply to the lower 75% of your data values, and the upper half of the color gradient to apply to the top 25% of your data values.



#### Color coding based on a logical condition

If you are color coding values based on a logical condition (in other words, using one of the **Format** options beginning with **If value is**), choose the **Background Color** , **Font Color** , and **Font Style** for values that meet the condition. By default, the background color is set to the first color of the categorical palette you have chosen for your conditional formatting rule.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-vis-conditional-formatting-rule-value-2308.png)

### Include Totals

If conditional formatting is enabled, you can toggle whether totals are included in the color coding scheme.

### Include Null Values as Zero

If conditional formatting is enabled, you can toggle whether null values should be represented as a zero.

## Adding a table chart to dashboards

When you add a table chart to a [dashboard](https://docs.cloud.google.com/looker/docs/viewing-dashboards), if the **Row Limit** is left blank, the dashboard imposes a limit of 1,000 rows to the table chart tile. To increase the row limit on a dashboard tile, enter a higher row limit up to 5,000, which is the maximum number of rows that can be presented.

Table charts with many rows that are added to a dashboard may look different when they are downloaded or scheduled in PDF format if the **Expand tables to show all rows** option is selected. See the [downloading](https://docs.cloud.google.com/looker/docs/downloading#downloading_a_dashboard_as_a_pdf) or [scheduling](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#expand_tables_to_show_all_rows) documentation pages for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
