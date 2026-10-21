---
url: https://docs.cloud.google.com/managed-spark/docs/templates/jdbc-to-bigquery/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:47.209671+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/templates/jdbc-to-bigquery/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# JDBC to BigQuery template

Use the Managed Service for Apache Spark JDBC to BigQuery template to extract data from JDBC databases to BigQuery.

This template supports the following databases as input:

  * MySQL
  * PostgreSQL
  * Microsoft SQL Server
  * Oracle



## Use the template

Run the template using the gcloud CLI or Managed Service for Apache Spark API.

### gcloud

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: Required. Your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project).
  * REGION: Required. [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * TEMPLATE_VERSION: Required. Specify `latest` for the latest template version, or the date of a specific version, for example, `2023-03-17_v0.1.0-beta` (visit [gs://dataproc-templates-binaries](https://console.cloud.google.com/storage/browser/dataproc-templates-binaries) or run `gcloud storage ls gs://dataproc-templates-binaries` to list available template versions).
  * SUBNET: Optional. If a subnet is not specified, the subnet in the specified REGION in the `default` network is selected. 

**Example:** `projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME`

  * JDBC_CONNECTOR_CLOUD_STORAGE_PATH: Required. The full Cloud Storage path, including the filename, where the JDBC connector jar is stored. You can use the following commands to download JDBC connectors for uploading to Cloud Storage: 
    * **MySQL:**
          
          wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.30.tar.gz
                

    * **Postgres SQL:**
          
          wget https://jdbc.postgresql.org/download/postgresql-42.2.6.jar
                

    * **Microsoft SQL Server:**
          
          wget https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/6.4.0.jre8/mssql-jdbc-6.4.0.jre8.jar
                

    * **Oracle:**
          
          wget https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc8/21.7.0.0/ojdbc8-21.7.0.0.jar
                

  * DATASET and TABLE: Required. Destination BigQuery dataset and table.
  * The following variables are used to construct the required JDBC_CONNECTION_URL: 
    * JDBC_HOST
    * JDBC_PORT
    * JDBC_DATABASE, or, for Oracle, JDBC_SERVICE
    * JDBC_USERNAME
    * JDBC_PASSWORD

Construct the JDBC_CONNECTION_URL using one of the following connector-specific formats:

    * **MySQL:**
          
          jdbc:mysql://JDBC_HOST:JDBC_PORT/JDBC_DATABASE?user=JDBC_USERNAME&password=JDBC_PASSWORD
                    

    * **Postgres SQL:**
          
          jdbc:postgresql://JDBC_HOST:JDBC_PORT/JDBC_DATABASE?user=JDBC_USERNAME&password=JDBC_PASSWORD
                    

    * **Microsoft SQL Server:**
          
          jdbc:sqlserver://JDBC_HOST:JDBC_PORT;databaseName=JDBC_DATABASE;user=JDBC_USERNAME;password=JDBC_PASSWORD
                    

    * **Oracle:**
          
          jdbc:oracle:thin:@//JDBC_HOST:JDBC_PORT/JDBC_SERVICE?user=JDBC_USERNAME&password=JDBC_PASSWORD
                    

  * DRIVER: Required. The JDBC driver which will be used for the connection: 
    * **MySQL:**
          
          com.mysql.cj.jdbc.Driver
                  

    * **Postgres SQL:**
          
          org.postgresql.Driver
                  

    * **Microsoft SQL Server:**
          
          com.microsoft.sqlserver.jdbc.SQLServerDriver
                  

    * **Oracle:**
          
          oracle.jdbc.driver.OracleDriver
                  

  * QUERY: Required. SQL Query to extract data from JDBC.
  * MODE: Required. Write mode for BigQuery output. Options: `append`, `overwrite`, `ignore`, or `errorifexists`.
  * TEMP_BUCKET: Required. Cloud Storage bucket name. This bucket is used for BigQuery loading. 

**Example:** `gs://templates/jdbc_to_cloud_storage_output`

  * INPUT_PARTITION_COLUMN, LOWERBOUND, UPPERBOUND, PARTITIONS: Optional. If used, all of the following parameters must be specified: 
    * **INPUT_PARTITION_COLUMN** : JDBC input table partition column name.
    * **LOWERBOUND** : JDBC input table partition column lower bound used to determine the partition stride.
    * **UPPERBOUND:** JDBC input table partition column upper bound used to decide the partition stride.
    * **PARTITIONS:** The maximum number of partitions that can be used for parallelism of table reads and writes. If specified, this value is used for the JDBC input and output connection. Default: `10`.
  * FETCHSIZE: Optional. How many rows to fetch per round trip. Default: 10.
  * TEMPVIEW and SQL_QUERY: Optional. You can use these two optional parameters to apply a Spark SQL transformation while loading data into BigQuery. TEMPVIEW is the temporary view name, and SQL_QUERY is the query statement. TEMPVIEW and the table name in SQL_QUERY must match. 
  * SERVICE_ACCOUNT: Optional. If not provided, the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.
  * PROPERTY and PROPERTY_VALUE: Optional. Comma-separated list of [Spark property](https://docs.cloud.google.com/managed-spark/docs/concepts/properties)=`value` pairs.
  * LABEL and LABEL_VALUE: Optional. Comma-separated list of `label`=`value` pairs.
  * LOG_LEVEL: Optional. Level of logging. Can be one of `ALL`, `DEBUG`, `ERROR`, `FATAL`, `INFO`, `OFF`, `TRACE`, or `WARN`. Default: `INFO`.
  * KMS_KEY: Optional. The Cloud Key Management Service key to use for encryption. If a key is not specified, data is [encrypted at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using a Google-owned and Google-managed encryption key. 

**Example:** `projects/PROJECT_ID/regions/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME`




Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud dataproc batches submit spark \
        --class=com.google.cloud.dataproc.templates.main.DataProcTemplate \
        --version="2.3" \
        --project="PROJECT_ID" \
        --region="REGION" \
        --jars="gs://dataproc-templates-binaries/TEMPLATE_VERSION/java/dataproc-templates.jar,JDBC_CONNECTOR_CLOUD_STORAGE_PATH" \
        --subnet="SUBNET" \
        --kms-key="KMS_KEY" \
        --service-account="SERVICE_ACCOUNT" \
        --properties="PROPERTY=PROPERTY_VALUE" \
        --labels="LABEL=LABEL_VALUE" \
        -- --template=JDBCTOBIGQUERY \
        --templateProperty log.level="LOG_LEVEL" \
        --templateProperty jdbctobq.bigquery.location="DATASET.TABLE" \
        --templateProperty jdbctobq.jdbc.url="JDBC_CONNECTION_URL" \
        --templateProperty jdbctobq.jdbc.driver.class.name="DRIVER" \
        --templateProperty jdbctobq.write.mode="MODE" \
        --templateProperty jdbctobq.temp.gcs.bucket="TEMP_BUCKET" \
        --templateProperty jdbctobq.sql="QUERY" \
        --templateProperty jdbctobq.sql.numPartitions="PARTITIONS" \
        --templateProperty jdbctobq.sql.partitionColumn="INPUT_PARTITION_COLUMN" \
        --templateProperty jdbctobq.sql.lowerBound="LOWERBOUND" \
        --templateProperty jdbctobq.sql.upperBound="UPPERBOUND" \
        --templateProperty jdbctobq.jdbc.fetchsize="FETCHSIZE" \
        --templateProperty jdbctobq.temp.table="TEMPVIEW" \
        --templateProperty jdbctobq.temp.query="SQL_QUERY"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud dataproc batches submit spark `
        --class=com.google.cloud.dataproc.templates.main.DataProcTemplate `
        --version="2.3" `
        --project="PROJECT_ID" `
        --region="REGION" `
        --jars="gs://dataproc-templates-binaries/TEMPLATE_VERSION/java/dataproc-templates.jar,JDBC_CONNECTOR_CLOUD_STORAGE_PATH" `
        --subnet="SUBNET" `
        --kms-key="KMS_KEY" `
        --service-account="SERVICE_ACCOUNT" `
        --properties="PROPERTY=PROPERTY_VALUE" `
        --labels="LABEL=LABEL_VALUE" `
        -- --template=JDBCTOBIGQUERY `
        --templateProperty log.level="LOG_LEVEL" `
        --templateProperty jdbctobq.bigquery.location="DATASET.TABLE" `
        --templateProperty jdbctobq.jdbc.url="JDBC_CONNECTION_URL" `
        --templateProperty jdbctobq.jdbc.driver.class.name="DRIVER" `
        --templateProperty jdbctobq.write.mode="MODE" `
        --templateProperty jdbctobq.temp.gcs.bucket="TEMP_BUCKET" `
        --templateProperty jdbctobq.sql="QUERY" `
        --templateProperty jdbctobq.sql.numPartitions="PARTITIONS" `
        --templateProperty jdbctobq.sql.partitionColumn="INPUT_PARTITION_COLUMN" `
        --templateProperty jdbctobq.sql.lowerBound="LOWERBOUND" `
        --templateProperty jdbctobq.sql.upperBound="UPPERBOUND" `
        --templateProperty jdbctobq.jdbc.fetchsize="FETCHSIZE" `
        --templateProperty jdbctobq.temp.table="TEMPVIEW" `
        --templateProperty jdbctobq.temp.query="SQL_QUERY"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud dataproc batches submit spark ^
        --class=com.google.cloud.dataproc.templates.main.DataProcTemplate ^
        --version="2.3" ^
        --project="PROJECT_ID" ^
        --region="REGION" ^
        --jars="gs://dataproc-templates-binaries/TEMPLATE_VERSION/java/dataproc-templates.jar,JDBC_CONNECTOR_CLOUD_STORAGE_PATH" ^
        --subnet="SUBNET" ^
        --kms-key="KMS_KEY" ^
        --service-account="SERVICE_ACCOUNT" ^
        --properties="PROPERTY=PROPERTY_VALUE" ^
        --labels="LABEL=LABEL_VALUE" ^
        -- --template=JDBCTOBIGQUERY ^
        --templateProperty log.level="LOG_LEVEL" ^
        --templateProperty jdbctobq.bigquery.location="DATASET.TABLE" ^
        --templateProperty jdbctobq.jdbc.url="JDBC_CONNECTION_URL" ^
        --templateProperty jdbctobq.jdbc.driver.class.name="DRIVER" ^
        --templateProperty jdbctobq.write.mode="MODE" ^
        --templateProperty jdbctobq.temp.gcs.bucket="TEMP_BUCKET" ^
        --templateProperty jdbctobq.sql="QUERY" ^
        --templateProperty jdbctobq.sql.numPartitions="PARTITIONS" ^
        --templateProperty jdbctobq.sql.partitionColumn="INPUT_PARTITION_COLUMN" ^
        --templateProperty jdbctobq.sql.lowerBound="LOWERBOUND" ^
        --templateProperty jdbctobq.sql.upperBound="UPPERBOUND" ^
        --templateProperty jdbctobq.jdbc.fetchsize="FETCHSIZE" ^
        --templateProperty jdbctobq.temp.table="TEMPVIEW" ^
        --templateProperty jdbctobq.temp.query="SQL_QUERY"

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Required. Your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project).
  * REGION: Required. [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * TEMPLATE_VERSION: Required. Specify `latest` for the latest template version, or the date of a specific version, for example, `2023-03-17_v0.1.0-beta` (visit [gs://dataproc-templates-binaries](https://console.cloud.google.com/storage/browser/dataproc-templates-binaries) or run `gcloud storage ls gs://dataproc-templates-binaries` to list available template versions).
  * SUBNET: Optional. If a subnet is not specified, the subnet in the specified REGION in the `default` network is selected. 

**Example:** `projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME`

  * JDBC_CONNECTOR_CLOUD_STORAGE_PATH: Required. The full Cloud Storage path, including the filename, where the JDBC connector jar is stored. You can use the following commands to download JDBC connectors for uploading to Cloud Storage: 
    * **MySQL:**
          
          wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.30.tar.gz
                

    * **Postgres SQL:**
          
          wget https://jdbc.postgresql.org/download/postgresql-42.2.6.jar
                

    * **Microsoft SQL Server:**
          
          wget https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/6.4.0.jre8/mssql-jdbc-6.4.0.jre8.jar
                

    * **Oracle:**
          
          wget https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc8/21.7.0.0/ojdbc8-21.7.0.0.jar
                

  * DATASET and TABLE: Required. Destination BigQuery dataset and table.
  * The following variables are used to construct the required JDBC_CONNECTION_URL: 
    * JDBC_HOST
    * JDBC_PORT
    * JDBC_DATABASE, or, for Oracle, JDBC_SERVICE
    * JDBC_USERNAME
    * JDBC_PASSWORD

Construct the JDBC_CONNECTION_URL using one of the following connector-specific formats:

    * **MySQL:**
          
          jdbc:mysql://JDBC_HOST:JDBC_PORT/JDBC_DATABASE?user=JDBC_USERNAME&password=JDBC_PASSWORD
                    

    * **Postgres SQL:**
          
          jdbc:postgresql://JDBC_HOST:JDBC_PORT/JDBC_DATABASE?user=JDBC_USERNAME&password=JDBC_PASSWORD
                    

    * **Microsoft SQL Server:**
          
          jdbc:sqlserver://JDBC_HOST:JDBC_PORT;databaseName=JDBC_DATABASE;user=JDBC_USERNAME;password=JDBC_PASSWORD
                    

    * **Oracle:**
          
          jdbc:oracle:thin:@//JDBC_HOST:JDBC_PORT/JDBC_SERVICE?user=JDBC_USERNAME&password=JDBC_PASSWORD
                    

  * DRIVER: Required. The JDBC driver which will be used for the connection: 
    * **MySQL:**
          
          com.mysql.cj.jdbc.Driver
                  

    * **Postgres SQL:**
          
          org.postgresql.Driver
                  

    * **Microsoft SQL Server:**
          
          com.microsoft.sqlserver.jdbc.SQLServerDriver
                  

    * **Oracle:**
          
          oracle.jdbc.driver.OracleDriver
                  

  * QUERY: Required. SQL Query to extract data from JDBC.
  * MODE: Required. Write mode for BigQuery output. Options: `append`, `overwrite`, `ignore`, or `errorifexists`.
  * TEMP_BUCKET: Required. Cloud Storage bucket name. This bucket is used for BigQuery loading. 

**Example:** `gs://templates/jdbc_to_cloud_storage_output`

  * INPUT_PARTITION_COLUMN, LOWERBOUND, UPPERBOUND, PARTITIONS: Optional. If used, all of the following parameters must be specified: 
    * **INPUT_PARTITION_COLUMN** : JDBC input table partition column name.
    * **LOWERBOUND** : JDBC input table partition column lower bound used to determine the partition stride.
    * **UPPERBOUND:** JDBC input table partition column upper bound used to decide the partition stride.
    * **PARTITIONS:** The maximum number of partitions that can be used for parallelism of table reads and writes. If specified, this value is used for the JDBC input and output connection. Default: `10`.
  * FETCHSIZE: Optional. How many rows to fetch per round trip. Default: 10.
  * TEMPVIEW and SQL_QUERY: Optional. You can use these two optional parameters to apply a Spark SQL transformation while loading data into BigQuery. TEMPVIEW is the temporary view name, and SQL_QUERY is the query statement. TEMPVIEW and the table name in SQL_QUERY must match. 
  * SERVICE_ACCOUNT: Optional. If not provided, the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.
  * PROPERTY and PROPERTY_VALUE: Optional. Comma-separated list of [Spark property](https://docs.cloud.google.com/managed-spark/docs/concepts/properties)=`value` pairs.
  * LABEL and LABEL_VALUE: Optional. Comma-separated list of `label`=`value` pairs.
  * LOG_LEVEL: Optional. Level of logging. Can be one of `ALL`, `DEBUG`, `ERROR`, `FATAL`, `INFO`, `OFF`, `TRACE`, or `WARN`. Default: `INFO`.
  * KMS_KEY: Optional. The Cloud Key Management Service key to use for encryption. If a key is not specified, data is [encrypted at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using a Google-owned and Google-managed encryption key. 

**Example:** `projects/PROJECT_ID/regions/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME`




HTTP method and URL: 
    
    
    POST https://dataproc.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/batches

Request JSON body: 
    
    
    
    {
      "environmentConfig": {
        "executionConfig": {
          "subnetworkUri": "SUBNET",
          "kmsKey": "KMS_KEY",
          "serviceAccount": "SERVICE_ACCOUNT"
        }
      },
      "labels": {
        "LABEL": "LABEL_VALUE"
      },
      "runtimeConfig": {
        "version": "2.3",
        "properties": {
          "PROPERTY": "PROPERTY_VALUE"
        }
      },
      "sparkBatch": {
        "mainClass": "com.google.cloud.dataproc.templates.main.DataProcTemplate",
        "args": [
          "--template","JDBCTOBIGQUERY",
          "--templateProperty","log.level=LOG_LEVEL",
          "--templateProperty","jdbctobq.bigquery.location=DATASET.TABLE",
          "--templateProperty","jdbctobq.jdbc.url=JDBC_CONNECTION_URL",
          "--templateProperty","jdbctobq.jdbc.driver.class.name=DRIVER",
          "--templateProperty","jdbctobq.sql=QUERY",
          "--templateProperty","jdbctobq.write.mode=MODE",
          "--templateProperty","jdbctobq.temp.gcs.bucket=TEMP_BUCKET",
          "--templateProperty","jdbctobq.sql.partitionColumn=INPUT_PARTITION_COLUMN",
          "--templateProperty","jdbctobq.sql.lowerBound=LOWERBOUND",
          "--templateProperty","jdbctobq.sql.upperBound=UPPERBOUND",
          "--templateProperty","jdbctobq.sql.numPartitions=PARTITIONS",
          "--templateProperty","jdbctobq.jdbc.fetchsize=FETCHSIZE"
        ],
        "jarFileUris": [
          "gs://dataproc-templates-binaries/TEMPLATE_VERSION/java/dataproc-templates.jar","JDBC_CONNECTOR_CLOUD_STORAGE_PATH"
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataproc.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/batches"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataproc.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/batches" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "projects/PROJECT_ID/regions/REGION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.dataproc.v1.BatchOperationMetadata",
        "batch": "projects/PROJECT_ID/locations/REGION/batches/BATCH_ID",
        "batchUuid": "de8af8d4-3599-4a7c-915c-798201ed1583",
        "createTime": "2023-02-24T03:31:03.440329Z",
        "operationType": "BATCH",
        "description": "Batch"
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
