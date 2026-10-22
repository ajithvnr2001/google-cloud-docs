---
url: https://docs.cloud.google.com/data-studio/release-notes-2017/
title: Release notes (2017) \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:57.864651+00:00
---

# Release notes (2017)  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/release-notes-2017/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Release notes (2017) Stay organized with collections  Save and categorize content based on your preferences. 

## 2017 releases

  * December 13, 2017 
  * December 7, 2017 
  * November 29, 2017 
  * November 16, 2017 
  * November 1, 2017 
  * October 26, 2017 
  * October 11, 2017 
  * October 5, 2017 
  * September 28, 2017 
  * September 6, 2017 
  * August 24, 2017 
  * July 19, 2017 
  * July 14, 2017 
  * June 22, 2017 
  * June 16, 2017 
  * June 2, 2017 
  * May 19, 2017 
  * April 27, 2017 
  * April 20, 2017 
  * April 13, 2017 
  * April 6, 2017 
  * March 30, 2017 
  * March 23, 2017 
  * March 17, 2017 
  * March 7, 2017 
  * March 2, 2017 
  * February 16, 2017 
  * February 9, 2017 
  * February 2, 2017 
  * January 26, 2017 
  * January 3, 2017 



## December 13, 2017

### Product updates

Community connector's now let developers more fully [define the connector schema](https://developers.google.com/looker-studioconnector/semantics), including:

  * field semantic type
  * field aggregation type
  * calculated fields
  * field groupings



## December 7, 2017

### Product updates

We've made 2 improvements to [BigQuery data sources](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery) :

  * You can now enable or disable automatic date detection in date-partitioned tables.
  * You can now override the default Billing Project ID and Project ID in custom queries.



### Documentation and help updates

You can now access 2 embedded example reports that show the [HYPERLINK](https://docs.cloud.google.com/data-studio/hyperlink) function in action.

## November 29, 2017

### Product updates

You can now **display clickable images in tables**. To do this, provide an `Image` field as the 2nd parameter of the [HYPERLINK function](https://docs.cloud.google.com/data-studio/hyperlink).

## November 16, 2017

### Product updates

  * You can now **display images in table** s using the [new IMAGE function](https://docs.cloud.google.com/data-studio/image). For example, you can use this to display YouTube video thumbnails or product images in your reports.
  * You can now use **custom queries** in all our database connectors.
  * The [data control](https://docs.cloud.google.com/data-studio/data-control) now supports **Attribution 360 (TV Attribution) and DFP (DoubleClick for Publishers)** data sets.
  * [Pivot tables](https://docs.cloud.google.com/data-studio/pivot-table-reference) can now display metrics as **bars and heatmaps.**



## November 1, 2017

### Product updates

You can now set a [default value](https://docs.cloud.google.com/data-studio/about-controls) for single-select style filter controls. Enter the default value exactly as it appears in your data, including case, punctuation, or special characters.

## October 26, 2017

### Product updates

  * You can now create [pivot tables](https://docs.cloud.google.com/data-studio/pivot-table-reference) in Data Studio.
  * You can now [show Google Analytics sampling](https://docs.cloud.google.com/data-studio/google-analytics-4-sampling) rates used in your Analytics-based charts.
  * [Field editing in reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) now lets you change data types and date formats within a report. You can also apply 3 analytical functions to metrics in your charts: 
    * Percent of Total
    * Difference from Total
    * Percent Difference from Total



## October 11, 2017

### Product updates

You can now remove community connectors. Removing an installed community connector will revoke authorization to both the connector and underlying system. [Learn more about community connectors](https://developers.google.com/looker-studioconnector/).

We've improved performance while editing reports with a large number of components.

We've updated the [Welcome to Data Studio! (Start Here)](https://datastudio.google.com/u/0/reporting/0B5FF6JBKbNJxOWItcWo2SVVVeGc/page/DjD) report to include new features.

## October 5, 2017

### Product updates

  * You can now choose [how to color the dimension data](https://docs.cloud.google.com/data-studio/how-to-color-your-reports) in your reports: 
    * **Color by order** colors the data according to its position in the chart. E.g., the first series is always blue.
    * **Color by dimension value** lets you define the colors to use for each value in your charts. E.g., "France" is always represented in blue. Coloring by dimension values ensures that your data uses color consistently, regardless of the position of that data in the chart. **This is now the default behavior for new reports.**
  * We've added an Embed URL option for embedding reports. This makes it even easier to embed a report into the new Google Sites. [Learn more](https://docs.cloud.google.com/data-studio/embed-a-report).



## September 28, 2017

### Product updates

  * Data sources now have a **Field editing in reports** option. When this option is enabled, you can change field names and aggregations within the reports that use that data source. This makes it easier to customize your reports without having to change the data source. [Learn more](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).
  * We've made a number of **improvements to embedding** Data Studio reports: 
    * You can now easily embed a Data Studio report in the [new Google Sites](https://docs.cloud.google.com/data-studio/embed-a-report). 
      * Just copy and paste the URL portion of the generated iframe code (the portion between the quotes in the `href="..."` property) into the Google Sites Embed widget.
    * We've added an **embedding shortcut button** to the report header ![The Embed button](https://docs.cloud.google.com/static/data-studio/images/iccodegrey6002xweb24dp-2017-09-26.png)
      * In edit mode, click this button to **enable embedding**
      * In view mode, click this button to **display the HTML iframe code** you can use to embed an enabled report. (Previously, you could only generate this code by editing the report.)
  * We've added a **full screen mode** button to the report header ![The Enter Full Screen button](https://docs.cloud.google.com/static/data-studio/images/icfullscreengrey6002xweb24dp-2017-09-26.png)
  * You now have 3 options for **controlling the report header** : 
    * **Always show** —the report header is always visible
    * **Auto hide** —the report header appears briefly, then is hidden. Hover your mouse over the header area to redisplay it
    * **Initially hide** —the report header is hidden until you hover your mouse over the header area



## September 6, 2017

### Product updates

  * You can now [build your own connectors](https://developers.google.com/looker-studioconnector/), allowing you to use Data Studio to display virtually any kind of data to which you have access.
  * You can now share your reports more widely by [embedding](https://docs.cloud.google.com/data-studio/embed-a-report) public or private reports in websites, blogs, and other web properties that support the `iframe` HTML tag.
  * The [data control](https://docs.cloud.google.com/data-studio/data-control) now supports AdWords, Search Console, YouTube, and DoubleClick Campaign Manager data sets, making it easier to create reports that are used across multiple accounts and/or data sources.
  * You can now create data sources based on CSV data stored in [Google Cloud Storage](https://docs.cloud.google.com/data-studio/connect-to-google-cloud-storage) folders and files.
  * You can now configure tables to automatically display metric totals. To do this, check the "Show summary row" option in the _DATA_ tab of the table properties panel.
  * You can now export data from charts directly to Google Sheets.



## August 24, 2017

### Product updates

  * Data Studio is now available in Russia.  Добро пожаловать в Data Studio! 



## July 19, 2017

### Product updates

  * You can now wrap long text in table cells: 
    * Edit your report
    * Select the table
    * Select the **STYLE** tab
    * Check the **Wrap text** option in the Table Body section.



[Learn more about using tables](https://docs.cloud.google.com/data-studio/table-reference).

## July 14, 2017

### Product updates

  * We've launched the **[data control](https://docs.cloud.google.com/data-studio/data-control) :**
    * The data control gives viewers a way to select the Google Analytics data they want to see in a report.
    * This makes it easy for you to share reports based on Google Analytics with viewers who want to use that report with their own Analytics data.
    * Using a data control eliminates the need to create separate reports and data sources for your various Google Analytics views.
  * **Tables** can now contain just dimensions or metrics. You no longer are required to have at least one dimension and one metric.
  * We've improved the **[Google Cloud SQL connector](https://docs.cloud.google.com/data-studio/connect-to-google-cloud-sql-for-mysql) :**
    * Faster data connection
    * SSL support
    * You can now connect via a CloudSQL instance name (no longer requires you to allow specific IP addresses).
  * We've improved the **report editor** : 
    * All new charts and controls appear with a uniform size and style when you initially place them on the canvas. To see this, select a component from the toolbar or Insert menu. Then click the canvas to place the component. As always, you can resize the chart to any size. 
      * You can still use the "click and draw" method to create new charts of any size.
    * All new controls appear with a drop shadow, to help distinguish them from text and charts. You can turn the shadow off by editing the selected control's _STYLE_ properties.



## June 22, 2017

### Product updates

  * Data Studio now supports [links in tabular data](https://docs.cloud.google.com/data-studio/hyperlinks-in-data) : 
    * Use the URL field type to display clickable links in tables
    * Use the HYPERLINK function to construct links in calculated fields.
  * We've added 2 Firebase template reports: 
    * [[Sample] Google Analytics for Firebase Report (Events)](https://datastudio.google.com/org//reporting/0B_U5RNpwhcE6MGdfZmRfcVZKVWs/page/Gg3/preview)
    * [[Sample] Google Analytics for Firebase Report (User Properties)](https://datastudio.google.com/org//reporting/0B_U5RNpwhcE6SXkyNUhiWWt1aHM/page/Ai3/preview)



## June 16, 2017

### Product updates

  * You can now [copy a data source!](https://docs.cloud.google.com/data-studio/copy-a-data-source)
  * [Filter controls](https://docs.cloud.google.com/data-studio/about-controls) now support single select and search.
  * You can now add a bubble size dimension to a scatter chart to have it display as a [bubble chart](https://docs.cloud.google.com/data-studio/scatter-chart-reference).
  * Bug fix: MCC sub-accounts now appear as expected even if the user's email is authorized to view, but is not the owner of, the AdWords account.
  * Bug fix: The "Last 7 days including today" date range now correctly includes all of today's data.



## June 2, 2017

### Product updates

  * You can now view and create feature requests using our new public issue reporting form. [Learn more](https://docs.cloud.google.com/data-studio/contact-us).
  * Report owners can now disable the option to export data from charts using the sharing dialog's _Advanced_ options. [Learn more](https://docs.cloud.google.com/data-studio/export-data-from-a-chart).



### Documentation updates

Learn more about [measuring report usage](https://docs.cloud.google.com/data-studio/measure-report-usage) with Google Analytics.

## May 19, 2017

### Product updates

  * [Add your Google Analytics measurement ID](https://docs.cloud.google.com/data-studio/report-settings) in the report settings panel to measure traffic to your reports.
  * You can now [export data](https://docs.cloud.google.com/data-studio/export-data-from-a-chart) from your charts to CSV.
  * [Combo charts](https://docs.cloud.google.com/data-studio/line-chart-and-combo-chart-reference) let you plot any kind of data using lines, bars, or both.
  * The [MySQL connector](https://docs.cloud.google.com/data-studio/connect-to-mysql) now supports secure connections via SSL.
  * The new secondary sort option in area charts, bar charts, time series, and the new combo chart lets you sort on the breakdown dimensions in those charts.



## April 27, 2017

### Product updates

  * Reports can now be viewed by anyone: no Google sign-in required. To take advantage of this feature, be sure to use "Owner's Credentials" for your data source access. [Learn more about sharing reports via URL](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports).

> In order to support non-signed in viewing, the report URL format has changed slightly. If your reports contained links to specific pages, you will need to update them to the new format. Specifically, if the link previously started with `#` or `open`, make sure it now begins with `org//reporting`. For example, the following link refers to page 2 of the "Warm Welcome" report:
> 
> <https://datastudio.google.com/org//reporting/0B_U5RNpwhcE6R3d5Nk5zOE5ZSGM/page/HjD>

  * Scorecards now have "Missing Data" option which allows you to choose to display either "No data" or "0" when there is no data to display.




## April 20, 2017

### Product updates

  * You can now decide whether to include or exclude hidden columns and filtered rows from Sheets data sources. [Learn more](https://docs.cloud.google.com/data-studio/connect-to-google-sheets).
  * Bars in tables now correctly show the relative scale for the entire data set. Preciously, this scale was set on a page by page basis.



## April 13, 2017

### Product updates

  * We've added a [Search Console template](https://datastudio.google.com/org/UTgoe29uR0C3F1FBAYBSww/reporting/0B_U5RNpwhcE6QXg4SXFBVGUwMjg/page/6zXD/preview) report.
  * [Bar charts](https://docs.cloud.google.com/data-studio/bar-chart-and-column-chart-reference) and [area charts](https://docs.cloud.google.com/data-studio/area-chart-reference) now support a 100% stacking option.



## April 6, 2017

### Product updates

#### Global availability update

Data Studio is now available in Poland. _Witamy!_

#### New table features

We've added 3 new features to tables in reports:

  * You can now specify a secondary sort column as part of the table's DATA settings.
  * You can now set a target reference line for bar graph columns in a table. This is similar to the target feature of bullet charts.
  * You can now display an X-axis for bar graph columns in a table.



[Learn more about tables](https://docs.cloud.google.com/data-studio/table-reference).

#### Metrics in CASE statements

You can now use metrics in CASE statements. [Learn more about CASE](https://docs.cloud.google.com/data-studio/case-searched).

#### New features link

We've added new features link from the Data Studio home page to this Help Center article, making it easier to keep up to date with new features. Look for it in the left hand navigation panel.

### Documentation updates

Reorganized the [data sources](https://docs.cloud.google.com/datastudio#topic=6268199) and [connectors](https://docs.cloud.google.com/datastudio#topic=6370347) topics to make browsing easier.

## March 30, 2017

### Product updates

#### Enhanced layout options

The following new report options give you more control over page layout and screen size:

  * Header visibility—make the report header always visible or auto-hide it
  * Navigation position—display report page navigation at the top or on the left
  * Display mode—fit the report to the width of the browser window, or display as actual size
  * Has margin—show or hide the report margin
  * Canvas Size—select from a number of preset canvas sizes or enter custom display dimensions.



Learn more about [report layout options](https://docs.cloud.google.com/data-studio/report-and-page-layout).

#### New fields available in the DCM connector:

  * \% Visible at Start
  * \% Visible at First Quartile
  * \% Visible at Midpoint
  * \% Visible at Third Quartile
  * \% Visible at Completion
  * \% Audible and Visible at Start
  * \% Audible and Visible at First Quartile
  * \% Audible and Visible at Midpoint
  * \% Audible and Visible at Third Quartile
  * \% Audible and Visible at Completion
  * Impressions Audible and Visible at Completion



#### Faster report performance

We've improved report caching for faster performance in both edit and view modes.

## March 23, 2017

### Product updates

#### Chart switching

Explore your data in edit mode by switching between chart types. For example, you can define a table with the dimensions and metrics you want, apply a filter, ensure the data looks right, then switch to a bar chart, preserving your configuration.

[Learn more about chart switching](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report).

#### Improved file upload column names

Field names in upload files can now contain spaces and special characters. (Commas in field names must still be quoted.)

#### Increased DCM advertiser support

The DoubleClick Campaign Manager connector now supports the full list of advertisers.

## March 17, 2017

### Product updates

The DoubleClick Campaign Manager (DCM) connector now supports the following new fields:

  * _Booked Activities_
  * _Booked Clicks_
  * _Booked Viewable Impressions_



The AdWords connector now supports the _Ad Group Type_ field.

We've added a new function:

  * POWER  \- Returns result of raising a value X to the power Y. X and Y can be metrics, dimensions, or constant values, but you can't mix dimensions and metrics in the same formula.



We've added 10 new fonts:

  * `<font color="#434343" face="Bubblegum Sans"> Bubblegum Sans`
  * `<font color="#434343" face="Boogaloo"> Boogaloo`
  * `<font color="#434343" face="Coming Soon"> Coming soon`
  * `<font color="#434343" face="Cormorant Unicase"> Cormorant Unicase`
  * `<font color="#434343" face="Eater"> Eater`
  * `<font color="#434343" face="Great Vibes"> Great Vibes`
  * `<font color="#434343" face="Oleo Script"> Oleo Script`
  * `<font color="#434343" face="Permanent Marker"> Permanent Marker`
  * `<font color="#434343" face="Raleway"> Raleyway​`
  * `<font color="#434343" face="Reenie Beanie"> Reenie Beanie`



## March 7, 2017

### Product updates

Data Studio is now available in over 180 countries. See the list of [**unsupported** countries](https://docs.cloud.google.com/data-studio/what-you-need-to-use-looker-studio).

We've added a file upload connector type, allowing you to upload up to 2GB of CSV data. [Learn more](https://docs.cloud.google.com/data-studio/upload-csv-files).

## March 2, 2017

### Product updates

You can now create more sophisticated filters, with conditional logic, metric filtering, and additional filter operators. It's also easier to reuse filters on multiple charts. [Learn more.](https://docs.cloud.google.com/data-studio/about-filter-properties)

You can now apply Google Analytics segments to your charts. [Learn more](https://docs.cloud.google.com/data-studio/deprecated-use-universal-analytics-segments).

We've improved added data source management. [Learn more](https://docs.cloud.google.com/data-studio/manage-added-reports-and-data-sources).

The DoubleClick Campaign Manager (DCM) connector now supports the following new fields:

  * Dimensions: 
    * _Placement Pixel Size_
    * _Advertiser Group_
    * _App_
    * _App ID_
    * _Environment_
    * _DBM Site_
    * _DBM Site ID_
  * Metrics: 
    * _Cost Per Click_
    * _Booked Impressions_
    * _Planned Media Cost_
    * _Effective CPM_
    * _Cross-device metrics_
    * _Click-through Revenue_
    * _View-through Revenue_
    * _Total Revenue_



The YouTube connector now supports the _Average Percentage Viewed_ metric.

### Documentation updates

  * Updated [How Data Studio caches data](https://docs.cloud.google.com/data-studio/manage-data-freshness)



## February 16, 2017

### Product updates

  * The DoubleClick Campaign Manager (DCM) connector now supports the following DoubleClick Bid Manager-related fields: 
    * DBM Advertiser
    * DBM Advertiser ID
    * DBM Insertion Order
    * DBM Insertion Order ID
    * DBM Line Item
    * DBM Line Item ID
    * DBM Partner
    * DBM Partner ID
  * The BigQuery connector now supports date partitioned tables.
  * You can now set metric decimal precision in tables.
  * Refreshing a data source will now detect field name changes in your data set.
  * The AdWords connector now includes Campaign ID and Keyword Quality Score fields.
  * The size limit for calculated fields has been increased to 2048 characters.



###  Documentation & Help updates 

Translated versions of these release notes will now be available approximately 1 week after the English version.

## February 9, 2017

### Product updates

``` \- You can now create AdWords data sources using up to 75 accounts in a Manager (MCC) account. See the [blog post](https://analytics.googleblog.com/2017/02/data-studio-enhanced-adwords-mcc-support.html) or [learn more](https://docs.cloud.google.com/data-studio/connect-to-google-ads). \- You can now create data sources based on Google Search Console. [Learn more](https://docs.cloud.google.com/data-studio/connect-to-search-console). \- We've improved report loading times by using magic.

###  Documentation & Help updates 

[Video tutorials](https://docs.cloud.google.com/looker-studio/answer/6390659) now have captions in the 10 supported Help Center languages.

## February 2, 2017

### Product updates

  * We've removed the 5-report limit: you can now create as many reports and data sources as you need in the free version of Data Studio.



## January 26, 2017

### Product updates

  * You can now create data sources that connect to PostgreSQL. [Learn more](https://docs.cloud.google.com/data-studio/connect-to-postgresql).
  * You can now see rolling weekly date windows that start on Monday. (Previously, the weekly window always started on Sunday.) [Learn more](https://docs.cloud.google.com/data-studio/set-report-date-ranges).
  * You can now use the Median and Percentile functions in BigQuery data sources.



## January 3, 2017

### Product updates

The YouTube connector now includes the video title. Refresh the fields of existing YouTube data sources to add the video title.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
