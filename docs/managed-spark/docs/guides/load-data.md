---
url: https://docs.cloud.google.com/managed-spark/docs/guides/load-data/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:16.530472+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/load-data/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Load data into BigQuery

This document shows how to use Managed Service for Apache Spark to run a Spark job that loads processed data from Cloud Storage into a BigQuery table. Managed Service for Apache Spark streamlines this process by managing the Spark environment and the necessary connectors.

See [Transform data](https://docs.cloud.google.com/managed-spark/docs/guides/transform-data) for a guide to processing data using PySpark on Managed Service for Apache Spark.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,bigquery.googleapis.com,storage.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataproc, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,bigquery.googleapis.com,storage.googleapis.com)

  8. [](https://docs.cloud.google.com/storage/docs/creating-buckets)Create a Cloud Storage bucket.
  9. [Create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster) that uses image version `2.1` or later.
  10. [Create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets).



## Prepare the PySpark script

  1. Create a local Python file named `load_analytics_data.py`.

  2. Add the following code to the file. This script reads data from a Cloud Storage path, performs an aggregation, and writes the result to BigQuery.
         
         from pyspark.sql import SparkSession
         from pyspark.sql.functions import sum as _sum
         import sys
         
         # --- Configuration ---
         gcs_bucket = "BUCKET_NAME"
         bq_project = "PROJECT_ID"
         bq_dataset = "DATASET"
         bq_table = "corpus_word_counts"
         
         # --- Paths ---
         processed_path = f"gs://{gcs_bucket}/processed/processed_data"
         temp_gcs_path = f"{gcs_bucket}"
         
         # --- Spark Session Initialization ---
         spark = SparkSession.builder \
            .appName("Dataproc-BigQuery-Load") \
            .config("spark.hadoop.google.cloud.bigdata.connector.temporary.gcs.bucket", temp_gcs_path) \
            .getOrCreate()
         
         # --- Read Processed Data from Cloud Storage ---
         processed_df = spark.read.parquet(processed_path)
         
         # --- Final Aggregation for Analytics-Ready Stage ---
         analytics_df = processed_df.groupBy("corpus") \
            .agg(_sum("word_count_int").alias("total_word_count")) \
            .orderBy("corpus")
         
         print("Aggregated Analytics-Ready data:")
         analytics_df.show()
         
         # --- Write DataFrame to BigQuery ---
         print(f"Writing data to BigQuery table: {bq_dataset}.{bq_table}")
         
         analytics_df.write \
            .format("bigquery") \
            .option("table", f"{bq_project}.{bq_dataset}.{bq_table}") \
            .mode("append") \
            .save()
         
         print("Successfully wrote data to BigQuery.")
         
         # --- Stop Spark Session ---
         spark.stop()
         

  3. Replace the following placeholders:

     * `BUCKET_NAME`: the name of your Cloud Storage bucket.
     * `PROJECT_ID`: your Google Cloud project ID.
  4. Upload the `load_analytics_data.py` script to your Cloud Storage bucket.




## Submit the Managed Service for Apache Spark job

Submit the PySpark script as a job to your Managed Service for Apache Spark cluster.

  1. In a terminal, run the `gcloud dataproc jobs submit pyspark` command:
         
         gcloud dataproc jobs submit pyspark gs://YOUR_BUCKET_NAME/scripts/load_analytics_data.py \
             --cluster=CLUSTER_NAME \
             --region=REGION
         

  2. Replace the following placeholders:

     * `BUCKET_NAME`: the name of your Cloud Storage bucket.
     * `CLUSTER_NAME`: the name of your Managed Service for Apache Spark cluster.
     * `REGION`: the region where your cluster is located.

The command submits a PySpark job to Managed Service for Apache Spark. Managed Service for Apache Spark workers fetch the script from the specified Cloud Storage path and execute it on the cluster.




## Verify the data load

  1. In the Google Cloud console, go to the Managed Service for Apache Spark **Jobs** page to monitor the job's execution and view driver output logs.

  2. After the job completes, go to the **BigQuery** page.

  3. In the Explorer panel, find your project and dataset, then select the `corpus_word_counts` table.

  4. Click the **Preview** tab to inspect the loaded data.




## How the Spark-BigQuery connector works

The Spark-BigQuery Connector enables Spark applications to read from and write to BigQuery. On Managed Service for Apache Spark clusters with image versions 2.1 or later, the connector is pre-installed.

The connector uses an indirect write method to load data. This method leverages both Managed Service for Apache Spark and BigQuery for high performance.

  1. The Spark job on the Managed Service for Apache Spark cluster writes the final DataFrame to a temporary location in a Cloud Storage bucket.

  2. After the write to Cloud Storage completes, the connector triggers a BigQuery Load Job.

  3. BigQuery ingests the data from the temporary Cloud Storage location into the target table.




This indirect approach decouples the Spark computation from the BigQuery ingestion. This decoupling allows each service to operate efficiently and ensures high throughput for large data loads.

## What's next

  * Learn more about the [Spark-BigQuery connector](https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-connector-spark-example).
  * Learn how to [query and visualize data in BigQuery](https://docs.cloud.google.com/bigquery/docs/visualize-data-colab).
  * Explore how to [visualize BigQuery data using Looker](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
