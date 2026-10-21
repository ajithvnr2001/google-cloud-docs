---
url: https://docs.cloud.google.com/looker/docs/create-view-edit-reports/
title: Create, view, and edit Looker reports \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:24:13.793031+00:00
---

# Create, view, and edit Looker reports  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/create-view-edit-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Create, view, and edit Looker reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

The Looker reports feature lets you create, view, and edit Data Studio reports in your Looker instance, including both governed and ad hoc data. You can share and manage your reports in Looker folders and see your recent reports and the reports that you have marked as favorites from the Looker **Home** page.

## Before you begin

To use Looker reports, your Looker instance must meet all [requirements](https://docs.cloud.google.com/looker/docs/enabling-studio-in-looker#requirements_and_limitations) for Looker reports, and your Looker admin must [enable Looker reports](https://docs.cloud.google.com/looker/docs/enabling-looker-reports#enabling).

You may also need to grant your users permissions to interact with Looker reports features. See the [Overview of permissions for Looker reports documentation page](https://docs.cloud.google.com/looker/docs/overview-of-permissions-for-looker-reports) for more information about Looker reports permissions.

## Accessing Looker reports

You can access Looker reports in the following ways, depending on the [permissions](https://docs.cloud.google.com/looker/docs/overview-of-permissions-for-looker-reports) that your instance admin has granted you:

  * From the Looker main navigation panel
  * From an Explore page
  * From a previously created or shared report
  * From Looker search



### From the Looker main navigation panel

In the Looker main navigation panel, click the **Create** button, and then select the **Report** menu item to open the Looker reports editor tool, where you can create a new Looker report.

**Note:** You must have the [`save_dashboards`](https://docs.cloud.google.com/looker/docs/overview-of-permissions-for-looker-reports#save_dashboards) permission to save or edit reports.

![The Create Report button in the Looker left navigation panel.](https://docs.cloud.google.com/static/looker/docs/images/looker-main-nav-create-report-2412.png)

### From an Explore page

From a [Looker Explore page](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#explores_are_the_starting_point_for_exploration), you can open a Looker report.

**Note:** You must have the [`explore`](https://docs.cloud.google.com/looker/docs/overview-of-permissions-for-looker-reports#explore) permission to view Looker Explores and open a report from an Explore.

#### Create a new Looker report

Click the **Create report from fields** button to open the Looker report editor tool, where you can create a new Looker report.

### From a previously created or shared report

If you have previously created any Looker reports, or if another user has shared a report with you, you will see the report in the folder where it was saved, under the **Reports** section. You can also access these reports from Looker search.

**Note:** You must have the [`see_user_dashboards`](https://docs.cloud.google.com/looker/docs/overview-of-permissions-for-looker-reports#see_user_dashboards) permission to view reports.

For more information about saving, moving, copying, and sharing Looker reports, see the [Move, share, and copy reports](https://docs.cloud.google.com/looker/docs/move-share-copy-reports) documentation page.

### From Looker search

You can use [Looker search](https://docs.cloud.google.com/looker/docs/finding-content#searching_for_saved_content) to find Looker reports that you created or that other users have shared with you.

**Note:** Your Looker instance must be running Looker 25.4 or later to find Looker reports.

To search for a report, follow these steps:

  1. Place your cursor in the search **Start typing to search** search input box in the application header. If the application window is narrow, the input box will be replaced by a search **Search** icon.
  2. Enter your search term.
  3. In the **Reports** section of the search results, Looker displays a list of matching reports that you can access. Looker also displays the name of the report's parent folder next to the report name.
  4. Optionally, to view additional search results, click **Show More**.
  5. Select a report from the search results to view that report.



## Using Looker reports

Looker reports have most of the features of Data Studio. This section presents a list of links for common tasks that will take you to the Data Studio documentation for those tasks.

**Note:** For a list of Data Studio features that are and that are not supported by Looker reports, see the [Feature availability in Looker reports](https://docs.cloud.google.com/looker/docs/report-feature-availability) documentation page.

Before you can get started creating or editing reports, you may need to [use the Looker connector to connect to a Looker Explore](https://docs.cloud.google.com/looker/docs/studio/connect-to-looker) as a Data Studio data source. You may also need to grant your users permissions to interact with Looker reports features. See the [Overview of permissions for Looker reports documentation page](https://docs.cloud.google.com/looker/docs/overview-of-permissions-for-looker-reports) for more information about Looker reports permissions.

The following is a list of Data Studio documentation pages for common tasks:

  * [Quick start guide](https://docs.cloud.google.com/looker/docs/studio/quick-start-guide)
  * [A typical Data Studio workflow](https://docs.cloud.google.com/looker/docs/studio/a-typical-looker-studio-workflow)
  * [Create a report](https://docs.cloud.google.com/looker/docs/studio/create-a-report)
  * [Edit a report](https://docs.cloud.google.com/looker/docs/studio/edit-a-report)
  * [Add data to a report](https://docs.cloud.google.com/looker/docs/studio/add-data-to-a-report)
  * [Add charts and controls to your report](https://docs.cloud.google.com/looker/docs/studio/add-charts-and-controls-to-your-report)
  * [Rename reports, data sources, and blends](https://docs.cloud.google.com/looker/docs/studio/rename-reports-data-sources-and-blends)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
