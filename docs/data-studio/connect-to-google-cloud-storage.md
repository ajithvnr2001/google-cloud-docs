---
url: https://docs.cloud.google.com/data-studio/connect-to-google-cloud-storage/
title: Connect to Cloud Storage \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:32.854248+00:00
---

# Connect to Cloud Storage  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-google-cloud-storage/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Storage offers world-wide storage and retrieval of any amount of data. Cloud Storage combines the performance and scalability of Google's cloud with advanced security and sharing capabilities. The Google Cloud Storage connector lets you create and share reports and dashboards based on your Cloud Storage data.

## How to connect to Cloud Storage

A Cloud Storage data source can connect to a single text file, in CSV format, or to a folder stored in your Google Cloud Storage bucket. If you connect to a folder, Data Studio will try to connect to all the CSV files it finds to populate the data source.

> When connecting to a folder, be sure that all the text files in that folder share the same structure (schema). Trying to connect a data source to files with different structures will cause an error.

### Connecting to Cloud Storage

To connect to Cloud Storage, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click ![The Create icon.](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.
  3. Select the **Google Cloud Storage** connector from the list
  4. If prompted, **AUTHORIZE** access to your data.
  5. Enter the path to your data: 
     1. Include the bucket name and any parent folders
     2. **To select a single file** , enter the filename
     3. **To select multiple files** , enter the final folder name and select **Use all files in path** option
  6. In the upper right, click **CONNECT**. 
     1. The data source fields panel appears.
     2. The data source is now connected to your [dataset](https://docs.cloud.google.com/data-studio/dataset).



## Configure the data source

The data source fields panel is where you configure the data source by renaming fields and adding descriptions, adding calculated fields, and changing data types and aggregations. Learn more about [working with data source fields](https://docs.cloud.google.com/data-studio/model-your-data).

## Control who sees the data

At the top of the fields panel, you can change the data credentials. Credentials control who can see the data that this data source provides.

**OWNER'S CREDENTIALS** let other people view or create reports that use this data without requiring them to have their own access to the dataset.

**VIEWER'S CREDENTIALS** , on the other hand, require each user of the data source to provide their own credentials to access the dataset.

**SERVICE ACCOUNT CREDENTIALS** rely on a special type of Google Account that represents a non-human user that can authenticate and be authorized to access data.

[Learn more about data credentials](https://docs.cloud.google.com/data-studio/data-credentials-article).

## Create a new report from the data source

To create a new report from the data source, follow these steps:

  1. In the upper right, click **CREATE REPORT**. The report editor appears.
  2. Click **ADD TO REPORT**. 
     1. This action adds the data source to the report.
     2. You can now create charts and controls that get their data from this data source.



### New to Data Studio?

Take the [Create a report tutorial](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report).

## Update the data

If you add new data to the files, or add new files to the folder, that data is automatically available in the data source. This ensures that your reports are always up to date, subject to the [data freshness](https://docs.cloud.google.com/data-studio/manage-data-freshness) settings of the data source.

## File format

You should be sure that the files you connect to are properly named and formatted. Otherwise, errors might occur, or your data may not look right in your reports.

[Learn more about Cloud Storage Objects](https://docs.cloud.google.com/storage/docs/objects#naming).

Probably the most common cause of content errors is improper use of separators, quote marks and line break characters in the data. Understanding how Data Studio handles these can save you trouble down the road.

### Only tabular data

The Cloud Storage connector can only handle files of tabular data in CSV format. This means your files must have a regular structure of properly separated rows and columns. Each row must have the same number of columns, even if data is missing for a particular cell in the table. Trying to connect to a file with merged cells, or an inconsistent structure will fail with an error.

**Important:** Every file you connect to for a given data source must have exactly the same structure, with the same fields in the same order.

If you need to add or delete fields in an existing data source, you must delete all the previously uploaded files before connecting to files with the new structure. (Or create a new data source using the new file structure.)

### Separators

All the fields in your data must be separated from each other by commas.

If there are commas within the actual data in a field, that field must be surrounded by quotes. If your data includes double quotes, you can use a single quote character to surround the field.

### Header row

The first line in your file must be a header row. This row will tell Data Studio how to name your fields. Field names must be unique, so you can't have duplicate values in your header row. The header row must also follow the rules mentioned in the separators section.

### Line breaks

Each line in the file must end with a line break. The Cloud Storage connector does not support line breaks in your data even if these are escaped by quotes.

## Limit of the Cloud Storage connector

The Google Cloud Storage connector is limited to a file size of 100 MB per data source.

## Troubleshooting

See the [Data Studio troubleshooting guide](https://docs.cloud.google.com/data-studio/troubleshooting-guide) for a list of common error messages and steps to resolve them.

## Related resources

  * [Google Cloud Storage](https://cloud.google.com/storage/)
  * [About data sources](https://docs.cloud.google.com/data-studio/about-data-sources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
