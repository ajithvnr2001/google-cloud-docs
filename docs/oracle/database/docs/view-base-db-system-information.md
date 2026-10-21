---
url: https://docs.cloud.google.com/oracle/database/docs/view-base-db-system-information/
title: View DB systems information \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:14.906956+00:00
---

# View DB systems information  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/view-base-db-system-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  View DB systems information Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view information for a DB system and its databases in Google Cloud.

## Before you begin

Make sure that you have the required Identity and Access Management (IAM) roles and permissions to view details of a DB system and its databases:

  * `roles/oracledatabase.dbSystemViewer`
  * `roles/oracledatabase.databaseViewer`
  * `roles/oracledatabase.pluggableDatabaseViewer`



For information about how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

## View DB system details

To view details of a DB system and its databases, do the following:

### Console

  1. Go to the **Base Database Service** page.

[Go to Base Database Service](https://console.cloud.google.com/oracle/basedb/)

  2. Click the name of the DB system.

The **DB system details** page shows you the details of the DB system.

  3. To view change logs, select the **Operations** tab.

  4. To view the details of the databases, do the following:

     1. Go to the **Databases** section.
     2. Click the name of the container database to view its details.

The **Database details** page shows you the details.

     3. To view the details of the pluggable databases, on the **Database details** page, go to the **Pluggable databases** section.

     4. Click the name of a pluggable database to view its details.

The **Pluggable database details** page shows you the details.

     5. To view the connection strings of the pluggable database, select the **Connections** tab.




###  API 

  * **List DB systems**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/dbSystems"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region of your DB systems.
  * **View DB system details**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/dbSystems/DB_SYSTEM_ID"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region of your DB systems.
    * DB_SYSTEM_ID: the ID of your DB system.
  * **List container databases of a DB system**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databases?filter="dbSystem=\"projects/PROJECT_ID/locations/REGION/dbSystems/DB_SYSTEM_ID\""
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project which contains your DB system. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region of your DB system.
    * DB_SYSTEM_ID: the ID of your DB system.
  * **View container database details**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/databases/CONTAINER_DB_ID"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region of your DB system.
    * CONTAINER_DB_ID: the ID of your container database.
  * **List pluggable databases of a container database**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/pluggableDatabases?filter="database=\"projects/PROJECT_ID/locations/REGION/databases/CONTAINER_DB_ID\""
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project which contains your DB system. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region of your DB system.
    * CONTAINER_DB_ID: the ID of your container database.
  * **View pluggable database details**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/pluggableDatabases/PLUGGABLE_DB_ID"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region of your DB system.
    * PLUGGABLE_DB_ID: the ID of your pluggable database.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
