---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-spanner-dv/
title: Cloud Storage Avro to Spanner Data Validation template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:33.516071+00:00
---

# Cloud Storage Avro to Spanner Data Validation template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-spanner-dv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Cloud Storage Avro to Spanner Data Validation template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Cloud Storage Avro files to Spanner Data Validation template is a batch pipeline that reads data from Cloud Storage and Spanner and compares them to validate migration correctness.

## Pipeline requirements

  * The Cloud Storage directory for Avro files must exist before pipeline execution. Generate these Avro files by running the [SourceDB to Cloud Spanner](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner) pipeline with the `gcsOutputDirectory` parameter.
  * The target BigQuery dataset for validation results must exist before pipeline execution.
  * The Spanner tables must exist before pipeline execution.
  * The Spanner tables must have a compatible schema (either directly or through schema mapping).
  * To validate a migration performed by the [SourceDB to Cloud Spanner pipeline](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner), you must pass identical values for any shared configurations (such as `sessionFilePath`, `schemaOverridesFilePath`, and `transformationJarPath`).



## Template parameters

### Required parameters

  * **gcsInputDirectory** : This directory is used to read the AVRO files of the records read from source. For example, `gs://your-bucket/your-path`.
  * **projectId** : This is the name of the Cloud Spanner project.
  * **instanceId** : The destination Cloud Spanner instance.
  * **databaseId** : The destination Cloud Spanner database.
  * **bigQueryDataset** : The BigQuery dataset ID where the validation results will be stored. For example, `validation_report_dataset`.



### Optional parameters

  * **spannerHost** : The Cloud Spanner endpoint to call in the template. For example, `https://batch-spanner.googleapis.com`. Defaults to: <https://batch-spanner.googleapis.com>.
  * **spannerPriority** : The request priority for Cloud Spanner calls. The value must be one of: [`HIGH`,`MEDIUM`,`LOW`]. Defaults to `HIGH`.
  * **sessionFilePath** : Session file path in Cloud Storage that contains mapping information from Spanner Migration Tool. Defaults to empty.
  * **schemaOverridesFilePath** : A file which specifies the table and the column name overrides from source to spanner. Defaults to empty.
  * **tableOverrides** : These are the table name overrides from source to spanner. They are written in the following format: [{SourceTableName1, SpannerTableName1}, {SourceTableName2, SpannerTableName2}] This example shows mapping Singers table to Vocalists and Albums table to Records. For example, `[{Singers, Vocalists}, {Albums, Records}]`. Defaults to empty.
  * **columnOverrides** : These are the column name overrides from source to spanner. They are written in the following format: [{SourceTableName1.SourceColumnName1, SourceTableName1.SpannerColumnName1}, {SourceTableName2.SourceColumnName1, SourceTableName2.SpannerColumnName1}]. Note that the SourceTableName should remain the same in both the source and spanner pair. To override table names, use tableOverrides.The example shows mapping SingerName to TalentName and AlbumName to RecordName in Singers and Albums table respectively. For example, `[{Singers.SingerName, Singers.TalentName}, {Albums.AlbumName, Albums.RecordName}]`. Defaults to empty.
  * **runId** : A unique identifier for the validation run. If not provided, the Dataflow Job Name will be used. For example, `run_20230101_120000`.
  * **transformationJarPath** : Custom jar location in Cloud Storage that contains the custom transformation logic for processing records. Defaults to empty.
  * **transformationClassName** : Fully qualified class name having the custom transformation logic. It is a mandatory field in case transformationJarPath is specified. Defaults to empty.
  * **transformationCustomParameters** : String containing any custom parameters to be passed to the custom transformation class. Defaults to empty.
  * **tables** : A comma-separated list of source tables to include in the validation run. Defaults to empty.
  * **tableConfigurationFilePath** : A GCS file path containing a JSON list of source tables to validate. This must be a JSON file with the structure `{"tableNames": ["table1", "table2"]}`. Optionally, `optionalConfigurations.<sourceTable>.spannerQuery` sets the Spanner query used to read that table, e.g. to restrict it to the selected `shardIds`. Key a Spanner-only table by its Spanner name. See the 'Validating a subset of shards' section of the module README.md for the query rules. Defaults to empty.
  * **shardIds** : A comma-separated list of logical shard IDs (the IDs used by the sourcedb-to-spanner template, which appear as the `<table>/<shardId>/` directory in the Avro output). When set, only those shards are validated. Tables with a session file `ShardIdColumn` are filtered on that column; every other in-scope table needs a `spannerQuery` in `tableConfigurationFilePath`, otherwise the job fails. For example, `shard_001,shard_007`. Defaults to empty.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Cloud Storage Avro files to Spanner Data Validation** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud CLI

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Avro_to_Spanner_Data_Validator \
        --region=REGION_NAME \
        --parameters \
           gcsInputDirectory=PATH_TO_AVRO_FILES,\
           projectId=PROJECT_ID,\
           instanceId=INSTANCE_ID,\
           databaseId=DATABASE_ID,\
           bigQueryDataset=BIGQUERY_DATASET

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `PATH_TO_AVRO_FILES`: the Cloud Storage path to the Avro files.
  * `PROJECT_ID`: the Spanner project ID.
  * `INSTANCE_ID`: the destination Spanner instance ID.
  * `DATABASE_ID`: the destination Spanner database ID.
  * `BIGQUERY_DATASET`: the BigQuery dataset ID for the validation results.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launchParameter": {
         "jobName": "JOB_NAME",
         "parameters": {
           "gcsInputDirectory": "PATH_TO_AVRO_FILES",
           "projectId": "PROJECT_ID",
           "instanceId": "INSTANCE_ID",
           "databaseId": "DATABASE_ID",
           "bigQueryDataset": "BIGQUERY_DATASET"
         },
         "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Avro_to_Spanner_Data_Validator"
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
  * `PATH_TO_AVRO_FILES`: the Cloud Storage path to the Avro files.
  * `PROJECT_ID`: the Spanner project ID.
  * `INSTANCE_ID`: the destination Spanner instance ID.
  * `DATABASE_ID`: the destination Spanner database ID.
  * `BIGQUERY_DATASET`: the BigQuery dataset ID for the validation results.



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2026 Google LLC
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
    
    import static com.google.cloud.teleport.v2.constants.GCSSpannerDVConstants.SOURCE_TAG;
    import static com.google.cloud.teleport.v2.constants.GCSSpannerDVConstants.SPANNER_TAG;
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.config.TableConfiguration;
    import com.google.cloud.teleport.v2.dto.ComparisonRecord;
    import com.google.cloud.teleport.v2.fn.SchemaMapperProviderFn;
    import com.google.cloud.teleport.v2.options.GCSSpannerDVOptions;
    import com.google.cloud.teleport.v2.spanner.ddl.Ddl;
    import com.google.cloud.teleport.v2.spanner.migrations.schema.ISchemaMapper;
    import com.google.cloud.teleport.v2.spanner.migrations.transformation.CustomTransformation;
    import com.google.cloud.teleport.v2.transforms.MatchRecordsTransform;
    import com.google.cloud.teleport.v2.transforms.ReportResultsTransform;
    import com.google.cloud.teleport.v2.transforms.SourceReaderTransform;
    import com.google.cloud.teleport.v2.transforms.SpannerInformationSchemaProcessorTransform;
    import com.google.cloud.teleport.v2.transforms.SpannerReaderTransform;
    import com.google.common.annotations.VisibleForTesting;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerConfig;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.SerializableFunction;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.PCollectionView;
    import org.joda.time.Instant;
    
    @Template(
        name = "Avro_to_Spanner_Data_Validator",
        category = TemplateCategory.BATCH,
        displayName = "Cloud Storage Avro files to Spanner Data Validation",
        description =
            "Batch pipeline that reads data from Cloud Storage and Spanner and compares them to validate migration"
                + " correctness.",
        optionsClass = GCSSpannerDVOptions.class,
        flexContainerName = "avro-to-spanner-dv",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-spanner-dv",
        contactInformation = "https://cloud.google.com/support",
        preview = true,
        requirements = {
          "The Cloud Storage directory for Avro files must exist before pipeline execution.",
          "The target BigQuery dataset for validation results must exist before pipeline execution.",
          "The Spanner tables must exist before pipeline execution.",
          "The Spanner tables must have a compatible schema (either directly or through schema mapping)."
        })
    public class GCSSpannerDV {
    
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        GCSSpannerDVOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(GCSSpannerDVOptions.class);
        run(options);
      }
    
      public static PipelineResult run(GCSSpannerDVOptions options) {
        Pipeline pipeline = Pipeline.create(options);
    
        TableConfiguration tableConfig = TableConfiguration.parseFromOptions(options);
    
        SpannerConfig spannerConfig = createSpannerConfig(options);
    
        // Fetch Spanner DDL using Info schema
        final PCollectionView<Ddl> ddlView =
            pipeline.apply(
                "ReadSpannerInformationSchema",
                new SpannerInformationSchemaProcessorTransform(spannerConfig));
    
        // Get Schema mapper provider, we get Ddl from a side input
        // so the mapper has to be initialized lazily
        SerializableFunction<Ddl, ISchemaMapper> schemaMapperProvider =
            new SchemaMapperProviderFn(
                options.getSessionFilePath(),
                options.getSchemaOverridesFilePath(),
                options.getTableOverrides(),
                options.getColumnOverrides());
    
        CustomTransformation customTransformation =
            CustomTransformation.builder(
                    options.getTransformationJarPath(), options.getTransformationClassName())
                .setCustomParameters(options.getTransformationCustomParameters())
                .build();
    
        // Get Source records hashes
        PCollection<ComparisonRecord> sourceRecords =
            pipeline.apply(
                "ReadSourceRecords",
                new SourceReaderTransform(
                    options.getGcsInputDirectory(),
                    ddlView,
                    schemaMapperProvider,
                    customTransformation,
                    tableConfig));
    
        // Get Spanner records hashes
        PCollection<ComparisonRecord> spannerRecords =
            pipeline.apply(
                "ReadSpannerRecords",
                new SpannerReaderTransform(spannerConfig, ddlView, schemaMapperProvider, tableConfig));
    
        PCollectionTuple inputs =
            PCollectionTuple.of(SOURCE_TAG, sourceRecords).and(SPANNER_TAG, spannerRecords);
    
        // Match records to determine equivalence
        PCollectionTuple matchResults = inputs.apply("MatchRecords", new MatchRecordsTransform());
    
        // Report results of the validation
        Instant startTimestamp = Instant.now();
        String runId = options.getRunId();
        if (runId == null) {
          runId = String.format("%s_%s", options.getJobName(), startTimestamp);
        }
    
        matchResults.apply(
            "ReportResults",
            new ReportResultsTransform(options.getBigQueryDataset(), runId, startTimestamp));
    
        return pipeline.run();
      }
    
      @VisibleForTesting
      static SpannerConfig createSpannerConfig(GCSSpannerDVOptions options) {
        return SpannerConfig.create()
            .withProjectId(ValueProvider.StaticValueProvider.of(options.getProjectId()))
            .withHost(ValueProvider.StaticValueProvider.of(options.getSpannerHost()))
            .withInstanceId(ValueProvider.StaticValueProvider.of(options.getInstanceId()))
            .withDatabaseId(ValueProvider.StaticValueProvider.of(options.getDatabaseId()))
            .withRpcPriority(ValueProvider.StaticValueProvider.of(options.getSpannerPriority()));
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
