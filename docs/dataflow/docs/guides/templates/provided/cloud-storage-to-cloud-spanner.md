---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-cloud-spanner/
title: Cloud Storage Text to Spanner template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:11.005116+00:00
---

# Cloud Storage Text to Spanner template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-cloud-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Cloud Storage Text to Spanner template Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage Text to Spanner template is a batch pipeline that reads CSV text files from Cloud Storage and imports them to a Spanner database. 

## Pipeline requirements

  * The target Spanner database and table must exist.
  * You must have read permissions for the Cloud Storage bucket and write permissions for the target Spanner database.
  * The input Cloud Storage path containing the CSV files must exist.
  * You must create an import manifest file containing a JSON description of the CSV files, and you must store that manifest file in Cloud Storage.
  * If the target Spanner database already has a schema, any columns specified in the manifest file must have the same data types as their corresponding columns in the target database's schema.
  * The manifest file, encoded in ASCII or UTF-8, must match the following format: 

### Manifest format and example

The format of the manifest file corresponds to the following message type, shown here in [protocol buffer](https://developers.google.com/protocol-buffers/docs/proto3) format: 
        
        message ImportManifest {
          // The per-table import manifest.
          message TableManifest {
            // Required. The name of the destination table.
            string table_name = 1;
            // Required. The CSV files to import. This value can be either a filepath or a glob pattern.
            repeated string file_patterns = 2;
            // The schema for a table column.
            message Column {
              // Required for each Column that you specify. The name of the column in the
              // destination table.
              string column_name = 1;
              // Required for each Column that you specify. The type of the column.
              string type_name = 2;
            }
            // Optional. The schema for the table columns.
            repeated Column columns = 3;
          }
          // Required. The TableManifest of the tables to be imported.
          repeated TableManifest tables = 1;
        
          enum ProtoDialect {
            GOOGLE_STANDARD_SQL = 0;
            POSTGRESQL = 1;
          }
          // Optional. The dialect of the receiving database. Defaults to GOOGLE_STANDARD_SQL.
          ProtoDialect dialect = 2;
        }

The following example shows a manifest file for importing tables called `Albums` and `Singers` into a GoogleSQL-dialect database. The `Albums` table uses the column schema that the job retrieves from the database, and the `Singers` table uses the schema that the manifest file specifies: 
        
        {
          "tables": [
            {
              "table_name": "Albums",
              "file_patterns": [
                "gs://bucket1/Albums_1.csv",
                "gs://bucket1/Albums_2.csv"
              ]
            },
            {
              "table_name": "Singers",
              "file_patterns": [
                "gs://bucket1/Singers*.csv"
              ],
              "columns": [
                {"column_name": "SingerId", "type_name": "INT64"},
                {"column_name": "FirstName", "type_name": "STRING"},
                {"column_name": "LastName", "type_name": "STRING"}
              ]
            }
          ]
        }

  * Text files to be imported must be in CSV format, with ASCII or UTF-8 encoding. We recommend not using byte order mark (BOM) in UTF-8 encoded files.
  * Data must match one of the following [types](https://docs.cloud.google.com/spanner/docs/data-definition-language#data_types): 

### GoogleSQL
        
        BOOL
            INT64
            FLOAT64
            NUMERIC
            STRING
            DATE
            TIMESTAMP
            BYTES
            JSON

### PostgreSQL
        
        boolean
            bigint
            double precision
            numeric
            character varying, text
            date
            timestamp with time zone
            bytea

**Note:** If you do not specify the target table's column names and data types in the import manifest file, the columns in the CSV files must be in the same order as the columns in the target database. You can see the order of the columns in your table by running the following query: 
        
        SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME =
              TABLE_NAME ORDER BY ORDINAL_POSITION

**Warning:** If the target Spanner database is not empty, new data might overwrite pre-existing data.

## Template parameters

### Required parameters

    * **instanceId** : The instance ID of the Spanner database.
    * **databaseId** : The database ID of the Spanner database.
    * **importManifest** : The path in Cloud Storage to use when importing manifest files. For example, `gs://your-bucket/your-folder/your-manifest.json`.

### Optional parameters

    * **spannerHost** : The Cloud Spanner endpoint to call in the template. Only used for testing. For example, `https://batch-spanner.googleapis.com`. Defaults to: <https://batch-spanner.googleapis.com>.
    * **columnDelimiter** : The column delimiter that the source file uses. The default value is `,`. For example, `,`.
    * **fieldQualifier** : The character that must surround any value in the source file that contains the columnDelimiter. The default value is double quotes.
    * **trailingDelimiter** : Specifies whether the lines in the source files have trailing delimiters, that is, whether the `columnDelimiter` character appears at the end of each line, after the last column value. The default value is `true`.
    * **escape** : The escape character the source file uses. By default, this parameter is not set and the template does not use the escape character.
    * **nullString** : The string that represents a `NULL` value. By default, this parameter is not set and the template does not use the null string.
    * **dateFormat** : The format used to parse date columns. By default, the pipeline tries to parse the date columns as `yyyy-M-d[' 00:00:00']`, for example, as `2019-01-31` or `2019-1-1 00:00:00`. If your date format is different, specify the format using the java.time.format.DateTimeFormatter (<https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/format/DateTimeFormatter.html>) patterns.
    * **timestampFormat** : The format used to parse timestamp columns. If the timestamp is a long integer, then it is parsed as Unix epoch time. Otherwise, it is parsed as a string using the java.time.format.DateTimeFormatter.ISO_INSTANT (<https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/format/DateTimeFormatter.html#ISO_INSTANT>) format. For other cases, specify your own pattern string, for example, using `MMM dd yyyy HH:mm:ss.SSSVV` for timestamps in the form of `Jan 21 1998 01:02:03.456+08:00`.
    * **spannerProjectId** : The ID of the Google Cloud project that contains the Spanner database. If not set, the project ID of the default Google Cloud project is used.
    * **spannerPriority** : The request priority for Spanner calls. Possible values are `HIGH`, `MEDIUM`, and `LOW`. The default value is `MEDIUM`.
    * **handleNewLine** : If `true`, the input data can contain newline characters. Otherwise, newline characters cause an error. The default value is `false`. Enabling newline handling can reduce performance.
    * **invalidOutputPath** : The Cloud Storage path to use when writing rows that cannot be imported. For example, `gs://your-bucket/your-path`. Defaults to empty.
    * **maxNumRows** : The maximum number of rows to write to Spanner. The default value is 500.

If you need to use customized date or timestamp formats, make sure they're valid `[java.time.format.DateTimeFormatter](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/format/DateTimeFormatter.html#ISO_INSTANT)` patterns. The following table shows additional examples of customized formats for date and timestamp columns:

Type | Input value | Format | Remark  
---|---|---|---  
`DATE` | 2011-3-31 |  | By default, the template can parse this format. You don't need to specify the `dateFormat` parameter.  
`DATE` | 2011-3-31 00:00:00 |  | By default, the template can parse this format. You don't need to specify the format. If you like, you can use `yyyy-M-d' 00:00:00'`.  
`DATE` | 01 Apr, 18 | dd MMM, yy |   
`DATE` | Wednesday, April 3, 2019 AD | EEEE, LLLL d, yyyy G |   
`TIMESTAMP` | 2019-01-02T11:22:33Z  
2019-01-02T11:22:33.123Z  
2019-01-02T11:22:33.12356789Z  
|  | The default format `ISO_INSTANT` can parse this type of timestamp. You don't need to provide the `timestampFormat` parameter.  
`TIMESTAMP` | 1568402363 |  | By default, the template can parse this type of timestamp and treat it as Unix epoch time.  
`TIMESTAMP` | Tue, 3 Jun 2008 11:05:30 GMT | EEE, d MMM yyyy HH:mm:ss VV |   
`TIMESTAMP` | 2018/12/31 110530.123PST | yyyy/MM/dd HHmmss.SSSz |   
`TIMESTAMP` | 2019-01-02T11:22:33Z or 2019-01-02T11:22:33.123Z | yyyy-MM-dd'T'HH:mm:ss[.SSS]VV | If the input column is a mix of 2019-01-02T11:22:33Z and 2019-01-02T11:22:33.123Z, the default format can parse this type of timestamp. You don't need to provide your own format parameter. You can use `yyyy-MM-dd'T'HH:mm:ss[.SSS]VV` to handle both cases. You cannot use `yyyy-MM-dd'T'HH:mm:ss[.SSS]'Z'`, because the postfix 'Z' must be parsed as a time-zone ID, not a character literal. Internally, the timestamp column is converted to a `[java.time.Instant](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/Instant.html)`. Therefore, it must be specified in UTC or have time zone information associated with it. Local datetime, such as 2019-01-02 11:22:33, cannot be parsed as a valid `java.time.Instant`.   
`TIMESTAMP` | 2023-03-22 19:04:05  
2023-03-22 19:04:05.3  
2023-03-22 19:04:05.34  
2023-03-22 19:04:05.345  
| `yyyy-MM-dd HH:mm:ss[.[SSS][SS][S]]` | If the input column contains timestamps with varying fractional second precision, you can use brackets to specify an optional amount of digits. This example allows for 0, 1, 2, or 3 fractional digits.  
  
## Run the template

### Console

    1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
    2. In the **Job name** field, enter a unique job name. 
    3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

    4. From the **Dataflow template** drop-down menu, select the **Text Files on Cloud Storage to Cloud Spanner** template.
    5. In the provided parameter fields, enter your parameter values.
    6. Click **Run job**.

### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/GCS_Text_to_Cloud_Spanner \
        --region REGION_NAME \
        --parameters \
    instanceId=INSTANCE_ID,\
    databaseId=DATABASE_ID,\
    importManifest=GCS_PATH_TO_IMPORT_MANIFEST

Replace the following:

    * `JOB_NAME`: a unique job name of your choice 
    * `VERSION`: the version of the template that you want to use 

You can use the following values:

      * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
      * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
    * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
    * `INSTANCE_ID`: your Spanner instance ID
    * `DATABASE_ID`: your Spanner database ID
    * `GCS_PATH_TO_IMPORT_MANIFEST`: the Cloud Storage path to your import manifest file

### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/GCS_Text_to_Cloud_Spanner
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "instanceId": "INSTANCE_ID",
           "databaseId": "DATABASE_ID",
           "importManifest": "GCS_PATH_TO_IMPORT_MANIFEST"
       },
       "environment": {
           "machineType": "n1-standard-2"
       }
    }

Replace the following:

    * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
    * `JOB_NAME`: a unique job name of your choice 
    * `VERSION`: the version of the template that you want to use 

You can use the following values:

      * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
      * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
    * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
    * `INSTANCE_ID`: your Spanner instance ID
    * `DATABASE_ID`: your Spanner database ID
    * `GCS_PATH_TO_IMPORT_MANIFEST`: the Cloud Storage path to your import manifest file

## Template source code

### Java

This template's [source code](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/src/main/java/com/google/cloud/teleport/spanner/TextImportPipeline.java) is in the GoogleCloudPlatform/DataflowTemplates repository on GitHub.

## What's next

    * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
    * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

    * ### Products and pricing

      * [ See all products ](https://cloud.google.com/products/)
      * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
      * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
      * [ Contact sales ](https://cloud.google.com/contact/)
    * ### Support

      * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
      * [ Support ](https://cloud.google.com/support-hub/)
      * [ Release Notes ](https://docs.cloud.google.com/release-notes)
      * [ System status ](https://status.cloud.google.com)
    * ### Resources

      * [ GitHub ](https://github.com/googlecloudPlatform/)
      * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
      * [ Code samples ](https://docs.cloud.google.com/docs/samples)
      * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
      * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * ### Engage

      * [ Blog ](https://cloud.google.com/blog/)
      * [ Events ](https://cloud.google.com/events/)
      * [ X (Twitter) ](https://x.com/googlecloud)
      * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
      * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)

[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)
    * [ Android ](https://developer.android.com/)
    * [ Chrome ](https://developer.chrome.com/)
    * [ Firebase ](https://firebase.google.com/)
    * [ Google AI ](https://ai.google.com/)
    * [ About Google ](https://about.google/)
    * [ Privacy ](https://policies.google.com/privacy)
    * [ Site terms ](https://policies.google.com/terms?hl=en)
    * [ Google Cloud terms ](https://cloud.google.com/product-terms)
    * Manage cookies 
    * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
    * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)
    * English
    * Deutsch
    * Español
    * Español – América Latina
    * Français
    * Indonesia
    * Italiano
    * Português
    * Português – Brasil
    * עברית
    * 中文 – 简体
    * 中文 – 繁體
    * 日本語
    * 한국어



