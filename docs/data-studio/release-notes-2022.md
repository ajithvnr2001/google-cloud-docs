---
url: https://docs.cloud.google.com/data-studio/release-notes-2022/
title: Release notes (2022) \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:57.313683+00:00
---

# Release notes (2022)  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/release-notes-2022/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Release notes (2022) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Request new features or upvote existing feature requests [here](https://docs.cloud.google.com/data-studio/contact-us).

  * December 20, 2022 
  * December 1, 2022 
  * November 10, 2022 
  * October 11, 2022 
  * September 4, 2022 
  * August 4, 2022 
  * July 28, 2022 
  * July 14, 2022 
  * June 29, 2022 
  * June 20, 2022 
  * June 16, 2022 
  * May 26, 2022 
  * May 12, 2022 
  * April 28, 2022 
  * April 21, 2022 
  * April 7, 2022 
  * March 24, 2022 
  * March 17, 2022 
  * March 11, 2022 
  * February 17, 2022 
  * February 10, 2022 
  * January 27, 2022 



####  See older releases 

  * [ 2021 ](https://docs.cloud.google.com/data-studio/release-notes-2021)
  * [ 2020 ](https://docs.cloud.google.com/data-studio/release-notes-2020)
  * [ 2019 ](https://docs.cloud.google.com/data-studio/release-notes-2019)
  * [ 2018 ](https://docs.cloud.google.com/data-studio/release-notes-2018)
  * [ 2017 ](https://docs.cloud.google.com/data-studio/release-notes-2017)
  * [ 2016 ](https://docs.cloud.google.com/data-studio/release-notes-2016)



##  December 20, 2022 

###  Product Updates 

####  **Monitor a report's Google Analytics 4 usage data**

For Data Studio reports that connect to Google Analytics 4 (GA4) data, you can now monitor quota token usage to more easily keep your reports within [ Google Analytics Data API (GA4) quotas ](https://developers.google.com/analytics/devguides/reporting/data/v1/quotas). 

In edit mode, right-click on a report chart or canvas to access the _Google Analytics Token Usage_ dialog, where you can view both the amount of quota tokens consumed by report components and the remaining amount of tokens. This information, combined with the recommended [ best practices for reducing the amount of data that is queried from GA4 ](http://support.google.com/looker-studio/answer/12182485#ga4-quota), can help reports keep within GA4 quota limits. 

![](https://docs.cloud.google.com/static/l/data-studio/ages/ga4tokenusagedialog2022-12-20.png)

##  December 1, 2022 

###  Announcements 

####  **Data Studio Pro is now generally available**

Contact [ Google Cloud Sales ](https://cloud.google.com/contact?direct=true) today to get Data Studio Pro. 

###  Product updates 

####  **Set up organizational ownership of Data Studio assets**

Data Studio Pro customers can link Data Studio to a Google Cloud project and perform a one-time migration of existing Data Studio assets to that project. Organizational ownership of Data Studio assets gives you the following benefits: 

  * All the Data Studio assets that your users create are stored in a Google Cloud project. 
  * Assets won't be deleted when the users who own them leave your organization. 
  * You can assign project-level permissions using IAM that apply to all Data Studio assets in your organization. 
  * Data Studio assets that are owned by a Google Cloud project are available to other Cloud services (for example, lineage in Dataplex). 



[ Learn more ](https://docs.cloud.google.com/l/data-studio/nk-looker-studio-pro-to-a-google-cloud-project-mau-version). 

####  **Team workspaces public launch**

Data Studio Pro customers can manage access to their reports and data source at scale with team workspaces. 

[ Learn more ](https://docs.cloud.google.com/l/data-studio/out-team-workspaces). 

####  **Hide and show the report editor properties panel**

You can now choose which properties panels to display while editing your reports. On the far right of the editor, use the panel manager to hide and show the properties and data panels. ![The properties panel, data panel, and panel manager. The panel manager consists of 2 buttons arranged vertically. Click the top button to hide/show the data panel. Click the bottom button to hide/show the properties panel.](https://docs.cloud.google.com/static/l/data-studio/ages/panel-manager-release-notes-image.png)

##  November 10, 2022 

###  Product updates 

####  **Report editor improvements**

We've added the following improvements to the Data Studio report editor: 

  * **Resizable component properties panel.** You can resize the component properties panel. 
  * **Zoom control**. While in edit mode, you can use the Zoom control and menu to increase or decrease the report canvas' display scale. 



![The report editor, with the Zoom \(magnifying glass\) control selected. The Zoom control is located in the toolbar. The drop down arrow next to the control displays zoom options and hotkeys.](https://docs.cloud.google.com/static/l/data-studio/ages/zoom-control-lang-neutral-2022-11-10.png)

####  Google Analytics Data API (GA4) concurrent request quotas enforced for Data Studio reports 

Data Studio reports that visualize Google Analytics 4 data are subject to Analytics Data API (GA4) quotas for concurrent requests. Reports that exceed this quota may display the following error message: 

Exhausted concurrent requests quota. 

Learn more about [ what you can do ](https://docs.cloud.google.com/l/data-studio/oubleshooting-guide) if you experience this error. 

##  Oct 11, 2022 

###  Product updates 

####  Data Studio is now Data Studio 

We are unifying our business intelligence product family under the Looker umbrella, bringing together Looker, Data Studio, and core Google technologies like artificial intelligence (AI) and machine learning (ML). Data Studio is still free, and has the same features as Data Studio. 

To learn more, [ read our blog post ](https://cloud.google.com/blog/products/data-analytics/looker-next-evolution-business-intelligence-data-studio). 

**Note** : 

  * The product has a new URL: lookerstudio.google.com. 
  * This Help Center also has a new URL: support.google.com/looker-studio. 



Links to the previous product and Help Center will redirect to the new URLs. 

####  Data Studio Pro 

Data Studio Pro is the paid version of Data Studio. With Data Studio Pro, you get access to all the features of Data Studio, plus enhanced enterprise capabilities and technical support. [ Learn more ](https://docs.cloud.google.com/l/data-studio/out-looker-studio-pro). 

####  Data Studio / Looker Integration Public Preview 

The Looker connector for Data Studio (formerly Data Studio) is now available in preview. The Looker connector lets data workers self-serve while enabling organizations to maintain governance over their data. The connector is compatible with Google Cloud hosted instances of Looker version 22.16 or higher. 

Submit this [ sign-up form ](https://forms.gle/bw7uaNUTcsEQxVRK7) to get access. 

[ Learn more ](https://docs.cloud.google.com/l/data-studio/nnect-to-looker) about the Looker integration. 

##  Sep 4, 2022 

###  Product updates 

####  Resizable editor panels 

The following panels in the report editor are now resizable: 

  * Data panel 
  * Left-hand page navigation 
  * Version history 



To reset the panels to the default size, in the menus, click **View > Reset panel layouts **. 

##  August 4, 2022 

###  Product updates 

####  Visualize data from Google Analytics 4 sub and roll-up properties 

You can connect to Google Analytics 4 subproperties and roll-up properties using the [ Google Analytics connector ](https://docs.cloud.google.com/l/data-studio/nnect-to-google-analytics). 

Learn more about [ structuring your Analytics account ](https://support.google.com/analytics/answer/9679158). 

##  July 28, 2022 

###  Product updates 

####  Data control support for Google Analytics 4 properties 

The data control now supports Google Analytics 4 properties. [ Learn more about the data control ](https://docs.cloud.google.com/l/data-studio/ta-control). 

###  Documentation updates 

####  New: How to use Data Studio 

Learn the fundamentals of Data Studio with the _How to use Data Studio_ guide. The _How to_ guide will help you understand the core concepts you'll need to know to "think with Data Studio." You'll learn how to perform the most common tasks in Data Studio and find links to more in-depth content to increase your expertise. 

[ Read the guide now ](https://docs.cloud.google.com/looker-studio/topic/12141289). 

####  Updated: Use Data Studio with the Google Cloud Platform Agreement 

To accept that Data Studio be governed by the Google Cloud Platform Terms of Service, you must have a Google Cloud role that grants the ` roles/billing.viewer ` permission, such as **Billing Account Viewer**. (Previously, [ ](https://docs.cloud.google.com/lhttps://cloud.google.com/looker/use-looker-studio-with-the-google-cloud-platform-agreement%20this%20article%20</a>%20didn't%20include%20this%20requirement.\)%20</p>%20<a%20name=)

##  July 14, 2022 

###  Product updates 

####  IP address change for firewall access 

The IP addresses needed to connect Data Studio to a database behind a firewall are changing. To continue accessing your data, you'll need to open new IP addresses, as listed below. **The deadline for making this change is Jun 21, 2023.**

Affected data sources include those created with the following connectors: 

  * Amazon Redshift 
  * MySQL 
  * PostgreSQL 
  * Microsoft SQL Server 2017 



New IP addresses to open: 

  * 142.251.74.0/23 
  * 142.251.74.0/23 Correction: 2023-01-25 This address was erroneously listed twice. 
  * 2001:4860:4807::/48 (Optional, for platforms that support IPv6) 



You must also keep this address open until the deadline: 

  * 74.125.0.0/16 



After the deadline, you can close these old IP addresses: 

  * 64.18.0.0/20 
  * 64.233.160.0/19 
  * 66.102.0.0/20 
  * 66.249.80.0/20 
  * 72.14.192.0/18 
  * 108.177.8.0/21 
  * 173.194.0.0/16 
  * 207.126.144.0/20 
  * 209.85.128.0/17 
  * 216.58.192.0/19 
  * 216.239.32.0/19 



##  June 29, 2022 

###  Product updates 

####  Use Data Studio with the Google Cloud Platform Agreement 

Cloud Identity and Google Workspace administrators can choose to have their Google Cloud Platform Agreement govern their use of Data Studio on behalf of their organization. [ Data Studio Terms of Service ](https://cloud.google.com/looker/use-looker-studio-with-the-google-cloud-platform-agreementLearn%20more%20</a>.%20</p>%20<p>%20View%20the%20<a%20href=). 

####  Line map layer in Google Maps 

You can now visualize BigQuery linestring data using a line map in a Google Maps chart. Line maps are useful for understanding physical networks and flows. For example, you may want to visualize the volume of goods flowing through your supply chain, examine traffic congestion in a city, or study the water infrastructure in a region. [ Learn more about line maps ](https://docs.cloud.google.com/lo/data-studio/gle-maps-reference). 

##  June 20, 2022 

###  Product updates 

####  Google Cloud service account data credentials 

Google Cloud and Workspace users can now use service account credentials to access BigQuery data in Data Studio. Using a service account provides a number of benefits, such as ensuring that data access isn't tied to a particular user, so data sources continue to work even if the person who created the data source leaves your organization. 

Learn more: 

  * [ Set up a Cloud service account for Data Studio ](https://docs.cloud.google.com/lo/data-studio/-up-a-google-cloud-service-account-for-looker-studio)
  * [ Use service account credentials in your data source ](https://docs.cloud.google.com/lo/data-studio/a-credentials)



##  June 16, 2022 

###  Product updates 

![The data panel is available when a report is in Edit mode and displays all data sources and fields in expandable and collapsable sections, as well as a search bar for finding fields in connected data sets.](https://docs.cloud.google.com/static/lo/data-studio/ges/data-panel-v2-numbered-2022-06-15.png)

It's now easier to access all the data that's available to use in your reports. When you edit a report, you'll find a new _Data_ panel in the properties panel. The data panel lists all of the data sources that have been added to the report. Expand a data source to access all the fields and parameters in that data source. Drag fields from the data panel to a chart or canvas to add that data to the report. 

[ Learn more about configuring report components ](https://docs.cloud.google.com/lo/data-studio/figure-report-components). 

####  Explore BigQuery data in a Data Studio report 

You can now visualize a BigQuery table or custom query in Data Studio using the "Explore" options in the BigQuery console. Simply select a table or run a query, then click **Explore with Data Studio**. 

[ Take a tutorial ](https://docs.cloud.google.com/bigquery/docs/visualize-data-studio). 

####  Linking API general availability 

The Data Studio Linking API is now generally available. The Linking API provides a reliable interface to configure and forward users directly to a Data Studio report via a URL. When users follow a Linking API URL they have a streamlined experience to quickly view and interact with their data. 

[ Learn more about the Linking API ](https://developers.google.com/looker-studio/integrate/linking-api). 

##  May 26, 2022 

###  Documentation updates 

####  Troubleshooting guide 

We've published this [ troubleshooting guide ](https://docs.cloud.google.com/lo/data-studio/ubleshooting-guide) to help you learn how to resolve issues with charts, reports, and data sources. 

##  May 12, 2022 

###  Product updates 

####  Pivot table optional metrics 

You can now use [ optional metrics ](https://docs.cloud.google.com/lo/data-studio/ional-metrics) in pivot tables. 

####  More Custom Cache Options 

You can now schedule [ data freshness ](https://docs.cloud.google.com/lo/data-studio/age-data-freshness) to update minutely every 1 to 50 minutes, or hourly every 1 to 12 hours for the following connectors: 

  * MySQL 
  * PostgreSQL 
  * MS SQL Server 
  * Amazon Redshift 
  * CloudSQL for MySQL 
  * Google Cloud Storage 
  * Cloud Spanner 



[ Learn more about connecting to database platforms ](https://docs.cloud.google.com/looker-studio/topic/7332343). 

##  April 28, 2022 

###  Product updates 

####  Updated report templates 

When you open a template, in the top right corner, you'll see icons indicating the data sources used by the report. 

To replace any data sources in the report with your data, click **Use my own data** , then click **Replace data.**

To make a copy of the template, click **Edit and share**. You can then modify and share the report as your own. 

[ Learn more about templates ](https://docs.cloud.google.com/lo/data-studio/ate-a-report-from-a-template). 

##  April 21, 2022 

###  Product updates 

####  More data from Google Ads 

You can now visualize the following Ads shopping fields: 

  * _Average cart size_
  * _Average order value_
  * _Brand_
  * _Channel_
  * _Channel Exclusivity_
  * _Click Share_
  * _Custom Label 0_
  * _Custom Label 1_
  * _Custom Label 2_
  * _Custom Label 3_
  * _Custom Label 4_
  * _Order COGS_
  * _Order Gross Profit_
  * _Product Condition_
  * _Product Title_
  * _Product Type L1_
  * _Product Type L2_
  * _Product Type L3_
  * _Product Type L4_
  * _Product Type L5_
  * _Search Abs Top IS_
  * _Avg. Product Price_
  * _Offer ID (Item ID in CM panel)_
  * _Category L1 symbol_
  * _Category L2 symbol_
  * _Category L3 symbol_
  * _Category L4 symbol_
  * _Category L5 symbol_
  * _Merchant Center ID_
  * _Country of sale_



To see these fields in your reports, [ refresh the data source ](https://docs.cloud.google.com/lo/data-studio/resh-data-source-fields). 

##  April 7, 2022 

###  Product updates 

####  Microsoft SQL Server / Amazon Redshift connectors to general availability 

We've removed the "beta" label from the Microsoft SQL Server and Amazon Redshift connectors. With this release, Data Studio now fully supports the following JDBC database products: 

  * [ Amazon Redshift ](https://docs.cloud.google.com/lo/data-studio/nect-to-amazon-redshift)
  * [ Microsoft SQL Server 2017 ](https://docs.cloud.google.com/lo/data-studio/nect-to-microsoft-sql-server)
  * [ MySQL ](https://docs.cloud.google.com/lo/data-studio/nect-to-mysql)
  * [ PostgreSQL ](https://docs.cloud.google.com/lo/data-studio/nect-to-postgresql)



##  March 31, 2022 

###  Product updates 

####  More data from Search Console 

You can now include data from discover and googleNews search types in your Search Console reports. These search types are available when you connect to the URL Impression table. 

Learn more about [ connecting to Search Console ](https://docs.cloud.google.com/lo/data-studio/nect-to-search-console). 

####  More data in tables 

You can now display up to 50,000 rows in tables in your reports. Previously, tables could display a maximum of 5,000 rows. 

##  March 24, 2022 

###  Product updates 

####  Chart cross-filtering on by default 

Cross-filtering lets you interact with one chart and apply that interaction as a filter to other charts in the report. Previously, cross-filtering was turned off for all charts by default. Starting this week, cross-filtering is turned on for charts based on most connectors, with the following exceptions: 

  * Campaign Manager 360 
  * Display and Video 360 
  * Google Ad Manager 360 
  * Google Ads 
  * Google Analytics 
  * Search Ads 360 
  * Search Console 
  * Youtube Analytics 



Learn how to [ turn on cross-filtering on and off ](https://docs.cloud.google.com/lo/data-studio/rt-cross-filtering). 

##  March 17, 2022 

###  Product updates 

####  Improved report templates 

You can now add data to reports template more easily. When you open a template, you'll see the added data sources in the top right corner. 

![](https://docs.cloud.google.com/static/lo/data-studio/ges/template-add-data-2-2022-03-17.png)

**How to use a template**

  1. To see what the template looks like using your own data, in the top right, click **Add data.**
  2. To turn the template into your own report, click **Edit and share**. 



[ Learn more ](https://docs.cloud.google.com/lo/data-studio/ate-a-report-from-a-template). 

##  March 11, 2022 

###  Product updates 

####  More data from Google Ads 

The [ Google Ads connector ](https://docs.cloud.google.com/lo/data-studio/nect-to-google-ads) now lets you visualize the following Ads trial campaigns fields: 

  * Account Time Zone 
  * Base Campaign Id 
  * Base Campaign Name 
  * Trial Campaign Id 
  * Trial Campaign Name 
  * Trial Campaign Start Time (UTC) 
  * Trial Campaign End Time (UTC) 
  * Trial Campaign Display Status 
  * Campaign Trial Type 
  * Trial Id 
  * Trial Description 



To see these fields in your reports, [ refresh the data source ](https://docs.cloud.google.com/lo/data-studio/resh-data-source-fields). 

####  Home page search keywords 

You can now find reports and data sources more easily by using **to:** , **from:** and **me** keywords. Navigate to the Data Studio home page, click Reports, Data Sources, or Explorations, then enter your search in the search field. 

![](https://docs.cloud.google.com/static/lo/data-studio/ges/search-keywords-2022-03-11.png)

_Search keywords_

  * ` to: ` _someone@example.com -_ finds assets you've shared with that person. 
  * ` from: ` _someone@example.com -_ finds assets that person has shared with you. 
  * ` to:me ` \- finds assets shared with you by anyone. 
  * ` from:me ` \- finds assets you've shared with anyone. 
  * ` me ` \- searches for ` to:me ` or ` from:me ` or ` owner:me ` (Note: this also does a literal search for "me"). 
  * ` owner:me ` \- finds assets owned by you (Note: this is the same as the current behavior of searching for your own email address). 



You can make more complex searches by using "AND", "OR", and grouping with parentheses. For example: ` owner:me AND (to:boss@example.com OR president@example.com) `

##  February 17, 2022 

###  Product updates 

####  Improved data blending 

Visualizing data based on multiple data sources is now more powerful and more flexible. With data blending you can now select from 5 different join operators: 

  * Inner join 
  * Left outer join 
  * Right outer join 
  * Full outer join 
  * Cross join 



(Previously, you were limited to left outer join.) 

When you create a blend, you can now select different fields for each join configuration. (Previously, you had to use the same fields across each join configuration in the blend.) 

Learn more about [ blending improvements and see the updated documentation and examples ](https://docs.cloud.google.com/lo/data-studio/-blends-work-in-looker-studio). 

####  Optional client authentication in MySQL and PostgreSQL connectors 

You can now enable SSL encryption for MySQL and PostgreSQL data sources without having to provide client certificates. 

Learn more about connecting to [ MySQL ](https://docs.cloud.google.com/lo/data-studio/nect-to-mysql) and [ PostgreSQL ](https://docs.cloud.google.com/lo/data-studio/nect-to-postgresql) databases. 

####  Report title as scheduled email attachment file name 

Reports sent as scheduled email or downloaded as PDF now use the report name as the attachment and downloaded file name. 

##  February 10, 2022 

###  Product updates 

####  Connect to the new Search Ads 360 

You can now [ connect to the new Search Ads 360 ](https://docs.cloud.google.com/lo/data-studio/nect-to-the-new-search-ads-360). Learn more about what's new in this [ blog post ](https://blog.google/products/marketingplatform/360/introducing-new-search-ads-360/). 

####  Heatmap layer in Google Maps 

You can now visualize your data using a heatmap in a Google Maps chart. [ Learn more about heatmaps ](https://docs.cloud.google.com/lo/data-studio/gle-maps-reference). 

####  Improved page navigation in embedded reports 

You can now navigate through multipage [ embedded reports ](https://docs.cloud.google.com/lo/data-studio/ed-a-report) as you can non-embedded reports. Previously, page navigation only appeared at the bottom of the embedded report. 

To turn this feature on: 

  1. Edit your embedded report. 
  2. Select **File > Embed report **. 
  3. Turn on **Show report navigation in embedded mode**. 



[ Learn more about page navigation ](https://docs.cloud.google.com/lo/data-studio/-pages-and-report-navigation). 

####  More control over BigQuery data freshness 

You can customize the data refresh rate for BigQuery data sources. Custom refresh lets you choose from increments of 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50 minutes, and from 1 to 12 hours. [ Learn more about data freshness ](https://docs.cloud.google.com/lo/data-studio/age-data-freshness). 

##  January 27, 2022 

###  Product updates 

####  Page navigation in edit mode 

Use the **View > Show navigation in edit mode ** menu option to enable rich page navigation while editing your reports as well as when viewing them. Learn more about [ adding pages and report navigation ](https://docs.cloud.google.com/lo/data-studio/-pages-and-report-navigation). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
