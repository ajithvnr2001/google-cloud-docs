---
url: https://docs.cloud.google.com/managed-spark/docs/guides/query-bigquery-tables/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:24.554617+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/query-bigquery-tables/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

## Query BigQuery tables

This document explains how you can use Spark SQL and the Spark DataFrame API in Managed Service for Apache Spark workloads to query BigQuery tables.

## Before you begin

Enable the APIs and, if needed, grant Identity and Access Management roles.

### Enable APIs

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,bigquery.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataproc and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,bigquery.googleapis.com)




### Grant Identity and Access Management roles

Managed Service for Apache Spark and BigQuery role grants are required To run the examples on this page. Depending on organization policy, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#do_you_need_to_grant_roles).

#### Managed Service for Apache Spark roles

By default, batches and sessions run as the [Compute Engine default service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account) unless a custom service account is specified for the workload or session.

**Service Account User role**

To get the permissions that you need to submit a batch workload, ask your administrator to grant you the [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) IAM role on Compute Engine default service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Dataproc Worker role**

To ensure that Compute Engine default service account has the necessary permissions to submit a batch workload, ask your administrator to grant the [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) IAM role to Compute Engine default service account on project. **Important:** You must grant this role to Compute Engine default service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give Compute Engine default service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### BigQuery roles

The service account used to run a Managed Service for Apache Spark batch workload or interactive session must be granted the following IAM roles on the following resources:

  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) to read data from tables, as follows:

    * Reading from bigquery.DATASET_ID.SOURCE_TABLE in the Spark SQL SELECT and INSERT INTO examples.
    * Reading from INFORMATION_SCHEMA in the DataFrame API example.
  * [BigQuery User (`roles/bigquery.user`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) to allow Spark to execute jobs that interact with BigQuery.

  * [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) to write data or metadata, as follows:

    * For the Spark SQL INSERT INTO example, to write to the bigquery.DATASET_ID.DESTINATION_TABLE.
    * For the DataFrame API example querying INFORMATION_SCHEMA, this role is needed on the DATASET_ID provided in `.option('materializationDataset', ...)` to allow the connector to create temporary tables for the results.



## Submit a Spark batch workload

You can use the Google Cloud console, the Google Cloud CLI, or the Managed Service for Apache Spark API to [submit a Managed Service for Apache Spark batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch#submit_a_spark_batch_workload).

### Use Spark SQL

You can use the Spark BigQuery catalog to query standard BigQuery tables directly from batch workloads or interactive sessions. This method lets you use standard GoogleSQL syntax to interact with BigQuery data within `spark-sql` jobs without writing PySpark code or creating temporary views using the DataFrame API.

**Note:** This catalog integration does not support querying `INFORMATION_SCHEMA` views. To query `INFORMATION_SCHEMA`, you must use the DataFrame API.

### Configure the BigQuery catalog

To enable the BigQuery catalog, provide the following Spark properties to your Spark SQL batch workload or interactive session:

  * `dataproc.sparkBqConnector.version=CONNECTOR_VERSION`: Specifies the Spark BigQuery connector version.
  * `spark.sql.catalog.bigquery=com.google.cloud.spark.bigquery.BigQueryCatalog`: (Optional) Registers the `bigquery` catalog as a Spark SQL catalog.



Google Cloud CLI example:
    
    
    gcloud dataproc batches submit spark-sql \
        --project=PROJECT_ID \
        --region=REGION \
        --version=RUNTIME_VERSION \
        --subnet=SUBNET \
        --service-account=SERVICE_ACCOUNT \
        --properties="dataproc.sparkBqConnector.version=CONNECTOR_VERSION,spark.sql.catalog.bigquery=com.google.cloud.spark.bigquery.BigQueryCatalog" \
        gs://BUCKET/my_query.sql
    

Replace the following:

  * `PROJECT_ID`: Project ID. Project IDs are listed in the **Project info** section in the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
  * `REGION`: Region where the batch will run
  * `RUNTIME_VERSION`: Optional. [Managed Service for Apache Spark runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions). If not specified, the current [default runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions) is selected.
  * `CONNECTOR_VERSION`: [Spark BigQuery connector](https://docs.cloud.google.com/managed-spark/docs/guides/spark-bigquery-connector) version. To find a connector version that is compatible with the `RUNTIME_VERSION`, see [Managed Service for Apache Spark runtime releases](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-versions). If the connector is not pre-installed, you can find available versions on the [GitHub releases page](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases).
  * `SUBNET`: Optional. Subnetwork to use for the batch workload. If not specified, the `default` subnetwork is used.
  * `SERVICE_ACCOUNT`: Optional. Service account the batch job will run as. If not specified, the [Compute Engine default service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account) is used.
  * `BUCKET`: Cloud Storage bucket containing the SQL file.



### Query BigQuery tables

After you configure the catalog, you can reference BigQuery tables in a SQL script using the following format: `bigquery.DATASET_ID.TABLE_ID`.

Sample SQL query:
    
    
    -- Query data from a BigQuery table.
    SELECT
      column_a,
      SUM(column_b)
    FROM
      bigquery.DATASET_ID.SOURCE_TABLE
    WHERE
      partition_date = CURRENT_DATE()
    GROUP BY column_a;
    
    -- Insert results into another BigQuery table.
    INSERT INTO bigquery.DATASET_ID.DESTINATION_TABLE
    SELECT column_a, column_b
    FROM bigquery.DATASET_ID.SOURCE_TABLE
    WHERE column_c = 'some_value';
    

Replace the following:

  * `DATASET_ID`: BigQuery dataset ID.
  * `SOURCE_TABLE`: ID of the table to query.
  * `DESTINATION_TABLE`: ID of the table to insert data into.



## Use the DataFrame API

The DataFrame API is required to access `INFORMATION_SCHEMA` views.

  * To query `INFORMATION_SCHEMA`:

    * Set `spark.conf.set('viewsEnabled', 'true')`.
    * Provide `.option('materializationDataset', 'DATASET_ID')` for the connector to write temporary results.



Sample PySpark query:
    
    
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName('BigQuery Info Schema Test').getOrCreate()
    
    # Required for INFORMATION_SCHEMA.
    spark.conf.set('viewsEnabled', 'true')
    
    # Query INFORMATION_SCHEMA.TABLES.
    info_schema_df = spark.read.format('bigquery') \
      .option('project', 'PROJECT_ID') \
      .option('materializationDataset', 'DATASET_ID') \
      .load(f'SELECT table_name, creation_time FROM `PROJECT_ID.DATASET_ID.INFORMATION_SCHEMA.TABLES`')
    info_schema_df.show(5, truncate=False)
    

Replace the following:

  * `PROJECT_ID`: Project ID. Project IDs are listed in the **Project info** section in the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
  * `DATASET_ID`: BigQuery dataset ID where the SparkvBigQuery connector can write temporary data.



See [Submit a PySpark wordcount batch workload](https://docs.cloud.google.com/managed-spark/docs/guides/spark-bigquery-connector#submit_a_pyspark_wordcount_batch_workload) for a PySpark example that reads data from a standard BigQuery table, and then writes the results to an output table.

## What's next

  * Learn about the [Spark BigQuery connector](https://docs.cloud.google.com/managed-spark/docs/guides/spark-bigquery-connector).
  * Review [Managed Service for Apache Spark quotas](https://docs.cloud.google.com/managed-spark/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
