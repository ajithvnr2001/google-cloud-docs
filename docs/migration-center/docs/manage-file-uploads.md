---
url: https://docs.cloud.google.com/migration-center/docs/manage-file-uploads/
title: Manage file uploads \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:23.320283+00:00
---

# Manage file uploads  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/manage-file-uploads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Manage file uploads Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage your file uploads in Google Cloud Migration Center.

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

## Delete a file import job

You can delete a file import job from the Google Cloud console. Deleting a file import job also reverts all of the changes on the assets done by that file import job.

To delete a file import job, do the following:

  1. In the Google Cloud console, go to the **Data import** page.

[Go to Data import](https://console.cloud.google.com/migration/discovery/dataImport)

  2. In the **File uploads** tab, select the file import job that you want to delete, then click **Delete**.

  3. In the confirmation dialog, click **Confirm**.




## What's next

  * Learn more about [Migration Center collection methods](https://docs.cloud.google.com/migration-center/docs/start-asset-discovery#collection_methods).
  * Learn more about [automatic data collection with discovery client](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
