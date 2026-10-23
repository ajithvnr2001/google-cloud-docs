---
url: https://docs.cloud.google.com/lakehouse/docs/migrate-dataproc-metastore/
title: Migrate metadata from Dataproc Metastore to Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:34.085077+00:00
---

# Migrate metadata from Dataproc Metastore to Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/migrate-dataproc-metastore/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Migrate metadata from Dataproc Metastore to Lakehouse Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to migrate metadata from a Dataproc Metastore service to an [Apache Iceberg REST catalog](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint) endpoint or a [Hive catalog](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore) endpoint, built on borderless Lakehouse.

#### Use cases

  * **Serverless Modernization:** Transition from a conventional Hive Metastore (HMS) to an automatically scaling, fully managed catalog, which eliminates the operational overhead of metastore management.
  * **Multi-Engine Collaboration:** Enable data sharing across engines—including Apache Spark, Apache Flink, Apache Hive, and BigQuery—so data scientists and analysts can work on the same tables simultaneously without file duplication.
  * **Direct BigQuery Integration:** Query open-source tables directly from BigQuery with high-performance execution.
  * **Unified Governance:** Consolidate metadata into a single source of truth for simplified data discovery and consistent policy enforcement.
  * **Modern Table Formats:** Seamlessly adopt advanced open formats like Apache Iceberg while maintaining full compatibility with your existing Hive workloads.



## Before you begin

  1. Make sure that an active [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/overview) service exists as the migration source.
  2. Make sure that the target Hive catalog or Iceberg catalog exists and includes the Cloud Storage buckets or paths where your source table data and metadata reside (for example, the [Dataproc Metastore warehouse bucket](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore#create-bucket), such as `gs://gcs-your-project-name-0825d7b3-0627-4637-8fd0-cc6271d00eb4/hive-warehouse`). 

If the destination catalog doesn't include the data location, table migration fails because the target catalog cannot register the tables. For Iceberg catalog creation, see [Set up the Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog#create_a_catalog).

To create a Hive catalog, see [Create a Lakehouse Hive catalog](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore).

  3. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Lakehouse, Dataproc Metastore APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,metastore.googleapis.com)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Lakehouse, Dataproc Metastore APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,metastore.googleapis.com)




### Required roles

To get the permissions that you need to trigger the migration, ask your administrator to grant you the following IAM roles on the Dataproc Metastore service: 

  * Start the migration: [Dataproc Metastore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`) 
  * Create Hive or Iceberg catalogs: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) 
  * Migrate metadata to destination catalogs using a target project: BigLake Admin (`roles/biglake.admin`) on the Dataproc Metastore service agent (`service-PROJECT_NUMBER@gcp-sa-metastore.iam.gserviceaccount.com`). 
  * Write migration reports for the report bucket (if not using the service artifacts bucket): Storage Object Admin (`roles/storage.objectAdmin`) on the Dataproc Metastore service agent (`service-PROJECT_NUMBER@gcp-sa-metastore.iam.gserviceaccount.com`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## How a migration works

The migration process works as follows:

  1. **Choose your target catalog** : Select the destination Hive catalog endpoint or Apache Iceberg REST catalog endpoint for your migration.
  2. **Trigger migration** : Run the [`gcloud metastore services migrations start`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/migrations/start) command or call the [`startMigration`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/startMigration) method on your Dataproc Metastore service to initiate the migration.
  3. **Poll for status** : Monitor the progress of the migration using the [`gcloud metastore services migrations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/migrations/describe) command or by polling the [target execution](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation).
  4. **Review reports** : Review the detailed JSON reports written to your specified Cloud Storage path to verify the results.



## Run a migration

To run a migration, you trigger the migration process and then monitor its progress.

### Start the migration

To trigger the metadata migration on a Dataproc Metastore service, use the Google Cloud console, the `gcloud` CLI, or the REST API.

###  Console 

  1. In the Google Cloud console, go to the **Dataproc Metastore** page.

[Go to Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. In the metastore services list, click the name of the service you want to migrate.

  3. On the service detail page, click **Migrate to Lakehouse** in the top navigation bar.

  4. For **Migration name** , enter a display name for your migration.

  5. For **Migration type** , select **Backfill migration** to perform the migration, or **Dry run** to validate the migration without writing metadata to the destination catalog.

  6. Configure the target settings:

     * **Reports** : (Optional) Select the Cloud Storage path to save your migration status report. If not specified, the report is generated in your Dataproc Metastore service's artifacts bucket.
     * **Conflict handling** : Select if you want to skip or overwrite duplicate database entries.
  7. For **Destination** , select the types of catalog you want to migrate to, **Iceberg REST catalog endpoint** or **Hive metastore**. You can migrate to one catalog or both catalogs at the same time, depending on the type of tables you need to migrate from your source database.

If you are migrating to the Iceberg REST catalog:

     1. For **Project** , select the project that contains the catalog you want to migrate to.
     2. For **Iceberg REST catalog** , select the catalog you want to migrate to, or click **Create catalog** to create a new one.

If you are migrating to the Hive catalog:

     1. For **Project** , select the project that contains the catalog you want to migrate to.
     2. For **Hive catalog** , select the catalog you want to migrate to, or click **Create catalog** to create a new one.
  8. Click **Start Migration**.




You are automatically redirected to the **Migrations** tab. Under **Managed Migrations** , your migration is listed and the state continues to update until the migration is finished.

###  gcloud 

To start the migration using `gcloud`, run the [`gcloud metastore services migrations start`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/migrations/start) command:
    
    
    gcloud metastore services migrations start SERVICE_ID \
        --location=REGION \
        --hive-catalog="projects/PROJECT_ID/catalogs/HIVE_CATALOG_ID" \
        --hive-databases="HIVE_DB_1,HIVE_DB_2" \
        --iceberg-catalog="projects/PROJECT_ID/catalogs/ICEBERG_CATALOG_ID" \
        --iceberg-namespaces="ICEBERG_NAMESPACE_1,ICEBERG_NAMESPACE_2" \
        --async
    

**Note:** You can specify `*` for `--hive-databases` or `--iceberg-namespaces` to migrate all databases or namespaces.

Replace the following:

  * `SERVICE_ID`: the ID of the Dataproc Metastore service
  * `REGION`: the region of the Dataproc Metastore service
  * `PROJECT_ID`: your Google Cloud project ID
  * `HIVE_CATALOG_ID`: the destination Hive catalog ID
  * `HIVE_DB_1`, `HIVE_DB_2`: the Hive databases to migrate.
  * `ICEBERG_CATALOG_ID`: the destination Iceberg catalog ID
  * `ICEBERG_NAMESPACE_1`, `ICEBERG_NAMESPACE_2`: the Iceberg namespaces to migrate.



###  REST 

To trigger the metadata migration using the REST API, call the [`startMigration`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/startMigration) method with a [`BigLakeMetastoreMigrationConfig`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.migrationExecutions#BigLakeMetastoreMigrationConfig) configuration:

**Note:** You can use `["*"]` for `databases` or `namespaces` to migrate all databases or namespaces.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "migrationExecution": {
            "biglakeMetastoreMigrationConfig": {
              "mode": "BACKFILL",
              "dryRun": false,
              "reportPath": "gs://BUCKET_NAME/PATH/",
              "conflictPolicy": "SKIP",
              "hiveConfig": {
                "catalog": "projects/PROJECT_ID/catalogs/HIVE_CATALOG_ID",
                "databases": ["HIVE_DB_1", "HIVE_DB_2"]
              },
              "icebergConfig": {
                "catalog": "projects/PROJECT_ID/catalogs/ICEBERG_CATALOG_ID",
                "namespaces": ["ICEBERG_NAMESPACE_1", "ICEBERG_NAMESPACE_2"]
              }
            }
          }
        }' \
        "https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/services/SERVICE_ID:startMigration"
    

Replace the following:

  * `BUCKET_NAME`: the name of the Cloud Storage bucket for reports
  * `PATH`: the path in the bucket for reports
  * `PROJECT_ID`: your Google Cloud project ID
  * `HIVE_CATALOG_ID`: the destination Hive catalog ID
  * `HIVE_DB_1`, `HIVE_DB_2`: the Hive databases to migrate.
  * `ICEBERG_CATALOG_ID`: the destination Iceberg catalog ID
  * `ICEBERG_NAMESPACE_1`, `ICEBERG_NAMESPACE_2`: the Iceberg namespaces to migrate.
  * `REGION`: the region of the Dataproc Metastore service
  * `SERVICE_ID`: the ID of the Dataproc Metastore service



### Poll the migration execution

The request starts a [long-running operation](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation) (LRO) and returns a unique migration execution ID. You can monitor the progress of your run using the `gcloud` CLI or the REST API:

###  gcloud 

To describe the migration execution using `gcloud`, run the [`gcloud metastore services migrations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/migrations/describe) command:
    
    
    gcloud metastore services migrations describe MIGRATION_EXECUTION_ID \
        --service=SERVICE_ID \
        --location=REGION
    

Replace the following:

  * `MIGRATION_EXECUTION_ID`: the ID of the migration execution returned in the previous step
  * `SERVICE_ID`: the ID of the Dataproc Metastore service
  * `REGION`: the region of the Dataproc Metastore service



###  REST 

To monitor the progress of your run using the REST API, call the [`get`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.migrationExecutions/get) method on that execution path:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/services/SERVICE_ID/migrationExecutions/MIGRATION_EXECUTION_ID"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID
  * `REGION`: the region of the Dataproc Metastore service
  * `SERVICE_ID`: the ID of the Dataproc Metastore service
  * `MIGRATION_EXECUTION_ID`: the ID of the migration execution returned in the previous step



## Detailed migration report

After the migration (backfill or dry run) completes, the migration tool writes two detailed JSON report files based on the [`MigrationReport`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/MigrationReport) schema to the target Cloud Storage path specified in `reportPath`:

  * `summary.json`: Contains the high-level aggregated [`MigrationSummary`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.migrationExecutions#MigrationSummary) structure.
  * `full_report.json`: Contains a detailed, more granular migration report. For more information, see [`CatalogReport`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/CatalogReport).



To view the report in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Dataproc Metastore** page.

[Go to Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. In the metastore services list, click the display name of the service that contains the report.

The **Migrations** page opens.

  3. Under **Managed Migrations** , select the name of the migration that contains the report.

The **Migration details** page opens, displaying details about the migrated databases and tables and their migration status.




## Limitations

  * The destination catalog must include the Cloud Storage buckets or paths where the source table data and metadata reside (such as the [Dataproc Metastore warehouse bucket](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore#create-bucket)). If the target catalog is not configured with the data bucket location, the destination catalog cannot register the tables and table migration fails.
  * The tool only supports a one-time backfill. Any metadata changes to your source Dataproc Metastore after the migration don't propagate automatically. You must rerun the migration to sync the target catalog with your source.
  * The migration is bound by the limitations of the destination catalogs. If a Dataproc Metastore table contains a schema structure or property unsupported by the target catalog (such as complex types), the migration for that specific table fails.
  * Dataproc Metastore permissions for tables or databases aren't migrated over to Lakehouse.



## What's next

  * Learn more about the [Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs).
  * Learn how to [Set up Spark and Hive with the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore).
  * Learn how to [Query Iceberg tables with Lakehouse runtime catalog, Spark, and BigQuery](https://docs.cloud.google.com/lakehouse/docs/query-iceberg-tables-with-lakehouse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
