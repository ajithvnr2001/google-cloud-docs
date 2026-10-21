---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-import-from-file/
title: Import from a dump file \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:01:03.415243+00:00
---

# Import from a dump file  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-import-from-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Import from a dump file Stay organized with collections  Save and categorize content based on your preferences. 

Before importing data, you must:

  1. [Create a database cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-create-cluster) to import the data to.

  2. Upload the dump file to a storage bucket. See [Upload objects to storage buckets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/upload-download-storage-objects#upload_objects_to_storage_buckets) for instructions.

  3. Grant the Database Service import service account read access to the dump file. See [Grant and obtain storage access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#grant_bucket_access). For example, you can grant the `project-bucket-object-viewer` role to the import service account.

The Database Service system automatically creates this service account when the database cluster is created. The database cluster status includes both the name and namespace of the import service account.

To retrieve the import service account's name and namespace, run the following command:
         
         kubectl --kubeconfig=MGMT_API_KUBECONFIG \
           get dbcluster.postgresql -n PROJECT_ID DATABASE_CLUSTER_NAME \
           -o jsonpath='{.status.serviceAccounts.import}'
         

This command returns a JSON object containing the name and namespace details: `{"name":"postgresql-import-DATABASE_CLUSTER_NAME","namespace":"SERVICE_ACCOUNT_NAMESPACE"}`




WARNING: The database dump file must be created using `pg_dump` with an archive format compatible with `pg_restore`. Plain SQL format dumps (default if no format option is specified) are **not** supported.

You can import a dump file into a database cluster using either the GDC console or the Distributed Cloud CLI:

###  Console 

  1. Open the **Database cluster overview** page in the GDC console to see the cluster that contains the database you are importing.

  2. Click **Import**. The **Import data to accounts** panel opens.

  3. In the **Source** section of the **Import data to accounts** panel, specify the location of the SQL data dump file you uploaded previously.

  4. In the **Destination** field, specify an existing destination database for the import.

**Note:** You can leave this field empty if the dump file already specifies a destination. If the dump file specifies a destination and you fill the **Destination** field, the **Destination** field overrides the destination specified in the dump file.
  5. Click **Import**. A banner on the GDC console shows the status of the import.




###  gdcloud CLI 

  1. Before using Distributed Cloud CLI, [install and initialize](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) it. Then, [authenticate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth) with your organization.

  2. Run the following command to import a dump file into a database:
         
         gdcloud database import sql DATABASE_CLUSTER BUCKET_NAME/sample.dmp \
             --project=PROJECT_NAME
         

Replace the following:

     * DATABASE_CLUSTER with the name of the database cluster to import data into.
     * BUCKET_NAME/SAMPLE.dmp with the location of the dump file.
     * PROJECT_NAME with the name of the project that the database cluster is in.
  3. Run the following command to check the status of the import:
         
         gdcloud database operations list --project=PROJECT_NAME --cluster=DATABASE_CLUSTER
         




###  API 
    
    
    apiVersion: postgresql.dbadmin.gdc.goog/v1
    kind: Import
    metadata:
      name: IMPORT_NAME
      namespace: USER_PROJECT
    spec:
      dbclusterRef: DBCLUSTER_NAME
      dumpStorage:
        s3Options:
          bucket: BUCKET_NAME
          key: DUMP_FILE_PATH
        type: S3
    

Replace the following variables:

  * `IMPORT_NAME`: the name of the import operation.
  * `USER_PROJECT`: the name of the user project where the database cluster to import is created.
  * `DBCLUSTER_NAME`: the name of the database cluster.
  * `BUCKET_NAME`: the name of the object storage bucket that stores the import files.
  * `DUMP_FILE_PATH`: the name of the object storage path to the stored files.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
