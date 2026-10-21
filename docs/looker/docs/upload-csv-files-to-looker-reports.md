---
url: https://docs.cloud.google.com/looker/docs/upload-csv-files-to-looker-reports/
title: Upload CSV files to Looker reports \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:18:06.408719+00:00
---

# Upload CSV files to Looker reports  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/upload-csv-files-to-looker-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Upload CSV files to Looker reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

**Note:** For information about uploading CSV files to Data Studio, see [Upload CSV files to Data Studio](https://docs.cloud.google.com/looker/docs/studio/upload-csv-files-to-looker-studio).

You can bring data into Looker reports from any source that provides CSV (comma-separated values) files. You can upload CSV files directly from your computer.

**Note:** Uploading data to Looker reports using CSV file upload is free.

## Create a CSV file data source

Looker reports store uploaded CSV files in data sets. A data set can contain one or more CSV files with the same column headers. A CSV file data source can contain one or more data sets.

To create a new CSV file data source, follow these steps:

  1. Open a Looker report.
  2. Click the **Create** button and then select **Data source**.
  3. Select the **CSV file upload** Google connector.
  4. Create a new data set by clicking the **Add data set** button. 
     * You can also drag one or more CSV files to the **Available data sets** section, and the Looker report will create a new data set that contains the uploaded files.
  5. When you have finished uploading files, click the **Connect** button.



Your uploaded data is stored in Cloud Storage. There are many benefits to this storage setup, including both the ability to access and download your data from the cloud and the ability to use other Google Cloud services with your data.

[Learn more about Cloud Storage](https://docs.cloud.google.com/storage/docs).

## Add CSV files to a data set

You can upload multiple files to a data set, as long as the column headers match. When you add new files, that data gets appended to the data set. This lets you update your data as time goes on.

To add CSV files to a data set, follow these steps:

  1. Open a Looker report.
  2. Click the **Data sources** tab.
  3. Select the data source that contains your CSV files.
  4. Click **Edit Connection**.
  5. From the **Available data sets** section, select the data set from which you'd like to add files.
  6. Click the **Add file** button. 
     * You can also drag one or more CSV files to the **Files in the data set** section.
  7. Once you have finished uploading files, click the **Reconnect** button.

**Note:** Uploaded data is appended (added) to existing data, not merged with it. The Looker report does not remove duplicate records that may be shared across your CSV files.

## Sharing data sets

The data sets that you create belong to you and are not shareable. However, once you create a data source that is based on your data set, you can [share that data source](https://docs.cloud.google.com/looker/docs/studio/share-reusable-data-sources) with other users. This means that your data sets can be used in shared data sources and reports, but only you can access the data set itself.

## Upload file format

Confirm that the files you upload are correctly formatted. Otherwise, errors might occur during the upload, or your data may not look right in your reports.

A common cause of content errors is the improper use of separators, quotation marks, and line break characters in the uploaded data. Understanding how CSV file upload handles these can save you trouble in the future.

### UTF-8 encoding

Your upload file should be in UTF-8 encoding. This is a standard encoding for most applications on the web.

However, if you are exporting data from certain desktop products, such as Microsoft Excel™, you may need to convert your file to UTF-8 before you upload it to a Looker report. Otherwise, the Looker report may return an error message such as `File is Invalid.`

### Only tabular data

CSV file upload can only import files of tabular data. This means that your files must have a regular structure of rows and columns. Each row must have the same number of columns, even if data is missing for a particular cell in the table. Trying to upload a file with merged cells, or an inconsistent structure, will fail with an upload error.

**Important:** Every file you upload to a given data set must have exactly the same structure, with the same fields in the same order.

If you need to add or delete fields in an existing data set, you must delete all the previously uploaded files before uploading files with the new structure. (Or create a new data set using the new file structure.)

### Separators

All the fields in your data must be separated from each other by commas.

If there are commas within the actual data in a field you want to upload, that field must be surrounded by quotes. If your data includes double quotes, you can use a single quote character to surround the field.

### Header row

The first line in your file must be a header row. This row will tell the Looker report how to name your fields. Field names must be unique, so you can't have duplicate values in your header row.

Column names must:

  * Contain only letters, numbers, or underscores. Other punctuation or special characters are not allowed.
  * Start with a letter or underscore
  * Be at most 128 characters long



The header row must also follow the rules for separators.

### Line breaks

Each line in the file must end with a line break. CSV file upload does not support line breaks in your data even if these are escaped by quotes.

## Troubleshooting

The following sections describe common errors that you may see while uploading CSV files.

### Error: File is Invalid

If Looker displays the error `File is Invalid` after attempting to upload a CSV file, check for the following possible causes:

  * The file contains invalid UTF-8 characters.
  * The file is not actually a CSV file. For example, if you rename a PDF file to use the ".csv" extension, then the Looker report won't be able to properly parse the file.



## Limits of CSV file upload

CSV file upload is subject to the following limits:

  * 1000 data sets per user
  * 2GB total storage per user
  * 100 uploads per data set per day
  * 100MB file size limit per data set



## Related resources

[About data sources](https://docs.cloud.google.com/looker/docs/studio/about-data-sources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
