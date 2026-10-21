---
url: https://docs.cloud.google.com/managed-spark/docs/guides/connect-to-data-sources/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:45.572823+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/connect-to-data-sources/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to data sources

Managed Service for Apache Spark integrates with databases, data warehouses, and streaming services to process data from multiple systems. This document shows you how to connect Managed Service for Apache Spark clusters to data sources inside and outside of Google Cloud.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that you have the permissions required to complete this guide. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Managed Service for Apache Spark, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,bigquery.googleapis.com,storage.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. Verify that you have the permissions required to complete this guide. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Managed Service for Apache Spark, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,bigquery.googleapis.com,storage.googleapis.com)

  10. [Create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster).
  11. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  12. Make sure that you have the required permissions to access data sources.



### Required roles

Certain Identity and Access Management (IAM) roles are required to run the examples on this page. Depending on organization policies, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects,folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### User roles

To get the permissions that you need to create a Managed Service for Apache Spark cluster, ask your administrator to grant you the following IAM roles: 

  * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account



#### Service account role

To ensure that the Compute Engine default service account has the necessary permissions to create a Managed Service for Apache Spark cluster, ask your administrator to grant the [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) IAM role to the Compute Engine default service account on the project. **Important:** You must grant this role to the Compute Engine default service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

## Connect to Google Cloud services

This section shows you how to connect Managed Service for Apache Spark to Google Cloud and external data sources.

### Connect to Cloud Storage

Managed Service for Apache Spark uses Cloud Storage as its default distributed file system. To read and write data from and to Cloud Storage buckets, use the `gs://` URI prefix. No additional configuration is required.

The following example shows how to read a CSV file from a Cloud Storage bucket and then write a Parquet file to the bucket.
    
    
    # Read a CSV file from a Cloud Storage bucket into a Spark DataFrame
    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("gs://BUCKET_NAME/path/to/data.csv")
    
    df.show()
    
    # Write a Spark DataFrame to a Cloud Storage bucket
    df.write.format("parquet") \
        .mode("overwrite") \
        .save("gs://BUCKET_NAME/path/to/output.parquet")
    

### Connect to BigQuery

The BigQuery connector is pre-installed on Managed Service for Apache Spark `2.1` and later image versions. The connector enables large-scale data transfer between Managed Service for Apache Spark and BigQuery.

The following example shows how to read a BigQuery table into a Spark DataFrame, and then perform a query.
    
    
    # Set up the BigQuery connector.
    spark.conf.set("spark.sql.sources.provider", "bigquery")
    spark.conf.set("viewsEnabled", "true")
    spark.conf.set("materializationDataset", "YOUR_BQ_DATASET")
    
    # Read a BigQuery table into a Spark DataFrame,
    df = spark.read.format("bigquery") \
        .option("table", "bigquery-public-data.samples.shakespeare") \
        .load()
    
    df.createOrReplaceTempView("shakespeare")
    
    # Perform a query on the data,
    word_counts = spark.sql("SELECT word, SUM(word_count) as count FROM shakespeare GROUP BY word ORDER BY count DESC")
    word_counts.show()
    

## Connect to external databases using JDBC

You can connect Managed Service for Apache Spark to a database that provides a Java Database Connectivity (JDBC) driver, such as PostgreSQL or MySQL, using the Spark built-in JDBC data source.

### Make the JDBC driver available

To connect to a database with JDBC, make the driver's JAR file available on the Spark classpath.

### Per-job

Store the driver JAR in a Cloud Storage bucket, and reference it with the `--jars` flag when you submit a job. Spark distributes the JAR file to the necessary nodes for the job. This is the recommended approach for job-specific dependencies.

### Cluster-wide

If all jobs on a cluster require a specific driver, configure the `spark:spark.jars` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties) when you create the cluster to reference the driver JAR in Cloud Storage. This injects the dependency into the Spark driver and executor classpaths while maintaining classpath isolation for the Managed Service for Apache Spark agent.

**Caution:** Don't copy JAR files directly into cluster system directories such as `/usr/lib/spark/jars/`. Placing custom JARs in system directories pollutes the Managed Service for Apache Spark agent classpath and can cause class resolution errors during job cancellation, leaving YARN applications orphaned.

Create the cluster with the `spark:spark.jars` cluster property:
    
    
    gcloud dataproc clusters create my-jdbc-cluster \
        --region=REGION \
        --image-version=2.2-debian11 \
        --properties="spark:spark.jars=gs://YOUR_BUCKET_NAME/drivers/postgresql-42.7.3.jar"
    

### Read from a PostgreSQL database

This example uses the per-job method to connect to a PostgreSQL database.

  1. Download the PostgreSQL JDBC driver JAR, and upload it to a Cloud Storage bucket.

  2. Submit your PySpark job and reference the driver's Cloud Storage path with the `--jars` flag.
         
         gcloud dataproc jobs submit pyspark my_job.py \
             --cluster=MY_CLUSTER \
             --region=REGION \
             --jars=gs://YOUR_BUCKET_NAME/drivers/postgresql-42.7.3.jar
         

  3. Use the following code in your `job.py` file to read from and write to the database.
         
         from pyspark.sql import SparkSession
         
         def main():
             # WARNING: Do not hardcode credentials. Use a service like Secret Manager
             # to handle sensitive credentials.
             db_properties = {
                 "user": "USERNAME",
                 "password": "PASSWORD",
                 "driver": "org.postgresql.Driver"
             }
         
             jdbc_url = "jdbc:postgresql://DB_HOST:DB_PORT/DATABASE"
         
             spark = SparkSession.builder.appName("Postgres JDBC Example").getOrCreate()
         
             # Read data from a PostgreSQL table
             df = spark.read.jdbc(url=jdbc_url, table="public.my_table", properties=db_properties)
         
             df.printSchema()
             df.show()
         
             # Write data to a new PostgreSQL table
             (df.write
                 .jdbc(url=jdbc_url,
                       table="public.new_table",
                       mode="overwrite",
                       properties=db_properties))
         
         if __name__ == "__main__":
             main()
         




## Connect to external databases using ODBC

To connect to data sources where a JDBC driver is unavailable, use an Open Database Connectivity (ODBC) driver. Use an initialization action to install the driver and its dependencies on each node when you create the cluster.

This example demonstrates how to connect to a Microsoft SQL Server instance.

  1. Create the initialization action script.

     1. Create a script that installs the Microsoft SQL Server ODBC driver for Debian.
**Note:** This script is for Debian 11. If you use a different Managed Service for Apache Spark image base, modify the repository setup and package names.
    
    #!/bin/bash
        # Initialization action for installing MS SQL ODBC driver on the cluster.
    
        set -e -x
    
        # Install dependencies for the driver.
        apt-get update
        apt-get install -y --no-install-recommends curl gnupg unixodbc-dev
    
        # Add Microsoft's official repository.
        curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
        curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
    
        # Install the driver.
        apt-get update
        ACCEPT_EULA=Y apt-get install -y msodbcsql18
    
        # Install the pyodbc library for Python.
        pip install pyodbc
        ```
    
    1.  Upload the script to a Cloud Storage bucket.
    
    ```shell
        gsutil cp install-odbc-mssql.sh gs://YOUR_BUCKET_NAME/init-actions/
        ```
    

  2. Create a Managed Service for Apache Spark cluster that runs the initialization action.

When you create your cluster, point to the initialization action script in Cloud Storage.
         
         gcloud dataproc clusters create my-odbc-cluster \
             --region=REGION \
             --image-version=2.2-debian11 \
             --initialization-actions=gs://BUCKET_NAME/init-actions/install-odbc-mssql.sh
         

  3. Connect and query using PySpark

After the cluster is running, the ODBC driver and `pyodbc` library are available. The following code uses `pyodbc` on the driver node to fetch data into a Pandas DataFrame, and then converts it into a Spark DataFrame for distributed processing.

**Note:** This pattern loads the entire result set into driver memory. It is suitable for datasets that fit in memory of a single node.
         
         import pyodbc
         import pandas as pd
         from pyspark.sql import SparkSession
         
         def get_sql_data(connection_string, query):
             """
             Connects to the database using pyodbc, executes a query,
             and returns the result as a Pandas DataFrame.
             """
             cnxn = pyodbc.connect(connection_string)
             pdf = pd.read_sql(query, cnxn)
             cnxn.close()
             return pdf
         
         def main():
             spark = SparkSession.builder.appName("ODBC Example").getOrCreate()
         
             # WARNING: Do not hardcode credentials. Use Secret Manager.
             server = 'SERVER.database.windows.net'
             database = 'DATABASE'
             username = 'USERNAME'
             password = 'PASSWORD'
             driver = '{ODBC Driver 18 for SQL Server}' # The driver name must match the installed driver.
         
             # Create the connection string.
             connection_string = f'DRIVER={driver};SERVER=tcp:{server},1433;DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
         
             sql_query = "SELECT * FROM Sales.Customer"
         
             # Fetch data as a Pandas DataFrame.
             pandas_df = get_sql_data(connection_string, sql_query)
         
             # Convert the Pandas DataFrame to a Spark DataFrame for distributed processing.
             spark_df = spark.createDataFrame(pandas_df)
         
             print("Successfully read data from SQL Server:")
             spark_df.printSchema()
             spark_df.show(5)
         
             # You can now perform distributed operations on the Spark DataFrame.
             print(f"Total number of customers: {spark_df.count()}")
         
         if __name__ == "__main__":
             main()
         




## Best practices

This section describes best practices for managing credentials and dependencies.

### Credential management

Don't hardcode passwords or other secrets in your code. Use Secret Manager to store credentials securely and access them from your Managed Service for Apache Spark jobs.

### Dependency management

Use initialization actions to install drivers and libraries when you create a cluster. For complex environments, consider building a custom Managed Service for Apache Spark image with all dependencies pre-installed. A custom image reduces cluster startup time and ensures consistency.

Copy initialization action scripts from public sources to your own versioned Cloud Storage bucket before you use them in production. Don't reference public scripts directly, as they can change without notice.

## What's next

  * Learn more about [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).
  * Learn how to [create a custom image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-images).
  * Learn more about [Initialization Actions](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
