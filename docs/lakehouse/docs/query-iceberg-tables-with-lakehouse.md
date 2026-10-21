---
url: https://docs.cloud.google.com/lakehouse/docs/query-iceberg-tables-with-lakehouse/
title: Quickstart: Create and query an Iceberg table in Lakehouse using the Google Cloud CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:41.772865+00:00
---

# Quickstart: Create and query an Iceberg table in Lakehouse using the Google Cloud CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/query-iceberg-tables-with-lakehouse/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and query an Iceberg table in Lakehouse using the Google Cloud CLI

In this quickstart, you learn how borderless Lakehouse lets you share Apache Iceberg tables between open-source engines and Google Cloud by managing table metadata, including schemas, snapshots, and storage locations, in the Lakehouse runtime catalog.

To complete this quickstart, you perform the following steps:

  1. **Create a catalog** : Create a multiple-bucket catalog in the Lakehouse runtime catalog backed by Cloud Storage.
  2. **Create an Iceberg table with Spark** : Run a PySpark script on Managed Service for Apache Spark to try out an open-source workload without setting up your own cluster. Spark connects through the Apache Iceberg REST catalog endpoint, which also works with any Iceberg-compatible engine like self-managed Spark, Trino, or Apache Flink.
  3. **Query the table in BigQuery** : Query that same table in BigQuery using the 4-part **P.C.N.T** (**Project.Catalog.Namespace.Table**) syntax, with no ETL or manual table registration needed.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigLake, Managed Service for Apache Spark, Cloud Storage, BigQuery, and Compute Engine APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable biglake.googleapis.com dataproc.googleapis.com storage.googleapis.com bigquery.googleapis.com compute.googleapis.com

  8. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/biglake.admin, roles/storage.admin, roles/dataproc.editor, roles/resourcemanager.projectIamAdmin, roles/bigquery.jobUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the BigLake, Managed Service for Apache Spark, Cloud Storage, BigQuery, and Compute Engine APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable biglake.googleapis.com dataproc.googleapis.com storage.googleapis.com bigquery.googleapis.com compute.googleapis.com

  15. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/biglake.admin, roles/storage.admin, roles/dataproc.editor, roles/resourcemanager.projectIamAdmin, roles/bigquery.jobUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.




## Set up your environment and create a bucket

Open Cloud Shell and create a Cloud Storage bucket to hold a PySpark script and Iceberg table data:

  1. In the Google Cloud console, click **Activate Cloud Shell**.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Click **Authorize** if prompted.

  3. Set environment variables for your project, region, bucket, and catalog name so you can reuse them throughout this quickstart:
         
         export PROJECT_ID=$(gcloud config get-value project)
         export REGION="us-central1"
         export BUCKET_NAME="${PROJECT_ID}-lakehouse-quickstart"
         export LAKEHOUSE_CATALOG_ID="quickstart_catalog"

  4. Create a Cloud Storage bucket in your selected region:
         
         gcloud storage buckets create gs://${BUCKET_NAME} \
             --project=${PROJECT_ID} \
             --location=${REGION}




### Grant permissions to the Spark service account

By default, Managed Service for Apache Spark runs batch jobs using your project's [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-accounts#default-service-accounts). Grant this service account the following IAM roles so it can read your PySpark script from Cloud Storage and interact with the Lakehouse runtime catalog and BigQuery:

Role | Resource | Purpose  
---|---|---  
**Dataproc Worker**  
(`roles/dataproc.worker`) | Project | Run Managed Service for Apache Spark batch workloads.  
**Service Usage Consumer**  
(`roles/serviceusage.serviceUsageConsumer`) | Project | Use project APIs and quota.  
**BigLake Editor**  
(`roles/biglake.editor`) | Project | Create catalog resources and request vended storage credentials.  
**BigQuery Data Editor**  
(`roles/bigquery.dataEditor`) | Project | Manage BigQuery metadata for your tables.  
**Storage Object Viewer**  
(`roles/storage.objectViewer`) | Bucket | Read your PySpark script from your Cloud Storage bucket.  
  
Notice that the Spark service account only needs the **Storage Object Viewer** role (`roles/storage.objectViewer`) to read your PySpark script. It doesn't need direct write access to your bucket because the Lakehouse runtime catalog vends temporary, table-scoped write credentials when the job runs.

In Cloud Shell, run the following script to grant these roles:
    
    
    PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} \
        --format='value(projectNumber)')
    SPARK_SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
    
    for ROLE in \
        "roles/dataproc.worker" \
        "roles/serviceusage.serviceUsageConsumer" \
        "roles/biglake.editor" \
        "roles/bigquery.dataEditor"; do
      gcloud projects add-iam-policy-binding ${PROJECT_ID} \
          --member="serviceAccount:${SPARK_SA}" \
          --role="${ROLE}"
    done
    
    gcloud storage buckets add-iam-policy-binding gs://${BUCKET_NAME} \
        --member="serviceAccount:${SPARK_SA}" \
        --role="roles/storage.objectViewer"

## Create a catalog in the Lakehouse runtime catalog

Create a catalog in the Lakehouse runtime catalog for your Apache Iceberg tables.

  1. In Cloud Shell, create a multiple-bucket catalog. A multiple-bucket catalog lets you name your catalog independently of any bucket name and associate multiple Cloud Storage buckets with a single catalog. Enable credential vending mode so that the Lakehouse runtime catalog can securely issue temporary storage credentials to Spark on your behalf.
         
         gcloud biglake iceberg catalogs create ${LAKEHOUSE_CATALOG_ID} \
             --project=${PROJECT_ID} \
             --catalog-type=biglake \
             --default-location=gs://${BUCKET_NAME} \
             --credential-mode=vended-credentials

  2. Give the catalog access to your bucket:

With credential vending, the catalog's auto-provisioned service account needs the **Storage Object User** role (`roles/storage.objectUser`) on your bucket so it can generate temporary access tokens for client engines.
         
         # Retrieve the auto-provisioned catalog service account email
         CATALOG_SA=$(gcloud biglake iceberg catalogs describe ${LAKEHOUSE_CATALOG_ID} \
             --project=${PROJECT_ID} \
             --format='value(biglake-service-account)')
         
         # Grant the Storage Object User role to the catalog service account on your bucket
         gcloud storage buckets add-iam-policy-binding gs://${BUCKET_NAME} \
             --member="serviceAccount:${CATALOG_SA}" \
             --role="roles/storage.objectUser"




## Create an Iceberg table with a PySpark job

With your catalog and permissions ready, you can run a PySpark job on Managed Service for Apache Spark to create an Iceberg table and insert some sample data.

### Create and upload a PySpark script

  1. In Cloud Shell, create a file named `quickstart.py`:
         
         cat << 'EOF' > quickstart.py
         from pyspark.sql import SparkSession
         
         spark = SparkSession.builder.appName("quickstart").getOrCreate()
         
         # Create a namespace
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
         EOF

This script starts a Spark session, creates a namespace called `quickstart_namespace` and an Iceberg table called `quickstart_table`, and inserts three rows of sample data. Because the SQL statements don't specify a bucket path (`LOCATION`), the Lakehouse runtime catalog automatically stores the namespace and table files in your catalog's `--default-location` bucket (`gs://${BUCKET_NAME}`).

  2. Copy `quickstart.py` to your Cloud Storage bucket so Managed Service for Apache Spark can access it:
         
         gcloud storage cp quickstart.py gs://${BUCKET_NAME}/quickstart.py




### Run the PySpark script

Submit your PySpark script as a Managed Service for Apache Spark batch job, which runs your code with pre-installed Iceberg libraries without the need to provision a cluster.

The `--properties` flag configures Spark to connect to your catalog in the Lakehouse runtime catalog using the Apache Iceberg REST catalog endpoint:

  1. In Cloud Shell, submit the batch job:
         
         gcloud dataproc batches submit pyspark gs://${BUCKET_NAME}/quickstart.py \
             --project=${PROJECT_ID} \
             --region=${REGION} \
             --version=2.2 \
             --properties="spark.sql.catalog.quickstart_catalog=org.apache.iceberg.spark.SparkCatalog,\
         spark.sql.catalog.quickstart_catalog.type=rest,\
         spark.sql.catalog.quickstart_catalog.uri=https://biglake.googleapis.com/iceberg/v1/restcatalog,\
         spark.sql.catalog.quickstart_catalog.warehouse=bl://projects/${PROJECT_ID}/catalogs/${LAKEHOUSE_CATALOG_ID},\
         spark.sql.catalog.quickstart_catalog.io-impl=org.apache.iceberg.gcp.gcs.GCSFileIO,\
         spark.sql.catalog.quickstart_catalog.header.x-goog-user-project=${PROJECT_ID},\
         spark.sql.catalog.quickstart_catalog.rest.auth.type=org.apache.iceberg.gcp.auth.GoogleAuthManager,\
         spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,\
         spark.sql.catalog.quickstart_catalog.header.X-Iceberg-Access-Delegation=vended-credentials,\
         spark.sql.catalog.quickstart_catalog.gcs.oauth2.refresh-credentials-endpoint=https://oauth2.googleapis.com/token"

In addition to standard Iceberg settings (`SparkCatalog`, `type=rest`, and `IcebergSparkSessionExtensions`), these properties configure the Lakehouse runtime catalog connection:

     * **`uri` and `warehouse` (`bl://...`)**: Connect Spark to the Lakehouse runtime catalog Apache Iceberg REST catalog endpoint and route requests to your multiple-bucket catalog.
     * **`rest.auth.type` and `header.x-goog-user-project`**: Authenticate REST requests using the Spark service account's credentials and bill API quota to your project.
     * **`header.X-Iceberg-Access-Delegation`, `io-impl`, and `gcs.oauth2.refresh-credentials-endpoint`**: Request temporary, vended Cloud Storage credentials from the catalog and configure Iceberg's `GCSFileIO` client to write data files using those tokens.

For more information about these settings, see [Configure client application](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog#configure-catalog) and the [Apache Iceberg Spark configuration documentation](https://iceberg.apache.org/docs/latest/spark-configuration/).

When the job finishes, the output is similar to the following:
    
    Batch [cb9d84e9489d408baca4f9e7ab4c64ff] finished.
    metadata:
      '@type': type.googleapis.com/google.cloud.dataproc.v1.BatchOperationMetadata
      batch: projects/PROJECT_ID/locations/us-central1/batches/cb9d84e9489d408baca4f9e7ab4c64ff
      batchUuid: 54b0b9d2-f0a1-4fdf-ae44-eead3f8e60e9
      createTime: '2026-01-24T00:10:50.224097Z'
      description: Batch
      labels:
        goog-dataproc-batch-id: cb9d84e9489d408baca4f9e7ab4c64ff
        goog-dataproc-batch-uuid: 54b0b9d2-f0a1-4fdf-ae44-eead3f8e60e9
        goog-dataproc-drz-resource-uuid: batch-54b0b9d2-f0a1-4fdf-ae44-eead3f8e60e9
        goog-dataproc-location: us-central1
      operationType: BATCH
      name: projects/PROJECT_ID/regions/us-central1/operations/32287926-5f61-3572-b54a-fbad8940d6ef
    




## Query the table from BigQuery

Now that Spark has written your Iceberg table, you can query it right away in BigQuery using the 4-part **P.C.N.T** (**Project.Catalog.Namespace.Table**) syntax:

  1. In Cloud Shell, run the following `bq query` command:
         
         bq query --project_id=${PROJECT_ID} --location=${REGION} --use_legacy_sql=false \
             "SELECT * FROM \`${PROJECT_ID}.${LAKEHOUSE_CATALOG_ID}.quickstart_namespace.quickstart_table\`"

The output shows the three rows that you inserted with your PySpark job:
         
         +----+-------+
         | id | name  |
         +----+-------+
         |  1 | one   |
         |  2 | two   |
         |  3 | three |
         +----+-------+
         




Because the Lakehouse runtime catalog tracks the Iceberg metadata and handles storage access, BigQuery reads the underlying files in Cloud Storage as soon as Spark commits the snapshot.

At this same point, you can also read from or write to `quickstart_table` using any other Iceberg-compatible engine, such as Trino, Flink, or a self-managed Spark cluster. Because credential vending is enabled on your catalog, an external engine only needs the **BigLake Viewer** role (`roles/biglake.viewer`) on your project to read the table, or the **BigLake Editor** role (`roles/biglake.editor`) to also write data and commit new snapshots. To learn how to connect other engines, see [Set up the Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog#configure-catalog).

## Clean up

To avoid incurring unnecessary charges to your Google Cloud account, delete the resources you created in this quickstart. Deleting the table, namespace, and catalog removes the metadata registration from the Lakehouse runtime catalog, while deleting the bucket removes the underlying Parquet data and Iceberg metadata files stored in Cloud Storage:

  1. In Cloud Shell, delete the table from your catalog:
         
         gcloud biglake iceberg tables delete quickstart_table \
             --project=${PROJECT_ID} \
             --catalog=${LAKEHOUSE_CATALOG_ID} \
             --namespace=quickstart_namespace \
             --quiet

  2. Delete the namespace from your catalog:
         
         gcloud biglake iceberg namespaces delete quickstart_namespace \
             --project=${PROJECT_ID} \
             --catalog=${LAKEHOUSE_CATALOG_ID} \
             --quiet

  3. Delete your catalog:
         
         gcloud biglake iceberg catalogs delete ${LAKEHOUSE_CATALOG_ID} \
             --project=${PROJECT_ID} --quiet

  4. Delete your Cloud Storage bucket and all its contents:
         
         gcloud storage rm -r gs://${BUCKET_NAME}




## What's next

  * Try the [Create and query an Iceberg table using the Google Cloud console](https://docs.cloud.google.com/lakehouse/docs/query-iceberg-tables-console) quickstart to create namespaces and Iceberg tables in the UI and modify data using BigQuery data manipulation language (DML).
  * Try the [Set up cross-cloud data access codelab](https://docs.cloud.google.com/lakehouse/docs/cross-cloud-data-access-codelab) to query data across Amazon Web Services (AWS), AlloyDB for PostgreSQL, and Cloud Storage without ETL.
  * Learn about [multiple-bucket catalogs](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#storage-multiple-buckets) and the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint).
  * Learn how to [manage catalogs in the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/manage-catalogs).
  * Learn about [Apache Iceberg tables managed by Lakehouse](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
