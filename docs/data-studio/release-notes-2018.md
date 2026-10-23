---
url: https://docs.cloud.google.com/data-studio/release-notes-2018/
title: Release notes (2018) \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:47.779198+00:00
---

# Release notes (2018)  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/release-notes-2018/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Release notes (2018) Stay organized with collections  Save and categorize content based on your preferences. 

## 2018 releases

  * December 19, 2018 
  * December 14, 2018 
  * November 30, 2018 
  * November 15, 2018 
  * November 2, 2018 
  * October 18, 2018 
  * October 11, 2018 
  * October 3, 2018 
  * September 20, 2018 
  * September 13, 2018 
  * September 06, 2018 
  * Aug 30, 2018 
  * Aug 15, 2018 
  * Aug 2, 2018 
  * July 26, 2018 
  * July 12, 2018 
  * July 3, 2018 
  * June 28, 2018 
  * June 21, 2018 
  * June 14, 2018 
  * June 7, 2018 
  * May 24, 2018 
  * April 26, 2018 
  * April 12, 2018 
  * April 5, 2018 
  * March 27, 2018 
  * March 20, 2018 
  * March 6, 2018 
  * February 6, 2018 
  * January 31, 2018 
  * January 24, 2018 
  * January 12, 2018 



## December 19, 2018

### Product updates

#### Community visualizations in developer preview

Developers can now create [community visualizations](https://docs.cloud.google.com/data-studio/community-visualizations-developer-preview) that work with your data and can be configured just like Data Studio's default charts. The feature is now ready for all developers to build and use visualizations in reports. The [developer preview program](https://developers.google.com/looker-studiovisualization/developer-preview) lets developers try out new and cutting-edge features as they are in progress.

#### Community connectors out of developer preview

[Community connectors](https://docs.cloud.google.com/data-studio/about-community-connectors) are now generally available. Community connectors allow anyone to build their own connections to any internet-accessible data source.

#### Custom SQL support in Cloud SQL connector

You can now use custom SQL statements in the [Google Cloud SQL for MySQL connector](https://docs.cloud.google.com/data-studio/connect-to-google-cloud-sql-for-mysql).

#### Display & Video 360 data source bug fix

We've fixed a bug that prevented you from creating calculated field dimensions in Display & Video 360 data sources.

## December 14, 2018

### Product updates

#### Preset charts and improved chart placement

We've streamlined the way you add visualizations to your reports. You can now choose from a selection of preset charts and add them to the canvas with a single click. The presets include a variety of styling options. For example, you can add a table with a heatmap already applied, or a 100% stacked bar chart. You can also apply different presets to charts that you've already added to the report.

####  Chart interaction filters now include brushing 

[ Chart interactions ](https://docs.cloud.google.com/data-studio/chart-cross-filtering) let you turn your charts into filter controls. **Brushing** allows you to drag your mouse across a chart to select a range of values to filter by. For example, you can use a time series to filter your report by a time frame highlighted on the chart. 

#### Duplicate filters and blended data sources

You can now copy filters and blended data sources within the same report. To do this, edit your report, then choose the **Resource** menu and select the resource you want to manage. Use the **Duplicate** action to make the copy. You can then apply the copied filter or blended data source to other charts in the report.

![The Manage filters option is highlighted in the Resource menu.](https://docs.cloud.google.com/static/data-studio/images/manage-filters-duplicate-2018-12-14.png)

#### New options for handling of missing data

Tables and scorecards now provide a **Missing data** option in the STYLE properties panel. When your data is missing values, charts can display 0, No data, - (hyphen), or null.

## November 30, 2018

### Product updates

#### Embed external content in your reports

You can now add content hosted on other sites in your reports. Using the [URL embed](https://docs.cloud.google.com/data-studio/embed-external-content-in-reports) feature, you can include YouTube videos, web pages, and Google Docs to create robust multi-media experiences for your viewers.

#### PDF download improvements

We've fine-tuned [PDF download](https://docs.cloud.google.com/data-studio/download-a-looker-studio-report-as-pdf) to better support larger reports and reduce time-out errors.

## November 15, 2018

### Product updates

The [Ad Manager 360 connector](https://docs.cloud.google.com/data-studio/connect-to-google-ad-manager-360) lets you visualize over 50 Ad Manager fields directly in Data Studio. Google Ad Manager is a comprehensive hosted ad serving platform that streamlines your ad management, whether you deliver ads to websites, mobile webpages, mobile apps, games, or a combination of these. [Learn more about Google Ad Manager](https://docs.cloud.google.com/admanager/answer/6022000?ref_topic=7519088).

## November 2, 2018

### Product updates

#### Chart-specific calculated fields

You can now add calculated fields directly to a chart in your report. [Chart-specific calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields) let report editors create fields that use the same features as calculated fields in data sources. In addition, chart-specific calculated fields work on blended data.

To create a chart-specific calculated field, select a chart and click **+Add dimension** or **+Add metric** in the DATA properties panel.

#### Chart interactions

You can now [turn your charts into interactive filters](https://docs.cloud.google.com/data-studio/chart-cross-filtering). Viewers can click a dimension value in one chart to filter other charts on the page by the selected value.

#### Search All filter control

In addition to the familiar list style filter control, you now have a new option: [Search All](https://docs.cloud.google.com/looker-studio/answer/9174029#search-all). Report viewers can use advanced search options to filter the report.

#### Updated dimension and metric picker

It's now easier to find and select dimensions and metrics in the component properties panel. When you click a field chip in the right-hand properties panel, the picker now shows field groupings, if available. In addition, you can use both your mouse and keyboard to scroll through the list.

#### Multi-select improvements

You can now resize multiple components at the same time. Just select the charts, controls, images, or shapes you want to resize, then drag a selection box corner to adjust the size.

We've also made it easier to select, move, and resize components that are partially hidden by other components.

## October 18, 2018

### Product updates

  * We've added over 2 dozen fields to the [Search Ads 360 connector](https://docs.cloud.google.com/data-studio/connect-to-search-ads-360-deprecated). To use these fields, [create](https://datastudio.google.com/datasources/create) a new Search Ads 360 data source, or [refresh](https://docs.cloud.google.com/data-studio/refresh-data-source-fields) an existing data source.
  * We've made Undo / Redo in the report editor more reliable.



## October 11, 2018

### Product updates

_This week's features have been postponed temporarily._

### October 3, 2018

### Product updates

  * You can now [download reports as PDF](https://docs.cloud.google.com/data-studio/download-a-looker-studio-report-as-pdf). You can save all pages of the report, or select the pages you want to download and determine their order. Saved reports can include a link back to the report in Data Studio, and you can add password protection to keep your data private.
  * We've added **new "to date" options** to date ranges. These new options let you set a rolling time period without needing to manually update the date range. You can now select from: 
    * **Week to date (Starts Sunday)**
    * **Week to date (Starts Monday)**
    * **Month to date**
    * **Quarter to date**
    * **Year to date**



## September 20, 2018

### Product updates

  * Data Studio is no longer in beta.
  * Calculated fields now support literal negative numbers, for example: Metric * -1.



## September 13, 2018

### Product updates

Google Marketing Platform users can now access their Data Studio reports from within GMP products. GMP users will see their Data Studio reports in the Analytics, Optimize and Tag Manager headers. Simply click on the Data Studio icon to see a list of recent reports or use the search functionality within the header to find a specific report.

## September 06, 2018

### Product updates

  * You can now create data sources based on extracted data. Extracted data sources provide faster performance because the data is static until you refresh it. [Learn more](https://docs.cloud.google.com/data-studio/extract-data-for-faster-performance).



## August 30, 2018

We've improved error messaging in Community Connectors. If you experience connection issues with a third party connector, you'll see error details and support links to help you resolve the issue.

## August 15, 2018

### Product updates

**Important:** **Note for current users of the Campaign Manager 360 connector:** Beginning August 21st, 2018, components using data from the Campaign Manager 360 (previously, DoubleClick Campaign Manager - DCM) connector will no longer support requests for more than two years of data. Components based on Campaign Manager 360 data sources will show an error message when their date range is set to greater than two years. Please update your reports to request less than two years of Campaign Manager 360 data in advance of this change.

You can now [copy and paste chart and control styles](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report). This makes it easier to create consistent looking reports.

## August 2, 2018

### Product updates

  * You can now **connect Data Studio to more Google Marketing Platform products:**
    * **Display & Video 360** is the evolution and consolidation of DoubleClick Bid Manager, Campaign Manager, Studio, and Audience Center. [Learn more about the Display & Video 360 connector](https://docs.cloud.google.com/data-studio/connect-to-display--video-360).
    * **Search Ads 360** is a search management platform that helps agencies and marketers efficiently manage some of the largest search marketing campaigns in the world, across multiple engines and media channels. [Learn more about the Search Ads 360 connector](https://docs.cloud.google.com/data-studio/connect-to-search-ads-360-deprecated).
  * The BigQuery connector now supports explicit data locations. [Learn more](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery).



### Documentation updates

We've added new template reports for **Display & Video 360** and **Search Ads 360** to the [Report Gallery](https://datastudio.google.com/gallery).To use these templates with your own data, preview the report with the links below, then click **USE TEMPLATE**. You can add your own data source and have a functional report in under a minute.

[ Display & Video 360 template report ](https://datastudio.google.com/reporting/1u8yeqgfWIv4iI6eX-vCzNKw0jPN9z8vD/page/pWmV/preview). |  [ Search Ads 360 template report.](https://datastudio.google.com/u/0/reporting/1im01Jl0AP0t3rZH87YU3sXwi2rXNo1oG/page/t4lV/preview)  
---|---  
  
## July 26, 2018

### Product updates

  * Data Studio is now part of **Google Marketing Platform**. We've unified our DoubleClick advertiser products and the Google Analytics 360 Suite under a single brand: Google Marketing Platform. As part of the launch of Google Marketing Platform on July 24, Google Analytics 360 Suite Home has become Platform Home.

> Data Studio's functionality and availability are not affected by these changes. You will, however, see the new Google Marketing Platform brand - including new product names and logos - reflected in product interfaces, help centers, trainings, and more. [Learn more](https://support.google.com/looker-studio/answer/9031231).




``` \- You can now share a **direct link to your Community Connector**. When a user follows the link, it will take them directly to Data Studio with your connector selected. [Learn more](https://developers.google.com/looker-studioconnector/direct-links).

### Documentation updates

You'll notice a fresh new look for all the Google Help Centers, based on [Material Design](https://design.google/). The new design has been optimized for mobile and delivering a better experience for users around the globe.

## July 12, 2018

### Product updates

You can now **blend data from multiple data sources**. For example, you can blend two different Google Analytics data sources to measure the performance of your app and website in a single visualization. You can blend data from different kinds of data sources, as long as there is at least one common field with which to join the data. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).

**Share your data stories on social media** platforms like Twitter, LinkedIn, Facebook, Google+, or on chat applications like Hangouts, or iMessage. [Learn more about sharing on social media](https://docs.cloud.google.com/data-studio/share-reports-on-social-media).

## July 3, 2018

### Product updates

The **Search Console connector** now gives you access to up to **16 months of data**. This data is also available in the Search Console interface (see the [blog post](https://webmasters.googleblog.com/2018/01/introducing-new-search-console.html) ), and in the Search Console API ( [tweet](https://twitter.com/googlewmc/status/1008754160618082304) ).

## June 28, 2018

### Product updates

  * We've made 2 improvements to calculated fields: 
    * Messages for the most common errors are now more informative.
    * You can now format your formulas automatically with the FORMAT FORMULA button.
  * You can now use SVG images in your reports.



## June 21, 2018

### Product updates

  * You can now have **more data in your charts**. Most charts now allow up to 20 dimensions and 20 metrics. Time series support up to 20 metrics. Tables support 10 dimensions and up to 20 metrics. Pivot tables, scorecards, and bullet charts are unchanged.

  * You can now **change the grid size** in the report editor. This makes it easier to create standardized report layouts. The new [Grid Settings options](https://support.google.com/looker-studio/topic/9207420) are located in the _Layout and Theme_ panel.

    * We've built an [example report](https://docs.cloud.google.com/data-studio/example-reports) to demonstrate how you can use the grid. **Check it out!**
  * You can now **embed Data Studio reports** in social media platforms, such as Reddit and Medium, that use the [oEmbed](https://oembed.com/) format. [Learn about more embedding](https://docs.cloud.google.com/data-studio/embed-a-report).

  * Community connectors now support **username/password, and API Token authentication**. [Learn more](https://docs.cloud.google.com/data-studio/community-connector-authorization).




## June 14, 2018

### Product updates

  * You can now generate **thumbnail images** for your reports using the new /thumbnail URL endpoint. Thumbnails are useful for showing viewers a preview of the report's first page. Use them when sharing reports via email, embedding in a website or blog post, etc. [Learn more about thumbnail images](https://docs.cloud.google.com/data-studio/create-a-thumbnail-image-of-your-report).

    * We've **changed the default metric aggregation** for "flexible schema" data sources. (These are data sources based on data sets where we can't know the schema ahead of time, such as Sheets and BigQuery.) In the past, metrics in those data sources defaulted to aggregation type `Sum`. They will now default to aggregation type `None`. This should have no effect on your reports, as the default aggregation of a metric in a chart is still `Sum`. And as before, you can override the default aggregation in the data source or by editing the fields in the report.

In addition, you'll notice new metric icons indicating the aggregation type in your chart configuration:

Icon label  |  Aggregation   
---|---  
AUT  |  Auto   
SUM  |  Sum   
AVG  |  Average   
MIN  |  Min   
MAX  |  Max   
CT  |  Count   
CTD  |  Count Distinct   



### Documentation and help updates

We've add an [example reports](https://docs.cloud.google.com/data-studio/example-reports) article to the Help Center. This page curates a number of demonstration and example reports you can use to see Data Studio features in action. This information is currently only available in English.

## June 7, 2018

### Product updates

  * You can now apply **running calculations** to metrics in your reports. Running calculations compute summary results for each record of data, helping you see how each contributes to the whole picture. [Learn more](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) or view a [sample report](https://datastudio.google.com/u/0/reporting/1DA4qG1pPOqc4KwQz0QpN1rskVGaCdH5I/page/1PzS?utm_source=hc&utm_medium=link&utm_campaign=release-notes&utm_content=demo-reports).
  * You can now access the [Product Overview](https://datastudio.google.com/overview), [Report Gallery](https://datastudio.google.com/gallery), and [Connector Gallery](https://datastudio.google.com/data) from the left-hand navigation in the Data Studio Home page. 
    * [Learn more about the Report Gallery](https://docs.cloud.google.com/data-studio/the-report-gallery).
  * BigQuery data sources now automatically provide a default _Record Count_ metric. You can use this as a breakdown dimension to show the number of records being aggregated by your charts.



## May 24, 2018

### Product updates

  * We've **added some features to Cartesian charts** : 
    * You can now control the display direction of the X and Y axes in area, bar, combo, scatter, and time series charts. In the chart's STYLE properties, under Axes, use the checkboxes to reverse the display order of each axis. [See a demonstration](https://datastudio.google.com/reporting/1x3c58gLBc2DxoB5o3BiyWG8uPMWaK_TE/page/6cRS?utm_source=hc&utm_medium=link&utm_campaign=release-notes&utm_content=demo-reports).
    * Combo charts now support stacked bars.
  * **3rd party connectors now support passing parameters** from reports to the data source. This makes reports based on these connectors more flexible. [Learn more](https://docs.cloud.google.com/data-studio/parameters).



## April 26, 2018

### Product updates

  * You can now connect to Google Cloud Spanner databases. Cloud Spanner is an enterprise-grade, globally-distributed, and strongly consistent database service that combines the benefits of relational database structure with non-relational horizontal scale. [Learn more](https://docs.cloud.google.com/data-studio/connect-to-google-cloud-spanner).
  * [Pivot tables](https://docs.cloud.google.com/data-studio/pivot-table-reference) now let you include up to 10 metrics in your analysis.



## April 12, 2018

### Product updates

You can now toggle table headers on or off using the **Show header** option (located in the table properties STYLE panel). [Learn more about tables](https://docs.cloud.google.com/data-studio/table-reference).

## April 5, 2018

### Product updates

We've launched a **new connector gallery**. It's now easier to find and access both Google and Community connectors. To see the connector gallery, [create a new data source](https://datastudio.google.com/datasources/create).

## March 27, 2018

### Product updates

  * As a part of the **General Data Protection Regulation (GDPR)** , you can now review and accept the Data Processing Terms, as well as supply contact information and company details, by going to ![the Settings icon](https://docs.cloud.google.com/static/data-studio/images/settings-gear-icon-2014-08-20-image.png)**User Settings > Account & Privacy** in Data Studio. Learn more about the [GDPR](https://cloud.google.com/looker/about-the-general-data-protection-regulation-gdpr).
  * The list of available spreadsheets should now load faster when creating Google Sheets data sources.



## March 20, 2018

### Product updates

You can now [bookmark a report](https://docs.cloud.google.com/data-studio/create-custom-bookmark-links-with-report-settings) and preserve its filter settings. This lets you create custom views of your data, as well as specify default settings for multi-select filters.

## March 6, 2018

### Product updates

  * We've improved the [calculated fields editor](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields) with a larger text box and drag-and-drop field selection.
  * Switching chart types now better preserves style settings.



## February 6, 2018

### Product updates

  * You can now configure charts more efficiently by dragging and dropping fields in the report [editor properties panel](https://support.google.com/looker-studio/topic/9207420). [Learn more by watching this video](https://youtu.be/-vGMnYrwVO8).
  * You can now [connect securely to PostgreSQL](https://docs.cloud.google.com/data-studio/connect-to-postgresql) using SSL.



## January 31, 2018

### Product updates

You can now access the following new fields in YouTube data sources:

  * _Video Link_ —provides a clickable link to open the video in new tab
  * _Thumbnail Link_ —provides a clickable link to open the thumbnail image in new tab
  * _Thumbnail_ —displays the video thumbnail image
  * _Linked Thumbnail_ —displays a clickable image of the video thumbnail, which opens the video in new tab



These fields appear automatically in new data sources. To add them to an existing data source, edit the data source, then click **REFRESH FIELDS**. [Learn more](https://docs.cloud.google.com/data-studio/refresh-data-source-fields).

In addition, for new data sources, the _Video Length_ field is now a metric, with an aggregation of AVERAGE. (This change will not be applied to existing data sources, even if you reconnect them.)

## January 24, 2018

### Product updates

  * You can now include up to 3 pivot tables per report page. (The previous limit was 1 pivot table per page.)
  * We've fixed a bug in the COUNT_DISTINCT function. The function now works correctly when filters and date ranges are applied to the data.



## January 12, 2018

### Product updates

  * You can now sort data in charts based on any metric in your data source, even if that field is not in the chart. You can also change the aggregation of the sort fields (the same way you can with other fields in the chart). [Learn more](https://docs.cloud.google.com/data-studio/table-reference).
  * We've fixed a bug in the PERCENTILE function. When using BigQuery Legacy SQL, the function was using the N-1th percentile calculation. The function now correctly uses the Nth percentile.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
