---
url: https://docs.cloud.google.com/composer/docs/composer-2/run-data-analytics-dag-azure/
title: Run a Data Analytics DAG in Google Cloud using data from Azure \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:18.371453+00:00
---

# Run a Data Analytics DAG in Google Cloud using data from Azure  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/run-data-analytics-dag-azure/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Run a Data Analytics DAG in Google Cloud using data from Azure Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/run-data-analytics-dag-azure "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/run-data-analytics-dag-azure "View this page for Managed Airflow \(Legacy Gen 1\)")

This tutorial is a modification of [Run a Data Analytics DAG in Google Cloud](https://docs.cloud.google.com/composer/docs/composer-2/run-data-analytics-dag-googlecloud) that shows how to connect your Managed Airflow environment to Microsoft Azure to utilize data stored there. It shows how to use Managed Airflow to create an [Apache Airflow](http://airflow.apache.org/) DAG. The DAG joins data from a BigQuery public dataset and a CSV file stored in an [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/#overview) and then runs a Managed Service for Apache Spark batch job to process the joined data.

The BigQuery public dataset in this tutorial is [ghcn_d](https://console.cloud.google.com/marketplace/details/noaa-public/ghcn-d), an integrated database of climate summaries across the globe. The [CSV file](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/2022_airflow_summit/holidays.csv) contains information about the dates and names of US holidays from 1997 to 2021.

The question we want to answer using the DAG is: "How warm was it in Chicago on Thanksgiving for the past 25 years?"

## Objectives

  * Create a Managed Airflow environment in the default configuration
  * Create a blob in Azure
  * Create an empty BigQuery dataset
  * Create a new Cloud Storage bucket
  * Create and run a DAG that includes the following tasks: 
    * Load an external dataset from Azure Blob Storage to Cloud Storage
    * Load an external dataset from Cloud Storage to BigQuery
    * Join two datasets in BigQuery
    * Run a data analytics PySpark job



## Before you begin

### Enable APIs

Enable the following APIs:

###  Console 

Enable the Managed Service for Apache Spark, Managed Airflow, BigQuery, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,composer.googleapis.com,bigquery.googleapis.com,storage.googleapis.com)

###  gcloud 

Enable the Managed Service for Apache Spark, Managed Airflow, BigQuery, Cloud Storage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable dataproc.googleapis.com  composer.googleapis.com  bigquery.googleapis.com  storage.googleapis.com

### Grant permissions

Grant the following roles and permissions to your user account:

  * Grant [roles for managing Managed Airflow environments and environment buckets](https://docs.cloud.google.com/composer/docs/composer-2/access-control#manage_environments_and_environment_buckets).

  * Grant the **BigQuery Data Owner** (`roles/bigquery.dataOwner`) role to [create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets#before_you_begin).

  * Grant the **Storage Admin** (`roles/storage.admin`) role to [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).




### Create and prepare your Managed Airflow environment

  1. [Create a Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments) with default parameters:

     * Choose a US-based region.
     * Choose the latest [Managed Airflow version](https://docs.cloud.google.com/composer/docs/composer-versions).
**Note:** The BigQuery portion of this tutorial must run in the `US` multiregion. We recommend choosing a US region for your Managed Airflow environment to reduce cost and latency, but the tutorial can still run if your Managed Airflow environment is in another region.
  2. Grant the following roles to the service account used in your Managed Airflow environment in order for the Airflow workers to successfully run DAG tasks:

     * **BigQuery User** (`roles/bigquery.user`)
     * **BigQuery Data Owner** (`roles/bigquery.dataOwner`)
     * **Service Account User** (`roles/iam.serviceAccountUser`)
     * **Dataproc Editor** (`roles/dataproc.editor`)
     * **Dataproc Worker** (`roles/dataproc.worker`)



### Create and modify related resources in Google Cloud

  1. Install the `apache-airflow-providers-microsoft-azure` [PyPI package](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies#install-pypi) in your Managed Airflow environment.

  2. [Create an empty BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset) with the following parameters:

     * **Name** : `holiday_weather`
     * **Region** : `US`
  3. [Create a new Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in the `US` multiregion.

  4. Run the following command to [enable private Google access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) on the default subnet in the region where you would like to run Managed Service for Apache Spark to fulfill [networking requirements](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/network). We recommend using the same region as your Managed Airflow environment.
         
         gcloud compute networks subnets update default \
             --region DATAPROC_SERVERLESS_REGION \
             --enable-private-ip-google-access
         


**Caution:** The empty BigQuery dataset must be located in the US region to satisfy [colocation requirements](https://docs.cloud.google.com/bigquery-transfer/docs/locations#colocation_required) for transferring the BigQuery public dataset [ghcn_d](https://console.cloud.google.com/marketplace/details/noaa-public/ghcn-d).

### Create related resources in Azure

  1. [Create a storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#create-a-storage-account-1) with the default settings.

  2. [Get the access key and connection string](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal#view-account-access-keys) for your storage account.

  3. [Create a container](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container) with default options in your newly created storage account.

  4. [Grant the Storage Blob Delegator](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal?tabs=current) role for the container created in the previous step.

  5. Upload [holidays.csv](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/2022_airflow_summit/holidays.csv) to [create a block blob](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal#upload-a-block-blob) with default options in Azure portal.

  6. [Create a SAS token](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/create-sas-tokens?tabs=Containers#create-sas-tokens-in-the-azure-portal) for the block blob you created in the previous step in the Azure portal.

     * **Signing method** : User delegation key
     * **Permissions** : Read
     * **Allowed IP address** : None
     * **Allowed protocols** : HTTPS only

**Note:** SAS tokens are a secure and [documented way of accessing your Azure storage account](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/create-sas-tokens?tabs=Containers). However, they are time-sensitive and each has an expiration date. Please choose an expiration date accordingly.

### Connect to Azure from Managed Airflow

**Note:** We recommend to **store all credentials for connections in Secret Manager**. If you plan to use this tutorial for production purposes, consider configuring Secret Manager for your environment. For more information, see [Configure Secret Manager for your environment](https://docs.cloud.google.com/composer/docs/composer-2/configure-secret-manager).

Add your Microsoft Azure [connection](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html) using the Airflow UI:

  1. Go to **Admin > Connections**.

  2. Create a new connection with the following configuration:

     * **Connection Id:** `azure_blob_connection`
     * **Connection Type:** `Azure Blob Storage`
     * **Blob Storage Login:** your storage account name
     * **Blob Storage Key:** the access key for your storage account
     * **Blob Storage Account Connection String:** your storage account connection string
     * **SAS Token:** the SAS token generated from your blob



## Data processing using Managed Service for Apache Spark

### Explore the example PySpark Job

The code shown below is an example PySpark job that converts temperature from tenths of a degree in Celsius to degrees Celsius. This job converts temperature data from the dataset into a different format.
    
    
    import sys
    
    
    from py4j.protocol import Py4JJavaError
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col
    
    
    if __name__ == "__main__":
        BUCKET_NAME = sys.argv[1]
        READ_TABLE = sys.argv[2]
        WRITE_TABLE = sys.argv[3]
    
        # Create a SparkSession, viewable via the Spark UI
        spark = SparkSession.builder.appName("data_processing").getOrCreate()
    
        # Load data into dataframe if READ_TABLE exists
        try:
            df = spark.read.format("bigquery").load(READ_TABLE)
        except Py4JJavaError as e:
            raise Exception(f"Error reading {READ_TABLE}") from e
    
        # Convert temperature from tenths of a degree in celsius to degrees celsius
        df = df.withColumn("value", col("value") / 10)
        # Display sample of rows
        df.show(n=20)
    
        # Write results to GCS
        if "--dry-run" in sys.argv:
            print("Data will not be uploaded to BigQuery")
        else:
            # Set GCS temp location
            temp_path = BUCKET_NAME
    
            # Saving the data to BigQuery using the "indirect path" method and the spark-bigquery connector
            # Uses the "overwrite" SaveMode to ensure DAG doesn't fail when being re-run
            # See https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#save-modes
            # for other save mode options
            df.write.format("bigquery").option("temporaryGcsBucket", temp_path).mode(
                "overwrite"
            ).save(WRITE_TABLE)
            print("Data written to BigQuery")

### Upload the PySpark file to Cloud Storage

To upload the PySpark file to Cloud Storage:

  1. Save [data_analytics_process.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/2022_airflow_summit/data_analytics_process.py) to your local machine.

  2. In the Google Cloud console go to the **Cloud Storage browser** page:

[Go to Cloud Storage browser](https://console.cloud.google.com/storage)

  3. Click the name of the bucket you created earlier.

  4. In the **Objects** tab for the bucket, click the **Upload files** button, select `data_analytics_process.py` in the dialog that appears, and click **Open**.




## Data analytics DAG

### Explore the example DAG

The DAG uses multiple operators to transform and unify the data:

  * The [`AzureBlobStorageToGCSOperator`](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/_api/airflow/providers/microsoft/azure/transfers/azure_blob_to_gcs/index.html) transfers the [holidays.csv](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/2022_airflow_summit/holidays.csv) file from your Azure block blob to your Cloud Storage bucket.

  * The [`GCSToBigQueryOperator`](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/transfers/gcs_to_bigquery/index.html) ingests the [holidays.csv](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/2022_airflow_summit/holidays.csv) file from Cloud Storage to a new table in the BigQuery `holidays_weather` dataset you created earlier.

  * The [`DataprocCreateBatchOperator`](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/dataproc.html#create-a-batch) creates and runs a PySpark batch job using Managed Service for Apache Spark.

  * The [`BigQueryInsertJobOperator`](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/bigquery.html#execute-bigquery-jobs) joins the data from [holidays.csv](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/2022_airflow_summit/holidays.csv) on the "Date" column with weather data from the BigQuery public dataset [ghcn_d](https://console.cloud.google.com/marketplace/details/noaa-public/ghcn-d). The `BigQueryInsertJobOperator` tasks are dynamically generated using a for loop, and these tasks are in a [`TaskGroup`](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html?highlight=taskgroup#taskgroups) for better readability in the Graph View of the Airflow UI.


**Important:** The `DataprocCreateBatchOperator` is available in the `apache-airflow-providers-google` package versions 6.2.0 and later. The required versions of this package are preinstalled in your environment starting from [Managed Airflow versions 1.17.10 and 2.0.3](https://docs.cloud.google.com/composer/docs/composer-versions).
    
    
    import datetime
    
    from airflow import models
    from airflow.providers.google.cloud.operators import dataproc
    from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
    from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
        GCSToBigQueryOperator,
    )
    from airflow.providers.microsoft.azure.transfers.azure_blob_to_gcs import (
        AzureBlobStorageToGCSOperator,
    )
    from airflow.utils.task_group import TaskGroup
    
    PROJECT_NAME = "{{var.value.gcp_project}}"
    REGION = "{{var.value.gce_region}}"
    
    # BigQuery configs
    BQ_DESTINATION_DATASET_NAME = "holiday_weather"
    BQ_DESTINATION_TABLE_NAME = "holidays_weather_joined"
    BQ_NORMALIZED_TABLE_NAME = "holidays_weather_normalized"
    
    # Dataproc configs
    BUCKET_NAME = "{{var.value.gcs_bucket}}"
    PYSPARK_JAR = "gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar"
    PROCESSING_PYTHON_FILE = f"gs://{BUCKET_NAME}/data_analytics_process.py"
    
    # Azure configs
    AZURE_BLOB_NAME = "{{var.value.azure_blob_name}}"
    AZURE_CONTAINER_NAME = "{{var.value.azure_container_name}}"
    
    BATCH_ID = "data-processing-{{ ts_nodash | lower}}"  # Dataproc serverless only allows lowercase characters
    BATCH_CONFIG = {
        "pyspark_batch": {
            "jar_file_uris": [PYSPARK_JAR],
            "main_python_file_uri": PROCESSING_PYTHON_FILE,
            "args": [
                BUCKET_NAME,
                f"{BQ_DESTINATION_DATASET_NAME}.{BQ_DESTINATION_TABLE_NAME}",
                f"{BQ_DESTINATION_DATASET_NAME}.{BQ_NORMALIZED_TABLE_NAME}",
            ],
        },
        "environment_config": {
            "execution_config": {
                "service_account": "{{var.value.dataproc_service_account}}"
            }
        },
    }
    
    yesterday = datetime.datetime.combine(
        datetime.datetime.today() - datetime.timedelta(1), datetime.datetime.min.time()
    )
    
    default_dag_args = {
        # Setting start date as yesterday starts the DAG immediately when it is
        # detected in the Cloud Storage bucket.
        "start_date": yesterday,
        # To email on failure or retry set 'email' arg to your email and enable
        # emailing here.
        "email_on_failure": False,
        "email_on_retry": False,
    }
    
    with models.DAG(
        "azure_to_gcs_dag",
        # Continue to run DAG once per day
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args,
    ) as dag:
        azure_blob_to_gcs = AzureBlobStorageToGCSOperator(
            task_id="azure_blob_to_gcs",
            # Azure args
            blob_name=AZURE_BLOB_NAME,
            container_name=AZURE_CONTAINER_NAME,
            wasb_conn_id="azure_blob_connection",
            filename=f"https://console.cloud.google.com/storage/browser/{BUCKET_NAME}/",
            # GCP args
            gcp_conn_id="google_cloud_default",
            object_name="holidays.csv",
            bucket_name=BUCKET_NAME,
            gzip=False,
            impersonation_chain=None,
        )
    
        create_batch = dataproc.DataprocCreateBatchOperator(
            task_id="create_batch",
            project_id=PROJECT_NAME,
            region=REGION,
            batch=BATCH_CONFIG,
            batch_id=BATCH_ID,
        )
    
        load_external_dataset = GCSToBigQueryOperator(
            task_id="run_bq_external_ingestion",
            bucket=BUCKET_NAME,
            source_objects=["holidays.csv"],
            destination_project_dataset_table=f"{BQ_DESTINATION_DATASET_NAME}.holidays",
            source_format="CSV",
            schema_fields=[
                {"name": "Date", "type": "DATE"},
                {"name": "Holiday", "type": "STRING"},
            ],
            skip_leading_rows=1,
            write_disposition="WRITE_TRUNCATE",
        )
    
        with TaskGroup("join_bq_datasets") as bq_join_group:
            for year in range(1997, 2022):
                BQ_DATASET_NAME = f"bigquery-public-data.ghcn_d.ghcnd_{str(year)}"
                BQ_DESTINATION_TABLE_NAME = "holidays_weather_joined"
                # Specifically query a Chicago weather station
                WEATHER_HOLIDAYS_JOIN_QUERY = f"""
                SELECT Holidays.Date, Holiday, id, element, value
                FROM `{PROJECT_NAME}.holiday_weather.holidays` AS Holidays
                JOIN (SELECT id, date, element, value FROM {BQ_DATASET_NAME} AS Table
                WHERE Table.element="TMAX" AND Table.id="USW00094846") AS Weather
                ON Holidays.Date = Weather.Date;
                """
    
                # For demo purposes we are using WRITE_APPEND
                # but if you run the DAG repeatedly it will continue to append
                # Your use case may be different, see the Job docs
                # https://cloud.google.com/bigquery/docs/reference/rest/v2/Job
                # for alternative values for the writeDisposition
                # or consider using partitioned tables
                # https://cloud.google.com/bigquery/docs/partitioned-tables
                bq_join_holidays_weather_data = BigQueryInsertJobOperator(
                    task_id=f"bq_join_holidays_weather_data_{str(year)}",
                    configuration={
                        "query": {
                            "query": WEATHER_HOLIDAYS_JOIN_QUERY,
                            "useLegacySql": False,
                            "destinationTable": {
                                "projectId": PROJECT_NAME,
                                "datasetId": BQ_DESTINATION_DATASET_NAME,
                                "tableId": BQ_DESTINATION_TABLE_NAME,
                            },
                            "writeDisposition": "WRITE_APPEND",
                        }
                    },
                    location="US",
                )
    
            azure_blob_to_gcs >> load_external_dataset >> bq_join_group >> create_batch

### Use the Airflow UI to add variables

In Airflow, [variables](https://airflow.apache.org/docs/apache-airflow/stable/howto/variable.html) are an universal way to store and retrieve arbitrary settings or configurations as a simple key value store. This DAG uses Airflow variables to store common values. To add them to your environment:

  1. [Access the Airflow UI from the Managed Airflow console](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface#accessing-from-console).

  2. Go to **Admin > Variables**.

  3. Add the following variables:

     * `gcp_project`: your project ID.

     * `gcs_bucket`: the name of the bucket you created earlier (without the `gs://` prefix).

     * `gce_region`: the region where you want your Managed Service for Apache Spark job that meets [Managed Service for Apache Spark networking requirements](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/network). This is the region where you enabled private Google access earlier.

     * `dataproc_service_account`: the service account for your Managed Airflow environment. You can find this service account on the environment configuration tab for your Managed Airflow environment.

     * `azure_blob_name`: the name of the blob you created earlier.

     * `azure_container_name`: the name of the container you created earlier.




### Upload the DAG to your environment's bucket

Managed Airflow schedules DAGs that are located in the `/dags` folder in your environment's bucket. To upload the DAG using the Google Cloud console:

  1. On your local machine, save [azureblobstoretogcsoperator_tutorial.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/workflows/azureblobstoretogcsoperator_tutorial.py).

  2. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  3. In the list of environments, in the **DAG folder** column click the **DAGs** link. The DAGs folder of your environment opens.

  4. Click **Upload files**.

  5. Select `azureblobstoretogcsoperator_tutorial.py` on your local machine and click **Open**.




### Trigger the DAG

  1. In your Managed Airflow environment, click the **DAGs** tab.

  2. Click into DAG id `azure_blob_to_gcs_dag`.

  3. Click **Trigger DAG**.

  4. Wait about five to ten minutes until you see a green check indicating the tasks have been completed successfully.




### Validate the DAG's success

  1. In Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, click your project name.

  3. Click `holidays_weather_joined`.

  4. Click preview to view the resulting table. Note that the numbers in the value column are in tenths of a degree Celsius.

  5. Click `holidays_weather_normalized`.

  6. Click preview to view the resulting table. Note that the numbers in the value column are in degree Celsius.




## Cleanup

Delete individual resources that you created for this tutorial:

  * [Delete the container you created in Azure](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal#clean-up-resources).

  * [Delete the Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) that you created for this tutorial.

  * [Delete the BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/managing-datasets#deleting_datasets).

  * [Delete the Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/delete-environments), including manually deleting the environment's bucket.




## What's next

  * [Run a Data Analytics DAG in Google Cloud](https://docs.cloud.google.com/composer/docs/composer-2/run-data-analytics-dag-googlecloud).
  * [Run a Data Analytics DAG in AWS](https://docs.cloud.google.com/composer/docs/composer-2/run-data-analytics-dag-aws).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
