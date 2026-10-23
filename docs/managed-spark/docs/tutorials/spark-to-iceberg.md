---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-to-iceberg/
title: Transform data and write to an Apache Iceberg table \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:32.190332+00:00
---

# Transform data and write to an Apache Iceberg table  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-to-iceberg/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Transform data and write to an Apache Iceberg table Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to read New York City (NYC) taxi trip records from a Parquet file on Cloud Storage, transform them with Apache Spark on Managed Service for Apache Spark serverless runtime `3.0`, and write the aggregated results into an Apache Iceberg table using the BigLake REST Catalog.

In this tutorial, you complete the following tasks:

  1. Stage NYC taxi Parquet data.
  2. Write the PySpark job script.
  3. Submit the serverless batch job.
  4. Verify and query the Iceberg table.



## Before you begin

Set up your project and perform other startup tasks.

### Set up your Google Cloud project

Set up your project as needed to enable APIs, grant Identity and Access Management (IAM) roles, authenticate Application Default Credentials, and create a Cloud Storage bucket.

#### Enable APIs

Use the Google Cloud console to enable the required APIs.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc, Cloud Storage, BigQuery, BigLake, Cloud Logging, Compute Engine, Cloud Resource Manager, and Dataproc Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,storage.googleapis.com,bigquery.googleapis.com,biglake.googleapis.com,logging.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com,dataprocrm.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataproc, Cloud Storage, BigQuery, BigLake, Cloud Logging, Compute Engine, Cloud Resource Manager, and Dataproc Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,storage.googleapis.com,bigquery.googleapis.com,biglake.googleapis.com,logging.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com,dataprocrm.googleapis.com)

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Create a Cloud Storage bucket: 
         
         gcloud storage buckets create gs://BUCKET_NAME

Replace `BUCKET_NAME` with a bucket name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). 



### Grant IAM roles if needed

Certain IAM roles are required to run the examples on this page. Depending on organization policies, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects,folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**User roles**

By default, Managed Service for Apache Spark serverless runtime `3.0` runs under your end-user credentials (EUC). Service account roles are not required. For more information, see [Personas and serverless IAM roles](https://docs.cloud.google.com/managed-spark/docs/concepts/personas-and-serverless-iam-roles#choose-a-runtime-version).

To get the permissions that you need to submit a serverless batch workload, ask your administrator to grant you the following IAM roles: 

  * Run workloads on Runtime 3.x (default EUC): 
    * [Dataproc Serverless Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`) on the project
    * [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) on the project
    * [BigQuery Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`) on the project
    * [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) on the project



Your administrator can run the following bash script to grant roles to your user account.
    
    
    ```bash
    for ROLE in \
      roles/dataproc.serverlessEditor \
      roles/biglake.admin \
      roles/bigquery.admin \
      roles/storage.objectAdmin
    do
      gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
        --member="user:${USER_ACCOUNT}" \
        --role="${ROLE}"
    done
    ```
    

### Configure environment variables

Run the following bash script to set shell environment variables used throughout this tutorial.

**Note:** Run all commands in this tutorial within the same terminal session so that these environment variables remain set. If you open a new terminal window or disconnect, re-run this configuration block.
    
    
    # 1. Active project ID, user account, and project number
    export PROJECT_ID="$(gcloud config get-value project)"
    export USER_ACCOUNT="$(gcloud config get-value account)"
    export PROJECT_NUMBER="$(gcloud projects describe "${PROJECT_ID}" --format="value(projectNumber)")"
    
    # 2. Regional deployment and networking settings
    export REGION="us-central1"
    export SUBNET_NAME="default"
    export SUBNET_RANGE="10.128.0.0/20"
    
    # 3. Storage and BigLake Iceberg catalog resources
    export BUCKET_NAME="BUCKET_NAME"
    export OUTPUT_CATALOG_NAME="lakehouse"
    export OUTPUT_DATASET_NAME="nyc_taxi"
    export OUTPUT_TABLE_NAME="yellow_trips_analyzed"
    export INPUT_PARQUET_PATH="gs://${BUCKET_NAME}/raw/nyc_taxi/yellow_tripdata_2024-01.parquet"
    

Replace the following:

  * `BUCKET_NAME`: the name of the Cloud Storage bucket that you created in Set up your Google Cloud project.



## Step 1. Create a BigLake Iceberg catalog

The BigLake Iceberg REST Catalog allows Spark workloads and BigQuery to discover, read, and write Iceberg tables.

  1. Create the BigLake Iceberg catalog.

Create the catalog with its default location pointing to your warehouse path in Cloud Storage.
         
         gcloud biglake iceberg catalogs create "${OUTPUT_CATALOG_NAME}" \
           --project="${PROJECT_ID}" \
           --catalog-type=biglake \
           --default-location="gs://${BUCKET_NAME}/warehouse" \
           --credential-mode=end-user
         

  2. Verify catalog health.
         
         gcloud biglake iceberg catalogs describe "${OUTPUT_CATALOG_NAME}" --project="${PROJECT_ID}"
         




## Step 2. Stage the NYC taxi Parquet data

The NYC Taxi & Limousine Commission (TLC) publishes monthly trip records in Parquet. Download one month of data and copy it to your Cloud Storage bucket.
    
    
    curl -L -o yellow_tripdata_2024-01.parquet \
      https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet
    
    gcloud storage cp yellow_tripdata_2024-01.parquet "${INPUT_PARQUET_PATH}"
    
    gcloud storage ls "${INPUT_PARQUET_PATH}"
    

## Step 3. Write the PySpark job script

Create `taxi_to_iceberg.py`. This script reads the raw Parquet records, filters invalid trips, computes daily passenger, fare, tip, and revenue aggregates, and writes an Iceberg table using the BigLake REST catalog.
    
    
    """Read NYC taxi Parquet from Cloud Storage and write aggregates to an Iceberg table."""
    
    import sys
    
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import (
        avg,
        col,
        count,
        round as spark_round,
        sum as spark_sum,
        to_date,
        when,
    )
    
    def main():
      if len(sys.argv) < 5:
        print(
            "Usage: taxi_to_iceberg.py <input_parquet_path> <catalog_name>"
            " <dataset_name> <table_name>"
        )
        sys.exit(1)
    
      input_path, catalog_name, dataset_name, table_name = sys.argv[1:5]
      full_table = f"`{catalog_name}`.{dataset_name}.{table_name}"
    
      # Iceberg extensions are enabled here; catalog properties are passed at
      # submit time via --flags-file (see Step 4).
      spark = (
          SparkSession.builder.appName("NYC Taxi Parquet to Iceberg")
          .config(
              "spark.sql.extensions",
              "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
          )
          .getOrCreate()
      )
    
      print(f"Reading raw Parquet data from: {input_path}")
      raw_df = spark.read.parquet(input_path)
      raw_df.printSchema()
    
      cleaned_df = (
          raw_df.filter(
              (col("trip_distance") > 0)
              & (col("fare_amount") > 0)
              & (col("passenger_count") > 0)
          )
          .withColumn("trip_date", to_date(col("tpep_pickup_datetime")))
          .withColumn(
              "tip_pct",
              when(
                  col("fare_amount") > 0,
                  spark_round((col("tip_amount") / col("fare_amount")) * 100, 2),
              ).otherwise(0.0),
          )
      )
    
      aggregated_df = (
          cleaned_df.groupBy("trip_date", "payment_type")
          .agg(
              count("*").alias("total_trips"),
              spark_sum("passenger_count").alias("total_passengers"),
              spark_round(avg("trip_distance"), 2).alias("avg_distance"),
              spark_round(avg("fare_amount"), 2).alias("avg_fare"),
              spark_round(avg("tip_pct"), 2).alias("avg_tip_percentage"),
              spark_round(spark_sum("total_amount"), 2).alias("total_revenue"),
          )
          .orderBy("trip_date", "payment_type")
      )
    
      aggregated_df.show(10, truncate=False)
    
      # Create the namespace, then write with DataFrameWriterV2 (writeTo).
      spark.sql(f"CREATE NAMESPACE IF NOT EXISTS `{catalog_name}`.{dataset_name}")
      spark.catalog.setCurrentCatalog(catalog_name)
      aggregated_df.writeTo(full_table).using("iceberg").createOrReplace()
    
      print(f"Wrote Iceberg table: {full_table}")
      spark.stop()
    
    if __name__ == "__main__":
      main()
    

**Important:** When writing to a BigLake Iceberg catalog, always use the `writeTo` (`DataFrameWriterV2`) API, set the current catalog first, ensure the namespace exists, and surround the catalog name with backticks in SQL and `writeTo` calls.

## Step 4. Submit the serverless batch job

Define the catalog properties in a configuration file and submit the batch job to Managed Service for Apache Spark serverless.

  1. Define Iceberg catalog properties in a YAML flags file.

Create `iceberg-flags.yaml` that contains the BigLake REST Catalog properties. The Google Cloud CLI reads this file using the `--flags-file` argument.
         
         cat <<EOF > iceberg-flags.yaml
         --properties:
           spark.sql.catalog.${OUTPUT_CATALOG_NAME}: org.apache.iceberg.spark.SparkCatalog
           spark.sql.catalog.${OUTPUT_CATALOG_NAME}.type: rest
           spark.sql.catalog.${OUTPUT_CATALOG_NAME}.uri: https://biglake.googleapis.com/iceberg/v1/restcatalog
           spark.sql.catalog.${OUTPUT_CATALOG_NAME}.io-impl: org.apache.iceberg.gcp.gcs.GCSFileIO
           spark.sql.catalog.${OUTPUT_CATALOG_NAME}.header.x-goog-user-project: ${PROJECT_ID}
           spark.sql.catalog.${OUTPUT_CATALOG_NAME}.warehouse: bl://projects/${PROJECT_ID}/catalogs/${OUTPUT_CATALOG_NAME}
           spark.sql.catalog.${OUTPUT_CATALOG_NAME}.rest.auth.type: org.apache.iceberg.gcp.auth.GoogleAuthManager
           spark.sql.extensions: org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
         EOF
         

Property | Purpose / Description  
---|---  
`spark.sql.catalog.${OUTPUT_CATALOG_NAME}` | Registers Apache Iceberg's catalog plugin (`org.apache.iceberg.spark.SparkCatalog`) for the custom catalog name.  
`type` | Sets the catalog type to use the Apache Iceberg REST catalog specification (`rest`).  
`uri` | The REST API endpoint URL for BigLake REST Metastore.  
`io-impl` | Configures Iceberg to use Cloud Storage FileIO (`org.apache.iceberg.gcp.gcs.GCSFileIO`) for high-performance data and metadata read/write operations.  
`header.x-goog-user-project` | Passes your Google Cloud project ID as a request header for BigLake API quota and billing attribution.  
`warehouse` | The BigLake Resource URI (`bl://projects/...`) pointing to the specific catalog resource in your Google Cloud project.  
`rest.auth.type` | Automatically authenticates REST catalog API calls using Google Cloud credentials (`org.apache.iceberg.gcp.auth.GoogleAuthManager`).  
`spark.sql.extensions` | Enables Iceberg SQL extensions and `DataFrameWriterV2` (`writeTo`) support in Spark SQL.  
  2. Submit the PySpark batch job.

Set the runtime version and target table variables, then submit the batch job using `gcloud dataproc batches submit pyspark`:
         
         export RUNTIME_VERSION="3.0"
         export SCRIPT_FILE="taxi_to_iceberg.py"
         
         gcloud dataproc batches submit pyspark "${SCRIPT_FILE}" \
           --flags-file=iceberg-flags.yaml \
           --project="${PROJECT_ID}" \
           --region="${REGION}" \
           --version="${RUNTIME_VERSION}" \
           --subnet="${SUBNET_NAME}" \
           --deps-bucket="gs://${BUCKET_NAME}" \
           -- \
           "${INPUT_PARQUET_PATH}" \
           "${OUTPUT_CATALOG_NAME}" \
           "${OUTPUT_DATASET_NAME}" \
           "${OUTPUT_TABLE_NAME}"
         

Notes:

     * When submitting a local Python script, the gcloud CLI uses `--deps-bucket` to stage the script file into Cloud Storage before starting the job.
     * On the first runtime `3.0` submission using your end-user credentials (EUC), you will receive a one-time OAuth consent prompt. Grant access and resubmit.
     * When using runtime `3.0`, you might observe warnings from `DataprocRMExecutorsAllocator` in driver logs during executor teardown. These warnings are transient and nonfatal assuming the batch reaches `SUCCEEDED`.



## Step 5: Verify and query the Iceberg table

Verify the output files in Cloud Storage, confirm the table registration in BigLake, and query the table using BigQuery.

  1. Inspect Iceberg files in Cloud Storage.

Verify that the Iceberg warehouse contains the expected `metadata/` and `data/` directories:
         
         gcloud storage ls -r "gs://${BUCKET_NAME}/warehouse/${OUTPUT_DATASET_NAME}/${OUTPUT_TABLE_NAME}/"
         

  2. Verify table registration with BigLake.
         
         gcloud biglake iceberg tables describe "${OUTPUT_TABLE_NAME}" \
           --catalog="${OUTPUT_CATALOG_NAME}" \
           --namespace="${OUTPUT_DATASET_NAME}" \
           --project="${PROJECT_ID}"
         

  3. Query from BigQuery.

BigLake automatically registers the Iceberg table in BigQuery:
         
         bq query \
           --project_id="${PROJECT_ID}" \
           --location="${REGION}" \
           --use_legacy_sql=false \
           "SELECT trip_date, payment_type, total_trips, avg_fare, avg_tip_percentage, total_revenue
            FROM \`${PROJECT_ID}.${OUTPUT_CATALOG_NAME}.${OUTPUT_DATASET_NAME}.${OUTPUT_TABLE_NAME}\`
            ORDER BY total_trips DESC LIMIT 10"
         




## Clean up

To avoid incurring charges to your Google Cloud account, delete the resources you created in this tutorial.
    
    
    # 1. Delete BigLake Iceberg catalog, and table metadata
    gcloud biglake iceberg catalogs delete "${OUTPUT_CATALOG_NAME}" \
      --project="${PROJECT_ID}" --quiet 2>/dev/null || true
    
    # 2. Delete BigQuery dataset (if created)
    bq rm -r -f -d "${PROJECT_ID}:${OUTPUT_DATASET_NAME}" 2>/dev/null || true
    
    # 3. Delete Cloud Storage bucket and warehouse files
    gcloud storage rm -r "gs://${BUCKET_NAME}"
    

## What's next

  * Learn more about [Managed Service for Apache Spark serverless batch workloads](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch).
  * Explore [Personas and serverless IAM roles](https://docs.cloud.google.com/managed-spark/docs/concepts/personas-and-serverless-iam-roles).
  * Read about [BigLake Iceberg tables in BigQuery](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery).
  * See [Troubleshoot common Lakehouse issues](https://docs.cloud.google.com/lakehouse/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
