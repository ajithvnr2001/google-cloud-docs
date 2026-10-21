---
url: https://docs.cloud.google.com/looker/docs/studio/edit-a-data-source-article/
title: Edit a data source \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:10:19.695111+00:00
---

# Edit a data source  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/studio/edit-a-data-source-article/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Edit a data source Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to edit and configure data sources you, or someone else, has already created. To learn how to create new data sources, see [Add data to a report](https://docs.cloud.google.com/data-studio/add-data-to-a-report).

**Caution:** When you edit a reusable data source (for example, by hiding fields, changing field types, or removing fields), the changes affect every report that uses that data source. If you hide a field that is used in another report, charts in that report break and display an **Invalid Dimensions** or **Invalid Metric** error. 

## How to edit a data source

To edit an embedded data source, [edit the report](https://docs.cloud.google.com/data-studio/edit-a-report) in which it's embedded.

### Edit a data source from within a report

While you're editing a report, you can see all data sources that are used by that report in the **Resources** menu:

  1. Edit your report.
  2. In the menus, select **Resource > Manage added data sources**.
  3. Locate the data source in the list. Then, to the right, click ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit**.



You can also edit the data source for a specific component by following these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a component.
  3. In the **Properties** panel, select the **SETUP** tab.
  4. In the **Data Source** section, edit the data source by clicking ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit**.

**Note:** These methods work for both embedded and reusable data sources.

### Edit a data source from the home page

You can find and edit all your reusable data sources in the Data sources list on the home page by following these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. At the top of the Data Studio home page, click **Data Sources**.
  3. Browse or search for the data source that you want to edit.
  4. Click that data source in the list.

**Note:** Only reusable data sources appear in this list. To edit an embedded data source, follow the steps shown previously.

## About field IDs

Each field in a data source has a unique internal field ID. Data Studio uses field IDs to identify dimensions and metrics in charts and controls. For example, filter controls use field IDs to filter all charts that contain that field ID.

You can't edit field IDs in the data source editor. This limitation prevents breaking other reports that might use the same data source. However, you can override field IDs at the report level. This is useful if you want a filter control to work across charts that use different data sources. Learn more about [managing field names and IDs](https://docs.cloud.google.com/data-studio/manage-field-ids).

## Who can edit a data source

To edit a **reusable data source** , you must either be the owner of the data source or have _Can Edit_ access permission to the data source.

To edit an **embedded data source** , you must either be the owner of the report or have _Can Edit_ access permission to the report.

## What you can edit

Data source editors can do the following:

  * [Share](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports) the data source
  * [Rename the data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Rename and duplicate fields](https://docs.cloud.google.com/data-studio/create-rename-copy-hide-and-remove-fields)
  * Create [calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields), [custom bins](https://docs.cloud.google.com/data-studio/create-a-custom-bin), and [custom groups](https://docs.cloud.google.com/data-studio/create-a-custom-group)
  * Create [parameters](https://docs.cloud.google.com/data-studio/parameters)
  * Change [field aggregations](https://docs.cloud.google.com/data-studio/model-your-data)
  * Add field descriptions
  * Change [field data types](https://docs.cloud.google.com/data-studio/data-types)
  * [Refresh](https://docs.cloud.google.com/data-studio/refresh-data-source-fields) data source fields
  * [Edit the data source connection](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection)
  * Change the [data credentials](https://docs.cloud.google.com/data-studio/data-credentials-article)
  * Enable [native functions](https://docs.cloud.google.com/data-studio/nativedimension)



If you are the owner of the data source, you can also perform the following tasks:

  * [Remove and restore](https://docs.cloud.google.com/data-studio/delete-a-data-source) the data source
  * [Make someone else the owner](https://docs.cloud.google.com/data-studio/transfer-ownership) of that data source



If you are the owner of the data credentials that are used by the data source, you can also [revoke](https://docs.cloud.google.com/data-studio/data-credentials-article) the data credentials.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
