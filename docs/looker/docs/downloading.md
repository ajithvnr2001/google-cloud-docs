---
url: https://docs.cloud.google.com/looker/docs/downloading/
title: Downloading content \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:10.889156+00:00
---

# Downloading content  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/downloading/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Downloading content Stay organized with collections  Save and categorize content based on your preferences. 

This page describes downloading content — visualizations or data — from Looker.

To download content, you must be given the [`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) or [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permission by a Looker admin.

The process and options for downloading content and formatting downloaded content vary based on whether you're downloading from a Look or an Explore, from a dashboard, or from a merged results query.

## Downloading data from a Look or an Explore

**Note:** If you're using Looker's [new Explore experience](https://docs.cloud.google.com/looker/docs/new-explore-experience-overview), see the [Viewing and interacting with Explores in the new Explore experience](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#save-or-share-menu) documentation page.

To download data from a Look or an Explore page, select the gear menu in the upper right and select **Download**.

Looker displays the **Download** window, where you can name and format your download.

![](https://docs.cloud.google.com/static/looker/docs/images/download-look-explore-modal-2300.png)

The following sections will walk you through each field in the **Download** window:

  * Format
  * Filename
  * Results
  * Data values
  * Number of rows and columns to include



### Format

> Downloads to formats that use the renderer (PNG and PDF) will use results from [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode). If your download is in another format, the download will show results from whichever mode — development or production — you are in.

Data can be downloaded from Looks and Explores in the following file formats:

  * TXT (tab-separated values)
  * Excel spreadsheet (Excel 2007 or later)
  * CSV
  * JSON
  * HTML
  * Markdown
  * PNG (image of visualization)



While choosing your data format for downloading, if you don't see the HTML or PNG (image of visualization) options (for Looks), talk to your Looker admin about installing the appropriate version of the [Chromium renderer](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium) for your Looker instance.

For JSON format, Looker uses field [labels](https://docs.cloud.google.com/looker/docs/reference/param-field-label) as its rendered value in its JSON output. See the [Change in JSON formatting](https://www.googlecloudcommunity.com/gc/Modeling/Change-in-JSON-Render-Formatting-6-22/td-p/565932) Community post for more information about how Looker renders fields in JSON format.

[Transposed tables](https://docs.cloud.google.com/looker/docs/table-options#transpose) will render in PNG downloads only.

For Looker developers, if you are in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode), data downloads in most file formats query your model as it is in Development Mode. PDF and PNG file formats are the exception; data downloads in those file formats always query your model as if it is in Production Mode.

### Filename

You can enter a filename for the download or use the default filename that is pre-populated in the field. Looker will automatically append the appropriate file extension based on your selection in the **Format** field.

### Results

**Note:** The **Results** section is not available for PNG format.

In the **Results** section, choose whether you want visualization settings applied to your TXT, Excel, CSV, JSON, HTML, or Markdown data download.

If you choose **With visualization options applied** , Looker applies some of the visualization settings to your download. Any of the following settings in the [Plot](https://docs.cloud.google.com/looker/docs/table-options#plot_menu_options), [Series](https://docs.cloud.google.com/looker/docs/table-options#series_menu_options), and [Formatting](https://docs.cloud.google.com/looker/docs/table-options#formatting_menu_options) menus that are configured for the visualization will be applied to the data download:

  * [Show Row Numbers](https://docs.cloud.google.com/looker/docs/table-options#show_row_numbers)
  * [Show Totals](https://docs.cloud.google.com/looker/docs/table-options#show_totals)
  * [Show Row Totals](https://docs.cloud.google.com/looker/docs/table-options#show_row_totals)
  * [Limit Displayed Rows](https://docs.cloud.google.com/looker/docs/table-options#limit_displayed_rows) to a maximum of 500 rows shown or hidden
  * [Show Full Field Name](https://docs.cloud.google.com/looker/docs/table-options#show_full_field_name)
  * [Custom labels](https://docs.cloud.google.com/looker/docs/table-options#label) for each column (Looker uses field [labels](https://docs.cloud.google.com/looker/docs/reference/param-field-label) as its rendered value in its JSON output. See the [Change in JSON formatting](https://www.googlecloudcommunity.com/gc/Modeling/Change-in-JSON-Render-Formatting-6-22/td-p/565932) Looker Community post for more information about how Looker renders fields in JSON format).
  * [Conditional Formatting](https://docs.cloud.google.com/looker/docs/table-options#enable_conditional_formatting) for downloads of table chart visualizations in Excel format

**Note:** Conditional formatting is displayed in Excel deliveries of Looks and Explores with table chart visualizations only if the **Along a scale Rule** is applied. In addition, row-level highlighting in conditional formatting is not supported for Excel exports. If your dashboard requires row-level highlighting, use the PDF or image export formats instead, as they fully support this feature.



Some visualization settings are not applied to downloaded results. For example:

  * Custom header text color and background color are not applied to downloaded results, except for PNG files.
  * For results tables with pivots and multiple measures, each pivot value is repeated across columns rather than represented as one merged column. HTML and PNG downloads are an exception, so the merged column is preserved.
  * When you download from a dashboard, the dashboard tile title is not included in downloaded results.
  * The **Totals** and **Row Totals** values are included in downloaded results, but the respective row and columns are not labeled.
  * [Subtotals](https://docs.cloud.google.com/looker/docs/table-options#subtotals) won't be downloaded for queries that can't be streamed.



Columns in table charts that have been [manually rearranged](https://docs.cloud.google.com/looker/docs/table-options#manually_moving_and_pinning_columns) will appear in their original order in the download if the query includes any of the following elements:

  * fields that are deliberately [hidden from the visualization](https://docs.cloud.google.com/looker/docs/creating-visualizations#hiding_fields_from_visualizations)
  * fields that are present in the [underlying SQL](https://docs.cloud.google.com/looker/docs/how-looker-generates-sql#viewing_the_query) but that are not present in the visualization, such as the following:

    * a dimension present in the visualization that contains a [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link) parameter that references another field that is not present in the visualization.
    * a field that uses the [`case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) parameter.
    * a dimension that is present in the visualization that references another field with the [`{{ field_name._value }} Liquid variable syntax`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#accessing_variables_from_other_fields), which is not present in the visualization.
  * One or more fields with [dimension fill](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) enabled

  * Three or more [pivoted fields](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions)

  * [Row totals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals) enabled

  * One or more fields that include the [`order_by_field`](https://docs.cloud.google.com/looker/docs/reference/param-field-order-by-field) LookML parameter in the field definition

  * [Merged results](https://docs.cloud.google.com/looker/docs/merged-results) queries 




In addition, Looker's CSV export prioritizes the raw data structure over visualization-applied column reordering. To preserve the visual column order for merged queries, you can export to Excel (`.xlsx`), deliver the data to Google Sheets, or reorder the columns in the underlying Explore before saving. 

If you choose **As displayed in the data table** , visualization options won't be applied and the download will appear like the data table in the **Data** section of the Look or Explore.

### Data values

**Note:** The **Data values** section is not available for PNG format.

In the **Data values** section, choose how you want the downloaded query results to appear:

  * If you choose **Unformatted** , Looker does not apply any special formatting of your query results, such as rounding long numbers or adding special characters your Looker developers may have put in place. This is often preferred when data is being fed into another tool for processing.
  * If you choose **Formatted** , the appearance of the data will be similar to the **Explore** experience in Looker, although some features (such as linking) aren't supported by all file types. For example, any formatting applied with the [`html`](https://docs.cloud.google.com/looker/docs/reference/param-field-html) parameter won't be applied to TXT, CSV, Excel, or JSON downloads.



#### Date and time formats in CSV downloads

When you download data in CSV format, the date and time format that's used depends on whether query results are retrieved from cache or from a new query:

  * **Cached results** : Looker reuses the string that's generated for the UI display, which uses ISO 8601 offset notation (such as `2026-01-06T20:17:50+00:00`).
  * **Uncached results** : When a new query runs on the database (such as when downloading **All Results** or running scheduled deliveries), Looker's CSV renderer processes the data directly, which defaults to UTC notation (such as `2026-01-06T20:17:50 UTC`).



Both notations represent the same point in time. To enforce a consistent date and time format in CSV downloads, you can specify the display format that you want by using the [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) parameter in the LookML dimension (for example, `value_format: "yyyy-mm-dd hh:mm:ss\" +00:00\""`). For fields that are defined with `type: date_time`, this formatting might be ignored in some CSV rendering scenarios.

### Number of rows and columns to include

**Note:** The **Number of rows and columns to include** section is not available for PNG format.

You can choose how much data you want to download as follows:

  * **Current result table** : Number of rows that are specified by the row limit of your content.
  * **All results** : All results that are returned by the query. Before selecting this option, see the All Results section on this page.
  * **Custom** : A custom number of rows to download. If your content contains pivoted data, you can also set a custom number of columns to download. Users with [`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) permissions are limited to a maximum of 5,000 rows (or up to 50,000 rows if an admin has configured a higher [visualization limit](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits)) and 50 columns, while users with [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permissions are allowed to download more, subject to system or query limits. 

Setting granular, per-user or per-role custom download limits (such as restricting specific users to exactly 100,000 rows) is not directly supported. Any custom download limit is applied as an instance-wide setting that affects all users.

As a workaround to enforce a custom row download cap instance-wide, you can modify the `max-unstreamed-limit` startup flag on your Looker instance. Setting this startup flag to 100,000 restricts all users on the instance to a maximum of exactly 100,000 rows.




#### All results

When you select **Run** in a Look or an Explore, Looker checks your permissions and determines whether the complexity of the query and the database dialect will allow the entire query to be downloaded. If you have the permissions (for results over a set limit) and if Looker determines that your entire query can be downloaded, the **All results** option will be available in the **Download** window.

The **All results** option is typically disabled for queries that do any of the following:

  * Involve [row totals](https://docs.cloud.google.com/looker/docs/best-practices/row-limits-in-looker) or [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations)
  * Use [percent of total](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percent_of_total), [percent of previous](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percent_of_previous), or [running totals](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#running_total) types of measures
  * Retrieve data from a database dialect that cannot stream results
  * Include pivoted columns that Looker calculates because the data comes from a database dialect that cannot calculate the pivots



> Even when the **All results** option is available, you should still use caution when downloading all results. Some queries are very large, containing thousands or millions of rows, which can overwhelm most spreadsheet programs — or even your Looker instance.

If the **All results** option is unavailable, you can use the **Custom** option to specify the maximum number of rows that are allowed with your permissions.

##### Streaming query results

Streaming refers to Looker's ability to process data in chunks, rather than all at once. If Looker can stream a result set, then unlimited downloads are possible. The **All results** option relies on Looker's ability to stream results, and **All results** won't be available if streaming results isn't possible.

**Note:** Looker streams downloaded results to all formats except rendered formats (HTML, PNG).

In addition to the format limitations, there are two cases where streaming is not possible:

  1. **Table calculations** : Table calculations cannot be streamed. Therefore, to download unlimited results for a query, you must remove table calculations from the query.
  2. **Database limitations** : Some databases cannot stream if pivots are included in the query. For these databases, you must remove pivots to download unlimited results. Some databases can't stream any results, which means that unlimited downloads are not possible.



These databases support streaming:

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
  
These are the databases that support streaming with pivots applied:

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
  
##### Remove all sorts from query

When you select **All Results** , you may also see the option to **Remove all sorts from query**. This option prevents sorting on your query before you download the results. Selecting this option may speed up your download, since sorting a query can be costly to performance for certain database types.

**Note:** The **Remove all sorts from query** option is not supported for pivoted results.

##### Allow large results

When you're downloading a large result set in Looker using [Google BigQuery](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery) as your database dialect and you select **All Results** , you may see the **Allow large results** option. This is because Google BigQuery has a _maximum response size_ for query results, as described on the [Write query results](https://docs.cloud.google.com/bigquery/docs/writing-results#large-results) documentation page. To download results that exceed the BigQuery maximum response size, Looker must perform a different process.

If you select **Allow large results** , the download process is affected as follows:

  * The `allowLargeResults` BigQuery option is set to `true` for the query.
  * The `ORDER BY` clauses in the query are removed.
  * The query will write to a [PDT temp schema](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#creating_a_temporary_dataset_for_persistent_derived_tables) and requires permission to write to one.
  * The results of the query are stored in this temporary scratch schema under a random table name for one hour.



### Download or open in browser

Once you've selected your options, you can select the **Download** button to download a file to your computer, or select **Open in Browser** to view the file in the browser.

## Downloading data from a merged results query

To download [merged results](https://docs.cloud.google.com/looker/docs/merged-results) queries, you can [save the query to a dashboard](https://docs.cloud.google.com/looker/docs/merged-results#saving_your_merged_results_to_a_dashboard) and then download the dashboard as a PDF or as a collection of CSV files. However, you must download the entire dashboard — you cannot download the data from just a single tile that is based on a merged results query.

When you're downloading merged results as a CSV file, custom column reordering that's applied in the visualization is ignored because CSV export prioritizes the raw data structure. To preserve visual column ordering for merged queries, you can export to Excel (`.xlsx`), deliver the data to Google Sheets, or reorder the columns in the underlying Explore before saving. 

## Downloading data from a dashboard

To download the entire dashboard, select **Download** from the dashboard's three-dot menu more_vert.

Selecting **Download** opens a dialog that lets you select PDF or CSV as your download format.

### Downloading a dashboard as a PDF

**Note:** PDF downloads may not exactly match the layout or sizing of the dashboard as viewed within Looker.

You can download your entire dashboard as a PDF, which means you will get a PDF that displays the dashboard title, any dashboard filters, some or all dashboard tiles, and the time zone that the dashboard was run in. The PDF will also include a timestamp that shows when the dashboard was downloaded. For [dashboards that have tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#download-pdf), all the tabs will appear in the same PDF. The contents of each tab will be organized under a content header with the name of the tab.

Downloads in PDF format always return data from the model as if it is in [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode), even if you are in Development Mode.

When you download a dashboard as a PDF, any applied [theme](https://docs.cloud.google.com/looker/docs/themes-for-internal-dashboards) will be reflected in the downloaded file.

If your dashboard includes [filters on visualization tiles](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#filters-on-visualization-tiles), those filters are captured in a format that's based on the visible frame. If a tile filter bar contains overflowing filters that require scrolling, only the filters visible on the screen are included in the PDF; overflowing filters are cut off.

**Important** : Starting in Looker 26.4, table charts, scatterplot charts, and Google Maps charts that have [increased row limits](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits) are subject to the following limitations when you download, send, or schedule dashboards in PDF format: 

  * The query results for each table chart on a dashboard will display up to 50,000 rows, to a maximum total limit of 200,000 cells per dashboard. 
  * If the combined total of cells for table charts on a dashboard is greater than 200,000 cells, table chart results may be trimmed. If the maximum is reached, users will see a warning that will also be displayed at the bottom of the rendered PDF. 
  * Table charts on a dashboard PDF will display more rows than are displayed on the dashboard tile thumbnail only when the **Expand tables to show all rows** option is selected. 
  * Scatterplot charts and Google Maps charts support up to 50,000 data points (rows) in PDF downloads. The charts will render as the they appear in the tile thumbnail, [or fail](https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-chromium-renderer) based on standard renderer limitations. 



To download a dashboard as a PDF, follow these steps:

  1. Select **PDF** from the **Format** drop-down menu.
  2. Select an option from the **Paper Size** drop-down menu.

The **Fit Page to Dashboard** option is the default; it sizes the PDF to the default width for dashboards (1260 px). Other paper size options size the PDF to match a standard paper size and fit all or part of the dashboard within it. Depending on the layout of the dashboard and the paper size selected, some PDF outputs may differ from the dashboard layout when viewed within Looker. For example, when the paper size selected is narrower than the dashboard, you may encounter issues with the spacing or other formatting and need to make some adjustments:

     * Large visualizations or groups of overlapping tiles may need to be resized to fit in the PDF.
     * Tiles that contain tables may not show all table columns in the PDF.
     * Tiles may be reduced in width to fit the PDF. Similarly, tiles that require scrolling in the Looker app may not expand to display all content.

If you don't see the **Paper Size** option, talk to your Looker admin about installing the latest version of the [Chromium renderer](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium) for your Looker instance.

  3. If you select something other than **Fit Page to Dashboard** in the **Paper Size** drop-down, or if you select **Page breaks between tabs** for a dashboard that has tabs, an **Orientation** option appears. You can choose to orient the dashboard in portrait or landscape position.

  4. Select or leave unselected **Expand tables to show all rows**. If you select this option, for dashboard tiles that use [table](https://docs.cloud.google.com/looker/docs/table-options) visualizations, the PDF will show all the rows that are available in the table visualization, not just the rows that are visible in the dashboard tile thumbnail.

Starting in Looker 26.4, the query results for each table chart on a dashboard PDF can display up to 50,000 rows, to a maximum total limit of 200,000 cells per dashboard, if your admin has [increased the row limit setting](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits). If the combined cell total for the table charts on a dashboard is greater than 200,000 cells, table chart results may be trimmed. If this maximum is reached, users will see a warning that will also be displayed at the bottom of the rendered PDF.

If you don't select the **Expand all tables to show all rows** option, only the rows that are visible in the thumbnail without scrolling will appear in the PDF. Dashboard and query filters will still apply, as will visualization settings such as [row limits](https://docs.cloud.google.com/looker/docs/table-options#row_limit), [column limits](https://docs.cloud.google.com/looker/docs/table-options#column_limit), and settings that are made with the [**Limit Displayed Rows**](https://docs.cloud.google.com/looker/docs/table-options#limit_displayed_rows) option.

If the **Expand Tables to Show All Rows** option is selected, dashboard tiles that contain table visualizations may look slightly different in downloaded PDFs than they do inside Looker. The following differences may be noticeable in the PDF:

     * Customizations to background colors and font sizes are removed from column headers and subtotal rows.
     * If no custom theme is set, Tables appear in the [white theme](https://docs.cloud.google.com/looker/docs/table-options#table_theme). Otherwise, the custom theme is applied when downloaded.
     * The [sort icon](https://docs.cloud.google.com/looker/docs/table-options#sorting_columns) does not appear on pivoted tables that were not manually sorted.
     * Tables with [**Size Columns to Fit**](https://docs.cloud.google.com/looker/docs/table-options#size_columns_to_fit) enabled stretch to the full width of the tile.
     * Tables with [row grouping](https://docs.cloud.google.com/looker/docs/table-options#grouping-menu-options) enabled download as flat data, and the grouping column expands to display all columns.

Additionally, for tables with more than 20,000 cells, the following differences may be noticeable in the PDF:

     * [Conditional formatting](https://docs.cloud.google.com/looker/docs/table-options#enable_conditional_formatting) options other than **Background color** no longer appear.
     * [Cell visualizations](https://docs.cloud.google.com/looker/docs/table-options#cell_visualization) on numeric columns no longer appear.

If you don't see the **Expand tables to show all rows** option, talk to your Looker admin about installing the appropriate version of the [Chromium renderer](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium) for your Looker instance.

**Caution:** If the **Expand Tables to Show All Rows** option is selected, tiles that contain table visualizations may look slightly different in downloaded PDFs than they do inside Looker.
  5. Select or leave unselected **Arrange dashboard tiles in a single column**. If you select this option, the PDF displays dashboard tiles in a single vertical column. If you don't select this option, the dashboard tiles appear as they are arranged in the dashboard.

  6. If your [dashboard has tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#download-pdf), select or leave unselected **Page breaks between tabs** to separate tabs on to different pages, and choose a page orientation from the **Orientation** menu. If you don't select **Page breaks between tabs** , and multiple tabs are selected (for example, if **Whole dashboard** , or if one or more tabs are specified for the **Custom** option), all tabs will appear on the same page. The contents of each tab will be organized under a content header with the name of the tab.

  7. If your dashboard has tabs, select an option from the **Download Tabs** menu. You can choose to download the entire dashboard, the tab that is open, or a custom selection of tabs. If you choose **Custom** , you can specify the tabs to download in the **Select Tabs** field.

  8. Select **Open in Browser** to see an image of the PDF in a new tab of your browser. From there, you can opt to download the PDF using your browser's controls.

  9. Select **Cancel** if you no longer want to download the dashboard.

  10. Select **Download** to initiate the download. A new tab in your browser will open, showing the status of your download.




### Downloading a dashboard as a CSV file

You can download all the query tiles from your dashboard as a zipped collection of CSV files. Text tiles are not included in the ZIP file. To download your dashboard as a collection of CSV files, follow these steps:

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-beta-csv-format-2220.png)

  1. Select **CSV** from the **Format** drop-down menu.
  2. Select **Cancel** if you no longer want to download the dashboard.
  3. Select **Download** to initiate the download of your zipped CSV collection.



When you download a dashboard as CSV files, the options for formatting downloads, such as setting custom row limits or choosing all results, are unavailable. The row limits in the downloaded files correlate to the row limits on the corresponding tiles.

Looker generates zipped files using UTF-8 encoding. If the characters in your CSV filenames appear garbled, there may be a conflict between Looker's UTF-8 encoding and the default encoding of your machine's operating system or a third-party application. Looker suggests that you use a file extractor that recognizes UTF-8, such as [7-Zip](https://www.7-zip.org/), and ensure that any third-party applications are configured to support UTF-8.

### Downloading data from dashboard tiles

**Note:** You cannot download the data from dashboard tiles that are based on [merged results](https://docs.cloud.google.com/looker/docs/merged-results) queries, but the data from merged results tiles is included if you download a dashboard as a PDF or as a collection of CSV files.

To download the data from a dashboard tile, select the three-dot icon on the tile and select **Download data** :

![](https://docs.cloud.google.com/static/looker/docs/images/dashboards-beta-tile-download-718.png)

The **Download data** dialog displays several options that are are similar to those for a Look or an Explore. Expand the **Advanced data options** menu to see all available options for your download:

![](https://docs.cloud.google.com/static/looker/docs/images/dashboards-beta-tile-download-modal-2316.png)

  * **Format**
  * **Results**
  * **Data values**
  * **Number of rows and columns to include**



#### Format

You can download data from dashboard tiles in the following file formats:

  * TXT (tab-separated values)
  * Excel spreadsheet (Excel 2007 or later)
  * CSV
  * JSON
  * HTML
  * Markdown
  * PNG (image of visualization)

**Note:** PNG downloads use results from [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode). Other formats show results from whichever mode you are in when you perform the download.

Depending on the format you select, some options in the **Advanced data options** menu may not be available.

If the HTML or PNG (image of visualization) options are missing, consult your Looker admin about installing the appropriate version of the [Chromium renderer](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium) for your Looker instance.

For JSON format, Looker uses field [labels](https://docs.cloud.google.com/looker/docs/reference/param-field-label) as its rendered value in its JSON output. See the [Change in JSON formatting](https://www.googlecloudcommunity.com/gc/Modeling/Change-in-JSON-Render-Formatting-6-22/td-p/565932) Community post for more information about how Looker renders fields in JSON format.

[Transposed table visualizations](https://docs.cloud.google.com/looker/docs/table-options#transpose) will render in PDF and PNG downloads only.

Downloads in PNG format always return data from the model as it is in [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode), even if you are in Development Mode.

#### Results

In the **Results** section, choose whether you want visualization settings applied to your data download:

  * If you choose **With visualization options applied** , Looker applies some of the visualization settings to your download. Any of the following settings in the [Plot](https://docs.cloud.google.com/looker/docs/legacy-table-options#plot_menu_options), [Series](https://docs.cloud.google.com/looker/docs/legacy-table-options#series_menu_options), and [Formatting](https://docs.cloud.google.com/looker/docs/legacy-table-options#formatting_menu_options) menus that are configured for the visualization will be applied to the data download:

    * [Show Row Numbers](https://docs.cloud.google.com/looker/docs/legacy-table-options#show_row_numbers)
    * [Hide Totals](https://docs.cloud.google.com/looker/docs/legacy-table-options#hide_totals)
    * [Hide Row Totals](https://docs.cloud.google.com/looker/docs/legacy-table-options#hide_row_totals)
    * [Limit Displayed Rows](https://docs.cloud.google.com/looker/docs/legacy-table-options#limit_displayed_rows) to a maximum of 500 rows shown or hidden.
    * [Show Full Field Name](https://docs.cloud.google.com/looker/docs/legacy-table-options#show_full_field_name)
    * [Custom labels](https://docs.cloud.google.com/looker/docs/legacy-table-options#customizations) for each column (Looker uses field [labels](https://docs.cloud.google.com/looker/docs/reference/param-field-label) as its rendered value in its JSON output. See the [Change in JSON formatting](https://www.googlecloudcommunity.com/gc/Modeling/Change-in-JSON-Render-Formatting-6-22/td-p/565932) Looker Community post for more information about how Looker renders fields in JSON format).
    * [Conditional Formatting](https://docs.cloud.google.com/looker/docs/legacy-table-options#conditional_formatting) for downloads of table chart visualizations in Excel format.
**Note:** Conditional formatting will be displayed in downloads in Excel format with table chart visualizations only if the **Along a scale Rule** is applied. In addition, row-level highlighting in conditional formatting is not supported for Excel exports. If your dashboard requires row-level highlighting, use the PDF or image export formats instead, as they fully support this feature.

Columns in table charts that have been [manually rearranged](https://docs.cloud.google.com/looker/docs/table-options#manually_moving_and_pinning_columns) will appear in their original order in the download if the query includes any of the following elements:

    * One or more fields that are [hidden from the visualization](https://docs.cloud.google.com/looker/docs/creating-visualizations#hiding_fields_from_visualizations)
    * One or more fields that reference a dimension in the [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link) parameter that is not selected in the current Explore
    * One or more fields with [dimension fill](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) enabled
    * Three or more [pivoted fields](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions)
    * [Row totals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals) enabled
    * [Merged results](https://docs.cloud.google.com/looker/docs/merged-results) queries 



If you choose **As displayed in the data table** , visualization options will not be applied and the download will appear like the data table in the **Data** section of the Look or Explore.

#### Data values

In the **Data values** section, choose how you want the downloaded results to appear:

  * If you choose **Formatted** , the data will appear more similar to the **Explore** experience in Looker, although some features (such as linking) aren't supported by all file formats.
  * If you choose **Unformatted** , Looker does not apply any special formatting of your results, such as rounding long numbers or adding special characters your Looker developers may have put in place. This is often preferred when data is being fed into another tool for processing.



#### Number of rows and columns to include

You can specify how much data is included in your download in this section. In most tiles, this section of the download dialog is named **Number of rows to include** ; if the tile query contains any pivoted dimensions, this section is named **Number of rows and columns to include**. Your options include:

  * **Current result table** : Number of rows specified by the row limit — and column limit, if the tile query contains at least one pivoted dimension — of your tile's underlying data table.
  * **All Results** : All results that are returned by the tile query, even if the tile's data table specifies a more restrictive [row limit or column limit](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#limiting_data). Before selecting this option, see the Considerations when using the All Results or Custom option section on this page. This option is not visible to users who don't have [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permissions.
  * **Custom** : A custom number of rows to download. If your content contains pivoted data, you can also set a custom number of columns to download. Users with [`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) permissions are limited to a maximum of 5,000 rows (or up to 50,000 rows if an admin has configured a higher [visualization limit](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits)) and 50 columns, while users with [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permissions are allowed to download more, subject to system or query limits. 

Setting granular, per-user or per-role custom download limits (such as restricting specific users to exactly 100,000 rows) is not directly supported. Any custom download limit is applied as an instance-wide setting that affects all users.

As a workaround to enforce a custom row download cap instance-wide, you can modify the `max-unstreamed-limit` startup flag on your Looker instance. Setting this startup flag to 100,000 restricts all users on the instance to a maximum of exactly 100,000 rows.




##### Considerations when using the All Results or Custom option

Looker checks your permissions and determines whether the complexity of the query and the database dialect will allow the entire query to be downloaded. If you have the permissions to download results over a set limit and if Looker determines that your entire query can be downloaded, the **All Results** option will be available in the **Download** window.

The **All Results** option is typically disabled for queries that:

  * Involve [row totals](https://docs.cloud.google.com/looker/docs/best-practices/row-limits-in-looker)
  * Use [percent of total](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percent_of_total), [percent of previous](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percent_of_previous), or [running totals](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#running_total) types of measures
  * Retrieve data from a database dialect that cannot stream results
  * Include pivoted columns that Looker calculates because the data comes from a database dialect that cannot calculate the pivots

**Note:** Even when the **All Results** option is available, you should still use caution when downloading all results. Some queries are very large, containing thousands or millions of rows, which can overwhelm most spreadsheet programs — or even your Looker instance.

If the **All Results** option is unavailable, you can use the **Custom** option to specify the maximum number of rows allowed with your permissions. When you select **Custom** , you can specify a number of result rows to download. If your query contains any pivoted dimensions, you can also specify a number of columns to download.

## For admins: Enabling downloading data for your Looker instance

Certain downloading options require that admins of customer-hosted Looker deployments have installed the appropriate version of the [Chromium renderer](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium). If your instance is Looker-hosted, Chromium is already installed.

The [Managing business user features](https://docs.cloud.google.com/looker/docs/managing-business-user-features#downloading_data_from_dashboard_tiles_without_download_permission) documentation page has important admin information about the download process:

  * [User permissions and dashboard downloads](https://docs.cloud.google.com/looker/docs/managing-business-user-features#downloading_data_from_dashboard_tiles_without_download_permission)
  * [Rendering image-based formats for download](https://docs.cloud.google.com/looker/docs/managing-business-user-features#rendering_image-based_formats_delivery)
  * [Rendered formats and download permissions](https://docs.cloud.google.com/looker/docs/managing-business-user-features#downloading_content_in_rendered_format)
  * [JSON download formats](https://docs.cloud.google.com/looker/docs/managing-business-user-features#formatting_json_deliveries_and_downloads)
  * [Troubleshooting downloads of large Excel files](https://docs.cloud.google.com/looker/docs/managing-business-user-features#large_excel_files_hanging_or_not_opening)



To learn more about the permissions that must be assigned to users to enable them to download — specifically the [`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) and [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permissions — visit the [**Roles**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
