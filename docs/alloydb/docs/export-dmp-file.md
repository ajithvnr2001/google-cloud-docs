---
url: https://docs.cloud.google.com/alloydb/docs/export-dmp-file/
title: Export a DMP file \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:40.321121+00:00
---

# Export a DMP file  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/export-dmp-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Export a DMP file Stay organized with collections  Save and categorize content based on your preferences. 

To create a portable, binary archive of an AlloyDB for PostgreSQL database that you can later restore using the `pg_restore` tool, you can export your database to a custom-format DMP file using `pg_dump`.

The procedure to perform the export involves these tasks:

  1. Create a Cloud Storage bucket to store the DMP file in.

  2. Prepare a client host to perform the export operation.

  3. Export the database to the DMP file.

  4. Clean up the resources created to perform the procedure.




## Before you begin

  * You must have the Owner (`roles/owner`) or Editor (`roles/editor`) basic IAM role in the Google Cloud project you are using, or you must have these predefined IAM roles: 
    * AlloyDB Admin (`roles/alloydb.admin`) or AlloyDB Viewer (`roles/alloydb.viewer`)
    * Storage Admin (`roles/storage.admin`)
    * Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`)



## Create a Cloud Storage bucket

[Create a standard storage, regional storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in the project and region where your AlloyDB database is located.

## Prepare a client host

To prepare a client host to perform the export operation, you create a Compute Engine VM that can connect to the AlloyDB primary instance where your database is located, and install the `pg_dump` tool and the Google Cloud CLI on that VM.

  1. Follow the instructions [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql) to create a Compute Engine VM with the proper connectivity and the `pg_dump` tool installed. When following these instructions, make sure to allocate enough local storage to the Compute Engine VM to accommodate the DMP file you will create.

  2. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) to provide command-line access to create the DMP file in the Cloud Storage bucket.




## Export the database

To export the database to a DMP file, you get the IP address of the AlloyDB primary instance where your database is located and then use the `pg_dump` tool.

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

  3. Export the database to a DMP file: 
         
         pg_dump -h IP_ADDRESS -U postgres -F custom \
           DB_NAME > DMP_FILE_NAME

You are prompted to enter the password of the `postgres` user.

Replace the following:

     * `IP_ADDRESS`: The IP address of the primary instance.
     * `-F custom`: Sets the format of the DMP file to a custom-format archive that you can later import using the `pg_restore` tool.
     * `DB_NAME`: The name of the database you want to export.
     * `DMP_FILE_NAME`: Provide a file name for the DMP file to create on the client host's local file system.

For information about additional options that the `pg_dump` command supports, see the [PostgreSQL `pg_dump` documentation](https://www.postgresql.org/docs/17/app-pgdump.html).

  4. Copy the DMP file to the Cloud Storage bucket you created earlier: 
         
         gcloud storage cp DMP_FILE_NAME gs://BUCKET_NAME




## Clean up resources

After successfully exporting the DMP file, you can [delete the Compute Engine VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) you used during the export procedure.

## What's next

  * Learn how to [export a CSV file](https://docs.cloud.google.com/alloydb/docs/export-csv-file).
  * Learn how to [export a SQL dump file](https://docs.cloud.google.com/alloydb/docs/export-sql-file). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
