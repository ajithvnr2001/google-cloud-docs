---
url: https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore/
title: Hive metastore \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:40.947407+00:00
---

# Hive metastore  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Hive metastore Stay organized with collections  Save and categorize content based on your preferences. 

Dataproc Metastore is a fully managed, highly available, autohealing, serverless, Apache Hive metastore (HMS) that runs on Google Cloud.

To fully manage your metadata, Dataproc Metastore maps your data to [Apache Hive](https://hive.apache.org/) tables.

## Supported Apache Hive versions

Dataproc Metastore only supports specific versions of Apache Hive. For more information, see the [Hive version policy](https://docs.cloud.google.com/dataproc-metastore/docs/version-policy).

## How Hive handles metadata

Since Dataproc Metastore is a Hive metastore, it's important to understand how it manages your metadata.

By default, all Hive applications can have _managed internal tables_ or _unmanaged external tables_. That is, the metadata that you store in a Dataproc Metastore service can exist in both internal and external tables.

When modifying data, a Dataproc Metastore service (Hive) treats internal and external tables differently.

  * **Internal tables**. Manages both metadata and table data.
  * **External tables**. Only manages metadata.



For example, if you delete a table definition using the `DROP TABLE` Hive SQL statement:
    
    
    drop table my_table
    

  * **Internal tables**. Dataproc Metastore deletes all metadata. It also deletes the files associated with the table.

  * **External tables**. Dataproc Metastore only deletes the metadata. It keeps the data associated with the table.




## Hive warehouse directory

Dataproc Metastore uses the Hive warehouse directory to manage your internal tables. The Hive warehouse directory is where your actual data is stored.

When you use a Dataproc Metastore service, the default Hive warehouse directory is a Cloud Storage bucket. Dataproc Metastore only supports the use of Cloud Storage buckets for the warehouse directory. In comparison, this is different to an on-premises HMS, where the Hive warehouse directory usually points to a local directory.

This bucket is automatically created for you every time you create a Dataproc Metastore service. This value can be changed by setting a Hive Metastore configuration override on the `hive.metastore.warehouse.dir` property.

### Artifacts Cloud Storage buckets

The artifacts bucket stores your Dataproc Metastore artifacts, such as exported metadata and managed internal table data.

When you create a Dataproc Metastore service, a Cloud Storage bucket is automatically created for you in your project. By default both the artifacts bucket and the warehouse directory point to the same bucket. You can't change the location of the artifacts bucket, however, you can change the location of the Hive warehouse directory.

The artifacts bucket is located at the following location:

  * `gs://your-artifacts-bucket/hive-warehouse`.
  * For example, `gs://gcs-your-project-name-0825d7b3-0627-4637-8fd0-cc6271d00eb4`.

**Note:** This bucket is created with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) and can't be changed to use fine-grained ACLs.

#### Access the Hive warehouse directory

After your bucket is automatically created for you, ensure that your [Managed Service for Apache Spark service accounts](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#dataproc_service_accounts_2) have permission to access the Hive warehouse directory.

  * To access the warehouse directory at the object level (for example, gs://mybucket/object), grant the Managed Service for Apache Spark service accounts read and write access to the storage object of the bucket, using the `roles/storage.objectAdmin` role. This role must be set at the bucket level or higher.

  * To access the warehouse directory when you use a top-level folder, (for example, gs://mybucket), grant the Managed Service for Apache Spark service accounts read and write access to the storage object of the bucket, using the `roles/storage.storageAdmin` role.




If the Hive warehouse directory is not in the same project as the Dataproc Metastore, ensure that the Dataproc Metastore service agent has permission to access the Hive warehouse directory. The service agent for a Dataproc Metastore project is `service-PROJECT_NUMBER@gcp-sa-metastore.iam.gserviceaccount.com`. Grant the service agent read and write access to the bucket using the [`roles/storage.objectAdmin`](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) role.

### Find the Hive warehouse directory

  1. Open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.
  2. Click the name of your service.

The Service detail page opens.

  3. In the configuration table, find **Metastore config overrides** > **hive.metastore.warehouse.dir**.

  4. Find the value that starts with `gs://`.

This value is the location of your Hive warehouse directory.

![A view of the configuration table showing the Hive warehouse directory path.](https://docs.cloud.google.com/static/dataproc-metastore/images/dataproc-metastore-hive-warehouse-dir.png)




### Change the Hive warehouse directory

To use your own Cloud Storage bucket with Dataproc Metastore, set a Hive Metastore configuration override to point to the new bucket location.

If you change your default warehouse directory, follow these recommendations.

  * Don't use the Cloud Storage bucket root (`gs://mybucket`) to store Hive tables.

  * Make sure your Dataproc Metastore VM service account has permission to access the Hive warehouse directory.

  * For best results, use Cloud Storage buckets that are located in the same region as your Dataproc Metastore service. Although Dataproc Metastore allows cross-region buckets, colocated resources perform better. For example, a `europe-west1` bucket doesn't work well with a `us-central1` service. Cross-region access results in higher latency, lack of regional failure isolation, and charges for cross-region network bandwidth.




#### To change the Hive warehouse directory

  1. Open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.
  2. Click the name of your service.

The Service detail page opens.

  3. In the configuration table, find the **Metastore config overrides** > **hive.metastore.warehouse.dir** section.

  4. Change the `hive.metastore.warehouse.dir` value to the location of your new bucket. For example, `gs://my-bucket/path/to/location`.




### Delete your bucket

Deleting your Dataproc Metastore service doesn't automatically delete your Cloud Storage artifacts bucket. Your bucket isn't automatically deleted because it might contain useful post-service data. To delete your bucket, run a Cloud Storage [delete operation](https://docs.cloud.google.com/storage/docs/deleting-buckets).

**Caution:** Don't delete your artifacts bucket until after you delete your Dataproc Metastore service. If you delete your artifacts bucket first, the service might stop working.

## What's next

  * [Create a service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service)
  * [Update and delete a service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)
  * [Import metadata into a service](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
