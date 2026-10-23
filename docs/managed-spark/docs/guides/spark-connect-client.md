---
url: https://docs.cloud.google.com/managed-spark/docs/guides/spark-connect-client/
title: Use the serverless Spark Connect client \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:45.057143+00:00
---

# Use the serverless Spark Connect client  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/spark-connect-client/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use the serverless Spark Connect client Stay organized with collections  Save and categorize content based on your preferences. 

The Spark Connect client is a wrapper of the Managed Service for Apache Spark Connect client. It lets applications communicate with a remote Managed Service for Apache Spark session using the [Spark Connect](https://spark.apache.org/spark-connect/) protocol. This document shows you how to install, configure, and use the client.

## Before you begin

  1. Ensure you have the [Identity and Access Management roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#dataproc-roles) that contain the permissions needed to manage interactive sessions and session templates.

  2. If you run the client outside of Google Cloud, provide [authentication credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc). Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file.




## Install or uninstall the client

You can install or uninstall the `dataproc-spark-connect` package using `pip`.

### Install

To install the latest version of the client, run the following command:
    
    
    pip install -U dataproc-spark-connect
    

### Uninstall

To uninstall the client, run the following command:
    
    
    pip uninstall dataproc-spark-connect
    

## Configure the client

Specify the project and region for your session. You can set these values using environment variables or by using the builder API in your code.

### Environment variables

Set the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_REGION` environment variables. 

Expand example Collapse example
    
    
    # Google Cloud Configuration for Managed Spark Connect Integration Tests
    # Copy this file to .env and fill in your actual values
    
    # ============================================================================
    # REQUIRED CONFIGURATION
    # ============================================================================
    
    # Your Google Cloud Project ID
    GOOGLE_CLOUD_PROJECT="your-project-id"
    
    # Google Cloud Region where Managed Spark sessions will be created
    GOOGLE_CLOUD_REGION="us-central1"
    
    # Path to service account key file (if using SERVICE_ACCOUNT auth)
    GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
    
    # ============================================================================
    # AUTHENTICATION CONFIGURATION
    # ============================================================================
    
    # Authentication type (SERVICE_ACCOUNT or END_USER_CREDENTIALS). If not set, API default is used.
    # MANAGED_SPARK_CONNECT_AUTH_TYPE="SERVICE_ACCOUNT"
    # MANAGED_SPARK_CONNECT_AUTH_TYPE="END_USER_CREDENTIALS"
    
    # Service account email for workload authentication (optional)
    # MANAGED_SPARK_CONNECT_SERVICE_ACCOUNT="your-service-account@your-project.iam.gserviceaccount.com"
    
    # ============================================================================
    # SESSION CONFIGURATION
    # ============================================================================
    
    # Session timeout in seconds (how long session stays active)
    # MANAGED_SPARK_CONNECT_TTL_SECONDS="3600"
    
    # Session idle timeout in seconds (how long session stays active when idle)
    # MANAGED_SPARK_CONNECT_IDLE_TTL_SECONDS="900"
    
    # Automatically terminate session when Python process exits (true/false)
    # MANAGED_SPARK_CONNECT_SESSION_TERMINATE_AT_EXIT="false"
    
    # Custom file path for storing active session information
    # MANAGED_SPARK_CONNECT_ACTIVE_SESSION_FILE_PATH="/tmp/managed_spark_connect_session"
    
    # ============================================================================
    # DATA SOURCE CONFIGURATION
    # ============================================================================
    
    # Default data source for Spark SQL (currently only supports "bigquery")
    # Only available for Managed Spark runtime version 2.3
    # MANAGED_SPARK_CONNECT_DEFAULT_DATASOURCE="bigquery"
    
    # ============================================================================
    # ADVANCED CONFIGURATION
    # ============================================================================
    
    # Custom Dataproc API endpoint (uncomment if needed)
    # GOOGLE_CLOUD_DATAPROC_API_ENDPOINT="your-region-dataproc.googleapis.com"
    
    # Subnet URI for Managed Spark Connect (full resource name format)
    # Example: projects/your-project-id/regions/us-central1/subnetworks/your-subnet-name
    # MANAGED_SPARK_CONNECT_SUBNET="projects/your-project-id/regions/us-central1/subnetworks/your-subnet-name"
    
    

### Builder API

Use the `.projectId()` and `.location()` methods.
    
    
    spark = DataprocSparkSession.builder.projectId("my-project").location("us-central1").getOrCreate()
    

## Start a Spark session

To start a Spark session, add the required imports to your PySpark application or notebook, then call the `DataprocSparkSession.builder.getOrCreate()` API.

  1. Import the `DataprocSparkSession` class.

  2. Call the `getOrCreate()` method to start the session.
         
         from google.cloud.dataproc_spark_connect import DataprocSparkSession
         spark = DataprocSparkSession.builder.getOrCreate()
         




## Configure Spark properties

To configure Spark properties, chain one or more `.config()` methods to the builder.
    
    
    from google.cloud.dataproc_spark_connect import DataprocSparkSession
    
    spark = DataprocSparkSession.builder.config('spark.executor.memory', '48g').config('spark.executor.cores', '8').getOrCreate()
    

**Note:** Managed Service for Apache Spark `3.0`\+ runtimes support Spark [single-node execution](https://spark.apache.org/docs/latest/submitting-applications.html#master-urls). To enable it, set `spark.master=local` in your session config.

## Use advanced configuration

For advanced configuration, use the `Session` class to customize settings such as the subnetwork or runtime version.
    
    
    from google.cloud.dataproc_spark_connect import DataprocSparkSession
    from google.cloud.dataproc_v1 import [Session](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.html)
    
    session_config = Session()
    session_config.environment_config.execution_config.subnetwork_uri = 'SUBNET'
    session_config.runtime_config.version = '3.0'
    
    spark = DataprocSparkSession.builder.projectId('my-project').location('us-central1').dataprocSessionConfig(session_config).getOrCreate()
    

## Reuse a named session

Named sessions let you share a single Spark session across multiple notebooks while avoiding repeated session startup-time delays.

  1. In your first notebook, create a session with a custom ID.
         
         from google.cloud.dataproc_spark_connect import DataprocSparkSession
         
         session_id = 'my-ml-pipeline-session'
         spark = DataprocSparkSession.builder.dataprocSessionId(session_id).getOrCreate()
         df = spark.createDataFrame([(1, 'data')], ['id', 'value'])
         df.show()
         

  2. In another notebook, reuse the session by specifying the same session ID.
         
         from google.cloud.dataproc_spark_connect import DataprocSparkSession
         
         session_id = 'my-ml-pipeline-session'
         spark = DataprocSparkSession.builder.dataprocSessionId(session_id).getOrCreate()
         df = spark.createDataFrame([(2, 'more-data')], ['id', 'value'])
         df.show()
         




Session IDs must be 4-63 characters long, start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens. The ID cannot end with a hyphen. A session with an ID that is in a `TERMINATED` state cannot be reused.

## Use Spark SQL magic commands

The package supports the [`sparksql-magic` library](https://github.com/cryeo/sparksql-magic) to execute Spark SQL queries in Jupyter notebooks. Magic commands are an optional feature.

  1. Install the required dependencies.
         
         pip install IPython sparksql-magic
         

  2. Load the magic extension.
         
         %load_ext sparksql_magic
         

  3. Optional: configure default settings.
         
         %config SparkSql.limit=20
         

  4. Execute SQL queries.
         
         %%sparksql
         SELECT * FROM your_table
         




To use advanced options, add flags to the `%%sparksql` command. For example, to cache results and create a view, run the following command:
    
    
    %%sparksql --cache --view result_view df
    SELECT * FROM your_table WHERE condition = true
    

The following options are available:

  * `--cache` or `-c`: caches the DataFrame.
  * `--eager` or `-e`: caches with eager loading.
  * `--view VIEW` or `-v VIEW`: creates a temporary view.
  * `--limit N` or `-l N`: overrides the default row display limit.
  * `variable_name`: stores the result in a variable.



## What's next

  * Learn more about [Managed Service for Apache Spark sessions](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates).

  * [Visualize Spark DataFrames in notebooks](https://docs.cloud.google.com/managed-spark/docs/guides/visualize-dataframes-notebooks).

  * [Run PySpark code in BigQuery Studio notebooks](https://docs.cloud.google.com/bigquery/docs/use-spark).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
