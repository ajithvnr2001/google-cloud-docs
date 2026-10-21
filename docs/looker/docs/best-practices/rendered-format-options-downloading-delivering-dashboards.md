---
url: https://docs.cloud.google.com/looker/docs/best-practices/rendered-format-options-downloading-delivering-dashboards/
title: Downloading or delivering dashboards in rendered formats \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:40.746770+00:00
---

# Downloading or delivering dashboards in rendered formats  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/rendered-format-options-downloading-delivering-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Downloading or delivering dashboards in rendered formats Stay organized with collections  Save and categorize content based on your preferences. 

You can [download](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_a_dashboard) a Looker dashboard in PDF or CSV format. You can [send or schedule](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards) a Looker dashboard in PDF, PNG, or CSV format. 

PDF and PNG formats are considered rendered formats. This page provides examples of the types of output these rendered formats produce, given different settings in Looker. 

**Important** : For customer-hosted Looker instances, [installation of Chromium](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#installing_rendering_software_to_run_standard_looker_features) is required to output rendered formats. 

All examples on this page use a dashboard called **Download Dashboard** , which features tiles with different chart types: 

  * A **Users by state** tile with a [map chart](https://docs.cloud.google.com/looker/docs/visualization-guide#maps)
  * Two tiles with [single value charts](https://docs.cloud.google.com/looker/docs/visualization-guide#single_value) — **Orders this month** and **Order items this month**
  * An **Orders by month** tile with a [table chart](https://docs.cloud.google.com/looker/docs/table-options) that features two columns of values that are represented as text and as a bar chart.
  * A **Users acquired over time** tile with a [column chart](https://docs.cloud.google.com/looker/docs/visualization-guide#column)
  * A **Sales by State and Category** tile with a table chart with values that are represented as text.



![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-render-options-1-2210.png)

## PDFs

To output PDFs, follow the instructions for [downloading a dashboard as a PDF](https://docs.cloud.google.com/looker/docs/downloading#downloading_a_dashboard_as_a_pdf) or, when sending or scheduling a dashboard, [choosing the PDF format](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#format). 

Table charts, scatterplot charts, and Google Maps charts that have [increased row limits](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits) are subject to the following limitations when you download, send, or schedule dashboards in PDF format: 

  * The query results for each table chart on a dashboard will display up to 50,000 rows, to a maximum total limit of 200,000 cells per dashboard. 
  * If the combined total of cells for table charts on a dashboard is greater than 200,000 cells, table chart results may be trimmed. If the maximum is reached, users will see a warning that will also be displayed at the bottom of the rendered PDF. 
  * Table charts on a dashboard PDF will display more rows than are displayed on the dashboard tile thumbnail only when the **Expand tables to show all rows** option is selected. 
  * Scatterplot charts and Google Maps charts support up to 50,000 data points (rows) in PDF downloads. The charts will render as the they appear in the tile thumbnail, [or fail](https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-chromium-renderer) based on standard renderer limitations. 



By default, a PDF file mirrors what you see when you view the dashboard in your browser at a width of 1680 pixels, subject to any limitations applied by your PDF reader. Here is an example of a PDF download with Looker's default settings: 

![Donwload Dashboard rendered as a PDF with Looker default settings.](https://docs.cloud.google.com/static/looker/docs/images/dashboard-render-options-2-2210.png)

You can change the appearance of the dashboard in the PDF by adjusting several Looker settings. When scheduling and sending, you can find these settings in the [**Advanced options**](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#advanced_options) tab of the **Schedule** or **Send** windows. When downloading, you can find these settings in the download window. 

  * **Paper Size** : This setting lets you specify the optimal size and orientation of dashboard PDFs.
  * **Expand tables to show all rows** : This setting lets you choose whether to display all rows of any table visualizations in the dashboard — rather than just those rows that display in the dashboard tile thumbnails.
  * **Arrange dashboard tiles in a single column** : This setting lets you choose whether to display the dashboard in a single-column layout.



### PDFs and the **Paper Size** setting

The default for the [Paper Size](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#paper_size) setting is the **Fit Page to Dashboard** option; it sizes the PDF to match the layout of the dashboard on the screen. 

Other paper size options size the PDF to match a standard paper size and fit the dashboard within it. You may be asked to choose an **Orientation** of portrait or landscape. Depending on the layout of the dashboard, large visualizations or groups of overlapping tiles may need to be resized to fit on a given page size. 

The **Paper Size** option may also introduce page breaks to format the content appropriately to the paper size and orientation you select. When a **Paper Size** is specified, Looker determines "rows" of elements that page breaks will form around. Looker does this to avoid inserting page breaks in the middle of visualizations. 

**Tip:** When you specify the paper size and orientation, consider element size and dashboard layout. Dashboard tiles may need to be reorganized to accommodate the selected page size and Looker-determined line breaks. For example, page breaks may occur in very tall dashboard elements or in overlapping groups of tiles, producing a garbled PDF. 

See the following section for an example of what a PDF with a non-default **Paper Size** setting looks like. 

### PDFs and the **Expand tables to show all rows** setting

The [**Expand tables to show all rows**](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#expand_tables_to_show_all_rows) setting is disabled by default. 

When enabled, this setting displays all rows of a table visualization, rather than just the rows that are visible in the tile thumbnail. Looker determines groups of dashboard tiles to break into rows (similar to how it determines page breaks). Then, Looker uses a CSS grid layout to position the groups of tiles to accommodate the expansion. Expanding the table increases the size of the grid rows, causing the elements around the expanded tables to move along with the expanded table. 

The following image shows what a PDF of the example dashboard would look like with a **Paper Size** setting of A5 (5.83 in. x 8.27 in.), a portrait **Orientation** , and an enabled **Expand tables to show all rows** setting. The tiles have been resized to fit the A5 width, the table tile at the bottom shows all rows of the table, and page breaks have been inserted between the tiles and also before the timestamp at the bottom of the PDF. 

![Download Dashboard rendered with the Paper Size setting, portrait Orientation, and Expand tables to show all rows setting enabled.](https://docs.cloud.google.com/static/looker/docs/images/dashboard-render-options-3-2210.png)

### PDFs and the **Arrange dashboard tiles in a single column** setting

The [**Arrange dashboard tiles in a single column**](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#arrange_dashboard_tiles_in_a_single_column) setting is disabled by default. 

A single-column PDF stacks each dashboard tile in a single column. The width of the PDF and dashboard tiles is 800 pixels. Wide tables will be scaled to fit within the 800-pixel, single-column rendering. 

Here is the example dashboard rendered as a single column PDF: 

![Download Dashboard rendered with all tiles stacked in a single column.](https://docs.cloud.google.com/static/looker/docs/images/dashboard-render-options-8-2210.png)

**Note:** Single column PDFs with the **Expand tables to show all rows** option applied often render with page breaks in the middle of expanded tables. However, no data should be cut off. 

## PNGs

The PNG format is available only when you [send or schedule](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards) dashboards. It is not available when you download dashboards. 

For the most part, PNG files render the same as PDF files, with a few differences: 

  * When the [**Arrange dashboard tiles in a single column**](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#arrange_dashboard_tiles_in_a_single_column) setting is selected, each tile renders as an individual PNG file rather than all tiles rendering together as a single file.
  * The **Paper Size** and **Expand tables to show all rows** settings are not available for PNG.
  * The only options for adjusting the appearance of PNG deliveries are the **Arrange dashboard tiles in a single column** setting and the [**Table resolution**](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#table_resolution) setting.



Here is what the delivery looks like when the **Table resolution** setting is set to **Normal**. Notice that the wide table, **Orders by State and Category** , is cut off — not all columns are rendered:

![Download Dashboard rendered as a PNG with normal table resolution selected and the Orders by State and Category table columns cut off.](https://docs.cloud.google.com/static/looker/docs/images/dashboard-render-options-9-2212.png)

Here is what the delivery looks like when the **Table resolution** setting is set to **Wide**. Recipients may need to scroll horizontally to see the entirety of the tiles:

![Download Dashboard rendered as a PNG with wide table resolution selected and tiles very wide.](https://docs.cloud.google.com/static/looker/docs/images/dashboard-render-options-10-2212.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
