---
url: https://docs.cloud.google.com/oracle/database/docs/delete-base-db-system/
title: Delete DB systems \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:14.665759+00:00
---

# Delete DB systems  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/delete-base-db-system/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Delete DB systems Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete a DB system in Google Cloud.

Deleting a DB system also deletes its container database and pluggable databases. You can't undo this later.

## Before you begin

Make sure that you have the required Identity and Access Management (IAM) roles and permissions to delete a DB system:

  * `roles/oracledatabase.dbSystemAdmin`



For information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

## Delete a DB system and its databases

To delete your DB system and its databases, do the following:

### Console

  1. Go to the **Base Database Service** page.

[Go to Base Database Service](https://console.cloud.google.com/oracle/basedb/)

  2. For the DB system which you want to delete, click more_vert **View actions** , and then click **Delete**.

  3. In the **Delete DB system?** dialog, type the DB system name to confirm deletion of your DB system.

  4. Click **Confirm**.




###  API 

To delete a DB system, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/dbSystems/DB_SYSTEM_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the DB system to be deleted. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your DB system.
  * DB_SYSTEM_ID: the ID of your DB system.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
