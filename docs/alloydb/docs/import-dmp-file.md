---
url: https://docs.cloud.google.com/alloydb/docs/import-dmp-file/
title: Import a DMP file \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:38.963001+00:00
---

# Import a DMP file  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/import-dmp-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Import a DMP file Stay organized with collections  Save and categorize content based on your preferences. 

To restore a binary database archive into an AlloyDB for PostgreSQL cluster, you can import a DMP file created by the `pg_dump` tool using the `custom` or `directory` format.

To import a file created by the `pg_dump` tool using the `plain` format, see [Import a SQL file](https://docs.cloud.google.com/alloydb/docs/import-sql-file).

The procedure to perform the import involves these tasks:

  1. Upload the DMP file to a Cloud Storage bucket.

  2. Prepare a client host to perform the import operation.

  3. Import the DMP file into the database.

  4. Clean up the resources created to perform the procedure.




## Before you begin

  * You must have the Owner (`roles/owner`) or Editor (`roles/editor`) basic IAM role in the Google Cloud project you are using, or you must have these predefined IAM roles: 
    * AlloyDB Admin (`roles/alloydb.admin`) or AlloyDB Viewer (`roles/alloydb.viewer`)
    * Storage Admin (`roles/storage.admin`)
    * Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`)



## Upload the DMP file

To upload the DMP file, you create a Cloud Storage bucket and then upload the DMP file to that bucket.

  1. [Create a standard storage, regional storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in the project and region where your AlloyDB database is located.

  2. [Upload the DMP file](https://docs.cloud.google.com/storage/docs/uploading-objects) to the storage bucket you created.




## Prepare a client host

To prepare a client host to perform the import operation, you create a Compute Engine VM that can connect to the AlloyDB primary instance where your database is located, and install the `pg_restore` tool and the Google Cloud CLI on that VM.

  1. Follow the instructions [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql) to create a Compute Engine VM with the proper connectivity and the `pg_restore` tool installed. When following these instructions, make sure to allocate enough local storage to the Compute Engine VM to accommodate the DMP file you are importing.

  2. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) to provide command-line access to the DMP file in the Cloud Storage bucket.




## Import the DMP file

To import the DMP file, you get the IP address of the AlloyDB primary instance where your database is located and then use the `pg_restore` tool to import the file into the database.

  1. Get the IP address of the AlloyDB primary instance where your database is located by [viewing its details](https://docs.cloud.google.com/alloydb/docs/instance-view). 
  2. SSH into the Compute Engine VM. 

### Console

     1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. In the list of virtual machine instances, click **SSH** in the row of the instance you created. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)

### gcloud

Use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to connect to the instance you created.
    
    gcloud compute ssh --project=PROJECT_ID --zone=ZONE VM_NAME

Replace the following:

     * `PROJECT_ID`: The ID of the project that contains the instance.
     * `ZONE`: The name of the zone in which the instance is located.
     * `VM_NAME`: The name of the instance.

  3. Copy the DMP file to the client host's local file system: 
         
         gcloud storage cp gs://BUCKET_NAME/DMP_FILE_NAME .

  4. Run the following command to create a TOC file that comments out all `EXTENSION` statements: 
         
         pg_restore \
         -l DMP_FILE_NAME | sed -E 's/(.* EXTENSION )/; \1/g' > TOC_FILE_NAME

Replace the following:

     * `DMP_FILE_NAME`: The DMP file on the local file system.
     * `TOC_FILE_NAME`: Provide a file name for the TOC file to create on the local file system.
  5. Import the DMP file: 
         
         pg_restore -h IP_ADDRESS -U postgres \
           -d DB_NAME \
           -L TOC_FILE_NAME \
           DMP_FILE_NAME

Replace the following:

     * `IP_ADDRESS`: The IP address of the primary instance.
     * `DB_NAME`: The name of the database to import into.
     * `TOC_FILE_NAME`: The TOC file you created in the previous step.
     * `DMP_FILE_NAME`: The DMP file.

The [`pg_restore` command](https://www.postgresql.org/docs/17/app-pgrestore.html) provides several additional options to control the data import operation.




## Clean up resources

After successfully importing the DMP file, you can [delete the Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) and delete the [Compute Engine VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) you used during the import procedure.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
