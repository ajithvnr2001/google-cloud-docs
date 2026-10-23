---
url: https://docs.cloud.google.com/lakehouse/docs/use-lakehouse-metastore-iceberg-rest-catalog/
title: Quickstart: Use the Iceberg REST catalog with Cloud Storage \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:02.476657+00:00
---

# Quickstart: Use the Iceberg REST catalog with Cloud Storage  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/use-lakehouse-metastore-iceberg-rest-catalog/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the Iceberg REST catalog with Cloud Storage

Learn how to use _Lakehouse_ by creating a _Lakehouse runtime catalog_ with a [Cloud Storage bucket](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#supported_catalog_types). This configuration establishes a managed metadata layer that connects open-source processing engines with Google Cloud.

You then run Managed Service for Apache Spark PySpark job to create an [Apache Iceberg table managed by Lakehouse](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-tables) using the _Apache Iceberg REST catalog_ endpoint.

Afterwards, you can query the resulting table directly from the Google Cloud console in BigQuery using the `project.catalog.namespace.table` syntax.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the BigLake, Dataproc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,dataproc.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigLake, Dataproc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,dataproc.googleapis.com)




## Grant IAM roles

To allow the Managed Service for Apache Spark PySpark job and Lakehouse runtime catalog to work with Cloud Storage and BigQuery, grant the necessary roles to their corresponding principals:

  1. In the Google Cloud console, click **Activate Cloud Shell**.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Click **Authorize**.

  3. Grant the **Dataproc Worker** role to the project's [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-accounts#default-service-accounts), which Managed Service for Apache Spark uses by default as detailed in [Managed Service for Apache Spark service accounts](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#dataproc-cluster-service-accounts).
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:$(gcloud projects describe PROJECT_ID --format='value(projectNumber)')-compute@developer.gserviceaccount.com" \
             --role="roles/dataproc.worker"

  4. Grant the **Service Usage Consumer** role to the project's Compute Engine default service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:$(gcloud projects describe PROJECT_ID --format='value(projectNumber)')-compute@developer.gserviceaccount.com" \
             --role="roles/serviceusage.serviceUsageConsumer"

  5. Grant the **BigLake Editor** role to the project's Compute Engine default service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:$(gcloud projects describe PROJECT_ID --format='value(projectNumber)')-compute@developer.gserviceaccount.com" \
             --role="roles/biglake.editor"

  6. Grant the **BigQuery Data Editor** role to the project's Compute Engine default service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:$(gcloud projects describe PROJECT_ID --format='value(projectNumber)')-compute@developer.gserviceaccount.com" \
             --role="roles/bigquery.dataEditor"

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID



## Create a Lakehouse runtime catalog

Create a Lakehouse runtime catalog to manage metadata for your Iceberg tables. You connect to this catalog in your PySpark job.

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click add_box **Create catalog**.

The **Create catalog** page opens.

  3. Select **Iceberg REST catalog** , and then select **Cloud Storage bucket**.

  4. For **Select a Cloud Storage bucket** , click **Browse** , and then click **Create new bucket**.

  5. Enter a unique name for your bucket.

Important 

Remember the name of your bucket. It is also automatically used as your Lakehouse catalog name. It can't be changed. You can add this name here now, if you want to store the name in the variable to use later in this tutorial.
         
         LAKEHOUSE_CATALOG_ID

If your bucket is located in a multi-region (e.g. `us`, `eu`), use a region in the same geographical location, such as `us-east1` or `europe-west4`. You can store the region in this variable to use later:
         
         REGION

Remember the region you create your bucket in. You _must_ use the same region later in this tutorial when you run your PySpark job with the `dataproc batches submit pyspark` command. If you create the bucket in a multi-region (e.g. `us`, `eu`), you should use a region in the same geographical location, such as `us-east1` or `europe-west4`. You can add this name here now, if you want to store the name in the variable to use later in this tutorial.
         
         REGION

  6. From the bucket list, select your bucket and click **Select**.

  7. For **Authentication method** , select **Credential vending mode**.

  8. Click **Create**.

Your catalog is created and the **Catalog details** page opens.

  9. Under **Authentication method** , click **Set bucket permissions**.

  10. In the dialog, click **Confirm**.

This verifies that your catalog's service account has the Storage Object User role on your storage bucket.

**Note:** Creation of the auto-provisioned catalog service account is [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency). This means that it takes time for the service account to propagate through the system. If you try to grant roles to the service account immediately after creation, the request might fail. To learn how long it takes, on average, for access changes to propagate, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).



## Create and run a PySpark job

To create and query an Iceberg table, first create a PySpark job with the necessary Spark SQL statements. Then run the job with Managed Service for Apache Spark.

### Create a PySpark script with a namespace and table

In a text editor, create a file named `quickstart.py` with the following content.

This PySpark script initializes a Spark session to perform several operations on an Iceberg catalog. The script first creates a namespace, if one doesn't already exist. It then creates an Iceberg table named `quickstart_table` with a basic schema. After the table is created, the script inserts three rows of data. Finally, it queries the table to retrieve all the inserted records.

These values are then used in the next step when you run the `gcloud dataproc batches submit pyspark` job.
    
    
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName("quickstart").getOrCreate()
    
    # Create a namespace (dataset) if it doesn't exist
    spark.sql("CREATE NAMESPACE IF NOT EXISTS `quickstart_catalog`.quickstart_namespace")
    
    # Create the table
    spark.sql("""
        CREATE OR REPLACE TABLE `quickstart_catalog`.quickstart_namespace.quickstart_table (
            id INT,
            name STRING
        )
        USING iceberg
    """)
    
    # Insert data into the table
    spark.sql("""
        INSERT INTO `quickstart_catalog`.quickstart_namespace.quickstart_table
        VALUES (1, 'one'), (2, 'two'), (3, 'three')
    """)
    

### Upload the script to your Cloud Storage bucket

After you create the `quickstart.py` script, upload it to the Cloud Storage bucket.

  1. In the Google Cloud console, go to **Cloud Storage buckets**.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of your bucket.

  3. On the **Objects** tab, click **Upload** > **Upload files**.

  4. In the file browser, select the `quickstart.py` file, and then click **Open**.




### Run the PySpark job

After you upload the `quickstart.py` script, run it as a Managed Service for Apache Spark batch job.

**Important:** Configure the following Managed Service for Apache Spark job with the same region that you created your bucket in earlier. If your bucket is located in a multi-region (e.g. `us`, `eu`), choose a region in the same geographical location, such as `us-east1` or `europe-west4`.

  1. In Cloud Shell, run the following Managed Service for Apache Spark batch job using the `quickstart.py` script.
         
         gcloud dataproc batches submit pyspark gs://LAKEHOUSE_CATALOG_ID/quickstart.py \
             --project=PROJECT_ID \
             --region=REGION \
             --version=2.2 \
             --properties="\
         spark.sql.defaultCatalog=quickstart_catalog,\
         spark.sql.catalog.quickstart_catalog=org.apache.iceberg.spark.SparkCatalog,\
         spark.sql.catalog.quickstart_catalog.type=rest,\
         spark.sql.catalog.quickstart_catalog.uri=https://biglake.googleapis.com/iceberg/v1/restcatalog,\
         spark.sql.catalog.quickstart_catalog.warehouse=gs://LAKEHOUSE_CATALOG_ID,\
         spark.sql.catalog.quickstart_catalog.io-impl=org.apache.iceberg.gcp.gcs.GCSFileIO,\
         spark.sql.catalog.quickstart_catalog.header.x-goog-user-project=PROJECT_ID,\
         spark.sql.catalog.quickstart_catalog.rest.auth.type=org.apache.iceberg.gcp.auth.GoogleAuthManager,\
         spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,\
         spark.sql.catalog.quickstart_catalog.header.X-Iceberg-Access-Delegation=vended-credentials,\
         spark.sql.catalog.quickstart_catalog.gcs.oauth2.refresh-credentials-endpoint=https://oauth2.googleapis.com/token"

Replace the following:

     * `LAKEHOUSE_CATALOG_ID`: the name of the Cloud Storage bucket that contains your PySpark application file.

**Important** :

This identifier is also the name of your Catalog. For example, if you created your bucket to store your catalog and named it `iceberg-bucket`, both your catalog name and bucket name are `iceberg-bucket`. This name is used later when you query your catalog in BigQuery, using the P.C.N.T syntax. For example `my-project.biglake-catalog-id-name.quickstart_namespace.quickstart_table`.

     * `PROJECT_ID`: your Google Cloud project ID.

     * `REGION`: the region to run the Managed Service for Apache Spark batch workload in.

When the job completes, it displays an output similar to the following:
    
    Batch [cb9d84e9489d408baca4f9e7ab4c64ff] finished.
    metadata:
    '@type': type.googleapis.com/google.cloud.dataproc.v1.BatchOperationMetadata
    batch: projects/your-project/locations/us-central1/batches/cb9d84e9489d408baca4f9e7ab4c64ff
    batchUuid: 54b0b9d2-f0a1-4fdf-ae44-eead3f8e60e9
    createTime: '2026-01-24T00:10:50.224097Z'
    description: Batch
    labels:
        goog-dataproc-batch-id: cb9d84e9489d408baca4f9e7ab4c64ff
        goog-dataproc-batch-uuid: 54b0b9d2-f0a1-4fdf-ae44-eead3f8e60e9
        goog-dataproc-drz-resource-uuid: batch-54b0b9d2-f0a1-4fdf-ae44-eead3f8e60e9
        goog-dataproc-location: us-central1
    operationType: BATCH
    name: projects/your-project/regions/us-central1/operations/32287926-5f61-3572-b54a-fbad8940d6ef
    




## Query the table from BigQuery

  1. In the Google Cloud console, go to **BigQuery**.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, enter the following statement. The query uses the `project.catalog.namespace.table` syntax.
         
         SELECT * FROM `PROJECT_ID.LAKEHOUSE_CATALOG_ID.quickstart_namespace.quickstart_table`;
         

Replace:

     * `PROJECT_ID`: your Google Cloud project ID.

     * `LAKEHOUSE_CATALOG_ID`: the catalog identifier to use in BigQuery queries.

**Important**

This identifier is also the name of your Cloud Storage bucket.

For example, if you created your bucket to store your catalog and named it `iceberg-bucket`, both your catalog name and bucket name are `iceberg-bucket`. This is used later when you query your catalog in BigQuery, using the P.C.N.T syntax. For example `my-project.biglake-catalog-id-name.quickstart_namespace.quickstart_table`.

  3. Click **Run**.

The query results show the data that you inserted with the PySpark job.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Update `quickstart.py` to delete the namespace (dataset) and table:
         
         from pyspark.sql import SparkSession
         
         spark = SparkSession.builder.appName("quickstart").getOrCreate()
         
         # Delete the table first, then the namespace (dataset)
         spark.sql("DROP TABLE `quickstart_catalog`.quickstart_namespace.quickstart_table")
         spark.sql("DROP NAMESPACE `quickstart_catalog`.quickstart_namespace")
         

Upload it to the Cloud Storage bucket:

     1. In the Google Cloud console, go to **Cloud Storage buckets**.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Click the name of your bucket.

     3. On the **Objects** tab, click **Upload** > **Upload files**.

     4. In the file browser, select the `quickstart.py` file, and then click **Open**.

In Cloud Shell, run another Managed Service for Apache Spark batch job using the updated `quickstart.py` script.
    
    gcloud dataproc batches submit pyspark gs://LAKEHOUSE_CATALOG_ID/quickstart.py \
        --project=PROJECT_ID \
        --region=REGION \
        --version=2.2 \
        --properties="\
    spark.sql.defaultCatalog=quickstart_catalog,\
    spark.sql.catalog.quickstart_catalog=org.apache.iceberg.spark.SparkCatalog,\
    spark.sql.catalog.quickstart_catalog.type=rest,\
    spark.sql.catalog.quickstart_catalog.uri=https://biglake.googleapis.com/iceberg/v1/restcatalog,\
    spark.sql.catalog.quickstart_catalog.warehouse=gs://LAKEHOUSE_CATALOG_ID,\
    spark.sql.catalog.quickstart_catalog.io-impl=org.apache.iceberg.gcp.gcs.GCSFileIO,\
    spark.sql.catalog.quickstart_catalog.header.x-goog-user-project=PROJECT_ID,\
    spark.sql.catalog.quickstart_catalog.rest.auth.type=org.apache.iceberg.gcp.auth.GoogleAuthManager,\
    spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,\
    spark.sql.catalog.quickstart_catalog.header.X-Iceberg-Access-Delegation=vended-credentials,\
    spark.sql.catalog.quickstart_catalog.gcs.oauth2.refresh-credentials-endpoint=https://oauth2.googleapis.com/token"

Replace the following:

     * `LAKEHOUSE_CATALOG_ID`: the name of the Cloud Storage bucket that contains your PySpark application file.

**Important** :

This identifier is also the name of your Catalog. For example, if you created your bucket to store your catalog and named it `iceberg-bucket`, both your catalog name and bucket name are `iceberg-bucket`. This name is used later when you query your catalog in BigQuery, using the P.C.N.T syntax. For example `my-project.biglake-catalog-id-name.quickstart_namespace.quickstart_table`.

     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the region to run the Managed Service for Apache Spark batch workload in.
  2. Go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  3. Select your LAKEHOUSE_CATALOG_ID catalog, and then click **Delete**.

  4. Go to **Cloud Storage Buckets**.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  5. Select your bucket and click **Delete**.




## What's next

  * Learn how to [manage Lakehouse catalogs](https://docs.cloud.google.com/lakehouse/docs/manage-catalogs).
  * Learn about [Apache Iceberg tables supported by the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
