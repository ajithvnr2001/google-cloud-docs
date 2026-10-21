---
url: https://docs.cloud.google.com/data-studio/copy-a-report/
title: Copy a report \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:16:25.228176+00:00
---

# Copy a report  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/copy-a-report/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Copy a report Stay organized with collections  Save and categorize content based on your preferences. 

You can duplicate any report to which you have access, unless the owner has specifically disabled this in the sharing options.

## How copying a report works

When you copy a report, the copy inherits the following from the original:

  * pages
  * charts
  * date range controls
  * filter controls
  * data and style settings (e.g. colors, fonts, decimal precision, etc.)
  * text, shapes, and images
  * Google Analytics segments
  * filters



Copying a report does **not** create copies of its data sources. When you copy a report, you must select which data source(s) to use for the copy. If you have at least view access to the original data sources, you can use those; otherwise, you must select new data sources to use.

You can add your own data sources to any reports you copy. Any report can be used as a template.

If you add a data source that doesn't match the schema of the original data source, the charts and controls on the report may break (since they won't have access to the dimensions and metrics they were built on.) Your selection of data source may impact filters and Google Analytics segments. Refer to the related resources section for more information.

Copying a report does NOT copy the Google Analytics measurement ID, if present. You must supply a new measurement ID for the copy.

## To copy a report

  1. View the report.

  2. In the top right, click more_vert and then click content_copy **Make a copy**.

  3. Select the data source(s) to use in the copy.

> The **Create new report** menu lists the original data sources added to the template on the left. On the right, you can choose the data sources to use in your copied report. If the original data source has been shared with you, you can use that one. Or you can select one of your own data sources, or even create a new one at this time.

  4. Click **CREATE REPORT**.




## Copy a report with 'unknown' data sources

When you copy a report that uses a data source that has not been shared with you, you must select a different data source to use. These non-shared data sources appear as **Unknown** in the data source selection dialog.

## Related resources

  * [Share reports](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports)
  * [Reuse and copy filters](https://docs.cloud.google.com/data-studio/create-edit-and-manage-filter-properties)
  * [Copy reports and components with segments](https://docs.cloud.google.com/data-studio/deprecated-use-universal-analytics-segments)
  * [Copy a data source](https://docs.cloud.google.com/data-studio/copy-a-data-source)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
