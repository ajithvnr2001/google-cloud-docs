---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/datastream-to-cloud-spanner/
title: Datastream to Spanner template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:45.377160+00:00
---

# Datastream to Spanner template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/datastream-to-cloud-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Datastream to Spanner template Stay organized with collections  Save and categorize content based on your preferences. 

The Datastream to Spanner template is a streaming pipeline that reads [Datastream](https://docs.cloud.google.com/datastream/docs) events from a Cloud Storage bucket and writes them to a Spanner database. It is intended for data migration from Datastream sources to Spanner. Specify either the `gcsPubSubSubscription` parameter to read data from Pub/Sub notifications, OR provide the `inputFilePattern` parameter to directly read data from files in Cloud Storage. 

All tables required for migration must exist in the destination Spanner database prior to template execution. Hence schema migration from a source database to destination Spanner must be completed prior to data migration. Data can exist in the tables prior to migration. This template does not propagate Datastream schema changes to the Spanner database. 

Data consistency is guaranteed only at the end of migration when all data has been written to Spanner. To store ordering information for each record written to Spanner, this template creates an additional table (called a shadow table) for each table in the Spanner database. This is used to ensure consistency at the end of migration. The shadow tables are not deleted after migration and can be used for validation purposes at the end of migration. 

Any errors that occur during operation, such as schema mismatches, malformed JSON files, or errors resulting from executing transforms, are recorded in an error queue. The error queue is a Cloud Storage folder which stores all the Datastream events that had encountered errors along with the error reason in text format. The errors can be transient or permanent and are stored in appropriate Cloud Storage folders in the error queue. The transient errors are retried automatically while the permanent errors are not. In case of permanent errors, you have the option of making corrections to the change events and moving them to the retriable bucket while the template is running. 

## Pipeline requirements

  * A Datastream stream in **Running** or **Not started** state.
  * A Cloud Storage bucket where Datastream events are replicated.
  * A Spanner database with existing tables. These tables can be empty or contain data.



## Template parameters

### Required parameters

  * **instanceId** : The Spanner instance where the changes are replicated.
  * **databaseId** : The Spanner database where the changes are replicated.



### Optional parameters

  * **inputFilePattern** : The Cloud Storage file location that contains the Datastream files to replicate. Typically, this is the root path for a stream. Support for this feature has been disabled. Please use this feature only for retrying entries that land in severe DLQ.
  * **inputFileFormat** : The format of the output file produced by Datastream. For example `avro,json`. Defaults to `avro`.
  * **sessionFilePath** : Session file path in Cloud Storage that contains mapping information from HarbourBridge.
  * **projectId** : The Spanner project ID.
  * **spannerHost** : The Cloud Spanner endpoint to call in the template. For example, `https://batch-spanner.googleapis.com`. Defaults to: <https://batch-spanner.googleapis.com>.
  * **gcsPubSubSubscription** : The Pub/Sub subscription being used in a Cloud Storage notification policy. For the name, use the format `projects/<PROJECT_ID>/subscriptions/<SUBSCRIPTION_NAME>`.
  * **streamName** : The name or template for the stream to poll for schema information and source type.
  * **shadowTablePrefix** : The prefix used to name shadow tables. Default: `shadow_`.
  * **shouldCreateShadowTables** : This flag indicates whether shadow tables must be created in Cloud Spanner database. Defaults to: true.
  * **rfcStartDateTime** : The starting DateTime used to fetch from Cloud Storage (<https://tools.ietf.org/html/rfc3339>). Defaults to: 1970-01-01T00:00:00.00Z.
  * **fileReadConcurrency** : The number of concurrent DataStream files to read. Defaults to: 30.
  * **deadLetterQueueDirectory** : The file path used when storing the error queue output. The default file path is a directory under the Dataflow job's temp location.
  * **dlqRetryMinutes** : The number of minutes between dead letter queue retries. Defaults to `10`.
  * **dlqMaxRetryCount** : The max number of times temporary errors can be retried through DLQ. Defaults to `500`.
  * **dataStreamRootUrl** : Datastream API Root URL. Defaults to: <https://datastream.googleapis.com/>.
  * **datastreamSourceType** : This is the type of source database that Datastream connects to. Example - mysql/oracle. Need to be set when testing without an actual running Datastream.
  * **roundJsonDecimals** : This flag if set, rounds the decimal values in json columns to a number that can be stored without loss of precision. Defaults to: false.
  * **runMode** : This is the run mode type. Default is regular. Use `retryDLQ` mode to process exclusively severe error files concurrently with your live migration pipeline. Use `retryAllDLQ` mode only when the regular pipeline is stopped. This mode processes both retry and severe directories. Do NOT run `retryAllDLQ` concurrently with any active pipeline as it will cause conflicts.
  * **transformationContextFilePath** : Transformation context file path in cloud storage used to populate data used in transformations performed during migrations Eg: The shard id to db name to identify the db from which a row was migrated.
  * **directoryWatchDurationInMinutes** : The Duration for which the pipeline should keep polling a directory in GCS. Datastreamoutput files are arranged in a directory structure which depicts the timestamp of the event grouped by minutes. This parameter should be approximately equal tomaximum delay which could occur between event occurring in source database and the same event being written to GCS by Datastream. 99.9 percentile = 10 minutes. Defaults to: 10.
  * **spannerPriority** : The request priority for Cloud Spanner calls. The value must be one of: [`HIGH`,`MEDIUM`,`LOW`]. Defaults to `HIGH`.
  * **dlqGcsPubSubSubscription** : The Pub/Sub subscription being used in a Cloud Storage notification policy for DLQ retry directory when running in regular mode. For the name, use the format `projects/<PROJECT_ID>/subscriptions/<SUBSCRIPTION_NAME>`. When set, the deadLetterQueueDirectory and dlqRetryMinutes are ignored.
  * **transformationJarPath** : Custom JAR file location in Cloud Storage for the file that contains the custom transformation logic for processing records in forward migration. Defaults to empty.
  * **transformationClassName** : Fully qualified class name having the custom transformation logic. It is a mandatory field in case transformationJarPath is specified. Defaults to empty.
  * **transformationCustomParameters** : String containing any custom parameters to be passed to the custom transformation class. Defaults to empty.
  * **filteredEventsDirectory** : This is the file path to store the events filtered via custom transformation. Default is a directory under the Dataflow job's temp location. The default value is enough under most conditions.
  * **sourceConfigURL** : Cloud Storage path to a shard config file for sharded migrations. It expects a HOCON or JSON file. For a sample file, please refer to v2/datastream-to-spanner/src/test/resources/DatastreamToSpannerSingleDFShardedMigrationIT/sharding-config.conf in the repository. For example, `gs://my-bucket/my-shard-config.conf`. For example, `gs://my-bucket/my-shard-config.conf`.
  * **tableOverrides** : These are the table name overrides from source to spanner. They are written in thefollowing format: [{SourceTableName1, SpannerTableName1}, {SourceTableName2, SpannerTableName2}]This example shows mapping Singers table to Vocalists and Albums table to Records. For example, `[{Singers, Vocalists}, {Albums, Records}]`. Defaults to empty.
  * **columnOverrides** : These are the column name overrides from source to spanner. They are written in thefollowing format: [{SourceTableName1.SourceColumnName1, SourceTableName1.SpannerColumnName1}, {SourceTableName2.SourceColumnName1, SourceTableName2.SpannerColumnName1}]Note that the SourceTableName should remain the same in both the source and spanner pair. To override table names, use tableOverrides.The example shows mapping SingerName to TalentName and AlbumName to RecordName in Singers and Albums table respectively. For example, `[{Singers.SingerName, Singers.TalentName}, {Albums.AlbumName, Albums.RecordName}]`. Defaults to empty.
  * **schemaOverridesFilePath** : A file which specifies the table and the column name overrides from source to spanner. Defaults to empty.
  * **shadowTableSpannerInstanceId** : Optional separate instance for shadow tables. If not specified, shadow tables will be created in the main instance. If specified, ensure shadowTableSpannerDatabaseId is specified as well. Defaults to empty.
  * **shadowTableSpannerDatabaseId** : Optional separate database for shadow tables. If not specified, shadow tables will be created in the main database. If specified, ensure shadowTableSpannerInstanceId is specified as well. Defaults to empty.
  * **failureInjectionParameter** : Failure injection parameter. Only used for testing. Defaults to empty.
  * **skipDirectoryName** : Records skipped from migration are written to this directory. Default directory name is skip.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Cloud Datastream to Spanner** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Cloud_Datastream_to_Spanner \
        --parameters \
    inputFilePattern=GCS_FILE_PATH,\
    streamName=STREAM_NAME,\
    instanceId=CLOUDSPANNER_INSTANCE,\
    databaseId=CLOUDSPANNER_DATABASE,\
    deadLetterQueueDirectory=DLQ
      

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `GCS_FILE_PATH`: the Cloud Storage path that is used to store datastream events. For example: `gs://bucket/path/to/data/`
  * `CLOUDSPANNER_INSTANCE`: your Spanner instance.
  * `CLOUDSPANNER_DATABASE`: your Spanner database.
  * `DLQ`: the Cloud Storage path for the error queue directory.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Cloud_Datastream_to_Spanner",
          "parameters": {
              "inputFilePattern": "GCS_FILE_PATH",
              "streamName": "STREAM_NAME"
              "instanceId": "CLOUDSPANNER_INSTANCE"
              "databaseId": "CLOUDSPANNER_DATABASE"
              "deadLetterQueueDirectory": "DLQ"
          }
       }
    }
      

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `GCS_FILE_PATH`: the Cloud Storage path that is used to store datastream events. For example: `gs://bucket/path/to/data/`
  * `CLOUDSPANNER_INSTANCE`: your Spanner instance.
  * `CLOUDSPANNER_DATABASE`: your Spanner database.
  * `DLQ`: the Cloud Storage path for the error queue directory.



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
    
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.api.services.datastream.v1.model.SourceConfig;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.cdc.dlq.DeadLetterQueueManager;
    import com.google.cloud.teleport.v2.cdc.dlq.PubSubNotifiedDlqIO;
    import com.google.cloud.teleport.v2.cdc.dlq.StringDeadLetterQueueSanitizer;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.datastream.sources.DataStreamIO;
    import com.google.cloud.teleport.v2.datastream.utils.DataStreamClient;
    import com.google.cloud.teleport.v2.options.DataStreamToSpannerOptions;
    import com.google.cloud.teleport.v2.spanner.ddl.Ddl;
    import com.google.cloud.teleport.v2.spanner.migrations.constants.Constants;
    import com.google.cloud.teleport.v2.spanner.migrations.schema.ISchemaOverridesParser;
    import com.google.cloud.teleport.v2.spanner.migrations.schema.NoopSchemaOverridesParser;
    import com.google.cloud.teleport.v2.spanner.migrations.schema.Schema;
    import com.google.cloud.teleport.v2.spanner.migrations.schema.SchemaFileOverridesParser;
    import com.google.cloud.teleport.v2.spanner.migrations.schema.SchemaStringOverridesParser;
    import com.google.cloud.teleport.v2.spanner.migrations.shard.Shard;
    import com.google.cloud.teleport.v2.spanner.migrations.shard.ShardingContext;
    import com.google.cloud.teleport.v2.spanner.migrations.source.config.JdbcShardConfig;
    import com.google.cloud.teleport.v2.spanner.migrations.source.config.SourceConfigParser;
    import com.google.cloud.teleport.v2.spanner.migrations.source.config.SourceConnectionConfig;
    import com.google.cloud.teleport.v2.spanner.migrations.transformation.CustomTransformation;
    import com.google.cloud.teleport.v2.spanner.migrations.transformation.TransformationContext;
    import com.google.cloud.teleport.v2.spanner.migrations.utils.DataflowWorkerMachineTypeUtils;
    import com.google.cloud.teleport.v2.spanner.migrations.utils.SecretManagerAccessorImpl;
    import com.google.cloud.teleport.v2.spanner.migrations.utils.SessionFileReader;
    import com.google.cloud.teleport.v2.spanner.migrations.utils.TransformationContextReader;
    import com.google.cloud.teleport.v2.templates.constants.DatastreamToSpannerConstants;
    import com.google.cloud.teleport.v2.templates.source.DatastreamToSpannerSourceConnectorRegistry;
    import com.google.cloud.teleport.v2.templates.spanner.ProcessInformationSchema;
    import com.google.cloud.teleport.v2.templates.transform.ChangeEventTransformerDoFn;
    import com.google.cloud.teleport.v2.transforms.DLQWriteTransform;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.base.Strings;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    import java.util.Optional;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineWorkerPoolOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.extensions.gcp.options.GcpOptions;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerConfig;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerServiceFactoryImpl;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.Flatten;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.Reshuffle;
    import org.apache.beam.sdk.transforms.View;
    import org.apache.beam.sdk.transforms.windowing.FixedWindows;
    import org.apache.beam.sdk.transforms.windowing.Window;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionList;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.PCollectionView;
    import org.apache.beam.sdk.values.TupleTagList;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    import org.threeten.bp.Duration;
    
    /**
     * This pipeline ingests DataStream data from GCS as events. The events are written to Cloud
     * Spanner.
     *
     * <p>NOTE: Future versions will support: Pub/Sub, GCS, or Kafka as per DataStream
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/datastream-to-spanner/README_Cloud_Datastream_to_Spanner.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Cloud_Datastream_to_Spanner",
        category = TemplateCategory.STREAMING,
        displayName = "Datastream to Cloud Spanner",
        description = {
          "The Datastream to Cloud Spanner template is a streaming pipeline that reads <a"
              + " href=\"https://cloud.google.com/datastream/docs\">Datastream</a> events from a Cloud"
              + " Storage bucket and writes them to a Cloud Spanner database. It is intended for data"
              + " migration from Datastream sources to Cloud Spanner.\n",
          "All tables required for migration must exist in the destination Cloud Spanner database prior"
              + " to template execution. Hence schema migration from a source database to destination"
              + " Cloud Spanner must be completed prior to data migration. Data can exist in the tables"
              + " prior to migration. This template does not propagate Datastream schema changes to the"
              + " Cloud Spanner database.\n",
          "Data consistency is guaranteed only at the end of migration when all data has been written"
              + " to Cloud Spanner. To store ordering information for each record written to Cloud"
              + " Spanner, this template creates an additional table (called a shadow table) for each"
              + " table in the Cloud Spanner database. This is used to ensure consistency at the end of"
              + " migration. The shadow tables are not deleted after migration and can be used for"
              + " validation purposes at the end of migration.\n",
          "Any errors that occur during operation, such as schema mismatches, malformed JSON files, or"
              + " errors resulting from executing transforms, are recorded in an error queue. The error"
              + " queue is a Cloud Storage folder which stores all the Datastream events that had"
              + " encountered errors along with the error reason in text format. The errors can be"
              + " transient or permanent and are stored in appropriate Cloud Storage folders in the"
              + " error queue. The transient errors are retried automatically while the permanent"
              + " errors are not. In case of permanent errors, you can run the pipeline in one of"
              + " two retry modes depending on your pipeline state. Use `retryDLQ` mode when the"
              + " regular pipeline is concurrently running and pointing to the same DLQ directory."
              + " This mode consumes only severe errors while the regular mode will consume the retriable errors."
              + " Use `retryAllDLQ` mode when the regular pipeline is not running or is stopped."
              + " The `retryAllDLQ` mode consumes errors from both the retry and severe buckets. Do NOT run `retryAllDLQ` concurrently"
              + " with the regular pipeline as they will conflict."
        },
        optionsClass = DataStreamToSpannerOptions.class,
        flexContainerName = "datastream-to-spanner",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/datastream-to-cloud-spanner",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "A Datastream stream in Running or Not started state.",
          "A Cloud Storage bucket where Datastream events are replicated.",
          "A Cloud Spanner database with existing tables. These tables can be empty or contain data.",
        },
        streaming = true,
        supportsAtLeastOnce = true)
    public class DataStreamToSpanner {
      private static final Logger LOG = LoggerFactory.getLogger(DataStreamToSpanner.class);
      private static final String AVRO_SUFFIX = "avro";
      private static final String JSON_SUFFIX = "json";
    
      static void validateSourceType(DataStreamToSpannerOptions options) {
        boolean isRetryMode = Constants.RUN_MODE_RETRY_DLQ.equals(options.getRunMode());
        if (isRetryMode) {
          // retry mode does not read from Datastream
          return;
        }
        String sourceType = getSourceType(options);
        if (!DatastreamToSpannerSourceConnectorRegistry.getSupportedSourceTypes()
            .contains(sourceType)) {
          throw new IllegalArgumentException(
              "Unsupported source type found: "
                  + sourceType
                  + ". Specify one of the following source types: "
                  + DatastreamToSpannerSourceConnectorRegistry.getSupportedSourceTypes());
        }
        options.setDatastreamSourceType(sourceType);
      }
    
      static String getSourceType(DataStreamToSpannerOptions options) {
        if (options.getDatastreamSourceType() != null) {
          return options.getDatastreamSourceType();
        }
        if (options.getStreamName() == null) {
          throw new IllegalArgumentException("Stream name cannot be empty.");
        }
        GcpOptions gcpOptions = options.as(GcpOptions.class);
        DataStreamClient datastreamClient;
        SourceConfig sourceConfig;
        try {
          datastreamClient = new DataStreamClient(gcpOptions.getGcpCredential());
          sourceConfig = datastreamClient.getSourceConnectionProfile(options.getStreamName());
        } catch (IOException e) {
          LOG.error("IOException Occurred: DataStreamClient failed initialization.");
          throw new IllegalArgumentException("Unable to initialize DatastreamClient: " + e);
        }
        return getSourceTypeFromConfig(sourceConfig);
      }
    
      static String getSourceTypeFromConfig(SourceConfig sourceConfig) {
        try {
          return DatastreamToSpannerSourceConnectorRegistry.getSourceTypeFromConfig(sourceConfig);
        } catch (IllegalArgumentException e) {
          LOG.error("Source Connection Profile Type Not Supported", e);
          throw e;
        }
      }
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
        LOG.info("Starting DataStream to Cloud Spanner");
        DataStreamToSpannerOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(DataStreamToSpannerOptions.class);
        boolean isRetryDLQMode = Constants.RUN_MODE_RETRY_DLQ.equals(options.getRunMode());
        options.setStreaming(!isRetryDLQMode);
        validateSourceType(options);
        run(options);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      public static PipelineResult run(DataStreamToSpannerOptions options) {
        return buildPipeline(options).run();
      }
    
      static Pipeline buildPipeline(DataStreamToSpannerOptions options) {
        long startTime = System.currentTimeMillis();
        /*
         * Stages:
         *   1) Ingest and Normalize Data to FailsafeElement with JSON Strings
         *   2) Write JSON Strings to Cloud Spanner
         *   3) Write Failures to GCS Dead Letter Queue
         */
        Pipeline pipeline = Pipeline.create(options);
        String workerMachineType =
            pipeline.getOptions().as(DataflowPipelineWorkerPoolOptions.class).getWorkerMachineType();
        Optional<Integer> resourceHintsMinCpus =
            DataflowWorkerMachineTypeUtils.getMinCpuResourceHint(pipeline.getOptions());
        DataflowWorkerMachineTypeUtils.validateMachineSpecs(workerMachineType, 4, resourceHintsMinCpus);
        DeadLetterQueueManager dlqManager = buildDlqManager(options);
        // Ingest session file into schema object.
        Schema schema = SessionFileReader.read(options.getSessionFilePath());
        /*
         * Stage 1: Ingest/Normalize Data to FailsafeElement with JSON Strings and
         * read Cloud Spanner information schema.
         *   a) Prepare spanner config and process information schema
         *   b) Read DataStream data from GCS into JSON String FailsafeElements
         *   c) Reconsume Dead Letter Queue data from GCS into JSON String FailsafeElements
         *   d) Flatten DataStream and DLQ Streams
         */
    
        // Prepare Spanner config
        SpannerConfig spannerConfig =
            SpannerConfig.create()
                .withProjectId(ValueProvider.StaticValueProvider.of(options.getProjectId()))
                .withHost(ValueProvider.StaticValueProvider.of(options.getSpannerHost()))
                .withInstanceId(ValueProvider.StaticValueProvider.of(options.getInstanceId()))
                .withDatabaseId(ValueProvider.StaticValueProvider.of(options.getDatabaseId()))
                .withRpcPriority(ValueProvider.StaticValueProvider.of(options.getSpannerPriority()))
                .withCommitRetrySettings(
                    [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                        .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(Duration.ofMinutes(4))
                        .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(Duration.ofMinutes(0))
                        .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(1)
                        .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(Duration.ofMinutes(0))
                        .[setInitialRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRpcTimeout_org_threeten_bp_Duration_)(Duration.ofMinutes(4))
                        .[setRpcTimeoutMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRpcTimeoutMultiplier_double_)(1)
                        .[setMaxRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRpcTimeout_org_threeten_bp_Duration_)(Duration.ofMinutes(4))
                        .[setMaxAttempts](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxAttempts_int_)(1)
                        .build());
        SpannerConfig shadowTableSpannerConfig = getShadowTableSpannerConfig(options);
        /* Process information schema
         * 1) Read information schema from destination Cloud Spanner database
         * 2) Check if shadow tables are present and create if necessary
         * 3) Return new information schema
         */
        PCollectionTuple ddlTuple =
            pipeline.apply(
                "Process Information Schema",
                new ProcessInformationSchema(
                    spannerConfig,
                    shadowTableSpannerConfig,
                    options.getShouldCreateShadowTables(),
                    options.getShadowTablePrefix(),
                    options.getDatastreamSourceType()));
        PCollectionView<Ddl> ddlView =
            ddlTuple
                .get(ProcessInformationSchema.MAIN_DDL_TAG)
                .apply("Cloud Spanner Main DDL as view", View.asSingleton());
    
        PCollectionView<Ddl> shadowTableDdlView =
            ddlTuple
                .get(ProcessInformationSchema.SHADOW_TABLE_DDL_TAG)
                .apply("Cloud Spanner shadow tables DDL as view", View.asSingleton());
    
        PCollection<FailsafeElement<String, String>> jsonRecords = null;
        // Elements sent to the Dead Letter Queue are to be reconsumed.
        // A DLQManager is to be created using PipelineOptions, and it is in charge
        // of building pieces of the DLQ.
        PCollectionTuple reconsumedElements = null;
        boolean isRegularMode = Constants.RUN_MODE_REGULAR.equals(options.getRunMode());
        if (isRegularMode && (!Strings.isNullOrEmpty(options.getDlqGcsPubSubSubscription()))) {
          reconsumedElements =
              dlqManager.getReconsumerDataTransformForFiles(
                  pipeline.apply(
                      "Read retry from PubSub",
                      new PubSubNotifiedDlqIO(
                          options.getDlqGcsPubSubSubscription(),
                          // file paths to ignore when re-consuming for retry
                          new ArrayList<String>(
                              Arrays.asList(
                                  "/severe/",
                                  "/tmp_retry",
                                  "/tmp_severe/",
                                  ".temp",
                                  "/tmp_skip/",
                                  "/" + options.getSkipDirectoryName())))));
        } else {
          if (isRegularMode) {
            reconsumedElements =
                dlqManager.getReconsumerDataTransform(
                    pipeline.apply(dlqManager.dlqReconsumer(options.getDlqRetryMinutes())));
          } else { // retryDLQ or retryAllDLQ mode
            PCollection<String> oneShotRecords =
                pipeline.apply("Read severe from OneShot", dlqManager.dlqOneShotReconsumer(startTime));
    
            if (Constants.RUN_MODE_RETRY_DLQ.equals(options.getRunMode())) {
              reconsumedElements = dlqManager.getReconsumerDataTransform(oneShotRecords);
            } else {
              // retryAllDLQ mode: Drain both the severe (one-shot) and retry (continuous) buckets
              PCollection<String> continuousRecords =
                  pipeline.apply(
                      "Read retry from Continuous",
                      dlqManager.dlqReconsumer(options.getDlqRetryMinutes()));
    
              PCollection<String> allRecords =
                  PCollectionList.of(continuousRecords)
                      .and(oneShotRecords)
                      .apply("Flatten DLQ Records", Flatten.pCollections());
    
              reconsumedElements = dlqManager.getReconsumerDataTransform(allRecords);
            }
          }
        }
        PCollection<FailsafeElement<String, String>> dlqJsonRecords =
            reconsumedElements
                .get(DeadLetterQueueManager.RETRYABLE_ERRORS)
                .setCoder(FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of()));
        if (isRegularMode) {
          LOG.info("Regular Datastream flow");
          PCollection<FailsafeElement<String, String>> datastreamJsonRecords =
              pipeline.apply(
                  new DataStreamIO(
                          options.getStreamName(),
                          options.getInputFilePattern(),
                          options.getInputFileFormat(),
                          options.getGcsPubSubSubscription(),
                          options.getRfcStartDateTime())
                      .withFileReadConcurrency(options.getFileReadConcurrency())
                      .withoutDatastreamRecordsReshuffle()
                      .withDirectoryWatchDuration(
                          org.joda.time.Duration.standardMinutes(
                              options.getDirectoryWatchDurationInMinutes()))
                      .withDatastreamSourceType(options.getDatastreamSourceType()));
          int maxNumWorkers = options.getMaxNumWorkers() != 0 ? options.getMaxNumWorkers() : 1;
          jsonRecords =
              PCollectionList.of(datastreamJsonRecords)
                  .and(dlqJsonRecords)
                  .apply(Flatten.pCollections())
                  .apply(
                      "Reshuffle",
                      Reshuffle.<FailsafeElement<String, String>>viaRandomKey()
                          .withNumBuckets(
                              maxNumWorkers * DatastreamToSpannerConstants.MAX_DOFN_PER_WORKER));
        } else {
          LOG.info("DLQ retry flow");
          jsonRecords =
              PCollectionList.of(dlqJsonRecords)
                  .apply(Flatten.pCollections())
                  .apply("Reshuffle", Reshuffle.viaRandomKey());
        }
        /*
         * Stage 2: Transform records
         */
    
        // Ingest transformation context file into memory.
        TransformationContext transformationContext =
            TransformationContextReader.getTransformationContext(
                options.getTransformationContextFilePath());
    
        // Ingest sharding context file into memory.
        ShardingContext shardingContext = getShardingContext(options);
    
        CustomTransformation customTransformation =
            CustomTransformation.builder(
                    options.getTransformationJarPath(), options.getTransformationClassName())
                .setCustomParameters(options.getTransformationCustomParameters())
                .build();
    
        // Create the overrides mapping.
        ISchemaOverridesParser schemaOverridesParser = configureSchemaOverrides(options);
    
        ChangeEventTransformerDoFn changeEventTransformerDoFn =
            ChangeEventTransformerDoFn.create(
                schema,
                schemaOverridesParser,
                transformationContext,
                shardingContext,
                options.getDatastreamSourceType(),
                customTransformation,
                options.getRoundJsonDecimals(),
                ddlView,
                spannerConfig);
    
        PCollectionTuple transformedRecords =
            jsonRecords.apply(
                "Apply Transformation to events",
                ParDo.of(changeEventTransformerDoFn)
                    .withSideInputs(ddlView)
                    .withOutputTags(
                        DatastreamToSpannerConstants.TRANSFORMED_EVENT_TAG,
                        TupleTagList.of(
                            Arrays.asList(
                                DatastreamToSpannerConstants.FILTERED_EVENT_TAG,
                                DatastreamToSpannerConstants.PERMANENT_ERROR_TAG,
                                DatastreamToSpannerConstants.SKIPPED_TABLE_EVENT_TAG))));
    
        /*
         * Stage 3: Write filtered records to GCS
         */
        String tempLocation =
            options.as(DataflowPipelineOptions.class).getTempLocation().endsWith("/")
                ? options.as(DataflowPipelineOptions.class).getTempLocation()
                : options.as(DataflowPipelineOptions.class).getTempLocation() + "/";
        String filterEventsDirectory =
            options.getFilteredEventsDirectory().isEmpty()
                ? tempLocation + "filteredEvents/"
                : options.getFilteredEventsDirectory();
        LOG.info("Filtered events directory: {}", filterEventsDirectory);
        TextIO.Write filterEventsWrite;
        if (options.getRunner() != null && options.getRunner().getSimpleName().equals("DirectRunner")) {
          // DirectRunner does not support dynamic sharding for unbounded PCollections
          filterEventsWrite =
              TextIO.write()
                  .to(filterEventsDirectory)
                  .withSuffix(".json")
                  .withWindowedWrites()
                  .withNumShards(20);
        } else {
          // Cloud Dataflow natively supports dynamic sharding
          filterEventsWrite =
              TextIO.write().to(filterEventsDirectory).withSuffix(".json").withWindowedWrites();
        }
    
        transformedRecords
            .get(DatastreamToSpannerConstants.FILTERED_EVENT_TAG)
            .apply(Window.into(FixedWindows.of(org.joda.time.Duration.standardMinutes(1))))
            .apply("Write Filtered Events To GCS", filterEventsWrite);
    
        spannerConfig =
            SpannerServiceFactoryImpl.createSpannerService(
                spannerConfig, options.getFailureInjectionParameter());
        shadowTableSpannerConfig =
            SpannerServiceFactoryImpl.createSpannerService(
                shadowTableSpannerConfig, options.getFailureInjectionParameter());
    
        /*
         * Stage 4: Write transformed records to Cloud Spanner
         */
        SpannerTransactionWriter.Result spannerWriteResults =
            transformedRecords
                .get(DatastreamToSpannerConstants.TRANSFORMED_EVENT_TAG)
                .apply(
                    "Write events to Cloud Spanner",
                    new SpannerTransactionWriter(
                        spannerConfig,
                        shadowTableSpannerConfig,
                        ddlView,
                        shadowTableDdlView,
                        options.getShadowTablePrefix(),
                        options.getDatastreamSourceType(),
                        isRegularMode));
        /*
         * Stage 5: Write failures to GCS Dead Letter Queue
         * a) Retryable errors are written to retry GCS Dead letter queue
         * b) Severe errors are written to severe GCS Dead letter queue
         */
        // We will write only the original payload from the failsafe event to the DLQ.  We are doing
        // that in
        // StringDeadLetterQueueSanitizer.
        spannerWriteResults
            .retryableErrors()
            .apply(
                "DLQ: Write retryable Failures to GCS",
                MapElements.via(new StringDeadLetterQueueSanitizer()))
            .setCoder(StringUtf8Coder.of())
            .apply(
                "Write To DLQ",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqManager.getRetryDlqDirectoryWithDateTime())
                    .withTmpDirectory(options.getDeadLetterQueueDirectory() + "/tmp_retry/")
                    .setIncludePaneInfo(true)
                    .build());
        PCollection<FailsafeElement<String, String>> dlqErrorRecords =
            reconsumedElements
                .get(DeadLetterQueueManager.PERMANENT_ERRORS)
                .setCoder(FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of()));
        // TODO: Write errors from transformer and spanner writer into separate folders
        PCollection<FailsafeElement<String, String>> permanentErrors =
            PCollectionList.of(dlqErrorRecords)
                .and(spannerWriteResults.permanentErrors())
                .and(transformedRecords.get(DatastreamToSpannerConstants.PERMANENT_ERROR_TAG))
                .apply(Flatten.pCollections());
        // increment the metrics
        permanentErrors
            .apply("Update metrics", ParDo.of(new MetricUpdaterDoFn(isRegularMode)))
            .apply(
                "DLQ: Write Severe errors to GCS",
                MapElements.via(new StringDeadLetterQueueSanitizer()))
            .setCoder(StringUtf8Coder.of())
            .apply(
                "Write To DLQ",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqManager.getSevereDlqDirectoryWithDateTime())
                    .withTmpDirectory((options).getDeadLetterQueueDirectory() + "/tmp_severe/")
                    .setIncludePaneInfo(true)
                    .build());
    
        /*
         * Stage 6: Write skipped table events to the skip directory. These come from the transformer
         * (table dropped in the session file) and from the Spanner writer (table not present in
         * Spanner, e.g. when no session file is provided).
         */
        PCollectionList.of(transformedRecords.get(DatastreamToSpannerConstants.SKIPPED_TABLE_EVENT_TAG))
            .and(spannerWriteResults.skippedTableEvents())
            .apply("Flatten skipped table events", Flatten.pCollections())
            .setCoder(FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of()))
            .apply(
                "GCS: Write skipped tables to GCS directory",
                MapElements.via(new StringDeadLetterQueueSanitizer()))
            .setCoder(StringUtf8Coder.of())
            .apply(
                "Write skipped tables to GCS",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(
                        options.getDeadLetterQueueDirectory() + "/" + options.getSkipDirectoryName())
                    .withTmpDirectory(options.getDeadLetterQueueDirectory() + "/tmp_skip/")
                    .setIncludePaneInfo(true)
                    .build());
    
        return pipeline;
      }
    
      static ShardingContext getShardingContext(DataStreamToSpannerOptions options) {
        // Ingest sharding context file into memory.
        ShardingContext shardingContext = new ShardingContext();
        if (options.getSourceConfigURL() != null && !options.getSourceConfigURL().isEmpty()) {
          try {
            SourceConfigParser parser = new SourceConfigParser(new SecretManagerAccessorImpl());
            SourceConnectionConfig sourceConfig =
                parser.parseConfiguration(
                    getSourceType(options), options.getSourceConfigURL(), /* resolveSecrets= */ false);
    
            if (sourceConfig instanceof JdbcShardConfig jdbcShardConfig) {
              List<Shard> shards = jdbcShardConfig.getShardConfigs();
              Map<String, Map<String, String>> streamToDbAndShardMap = new HashMap<>();
              for (Shard shard : shards) {
                // TO-DO: add checks in SourceConfigParser to ensure not null fields.
                streamToDbAndShardMap
                    .computeIfAbsent(shard.getStreamId(), k -> new HashMap<>())
                    .put(shard.getDbName(), shard.getLogicalShardId());
              }
              shardingContext = new ShardingContext(streamToDbAndShardMap);
            }
          } catch (Exception e) {
            throw new RuntimeException("Failed to parse source config URL", e);
          }
        }
        return shardingContext;
      }
    
      static SpannerConfig getShadowTableSpannerConfig(DataStreamToSpannerOptions options) {
        // Validate shadow table Spanner config - both instance and database must be specified together
        String shadowTableSpannerInstanceId = options.getShadowTableSpannerInstanceId();
        String shadowTableSpannerDatabaseId = options.getShadowTableSpannerDatabaseId();
        LOG.info(
            "Input Shadow table db -  instance {} and database {}",
            shadowTableSpannerInstanceId,
            shadowTableSpannerDatabaseId);
    
        if ((Strings.isNullOrEmpty(shadowTableSpannerInstanceId)
                && !Strings.isNullOrEmpty(shadowTableSpannerDatabaseId))
            || (!Strings.isNullOrEmpty(shadowTableSpannerInstanceId)
                && Strings.isNullOrEmpty(shadowTableSpannerDatabaseId))) {
          throw new IllegalArgumentException(
              "Both shadowTableSpannerInstanceId and shadowTableSpannerDatabaseId must be specified together");
        }
        // If not specified, use main instance and main database values. The shadow table database
        // stores the shadow tables and by default, is the same as the main database for backward
        // compatibility.
        if (Strings.isNullOrEmpty(shadowTableSpannerInstanceId)
            && Strings.isNullOrEmpty(shadowTableSpannerDatabaseId)) {
          shadowTableSpannerInstanceId = options.getInstanceId();
          shadowTableSpannerDatabaseId = options.getDatabaseId();
          LOG.info(
              "Overwrote shadow table instance - {} and db- {}",
              shadowTableSpannerInstanceId,
              shadowTableSpannerDatabaseId);
        }
        return SpannerConfig.create()
            .withProjectId(ValueProvider.StaticValueProvider.of(options.getProjectId()))
            .withHost(ValueProvider.StaticValueProvider.of(options.getSpannerHost()))
            .withInstanceId(ValueProvider.StaticValueProvider.of(shadowTableSpannerInstanceId))
            .withDatabaseId(ValueProvider.StaticValueProvider.of(shadowTableSpannerDatabaseId))
            .withRpcPriority(ValueProvider.StaticValueProvider.of(options.getSpannerPriority()))
            .withCommitRetrySettings(
                [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                    .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(Duration.ofMinutes(4))
                    .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(Duration.ofMinutes(0))
                    .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(1)
                    .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(Duration.ofMinutes(0))
                    .[setInitialRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRpcTimeout_org_threeten_bp_Duration_)(Duration.ofMinutes(4))
                    .[setRpcTimeoutMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRpcTimeoutMultiplier_double_)(1)
                    .[setMaxRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRpcTimeout_org_threeten_bp_Duration_)(Duration.ofMinutes(4))
                    .[setMaxAttempts](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxAttempts_int_)(1)
                    .build());
      }
    
      static DeadLetterQueueManager buildDlqManager(DataStreamToSpannerOptions options) {
        String tempLocation =
            options.as(DataflowPipelineOptions.class).getTempLocation().endsWith("/")
                ? options.as(DataflowPipelineOptions.class).getTempLocation()
                : options.as(DataflowPipelineOptions.class).getTempLocation() + "/";
        String dlqDirectory =
            options.getDeadLetterQueueDirectory().isEmpty()
                ? tempLocation + "dlq/"
                : options.getDeadLetterQueueDirectory();
        LOG.info("Dead-letter queue directory: {}", dlqDirectory);
        options.setDeadLetterQueueDirectory(dlqDirectory);
        return DeadLetterQueueManager.create(dlqDirectory, options.getDlqMaxRetryCount(), true);
      }
    
      static ISchemaOverridesParser configureSchemaOverrides(DataStreamToSpannerOptions options) {
        // incorrect configuration
        if (!options.getSchemaOverridesFilePath().isEmpty()
            && (!options.getTableOverrides().isEmpty() || !options.getColumnOverrides().isEmpty())) {
          throw new IllegalArgumentException(
              "Only one of file based or string based overrides must be configured! Please correct the configuration and re-run the job");
        }
        // string based overrides
        if (!options.getTableOverrides().isEmpty() || !options.getColumnOverrides().isEmpty()) {
          Map<String, String> userOptionsOverrides = new HashMap<>();
          if (!options.getTableOverrides().isEmpty()) {
            userOptionsOverrides.put("tableOverrides", options.getTableOverrides());
          }
          if (!options.getColumnOverrides().isEmpty()) {
            userOptionsOverrides.put("columnOverrides", options.getColumnOverrides());
          }
          return new SchemaStringOverridesParser(userOptionsOverrides);
        }
        // file based overrides
        if (!options.getSchemaOverridesFilePath().isEmpty()) {
          return new SchemaFileOverridesParser(options.getSchemaOverridesFilePath());
        }
        // no overrides
        return new NoopSchemaOverridesParser();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
