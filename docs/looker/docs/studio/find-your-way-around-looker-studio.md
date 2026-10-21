---
url: https://docs.cloud.google.com/looker/docs/studio/find-your-way-around-looker-studio/
title: Quick start guide \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:38:50.911040+00:00
---

# Quick start guide  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/studio/find-your-way-around-looker-studio/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Quick start guide Stay organized with collections  Save and categorize content based on your preferences. 

This page explains six key steps that can help you to quickly get started using Data Studio.

**Note:** Data Studio is a flexible tool: There are often multiple ways to achieve the same results. The workflow described here is just a basic example that shows data from different sources. Your results may look different from what's shown here.

## ![](https://docs.cloud.google.com/static/data-studio/images/1-large-10-17-2014-image.png) Start with a report

[Reports](https://docs.cloud.google.com/data-studio/report) let you visualize your data, gain insights, and share those insights with others.

When you sign in to [Data Studio](https://datastudio.google.com), the home page appears with the **Reports** tab selected. All the [reports](https://docs.cloud.google.com/data-studio/report) that you have access to appear in the reports list. Use the plus buttons to create a new blank report.

![A user selects the + Create button on the Data Studio home page navigation panel to create new content in Data Studio.](https://docs.cloud.google.com/static/data-studio/images/how-to-use-ds-create-report-new-ui.png)

### View a report

To view a report that's been shared with you, click the report name in the reports list.

### Edit a report

To edit a report, follow these steps:

  1. View a report.
  2. In the header, click ![Edit icon](https://docs.cloud.google.com/static/data-studio/images/icmodeeditgrey6002xweb24dp-2016-10-12.png)**Edit**.



If you don't see an **Edit** button, then the report has been shared with only **Can view** access. If the owner of the report has allowed it, you can [make a copy](https://docs.cloud.google.com/data-studio/copy-a-report), which you can then edit.

### Create a report

To create a report, follow these steps:

  1. In the navigation panel, click ![The Create icon.](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create**.
  2. Select **Report**.



The report editor opens with the **Add data to report** panel open.

## ![](https://docs.cloud.google.com/static/data-studio/images/2-large-2014-10-17-image.png) Add data to the report

[Data sources](https://docs.cloud.google.com/data-studio/data-source) connect to your data and let you configure the [fields](https://docs.cloud.google.com/data-studio/field) that you can use in your report.

When you create a new report, the **Add data to report** panel opens. This panel lets you create a new data source or add an existing data source.

### Create a new data source

For example, you might want to connect to a BigQuery public dataset (to complete this step, you'll need a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) that is associated with a valid [Google Cloud billing account](https://cloud.google.com/billing/docs)).

To create a new BigQuery data source, follow these steps:

  1. In the **Add data to report** panel, click **Connect to data**.
  2. Select the BigQuery [connector](https://docs.cloud.google.com/data-studio/connector).
  3. If prompted, click **Authorize** to allow Data Studio to access your data on your behalf.
  4. Select **Public datasets**.
  5. Select your **Billing project**.
  6. Select the **faa** public dataset.
  7. Select the **us_airports** table.
  8. Click **Add** , and then confirm that you want to add the new data source to your report.
  9. The report editor appears, and a table with fields from your data source is placed on the canvas.
  10. To customize the table's data and style, use the [properties panel](https://docs.cloud.google.com/data-studio/properties-panel).
  11. To rename your report, in the header, click **Untitled report** and enter a new name.



### Connect to an existing data source

For example, you might want to connect to the sample Google Analytics data source that comes with Data Studio.

To connect to an existing Google Analytics dataset, follow these steps:

  1. In the **Add data to report** panel, click **My data sources**.
  2. Select the **Sample Google Analytics Data** data source.
  3. Click **Add** , and then confirm that you want to add the new data source to your report.
  4. The report editor appears, and a table with fields from your data source is placed on the canvas.
  5. To customize the table's data and style, use the [properties panel](https://docs.cloud.google.com/data-studio/properties-panel).
  6. To rename your report, in the header, click **Untitled report** and enter a new name.



![The Add data to report panel has two tabs for finding data to add to reports: Connect to data and My data sources.](https://docs.cloud.google.com/static/data-studio/images/add-data-to-report.png)

## ![](https://docs.cloud.google.com/static/data-studio/images/3-large-2014-10-17-image.png) Add charts and controls to the report

To add [components](https://docs.cloud.google.com/data-studio/component) to a report canvas, follow these steps:

  1. In the toolbar, click **Add a chart** , and then select a chart from the list.
  2. Click the canvas where you want the chart to appear.
  3. Move and resize the chart, as desired.
  4. Add or change the dimensions and metrics by clicking the fields in the properties panel or by dragging and dropping them from the data panel directly onto the chart.
  5. You can also create new charts by dragging a field from the data panel onto the canvas.



## ![](https://docs.cloud.google.com/static/data-studio/images/4-large-2014-10-17-image.png) View your report

See your report the way it looks to other viewers.

View mode lets users see the data and use any interactive controls that you've placed on the report without being able to change the structure of the report. If you can edit a report, you can switch between view mode and edit mode.

To enter view mode from edit mode, click ![Visibility icon](https://docs.cloud.google.com/static/data-studio/images/gmvisibilitygrey60048dp-2020-03-12.png)**View**.

To return to edit mode from view mode, click ![Edit icon.](https://docs.cloud.google.com/static/data-studio/images/gmcreategrey60048dp-2020-03-12.png)**Edit**.

## ![](https://docs.cloud.google.com/static/data-studio/images/5-large-2014-10-17-image.png) Share the report

Share reports with other viewers. Collaborate with other editors.

**Note:** Editors need to sign in to Google to edit a report; however, viewers don't need to be signed in to view a report.

To share a report with users, follow these steps:

  1. In the header, click ![Share icon](https://docs.cloud.google.com/static/data-studio/images/gmpersonaddgrey60048dp-2020-03-12.png)**Share**.
  2. Specify the people or groups with whom you want to share your report.
  3. Use the advanced options to change how individual addresses can access the report.

**Important:** Sharing a report doesn't share its data source. [Data source credentials](https://docs.cloud.google.com/data-studio/data-credentials) determine if a viewer can see the data in your report. If you a share report with others _and_ give them edit access, they can use the fields from that data source in charts, even if the data source itself has not been shared with them.

## ![](https://docs.cloud.google.com/static/data-studio/images/6-large-2014-10-17-image.png) Share the data source

Let other people create their own reports that are based on your data source.

**Note:** If you only want other people to view or edit your reports, you don't need to share the data source.

To share a data source, you must access it directly from the **Data Sources** page (not through the report). You must be signed into a Google Account to view or edit a data source.

To share a data source, follow these steps:

  1. Return to the Data Studio home page by clicking the![Data Studio logo](https://docs.cloud.google.com/static/data-studio/images/looker-studio-logo-svg.svg) Data Studio logo.
  2. In the navigation panel, click **Data Sources**.
  3. Locate the data source that you want to share.
  4. Click ![More](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--more-vertical.png)**More options**.
  5. Click ![Share icon](https://docs.cloud.google.com/static/data-studio/images/gmpersonaddgrey60048dp-2020-03-12.png)**Share**.
  6. Specify the people or groups with whom you want to share your data source.
  7. Use the advanced options to change how individual addressees can access the data source.

**Caution:** Use caution when sharing a data source with edit access. While sharing does not grant access to the underlying data, modifying a data source could cause it to be incompatible with existing charts that use that data source. Sharing a data source with view access lets people create reports without being able to change its structure.

## Key concepts

Here's a recap of the terms and concepts that are used on this page and throughout the Data Studio documentation.

Concept  |  What it does   
---|---  
Report  |  A Data Studio asset that contains a collection of **components** whose purpose is to present to viewers information and insights that are derived from your data.  Learn more [about reports](https://docs.cloud.google.com/data-studio/view-a-report).   
Component  |  A widget that you add to a report to display your data, such as **charts** , **tables** , and interactive**date range controls** and **filter controls**. Data components get their information from a **data source**.  You can also annotate your report with **text** , **shape** , **image** , and [ embedded content ](https://docs.cloud.google.com/data-studio/embed-external-content-in-reports) components.   
Connector / Data source  |  When you connect external data to Data Studio, you manage [connectors](/data-studio/connector), [data sources](/data-studio/data-source), and [credentials](/data-studio/data-credentials). Understanding how these three components work together helps you customize data presentation and securely share reports with your team.  Learn more about [ connecting to your data](https://docs.cloud.google.com/data-studio/about-data-sources).   
Field  |  A column of data.  Data Studio uses two basic types of fields: 

  * **Dimensions** are things that you want to measure, or that serve as ways to categorize your data. 
  * **Metrics** are numbers that measure the things that are contained in dimensions. 

Learn more about [ fields in reports](https://docs.cloud.google.com/data-studio/work-with-fields-in-reports).   
Credentials  |  The mechanism by which a data source determines who can see the data it provides.  Learn more about [ data source credentials](https://docs.cloud.google.com/data-studio/data-credentials).   
View mode / Edit mode  | 

  * **Edit mode** lets you edit the structure of a report and change, add, or remove data sources, and it lets you use interactive controls. 
    * People who can edit a report or data source are referred to as **editors**. 
  * **View mode** lets you see all the data that you are authorized to see, and it lets you use interactive controls. View mode does not allow you to modify the report structure. 
    * People who can only view a report or data source are referred to as **viewers**. 

  
Sharing and access permissions  |  When you share reports and data sources, you determine how other people can access the asset: 

  * **Can edit** access lets people modify and share the asset (making them **editors**). 
  * **Can view** access lets people view the asset, but they can't modify or share it (making them **viewers**). 

The advanced sharing options let you control other aspects of asset access, such as the ability to download the data or print the report.  The link sharing options let you share your assets more broadly around the internet.  Learn more [about sharing](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
