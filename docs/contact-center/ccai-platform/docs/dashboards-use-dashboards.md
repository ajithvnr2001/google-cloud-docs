---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-use-dashboards/
title: Use dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:23:58.635686+00:00
---

# Use dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-use-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Use dashboards Stay organized with collections  Save and categorize content based on your preferences. 

You can filter the data that displays in a dashboard and control the way the data is displayed. You can download data and schedule email delivery of dashboards. Filtering options are explained in each [dashboard page](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-overview).

## Dashboard capabilities

Every dashboard has the following icons to control the dashboard display and access dashboard capabilities:

  * **Reload data** : click refresh **Reload** to get data from the cache. If you change a filter setting before clicking refresh **Reload** , the dashboard gets the most recent data from the backend database.

  * **Hide and show filters** : click filter_list **Hide filters** to hide the filters on the dashboard. Click again to show the filters.

  * **Other dashboard actions** : click more_vert **Dashboard actions** to see other dashboard actions.




## Dashboard actions

With the more_vert **Dashboard actions** menu, you can clear cache and refresh, download, schedule delivery, reset filters and set each tile's time zone.

The following screenshot shows the **Dashboard actions** menu:

![The Dashboard actions menu.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboards-dashboard-actions.png)

### Clear cache and refresh

The **Clear cache and refresh** menu item clears the cache for the dashboard and gets the most recent data from the backend database.

The best practice for dashboards that don't automatically refresh after 20 seconds is to clear the cache and refresh the dashboard to get the most current data. The [email performance dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-email-performance) is an example of a dashboard that doesn't automatically refresh.

### Download

The **Download** menu item lets you download the data from a dashboard. The download includes the data that displays in your dashboard.

To download the data from a dashboard, follow these steps:

  1. Select **Download**.

  2. A dialog box will open.

![The download options dialog box.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboards-download-dialog.png)

**Note:** When a time related metric is exported it will appear in seconds. Otherwise, in the dashboards it will always appear as **HH:MM:SS**.
  3. Choose your download file format:

     * **PDF**

When you select PDF the following settings are available:

       * **Paper Size** : Select the desired paper size.

       * **Expand tables to show all rows** : Select this checkbox to show all rows.

       * **Arrange dashboard tiles in a single column** : Select this checkbox to arrange dashboards tiles in a single column. 

       * **Open in Browser** : Opens the pdf in your browser view.

     * **CSV** : Dashboard's query tiles as a zipped collection of CSV files, excluding text tiles.

  4. Click **Download**.




### Schedule delivery

The **Schedule delivery** menu item lets you schedule email deliveries of dashboards in PDF, CSV, or PNG formats at a frequency that you specify.

#### Starting a delivery from a dashboard

Go to the dashboard you wish to schedule for delivery. Click the **Schedule Delivery** button.

You can manage and modify these settings at any time from the dashboard settings menu.

#### Existing Schedule

If you have already created schedules for this dashboard, an existing schedules window appears. This window shows the schedules that you have set along with information about each schedule, such as destination and format.

![The existing schedules dialog.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboards-schedules.png)

Deliveries that use the Send now recurrence and schedules that were created by other people do not appear in this window.

#### Schedule and send window

If you select **New** from the existing schedules window, or, if you do not have any pre-existing schedules for the dashboard, once you have clicked **Schedule delivery** a schedule and send window opens.

This window lets you customize recurrence, destination, format, filters, and more.

#### Schedule Name

The top of the schedule and send window shows the name that is automatically given to the delivery. The name defaults to the dashboard's name.

To edit the schedule's name, select the name and make your edits.

#### Recurrence

Customize the timing of your delivery in the **Recurrence** section.

In the **Recurrence** dropdown choose how often you want your dashboard to be delivered. You can select from options such as **every 15 minutes** , **hourly** , **daily** , **weekly** , or **monthly**.

#### Send Now

You can choose to send the dashboard immediately using the **Send Now** option.

A one-time delivery of the dashboard is sent after you select the **Send Now** button at the bottom of the dashboard.

#### Destination

**Email** : Select the recipients you want to receive the dashboard. You can add recipient(s) within or outside your organization by entering their **Email address(es)**.

If you're entering multiple email addresses, select the Enter key, or add a comma, after each address.

#### Format

Select the **Format** in which you want to deliver your dashboard. You can choose between PDF, CSV, or PNG.

The Format field contains a drop-down menu of available formats:

**CSV zip file** : The unformatted data from the dashboard delivered as a collection of comma-separated values (CSV) files in a zipped directory. For deliveries to email, the ZIP file is delivered as an email attachment.

**PDF** : An image of the dashboard as a single PDF file. The default layout displays tiles as they are arranged in the dashboard, but other layout and sizing options are available under Advanced options. For deliveries to email, the file is delivered as an email attachment.

**PNG visualization** : An image of the dashboard as a single PNG file. The default layout displays tiles as they are arranged in the dashboard, but other layout options are available under Advanced options. For deliveries to email, the image appears inline within the body of the email.

#### Filters

Choose the filters tab to apply the filters to your dashboard. This ensures that only relevant data is sent to your recipients.

**Caution:** Known Issue: The **Test Now** button in the **Schedule Delivery > Filters** tab is currently not working. This will be fixed in an upcoming release.

![The filter options for the schedule delivery window.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboards-sched-delivery-filters.png)

The **Filters** tab in the schedule and send window shows any filters applied to the dashboard as well as their values. In this tab, you can edit the values for any existing filters applied to the dashboard and the new values will be applied to the delivery.

The dashboard itself will not be affected. You cannot add filters to your schedule in the Filters tab, only view and edit the values for existing dashboard filters.

For example, you might send regional teams results that are filtered for their states of interest.

#### Advanced options

The **Advanced options** tab provides additional customization for your delivery. The options available depend on the selected destination and format of your delivery.

##### Custom message

This option is available only for the email destination.

Enter a message you would like included in the body of emails to recipients. The limit is 1500 characters.

##### Include Links

This option is available only for the email destination.

Select this option to include in the data delivery emails a "view full dashboard" link that goes to the dashboard.

##### Expand tables to show all rows

This option is available only for PDF formats of dashboard deliveries.

Select the **Expand tables to show all rows** box to display all rows of any table visualizations in the dashboard — rather than just those rows that display in the dashboard tile thumbnails.

If the **Expand Tables to Show All Rows** option is selected, dashboard tiles that contain table visualizations may look slightly different in delivered PDFs than they do in the dashboard.

The following differences may be noticeable in the PDF:

  * Customizations to background colors and font sizes are removed from column headers and subtotal rows

  * Table appearance

  * Tables with Size Columns to Fit enabled stretch to the full width of the tile




Additionally, for tables with more than 20,000 cells, the following differences may be noticeable in the PDF:

  * Conditional formatting options other than background color no longer appear

  * Cell visualizations on numeric columns no longer appear




##### Arrange dashboard tiles in a single column.

This option is available only for the PDF and PNG visualization formats of dashboard deliveries.

This layout displays dashboard tiles in a single vertical column. Leave the box unchecked to show the tiles as they are arranged in the dashboard.

##### Paper size

This option is available only for PDF formats of dashboard deliveries.

You have the option to specify the optimal size and orientation of dashboard PDFs by selecting from the **Paper size** drop-down menu.

Large visualizations or groups of overlapping dashboard tiles may need to be resized to fit cleanly on a PDF page.

##### Delivery time zone

By default this will use the same timezone associated with the dashboard.

If you want to specify a different time zone, select the **time zone** from the drop-down menu. The time zone you select does not affect the data in your dashboard, just the timing of the delivery.

### Reset filters

The **Reset filters** menu item lets you reset the filters of your dashboard to their default settings.

### Each tile's time zone

The **Each tile's time zone** menu item lets you set the time zone for your dashboard.

## Tile actions

With the more_vert **Tile actions** menu, you can select options for a tile. The options vary depending on whether the tile is a standard tile or a table tile.

The following screenshot shows the **Tile actions** menu for a standard tile:

![The Tile actions menu for a standard tile.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboards-tile-actions-standard.png)

The following screenshot shows the **Tile actions** menu for a table tile:

![The Tile actions menu for a table tile.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboards-tile-actions-tables.png)

### Download Data

This opens a dialog box with a window where you can name and format your download.

Data can be downloaded in the following formats:

  * TXT (tab-separated values)

  * Excel spreadsheet (Excel 2007 or later)

  * CSV

  * JSON: For JSON format, field labels are used as its rendered value in its JSON output. See the [Change in JSON formatting;Community post](https://www.googlecloudcommunity.com/gc/Modeling/Change-in-JSON-Render-Formatting-6-22/td-p/565932?_ga=2.36973924.578722944.1685547925-1272889234.1654557569) for more information about how this renders fields in JSON format.

  * HTML

  * Markdown

  * PNG (image of visualization)




Expand the **Advanced** data options menu to see all available options for your download.

#### Values

Choose how you want the downloaded query results to appear:

  * If you choose **Unformatted** , special formatting is not applied to your query results, such as rounding long numbers or adding special characters. This is often preferred when data is being fed into another tool for processing.

  * If you choose **Formatted** , special formatting is applied, although some features (such as linking) aren't supported by all file types.




#### Results

  * If you choose **With visualization options applied** , the visualization settings are applied to your download.

  * If you choose **As displayed in the data table** , visualization options will not be applied and the download will appear like the data table.




#### Limits

You can choose how much data you want to download as follows:

**Caution:** Downloading an unlimited number of results is restricted for queries with table calculations. To download more than **Results in Table** , select **Custom** and enter a limit of up to 100000 rows.

**Results in table** : Number of rows specified by the row limit of your content.

**All Results** : All results returned by the query. Before selecting this option, see the All Results section on this page.

**Custom** : A custom number of rows.

### Clear cache & refresh

Click **Clear cache & refresh** to clear your cache and get data from the backend database.

### Autosize all columns

Click **Autosize all columns** to resize the width of each column to fit its column heading name or its longest data value, whichever is wider.

### Reset all column widths

Click **Reset all column widths** to reset each column to its default width.

## Table options

You can change the sort order and select options for the columns of a table.

### Sort columns

Click a column heading to switch the sort order from ascending to descending or from descending to ascending.

### Set column options

To set column options, click more_vert **Column options** , and then select **Freeze** , **Copy Value** , **Autosize All Columns** , or **Reset All Column Widths**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
