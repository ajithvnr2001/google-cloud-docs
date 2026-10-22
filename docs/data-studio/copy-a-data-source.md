---
url: https://docs.cloud.google.com/data-studio/copy-a-data-source/
title: Copy a data source \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:29.955456+00:00
---

# Copy a data source  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/copy-a-data-source/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Copy a data source Stay organized with collections  Save and categorize content based on your preferences. 

Copying a data source lets you create variations of your reports. For example, you can copy a template report, then attach different versions of the data source, with modified dimensions, metrics, or calculated fields, to support different sets of users. You can also make backup copies of a data source for safe keeping while you experiment.

## Duplicate a data source from within a report

Report editors can copy any embedded data sources in the report. Report editors can also copy reusable data sources if they have edit access to that data source.

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the menus, select **Resource arrow_forward_ios Manage added data sources**.
  3. Locate the data source in the list, then to the right, click content_copy **Duplicate**.
  4. In the data source configuration page, select the dataset for the new data source, then click **RECONNECT.**



If you copy a reusable data source from the **Manage added data sources** page, the new data source is embedded in the report.

## Copy a data source from the home page

You can make a copy of a reusable data source from the home page. You must be the owner of or have edit access to the data source to do this.

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. At the top of the page, click **Data Sources**.
  3. Browse, or use the search box in the upper right, to locate the data source you want to edit.
  4. Click that data source.
  5. In the upper right, click Make a copy content_copy.
  6. In the confirmation dialog, click **COPY DATA SOURCE.**
  7. In the data source configuration page, select the dataset for the new data source, then click **RECONNECT.**



## Field changes

If the new dataset you select for the copy has different fields from the original, you'll see those changed fields listed. You can edit the data source configuration by clicking **GO TO FIELDS**.

Learn more about [refreshing data source fields](https://docs.cloud.google.com/data-studio/refresh-data-source-fields).

## Update data credentials

If the data credentials used by the original data source are owned by another person, you can use your own credentials for the new data source by clicking **UPDATE CREDENTIALS**.

Learn more about [data credentials](https://docs.cloud.google.com/data-studio/data-credentials-article).

## How copying a data source works

When copying a data source, Data Studio tries to make sure you have access to the data by reconnecting to the underlying [dataset](https://docs.cloud.google.com/data-studio/dataset). If access can't be confirmed, you'll see the connectors panel, where you can select the dataset to use. Google Analytics, Google Ads, and file import data sources always require you to explicitly reconnect to the dataset. If the fields in the new dataset don't match the schema of the copied data source, you'll see a message detailing the new fields being added or missing fields being removed.

Whenever possible, the copied data source inherits the following from the original:

  * Dimensions
  * Metrics
  * Calculated fields
  * Field types
  * Aggregations
  * Data source credentials



Things that might prevent the data source from being duplicated exactly include:

  * Selecting a new dataset that doesn't exactly match the original
  * Selecting a new dataset to which you don't have the same access as the original
  * Changes made to the original dataset while the copy is in progress

**Warning:** Copying a data source never grants direct access to the dataset.

Copying a data source does **not** copy any reports that use the data source.

## Disable option to copy a data source

You can prevent other people from copying your data source using the _Advanced > Owner settings_ of the sharing dialog. You must be the owner of the data source to see these settings.

### To prevent a data source from being copied:

  1. Edit the data source.
  2. In the upper right, click person_add **Share**.
  3. Select the **Manage access** tab.
  4. Turn on the **Disable options to download, print, and copy for commenters and viewers** option.
  5. Click **Done**.



## Limits of copying a data source

Copying a data source doesn't copy or validate the actual data. It only duplicates the data source schema. If you connect the data source to a different dataset from the original, it's possible that calculated fields may not return the same results as the original data source. For example, a `REGEX_MATCH` function that works in the original data source might look for data that doesn't exist in the new dataset.

## Related resources

  * [About data sources](https://docs.cloud.google.com/data-studio/about-data-sources)
  * [Copy a report](https://docs.cloud.google.com/data-studio/copy-a-report)
  * [Share a data source](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
