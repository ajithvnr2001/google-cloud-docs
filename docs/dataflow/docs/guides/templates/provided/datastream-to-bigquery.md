---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/datastream-to-bigquery/
title: Datastream to BigQuery (Stream) template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:48.294903+00:00
---

# Datastream to BigQuery (Stream) template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/datastream-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Datastream to BigQuery (Stream) template Stay organized with collections  Save and categorize content based on your preferences. 

The Datastream to BigQuery template is a streaming pipeline that reads [Datastream](https://docs.cloud.google.com/datastream/docs) data and replicates it into BigQuery. The template reads data from Cloud Storage using Pub/Sub notifications and replicates it into a time partitioned BigQuery staging table. Following replication, the template executes a `MERGE` in BigQuery to upsert all change data capture (CDC) changes into a replica of the source table. Specify either the `gcsPubSubSubscription` parameter to read data from Pub/Sub notifications, OR provide the `inputFilePattern` parameter to directly read data from files in Cloud Storage.

The template handles creating and updating the BigQuery tables managed by the replication. When data definition language (DDL) is required, a callback to Datastream extracts the source table schema and translates it into BigQuery data types. Supported operations include the following: 

  * New tables are created as data is inserted.
  * New columns are added to BigQuery tables with null initial values.
  * Dropped columns are ignored in BigQuery and future values are null.
  * Renamed columns are added to BigQuery as new columns.
  * Type changes are not propagated to BigQuery.



It's recommended to run this pipeline using [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes), because the template performs de-duplication when it merges data from a temporary BigQuery table to the main BigQuery table. This step in the pipeline means there is no additional benefit to using exactly-once streaming mode.

## Pipeline requirements

  * A Datastream stream that is ready to or already replicating data.
  * [Cloud Storage Pub/Sub notifications](https://docs.cloud.google.com/storage/docs/reporting-changes) are enabled for the Datastream data.
  * BigQuery destination datasets are created and the Compute Engine Service Account has been granted administrator access to them.
  * A primary key is necessary in the source table for the destination replica table to be created.
  * A MySQL or Oracle source database. PostgreSQL and SQL Server databases are not supported.



## Template parameters

### Required parameters

  * **inputFileFormat** : The format of the output files produced by Datastream. Allowed values are `avro` and `json`. Defaults to `avro`.
  * **outputStagingDatasetTemplate** : The name of the dataset that contains staging tables. This parameter supports templates, for example `{_metadata_dataset}_log` or `my_dataset_log`. Normally, this parameter is a dataset name. Defaults to `{_metadata_dataset}`. Note: For MySQL sources, the database name is mapped to `{_metadata_schema}` instead of `{_metadata_dataset}`.
  * **outputDatasetTemplate** : The name of the dataset that contains the replica tables. This parameter supports templates, for example `{_metadata_dataset}` or `my_dataset`. Normally, this parameter is a dataset name. Defaults to `{_metadata_dataset}`. Note: For MySQL sources, the database name is mapped to `{_metadata_schema}` instead of `{_metadata_dataset}`.
  * **deadLetterQueueDirectory** : The path that Dataflow uses to write the dead-letter queue output. This path must not be in the same path as the Datastream file output. Defaults to `empty`.



### Optional parameters

  * **inputFilePattern** : The file location for Datastream file output in Cloud Storage, in the format `gs://<BUCKET_NAME>/<ROOT_PATH>/`.
  * **gcsPubSubSubscription** : The Pub/Sub subscription used by Cloud Storage to notify Dataflow of new files available for processing, in the format: `projects/<PROJECT_ID>/subscriptions/<SUBSCRIPTION_NAME>`.
  * **streamName** : The name or the template for the stream to poll for schema information. Defaults to: {_metadata_stream}. The default value is usually enough.
  * **rfcStartDateTime** : The starting DateTime to use to fetch data from Cloud Storage (<https://tools.ietf.org/html/rfc3339>). Defaults to: `1970-01-01T00:00:00.00Z`.
  * **fileReadConcurrency** : The number of concurrent DataStream files to read. Default is `10`.
  * **outputProjectId** : The ID of the Google Cloud project that contains the BigQuery datasets to output data into. The default for this parameter is the project where the Dataflow pipeline is running.
  * **outputStagingTableNameTemplate** : The template to use to name the staging tables. For example, `{_metadata_table}`. Defaults to `{_metadata_table}_log`.
  * **outputTableNameTemplate** : The template to use for the name of the replica tables, for example `{_metadata_table}`. Defaults to `{_metadata_table}`.
  * **ignoreFields** : Comma-separated fields to ignore in BigQuery. Defaults to: `_metadata_stream,_metadata_schema,_metadata_table,_metadata_source,_metadata_tx_id,_metadata_dlq_reconsumed,_metadata_primary_keys,_metadata_error,_metadata_retry_count`. For example, `_metadata_stream,_metadata_schema`.
  * **mergeFrequencyMinutes** : The number of minutes between merges for a given table. Defaults to `5`.
  * **dlqRetryMinutes** : The number of minutes between DLQ Retries. Defaults to `10`.
  * **dataStreamRootUrl** : The Datastream API root URL. Defaults to: <https://datastream.googleapis.com/>.
  * **applyMerge** : Whether to disable MERGE queries for the job. Defaults to `true`.
  * **mergeConcurrency** : The number of concurrent BigQuery MERGE queries. Only effective when applyMerge is set to true. Defaults to `30`.
  * **partitionRetentionDays** : The number of days to use for partition retention when running BigQuery merges. Defaults to `1`.
  * **useStorageWriteApiAtLeastOnce** : This parameter takes effect only if `Use BigQuery Storage Write API` is enabled. If `true`, at-least-once semantics are used for the Storage Write API. Otherwise, exactly-once semantics are used. Defaults to `false`.
  * **datastreamSourceType** : Override the source type detection for Datastream CDC data. When specified, this value will be used instead of deriving the source type from the read_method field. Valid values include 'mysql', 'postgresql', 'oracle', 'sqlserver', etc. This parameter is useful when the read_method field contains 'cdc' and the actual source type cannot be determined automatically.
  * **javascriptTextTransformGcsPath** : The Cloud Storage URI of the .js file that defines the JavaScript user-defined function (UDF) to use. For example, `gs://my-bucket/my-udfs/my_file.js`.
  * **javascriptTextTransformFunctionName** : The name of the JavaScript user-defined function (UDF) to use. For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see UDF Examples (<https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples>).
  * **javascriptTextTransformReloadIntervalMinutes** : Specifies how frequently to reload the UDF, in minutes. If the value is greater than 0, Dataflow periodically checks the UDF file in Cloud Storage, and reloads the UDF if the file is modified. This parameter allows you to update the UDF while the pipeline is running, without needing to restart the job. If the value is `0`, UDF reloading is disabled. The default value is `0`.
  * **pythonTextTransformGcsPath** : The Cloud Storage path pattern for the Python code containing your user-defined functions. For example, `gs://your-bucket/your-transforms/*.py`.
  * **pythonRuntimeVersion** : The runtime version to use for this Python UDF.
  * **pythonTextTransformFunctionName** : The name of the function to call from your JavaScript file. Use only letters, digits, and underscores. For example, `transform_udf1`.
  * **runtimeRetries** : The number of times a runtime will be retried before failing. Defaults to: 5.
  * **useStorageWriteApi** : If true, the pipeline uses the BigQuery Storage Write API (<https://cloud.google.com/bigquery/docs/write-api>). The default value is `false`. For more information, see Using the Storage Write API (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#storage-write-api>).
  * **numStorageWriteApiStreams** : When using the Storage Write API, specifies the number of write streams. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter. Defaults to: 0.
  * **storageWriteApiTriggeringFrequencySec** : When using the Storage Write API, specifies the triggering frequency, in seconds. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter.



## User-defined function

Optionally, you can extend this template by writing a user-defined function (UDF). The template calls the UDF for each input element. Element payloads are serialized as JSON strings. For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

### Function specification

The UDF has the following specification:

* **Input** : the CDC data, serialized as a JSON string.
* **Output** : a JSON string that matches the schema of the BigQuery destination table.

## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Datastream to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Optional: To switch from exactly-once processing to [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes), select **At Least Once**.
  7. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --enable-streaming-engine \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Cloud_Datastream_to_BigQuery \
        --parameters \
    inputFilePattern=GCS_FILE_PATH,\
    gcsPubSubSubscription=GCS_SUBSCRIPTION_NAME,\
    outputStagingDatasetTemplate=BIGQUERY_DATASET,\
    outputDatasetTemplate=BIGQUERY_DATASET,\
    outputStagingTableNameTemplate=BIGQUERY_TABLE,\
    outputTableNameTemplate=BIGQUERY_TABLE_log
      

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. `
  * `GCS_FILE_PATH`: the Cloud Storage path to Datastream data. For example: `gs://bucket/path/to/data/`
  * `GCS_SUBSCRIPTION_NAME`: the Pub/Sub subscription to read changed files from. For example: `projects/my-project-id/subscriptions/my-subscription-id`.
  * `BIGQUERY_DATASET`: your BigQuery dataset name.
  * `BIGQUERY_TABLE`: your BigQuery table template. For example, `{_metadata_schema}_{_metadata_table}_log`



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
    
              "inputFilePattern": "GCS_FILE_PATH",
              "gcsPubSubSubscription": "GCS_SUBSCRIPTION_NAME",
              "outputStagingDatasetTemplate": "BIGQUERY_DATASET",
              "outputDatasetTemplate": "BIGQUERY_DATASET",
              "outputStagingTableNameTemplate": "BIGQUERY_TABLE",
              "outputTableNameTemplate": "BIGQUERY_TABLE_log"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Cloud_Datastream_to_BigQuery",
       }
    }
      

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. `
  * `GCS_FILE_PATH`: the Cloud Storage path to Datastream data. For example: `gs://bucket/path/to/data/`
  * `GCS_SUBSCRIPTION_NAME`: the Pub/Sub subscription to read changed files from. For example: `projects/my-project-id/subscriptions/my-subscription-id`.
  * `BIGQUERY_DATASET`: your BigQuery dataset name.
  * `BIGQUERY_TABLE`: your BigQuery table template. For example, `{_metadata_schema}_{_metadata_table}_log`



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2020 Google LLC
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
    
    import static com.google.cloud.teleport.v2.transforms.StatefulRowCleaner.RowCleanerDeadLetterQueueSanitizer;
    
    import com.google.api.services.bigquery.model.TableRow;
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.metadata.TemplateParameter.TemplateEnumOption;
    import com.google.cloud.teleport.v2.cdc.dlq.DeadLetterQueueManager;
    import com.google.cloud.teleport.v2.cdc.dlq.StringDeadLetterQueueSanitizer;
    import com.google.cloud.teleport.v2.cdc.mappers.BigQueryDefaultSchemas;
    import com.google.cloud.teleport.v2.cdc.merge.BigQueryMerger;
    import com.google.cloud.teleport.v2.cdc.merge.MergeConfiguration;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.datastream.mappers.DataStreamMapper;
    import com.google.cloud.teleport.v2.datastream.mappers.MergeInfoMapper;
    import com.google.cloud.teleport.v2.datastream.sources.DataStreamIO;
    import com.google.cloud.teleport.v2.options.BigQueryStorageApiStreamingOptions;
    import com.google.cloud.teleport.v2.templates.DataStreamToBigQuery.Options;
    import com.google.cloud.teleport.v2.transforms.DLQWriteTransform;
    import com.google.cloud.teleport.v2.transforms.StatefulRowCleaner;
    import com.google.cloud.teleport.v2.transforms.StatefulRowCleaner.RowCleanerDeadLetterQueueSanitizer;
    import com.google.cloud.teleport.v2.transforms.UDFTextTransformer.InputUDFOptions;
    import com.google.cloud.teleport.v2.transforms.UDFTextTransformer.InputUDFToTableRow;
    import com.google.cloud.teleport.v2.utils.BigQueryIOUtils;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.annotations.VisibleForTesting;
    import com.google.common.base.Splitter;
    import java.util.EnumSet;
    import java.util.HashSet;
    import java.util.Set;
    import java.util.regex.Pattern;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.extensions.gcp.options.GcpOptions;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.[CreateDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.CreateDisposition.html);
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.[SchemaUpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.SchemaUpdateOption.html);
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.[WriteDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.WriteDisposition.html);
    import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy;
    import org.apache.beam.sdk.io.gcp.bigquery.TableDestination;
    import org.apache.beam.sdk.io.gcp.bigquery.WriteResult;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.Flatten;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.Reshuffle;
    import org.apache.beam.sdk.transforms.SerializableFunction;
    import org.apache.beam.sdk.transforms.SimpleFunction;
    import org.apache.beam.sdk.values.KV;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionList;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.TupleTag;
    import org.apache.beam.sdk.values.ValueInSingleWindow;
    import org.joda.[time](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryParameterValue.html#com_google_cloud_bigquery_QueryParameterValue_time_java_lang_String_).Duration;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * This pipeline ingests DataStream data from GCS. The data is then cleaned and validated against a
     * BigQuery Table. If new columns or tables appear, they are automatically added to BigQuery. The
     * data is then inserted into BigQuery staging tables and Merged into a final replica table.
     *
     * <p>NOTE: Future versions are planned to support: Pub/Sub, GCS, or Kafka as per DataStream
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/datastream-to-bigquery/README_Cloud_Datastream_to_BigQuery.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Cloud_Datastream_to_BigQuery",
        category = TemplateCategory.STREAMING,
        displayName = "Datastream to BigQuery",
        description = {
          "The Datastream to BigQuery template is a streaming pipeline that reads <a href=\"https://cloud.google.com/datastream/docs\">Datastream</a> data and replicates it into BigQuery. "
              + "The template reads data from Cloud Storage using Pub/Sub notifications and replicates it into a time partitioned BigQuery staging table. "
              + "Following replication, the template executes a MERGE in BigQuery to upsert all change data capture (CDC) changes into a replica of the source table.\n",
          "The template handles creating and updating the BigQuery tables managed by the replication. "
              + "When data definition language (DDL) is required, a callback to Datastream extracts the source table schema and translates it into BigQuery data types. Supported operations include the following:\n"
              + "- New tables are created as data is inserted.\n"
              + "- New columns are added to BigQuery tables with null initial values.\n"
              + "- Dropped columns are ignored in BigQuery and future values are null.\n"
              + "- Renamed columns are added to BigQuery as new columns.\n"
              + "- Type changes are not propagated to BigQuery."
        },
        optionsClass = Options.class,
        flexContainerName = "datastream-to-bigquery",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/datastream-to-bigquery",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "A Datastream stream that is ready to or already replicating data.",
          "<a href=\"https://cloud.google.com/storage/docs/reporting-changes\">Cloud Storage Pub/Sub notifications</a> are enabled for the Datastream data.",
          "BigQuery destination datasets are created and the Compute Engine Service Account has been granted admin access to them.",
          "A primary key is necessary in the source table for the destination replica table to be created.",
          "A MySQL, Oracle, PostgreSQL, or SQL Server source database."
        },
        streaming = true,
        supportsAtLeastOnce = true,
        supportsExactlyOnce = false)
    public class DataStreamToBigQuery {
    
      private static final Logger LOG = LoggerFactory.[getLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcResultSetLogger.html#com_google_cloud_bigquery_jdbc_BigQueryJdbcResultSetLogger_getLogger_java_lang_Class____)(DataStreamToBigQuery.class);
      private static final String AVRO_SUFFIX = "avro";
      private static final String JSON_SUFFIX = "json";
    
      /** The tag for the main output of the json transformation. */
      public static final TupleTag<TableRow> TRANSFORM_OUT = new TupleTag<TableRow>() {};
    
      /** String/String Coder for FailsafeElement. */
      public static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      /** The tag for the dead-letter output of the json to table row transform. */
      public static final TupleTag<FailsafeElement<String, String>> TRANSFORM_DEADLETTER_OUT =
          new TupleTag<FailsafeElement<String, String>>() {};
    
      /**
       * Options supported by the pipeline.
       *
       * <p>Inherits standard configuration options.
       */
      public interface Options
          extends PipelineOptions,
              StreamingOptions,
              InputUDFOptions,
              BigQueryStorageApiStreamingOptions {
    
        @TemplateParameter.GcsReadFile(
            order = 1,
            optional = true,
            groupName = "Source",
            description = "File location for Datastream file output in Cloud Storage.",
            helpText =
                "The file location for Datastream file output in Cloud Storage, in the format `gs://<BUCKET_NAME>/<ROOT_PATH>/`.")
        String getInputFilePattern();
    
        void setInputFilePattern(String value);
    
        @TemplateParameter.Enum(
            order = 2,
            enumOptions = {@TemplateEnumOption("avro"), @TemplateEnumOption("json")},
            description = "Datastream output file format (avro/json).",
            helpText =
                "The format of the output files produced by Datastream. Allowed values are `avro` and `json`. Defaults to `avro`.")
        @Default.String("avro")
        String getInputFileFormat();
    
        void setInputFileFormat(String value);
    
        @TemplateParameter.PubsubSubscription(
            order = 3,
            optional = true,
            description = "The Pub/Sub subscription on the Cloud Storage bucket.",
            helpText =
                "The Pub/Sub subscription used by Cloud Storage to notify Dataflow of new files available for processing, in the format: `projects/<PROJECT_ID>/subscriptions/<SUBSCRIPTION_NAME>`.")
        String getGcsPubSubSubscription();
    
        void setGcsPubSubSubscription(String value);
    
        @TemplateParameter.Text(
            order = 4,
            optional = true,
            description = "Name or template for the stream to poll for schema information.",
            helpText =
                "The name or the template for the stream to poll for schema information. Defaults to: {_metadata_stream}. The default value is usually enough.")
        String getStreamName();
    
        void setStreamName(String value);
    
        @TemplateParameter.DateTime(
            order = 5,
            optional = true,
            description =
                "The starting DateTime used to fetch from Cloud Storage "
                    + "(https://tools.ietf.org/html/rfc3339).",
            helpText =
                "The starting DateTime to use to fetch data from Cloud Storage (https://tools.ietf.org/html/rfc3339). Defaults to: `1970-01-01T00:00:00.00Z`.")
        @Default.String("1970-01-01T00:00:00.00Z")
        String getRfcStartDateTime();
    
        void setRfcStartDateTime(String value);
    
        @TemplateParameter.Integer(
            order = 6,
            optional = true,
            description = "File read concurrency",
            helpText = "The number of concurrent DataStream files to read. Default is `10`.")
        @Default.Integer(10)
        Integer getFileReadConcurrency();
    
        void setFileReadConcurrency(Integer value);
    
        @TemplateParameter.ProjectId(
            order = 7,
            optional = true,
            description = "Project Id for BigQuery datasets.",
            groupName = "Target",
            helpText =
                "The ID of the Google Cloud project that contains the BigQuery datasets to output data into. The default for this parameter is the project where the Dataflow pipeline is running.")
        String getOutputProjectId();
    
        void setOutputProjectId(String projectId);
    
        @TemplateParameter.Text(
            order = 8,
            groupName = "Target",
            description = "Name or template for the dataset to contain staging tables.",
            helpText =
                "The name of the dataset that contains staging tables. This parameter supports templates, for example `{_metadata_dataset}_log` or `my_dataset_log`. Normally, this parameter is a dataset name. Defaults to `{_metadata_dataset}`. Note: For MySQL sources, the database name is mapped to `{_metadata_schema}` instead of `{_metadata_dataset}`.")
        @Default.String("{_metadata_dataset}")
        String getOutputStagingDatasetTemplate();
    
        void setOutputStagingDatasetTemplate(String value);
    
        @TemplateParameter.Text(
            order = 9,
            optional = true,
            groupName = "Target",
            description = "Template for the name of staging tables.",
            helpText =
                "The template to use to name the staging tables. For example, `{_metadata_table}`. Defaults to `{_metadata_table}_log`.")
        @Default.String("{_metadata_table}_log")
        String getOutputStagingTableNameTemplate();
    
        void setOutputStagingTableNameTemplate(String value);
    
        @TemplateParameter.Text(
            order = 10,
            groupName = "Target",
            description = "Template for the dataset to contain replica tables.",
            helpText =
                "The name of the dataset that contains the replica tables. This parameter supports templates, for example `{_metadata_dataset}` or `my_dataset`. Normally, this parameter is a dataset name. Defaults to `{_metadata_dataset}`. Note: For MySQL sources, the database name is mapped to `{_metadata_schema}` instead of `{_metadata_dataset}`.")
        @Default.String("{_metadata_dataset}")
        String getOutputDatasetTemplate();
    
        void setOutputDatasetTemplate(String value);
    
        @TemplateParameter.Text(
            order = 11,
            groupName = "Target",
            optional = true,
            description = "Template for the name of replica tables.",
            helpText =
                "The template to use for the name of the replica tables, for example `{_metadata_table}`. Defaults to `{_metadata_table}`.")
        @Default.String("{_metadata_table}")
        String getOutputTableNameTemplate();
    
        void setOutputTableNameTemplate(String value);
    
        @TemplateParameter.Text(
            order = 12,
            optional = true,
            description = "Fields to be ignored",
            helpText =
                "Comma-separated fields to ignore in BigQuery. Defaults to: `_metadata_stream,_metadata_schema,_metadata_table,_metadata_source,_metadata_tx_id,_metadata_dlq_reconsumed,_metadata_primary_keys,_metadata_error,_metadata_retry_count`.",
            example = "_metadata_stream,_metadata_schema")
        @Default.String(
            "_metadata_stream,_metadata_schema,_metadata_table,_metadata_source,"
                + "_metadata_tx_id,_metadata_dlq_reconsumed,_metadata_primary_keys,"
                + "_metadata_error,_metadata_retry_count")
        String getIgnoreFields();
    
        void setIgnoreFields(String value);
    
        @TemplateParameter.Integer(
            order = 13,
            optional = true,
            description = "The number of minutes between merges for a given table",
            helpText = "The number of minutes between merges for a given table. Defaults to `5`.")
        @Default.Integer(5)
        Integer getMergeFrequencyMinutes();
    
        void setMergeFrequencyMinutes(Integer value);
    
        @TemplateParameter.Text(
            order = 14,
            description = "Dead letter queue directory.",
            helpText =
                "The path that Dataflow uses to write the dead-letter queue output. This path must not be in the same path as the Datastream file output. Defaults to `empty`.")
        @Default.String("")
        String getDeadLetterQueueDirectory();
    
        void setDeadLetterQueueDirectory(String value);
    
        @TemplateParameter.Integer(
            order = 15,
            optional = true,
            description = "The number of minutes between DLQ Retries.",
            helpText = "The number of minutes between DLQ Retries. Defaults to `10`.")
        @Default.Integer(10)
        Integer getDlqRetryMinutes();
    
        void setDlqRetryMinutes(Integer value);
    
        @TemplateParameter.Text(
            order = 16,
            optional = true,
            description = "Datastream API Root URL (only required for testing)",
            helpText = "The Datastream API root URL. Defaults to: https://datastream.googleapis.com/.")
        @Default.String("https://datastream.googleapis.com/")
        String getDataStreamRootUrl();
    
        void setDataStreamRootUrl(String value);
    
        @TemplateParameter.Boolean(
            order = 17,
            optional = true,
            description = "A switch to disable MERGE queries for the job.",
            helpText = "Whether to disable MERGE queries for the job. Defaults to `true`.")
        @Default.Boolean(true)
        Boolean getApplyMerge();
    
        void setApplyMerge(Boolean value);
    
        @TemplateParameter.Integer(
            order = 18,
            optional = true,
            parentName = "applyMerge",
            parentTriggerValues = {"true"},
            description = "Concurrent queries for merge.",
            helpText =
                "The number of concurrent BigQuery MERGE queries. Only effective when applyMerge is set to true. Defaults to `30`.")
        @Default.Integer(MergeConfiguration.DEFAULT_MERGE_CONCURRENCY)
        Integer getMergeConcurrency();
    
        void setMergeConcurrency(Integer value);
    
        @TemplateParameter.Integer(
            order = 19,
            optional = true,
            description = "Partition retention days.",
            helpText =
                "The number of days to use for partition retention when running BigQuery merges. Defaults to `1`.")
        @Default.Integer(MergeConfiguration.DEFAULT_PARTITION_RETENTION_DAYS)
        Integer getPartitionRetentionDays();
    
        void setPartitionRetentionDays(Integer value);
    
        @TemplateParameter.Boolean(
            order = 20,
            optional = true,
            parentName = "useStorageWriteApi",
            parentTriggerValues = {"true"},
            description = "Use at at-least-once semantics in BigQuery Storage Write API",
            helpText =
                "This parameter takes effect only if `Use BigQuery Storage Write API` is enabled. If `true`, at-least-once semantics are used for the Storage Write API. Otherwise, exactly-once semantics are used. Defaults to `false`.",
            hiddenUi = true)
        @Default.Boolean(false)
        @Override
        Boolean getUseStorageWriteApiAtLeastOnce();
    
        void setUseStorageWriteApiAtLeastOnce(Boolean value);
    
        @TemplateParameter.Text(
            order = 21,
            optional = true,
            description = "Datastream source type override",
            helpText =
                "Override the source type detection for Datastream CDC data. When specified, this value will be used instead of deriving the source type from the read_method field. Valid values include 'mysql', 'postgresql', 'oracle', 'sqlserver', etc. This parameter is useful when the read_method field contains 'cdc' and the actual source type cannot be determined automatically.")
        String getDatastreamSourceType();
    
        void setDatastreamSourceType(String value);
      }
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        [LOG](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryBaseResultSet.html#com_google_cloud_bigquery_jdbc_BigQueryBaseResultSet_LOG).info("Starting Input Files to BigQuery");
    
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
    
        options.setStreaming(true);
        options.setEnableStreamingEngine(true);
    
        validateOptions(options);
        run(options);
      }
    
      private static void validateOptions(Options options) {
        String outputDataset = options.getOutputDatasetTemplate();
        String outputStagingDs = options.getOutputStagingDatasetTemplate();
    
        String outputTable = options.getOutputTableNameTemplate();
        String outputStagingTb = options.getOutputStagingTableNameTemplate();
    
        if (outputDataset.equals(outputStagingDs) && outputTable.equals(outputStagingTb)) {
          throw new IllegalArgumentException(
              "Can not have equal templates for output tables and staging tables.");
        }
    
        String inputFileFormat = options.getInputFileFormat();
        if (!(inputFileFormat.equals(AVRO_SUFFIX) || inputFileFormat.equals(JSON_SUFFIX))) {
          throw new IllegalArgumentException(
              "Input file format must be one of: avro, json or left empty - found " + inputFileFormat);
        }
    
        BigQueryIOUtils.validateBQStorageApiOptionsStreaming(options);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      public static PipelineResult run(Options options) {
        /*
         * Stages:
         *   1) Ingest and Normalize Data to FailsafeElement with JSON Strings
         *   2) Write JSON Strings to TableRow Collection
         *       - Optionally apply a UDF
         *   3) BigQuery Output of TableRow Data
         *     a) Map New Columns & Write to Staging Tables
         *     b) Map New Columns & Merge Staging to Target Table
         *   4) Write Failures to GCS Dead Letter Queue
         */
    
        Pipeline pipeline = Pipeline.create(options);
        DeadLetterQueueManager dlqManager = buildDlqManager(options);
    
        String bigqueryProjectId = getBigQueryProjectId(options);
        String dlqDirectory = dlqManager.getRetryDlqDirectoryWithDateTime();
        String tempDlqDir = dlqManager.getRetryDlqDirectory() + "tmp/";
    
        InputUDFToTableRow<String> failsafeTableRowTransformer =
            new InputUDFToTableRow<String>(
                options.getJavascriptTextTransformGcsPath(),
                options.getJavascriptTextTransformFunctionName(),
                options.getJavascriptTextTransformReloadIntervalMinutes(),
                options.getPythonTextTransformGcsPath(),
                options.getPythonTextTransformFunctionName(),
                options.getRuntimeRetries(),
                FAILSAFE_ELEMENT_CODER);
    
        StatefulRowCleaner statefulCleaner = StatefulRowCleaner.of();
    
        /*
         * Stage 1: Ingest and Normalize Data to FailsafeElement with JSON Strings
         *   a) Read DataStream data from GCS into JSON String FailsafeElements (datastreamJsonRecords)
         *   b) Reconsume Dead Letter Queue data from GCS into JSON String FailsafeElements
         *     (dlqJsonRecords)
         *   c) Flatten DataStream and DLQ Streams (jsonRecords)
         */
        PCollection<FailsafeElement<String, String>> datastreamJsonRecords =
            pipeline.apply(
                new DataStreamIO(
                        options.getStreamName(),
                        options.getInputFilePattern(),
                        options.getInputFileFormat(),
                        options.getGcsPubSubSubscription(),
                        options.getRfcStartDateTime())
                    .withFileReadConcurrency(options.getFileReadConcurrency())
                    .withDatastreamSourceType(options.getDatastreamSourceType()));
    
        // Elements sent to the Dead Letter Queue are to be reconsumed.
        // A DLQManager is to be created using PipelineOptions, and it is in charge
        // of building pieces of the DLQ.
        PCollection<FailsafeElement<String, String>> dlqJsonRecords =
            pipeline
                .apply("DLQ Consumer/reader", dlqManager.dlqReconsumer(options.getDlqRetryMinutes()))
                .apply(
                    "DLQ Consumer/cleaner",
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
    
        PCollection<FailsafeElement<String, String>> jsonRecords =
            PCollectionList.of(datastreamJsonRecords)
                .and(dlqJsonRecords)
                .apply("Merge Datastream & DLQ", Flatten.pCollections());
    
        /*
         * Stage 2: Write JSON Strings to TableRow PCollectionTuple
         *   a) Optionally apply a Javascript or Python UDF
         *   b) Convert JSON String FailsafeElements to TableRow's (tableRowRecords)
         */
        PCollectionTuple tableRowRecords =
            jsonRecords.apply("UDF to TableRow/udf", failsafeTableRowTransformer);
    
        PCollectionTuple cleanedRows =
            tableRowRecords
                .get(failsafeTableRowTransformer.transformOut)
                .apply("UDF to TableRow/Oracle Cleaner", statefulCleaner);
    
        PCollection<TableRow> shuffledTableRows =
            cleanedRows
                .get(statefulCleaner.successTag)
                .apply(
                    "UDF to TableRow/ReShuffle",
                    Reshuffle.<TableRow>viaRandomKey().withNumBuckets(100));
    
        /*
         * Stage 3: BigQuery Output of TableRow Data
         *   a) Map New Columns & Write to Staging Tables (writeResult)
         *   b) Map New Columns & Merge Staging to Target Table (null)
         *
         *   failsafe: writeResult.getFailedInsertsWithErr()
         */
        // TODO(beam 2.23): InsertRetryPolicy should be CDC compliant
        Set<String> fieldsToIgnore = getFieldsToIgnore(options.getIgnoreFields());
    
        PCollection<KV<TableId, TableRow>> mappedStagingRecords =
            shuffledTableRows.apply(
                "Map to Staging Tables",
                new DataStreamMapper(
                        options.as(GcpOptions.class),
                        options.getOutputProjectId(),
                        options.getOutputStagingDatasetTemplate(),
                        options.getOutputStagingTableNameTemplate())
                    .withDataStreamRootUrl(options.getDataStreamRootUrl())
                    .withDefaultSchema(BigQueryDefaultSchemas.DATASTREAM_METADATA_SCHEMA)
                    .withDayPartitioning(true)
                    .withIgnoreFields(fieldsToIgnore));
    
        WriteResult writeResult;
        if (options.getUseStorageWriteApi()) {
          // SerializableCoder(com.google.cloud.bigquery.TableId) is not a deterministic key coder.
          // So we have to convert tableid to a string.
          writeResult =
              mappedStagingRecords
                  .apply(
                      "TableId to String",
                      MapElements.via(
                          new SimpleFunction<KV<TableId, TableRow>, KV<String, TableRow>>() {
                            @Override
                            public KV<String, TableRow> apply(KV<TableId, TableRow> input) {
                              TableId tableId = input.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ConnectionProperty.html#com_google_cloud_bigquery_ConnectionProperty_getKey__)();
                              String projectId = tableId.getProject();
                              if (projectId == null) {
                                projectId = bigqueryProjectId;
                              }
                              return KV.of(
                                  String.format(
                                      "%s:%s.%s", projectId, tableId.getDataset(), tableId.getTable()),
                                  input.getValue());
                            }
                          }))
                  .apply("Write Successful Records", buildBigQueryStorageWrite(fieldsToIgnore));
        } else {
          writeResult =
              mappedStagingRecords.apply(
                  "Write Successful Records",
                  BigQueryIO.<KV<TableId, TableRow>>write()
                      .to(new BigQueryDynamicConverters().bigQueryDynamicDestination())
                      .withFormatFunction(
                          element -> removeTableRowFields(element.getValue(), fieldsToIgnore))
                      .withFormatRecordOnFailureFunction(element -> element.getValue())
                      .withoutValidation()
                      .ignoreInsertIds()
                      .ignoreUnknownValues()
                      .withCreateDisposition([CreateDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.CreateDisposition.html).CREATE_NEVER)
                      .withWriteDisposition([WriteDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.WriteDisposition.html).WRITE_APPEND)
                      .withExtendedErrorInfo() // takes effect only when Storage Write API is off
                      .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors()));
        }
    
        if (options.getApplyMerge()) {
          shuffledTableRows
              .apply(
                  "Map To Replica Tables",
                  new DataStreamMapper(
                          options.as(GcpOptions.class),
                          options.getOutputProjectId(),
                          options.getOutputDatasetTemplate(),
                          options.getOutputTableNameTemplate())
                      .withDataStreamRootUrl(options.getDataStreamRootUrl())
                      .withDefaultSchema(BigQueryDefaultSchemas.DATASTREAM_METADATA_SCHEMA)
                      .withIgnoreFields(fieldsToIgnore))
              .apply(
                  "BigQuery Merge/Build MergeInfo",
                  new MergeInfoMapper(
                      bigqueryProjectId,
                      options.getOutputStagingDatasetTemplate(),
                      options.getOutputStagingTableNameTemplate(),
                      options.getOutputDatasetTemplate(),
                      options.getOutputTableNameTemplate()))
              .apply(
                  "BigQuery Merge/Merge into Replica Tables",
                  BigQueryMerger.of(
                      MergeConfiguration.bigQueryConfiguration()
                          .withProjectId(bigqueryProjectId)
                          .withMergeWindowDuration(
                              Duration.standardMinutes(options.getMergeFrequencyMinutes()))
                          .withMergeConcurrency(options.getMergeConcurrency())
                          .withPartitionRetention(options.getPartitionRetentionDays())));
        }
    
        /*
         * Stage 4: Write Failures to GCS Dead Letter Queue
         */
        PCollection<String> udfDlqJson =
            PCollectionList.of(tableRowRecords.get(failsafeTableRowTransformer.udfDeadletterOut))
                .and(tableRowRecords.get(failsafeTableRowTransformer.transformDeadletterOut))
                .apply("Transform Failures/Flatten", Flatten.pCollections())
                .apply(
                    "Transform Failures/Sanitize",
                    MapElements.via(new StringDeadLetterQueueSanitizer()));
    
        PCollection<String> rowCleanerJson =
            cleanedRows
                .get(statefulCleaner.failureTag)
                .apply(
                    "Transform Failures/Oracle Cleaner Failures",
                    MapElements.via(new RowCleanerDeadLetterQueueSanitizer()));
    
        PCollection<String> bqWriteDlqJson =
            BigQueryIOUtils.writeResultToBigQueryInsertErrors(writeResult, options)
                .apply("BigQuery Failures", MapElements.via(new BigQueryDeadLetterQueueSanitizer()));
    
        PCollectionList.of(udfDlqJson)
            .and(rowCleanerJson)
            .and(bqWriteDlqJson)
            .apply("Write To DLQ/Flatten", Flatten.pCollections())
            .apply(
                "Write To DLQ/Writer",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqDirectory)
                    .withTmpDirectory(tempDlqDir)
                    .setIncludePaneInfo(true)
                    .build());
    
        // Execute the pipeline and return the result.
        return pipeline.run();
      }
    
      private static Set<String> getFieldsToIgnore(String fields) {
        return new HashSet<>(Splitter.on(Pattern.compile("\\s*,\\s*")).splitToList(fields));
      }
    
      @VisibleForTesting
      static BigQueryIO.Write<KV<String, TableRow>> buildBigQueryStorageWrite(
          Set<String> fieldsToIgnore) {
        return BigQueryIO.<KV<String, TableRow>>write()
            .to(
                (SerializableFunction<ValueInSingleWindow<KV<String, TableRow>>, TableDestination>)
                    value -> {
                      String tableSpec = value.getValue().getKey();
                      return new TableDestination(tableSpec, "Table for " + tableSpec);
                    })
            .withFormatFunction(element -> removeTableRowFields(element.getValue(), fieldsToIgnore))
            .withFormatRecordOnFailureFunction(element -> element.getValue())
            .withoutValidation()
            .ignoreInsertIds()
            .withSchemaUpdateOptions(
                EnumSet.of(
                    [SchemaUpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.SchemaUpdateOption.html).ALLOW_FIELD_ADDITION, [SchemaUpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.SchemaUpdateOption.html).ALLOW_FIELD_RELAXATION))
            .withCreateDisposition([CreateDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.CreateDisposition.html).CREATE_NEVER)
            .withWriteDisposition([WriteDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.WriteDisposition.html).WRITE_APPEND);
      }
    
      @VisibleForTesting
      static TableRow removeTableRowFields(TableRow tableRow, Set<String> ignoreFields) {
        [LOG](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryBaseResultSet.html#com_google_cloud_bigquery_jdbc_BigQueryBaseResultSet_LOG).debug("BigQuery Writes: {}", tableRow);
        TableRow cleanTableRow = tableRow.clone();
        Set<String> rowKeys = tableRow.keySet();
    
        for (String rowKey : rowKeys) {
          if (ignoreFields.contains(rowKey)) {
            cleanTableRow.remove(rowKey);
          }
        }
    
        return cleanTableRow;
      }
    
      private static String getBigQueryProjectId(Options options) {
        return options.getOutputProjectId() == null
            ? options.as(GcpOptions.class).getProject()
            : options.getOutputProjectId();
      }
    
      private static DeadLetterQueueManager buildDlqManager(Options options) {
        String tempLocation =
            options.as(DataflowPipelineOptions.class).getTempLocation().endsWith("/")
                ? options.as(DataflowPipelineOptions.class).getTempLocation()
                : options.as(DataflowPipelineOptions.class).getTempLocation() + "/";
    
        String dlqDirectory =
            options.getDeadLetterQueueDirectory().isEmpty()
                ? tempLocation + "dlq/"
                : options.getDeadLetterQueueDirectory();
    
        [LOG](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryBaseResultSet.html#com_google_cloud_bigquery_jdbc_BigQueryBaseResultSet_LOG).info("Dead-letter queue directory: {}", dlqDirectory);
        return DeadLetterQueueManager.create(dlqDirectory);
      }
    }
    

## What's next

  * Learn how to [ implement Datastream and Dataflow for analytics](https://docs.cloud.google.com/datastream/docs/implementing-datastream-dataflow-analytics).
  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
