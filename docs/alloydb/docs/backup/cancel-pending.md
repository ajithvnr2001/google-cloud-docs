---
url: https://docs.cloud.google.com/alloydb/docs/backup/cancel-pending/
title: Cancel an in-progress backup operation \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:30:35.516313+00:00
---

# Cancel an in-progress backup operation  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/backup/cancel-pending/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Cancel an in-progress backup operation Stay organized with collections  Save and categorize content based on your preferences. 

To stop an unneeded or unintended backup before it finishes, you can cancel an in-progress an AlloyDB for PostgreSQL backup operation.

You can cancel a running backup operation if:

  * The source cluster of the backup is in the "Ready" state
  * The backup is in the "Pending" state



To cancel the backup operation, you cancel the long-running operation that AlloyDB initiated to perform the operation. Note that in some cases, your attempt to cancel the long-running operation can fail due to the current status of the operation.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Procedure

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the `operations cancel` command to cancel the long-running operation performing an AlloyDB backup.
    
    
    gcloud alloydb operations cancel OPERATION_ID \
        --region=REGION_ID \
        --project=PROJECT_ID

  * OPERATION_ID: The ID of the long-running operation, as reported by AlloyDB when the backup was started.
  * REGION_ID: The ID of the region where the backup is placed.
  * PROJECT_ID: The ID of the project where the backup is placed.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
