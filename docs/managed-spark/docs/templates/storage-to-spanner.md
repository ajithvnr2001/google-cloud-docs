---
url: https://docs.cloud.google.com/managed-spark/docs/templates/storage-to-spanner/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:32.370665+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/templates/storage-to-spanner/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Storage to Cloud Spanner template

Use the Managed Service for Apache Spark Cloud Storage to Spanner template to extract data from Cloud Storage to Spanner.

## Use the template

Run the template using the gcloud CLI or Managed Service for Apache Spark API.

### gcloud

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: Required. Your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project).
  * REGION: Required. [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * SUBNET: Optional. If a subnet is not specified, the subnet in the specified REGION in the `default` network is selected. 

**Example:** `projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME`

  * TEMPLATE_VERSION: Required. Specify `latest` for the latest template version, or the date of a specific version, for example, `2023-03-17_v0.1.0-beta` (visit [gs://dataproc-templates-binaries](https://console.cloud.google.com/storage/browser/dataproc-templates-binaries) or run `gcloud storage ls gs://dataproc-templates-binaries` to list available template versions).
  * CLOUD_STORAGE_INPUT_PATH: Required. Cloud Storage path from where input data will be read. 

**Example:** `gs://example-bucket/example-folder/`

  * FORMAT: Required. Input data format. Options: `avro`, `parquet`, or `orc`. **Note:** If `avro`, you must add "`file:///usr/lib/spark/connector/spark-avro.jar`" to the `jars` gcloud CLI flag or API field. 

**Example (the`file://` prefix references a Managed Service for Apache Spark jar file):**

`--jars=file:///usr/lib/spark/connector/spark-avro.jar,` [ ... other jars]
  * INSTANCE: Required. Spanner instance ID.
  * DATABASE: Required. Spanner database ID.
  * TABLE: Required. Spanner output table name.
  * SPANNER_JDBC_DIALECT: Required. Spanner JDBC dialect. Options: `googlesql` or `postgresql`. Defaults to `googlesql`.
  * MODE: Optional. Write mode for Spanner output. Options: `Append`, `Overwrite`, `Ignore`, or `ErrorifExists`. Defaults to `ErrorifExists`.
  * PRIMARY_KEY: Required. Comma separated Primary key columns needed when creating Spanner output table.
  * BATCHSIZE: Optional. Number of records to insert in one round trip into Spanner Table. Defaults to 1000.
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
        --jars="gs://dataproc-templates-binaries/TEMPLATE_VERSION/java/dataproc-templates.jar" \
        --subnet="SUBNET" \
        --kms-key="KMS_KEY" \
        --service-account="SERVICE_ACCOUNT" \
        --properties="PROPERTY=PROPERTY_VALUE" \
        --labels="LABEL=LABEL_VALUE" \
        -- --template GCSTOSPANNER \
        --templateProperty log.level="LOG_LEVEL" \
        --templateProperty project.id="PROJECT_ID" \
        --templateProperty gcs.spanner.input.format="FORMAT" \
        --templateProperty gcs.spanner.input.location="CLOUD_STORAGE_INPUT_PATH" \
        --templateProperty gcs.spanner.output.instance="INSTANCE" \
        --templateProperty gcs.spanner.output.database="DATABASE" \
        --templateProperty gcs.spanner.output.table="TABLE" \
        --templateProperty gcs.spanner.output.saveMode="MODE" \
        --templateProperty gcs.spanner.output.primaryKey="PRIMARY_KEY" \
        --templateProperty gcs.spanner.output.batchInsertSize="BATCHSIZE" \
        --templateProperty spanner.jdbc.dialect="SPANNER_JDBC_DIALECT"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud dataproc batches submit spark `
        --class=com.google.cloud.dataproc.templates.main.DataProcTemplate `
        --version="2.3" `
        --project="PROJECT_ID" `
        --region="REGION" `
        --jars="gs://dataproc-templates-binaries/TEMPLATE_VERSION/java/dataproc-templates.jar" `
        --subnet="SUBNET" `
        --kms-key="KMS_KEY" `
        --service-account="SERVICE_ACCOUNT" `
        --properties="PROPERTY=PROPERTY_VALUE" `
        --labels="LABEL=LABEL_VALUE" `
        -- --template GCSTOSPANNER `
        --templateProperty log.level="LOG_LEVEL" `
        --templateProperty project.id="PROJECT_ID" `
        --templateProperty gcs.spanner.input.format="FORMAT" `
        --templateProperty gcs.spanner.input.location="CLOUD_STORAGE_INPUT_PATH" `
        --templateProperty gcs.spanner.output.instance="INSTANCE" `
        --templateProperty gcs.spanner.output.database="DATABASE" `
        --templateProperty gcs.spanner.output.table="TABLE" `
        --templateProperty gcs.spanner.output.saveMode="MODE" `
        --templateProperty gcs.spanner.output.primaryKey="PRIMARY_KEY" `
        --templateProperty gcs.spanner.output.batchInsertSize="BATCHSIZE" `
        --templateProperty spanner.jdbc.dialect="SPANNER_JDBC_DIALECT"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud dataproc batches submit spark ^
        --class=com.google.cloud.dataproc.templates.main.DataProcTemplate ^
        --version="2.3" ^
        --project="PROJECT_ID" ^
        --region="REGION" ^
        --jars="gs://dataproc-templates-binaries/TEMPLATE_VERSION/java/dataproc-templates.jar" ^
        --subnet="SUBNET" ^
        --kms-key="KMS_KEY" ^
        --service-account="SERVICE_ACCOUNT" ^
        --properties="PROPERTY=PROPERTY_VALUE" ^
        --labels="LABEL=LABEL_VALUE" ^
        -- --template GCSTOSPANNER ^
        --templateProperty log.level="LOG_LEVEL" ^
        --templateProperty project.id="PROJECT_ID" ^
        --templateProperty gcs.spanner.input.format="FORMAT" ^
        --templateProperty gcs.spanner.input.location="CLOUD_STORAGE_INPUT_PATH" ^
        --templateProperty gcs.spanner.output.instance="INSTANCE" ^
        --templateProperty gcs.spanner.output.database="DATABASE" ^
        --templateProperty gcs.spanner.output.table="TABLE" ^
        --templateProperty gcs.spanner.output.saveMode="MODE" ^
        --templateProperty gcs.spanner.output.primaryKey="PRIMARY_KEY" ^
        --templateProperty gcs.spanner.output.batchInsertSize="BATCHSIZE" ^
        --templateProperty spanner.jdbc.dialect="SPANNER_JDBC_DIALECT"

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Required. Your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project).
  * REGION: Required. [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * SUBNET: Optional. If a subnet is not specified, the subnet in the specified REGION in the `default` network is selected. 

**Example:** `projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME`

  * TEMPLATE_VERSION: Required. Specify `latest` for the latest template version, or the date of a specific version, for example, `2023-03-17_v0.1.0-beta` (visit [gs://dataproc-templates-binaries](https://console.cloud.google.com/storage/browser/dataproc-templates-binaries) or run `gcloud storage ls gs://dataproc-templates-binaries` to list available template versions).
  * CLOUD_STORAGE_INPUT_PATH: Required. Cloud Storage path from where input data will be read. 

**Example:** `gs://example-bucket/example-folder/`

  * FORMAT: Required. Input data format. Options: `avro`, `parquet`, or `orc`. **Note:** If `avro`, you must add "`file:///usr/lib/spark/connector/spark-avro.jar`" to the `jars` gcloud CLI flag or API field. 

**Example (the`file://` prefix references a Managed Service for Apache Spark jar file):**

`--jars=file:///usr/lib/spark/connector/spark-avro.jar,` [ ... other jars]
  * INSTANCE: Required. Spanner instance ID.
  * DATABASE: Required. Spanner database ID.
  * TABLE: Required. Spanner output table name.
  * SPANNER_JDBC_DIALECT: Required. Spanner JDBC dialect. Options: `googlesql` or `postgresql`. Defaults to `googlesql`.
  * MODE: Optional. Write mode for Spanner output. Options: `Append`, `Overwrite`, `Ignore`, or `ErrorifExists`. Defaults to `ErrorifExists`.
  * PRIMARY_KEY: Required. Comma separated Primary key columns needed when creating Spanner output table.
  * BATCHSIZE: Optional. Number of records to insert in one round trip into Spanner Table. Defaults to 1000.
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
      "environmentConfig":{
        "executionConfig":{
          "subnetworkUri":"SUBNET",
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
          "--template","GCSTOSPANNER",
          "--templateProperty","project.id=PROJECT_ID",
          "--templateProperty","log.level=LOG_LEVEL",
          "--templateProperty","gcs.spanner.input.format=FORMAT",
          "--templateProperty","gcs.spanner.input.location=CLOUD_STORAGE_INPUT_PATH",
          "--templateProperty","gcs.spanner.output.instance=INSTANCE",
          "--templateProperty","gcs.spanner.output.database=DATABASE",
          "--templateProperty","gcs.spanner.output.table=TABLE",
          "--templateProperty","gcs.spanner.output.saveMode=MODE",
          "--templateProperty","gcs.spanner.output.primaryKey=PRIMARY_KEY",
          "--templateProperty","gcs.spanner.output.batchInsertSize=BATCHSIZE",
          "--templateProperty spanner.jdbc.dialect=SPANNER_JDBC_DIALECT"
        ],
        "jarFileUris":[
          "gs://dataproc-templates-binaries/TEMPLATE_VERSION/java/dataproc-templates.jar"
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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
