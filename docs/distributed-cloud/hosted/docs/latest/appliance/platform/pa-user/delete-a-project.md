---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/delete-a-project/
title: Delete a project \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:41.768030+00:00
---

# Delete a project  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/delete-a-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Delete a project Stay organized with collections  Save and categorize content based on your preferences. 

Delete a project to remove a group of resources within an organization. When deleting a project in Google Distributed Cloud (GDC) air-gapped appliance, the system first verifies the project is eligible for deletion. If the system reports precheck errors, you must manually fix the issues before you can initiate project deletion.

## Before you begin

To get the permissions needed to delete a project, ask your Organization IAM Admin to grant you the Project Editor role (`project-editor`).

## Delete a project and its resources

To delete a project, complete the following steps:

###  Console 

  1. From the navigation menu of the GDC console, click **Projects**.

  2. Select the project that you want to delete.

  3. Ensure the clusters attached to the project are assigned to other projects. A cluster must be attached to a project.

  4. Click delete **Delete Project**.

  5. When prompted, type `remove` and click **Confirm** to initiate the project deletion prechecks.




If the project deletion prechecks complete successfully, the GDC system begins deleting the project. If the prechecks fail, error codes are reported in a prompt.

###  gdcloud 

  1. Ensure you have the gdcloud CLI installed. For more information, see the gdcloud CLI [Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview#download_and_install_the) page.

  2. To delete the project, run:
         
         gdcloud projects delete PROJECT_ID
         

Replace `PROJECT_ID` with the unique identifier for the project to delete.




If the project deletion prechecks complete successfully, the GDC system begins deleting the project. If the prechecks don't complete successfully, precheck failures with corresponding error codes are reported in the gdcloud CLI.

You must manually fix the issues reported before you can delete the project. See the Handle project deletion precheck failures section for steps to manually fix precheck failures.

## Handle project deletion precheck failures

If the project deletion precheck task is not successful, you are given a code that maps to the issue. Locate the code and complete the outlined steps to fix the issue.

### OBJ-E0001: Buckets must be deleted in project

This error occurs when deleting a project if it has storage buckets remaining. You must remove the buckets before the project can be deleted successfully.

For more information, see [Delete storage buckets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/delete-storage-buckets) to manually delete your project's storage buckets.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
