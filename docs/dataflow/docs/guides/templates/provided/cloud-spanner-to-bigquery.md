---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-to-bigquery/
title: Spanner to BigQuery template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:49.182443+00:00
---

# Spanner to BigQuery template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Spanner to BigQuery template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Spanner to BigQuery template is a batch pipeline that reads data from a Spanner table and writes the data to BigQuery.

## Pipeline requirements

  * The source Spanner table must exist prior to running the pipeline.
  * The BigQuery dataset must exist prior to running the pipeline.
  * A JSON file that describes your BigQuery schema. 

The file must contain a top-level JSON array titled `fields`. The contents of the `fields` array must use the following pattern:   
`{"name": "COLUMN_NAME", "type": "DATA_TYPE"}`.

The following JSON describes an example BigQuery schema:
        
        {
          "fields": [
            {
              "name": "location",
              "type": "STRING"
            },
            {
              "name": "name",
              "type": "STRING"
            },
            {
              "name": "age",
              "type": "STRING"
            },
            {
              "name": "color",
              "type": "STRING"
            },
            {
              "name": "coffee",
              "type": "STRING"
            }
          ]
        }

The Spanner to BigQuery batch template doesn't support importing data into [`STRUCT` (Record)](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type) fields in the target BigQuery table.




## Template parameters

### Required parameters

  * **spannerInstanceId** : The instance ID of the Spanner database to read from.
  * **spannerDatabaseId** : The database ID of the Spanner database to export.
  * **outputTableSpec** : The BigQuery output table location to write the output to. For example, `<PROJECT_ID>:<DATASET_NAME>.<TABLE_NAME>`.Depending on the `createDisposition` specified, the output table might be created automatically using the user provided Avro schema.



### Optional parameters

  * **spannerProjectId** : The ID of the project that the Spanner database resides in. The default value for this parameter is the project where the Dataflow pipeline is running.
  * **spannerTableId** : The table name of the Spanner database to export. Ignored if sqlQuery is set.
  * **spannerRpcPriority** : The request priority (<https://cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions>) for Spanner calls. Possible values are `HIGH`, `MEDIUM`, and `LOW`. The default value is `HIGH`.
  * **sqlQuery** : The SQL query to use to read data from the Spanner database. Required if spannerTableId is empty.
  * **bigQuerySchemaPath** : The Cloud Storage path (gs://) to the JSON file that defines your BigQuery schema. This is required if the Create Disposition is not CREATE_NEVER For example, `gs://your-bucket/your-schema.json`.
  * **writeDisposition** : The BigQuery WriteDisposition (<https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationload>) value. For example, `WRITE_APPEND`, `WRITE_EMPTY`, or `WRITE_TRUNCATE`. Defaults to `WRITE_APPEND`.
  * **createDisposition** : The BigQuery CreateDisposition (<https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationload>). For example, `CREATE_IF_NEEDED` and `CREATE_NEVER`. Defaults to `CREATE_IF_NEEDED`.
  * **useStorageWriteApi** : If `true`, the pipeline uses the BigQuery Storage Write API (<https://cloud.google.com/bigquery/docs/write-api>). The default value is `false`. For more information, see Using the Storage Write API (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#storage-write-api>).
  * **useStorageWriteApiAtLeastOnce** : When using the Storage Write API, specifies the write semantics. To use at-least-once semantics (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics>), set this parameter to `true`. To use exactly-once semantics, set the parameter to `false`. This parameter applies only when `useStorageWriteApi` is `true`. The default value is `false`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Spanner to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Cloud_Spanner_to_BigQuery_Flex \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --parameters \
           spannerInstanceId=SPANNER_INSTANCE_ID,\
           spannerDatabaseId=SPANNER_DATABASE_ID,\
           spannerTableId=SPANNER_TABLE_ID,\
           sqlQuery=SQL_QUERY,\
           outputTableSpec=OUTPUT_TABLE_SPEC,\

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `SPANNER_INSTANCE_ID`: the Spanner instance ID
  * `SPANNER_DATABASE_ID`: the Spanner database ID
  * `SPANNER_TABLE_ID`: the Spanner table name
  * `SQL_QUERY`: the SQL query
  * `OUTPUT_TABLE_SPEC`: the BigQuery table location



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launchParameter": {
         "jobName": "JOB_NAME",
         "parameters": {
           "spannerInstanceId": "SPANNER_INSTANCE_ID",
           "spannerDatabaseId": "SPANNER_DATABASE_ID",
           "spannerTableId": "SPANNER_TABLE_ID",
           "sqlQuery": "SQL_QUERY",
           "outputTableSpec": "OUTPUT_TABLE_SPEC",
         },
         "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Cloud_Spanner_to_BigQuery_Flex",
         "environment": { "maxWorkers": "10" }
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
  * `SPANNER_INSTANCE_ID`: the Spanner instance ID
  * `SPANNER_DATABASE_ID`: the Spanner database ID
  * `SPANNER_TABLE_ID`: the Spanner table name
  * `SQL_QUERY`: the SQL query
  * `OUTPUT_TABLE_SPEC`: the BigQuery table location



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2022 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License"); you may not
     * use this file except in compliance with the License. You may obtain a copy of
     * the License at
     *
     *   http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
     * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
     * License for the specific language governing permissions and limitations under
     * the License.
     */
    package com.google.cloud.teleport.v2.templates;
    
    import static com.google.cloud.teleport.v2.utils.GCSUtils.getGcsFileAsString;
    import static org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition.CREATE_NEVER;
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.SpannerToBigQueryOptions;
    import com.google.cloud.teleport.v2.transforms.BigQueryConverters;
    import com.google.cloud.teleport.v2.transforms.SpannerToBigQueryTransform.StructToJson;
    import com.google.cloud.teleport.v2.utils.BigQueryIOUtils;
    import com.google.common.base.Strings;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.WriteDisposition;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerConfig;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerIO;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    
    /** Template to read data from a Spanner table and write into a BigQuery table. */
    @Template(
        name = "Cloud_Spanner_to_BigQuery_Flex",
        category = TemplateCategory.BATCH,
        displayName = "Spanner to BigQuery",
        description =
            "The Spanner to BigQuery template is a batch pipeline that reads data from a Spanner table, and writes them to a BigQuery table.",
        optionsClass = SpannerToBigQueryOptions.class,
        flexContainerName = "googlecloud-to-googlecloud",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/spanner-to-bigquery",
        contactInformation = "https://cloud.google.com/support")
    public final class SpannerToBigQuery {
    
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        PipelineOptionsFactory.register(SpannerToBigQueryOptions.class);
        SpannerToBigQueryOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(SpannerToBigQueryOptions.class);
    
        BigQueryIOUtils.validateBQStorageApiOptionsBatch(options);
    
        Pipeline pipeline = Pipeline.create(options);
    
        SpannerConfig spannerConfig =
            SpannerConfig.create()
                .withProjectId(
                    options.getSpannerProjectId().isEmpty()
                        ? options.getProject()
                        : options.getSpannerProjectId())
                .withDatabaseId(options.getSpannerDatabaseId())
                .withInstanceId(options.getSpannerInstanceId())
                .withRpcPriority(options.getSpannerRpcPriority());
    
        SpannerIO.Read read = SpannerIO.read().withSpannerConfig(spannerConfig);
    
        if (!Strings.isNullOrEmpty(options.getSqlQuery())) {
          read = read.withQuery(options.getSqlQuery());
        } else if (!Strings.isNullOrEmpty(options.getSpannerTableId())) {
          read = read.withTable(options.getSpannerTableId());
        } else {
          throw new IllegalArgumentException("either sqlQuery or spannerTableId required");
        }
        if (Strings.isNullOrEmpty(options.getBigQuerySchemaPath())
            && CreateDisposition.valueOf(options.getCreateDisposition()) != CREATE_NEVER) {
          throw new IllegalArgumentException(
              "bigQuerySchemaPath is required if CreateDisposition is not CREATE_NEVER");
        }
        pipeline
            .apply(read)
            .apply(new StructToJson())
            .apply("Write To BigQuery", writeToBigQuery(options));
    
        pipeline.run();
      }
    
      private static Write<String> writeToBigQuery(SpannerToBigQueryOptions options) {
        if (CreateDisposition.valueOf(options.getCreateDisposition()) == CREATE_NEVER) {
          return BigQueryIO.<String>write()
              .to(options.getOutputTableSpec())
              .withWriteDisposition(WriteDisposition.valueOf(options.getWriteDisposition()))
              .withCreateDisposition(CreateDisposition.valueOf(options.getCreateDisposition()))
              .withExtendedErrorInfo()
              .withFormatFunction(BigQueryConverters::convertJsonToTableRow);
        }
        return BigQueryIO.<String>write()
            .to(options.getOutputTableSpec())
            .withWriteDisposition(WriteDisposition.valueOf(options.getWriteDisposition()))
            .withCreateDisposition(CreateDisposition.valueOf(options.getCreateDisposition()))
            .withExtendedErrorInfo()
            .withFormatFunction(BigQueryConverters::convertJsonToTableRow)
            .withJsonSchema(getGcsFileAsString(options.getBigQuerySchemaPath()));
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
