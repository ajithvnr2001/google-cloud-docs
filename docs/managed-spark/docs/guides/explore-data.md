---
url: https://docs.cloud.google.com/managed-spark/docs/guides/explore-data/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:32.683550+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/explore-data/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Explore and extract data

A multi-stage data architecture organizes data into progressively refined quality tiers: bronze, silver, and gold. This architecture provides a structured methodology for transforming raw data into clean, reliable assets.

This document shows you how to create the bronze tier, where you land data from external source systems. This tier provides a single source of truth, ensures complete data lineage, and enables the reprocessing of pipelines.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,bigquery.googleapis.com,bigquerystorage.googleapis.com,storage.googleapis.com)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **Storage Object Admin, Dataproc Worker**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  11. Enable the Compute Engine, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,bigquery.googleapis.com,bigquerystorage.googleapis.com,storage.googleapis.com)

  12. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **Storage Object Admin, Dataproc Worker**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Land raw data in Cloud Storage

Ingest raw data into an initial storage layer in Cloud Storage. To simulate data ingestion, export a public dataset from BigQuery to a Cloud Storage bucket. This process mimics an external system delivering raw data files to a landing zone.

  1. Create a Cloud Storage bucket to serve as the data lake. Create it in the same region as your Managed Service for Apache Spark cluster to optimize performance.
         
         gsutil mb -l REGION gs://BUCKET_NAME/
         

  2. Export the `bigquery-public-data:samples.shakespeare` table to your Cloud Storage bucket in CSV format.
         
         bq extract \
             --destination_format CSV \
             "bigquery-public-data:samples.shakespeare" \
             "gs://BUCKET_NAME/raw/shakespeare/shakespeare.csv"
         

This command starts an export job that writes the table's contents to the specified Cloud Storage path.




## Read raw data with PySpark

After landing the data in Cloud Storage, use a PySpark job on a Managed Service for Apache Spark cluster to read and explore it. Apache Spark interacts with Cloud Storage through the Cloud Storage connector, which lets you use the `gs://` URI scheme to read and write data.

  1. Use the following PySpark script to create a SparkSession, configure it for Cloud Storage access, and read the raw CSV file into a DataFrame.
         
         from pyspark.sql import SparkSession
         
         # --- Configuration ---
         gcs_bucket = "BUCKET_NAME"
         raw_path = f"gs://{gcs_bucket}/raw/shakespeare/shakespeare.csv"
         # For local development only.
         service_account_key_path = "/path/to/your/service-account-key.json"
         
         # --- Spark Session Initialization ---
         spark = SparkSession.builder \
           .appName("DataprocETL-RawIngestion") \
           .config("spark.jars", "https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar") \
           .getOrCreate()
         
         # --- Authentication for local development ---
         # This step is not necessary when running on a Dataproc cluster
         # with the service account attached to the cluster VMs.
         spark.conf.set("google.cloud.auth.service.account.json.keyfile", service_account_key_path)
         
         # --- Read Raw Data from Cloud Storage ---
         # Read the raw CSV data into a DataFrame.
         # inferSchema=True scans the data to determine column types.
         raw_df = spark.read.csv(raw_path, header=True, inferSchema=True)
         
         # --- Initial Exploration ---
         print("Raw data count:", raw_df.count())
         print("Schema:")
         raw_df.printSchema()
         print("Sample of raw data:")
         raw_df.show(10, truncate=False)
         
         # --- Stop Spark Session ---
         spark.stop()
         

  2. Run the script as a Managed Service for Apache Spark job to ingest and explore the raw data.




## Data ingestion patterns

The bronze tier can support various ingestion patterns beyond batch file uploads. Managed Service for Apache Spark is a versatile engine capable of handling diverse ingestion scenarios.

### Streaming ingestion

For continuous data sources like IoT sensor data or application logs, use a streaming pipeline. You can use Managed Service for Apache Spark to process high-volume streams from a service like Pub/Sub or Apache Kafka and land the data in the bronze tier.

### Database ingestion

To keep the data lake synchronized with operational databases, use Change Data Capture (CDC). A Managed Service for Apache Spark job can subscribe to a Pub/Sub topic that receives change events, process the stream, and apply the changes to the raw datastore in Cloud Storage.

## What's next

  * Learn more about [Managed Service for Apache Spark](https://cloud.google.com/managed-spark/docs).
  * Learn more about the [Cloud Storage connector](https://cloud.google.com/managed-spark/docs/concepts/connectors/cloud-storage).
  * Explore [BigQuery public datasets](https://cloud.google.com/bigquery/public-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
