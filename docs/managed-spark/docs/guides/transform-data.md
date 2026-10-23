---
url: https://docs.cloud.google.com/managed-spark/docs/guides/transform-data/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:05.889869+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/transform-data/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Transform data

After you ingest raw data, the next phase is to create a processed data stage. This stage refines raw data into a validated, cleansed, and conformed dataset. This document provides a guide to building this processed data stage using PySpark on Managed Service for Apache Spark.

See [Explore and extract data](https://docs.cloud.google.com/managed-spark/docs/guides/explore-data) for a guide to ingest raw data using PySpark on Managed Service for Apache Spark.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

  8. Ensure you have raw data available in a Cloud Storage bucket.
  9. [Create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster) to run PySpark jobs.



## Clean and standardize data

The first step is to address common data quality issues. PySpark DataFrame API provides functions to perform foundational cleaning tasks in a distributed manner.

### Handle missing values

Handle null values by either dropping rows that contain them or by filling them with a default value.

  1. To drop rows where specific columns are null, use the `dropna()` method.

  2. To fill null values in specific columns with a default, use the `fillna()` method.
         
         # Assuming 'df' is the DataFrame read from the raw data stage
         # Drop rows where 'word' or 'corpus' is null
         cleaned_df = df.dropna(subset=["word", "corpus"])
         
         # Fill nulls in 'word_count' with 0
         cleaned_df = cleaned_df.fillna(0, subset=["word_count"])
         




### Correct data types

Enforce a correct and consistent schema for data integrity and performance. Use the `withColumn()` transformation with the `cast()` method to change a column's data type.
    
    
    from pyspark.sql.functions import col
    from pyspark.sql.types import IntegerType
    
    # Cast the 'word_count' column to integer
    typed_df = cleaned_df.withColumn("word_count_int", col("word_count").cast(IntegerType()))
    

### Remove duplicate records

Duplicate records can skew analytics. Use the `dropDuplicates()` method to remove duplicate rows from a DataFrame. To define uniqueness based on a specific set of columns, pass a list of column names to the `subset` parameter.
    
    
    # Remove rows that are complete duplicates across all columns
    deduped_df = typed_df.dropDuplicates()
    
    # Remove rows with duplicate 'word' and 'corpus' combinations
    key_deduped_df = typed_df.dropDuplicates(subset=["word", "corpus"])
    

### Filter outliers

Outliers can affect aggregations. A common method to identify outliers is the Interquartile Range (IQR). Filter out values that fall outside the range defined by the IQR.
    
    
    from pyspark.sql.functions import col
    
    # Calculate Q1, Q3, and IQR for the 'word_count_int' column
    quantiles = key_deduped_df.approxQuantile("word_count_int", [0.25, 0.75], 0.05)
    q1 = quantiles[0]
    q3 = quantiles[1]
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Filter out the outliers
    no_outliers_df = key_deduped_df.filter(
        (col("word_count_int") >= lower_bound) & (col("word_count_int") <= upper_bound)
    )
    

## Validate data against business rules

Programmatically validate data against business rules and quality constraints. Use Spark's built-in functions to perform validations. For example, use a join to check the integrity of data against a known set of reference values. An inner join retains only valid records, filtering out any with invalid values.

## Enrich the dataset

After you clean and validate the data, apply business logic. This step often involves enriching the dataset by combining it with other data sources and performing aggregations.
    
    
    # Example: Enriching with a hypothetical corpus metadata DataFrame
    corpus_metadata_data = [("Corpus A", 2010, "Fiction"), ("Corpus B", 1998, "News"), ("Corpus C", 2015, "Scientific")]
    corpus_metadata_df = spark.createDataFrame(corpus_metadata_data, ["corpus_name", "est_year", "genre"])
    
    # Join the main DataFrame with the metadata
    enriched_df = validated_df.join(
        corpus_metadata_df,
        validated_df.corpus == corpus_metadata_df.corpus_name,
        how="left"
    )
    

## Write the processed data to Cloud Storage

Persist the transformed DataFrame to the processed data stage in Cloud Storage. Use an optimized, columnar storage format like Parquet for this layer. Partition the data on a frequently filtered column to improve query performance.
    
    
    # --- Configuration ---
    processed_path = f"gs://BUCKET_NAME/processed/processed_data"
    
    # --- Write to Cloud Storage in Parquet format, partitioned by corpus ---
    enriched_df.write \
      .format("parquet") \
      .partitionBy("corpus") \
      .mode("overwrite") \
      .save(processed_path)
    
    print(f"Successfully wrote transformed data to {processed_path}")
    

The `mode("overwrite")` option ensures that each run of the pipeline replaces the previous output, which makes the job idempotent.

## What's next

  * Learn how to load the processed data into a data warehouse like [BigQuery](https://docs.cloud.google.com/bigquery/docs/loading-data).
  * Learn more about [Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
