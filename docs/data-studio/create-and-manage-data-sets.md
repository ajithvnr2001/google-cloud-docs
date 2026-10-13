---
url: https://docs.cloud.google.com/data-studio/create-and-manage-data-sets/
title: Create and manage data sets \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:42.656902+00:00
---

# Create and manage data sets  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-and-manage-data-sets/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create and manage data sets Stay organized with collections  Save and categorize content based on your preferences. 

A data set in the context of file upload is a collection of files with the same structure. Once a file upload data set exists in Data Studio, you can connect to it and create data sources that use that data, just as you would with other types of data.

## Create a data set

To create a data set, create a new File Upload data source and add a file to it:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click ![The Create icon.](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.
  3. Choose **File Upload** in the Connectors panel.
  4. Drag one or more files from your computer to the upload target, or click **UPLOAD FILES** and select the files you want.



Your files will be added to the data set.

> It may take some time to process your files. During this time, you can still add more data or create new sets.

## Edit a data set

There are two ways to edit a data set: by editing the connection of a data source based on the data set, or by going through the connectors panel.

### Edit the data source connection

  1. [Sign in to Data Studio.](https://datastudio.google.com) After signing in, you'll see the _Home_ page.
  2. Click the [DATA SOURCES](https://datastudio.google.com/navigation/datasources) tab.
  3. Click a data source that uses the data set you want to edit.
  4. Click EDIT CONNECTION in the upper left.



### Use the connectors panel

  1. [Sign in to Data Studio.](https://datastudio.google.com) After signing in, you'll see the _Home_ page.
  2. Click the [DATA SOURCES](https://datastudio.google.com/navigation/datasources) tab.
  3. Click ![Create new report or data source.](https://docs.cloud.google.com/static/data-studio/images/create-new-icon-2015-09-17.png).
  4. Choose **File Upload** in the Connectors panel.
  5. Click the data set you want to edit.



## Add data to a data set

You can add more files to a data set at any time. Edit the data set and click **ADD FILES**. Then, select one or more files to upload. There is no need to click RECONNECT. Any data sources that use the data set will automatically be able to access the new data.

**Warning:**

Adding data to a dataset appends it to the data set, as opposed to merging it. In other words, if you upload duplicate records, both records will appear in your data.

Every file you upload to a given data set must have exactly the same structure, with the same fields in the same order.

## Delete an upload file

Deleting an upload file removes its data from the data set. You can't undo this (though you can upload the same file again, if needed).

  1. Edit the data set.
  2. Mouse over the file you want to delete.
  3. Click the trash icon appears on the right.



## Rename a data set

When you first create a data set, it gets named using the name of the first file uploaded. To rename a data set:

  1. Edit the data set you want to rename.
  2. Click the current name in the files panel and enter a new name.



## Delete a data set

Deleting a data set permanently removes all the uploaded files.

  1. Edit the data set you want to delete.
  2. Click **DELETE DATA SET** at the bottom of the file list.

**Important:** Deleting a data set cannot be undone. 

## Fix upload errors

If your upload file has errors, Data Studio will display an error in the Status column of the file list. Click ERROR to display the actual problem found. Almost all these errors will be due to unexpected formatting in the uploaded file.

Learn more about [upload file format](https://docs.cloud.google.com/data-studio/upload-csv-files).

## Use an existing data set in a new data source

You can reuse data sets in any number of data sources.

  1. Create a new data source.
  2. Select **File Upload** in the _Connectors_ panel.
  3. Select an existing data set.
  4. Click **CONNECT** in the upper right.



## Change the data set for an existing data source

You can connect an existing data source to a different data set.

  1. Edit the data source connection.
  2. Select a new data set from the data sets list or create a new data set.
  3. Click **RECONNECT.**

**Important:** The new data set must match the structure of the previous data set, or your charts may break. 

## Access your data in Google Cloud Storage

All the data you upload via Data Studio is stored in Google Cloud Storage. You can access all your uploaded data there, as well as use other cloud services with the data. To access your data in the cloud:

  1. Edit a data set.
  2. Click **VIEW FILES IN CLOUD**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
