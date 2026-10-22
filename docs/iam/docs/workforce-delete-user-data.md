---
url: https://docs.cloud.google.com/iam/docs/workforce-delete-user-data/
title: Delete Workforce Identity Federation users and their data \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:06.601792+00:00
---

# Delete Workforce Identity Federation users and their data  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workforce-delete-user-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Delete Workforce Identity Federation users and their data Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to delete workforce users (also known as principals) and data that they exclusively own, collectively "users and data". To learn more about how Google Cloud deletes data, see [Data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion).

## Delete Workforce Identity Federation user data

**Caution:** Deleting users also deletes all of their data on Google Cloud.

To delete workforce users and data, you must initiate a delete request with a user resource ID that is formatted as follows:
    
    
    principal://iam.googleapis.com/locations/LOCATION/workforcePools/WORKFORCE_POOL_ID/subject/SUBJECT_ID
    

The stages in the data-deletion pipeline are as follows:

**Stage-1: Soft-deletion state:** After you initiate a delete request, the users and data are immediately marked for deletion and enter a 30-day soft- deletion state. In that state, the data can be deleted at anytime. After it is deleted, it cannot be accessed unless it is first recovered. You can _usually_ recover data that is in this state.

**Stage-2: Purged state:** Users and data that remain deleted longer than 30 days are in the purged state, meaning they are permanently deleted and cannot be recovered. After the data enters the purged state, the user identifier can be reused and assigned to another user. This is because the identifier is processed as a new entity in Identity and Access Management (IAM).

### Required permissions

This section details the IAM roles or permissions required to perform delete and undelete operations.

The permissions are as follows:

  * `iam.googleapis.com/workforcePoolSubjects.delete`
  * `iam.googleapis.com/workforcePoolSubjects.undelete`



These permissions are included in the Workforce Pool Admin role (`roles/iam.workforcePoolAdmin`).

### Delete users and data

To delete users and data, do the following:

### gcloud

Execute the following command:
    
    
    gcloud iam workforce-pools subjects delete \
        SUBJECT_ID \
        --workforce-pool=WORKFORCE_POOL_ID \
        --location=global
    

Replace the following:

  * `SUBJECT_ID`: the user resource ID to delete.
  * `WORKFORCE_POOL_ID`: the workforce pool ID.



### Undelete users and data

During the soft-deletion or pre-purge deletion phase, you can undo a user deletion.

To undelete a user, do the following:

### gcloud

To undo a user deletion, execute the following command:
    
    
    gcloud iam workforce-pools subjects undelete SUBJECT_ID \
        --workforce-pool=WORKFORCE_POOL_ID \
        --location=global
    

Replace the following:

  * `SUBJECT_ID`: the user resource ID for which to undo a previous delete.
  * `WORKFORCE_POOL_ID`: the workforce pool ID.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
