---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-change-streams-to-bigquery/
title: Spanner change streams to BigQuery template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:43:19.004366+00:00
---

# Spanner change streams to BigQuery template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-change-streams-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Spanner change streams to BigQuery template Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Spanner change streams connector doesn't support draining a job. To stop the pipeline, [cancel the job](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel) instead of draining it. Draining a job with the Spanner change streams connector can cause it to become stuck in a draining state. For more information, see [Draining](https://docs.cloud.google.com/spanner/docs/change-streams/use-dataflow#draining) in the Spanner documentation. 

With the Spanner change streams to BigQuery template, you stream data change records from Spanner and write them into BigQuery tables using the Dataflow Portable Runner. This integrates your Spanner data with BigQuery for real-time analytics and data warehousing.

## Template overview

Columns not watched aren't included in the BigQuery row. Any Spanner changes less than the Dataflow watermark are either successfully applied to the BigQuery tables or are stored in the dead-letter queue for retry. BigQuery rows are inserted out of order compared to the original Spanner commit timestamp ordering.

If the necessary BigQuery tables don't exist, the pipeline creates them. Otherwise, existing BigQuery tables are used. The schema of existing BigQuery tables must contain the corresponding tracked columns of the Spanner tables and any additional metadata columns that aren't ignored explicitly by the `ignoreFields` option. See the description of the metadata fields in the following list. Each new BigQuery row includes all columns watched by the change stream from its corresponding row in your Spanner table at the timestamp of the change record.

The following metadata fields are added to BigQuery tables. For more details about these fields, see [Data change records](https://docs.cloud.google.com/spanner/docs/change-streams/details#data-change-records) in "Change streams partitions, records, and queries."

  * `_metadata_spanner_mod_type`: The modification type (insert, update, or delete) of the Spanner transaction. Extracted from change stream data change record.
  * `_metadata_spanner_table_name`: The Spanner table name. This field is not the metadata table name of the connector.
  * `_metadata_spanner_commit_timestamp`: The Spanner [commit timestamp](https://docs.cloud.google.com/spanner/docs/commit-timestamp), which is the time when a change is committed. This value is extracted from the change stream data change record.
  * `_metadata_spanner_server_transaction_id`: A globally unique string that represents the Spanner [transaction](https://docs.cloud.google.com/spanner/docs/transactions) in which the change was committed. Only use this value in the context of processing change stream records. It isn't correlated with the transaction ID in Spanner's API. This value is extracted from the change stream data change record.
  * `_metadata_spanner_record_sequence`: The sequence number for the record within the Spanner transaction. Sequence numbers are always unique and monotonically increasing, but not necessarily contiguous, within a transaction. This value is extracted from the change stream data change record.
  * `_metadata_spanner_is_last_record_in_transaction_in_partition`: Indicates whether the record is the last record for a Spanner transaction in the current partition. This value is extracted from the change stream data change record.
  * `_metadata_spanner_number_of_records_in_transaction`: The number of data change records that are part of the Spanner transaction across all change stream partitions. This value is extracted from the change stream data change record.
  * `_metadata_spanner_number_of_partitions_in_transaction`: The number of [partitions](https://docs.cloud.google.com/spanner/docs/transactions#partitioned_dml_transactions) that return data change records for the Spanner transaction. This value is extracted from the change stream data change record.
  * `_metadata_big_query_commit_timestamp`: The commit timestamp when the row is inserted into BigQuery. If `useStorageWriteApi` is `true`, this column is not automatically created in the changelog table by the pipeline. In that case, you must manually add this column in the changelog table and set `CURRENT_TIMESTAMP` as its default value if needed.



When using this template, be aware of the following details:

  * You can use this template to propagate new columns on existing tables or new tables from Spanner to BigQuery. For more information, see Handle adding tracking tables or columns.
  * For `OLD_AND_NEW_VALUES` and `NEW_VALUES` value capture types, when the data change record contains an UPDATE change, the template needs to do a stale read to Spanner at the commit timestamp of the data change record to retrieve the unchanged but watched columns. Make sure to configure your database 'version_retention_period' properly for the stale read. For the `NEW_ROW` value capture type, the template is more efficient, because the data change record captures the full new row including columns that are not updated in UPDATE requests, and the template doesn't need to do a stale read.
  * To minimize network latency and network transport costs, run the Dataflow job from the same region as your Spanner instance or BigQuery tables. If you use sources, sinks, staging file locations, or temporary file locations that are located outside of your job's region, your data might be sent across regions. For more information, see [ Dataflow regions](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints).
  * This template supports all valid Spanner data types. If the BigQuery type is more precise than the Spanner type, precision loss might occur during the transformation. Specifically: 
    * For Spanner JSON type, the order of the members of an object is lexicographically ordered, but there is no such guarantee for BigQuery JSON type.
    * Spanner supports nanoseconds TIMESTAMP type, but BigQuery only supports microseconds TIMESTAMP type.



Learn more about [change streams](https://docs.cloud.google.com/spanner/docs/change-streams), [how to build change streams Dataflow pipelines](https://docs.cloud.google.com/spanner/docs/change-streams/use-dataflow), and [best practices](https://docs.cloud.google.com/spanner/docs/change-streams/use-dataflow#best_practices).

## Pipeline requirements

  * The Spanner instance must exist prior to running the pipeline.
  * The Spanner database must exist prior to running the pipeline.
  * The Spanner metadata instance must exist prior to running the pipeline.
  * The Spanner metadata database must exist prior to running the pipeline.
  * The Spanner change stream must exist prior to running the pipeline.
    * Only change streams that watch tables under the default schema are supported.
    * Change streams that watch tables under other schemas throw a [table not found error](https://github.com/GoogleCloudPlatform/DataflowTemplates/issues/2622). 
  * The BigQuery dataset must exist prior to running the pipeline.



## Handle adding tracking tables or columns

This section describes best practices for handling adding tracking Spanner tables and columns while the pipeline is running. The oldest supported template version for this feature is `2024-09-19-00_RC00`.

  * Before you add a new column to a Spanner change stream scope, first add the column to the BigQuery changelog table. The added column must have a matching data type and be `NULLABLE`. Wait at least 10 minutes before you continue to create the new column or table in Spanner. Writing into the new column without waiting might result in an unprocessed record with an [invalid error code](https://docs.cloud.google.com/bigquery/docs/error-messages) in your dead-letter queue.

For `NEW_ROW` or `NEW_ROW_AND_OLD_VALUES` value capture types, adding a new column with a default value during a running pipeline is supported by first adding the column to the BigQuery table and then adding it to the Spanner table.

For `NEW_VALUES` or `OLD_AND_NEW_VALUES`, adding a new column with a default value to a running pipeline might result in data loss. To avoid data loss, you must perform a manual export and import of your data using the following process:

    1. Stop the Dataflow pipeline.
    2. Add the column to the BigQuery table.
    3. Add the column with a default value in Spanner.
    4. Wait for the Spanner schema change and backfill to complete.
    5. Export the Spanner table data at a timestamp after the backfill is complete.
    6. Import the data into the BigQuery table, ensuring you handle the new column correctly.
    7. Start the Dataflow pipeline from the same timestamp used for the export.
**Note:** When you add a new column with a default value to an existing Spanner table, Spanner performs a backfill operation to populate all existing rows with this default value. This operation can take time depending on the size of your table. You can monitor the progress of the schema change, including the backfill, by querying the [`information_schema.COLUMNS`](https://docs.cloud.google.com/spanner/docs/information-schema) view in Spanner. The backfill is complete when the `SPANNER_STATE` of the new column is `COMMITTED`.
  * To add a new table, first add the table in the Spanner database. The table is automatically created in BigQuery when the pipeline receives a record for the new table. 
  * After you add the new columns or tables in the Spanner database, make sure to [alter your change stream](https://docs.cloud.google.com/spanner/docs/change-streams/manage#modify-table-columns) to track the new columns or tables that you want if they aren't tracked implicitly already.
  * The template doesn't drop tables or columns from BigQuery. If a column is dropped from the Spanner table, then null values are populated to the BigQuery changelog columns for records generated after the columns are dropped from the Spanner table, unless you manually drop the column from BigQuery.
  * The template doesn't support column type updates. Although Spanner supports changing a `STRING` column to a `BYTES` column or a `BYTES` column to a `STRING` column, you can't modify an existing column's data type or use the same column name with different data types in BigQuery. If you drop and recreate a column with the same name but a different type in Spanner, the data might be written into the existing BigQuery column, but the type is unchanged.
  * This template doesn't support column mode updates. Metadata columns replicated into BigQuery are set to the `REQUIRED` mode. All other columns replicated into BigQuery are set to `NULLABLE`, regardless of whether they are defined as `NOT NULL` in the Spanner table. You can't update the `NULLABLE` columns to the `REQUIRED` mode in BigQuery.
  * Changing a change stream's [value capture type ](https://docs.cloud.google.com/spanner/docs/change-streams#value-capture-type) is not supported for running pipelines.



## Template parameters

### Required parameters

  * **spannerInstanceId** : The Spanner instance to read change streams from.
  * **spannerDatabase** : The Spanner database to read change streams from.
  * **spannerMetadataInstanceId** : The Spanner instance to use for the change streams connector metadata table.
  * **spannerMetadataDatabase** : The Spanner database to use for the change streams connector metadata table.
  * **spannerChangeStreamName** : The name of the Spanner change stream to read from.
  * **bigQueryDataset** : The BigQuery dataset for change streams output.



### Optional parameters

  * **spannerProjectId** : The project to read change streams from. This value is also the project where the change streams connector metadata table is created. The default value for this parameter is the project where the Dataflow pipeline is running.
  * **spannerDatabaseRole** : The Spanner database role to use when running the template. This parameter is required only when the IAM principal who is running the template is a fine-grained access control user. The database role must have the `SELECT` privilege on the change stream and the `EXECUTE` privilege on the change stream's read function. For more information, see Fine-grained access control for change streams (<https://cloud.google.com/spanner/docs/fgac-change-streams>).
  * **spannerMetadataTableName** : The Spanner change streams connector metadata table name to use. If not provided, a Spanner change streams connector metadata table is automatically created during the pipeline flow. You must provide this parameter when updating an existing pipeline. Otherwise, don't provide this parameter.
  * **rpcPriority** : The request priority for Spanner calls. The value must be one of the following values: `HIGH`, `MEDIUM`, or `LOW`. The default value is `HIGH`.
  * **spannerHost** : The Cloud Spanner endpoint to call in the template. Only used for testing. For example, `https://batch-spanner.googleapis.com`.
  * **startTimestamp** : The starting DateTime (<https://datatracker.ietf.org/doc/html/rfc3339>), inclusive, to use for reading change streams. Ex-2021-10-12T07:20:50.52Z. Defaults to the timestamp when the pipeline starts, that is, the current time.
  * **endTimestamp** : The ending DateTime (<https://datatracker.ietf.org/doc/html/rfc3339>), inclusive, to use for reading change streams.Ex-2021-10-12T07:20:50.52Z. Defaults to an infinite time in the future.
  * **bigQueryProjectId** : The BigQuery project. The default value is the project for the Dataflow job.
  * **bigQueryChangelogTableNameTemplate** : The template for the name of the BigQuery table that contains the changelog. Defaults to: {_metadata_spanner_table_name}_changelog.
  * **deadLetterQueueDirectory** : The path to store any unprocessed records. The default path is a directory under the Dataflow job's temp location. The default value is usually sufficient.
  * **dlqRetryMinutes** : The number of minutes between dead-letter queue retries. The default value is `10`.
  * **ignoreFields** : A comma-separated list of fields (case sensitive) to ignore. These fields might be fields of watched tables, or metadata fields added by the pipeline. Ignored fields aren't inserted into BigQuery. When you ignore the _metadata_spanner_table_name field, the bigQueryChangelogTableNameTemplate parameter is also ignored. Defaults to empty.
  * **disableDlqRetries** : Whether or not to disable retries for the DLQ. Defaults to: false.
  * **spannerChangeStreamTvfNameList** : Semicolon-separated list of Spanner Change Stream TVF names to query and union. Defaults to empty.
  * **spannerDirectedReadOptions** : Directed read options for Cloud Spanner Change Stream reads. The value must be a JSON string format of DirectedReadOptions (e.g. {"includeReplicas":{"replicaSelections":[{"location":"us-central1","type":"READ_ONLY"}]}}). For more information, see Directed reads (<https://docs.cloud.google.com/spanner/docs/directed-reads>). Defaults to empty.
  * **useStorageWriteApi** : If true, the pipeline uses the BigQuery Storage Write API (<https://cloud.google.com/bigquery/docs/write-api>). The default value is `false`. For more information, see Using the Storage Write API (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#storage-write-api>).
  * **useStorageWriteApiAtLeastOnce** : When using the Storage Write API, specifies the write semantics. To use at-least once semantics (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics>), set this parameter to `true`. To use exactly-once semantics, set the parameter to `false`. This parameter applies only when `useStorageWriteApi` is `true`. The default value is `false`.
  * **numStorageWriteApiStreams** : When using the Storage Write API, specifies the number of write streams. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter. Defaults to: 0.
  * **storageWriteApiTriggeringFrequencySec** : When using the Storage Write API, specifies the triggering frequency, in seconds. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Cloud Spanner change streams to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Spanner_Change_Streams_to_BigQuery \
        --region REGION_NAME \
        --parameters \
    spannerInstanceId=SPANNER_INSTANCE_ID,\
    spannerDatabase=SPANNER_DATABASE,\
    spannerMetadataInstanceId=SPANNER_METADATA_INSTANCE_ID,\
    spannerMetadataDatabase=SPANNER_METADATA_DATABASE,\
    spannerChangeStreamName=SPANNER_CHANGE_STREAM,\
    bigQueryDataset=BIGQUERY_DATASET

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `SPANNER_INSTANCE_ID`: Spanner instance ID
  * `SPANNER_DATABASE`: Spanner database
  * `SPANNER_METADATA_INSTANCE_ID`: Spanner metadata instance ID
  * `SPANNER_METADATA_DATABASE`: Spanner metadata database
  * `SPANNER_CHANGE_STREAM`: Spanner change stream
  * `BIGQUERY_DATASET`: The BigQuery dataset for change streams output



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "spannerInstanceId": "SPANNER_INSTANCE_ID",
              "spannerDatabase": "SPANNER_DATABASE",
              "spannerMetadataInstanceId": "SPANNER_METADATA_INSTANCE_ID",
              "spannerMetadataDatabase": "SPANNER_METADATA_DATABASE",
              "spannerChangeStreamName": "SPANNER_CHANGE_STREAM",
              "bigQueryDataset": "BIGQUERY_DATASET"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Spanner_Change_Streams_to_BigQuery",
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
  * `SPANNER_INSTANCE_ID`: Spanner instance ID
  * `SPANNER_DATABASE`: Spanner database
  * `SPANNER_METADATA_INSTANCE_ID`: Spanner metadata instance ID
  * `SPANNER_METADATA_DATABASE`: Spanner metadata database
  * `SPANNER_CHANGE_STREAM`: Spanner change stream
  * `BIGQUERY_DATASET`: The BigQuery dataset for change streams output



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
    package com.google.cloud.teleport.v2.templates.spannerchangestreamstobigquery;
    
    import com.google.api.services.bigquery.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).[TableRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Table.TableRow.html);
    import com.google.cloud.[Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html);
    import com.google.cloud.teleport.metadata.[Template](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.Template.html);
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.cdc.dlq.DeadLetterQueueManager;
    import com.google.cloud.teleport.v2.cdc.dlq.StringDeadLetterQueueSanitizer;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.SpannerChangeStreamsToBigQueryOptions;
    import com.google.cloud.teleport.v2.templates.spannerchangestreamstobigquery.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).Mod;
    import com.google.cloud.teleport.v2.templates.spannerchangestreamstobigquery.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).ModColumnType;
    import com.google.cloud.teleport.v2.templates.spannerchangestreamstobigquery.schemautils.BigQueryUtils;
    import com.google.cloud.teleport.v2.templates.spannerchangestreamstobigquery.schemautils.OptionsUtils;
    import com.google.cloud.teleport.v2.transforms.DLQWriteTransform;
    import com.google.cloud.teleport.v2.utils.BigQueryIOUtils;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.base.Strings;
    import com.google.common.collect.ImmutableSet;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    import java.util.Set;
    import java.util.stream.Collectors;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html);
    import org.apache.beam.sdk.[PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html);
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.[CreateDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.CreateDisposition.html);
    import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy;
    import org.apache.beam.sdk.io.gcp.bigquery.[WriteResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.WriteResult.html);
    import org.apache.beam.sdk.io.gcp.spanner.SpannerConfig;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerIO;
    import org.apache.beam.sdk.io.gcp.spanner.changestreams.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).DataChangeRecord;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.Flatten;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.Reshuffle;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionList;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    // TODO(haikuo-google): Add integration test.
    // TODO(haikuo-google): Add README.
    // TODO(haikuo-google): Add stackdriver metrics.
    // TODO(haikuo-google): Ideally side input should be used to store schema information and shared
    // accross DoFns, but since side input fix is not yet deployed at the moment, we read schema
    // information in the beginning of the DoFn as a work around. We should use side input instead when
    // it's available.
    // TODO(haikuo-google): Test the case where tables or columns are added while the pipeline is
    // running.
    /**
     * This pipeline ingests {@link DataChangeRecord} from Spanner change stream. The {@link
     * DataChangeRecord} is then broken into {@link Mod}, which converted into {@link TableRow} and
     * inserted into BigQuery table.
     */
    @Template(
        name = "Spanner_Change_Streams_to_BigQuery",
        category = TemplateCategory.STREAMING,
        displayName = "Cloud Spanner change streams to BigQuery",
        description = {
          "The Cloud Spanner change streams to BigQuery template is a streaming pipeline that streams"
              + " Cloud Spanner data change records and writes them into BigQuery tables using Dataflow"
              + " Runner V2.\n",
          "All change stream watched columns are included in each BigQuery table row, regardless of"
              + " whether they are modified by a Cloud Spanner transaction. Columns not watched are not"
              + " included in the BigQuery row. Any Cloud Spanner change less than the Dataflow"
              + " watermark are either successfully applied to the BigQuery tables or are stored in the"
              + " dead-letter queue for retry. BigQuery rows are inserted out of order compared to the"
              + " original Cloud Spanner commit timestamp ordering.\n",
          "If the necessary BigQuery tables don't exist, the pipeline creates them. Otherwise, existing"
              + " BigQuery tables are used. The schema of existing BigQuery tables must contain the"
              + " corresponding tracked columns of the Cloud Spanner tables and any additional metadata"
              + " columns that are not ignored explicitly by the ignoreFields option. See the"
              + " description of the metadata fields in the following list. Each new BigQuery row"
              + " includes all columns watched by the change stream from its corresponding row in your"
              + " Cloud Spanner table at the change record's timestamp.\n",
          "The following metadata fields are added to BigQuery tables. For more details about these"
              + " fields, see Data change records in \"Change streams partitions, records, and"
              + " queries.\"\n"
              + "- _metadata_spanner_mod_type: The modification type (insert, update, or delete) of the"
              + " Cloud Spanner transaction. Extracted from change stream data change record.\n"
              + "- _metadata_spanner_table_name: The Cloud Spanner table name. Note this field is not"
              + " the metadata table name of the connector.\n"
              + "- _metadata_spanner_commit_timestamp: The Spanner commit timestamp, which is the time"
              + " when a change is committed. Extracted from change stream data change record.\n"
              + "- _metadata_spanner_server_transaction_id: A globally unique string that represents"
              + " the Spanner transaction in which the change was committed. Only use this value in the"
              + " context of processing change stream records. It isn't correlated with the transaction"
              + " ID in Spanner's API. Extracted from change stream data change record.\n"
              + "- _metadata_spanner_record_sequence: The sequence number for the record within the"
              + " Spanner transaction. Sequence numbers are guaranteed to be unique and monotonically"
              + " increasing (but not necessarily contiguous) within a transaction. Extracted from"
              + " change stream data change record.\n"
              + "- _metadata_spanner_is_last_record_in_transaction_in_partition: Indicates whether the"
              + " record is the last record for a Spanner transaction in the current partition."
              + " Extracted from change stream data change record.\n"
              + "- _metadata_spanner_number_of_records_in_transaction: The number of data change"
              + " records that are part of the Spanner transaction across all change stream partitions."
              + " Extracted from change stream data change record.\n"
              + "- _metadata_spanner_number_of_partitions_in_transaction: The number of partitions that"
              + " return data change records for the Spanner transaction. Extracted from change stream"
              + " data change record.\n"
              + "- _metadata_big_query_commit_timestamp: The commit timestamp of when the row is"
              + " inserted into BigQuery.\n",
          "Notes:\n"
              + "- This template does not propagate schema changes from Cloud Spanner to BigQuery."
              + " Because performing a schema change in Cloud Spanner is likely going to break the"
              + " pipeline, you might need to recreate the pipeline after the schema change.\n"
              + "- For OLD_AND_NEW_VALUES and NEW_VALUES value capture types, when the data change"
              + " record contains an UPDATE change, the template needs to do a stale read to Cloud"
              + " Spanner at the commit timestamp of the data change record to retrieve the unchanged"
              + " but watched columns. Make sure to configure your database 'version_retention_period'"
              + " properly for the stale read. For the NEW_ROW value capture type, the template is more"
              + " efficient, because the data change record captures the full new row including columns"
              + " that are not updated in UPDATEs, and the template does not need to do a stale read.\n"
              + "- You can minimize network latency and network transport costs by running the Dataflow"
              + " job from the same region as your Cloud Spanner instance or BigQuery tables. If you"
              + " use sources, sinks, staging file locations, or temporary file locations that are"
              + " located outside of your job's region, your data might be sent across regions. See"
              + " more about Dataflow regional endpoints.\n"
              + "- This template supports all valid Cloud Spanner data types, but if the BigQuery type"
              + " is more precise than the Cloud Spanner type, precision loss might occur during the"
              + " transformation. Specifically:\n"
              + "  - For Cloud Spanner JSON type, the order of the members of an object is"
              + " lexicographically ordered, but there is no such guarantee for BigQuery JSON type.\n"
              + "  - Cloud Spanner supports nanoseconds TIMESTAMP type, BigQuery only supports"
              + " microseconds TIMESTAMP type.\n",
          "Learn more about <a href=\"https://cloud.google.com/spanner/docs/change-streams\">change"
              + " streams</a>, <a"
              + " href=\"https://cloud.google.com/spanner/docs/change-streams/use-dataflow\">how to"
              + " build change streams Dataflow pipelines</a>, and <a"
              + " href=\"https://cloud.google.com/spanner/docs/change-streams/use-dataflow#best_practices\">best"
              + " practices</a>."
        },
        optionsClass = SpannerChangeStreamsToBigQueryOptions.class,
        flexContainerName = "googlecloud-to-googlecloud",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-change-streams-to-bigquery",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The Cloud Spanner instance must exist prior to running the pipeline.",
          "The Cloud Spanner database must exist prior to running the pipeline.",
          "The Cloud Spanner metadata instance must exist prior to running the pipeline.",
          "The Cloud Spanner metadata database must exist prior to running the pipeline.",
          "The Cloud Spanner change stream must exist prior to running the pipeline.",
          "The BigQuery dataset must exist prior to running the pipeline."
        },
        streaming = true,
        supportsExactlyOnce = true,
        supportsAtLeastOnce = true)
    public final class SpannerChangeStreamsToBigQuery {
    
      /** String/String Coder for {@link FailsafeElement}. */
      public static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      private static final Logger LOG = LoggerFactory.getLogger(SpannerChangeStreamsToBigQuery.class);
    
      // Max number of deadletter queue retries.
      private static final int DLQ_MAX_RETRIES = 5;
    
      private static final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) USE_RUNNER_V2_EXPERIMENT = "use_runner_v2";
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) {
        UncaughtExceptionLogger.register();
    
        LOG.info("Starting to replicate change records from Spanner change streams to BigQuery");
    
        SpannerChangeStreamsToBigQueryOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(SpannerChangeStreamsToBigQueryOptions.class);
    
        run(options);
      }
    
      private static void validateOptions(SpannerChangeStreamsToBigQueryOptions options) {
        if (options.getDlqRetryMinutes() <= 0) {
          throw new IllegalArgumentException("dlqRetryMinutes must be positive.");
        }
        if (options
            .getBigQueryChangelogTableNameTemplate()
            .equals(BigQueryUtils.BQ_CHANGELOG_FIELD_NAME_TABLE_NAME)) {
          throw new IllegalArgumentException(
              [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html).format(
                  "bigQueryChangelogTableNameTemplate cannot be set to '{%s}'. This value is reserved"
                      + " for the Cloud Spanner table name.",
                  BigQueryUtils.BQ_CHANGELOG_FIELD_NAME_TABLE_NAME));
        }
    
        BigQueryIOUtils.validateBQStorageApiOptionsStreaming(options);
      }
    
      private static void setOptions(SpannerChangeStreamsToBigQueryOptions options) {
        options.setStreaming(true);
        options.setEnableStreamingEngine(true);
    
        // Add use_runner_v2 to the experiments option, since change streams connector is only supported
        // on Dataflow runner v2.
        List<String> experiments = options.getExperiments();
        if (experiments == null) {
          experiments = new ArrayList<>();
        }
        if (!experiments.contains(USE_RUNNER_V2_EXPERIMENT)) {
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
      public static [PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html) run(SpannerChangeStreamsToBigQueryOptions options) {
        setOptions(options);
        validateOptions(options);
    
        /**
         * Stages: 1) Read {@link DataChangeRecord} from change stream. 2) Create {@link
         * FailsafeElement} of {@link Mod} JSON and merge from: - {@link DataChangeRecord}. - GCS Dead
         * letter queue. 3) Convert {@link Mod} JSON into {@link TableRow} by reading from Spanner at
         * commit timestamp. 4) Append {@link TableRow} to BigQuery. 5) Write Failures from 2), 3) and
         * 4) to GCS dead letter queue.
         */
        [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html) pipeline = [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html).create(options);
        DeadLetterQueueManager dlqManager = buildDlqManager(options);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) spannerProjectId = OptionsUtils.getSpannerProjectId(options);
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) dlqDirectory = dlqManager.getRetryDlqDirectoryWithDateTime();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tempDlqDirectory = dlqManager.getRetryDlqDirectory() + "tmp/";
    
        /**
         * There are two types of errors that can occur in this pipeline:
         *
         * <p>1) Error originating from modJsonStringToTableRow. Errors here are either due to pk values
         * missing, a spanner table / column missing in the in-memory map, or some Spanner read error
         * happening in readSpannerRow. We already retry the Spanner read error inline 3 times. Th other
         * types of errors are more likely to be un-retriable.
         *
         * <p>2) Error originating from BigQueryIO.write. BigQuery storage write API already retries all
         * transient errors and outputs more permanent errors.
         *
         * <p>As a result, it is reasonable to write all errors happening in the pipeline directly into
         * the permanent DLQ, since most of the errors are likely to be non-transient.
         */
        if (options.getDisableDlqRetries()) {
          LOG.info(
              "Disabling retries for the DLQ, directly writing into severe DLQ: {}",
              dlqManager.getSevereDlqDirectoryWithDateTime());
          dlqDirectory = dlqManager.getSevereDlqDirectoryWithDateTime();
          tempDlqDirectory = dlqManager.getSevereDlqDirectory() + "tmp/";
        }
    
        // Retrieve and parse the startTimestamp and endTimestamp.
        [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html) startTimestamp =
            options.getStartTimestamp().isEmpty()
                ? [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[now](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_now__)()
                : [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[parseTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_parseTimestamp_java_lang_String_)(options.getStartTimestamp());
        [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html) endTimestamp =
            options.getEndTimestamp().isEmpty()
                ? [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).MAX_VALUE
                : [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[parseTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_parseTimestamp_java_lang_String_)(options.getEndTimestamp());
    
        SpannerConfig spannerConfig =
            SpannerConfig.create()
                .withProjectId(spannerProjectId)
                .withInstanceId(options.getSpannerInstanceId())
                .withDatabaseId(options.getSpannerDatabase())
                .withRpcPriority(options.getRpcPriority());
        if (!Strings.isNullOrEmpty(options.getSpannerHost())) {
          spannerConfig =
              spannerConfig.withHost(ValueProvider.StaticValueProvider.of(options.getSpannerHost()));
        }
        // Propagate database role for fine-grained access control on change stream.
        if (options.getSpannerDatabaseRole() != null) {
          spannerConfig =
              spannerConfig.withDatabaseRole(
                  ValueProvider.StaticValueProvider.of(options.getSpannerDatabaseRole()));
        }
    
        SpannerIO.ReadChangeStream readChangeStream =
            SpannerIO.[readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_)()
                .withSpannerConfig(spannerConfig)
                .withMetadataInstance(options.getSpannerMetadataInstanceId())
                .withMetadataDatabase(options.getSpannerMetadataDatabase())
                .withChangeStreamName(options.getSpannerChangeStreamName())
                .withInclusiveStartAt(startTimestamp)
                .withInclusiveEndAt(endTimestamp)
                .withRpcPriority(options.getRpcPriority())
                .withDirectedReadOptions(options.getSpannerDirectedReadOptions());
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) spannerMetadataTableName = options.getSpannerMetadataTableName();
        if (spannerMetadataTableName != null) {
          readChangeStream = [readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_).withMetadataTable(spannerMetadataTableName);
        }
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tvfNameListString = options.getSpannerChangeStreamTvfNameList();
        if (tvfNameListString != null && !tvfNameListString.isEmpty()) {
          List<String> tvfNameList =
              Arrays.stream(tvfNameListString.[split](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_split_com_google_cloud_firestore_pipeline_expressions_Expression_)(";"))
                  .filter(name -> !name.[trim](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_trim__)().isEmpty())
                  .collect(Collectors.toList());
          if (!tvfNameList.isEmpty()) {
            readChangeStream = [readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_).withTvfNameList(tvfNameList);
          }
        }
    
        PCollection<DataChangeRecord> dataChangeRecord =
            [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__)
                .apply("Read from Spanner Change Streams", readChangeStream)
                .apply("Reshuffle DataChangeRecord", Reshuffle.viaRandomKey());
    
        PCollection<FailsafeElement<String, String>> sourceFailsafeModJson =
            dataChangeRecord
                .apply("DataChangeRecord To Mod JSON", ParDo.of(new DataChangeRecordToModJsonFn()))
                .apply(
                    "Wrap Mod JSON In FailsafeElement",
                    ParDo.of(
                        new DoFn<String, FailsafeElement<String, String>>() {
                          @ProcessElement
                          public void process(
                              @Element String input,
                              OutputReceiver<FailsafeElement<String, String>> receiver) {
                            receiver.output(FailsafeElement.of(input, input));
                          }
                        }))
                .setCoder(FAILSAFE_ELEMENT_CODER);
    
        PCollectionTuple dlqModJson =
            dlqManager.getReconsumerDataTransform(
                [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).apply(dlqManager.dlqReconsumer(options.getDlqRetryMinutes())));
        PCollection<FailsafeElement<String, String>> retryableDlqFailsafeModJson =
            dlqModJson.get(DeadLetterQueueManager.RETRYABLE_ERRORS).setCoder(FAILSAFE_ELEMENT_CODER);
    
        PCollection<FailsafeElement<String, String>> failsafeModJson =
            PCollectionList.of(sourceFailsafeModJson)
                .and(retryableDlqFailsafeModJson)
                .apply("Merge Source And DLQ Mod JSON", Flatten.pCollections());
    
        ImmutableSet.Builder<String> ignoreFieldsBuilder = ImmutableSet.builder();
        for ([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) ignoreField : options.getIgnoreFields().[split](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_split_com_google_cloud_firestore_pipeline_expressions_Expression_)(",")) {
          ignoreFieldsBuilder.add(ignoreField);
        }
        ImmutableSet<String> ignoreFields = ignoreFieldsBuilder.build();
        FailsafeModJsonToTableRowTransformer.FailsafeModJsonToTableRowOptions
            failsafeModJsonToTableRowOptions =
                FailsafeModJsonToTableRowTransformer.FailsafeModJsonToTableRowOptions.builder()
                    .setSpannerConfig(spannerConfig)
                    .setSpannerChangeStream(options.getSpannerChangeStreamName())
                    .setIgnoreFields(ignoreFields)
                    .setCoder(FAILSAFE_ELEMENT_CODER)
                    .setUseStorageWriteApi(options.getUseStorageWriteApi())
                    .build();
        FailsafeModJsonToTableRowTransformer.FailsafeModJsonToTableRow failsafeModJsonToTableRow =
            new FailsafeModJsonToTableRowTransformer.FailsafeModJsonToTableRow(
                failsafeModJsonToTableRowOptions);
    
        PCollectionTuple tableRowTuple =
            failsafeModJson.apply("Mod JSON To TableRow", failsafeModJsonToTableRow);
        // If users pass in the full BigQuery dataset ID (projectId.datasetName), extract the dataset
        // name for the setBigQueryDataset parameter.
        List<String> results = OptionsUtils.processBigQueryProjectAndDataset(options);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigqueryProject = [results](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.spi.v1.DnsRpc.ListResult.html#com_google_cloud_dns_spi_v1_DnsRpc_ListResult_results__).get(0);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigqueryDataset = [results](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.spi.v1.DnsRpc.ListResult.html#com_google_cloud_dns_spi_v1_DnsRpc_ListResult_results__).get(1);
    
        BigQueryDynamicDestinations.BigQueryDynamicDestinationsOptions
            bigQueryDynamicDestinationsOptions =
                BigQueryDynamicDestinations.BigQueryDynamicDestinationsOptions.builder()
                    .setSpannerConfig(spannerConfig)
                    .setChangeStreamName(options.getSpannerChangeStreamName())
                    .setIgnoreFields(ignoreFields)
                    .setBigQueryProject(bigqueryProject)
                    .setBigQueryDataset(bigqueryDataset)
                    .setBigQueryTableTemplate(options.getBigQueryChangelogTableNameTemplate())
                    .setUseStorageWriteApi(options.getUseStorageWriteApi())
                    .build();
        [WriteResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.WriteResult.html) writeResult;
        if (!options.getUseStorageWriteApi()) {
          writeResult =
              tableRowTuple
                  .get(failsafeModJsonToTableRow.transformOut)
                  .apply(
                      "Write To BigQuery",
                      BigQueryIO.<TableRow>write()
                          .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(BigQueryDynamicDestinations.of(bigQueryDynamicDestinationsOptions))
                          .withFormatFunction(element -> removeIntermediateMetadataFields(element))
                          .withFormatRecordOnFailureFunction(element -> element)
                          .withCreateDisposition([CreateDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.CreateDisposition.html).CREATE_IF_NEEDED)
                          .withWriteDisposition(Write.WriteDisposition.WRITE_APPEND)
                          .withExtendedErrorInfo()
                          .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors()));
        } else {
          writeResult =
              tableRowTuple
                  .get(failsafeModJsonToTableRow.transformOut)
                  .apply(
                      "Write To BigQuery",
                      BigQueryIO.<TableRow>write()
                          .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(BigQueryDynamicDestinations.of(bigQueryDynamicDestinationsOptions))
                          .withFormatFunction(element -> removeIntermediateMetadataFields(element))
                          .withFormatRecordOnFailureFunction(element -> element)
                          .withCreateDisposition([CreateDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.CreateDisposition.html).CREATE_IF_NEEDED)
                          .withWriteDisposition(Write.WriteDisposition.WRITE_APPEND)
                          .ignoreUnknownValues()
                          .withAutoSchemaUpdate(true) // only supported when using STORAGE_WRITE_API or
                          // STORAGE_API_AT_LEAST_ONCE.
                          .withExtendedErrorInfo()
                          .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors()));
        }
    
        PCollection<String> transformDlqJson =
            tableRowTuple
                .get(failsafeModJsonToTableRow.transformDeadLetterOut)
                .apply(
                    "Failed Mod JSON During Table Row Transformation",
                    MapElements.via(new StringDeadLetterQueueSanitizer()));
    
        PCollection<String> bqWriteDlqJson =
            BigQueryIOUtils.writeResultToBigQueryInsertErrors(writeResult, options)
                .apply(
                    "Failed Mod JSON During BigQuery Writes",
                    MapElements.via(new BigQueryDeadLetterQueueSanitizer()));
    
        PCollectionList.of(transformDlqJson)
            // Generally BigQueryIO storage write retries transient errors, and only more
            // persistent errors make it into DLQ.
            .and(bqWriteDlqJson)
            .apply("Merge Failed Mod JSON From Transform And BigQuery", Flatten.pCollections())
            .apply(
                "Write Failed Mod JSON To DLQ",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqDirectory)
                    .withTmpDirectory(tempDlqDirectory)
                    .setIncludePaneInfo(true)
                    .build());
    
        PCollection<FailsafeElement<String, String>> nonRetryableDlqModJsonFailsafe =
            dlqModJson.get(DeadLetterQueueManager.PERMANENT_ERRORS).setCoder(FAILSAFE_ELEMENT_CODER);
    
        nonRetryableDlqModJsonFailsafe
            .apply(
                "Write Mod JSON With Non-retryable Error To DLQ",
                MapElements.via(new StringDeadLetterQueueSanitizer()))
            .setCoder(StringUtf8Coder.of())
            .apply(
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqManager.getSevereDlqDirectoryWithDateTime())
                    .withTmpDirectory(dlqManager.getSevereDlqDirectory() + "tmp/")
                    .setIncludePaneInfo(true)
                    .build());
    
        return [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).run();
      }
    
      private static DeadLetterQueueManager buildDlqManager(
          SpannerChangeStreamsToBigQueryOptions options) {
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tempLocation =
            options.as(DataflowPipelineOptions.class).getTempLocation().endsWith("/")
                ? options.as(DataflowPipelineOptions.class).getTempLocation()
                : options.as(DataflowPipelineOptions.class).getTempLocation() + "/";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) dlqDirectory =
            options.getDeadLetterQueueDirectory().isEmpty()
                ? tempLocation + "dlq/" + options.getJobName() + "/"
                : options.getDeadLetterQueueDirectory();
    
        LOG.info("Dead letter queue directory: {}", dlqDirectory);
        return DeadLetterQueueManager.create(dlqDirectory, DLQ_MAX_RETRIES);
      }
    
      /**
       * Remove the following intermediate metadata fields that are not user data from {@link TableRow}:
       * _metadata_error, _metadata_retry_count, _metadata_spanner_original_payload_json.
       */
      private static [TableRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Table.TableRow.html) removeIntermediateMetadataFields([TableRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Table.TableRow.html) tableRow) {
        [TableRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Table.TableRow.html) cleanTableRow = tableRow.clone();
        Set<String> rowKeys = tableRow.keySet();
        Set<String> metadataFields = BigQueryUtils.getBigQueryIntermediateMetadataFieldNames();
    
        for ([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) rowKey : rowKeys) {
          if (metadataFields.contains(rowKey)) {
            cleanTableRow.remove(rowKey);
          } else if (rowKeys.contains("_type_" + rowKey)) {
            cleanTableRow.remove("_type_" + rowKey);
          }
        }
    
        return cleanTableRow;
      }
    
      /**
       * DoFn that converts a {@link DataChangeRecord} to multiple {@link Mod} in serialized JSON
       * format.
       */
      static class DataChangeRecordToModJsonFn extends DoFn<DataChangeRecord, String> {
    
        @ProcessElement
        public void process(@Element DataChangeRecord input, OutputReceiver<String> receiver) {
          for (org.apache.beam.sdk.io.gcp.spanner.changestreams.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).Mod changeStreamsMod :
              input.getMods()) {
            Mod mod =
                new Mod(
                    changeStreamsMod.getKeysJson(),
                    changeStreamsMod.getNewValuesJson(),
                    input.getCommitTimestamp(),
                    input.getServerTransactionId(),
                    input.isLastRecordInTransactionInPartition(),
                    input.getRecordSequence(),
                    input.getTableName(),
                    input.getRowType().stream().[map](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_map_java_util_Map_java_lang_String_java_lang_Object__)(ModColumnType::new).collect(Collectors.toList()),
                    input.getModType(),
                    input.getValueCaptureType(),
                    input.getNumberOfRecordsInTransaction(),
                    input.getNumberOfPartitionsInTransaction());
    
            [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) modJsonString;
    
            try {
              modJsonString = [mod](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_mod_com_google_cloud_firestore_pipeline_expressions_Expression_com_google_cloud_firestore_pipeline_expressions_Expression_).[toJson](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.PostPolicyV4.PostPolicyV4Document.html#com_google_cloud_storage_PostPolicyV4_PostPolicyV4Document_toJson__)();
            } catch (IOException e) {
              // Ignore exception and print bad format.
              modJsonString = [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html).format("\"%s\"", input);
            }
            receiver.output(modJsonString);
          }
        }
      }
    }
    

## Production considerations

When running the Spanner Change Streams to BigQuery template in a production environment, consider the following best practices to help ensure reliability and prevent data loss:

### Worker provisioning and scaling

  * **Set`maxNumWorkers` adequately:** Insufficient Dataflow workers can cause the pipeline to fall behind in processing change stream data. This can lead to increased latency and, in some scenarios, potential data loss due to internal connector timeouts and race conditions. The maximum number of workers must be sufficient to handle your peak Spanner write throughput.
  * **Sizing guidance:** While the optimal number varies with workload, consult the Spanner change streams guide on [Sizing your Dataflow cluster](https://docs.cloud.google.com/spanner/docs/change-streams/use-dataflow#size_your_cluster). Monitor your pipeline's performance and adjust as needed. For example, some high-throughput workloads might require increasing `maxNumWorkers` significantly (for example, from 20 to 100 or more).
  * **Autoscaling tuning:** Dataflow 's default horizontal autoscaling is primarily CPU-driven. If your pipeline lags but CPU utilization isn't high, consider tuning autoscaling. Lowering the `worker_utilization_hint` parameter can make autoscaling more responsive to other bottlenecks. See [Tune horizontal autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling#utilization-hint) for details.



### Monitoring and alerting

  * **Output Data Freshness (System Lag):** This is the most critical metric to monitor for this template. A consistently increasing "Output Data Freshness" (`dataflow.googleapis.com/job/system_lag`) indicates the pipeline is not keeping up with incoming changes from Spanner .
  * **Configure Alerts:** Set up Cloud Monitoring alerts on the "Output Data Freshness" metric. Establish a baseline for your pipeline and configure thresholds based on your business requirements for data latency. Promptly investigate any alerts for sustained increases in this metric. For more information, see [Dataflow job metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf).



### Interpreting logs

  * **`SpannerException: DEADLINE_EXCEEDED`:** While the connector has retries, frequent `com.google.cloud.spanner.SpannerException: DEADLINE_EXCEEDED` messages in the Dataflow worker logs are a strong indicator that the workers are struggling to read data from Spanner change streams in a timely manner. This often signals that the pipeline is under-provisioned in terms of worker resources.



### Spanner change stream configuration

  * **Retention Period:** Ensure the `retention_period` for your Spanner change stream is set to a duration sufficient to handle potential Dataflow pipeline slowdowns or outages. The default is 7 days. Consider setting this to 3-7 days to provide a larger buffer for the pipeline to recover and process any backlog without data loss due to changes expiring from the stream.



By implementing these practices, you can improve the resilience and performance of your Spanner Change Streams to BigQuery Dataflow pipeline.

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
