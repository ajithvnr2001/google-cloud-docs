---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-export-cluster/
title: Export a database cluster \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:53.526660+00:00
---

# Export a database cluster  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-export-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Export a database cluster Stay organized with collections  Save and categorize content based on your preferences. 

Before exporting data, you must:

Grant the Database Service export service account write access to the destination object storage bucket. This role binding must be created within the same namespace as the subject database cluster. See [Grant and obtain storage access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#grant_bucket_access).

The Database Service system automatically creates this service account when the database cluster is created. To find the namespace that contains the controller-maintained service account, use the following commands:
    
    
    kubectl get dbclusters.postgresql <var>DATABASE_CLUSTER_NAME</var> -n <var>PROJECT_NAMESPACE</var> -o jsonpath='{.status.serviceAccounts.export}'
    
    kubectl get dbclusters.postgresql <var>DATABASE_CLUSTER_NAME</var> -n <var>PROJECT_NAMESPACE</var> -o jsonpath='{.status.serviceAccounts.import}'
    

Once you have the namespace, the service account you're looking for is named `postgresql-export-DATABASE_CLUSTER_NAME`.

Replace `DATABASE_CLUSTER_NAME` with the name of the database cluster where you are exporting data.

You can export a database cluster to a data dump file using either the GDC console or the Distributed Cloud CLI:

###  Console 

  1. From the main menu, choose **Database Service**.
  2. Select the database cluster you want to export. This takes you to the **Database cluster overview** page for that cluster.
  3. Click file_upload **EXPORT**. The **Export data** panel opens.
  4. In the **Export data** panel, specify the storage location to export to.
  5. Click **EXPORT**. On screen messages indicate the status of the export process.



###  gdcloud CLI 

  1. Before using Distributed Cloud CLI, [install and initialize](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) it. Then, [authenticate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth) with your organization.
  2. Run the following command to export a database file to a dump file:
         
         gdcloud database export sql DATABASE_CLUSTER \
              BUCKET_NAME/SAMPLE.dmp --project=PROJECT_NAME
         

Replace the following:

     * DATABASE_CLUSTER with the name of the database cluster to export.
     * BUCKET_NAME/SAMPLE.dmp with the destination for the exported dump file.
     * PROJECT_NAME with the name of the project that the database cluster is in.



###  API 
    
    
    apiVersion: postgresql.dbadmin.gdc.goog/v1
    kind: Export
    metadata:
      name: EXPORT_NAME
      namespace: USER_PROJECT
    spec:
      dbclusterRef: DBCLUSTER_NAME
      exportLocation:
        s3Options:
          bucket: BUCKET_NAME
          key: dbs-export
        type: S3
    

Replace the following variables:

  * `EXPORT_NAME`: the name of the export operation.
  * `USER_PROJECT`: the name of the user project where the database cluster to be exported is created.
  * `DBCLUSTER_NAME`: the name of the database cluster.
  * `BUCKET_NAME`: the name of the object storage bucket to store the exported files.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
