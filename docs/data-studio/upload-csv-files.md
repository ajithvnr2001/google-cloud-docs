---
url: https://docs.cloud.google.com/data-studio/upload-csv-files/
title: Upload CSV files to Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:52.743553+00:00
---

# Upload CSV files to Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/upload-csv-files/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Upload CSV files to Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

You can bring data into Data Studio from almost any source by uploading CSV (comma-separated values) files. File upload lets you report on data not supported by a specific connector.

## How file upload works

When you upload a file, you add that file to a "dataset." You can then create a data source based on that dataset.

**Note:** Uploading data to Data Studio using file upload is free.

The datasets that you create belong to you and are not shareable; however, the data sources you create that are based on your datasets can be shared and edited like any other. This means that your datasets can be used in shared data sources and reports, but only you can access the dataset itself.

You can upload multiple files to a dataset. When you add new files, that data gets appended to the dataset.

**Note:** Uploaded data is appended (added) to existing data, not merged with it. You should take care to avoid uploading duplicate records if this would cause inaccuracies in your reports.

Your uploaded data is stored in Cloud Storage. There are many benefits to this including the ability to access and download your data from the cloud, and to use other Google Cloud services with your data.

[Learn more about Cloud Storage](https://docs.cloud.google.com/storage/docs).

## Create a CSV file data source

**Important:** This feature is being released gradually. You might not see it right away.

Data Studio stores uploaded CSV files in datasets. A dataset can contain one or more CSV files with the same column headers. A CSV file data source can contain one or more datasets.

To create a new CSV file data source, follow these steps:

  1. Sign in to Data Studio.
  2. Click the **Create** button and then select **Data source**.
  3. Select the **CSV file upload** Google connector.
  4. Create a new dataset by clicking the **Add data set** button. 
     * You can also drag one or more CSV files to the **Available data sets** section, and Data Studio will create a new dataset that contains the uploaded files.
  5. When you have finished uploading files, click the **Connect** button.



Your uploaded data is stored in Cloud Storage. There are many benefits to this storage setup, including both the ability to access and download your data from the cloud and the ability to use other Google Cloud services with your data.

[Learn more about Cloud Storage](https://docs.cloud.google.com/storage/docs).

## Add CSV files to a dataset

**Important:** This feature is being released gradually. You might not see it right away.

You can upload multiple files to a dataset, as long as the column headers match. When you add new files, that data gets appended to the dataset. This lets you update your data as time goes on.

To add CSV files to a dataset, follow these steps:

  1. Sign in to Data Studio.
  2. Click the **Data sources** tab.
  3. Select the data source that contains your CSV files.
  4. Click **Edit Connection**.
  5. From the **Available data sets** section, select the dataset from which you'd like to add files.
  6. Click the **Add file** button. 
     * You can also drag one or more CSV files to the **Files in the data set** section.
  7. Once you have finished uploading files, click the **Reconnect** button.

**Note:** Uploaded data is appended (added) to existing data, not merged with it. Data Studio does not remove duplicate records that may be shared across your CSV files.

## Sharing datasets

The datasets that you create belong to you and are not shareable. However, once you create a data source that is based on your dataset, you can [share that data source](https://docs.cloud.google.com/data-studio/share-reusable-data-sources) with other users. This means that your datasets can be used in shared data sources and reports, but only you can access the dataset itself.

## Upload file format

You should be sure that the files you upload are correctly formatted. Otherwise, errors might occur during the upload, or your data may not look right in your reports.

Probably the most common cause of content errors is improper use of separators, quotation marks, and line break characters in the uploaded data. Understanding how file upload handles these can save you trouble in the future.

### UTF-8 encoding

Your upload file should be in UTF-8 encoding. This is a standard encoding for most applications on the web.

However, if you are exporting data from certain desktop products, such as Microsoft Excel, you may need to convert your file to UTF-8 before you upload it with Data Studio. Otherwise, Data Studio may return an error message such as `Invalid characters in the file. Only UTF-8 encoded characters are supported.`

### Only tabular data

File upload can only import files of tabular data. This means your files must have a regular structure of rows and columns. Each row must have the same number of columns, even if data is missing for a particular cell in the table. Trying to upload a file with merged cells, or an inconsistent structure will fail with an upload error.

**Important:** Every file that you upload to a given dataset must have exactly the same structure, with the same fields in the same order.

If you need to add or delete fields in an existing dataset, you must delete all the previously uploaded files before uploading files with the new structure. (Or create a new dataset using the new file structure.)

### Separators

All the fields in your data must be separated from each other by commas.

If there are commas within the actual data in a field you want to upload, that field must be surrounded by quotes. If your data includes double quotes, you can use a single quote character to surround the field.

### Header row

The first line in your file must be a header row. This row will tell Data Studio how to name your fields. Field names must be unique, so you can't have duplicate values in your header row.

Column names must:

  * Contain only letters, numbers, or underscores. Other punctuation or special characters are not allowed.
  * Start with a letter or underscore
  * Be at most 128 characters long



The header row must also follow the rules for separators.

### Line breaks

Each line in the file must end with a line break. File upload does not support line breaks in your data even if these are escaped by quotes.

## Troubleshooting

The following sections describe common errors that you may see while uploading CSV files.

### Error: File is Invalid

If Data Studio displays the error `File is Invalid` after attempting to upload a CSV file, check for the following possible causes:

  * The file contains invalid UTF-8 characters.
  * The file is not actually a CSV file. For example, if you rename a PDF file to use the ".csv" extension, then Data Studio won't be able to properly parse the file.



## Limits of file upload

File upload is subject to the following limits:

  * 1000 datasets per user
  * 2GB total storage per user
  * 100 uploads per dataset per day
  * 100MB file size limit per dataset



## Related resources

[About data sources](https://docs.cloud.google.com/data-studio/about-data-sources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
