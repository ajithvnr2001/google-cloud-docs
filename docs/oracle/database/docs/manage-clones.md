---
url: https://docs.cloud.google.com/oracle/database/docs/manage-clones/
title: Manage refreshable clones \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:01.588397+00:00
---

# Manage refreshable clones  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/manage-clones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Manage refreshable clones Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage refreshable clones.

Oracle Database@Google Cloud lets you view, delete, disconnect, reconnect, and refresh refreshable clones.

## View refreshable clones of a database

To view refreshable clones of an Autonomous AI Database and their details, do the following:

### gcloud

  * **List refreshable clones**

Use the `gcloud oracle-database autonomous-databases list` command to list refreshable clones.
        
        gcloud oracle-database autonomous-databases get-refreshable-clones SOURCE_DATABASE_ID \
            --project=PROJECT_ID \
            --location=REGION
        

Replace the following:

    * SOURCE_DATABASE_ID: the ID of the source database.
    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where your source database is located.
  * **View refreshable clone details**

Use the `gcloud oracle-database autonomous-databases describe` command to view details of a deployment.
        
        gcloud oracle-database autonomous-databases describe CLONE_ID \
            --project=PROJECT_ID \
            --location=REGION
        

Replace the following:

    * CLONE_ID: the ID of the clone.
    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where your clone is located.



###  API 

  * **List refreshable clones**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/DATABASE_ID:getRefreshableClones"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region where your source database is located.
    * DATABASE_ID: the ID of your source database for which you want to view the clones.
  * **View refreshable clone details**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region where your source database is located.
    * CLONE_ID: the ID of the clone.



## Delete a refreshable clone

To delete a refreshable clone, do the following:

### gcloud

Use the `gcloud oracle-database autonomous-databases delete` command to delete a clone.
    
    
    gcloud oracle-database autonomous-databases delete CLONE_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * CLONE_ID: the ID of the clone.
  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region where your clone is located.



###  API 

To delete a refreshable clone, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region where your clone is located.
  * CLONE_ID: the ID of your clone.



## Disconnect a refreshable clone

You can disconnect a refreshable clone in order to open the database in read and write mode. The database is restarted during the process of disconnecting from the source database and any database sessions are disconnected. The database opens in read or write after it is disconnected from the source database. No automatic refreshes are performed while the database is disconnected.

To disconnect a refreshable clone from its source database, do the following:

### gcloud

To disconnect a refreshable clone from its source database, use the `gcloud oracle-database autonomous-databases update` command
    
    
    gcloud oracle-database autonomous-databases update CLONE_ID
    --project=PROJECT_ID
    --location=REGION
    --no-properties-refreshable-clone \
    --async
    

Replace the following:

  * CLONE_ID: the ID of your clone
  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your clone is located



###  API 

To disconnect a refreshable clone from its source database, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID \
    -d \
    '{
      "properties": { "refreshable_clone": false }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your clone is located
  * CLONE_ID: the ID of your clone



## Reconnect a refreshable clone

A database can be reconnected after it has been opened in read and write mode for updates. Reconnecting the database restarts the database in read-only mode and discard any changes made after the database was disconnected. Reconnecting the database doesn't automatically performs a refresh. Therefore, you must either manually initiate a refresh or wait for the next scheduled refresh of the database before changes are applied from the source.

To connect a refreshable clone to its source database, do the following:

### gcloud

To connect a refreshable clone to its source database, run the `gcloud oracle-database autonomous-databases update` command.
    
    
    gcloud oracle-database autonomous-databases update CLONE_ID
    --project=PROJECT_ID
    --location=REGION
    --properties-refreshable-clone \
    --async
    

Replace the following:

  * CLONE_ID: the ID of your clone
  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your clone is located



###  API 

To connect a refreshable clone to its source database, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID \
    -d \
    '{
      "properties": { "refreshable_clone": true }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your clone is located
  * CLONE_ID: the ID of your clone



## Refresh a clone

To refresh a manual or automatic clone, do the following:

### gcloud

To refresh a clone, use the `gcloud oracle-database autonomous-databases refresh` command.
    
    
    gcloud oracle-database autonomous-databases refresh CLONE_ID
    --project=PROJECT_ID
    --location=REGION
    --refresh-cutoff-time="CUTOFF_TIME" \
    --async
    

Replace the following:

  * CLONE_ID: the ID of your clone
  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your clone is located
  * CUTOFF_TIME: the timestamp to which the clone is refreshed. Changes made to the source database after this timestamp aren't part of the data refresh.

Uses RFC 3339, where generated output is always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. For examples, `2014-10-02T15:01:23Z`, `2014-10-02T15:01:23.045123456Z`, or `2014-10-02T15:01:23+05:30`.




###  API 

To refresh a clone, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID:refresh \
    -d \
    '{
      "name": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID",
      "refresh_cutoff_time": "CUTOFF_TIME"
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your clone is located
  * CLONE_ID: the ID of your clone
  * CUTOFF_TIME: the timestamp to which the clone is refreshed. Changes made to the source database after this timestamp aren't part of the data refresh.

Uses RFC 3339, where generated output is always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. For examples, `2014-10-02T15:01:23Z`, `2014-10-02T15:01:23.045123456Z`, or `2014-10-02T15:01:23+05:30`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
