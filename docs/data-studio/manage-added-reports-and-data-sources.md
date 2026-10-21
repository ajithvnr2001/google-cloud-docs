---
url: https://docs.cloud.google.com/data-studio/manage-added-reports-and-data-sources/
title: Manage added reports and data sources \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:26.503469+00:00
---

# Manage added reports and data sources  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/manage-added-reports-and-data-sources/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Manage added reports and data sources Stay organized with collections  Save and categorize content based on your preferences. 

In Data Studio, you can manage connections between reports and data sources. You can view, edit, add, or remove data sources in a report, or you can review all reports that connect to a specific data source.

## Manage added data sources

Control the data that appears in your Data Studio reports by managing added data sources. You can view, edit, remove, or add new data connections to ensure that your reports use the correct data. You might do this to update credentials, resolve connection issues, or define exactly what data is available in your reports.

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select **Resources** arrow_forward_ios **Manage added data sources**.



You'll see the following information:

### Type

**Embedded** data sources are part of the report and can only be used in the report in which they were created. You can edit the data source from within the report. If you share or copy the report, all of its embedded data sources are shared and copied, as well. [Learn more](https://docs.cloud.google.com/data-studio/embedded-data-sources).

**Reusable** data sources exist as separate assets and can be used in multiple reports. You can edit a reusable data source from within the report, or from the Data Studio home page.

### Used in report

Shows the number of charts using each data source.

### Status

Shows whether the data source is working properly or if there is a problem with the data source connection.

#### Problems with the connection

If you see problems with the data source connection, it may mean that the report-data source claim has been broken. Charts based on this data source will display the message "Failed To Get Data. The data source needs to be added to the report."

This can happen when the person who added the data source to the report leaves your organization, or has their permission to access the data source removed. In this case, someone else with permission to access that data source needs to add it back before those charts will work again. If you have this permission, you'll see a link to request access.

### Edit

Click this link to edit the data source. For a reusable data source, you must have edit access to that data source.

### Remove

If you added the data source to the report, you can remove it and release your claim to that data source. Any components that used that data source will show an alert instead of data.

To fix any broken charts or controls, you can:

  * Add the data source back to the report.
  * Select a different data source for the affected charts or controls.
  * Delete the affected charts or controls.



Note that changing a component to use a different data source does not remove the original one from the report.

**Note:** Removing an embedded data source disconnects it from the report but doesn't permanently delete the data source. Data Studio permanently deletes embedded data sources only when you permanently delete the parent report. To permanently delete an embedded data source without deleting the report, you can [convert the embedded data source to a reusable data source](https://docs.cloud.google.com/data-studio/embedded-data-sources#delete-an-embedded-data-source) and then delete it.

### Add a data source

Click **ADD A DATA SOURCE**.

  1. To create a new data source: 
     1. The **Connect to data** tab lets you select a [connector](https://docs.cloud.google.com/data-studio/connector), create a new data source, and add that to your report: 
        1. Select the type of data you want to visualize.
        2. Provide your account or other details.
        3. In the bottom right, click **Add**.
  2. The **My data sources** tab lets you add an existing [data source](https://docs.cloud.google.com/data-studio/data-source) to your report: 
     1. Locate the data source you want.
     2. In the bottom right, click **Add.**



## Manage added reports

To see the reports which use a particular data source:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Navigate to the [**Data sources**](https://datastudio.google.com/navigation/datasources) tab.
  3. Locate the data source that you want to manage, and then click more_vert **More option**.
  4. Click **Manage Added Reports**.



![The Manage added reports menu displays the information Report \[name\], Status, Action, and a Remove icon for each report that uses the data source.](https://docs.cloud.google.com/static/data-studio/images/manage-added-reports-2019-06-20.png)

  * **Status** shows if the data source has been added properly. If not, an alert icon will appear.
  * **Used in report** shows if there are charts or controls that reference the data source. This can help you make sure it's safe to remove a data source
  * Add a data source back to the report by clicking **Add** in the Action column.
  * Remove a data source from the report by clicking remove_circle_outline **Remove report from datasource**.



## Related resources

  * [Add data to a report](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Edit a data source](https://docs.cloud.google.com/data-studio/edit-a-data-source)
  * [Change the data source for a chart, page, or report](https://docs.cloud.google.com/data-studio/replace-the-data-source-for-a-component-page-or-report)
  * [Remove and restore a data source](https://docs.cloud.google.com/data-studio/delete-a-data-source)
  * [Embedded data sources](https://docs.cloud.google.com/data-studio/embedded-data-sources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
