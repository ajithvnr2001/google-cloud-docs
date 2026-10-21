---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-bigquery/
title: Bigtable change streams to BigQuery template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:43:22.856738+00:00
---

# Bigtable change streams to BigQuery template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Bigtable change streams to BigQuery template Stay organized with collections  Save and categorize content based on your preferences. 

The Bigtable change streams to BigQuery template is a streaming pipeline that streams Bigtable data change records and writes them into BigQuery tables by using Dataflow.

A [Bigtable change stream](https://docs.cloud.google.com/bigtable/docs/change-streams-overview) lets you subscribe to data mutations on a per-table basis. When you subscribe to table change streams, the following constraints apply:

  * Only modified cells and descriptors of delete operations are returned.
  * Only the new value of a modified cell is returned.



When data change records are written to BigQuery, rows might be inserted out of order compared to the original Bigtable commit timestamp ordering.

Changelog table rows that can't be written to BigQuery due to persistent error are permanently placed into a dead-letter queue (unprocessed messages queue) directory in Cloud Storage for human review or further processing by the user.

If the necessary BigQuery table doesn't exist, the pipeline creates it. Otherwise, an existing BigQuery table is used. The schema of existing BigQuery tables must contain the columns in the following table.

Each new BigQuery row includes one data change record returned by the change stream from its corresponding row in your Bigtable table.

## BigQuery output table schema

Column name | Type | Nullable | Description  
---|---|---|---  
`row_key` | `STRING` or `BYTES` | No | The row key of the changed row. When the `writeRowkeyAsBytes` pipeline option is set to `true`, the type of the column must be `BYTES`. Otherwise, use the `STRING` type.  
`mod_type` | `STRING` | No | The type of the row mutation. Use one of the following values: `SET_CELL`, `DELETE_CELLS`, or `DELETE_FAMILY`.  
`column_family` | `STRING` | No | The column family affected by the row mutation.  
`column` | `STRING` | Yes | The column qualifier affected by the row mutation. For the `DELETE_FAMILY` mutation type, set to `NULL`.  
`commit_timestamp` | `TIMESTAMP` | No | The time when Bigtable applies the mutation.  
`big_query_commit_timestamp` | `TIMESTAMP` | Yes | Optional: Specifies the time when BigQuery writes the row to an output table. The field isn't populated if the column name is present in the `bigQueryChangelogTableFieldsToIgnore` pipeline option value.  
`timestamp` | `TIMESTAMP` or `INT64` | Yes | The timestamp value of the cell affected by the mutation. When the `writeNumericTimestamps` pipeline option is set to `true`, the type of the column must be `INT64`. Otherwise use the `TIMESTAMP` type. For `DELETE_CELLS` and `DELETE_FAMILY` mutation types, set to `NULL`.  
`timestamp_from` | `TIMESTAMP` or `INT64` | Yes | Describes an inclusive start of the timestamp interval for all cells deleted by the `DELETE_CELLS` mutation. For other mutation types, set to `NULL`.  
`timestamp_to` | `TIMESTAMP` or `INT64` | Yes | Describes an exclusive end of the timestamp interval for all cells deleted by the `DELETE_CELLS` mutation. For other mutation types, set to `NULL`.  
`is_gc` | `BOOL` | No | Optional: When the mutation is triggered by a garbage collection policy, set to `true`. In all other cases, set to `false`. The field isn't populated when the column name is present in the `bigQueryChangelogTableFieldsToIgnore` pipeline option value.  
`source_instance` | `STRING` | No | Optional: Describes the name of the Bigtable instance that the mutation comes from. The field isn't populated when the column name is present in the `bigQueryChangelogTableFieldsToIgnore` pipeline option value.  
`source_cluster` | `STRING` | No | Optional: Describes the name of the Bigtable cluster that the mutation comes from. The field isn't populated when the column name is present in the `bigQueryChangelogTableFieldsToIgnore` pipeline option value.  
`source_table` | `STRING` | No | Optional: Describes the name of the Bigtable table that the mutation applies to. The value in this column might be useful if multiple Bigtable tables stream changes to the same BigQuery table. The field isn't populated when the column name is present in the `bigQueryChangelogTableFieldsToIgnore` pipeline option value.  
`tiebreaker` | `INT64` | No | Optional: When two mutations are registered at the same time by different Bigtable clusters, the mutation with the highest `tiebreaker` value is applied to the source table. Mutations with lower `tiebreaker` values are discarded. The field isn't populated when the column name is present in the `bigQueryChangelogTableFieldsToIgnore` pipeline option value.  
`value` | `STRING` or `BYTES` | Yes | The new value set by the mutation. When the `writeValuesAsBytes` pipeline option is set to `true`, the type of the column must be `BYTES`. Otherwise, use the `STRING` type. The value is set for `SET_CELL` mutations. For other mutation types, the value is set to `NULL`.  
  
## Pipeline requirements

  * The specified Bigtable source instance.
  * The specified Bigtable source table. The table must have change streams enabled.
  * The specified Bigtable application profile.
  * The specified BigQuery destination dataset.



## Template parameters

### Required parameters

  * **bigQueryDataset** : The dataset name of the destination BigQuery table.
  * **bigtableChangeStreamAppProfile** : The Bigtable application profile ID. The application profile must use single-cluster routing and allow single-row transactions.
  * **bigtableReadInstanceId** : The source Bigtable instance ID.
  * **bigtableReadTableId** : The source Bigtable table ID.



### Optional parameters

  * **writeRowkeyAsBytes** : Whether to write rowkeys as BigQuery `BYTES`. When set to `true`, row keys are written to the `BYTES` column. Otherwise, rowkeys are written to the `STRING` column. Defaults to `false`.
  * **writeValuesAsBytes** : When set to `true`, values are written to a column of type BYTES, otherwise to a column of type STRING . Defaults to: `false`.
  * **writeNumericTimestamps** : Whether to write the Bigtable timestamp as BigQuery INT64. When set to `true`, values are written to the INT64 column. Otherwise, values are written to the `TIMESTAMP` column. Columns affected: `timestamp`, `timestamp_from`, and `timestamp_to`. Defaults to `false`. When set to `true`, the time is measured in microseconds since the Unix epoch (January 1, 1970 at UTC).
  * **bigQueryProjectId** : The BigQuery dataset project ID. The default is the project for the Dataflow job.
  * **bigQueryChangelogTableName** : Destination BigQuery table name. If not specified, the value `bigtableReadTableId + "_changelog"` is used. Defaults to empty.
  * **bigQueryChangelogTablePartitionGranularity** : Specifies a granularity for partitioning the changelog table. When set, the table is partitioned. Use one of the following supported values: `HOUR`, `DAY`, `MONTH`, or `YEAR`. By default, the table isn't partitioned.
  * **bigQueryChangelogTablePartitionExpirationMs** : Sets the changelog table partition expiration time, in milliseconds. When set to `true`, partitions older than the specified number of milliseconds are deleted. By default, no expiration is set.
  * **bigQueryChangelogTableFieldsToIgnore** : A comma-separated list of the changelog columns that, when specified, aren't created and populated. Use one of the following supported values: `is_gc`, `source_instance`, `source_cluster`, `source_table`, `tiebreaker`, or `big_query_commit_timestamp`. By default, all columns are populated.
  * **dlqDirectory** : The directory to use for the dead-letter queue. Records that fail to be processed are stored in this directory. The default is a directory under the Dataflow job's temp location. In most cases, you can use the default path.
  * **bigtableChangeStreamMetadataInstanceId** : The Bigtable change streams metadata instance ID. Defaults to empty.
  * **bigtableChangeStreamMetadataTableTableId** : The ID of the Bigtable change streams connector metadata table. If not provided, a Bigtable change streams connector metadata table is automatically created during pipeline execution. Defaults to empty.
  * **bigtableChangeStreamCharset** : The Bigtable change streams charset name. Defaults to: UTF-8.
  * **bigtableChangeStreamStartTimestamp** : The starting timestamp (<https://tools.ietf.org/html/rfc3339>), inclusive, to use for reading change streams. For example, `2022-05-05T07:59:59Z`. Defaults to the timestamp of the pipeline start time.
  * **bigtableChangeStreamIgnoreColumnFamilies** : A comma-separated list of column family name changes to ignore. Defaults to empty.
  * **bigtableChangeStreamIgnoreColumns** : A comma-separated list of column name changes to ignore. Example: "cf1:col1,cf2:col2". Defaults to empty.
  * **bigtableChangeStreamName** : A unique name for the client pipeline. Lets you resume processing from the point at which a previously running pipeline stopped. Defaults to an automatically generated name. See the Dataflow job logs for the value used.
  * **bigtableChangeStreamResume** : When set to `true`, a new pipeline resumes processing from the point at which a previously running pipeline with the same `bigtableChangeStreamName` value stopped. If the pipeline with the given `bigtableChangeStreamName` value has never run, a new pipeline doesn't start. When set to `false`, a new pipeline starts. If a pipeline with the same `bigtableChangeStreamName` value has already run for the given source, a new pipeline doesn't start. Defaults to `false`.
  * **bigtableReadChangeStreamTimeoutMs** : The timeout for Bigtable ReadChangeStream requests in milliseconds.
  * **bigtableReadProjectId** : The Bigtable project ID. The default is the project for the Dataflow job.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Bigtable change streams to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Bigtable_Change_Streams_to_BigQuery \
        --parameters \
    bigtableReadInstanceId=BIGTABLE_INSTANCE_ID,\
    bigtableReadTableId=BIGTABLE_TABLE_ID,\
    bigtableChangeStreamAppProfile=BIGTABLE_APPLICATION_PROFILE_ID,\
    bigQueryDataset=BIGQUERY_DESTINATION_DATASET

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `BIGTABLE_INSTANCE_ID`: your Bigtable instance id.
  * `BIGTABLE_TABLE_ID`: your Bigtable table id.
  * `BIGTABLE_APPLICATION_PROFILE_ID`: your Bigtable application profile id.
  * `BIGQUERY_DESTINATION_DATASET`: the BigQuery destination dataset name



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
      "launch_parameter": {
        "jobName": "JOB_NAME",
        "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Bigtable_Change_Streams_to_BigQuery",
        "parameters": {
            "bigtableReadInstanceId": "BIGTABLE_INSTANCE_ID",
            "bigtableReadTableId": "BIGTABLE_TABLE_ID",
            "bigtableChangeStreamAppProfile": "BIGTABLE_APPLICATION_PROFILE_ID",
            "bigQueryDataset": "BIGQUERY_DESTINATION_DATASET"
        }
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
  * `BIGTABLE_INSTANCE_ID`: your Bigtable instance id.
  * `BIGTABLE_TABLE_ID`: your Bigtable table id.
  * `BIGTABLE_APPLICATION_PROFILE_ID`: your Bigtable application profile id.
  * `BIGQUERY_DESTINATION_DATASET`: the BigQuery destination dataset name



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2023 Google LLC
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
    package com.google.cloud.teleport.v2.templates.bigtablechangestreamstobigquery;
    
    import com.google.api.services.bigquery.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).[TableRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Table.TableRow.html);
    import com.google.cloud.[Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId.html);
    import com.google.cloud.bigtable.[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[ChangeStreamMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ChangeStreamMutation.html);
    import com.google.cloud.bigtable.[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[DeleteCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteCells.html);
    import com.google.cloud.bigtable.[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[DeleteFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteFamily.html);
    import com.google.cloud.bigtable.[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Entry.html);
    import com.google.cloud.bigtable.[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[SetCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html);
    import com.google.cloud.teleport.metadata.[Template](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.Template.html);
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.bigtable.options.BigtableCommonOptions.ReadChangeStreamOptions;
    import com.google.cloud.teleport.v2.bigtable.options.BigtableCommonOptions.ReadOptions;
    import com.google.cloud.teleport.v2.bigtable.utils.UnsupportedEntryException;
    import com.google.cloud.teleport.v2.cdc.dlq.DeadLetterQueueManager;
    import com.google.cloud.teleport.v2.options.BigtableChangeStreamToBigQueryOptions;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstobigquery.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).[BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html);
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstobigquery.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).Mod;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstobigquery.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).ModType;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstobigquery.schemautils.BigQueryUtils;
    import com.google.cloud.teleport.v2.transforms.DLQWriteTransform;
    import com.google.cloud.teleport.v2.utils.[BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html);
    import java.util.ArrayList;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html);
    import org.apache.beam.sdk.[PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html);
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.WriteDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy;
    import org.apache.beam.sdk.io.gcp.bigquery.[WriteResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.WriteResult.html);
    import org.apache.beam.sdk.io.gcp.bigtable.BigtableIO;
    import org.apache.beam.sdk.io.gcp.bigtable.BigtableIO.ExistingPipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.Values;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.commons.lang3.StringUtils;
    import org.joda.time.Instant;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * This pipeline ingests {@link ChangeStreamMutation} from Bigtable change stream. The {@link
     * ChangeStreamMutation} is then broken into {@link Mod}, which converted into {@link TableRow} and
     * inserted into BigQuery table.
     */
    @Template(
        name = "Bigtable_Change_Streams_to_BigQuery",
        category = TemplateCategory.STREAMING,
        displayName = "Cloud Bigtable Change Streams to BigQuery",
        description =
            "Streaming pipeline. Streams Bigtable data change records and writes them into BigQuery using Dataflow Runner V2.",
        optionsClass = BigtableChangeStreamToBigQueryOptions.class,
        optionsOrder = {
          BigtableChangeStreamToBigQueryOptions.class,
          ReadChangeStreamOptions.class,
          ReadOptions.class
        },
        skipOptions = {
          "bigtableReadAppProfile",
          "bigtableAdditionalRetryCodes",
          "bigtableRpcAttemptTimeoutMs",
          "bigtableRpcTimeoutMs"
        },
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-bigquery",
        flexContainerName = "googlecloud-to-googlecloud",
        contactInformation = "https://cloud.google.com/support",
        streaming = true)
    public final class BigtableChangeStreamsToBigQuery {
      private static final Logger LOG = LoggerFactory.getLogger(BigtableChangeStreamsToBigQuery.class);
    
      private static final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) USE_RUNNER_V2_EXPERIMENT = "use_runner_v2";
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) {
        LOG.info("Starting to replicate change records from Cloud Bigtable change streams to BigQuery");
    
        BigtableChangeStreamToBigQueryOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(BigtableChangeStreamToBigQueryOptions.class);
    
        run(options);
      }
    
      private static void setOptions(BigtableChangeStreamToBigQueryOptions options) {
        options.setStreaming(true);
        options.setEnableStreamingEngine(true);
    
        // Add use_runner_v2 to the experiments option, since change streams connector is only supported
        // on Dataflow runner v2.
        List<String> experiments = options.getExperiments();
        if (experiments == null) {
          experiments = new ArrayList<>();
        }
        boolean hasUseRunnerV2 = false;
        for ([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) experiment : experiments) {
          if (experiment.equalsIgnoreCase(USE_RUNNER_V2_EXPERIMENT)) {
            hasUseRunnerV2 = true;
            break;
          }
        }
        if (!hasUseRunnerV2) {
          experiments.add(USE_RUNNER_V2_EXPERIMENT);
        }
        options.[setExperiments](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListExperimentsResponse.Builder.html#com_google_cloud_dialogflow_cx_v3_ListExperimentsResponse_Builder_setExperiments_int_com_google_cloud_dialogflow_cx_v3_Experiment_)(experiments);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      public static [PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html) run(BigtableChangeStreamToBigQueryOptions options) {
        setOptions(options);
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) changelogTableName = getBigQueryChangelogTableName(options);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigtableProject = getBigtableProjectId(options);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigQueryProject = getBigQueryProjectId(options);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigQueryDataset = options.getBigQueryDataset();
    
        // If dataset doesn't exist and not checked, pipeline will start failing only after it sees the
        // first change from Cloud Bigtable. BigQueryIO can create table if it doesn't exist, but it
        // cannot create a dataset
        validateBigQueryDatasetExists(bigQueryProject, bigQueryDataset);
    
        // Retrieve and parse the startTimestamp
        Instant startTimestamp =
            options.getBigtableChangeStreamStartTimestamp().isEmpty()
                ? Instant.[now](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_now__)()
                : toInstant([Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[parseTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_parseTimestamp_java_lang_String_)(options.getBigtableChangeStreamStartTimestamp()));
    
        [BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html) sourceInfo =
            new [BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html)(
                options.getBigtableReadInstanceId(),
                options.getBigtableReadTableId(),
                getBigtableCharset(options),
                options.getBigtableChangeStreamIgnoreColumnFamilies(),
                options.getBigtableChangeStreamIgnoreColumns(),
                startTimestamp);
    
        [BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html) destinationInfo =
            new [BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html)(
                bigQueryProject,
                bigQueryDataset,
                changelogTableName,
                options.getWriteRowkeyAsBytes(),
                options.getWriteValuesAsBytes(),
                options.getWriteNumericTimestamps(),
                options.getBigQueryChangelogTablePartitionGranularity(),
                options.getBigQueryChangelogTablePartitionExpirationMs(),
                options.getBigQueryChangelogTableFieldsToIgnore());
    
        BigQueryUtils bigQuery = new BigQueryUtils(sourceInfo, destinationInfo);
    
        [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html) pipeline = [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html).create(options);
        DeadLetterQueueManager dlqManager = buildDlqManager(options);
    
        BigtableIO.ReadChangeStream readChangeStream =
            BigtableIO.[readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_)()
                .withChangeStreamName(options.getBigtableChangeStreamName())
                .withExistingPipelineOptions(
                    options.getBigtableChangeStreamResume()
                        ? ExistingPipelineOptions.RESUME_OR_FAIL
                        : ExistingPipelineOptions.FAIL_IF_EXISTS)
                .withProjectId(bigtableProject)
                .withMetadataTableInstanceId(options.getBigtableChangeStreamMetadataInstanceId())
                .withInstanceId(options.getBigtableReadInstanceId())
                .withTableId(options.getBigtableReadTableId())
                .withAppProfileId(options.getBigtableChangeStreamAppProfile())
                .withStartTime(startTimestamp);
    
        if (!StringUtils.isBlank(options.getBigtableChangeStreamMetadataTableTableId())) {
          readChangeStream =
              [readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_).withMetadataTableTableId(
                  options.getBigtableChangeStreamMetadataTableTableId());
        }
    
        PCollection<ChangeStreamMutation> dataChangeRecord =
            [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__)
                .apply("Read from Cloud Bigtable Change Streams", readChangeStream)
                .apply(Values.create());
    
        PCollection<TableRow> changeStreamMutationToTableRow =
            dataChangeRecord.apply(
                "ChangeStreamMutation To TableRow",
                ParDo.of(new ChangeStreamMutationToTableRowFn(sourceInfo, bigQuery)));
    
        Write<TableRow> bigQueryWrite =
            BigQueryIO.<TableRow>write()
                .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(destinationInfo.getBigQueryTableReference())
                .withSchema(bigQuery.getDestinationTableSchema())
                .withFormatFunction(element -> element)
                .withFormatRecordOnFailureFunction(element -> element)
                .withCreateDisposition(CreateDisposition.CREATE_IF_NEEDED)
                .withWriteDisposition(WriteDisposition.WRITE_APPEND)
                .withExtendedErrorInfo()
                .withMethod(Write.Method.STORAGE_API_AT_LEAST_ONCE)
                .withNumStorageWriteApiStreams(0)
                .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors());
    
        if (destinationInfo.isPartitioned()) {
          bigQueryWrite = bigQueryWrite.withTimePartitioning(bigQuery.getTimePartitioning());
        }
    
        // Unfortunately, due to https://github.com/apache/beam/issues/24090, it is no longer possible
        // to pass metadata via fake columns when writing to BigQuery. Previously we'd pass something
        // like retry count and then format it out before writing, but BQ would return original object
        // which would allow us to increment retry count and store it to DLQ with incremented number.
        // Because WRITE API doesn't allow access to original object, all metadata values are stripped
        // and we can only rely on retry policy and put all other persistently failing rows to DLQ as
        // a non-retriable severe failure.
        //
        // Since we're not going to be retrying such failures, we'll not use any reading from DLQ
        // capability.
    
        [WriteResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.WriteResult.html) writeResult =
            changeStreamMutationToTableRow.apply("Write To BigQuery", bigQueryWrite);
    
        writeResult
            .getFailedStorageApiInserts()
            .apply(
                "Failed Mod JSON During BigQuery Writes",
                MapElements.via(new BigQueryDeadLetterQueueSanitizer()))
            .apply(
                "Write rejected TableRow JSON To DLQ",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqManager.getSevereDlqDirectory() + "YYYY/MM/dd/HH/mm/")
                    .withTmpDirectory(dlqManager.getSevereDlqDirectory() + "tmp/")
                    .setIncludePaneInfo(true)
                    .build());
    
        return [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).run();
      }
    
      private static void validateBigQueryDatasetExists(
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigQueryProject, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigQueryDataset) {
        [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) options = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).newBuilder().build();
        options.setThrowNotFound(true);
    
        [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigQuery = options.getService();
        bigQuery.getDataset([DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId.html).of(bigQueryProject, bigQueryDataset));
      }
    
      private static Instant toInstant([Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html) timestamp) {
        if (timestamp == null) {
          return null;
        } else {
          return Instant.ofEpochMilli(timestamp.[getSeconds](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_getSeconds__)() * 1000 + timestamp.[getNanos](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_getNanos__)() / 1000000);
        }
      }
    
      private static DeadLetterQueueManager buildDlqManager(
          BigtableChangeStreamToBigQueryOptions options) {
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tempLocation =
            options.as(DataflowPipelineOptions.class).getTempLocation().endsWith("/")
                ? options.as(DataflowPipelineOptions.class).getTempLocation()
                : options.as(DataflowPipelineOptions.class).getTempLocation() + "/";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) dlqDirectory =
            options.getDlqDirectory().isEmpty() ? tempLocation + "dlq/" : options.getDlqDirectory();
    
        LOG.info("Dead letter queue directory: {}", dlqDirectory);
        return DeadLetterQueueManager.create(dlqDirectory, 1);
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getBigtableCharset(BigtableChangeStreamToBigQueryOptions options) {
        return StringUtils.isEmpty(options.getBigtableChangeStreamCharset())
            ? "UTF-8"
            : options.getBigtableChangeStreamCharset();
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getBigtableProjectId(BigtableChangeStreamToBigQueryOptions options) {
        return StringUtils.isEmpty(options.getBigtableReadProjectId())
            ? options.getProject()
            : options.getBigtableReadProjectId();
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getBigQueryChangelogTableName(
          BigtableChangeStreamToBigQueryOptions options) {
        return StringUtils.isEmpty(options.getBigQueryChangelogTableName())
            ? options.getBigtableReadTableId() + "_changelog"
            : options.getBigQueryChangelogTableName();
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getBigQueryProjectId(BigtableChangeStreamToBigQueryOptions options) {
        return StringUtils.isEmpty(options.getBigQueryProjectId())
            ? options.getProject()
            : options.getBigQueryProjectId();
      }
    
      /**
       * DoFn that converts a {@link ChangeStreamMutation} to multiple {@link Mod} in serialized JSON
       * format.
       */
      static class ChangeStreamMutationToTableRowFn extends DoFn<ChangeStreamMutation, TableRow> {
        private final [BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html) sourceInfo;
        private final BigQueryUtils bigQuery;
    
        ChangeStreamMutationToTableRowFn([BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html) source, BigQueryUtils bigQuery) {
          this.sourceInfo = source;
          this.bigQuery = bigQuery;
        }
    
        @ProcessElement
        public void process(@Element [ChangeStreamMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ChangeStreamMutation.html) input, OutputReceiver<TableRow> receiver)
            throws Exception {
          for ([Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Entry.html) entry : input.[getEntries](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ChangeStreamMutation.html#com_google_cloud_bigtable_data_v2_models_ChangeStreamMutation_getEntries__)()) {
            ModType modType = getModType(entry);
    
            Mod mod = null;
            switch (modType) {
              case SET_CELL:
                mod = new Mod(sourceInfo, input, ([SetCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html)) entry);
                break;
              case DELETE_CELLS:
                mod = new Mod(sourceInfo, input, ([DeleteCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteCells.html)) entry);
                break;
              case DELETE_FAMILY:
                mod = new Mod(sourceInfo, input, ([DeleteFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteFamily.html)) entry);
                break;
              default:
              case UNKNOWN:
                throw new UnsupportedEntryException(
                    "Cloud Bigtable change stream entry of type "
                        + entry.getClass().getName()
                        + " is not supported. The entry was put into a dead letter queue directory. "
                        + "Please update your Dataflow template with the latest template version");
            }
    
            [TableRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Table.TableRow.html) tableRow = new [TableRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Table.TableRow.html)();
            if (bigQuery.setTableRowFields(mod, tableRow)) {
              receiver.output(tableRow);
            }
          }
        }
    
        private ModType getModType([Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Entry.html) entry) {
          if (entry instanceof [SetCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html)) {
            return ModType.SET_CELL;
          } else if (entry instanceof [DeleteCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteCells.html)) {
            return ModType.DELETE_CELLS;
          } else if (entry instanceof [DeleteFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteFamily.html)) {
            return ModType.DELETE_FAMILY;
          }
          return ModType.UNKNOWN;
        }
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
