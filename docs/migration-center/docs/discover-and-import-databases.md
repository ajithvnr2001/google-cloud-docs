---
url: https://docs.cloud.google.com/migration-center/docs/discover-and-import-databases/
title: Discover and import databases \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:23.272458+00:00
---

# Discover and import databases  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/discover-and-import-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Discover and import databases Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the database collection scripts to discover, collect, and upload your database data to Migration Center. Migration Center uses [open-source collection scripts available on GitHub](https://github.com/GoogleCloudPlatform/database-assessment) to collect data. To understand the type of data that Migration Center collects, you can review the code of the collection scripts.

## Before you begin

  * The database collection scripts support the following databases and database versions: 
    * Microsoft SQL Server for Windows Versions 2008R2 (SP2) to SQL Server 2022
    * MySQL version 5.6 or later
    * PostgreSQL version 12 or later
  * If you run the collection scripts on Linux, ensure that the `zip` command-line utility is installed. Migration Center requires output data in ZIP format. Without the `zip` utility, the script generates an unsupported `.tar.gz` file.



## Download and run the scripts

To discover and collect data from your databases, follow these steps:

  1. Download the latest collection script archive for your database type:

     * [Download scripts for Microsoft SQL Server](https://github.com/GoogleCloudPlatform/database-assessment/releases/latest/download/db-migration-assessment-collection-scripts-sqlserver.zip).
     * [Download scripts for PostgreSQL](https://github.com/GoogleCloudPlatform/database-assessment/releases/latest/download/db-migration-assessment-collection-scripts-postgres.zip).
     * [Download scripts for MySQL](https://github.com/GoogleCloudPlatform/database-assessment/releases/latest/download/db-migration-assessment-collection-scripts-mysql.zip).
  2. Extract the downloaded archive and open the directory.

  3. Read the `README` file to verify system dependencies and configuration options for your database environment. On Linux, confirm that the `zip` utility is installed.

  4. Run the collection script as described in the `README` file. When the script finishes, it creates a ZIP archive containing the collected data in your selected output directory.




## Upload the collected data to Migration Center

The ZIP files created by the collection scripts contain all the specifications and performance data collected from your database.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `rma.collectors.create` on the project
  * `migrationcenter.sources.create` on the project
  * `migrationcenter.importJobs.create` on the project

  


To upload the ZIP files to Migration Center, follow these steps:

  1. In the Google Cloud console, go to the **Data import** page.

[Go to Data import](https://console.cloud.google.com/migration/discovery/dataImport)

  2. Click **Add data > Upload files**.

  3. In the **Set up file upload** section, enter the name of the file upload.

  4. From the **File format** list, select **Database import file**.

  5. Click **Select files to upload** , then select all the files that you want to upload.

  6. To upload the files, click **Upload files**.

  7. If the files are validated correctly, to create the assets from the files, click **Import data** , then click **Confirm**.




## Review the upload

After you upload your files, Migration Center validates them to check if they are formally correct. If the validation is successful, Migration Center then processes the data to create new assets, or update existing ones. You can check the status of your upload jobs from the Google Cloud console.

To review the status of your upload job, follow these steps:

  1. In the Google Cloud console, go to the **Data import** page.

[Go to Data import](https://console.cloud.google.com/migration/discovery/dataImport)

  2. In the **File uploads** tab, from the list of file imports, click the import job that you want to review.

  3. Review the **Status** for your uploaded files.

You can see your files in one of the following statuses:

     * **Completed**. The import of your file was successful.
     * **Ready**. Your file passed validation, and is ready to be imported.
     * **Pending**. Your file is waiting for another file to finish processing.
     * **Running**. Your file is processing.
     * **Validating**. Your file is in the validation stage.
     * **Failed validation**. Your file contains some errors. Fix the errors and then try to upload your file again.
     * **Failed**. Your file couldn't be imported.



### Review error details

If you encounter errors after importing your files, you can review the error message directly in the Google Cloud console.

To review the errors of your upload job, follow these steps:

  1. In the Google Cloud console, go to the **Data import** page.

[Go to Data import](https://console.cloud.google.com/migration/discovery/dataImport)

  2. In the **File uploads** tab, from the list of file imports, click the import file that shows a warning or error.

The import file details page shows the complete list of errors.




On the import file details page, you can review the assets and data fields that cause the errors, and view a description of the error. Errors in the file import job might prevent Migration Center from creating new assets or update existing ones with the new changes. To fix the error, edit your files and create a new file import job to upload them again.

For more information about the possible error messages, see [Troubleshoot file import errors](https://docs.cloud.google.com/migration-center/docs/troubleshooting/file-import-errors).

## What's next

  * Learn more about [Migration Center collection methods](https://docs.cloud.google.com/migration-center/docs/start-asset-discovery#collection_methods).
  * Learn how to [manage your file uploads](https://docs.cloud.google.com/migration-center/docs/manage-file-uploads).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
