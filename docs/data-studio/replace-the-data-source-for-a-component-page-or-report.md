---
url: https://docs.cloud.google.com/data-studio/replace-the-data-source-for-a-component-page-or-report/
title: Replace the data source for a component, page, or report \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:26.571803+00:00
---

# Replace the data source for a component, page, or report  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/replace-the-data-source-for-a-component-page-or-report/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Replace the data source for a component, page, or report Stay organized with collections  Save and categorize content based on your preferences. 

You can replace the data source for selected charts and controls, the current page, or the entire report. Reasons you might want to do this include:

  * Copying a report and replacing your data source with a client's data source. 
    * See also: [Add a data control to a report](https://docs.cloud.google.com/data-studio/data-control).
  * Testing a report with no email filters applied, then switching to a data source with email filtering.
  * Switching the data source for a selected component from one account, sheet, or database table to another.
  * Overriding the default page or report-level data source.



## What happens when you replace a data source

When you replace a data source in your report, Data Studio tries to map the fields in the old data source to the fields in the new data source based on a number of matching criteria, including field ID, field name, and other configuration information from the report itself. Data Studio won't try to map your old fields in calculated fields and filters.

If no suitable match is found, your report may display components with the following message:

`Important: Chart configuration incomplete. Invalid/Missing dimensions, metrics, filters.`

To fix this, edit the incomplete components and select new dimension, metric, sorting, or date range fields.

**Warning:** We strongly recommend that you review your entire report for accuracy after you replace any data sources that are used in the report.

## Replace a component data source

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select one or more charts or controls.
  3. In the selected component's **Properties** panel, select the **Setup** tab.
  4. In the **Data source** section, click the current data source name.
  5. Select an existing data source from the options that are listed, or click **\+ Add data** to add a new data source. 
     1. Learn more about [creating a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report).
  6. If prompted, click **Add to report.**



Replacing the data source for one component has no effect on the other components in your report.

## Replace a page or report-level data source

Most reports won't have page or report-level data sources unless you've explicitly set them. Setting a data source at the page or report level has **no effect on existing components** in your report. Instead, **new** **components** that you add use the page or report-level data source by default.

Replacing a page or report-level data source follows the same process as outlined previously.

### Replace the data source for the current page

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Navigate to a specific page.
  3. In the top navigation, first select **Page** and then select **Current page settings** to open the **Current Page Settings** panel.
  4. In the **Current Page Settings** panel, select the **Setup** tab, and then click the current data source (or **Select Data Source** , if no data source has been added).
  5. Select an existing data source or create a new one.
  6. If prompted, click **Add to report.**



### Replace the data source for the entire report

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the top navigation, select **File** and then select **Report settings** to open the **Report Settings** panel.
  3. In the **Report Settings** panel, click the current data source (or **Select Data Source** , if no data source has been added).
  4. Select an existing data source or create a new one.
  5. If prompted, click **Add to report.**



## Related resources

[Edit the data source connection.](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
