---
url: https://docs.cloud.google.com/managed-spark/docs/templates/jdbc-to-spanner/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:42.461753+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/templates/jdbc-to-spanner/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# JDBC to Cloud Spanner template

Use the Managed Service for Apache Spark JDBC to Spanner template to extract data from JDBC databases to Spanner.

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

  * The following variables are used to construct the required JDBC_CONNECTION_URL: 
    * JDBC_HOST, JDBC_PORT, JDBC_DATABASE, or, for Oracle, JDBC_SERVICE, JDBC_USERNAME, and JDBC_PASSWORD: Required. JDBC host, port, database, username, and password.
      * **MySQL:**
            
            jdbc:mysql://JDBC_HOST:JDBC_PORT/JDBC_DATABASE?user=JDBC_USERNAME&password=JDBC_PASSWORD

      * **PostgreSQL:**
            
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

    * QUERY or QUERY_FILE: Required. Set **either** `QUERY` or `QUERY_FILE` to specify the query to use to extract data from JDBC
    * INPUT_PARTITION_COLUMN, LOWERBOUND, UPPERBOUND, NUM_PARTITIONS: Optional. If used, all of the following parameters must be specified: 
      * **INPUT_PARTITION_COLUMN** : JDBC input table partition column name.
      * **LOWERBOUND** : JDBC input table partition column lower bound used to determine the partition stride.
      * **UPPERBOUND:** JDBC input table partition column upper bound used to decide the partition stride.
      * **NUM_PARTITIONS:** The maximum number of partitions that can be used for parallelism of table reads and writes. If specified, this value is used for the JDBC input and output connection. Default: `10`.
    * FETCHSIZE: Optional. How many rows to fetch per round trip. Default: 10.
    * JDBC_SESSION_INIT: Optional. Session initialization statement to read Java templates.
    * TEMPVIEW and SQL_QUERY: Optional. You can use these two optional parameters to apply a Spark SQL transformation while loading data into Spanner. TEMPVIEW is the temporary view name, and SQL_QUERY is the query statement. TEMPVIEW and the table name in SQL_QUERY must match. 
    * INSTANCE: Required. Spanner instance ID.
    * SPANNER_DATABASE: Required. Spanner database ID.
    * TABLE: Required. Spanner output table name.
    * SPANNER_JDBC_DIALECT: Required. Spanner JDBC dialect. Options: `googlesql` or `postgresql`. Defaults to `googlesql`.
    * MODE: Optional. Write mode for Spanner output. Options: `Append`, `Overwrite`, `Ignore`, or `ErrorIfExists`. Defaults to `ErrorIfExists`.
    * PRIMARY_KEY: Required. Comma separated Primary key columns needed when creating Spanner output table.
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
        -- --template=JDBCTOSPANNER \
        --templateProperty log.level="LOG_LEVEL" \
        --templateProperty project.id="PROJECT_ID" \
        --templateProperty jdbctospanner.jdbc.url="JDBC_CONNECTION_URL" \
        --templateProperty jdbctospanner.jdbc.driver.class.name="DRIVER" \
        --templateProperty jdbctospanner.jdbc.fetchsize="FETCHSIZE" \
        --templateProperty jdbctospanner.jdbc.sessioninitstatement="JDBC_SESSION_INIT" \
        --templateProperty jdbctospanner.sql="QUERY" \
        --templateProperty jdbctospanner.sql.file="QUERY_FILE" \
        --templateProperty jdbctospanner.sql.numPartitions="NUM_PARTITIONS" \
        --templateProperty jdbctospanner.sql.partitionColumn="INPUT_PARTITION_COLUMN" \
        --templateProperty jdbctospanner.sql.lowerBound="LOWERBOUND" \
        --templateProperty jdbctospanner.sql.upperBound="UPPERBOUND" \
        --templateProperty jdbctospanner.output.instance="INSTANCE" \
        --templateProperty jdbctospanner.output.database="SPANNER_DATABASE" \
        --templateProperty jdbctospanner.output.table="TABLE" \
        --templateProperty jdbctospanner.output.saveMode="MODE" \
        --templateProperty jdbctospanner.output.primaryKey="PRIMARY_KEY" \
        --templateProperty jdbctospanner.output.batch.size="BATCHSIZE" \
        --templateProperty jdbctospanner.temp.table="TEMPVIEW" \
        --templateProperty jdbctospanner.temp.query="SQL_QUERY" \
        --templateProperty spanner.jdbc.dialect="SPANNER_JDBC_DIALECT" 

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
        -- --template=JDBCTOSPANNER `
        --templateProperty log.level="LOG_LEVEL" `
        --templateProperty project.id="PROJECT_ID" `
        --templateProperty jdbctospanner.jdbc.url="JDBC_CONNECTION_URL" `
        --templateProperty jdbctospanner.jdbc.driver.class.name="DRIVER" `
        --templateProperty jdbctospanner.jdbc.fetchsize="FETCHSIZE" `
        --templateProperty jdbctospanner.jdbc.sessioninitstatement="JDBC_SESSION_INIT" `
        --templateProperty jdbctospanner.sql="QUERY" `
        --templateProperty jdbctospanner.sql.file="QUERY_FILE" `
        --templateProperty jdbctospanner.sql.numPartitions="NUM_PARTITIONS" `
        --templateProperty jdbctospanner.sql.partitionColumn="INPUT_PARTITION_COLUMN" `
        --templateProperty jdbctospanner.sql.lowerBound="LOWERBOUND" `
        --templateProperty jdbctospanner.sql.upperBound="UPPERBOUND" `
        --templateProperty jdbctospanner.output.instance="INSTANCE" `
        --templateProperty jdbctospanner.output.database="SPANNER_DATABASE" `
        --templateProperty jdbctospanner.output.table="TABLE" `
        --templateProperty jdbctospanner.output.saveMode="MODE" `
        --templateProperty jdbctospanner.output.primaryKey="PRIMARY_KEY" `
        --templateProperty jdbctospanner.output.batch.size="BATCHSIZE" `
        --templateProperty jdbctospanner.temp.table="TEMPVIEW" `
        --templateProperty jdbctospanner.temp.query="SQL_QUERY" `
        --templateProperty spanner.jdbc.dialect="SPANNER_JDBC_DIALECT" 

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
        -- --template=JDBCTOSPANNER ^
        --templateProperty log.level="LOG_LEVEL" ^
        --templateProperty project.id="PROJECT_ID" ^
        --templateProperty jdbctospanner.jdbc.url="JDBC_CONNECTION_URL" ^
        --templateProperty jdbctospanner.jdbc.driver.class.name="DRIVER" ^
        --templateProperty jdbctospanner.jdbc.fetchsize="FETCHSIZE" ^
        --templateProperty jdbctospanner.jdbc.sessioninitstatement="JDBC_SESSION_INIT" ^
        --templateProperty jdbctospanner.sql="QUERY" ^
        --templateProperty jdbctospanner.sql.file="QUERY_FILE" ^
        --templateProperty jdbctospanner.sql.numPartitions="NUM_PARTITIONS" ^
        --templateProperty jdbctospanner.sql.partitionColumn="INPUT_PARTITION_COLUMN" ^
        --templateProperty jdbctospanner.sql.lowerBound="LOWERBOUND" ^
        --templateProperty jdbctospanner.sql.upperBound="UPPERBOUND" ^
        --templateProperty jdbctospanner.output.instance="INSTANCE" ^
        --templateProperty jdbctospanner.output.database="SPANNER_DATABASE" ^
        --templateProperty jdbctospanner.output.table="TABLE" ^
        --templateProperty jdbctospanner.output.saveMode="MODE" ^
        --templateProperty jdbctospanner.output.primaryKey="PRIMARY_KEY" ^
        --templateProperty jdbctospanner.output.batch.size="BATCHSIZE" ^
        --templateProperty jdbctospanner.temp.table="TEMPVIEW" ^
        --templateProperty jdbctospanner.temp.query="SQL_QUERY" ^
        --templateProperty spanner.jdbc.dialect="SPANNER_JDBC_DIALECT" 




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

  * The following variables are used to construct the required JDBC_CONNECTION_URL: 
    * JDBC_HOST, JDBC_PORT, JDBC_DATABASE, or, for Oracle, JDBC_SERVICE, JDBC_USERNAME, and JDBC_PASSWORD: Required. JDBC host, port, database, username, and password.
      * **MySQL:**
            
            jdbc:mysql://JDBC_HOST:JDBC_PORT/JDBC_DATABASE?user=JDBC_USERNAME&password=JDBC_PASSWORD

      * **PostgreSQL:**
            
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

    * QUERY or QUERY_FILE: Required. Set **either** `QUERY` or `QUERY_FILE` to specify the query to use to extract data from JDBC
    * INPUT_PARTITION_COLUMN, LOWERBOUND, UPPERBOUND, NUM_PARTITIONS: Optional. If used, all of the following parameters must be specified: 
      * **INPUT_PARTITION_COLUMN** : JDBC input table partition column name.
      * **LOWERBOUND** : JDBC input table partition column lower bound used to determine the partition stride.
      * **UPPERBOUND:** JDBC input table partition column upper bound used to decide the partition stride.
      * **NUM_PARTITIONS:** The maximum number of partitions that can be used for parallelism of table reads and writes. If specified, this value is used for the JDBC input and output connection. Default: `10`.
    * FETCHSIZE: Optional. How many rows to fetch per round trip. Default: 10.
    * JDBC_SESSION_INIT: Optional. Session initialization statement to read Java templates.
    * TEMPVIEW and SQL_QUERY: Optional. You can use these two optional parameters to apply a Spark SQL transformation while loading data into Spanner. TEMPVIEW is the temporary view name, and SQL_QUERY is the query statement. TEMPVIEW and the table name in SQL_QUERY must match. 
    * INSTANCE: Required. Spanner instance ID.
    * SPANNER_DATABASE: Required. Spanner database ID.
    * TABLE: Required. Spanner output table name.
    * SPANNER_JDBC_DIALECT: Required. Spanner JDBC dialect. Options: `googlesql` or `postgresql`. Defaults to `googlesql`.
    * MODE: Optional. Write mode for Spanner output. Options: `Append`, `Overwrite`, `Ignore`, or `ErrorIfExists`. Defaults to `ErrorIfExists`.
    * PRIMARY_KEY: Required. Comma separated Primary key columns needed when creating Spanner output table.
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
          "--template","JDBCTOSPANNER",
          "--templateProperty","log.level=LOG_LEVEL",
          "--templateProperty","project.id=PROJECT_ID",
          "--templateProperty","jdbctospanner.jdbc.url=JDBC_CONNECTION_URL",
          "--templateProperty","jdbctospanner.jdbc.driver.class.name=DRIVER",
          "--templateProperty","jdbctospanner.jdbc.fetchsize=FETCHSIZE",
          "--templateProperty","jdbctospanner.jdbc.sessioninitstatement=JDBC_SESSION_INIT",
          "--templateProperty","jdbctospanner.sql=QUERY",
          "--templateProperty","jdbctospanner.sql.file=QUERY_FILE",
          "--templateProperty","jdbctospanner.sql.numPartitions=NUM_PARTITIONS",
          "--templateProperty","jdbctospanner.sql.partitionColumn=INPUT_PARTITION_COLUMN",
          "--templateProperty","jdbctospanner.sql.lowerBound=LOWERBOUND",
          "--templateProperty","jdbctospanner.sql.upperBound=UPPERBOUND",
          "--templateProperty","jdbctospanner.output.instance=INSTANCE",
          "--templateProperty","jdbctospanner.output.database=SPANNER_DATABASE",
          "--templateProperty","jdbctospanner.output.table=TABLE",
          "--templateProperty","jdbctospanner.output.saveMode=MODE",
          "--templateProperty","jdbctospanner.output.primaryKey=PRIMARY_KEY",
          "--templateProperty","jdbctospanner.output.batch.size=BATCHSIZE",
          "--templateProperty","jdbctospanner.temp.table=TEMPVIEW",
          "--templateProperty","jdbctospanner.temp.query=SQL_QUERY",
          "--templateProperty spanner.jdbc.dialect=SPANNER_JDBC_DIALECT"
        ],
        "jarFileUris": [
          "gs://dataproc-templates-binaries/TEMPLATE_VERSION/java/dataproc-templates.jar",
          "JDBC_CONNECTOR_CLOUD_STORAGE_PATH"
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
