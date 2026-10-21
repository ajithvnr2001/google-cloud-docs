---
url: https://docs.cloud.google.com/assured-workloads/docs/delete-folder/
title: Delete an Assured Workloads folder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:51.618107+00:00
---

# Delete an Assured Workloads folder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/delete-folder/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete an Assured Workloads folder

This page guides you through deleting an Assured Workloads folder and using the Google Cloud console.

**Important:** Before deleting an Assured Workloads folder, make sure that you first delete all projects within the folder.

To delete an Assured Workloads folder, do the following:

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. **Note:** This step is only necessary if you have an [Assured Workloads-created customer-managed encryption keys (CMEK) project](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek).  


In the project list, select the project with the same name as your Assured Workloads folder but with `cmek-` at the beginning. Then, click delete **Delete**.

  3. In the dialog that appears, type the project ID as instructed, and then click **Shut down** to delete the project.

  4. In the folder list, select the Assured Workloads folder, and then click delete **Delete**.

  5. In the dialog that appears, type the folder ID as instructed, and then click **Shut down** to delete the folder.

**Note:** Folders and projects may still be listed for up to 24 hours after they have been deleted.
  6. Click the menu **Navigation menu** , and then click **Compliance**.

  7. From the list of Assured Workloads folders, locate the folder you want to delete, and click delete **Delete**. In the dialog that appears, type the folder name as instructed, and then click **Confirm** to delete the folder.




## What's next

  * Learn how to [delete a Google Cloud folder](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#delete).
  * Learn how to [migrate a workload](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
