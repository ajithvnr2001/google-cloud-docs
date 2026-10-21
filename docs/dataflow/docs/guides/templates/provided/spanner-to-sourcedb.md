---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/spanner-to-sourcedb/
title: Spanner Change Streams to Source Database template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:19.811779+00:00
---

# Spanner Change Streams to Source Database template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/spanner-to-sourcedb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Spanner Change Streams to Source Database template Stay organized with collections  Save and categorize content based on your preferences. 

Streaming pipeline. Reads data from Spanner Change Streams and writes them to a source.

**Note:** The Spanner change streams connector doesn't support draining a job. To stop the pipeline, [cancel the job](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel) instead of draining it. Draining a job with the Spanner change streams connector can cause it to become stuck in a draining state. For more information, see [Draining](https://docs.cloud.google.com/spanner/docs/change-streams/use-dataflow#draining) in the Spanner documentation. 

## Template parameters

Parameter | Description  
---|---  
`changeStreamName` | The name of the Spanner change stream that the pipeline reads from.  
`instanceId` | The name of the Spanner instance where the change stream is present.  
`databaseId` | The name of the Spanner database that the change stream monitors.  
`spannerProjectId` | The name of the Spanner project.  
`metadataInstance` | The instance to store the metadata used by the connector to control the consumption of the change stream API data.  
`metadataDatabase` | The database to store the metadata used by the connector to control the consumption of the change stream API data.  
`sourceShardsFilePath` | Path to a Cloud Storage file containing connection profile information for source shards.  
`startTimestamp` | Optional: The starting timestamp for reading changes. Defaults to empty.  
`endTimestamp` | Optional: The end timestamp for reading changes. If no timestamp provided, reads indefinitely. Defaults to empty.  
`shadowTablePrefix` | Optional: The prefix used to name shadow tables. Default: `shadow_`.  
`sessionFilePath` | Optional: Session path in Cloud Storage that contains mapping information from HarbourBridge.  
`filtrationMode` | Optional: Mode of filtration. Specifies how to drop certain records based on a criteria. Supported modes are: `none` (filter nothing), `forward_migration` (filter records written using the forward migration pipeline). Defaults to `forward_migration`.  
`shardingCustomJarPath` | Optional: Custom JAR file location in Cloud Storage that contains the customization logic for fetching the shard id. If you set this parameter, set the `shardingCustomJarPath` parameter. Defaults to empty.  
`shardingCustomClassName` | Optional: Fully qualified class name having the custom shard id implementation. If `shardingCustomJarPath` is specified, this parameter is required. Defaults to empty.  
`shardingCustomParameters` | Optional: String containing any custom parameters to be passed to the custom sharding class. Defaults to empty.  
`sourceDbTimezoneOffset` | Optional: The timezone offset from UTC for the source database. Example value: +10:00. Defaults to: `+00:00`.  
`dlqGcsPubSubSubscription` | Optional: The Pub/Sub subscription being used in a Cloud Storage notification policy for DLQ retry directory when running in regular mode. The name should be in the format of projects/<project-id>/subscriptions/<subscription-name>. When set, the deadLetterQueueDirectory and dlqRetryMinutes are ignored.  
`skipDirectoryName` | Optional: Records skipped from reverse replication are written to this directory. Default directory name is skip.  
`maxShardConnections` | Optional: The maximum number of connections that a given shard can accept. Defaults to: `10000`.  
`deadLetterQueueDirectory` | Optional: The path used when storing the error queue output. The default path is a directory under the Dataflow job's temp location.  
`dlqMaxRetryCount` | Optional: The maximum number of times that temporary errors can be retried through the dead-letter queue. Defaults to 500.  
`runMode` | Optional: The run mode type. Supported values: `regular`, `retryDLQ`. Default: `regular`. Specify `retryDLQ` is retry severe dead-letter queue records only.  
`dlqRetryMinutes` | Optional: The number of minutes between dead-letter queue retries. Defaults to 10.  
  
## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Spanner Change Streams to Source Database** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud CLI

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Spanner_to_SourceDb \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --parameters \
           changeStreamName=CHANGE_STREAM_NAME,\
           instanceId=INSTANCE_ID,\
           databaseId=DATABASE_ID,\
           spannerProjectId=SPANNER_PROJECT_ID,\
           metadataInstance=METADATA_INSTANCE,\
           metadataDatabase=METADATA_DATABASE,\
           sourceShardsFilePath=SOURCE_SHARDS_FILE_PATH,\

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `CHANGE_STREAM_NAME`: the Name of the change stream to read from
  * `INSTANCE_ID`: the Cloud Spanner Instance Id.
  * `DATABASE_ID`: the Cloud Spanner Database Id.
  * `SPANNER_PROJECT_ID`: the Cloud Spanner Project Id.
  * `METADATA_INSTANCE`: the Cloud Spanner Instance to store metadata when reading from changestreams
  * `METADATA_DATABASE`: the Cloud Spanner Database to store metadata when reading from changestreams
  * `SOURCE_SHARDS_FILE_PATH`: the Path to GCS file containing the Source shard details



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launchParameter": {
         "jobName": "JOB_NAME",
         "parameters": {
           "changeStreamName": "CHANGE_STREAM_NAME",
           "instanceId": "INSTANCE_ID",
           "databaseId": "DATABASE_ID",
           "spannerProjectId": "SPANNER_PROJECT_ID",
           "metadataInstance": "METADATA_INSTANCE",
           "metadataDatabase": "METADATA_DATABASE",
           "sourceShardsFilePath": "SOURCE_SHARDS_FILE_PATH",
         },
         "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Spanner_to_SourceDb",
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
  * `CHANGE_STREAM_NAME`: the Name of the change stream to read from
  * `INSTANCE_ID`: the Cloud Spanner Instance Id.
  * `DATABASE_ID`: the Cloud Spanner Database Id.
  * `SPANNER_PROJECT_ID`: the Cloud Spanner Project Id.
  * `METADATA_INSTANCE`: the Cloud Spanner Instance to store metadata when reading from changestreams
  * `METADATA_DATABASE`: the Cloud Spanner Database to store metadata when reading from changestreams
  * `SOURCE_SHARDS_FILE_PATH`: the Path to GCS file containing the Source shard details



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2024 Google LLC
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
    
    import static com.google.cloud.teleport.v2.spanner.migrations.constants.[Constants](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.Constants.html).RUN_MODE_REGULAR;
    import static com.google.cloud.teleport.v2.spanner.migrations.constants.[Constants](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.Constants.html).RUN_MODE_RETRY_DLQ;
    
    import com.google.cloud.[Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html);
    import com.google.cloud.teleport.metadata.[Template](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.Template.html);
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.cdc.dlq.DeadLetterQueueManager;
    import com.google.cloud.teleport.v2.cdc.dlq.PubSubNotifiedDlqIO;
    import com.google.cloud.teleport.v2.cdc.dlq.StringDeadLetterQueueSanitizer;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.CommonTemplateJvmInitializer;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.SpannerToSourceDbOptions;
    import com.google.cloud.teleport.v2.spanner.ddl.Ddl;
    import com.google.cloud.teleport.v2.spanner.migrations.[shard](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html#com_google_cloud_bigtable_data_v2_models_Query_shard_java_util_List_com_google_cloud_bigtable_data_v2_models_KeyOffset__).Shard;
    import com.google.cloud.teleport.v2.spanner.migrations.transformation.CustomTransformation;
    import com.google.cloud.teleport.v2.spanner.migrations.utils.DataflowWorkerMachineTypeUtils;
    import com.google.cloud.teleport.v2.spanner.sourceddl.SourceSchema;
    import com.google.cloud.teleport.v2.templates.changestream.TrimmedShardedDataChangeRecord;
    import com.google.cloud.teleport.v2.templates.constants.[Constants](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.Constants.html);
    import com.google.cloud.teleport.v2.templates.dbutils.processor.ISpToSrcSourceConnector;
    import com.google.cloud.teleport.v2.templates.dbutils.processor.SourceProcessorFactory;
    import com.google.cloud.teleport.v2.templates.transforms.AssignShardIdFn;
    import com.google.cloud.teleport.v2.templates.transforms.ConvertChangeStreamErrorRecordToFailsafeElementFn;
    import com.google.cloud.teleport.v2.templates.transforms.ConvertDlqRecordToTrimmedShardedDataChangeRecordFn;
    import com.google.cloud.teleport.v2.templates.transforms.FilterRecordsFn;
    import com.google.cloud.teleport.v2.templates.transforms.PreprocessRecordsFn;
    import com.google.cloud.teleport.v2.templates.transforms.SourceWriterTransform;
    import com.google.cloud.teleport.v2.templates.transforms.SpannerInformationSchemaProcessorTransform;
    import com.google.cloud.teleport.v2.templates.transforms.UpdateDlqMetricsFn;
    import com.google.cloud.teleport.v2.transforms.DLQWriteTransform;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.base.Strings;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    import java.util.Optional;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineDebugOptions;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineWorkerPoolOptions;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineWorkerPoolOptions.AutoscalingAlgorithmType;
    import org.apache.beam.sdk.[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html);
    import org.apache.beam.sdk.[PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html);
    import org.apache.beam.sdk.coders.KvCoder;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.coders.VarLongCoder;
    import org.apache.beam.sdk.extensions.[avro](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_avro__).coders.AvroCoder;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerConfig;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerIO;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerServiceFactoryImpl;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.Flatten;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.Reshuffle;
    import org.apache.beam.sdk.transforms.[View](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.View.html);
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionList;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.PCollectionView;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /** This pipeline reads Spanner Change streams data and writes them to a source DB. */
    @Template(
        name = "Spanner_to_SourceDb",
        category = TemplateCategory.STREAMING,
        displayName = "Spanner Change Streams to Source Database",
        description =
            "Streaming pipeline. Reads data from Spanner Change Streams and"
                + " writes them to a source.",
        optionsClass = SpannerToSourceDbOptions.class,
        flexContainerName = "spanner-to-sourcedb",
        contactInformation = "https://cloud.google.com/support",
        hidden = false,
        streaming = true)
    public class SpannerToSourceDb {
    
      private static final Logger LOG = LoggerFactory.getLogger(SpannerToSourceDb.class);
    
      // JDBC Drivers
      private static final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) MYSQL_DRIVER = "com.mysql.cj.jdbc.Driver";
      private static final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) POSTGRESQL_DRIVER = "org.postgresql.Driver";
    
      // JDBC URL Prefixes
      private static final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) MYSQL_JDBC_PREFIX = "jdbc:mysql://";
      private static final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) POSTGRESQL_JDBC_PREFIX = "jdbc:postgresql://";
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) {
        UncaughtExceptionLogger.register();
    
        LOG.info("Starting Spanner change streams to sink");
    
        SpannerToSourceDbOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(SpannerToSourceDbOptions.class);
    
        // Stage SSL certificates to extraFiles if required as per the pipeline options.
        // Ref https://cloud.google.com/dataflow/docs/guides/templates/ssl-certificates
        new CommonTemplateJvmInitializer().beforeProcessing(options);
    
        boolean isRetryDLQMode = RUN_MODE_RETRY_DLQ.equals(options.getRunMode());
        options.setStreaming(!isRetryDLQMode);
    
        run(options);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      public static [PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html) run(SpannerToSourceDbOptions options) {
        long startTime = System.currentTimeMillis();
        [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html) pipeline = [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html).create(options);
        [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__)
            .getOptions()
            .as(DataflowPipelineWorkerPoolOptions.class)
            .setAutoscalingAlgorithm(AutoscalingAlgorithmType.THROUGHPUT_BASED);
    
        // calculate the max connections per worker
        int maxNumWorkers =
            [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).getOptions().as(DataflowPipelineWorkerPoolOptions.class).getMaxNumWorkers() > 0
                ? [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).getOptions().as(DataflowPipelineWorkerPoolOptions.class).getMaxNumWorkers()
                : 1;
        int connectionPoolSizePerWorker =
            calculateConnectionPoolSizePerWorker(options.getMaxShardConnections(), maxNumWorkers);
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) workerMachineType =
            [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).getOptions().as(DataflowPipelineWorkerPoolOptions.class).getWorkerMachineType();
        Optional<Integer> resourceHintsMinCpus =
            DataflowWorkerMachineTypeUtils.getMinCpuResourceHint([pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).getOptions());
        DataflowWorkerMachineTypeUtils.validateMachineSpecs(workerMachineType, 4, resourceHintsMinCpus);
    
        // Prepare Spanner config
        SpannerConfig spannerConfig =
            SpannerConfig.create()
                .withProjectId(ValueProvider.StaticValueProvider.of(options.getSpannerProjectId()))
                .withInstanceId(ValueProvider.StaticValueProvider.of(options.getInstanceId()))
                .withDatabaseId(ValueProvider.StaticValueProvider.of(options.getDatabaseId()))
                .withRpcPriority(ValueProvider.StaticValueProvider.of(options.getSpannerPriority()));
    
        // Create shadow tables
        // Note that there is a limit on the number of tables that can be created per DB: 5000.
        // If we create shadow tables per shard, there will be an explosion of tables.
        // Anyway the shadow table has Spanner PK so no need to again separate by the shard
        // Lookup by the Spanner PK should be sufficient.
    
        // Prepare Spanner config
        SpannerConfig spannerMetadataConfig =
            SpannerConfig.create()
                .withProjectId(ValueProvider.StaticValueProvider.of(options.getSpannerProjectId()))
                .withInstanceId(ValueProvider.StaticValueProvider.of(options.getMetadataInstance()))
                .withDatabaseId(ValueProvider.StaticValueProvider.of(options.getMetadataDatabase()))
                .withRpcPriority(ValueProvider.StaticValueProvider.of(options.getSpannerPriority()));
    
        // Fetch DDLs and create shadow tables in a DoFn to avoid launcher-side timeout.
        PCollectionTuple ddlTuple =
            [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).apply(
                "Process Information Schema",
                new SpannerInformationSchemaProcessorTransform(
                    spannerConfig, spannerMetadataConfig, options.getShadowTablePrefix()));
    
        final PCollectionView<Ddl> ddlView =
            ddlTuple
                .get(SpannerInformationSchemaProcessorTransform.MAIN_DDL_TAG)
                .apply("View Main DDL", [View](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.View.html).asSingleton());
    
        DataflowPipelineDebugOptions debugOptions = options.as(DataflowPipelineDebugOptions.class);
    
        final PCollectionView<Ddl> shadowTableDdlView =
            ddlTuple
                .get(SpannerInformationSchemaProcessorTransform.SHADOW_TABLE_DDL_TAG)
                .apply("View Shadow DDL", [View](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.View.html).asSingleton());
    
        List<Shard> shards;
        ISpToSrcSourceConnector sourceConnector;
        try {
          sourceConnector = SourceProcessorFactory.getSource(options.getSourceType());
          shards = sourceConnector.parseShardConfig(options.getSourceShardsFilePath());
        } catch (Exception e) {
          throw new RuntimeException("Error parsing shard list", e);
        }
    
        if (shards == null || shards.isEmpty()) {
          LOG.error("Shard list should have at least 1 element.");
          throw new IllegalArgumentException("Shard list should have at least 1 element.");
        }
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) shardingMode =
            sourceConnector.supportsSharding()
                ? [Constants](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.Constants.html).SHARDING_MODE_MULTI_SHARD
                : [Constants](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.Constants.html).SHARDING_MODE_SINGLE_SHARD;
    
        try {
          sourceConnector.validate(shards, options);
        } catch (Exception e) {
          throw new RuntimeException("Validation failed", e);
        }
    
        SourceSchema sourceSchema;
        try {
          sourceSchema = sourceConnector.getInformationSchema(shards);
        } catch (Exception e) {
          throw new RuntimeException("Error fetching source schema", e);
        }
        LOG.info("Source schema: {}", sourceSchema);
    
        if (shards.size() == 1 && !options.getIsShardedMigration()) {
          shardingMode = [Constants](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.Constants.html).SHARDING_MODE_SINGLE_SHARD;
          Shard shard = shards.get(0);
          if ([shard](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html#com_google_cloud_bigtable_data_v2_models_Query_shard_java_util_List_com_google_cloud_bigtable_data_v2_models_KeyOffset__).getLogicalShardId() == null || [shard](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html#com_google_cloud_bigtable_data_v2_models_Query_shard_java_util_List_com_google_cloud_bigtable_data_v2_models_KeyOffset__).getLogicalShardId().isEmpty()) {
            [shard](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html#com_google_cloud_bigtable_data_v2_models_Query_shard_java_util_List_com_google_cloud_bigtable_data_v2_models_KeyOffset__).setLogicalShardId([Constants](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.Constants.html).DEFAULT_SHARD_ID);
            LOG.info(
                "Logical shard id was not found, hence setting it to : " + [Constants](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.Constants.html).DEFAULT_SHARD_ID);
          }
        }
    
        buildPipeline(
            pipeline,
            options,
            sourceSchema,
            shards,
            ddlView,
            shadowTableDdlView,
            spannerConfig,
            spannerMetadataConfig,
            connectionPoolSizePerWorker,
            shardingMode,
            startTime,
            maxNumWorkers);
    
        return [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).run();
      }
    
      static void buildPipeline(
          [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html) pipeline,
          SpannerToSourceDbOptions options,
          SourceSchema sourceSchema,
          List<Shard> shards,
          PCollectionView<Ddl> ddlView,
          PCollectionView<Ddl> shadowTableDdlView,
          SpannerConfig spannerConfig,
          SpannerConfig spannerMetadataConfig,
          int connectionPoolSizePerWorker,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) shardingMode,
          long startTime,
          int maxNumWorkers) {
    
        DataflowPipelineDebugOptions debugOptions = options.as(DataflowPipelineDebugOptions.class);
        boolean isRegularMode = RUN_MODE_REGULAR.equals(options.getRunMode());
        PCollectionTuple reconsumedElements = null;
        DeadLetterQueueManager dlqManager = buildDlqManager(options);
    
        int reshuffleBucketSize =
            maxNumWorkers
                * (debugOptions.getNumberOfWorkerHarnessThreads() > 0
                    ? debugOptions.getNumberOfWorkerHarnessThreads()
                    : [Constants](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.Constants.html).DEFAULT_WORKER_HARNESS_THREAD_COUNT);
    
        if (isRegularMode && (!Strings.isNullOrEmpty(options.getDlqGcsPubSubSubscription()))) {
          reconsumedElements =
              dlqManager.getReconsumerDataTransformForFiles(
                  [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).apply(
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
                    [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).apply(dlqManager.dlqReconsumer(options.getDlqRetryMinutes())));
          } else { // retryDLQ or retryAllDLQ mode
            PCollection<String> oneShotRecords =
                [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).apply("Read severe from OneShot", dlqManager.dlqOneShotReconsumer(startTime));
    
            if (RUN_MODE_RETRY_DLQ.equals(options.getRunMode())) {
              reconsumedElements = dlqManager.getReconsumerDataTransform(oneShotRecords);
            } else {
              // retryAllDLQ mode: Drain both the severe (one-shot) and retry (continuous) buckets
              PCollection<String> continuousRecords =
                  [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).apply(
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
    
        PCollection<FailsafeElement<String, String>> dlqJsonStrRecords =
            reconsumedElements
                .get(DeadLetterQueueManager.RETRYABLE_ERRORS)
                .setCoder(FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of()));
    
        PCollection<TrimmedShardedDataChangeRecord> dlqRecords =
            dlqJsonStrRecords.apply(
                "Convert DLQ records to TrimmedShardedDataChangeRecord",
                ParDo.of(new ConvertDlqRecordToTrimmedShardedDataChangeRecordFn()));
        PCollection<TrimmedShardedDataChangeRecord> mergedRecords = null;
    
        if (options.getFailureInjectionParameter() != null
            && !options.getFailureInjectionParameter().isBlank()) {
          spannerConfig =
              SpannerServiceFactoryImpl.createSpannerService(
                  spannerConfig, options.getFailureInjectionParameter());
        }
    
        if (isRegularMode) {
          PCollection<TrimmedShardedDataChangeRecord> changeRecordsFromDB =
              [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__)
                  .apply(
                      getReadChangeStreamDoFn(
                          options,
                          spannerConfig)) // This emits PCollection<DataChangeRecord> which is Spanner
                  // change
                  // stream data
                  .apply("Reshuffle", Reshuffle.viaRandomKey())
                  .apply("Filteration", ParDo.of(new FilterRecordsFn(options.getFiltrationMode())))
                  .apply("Preprocess", ParDo.of(new PreprocessRecordsFn()));
          mergedRecords =
              PCollectionList.of(changeRecordsFromDB)
                  .and(dlqRecords)
                  .apply("Flatten", Flatten.pCollections());
        } else {
          mergedRecords = dlqRecords;
        }
        CustomTransformation customTransformation =
            CustomTransformation.builder(
                    options.getTransformationJarPath(), options.getTransformationClassName())
                .setCustomParameters(options.getTransformationCustomParameters())
                .build();
    
        if (options.getFailureInjectionParameter() != null
            && !options.getFailureInjectionParameter().isBlank()) {
          spannerMetadataConfig =
              SpannerServiceFactoryImpl.createSpannerService(
                  spannerMetadataConfig, options.getFailureInjectionParameter());
        }
    
        SourceWriterTransform.Result sourceWriterOutput =
            mergedRecords
                .apply(
                    "AssignShardId", // This emits PCollection<KV<Long,
                    // TrimmedShardedDataChangeRecord>> which is Spanner change stream data with key as
                    // PK
                    // mod
                    // number of parallelism
                    ParDo.of(
                            new AssignShardIdFn(
                                spannerConfig,
                                ddlView,
                                sourceSchema,
                                shardingMode,
                                shards.get(0).getLogicalShardId(),
                                options.getSkipDirectoryName(),
                                options.getShardingCustomJarPath(),
                                options.getShardingCustomClassName(),
                                options.getShardingCustomParameters(),
                                options.getMaxShardConnections() * shards.size(),
                                options.getSourceType(),
                                options.getSessionFilePath(),
                                options.getSchemaOverridesFilePath(),
                                options.getTableOverrides(),
                                options
                                    .getColumnOverrides())) // currently assume that all shards accept
                        // the
                        // same source type
                        .withSideInputs(ddlView))
                .setCoder(
                    KvCoder.of(VarLongCoder.of(), AvroCoder.of(TrimmedShardedDataChangeRecord.class)))
                .apply("Reshuffle2", Reshuffle.of())
                .apply(
                    "Write to source",
                    new SourceWriterTransform(
                        shards,
                        spannerMetadataConfig,
                        options.getSourceDbTimezoneOffset(),
                        ddlView,
                        shadowTableDdlView,
                        sourceSchema,
                        options.getShadowTablePrefix(),
                        options.getSkipDirectoryName(),
                        connectionPoolSizePerWorker,
                        options.getSourceType(),
                        customTransformation,
                        options.getSessionFilePath(),
                        options.getSchemaOverridesFilePath(),
                        options.getTableOverrides(),
                        options.getColumnOverrides()));
    
        PCollection<FailsafeElement<String, String>> dlqPermErrorRecords =
            reconsumedElements
                .get(DeadLetterQueueManager.PERMANENT_ERRORS)
                .setCoder(FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of()));
    
        PCollection<FailsafeElement<String, String>> permErrorsFromSourceWriter =
            sourceWriterOutput
                .permanentErrors()
                .setCoder(StringUtf8Coder.of())
                .apply(
                    "Reshuffle3", Reshuffle.<String>viaRandomKey().withNumBuckets(reshuffleBucketSize))
                .apply(
                    "Convert permanent errors from source writer to DLQ format",
                    ParDo.of(new ConvertChangeStreamErrorRecordToFailsafeElementFn()))
                .setCoder(FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of()));
    
        PCollection<FailsafeElement<String, String>> permanentErrors =
            PCollectionList.of(dlqPermErrorRecords)
                .and(permErrorsFromSourceWriter)
                .apply(Flatten.pCollections())
                .apply("Reshuffle", Reshuffle.viaRandomKey());
    
        permanentErrors
            .apply("Update DLQ metrics", ParDo.of(new UpdateDlqMetricsFn(isRegularMode)))
            .apply(
                "DLQ: Write Severe errors to GCS",
                MapElements.via(new StringDeadLetterQueueSanitizer()))
            .setCoder(StringUtf8Coder.of())
            .apply(
                "Write To DLQ for severe errors",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqManager.getSevereDlqDirectoryWithDateTime())
                    .withTmpDirectory((options).getDeadLetterQueueDirectory() + "/tmp_severe/")
                    .setIncludePaneInfo(true)
                    .build());
    
        PCollection<FailsafeElement<String, String>> retryErrors =
            sourceWriterOutput
                .retryableErrors()
                .setCoder(StringUtf8Coder.of())
                .apply(
                    "Reshuffle4", Reshuffle.<String>viaRandomKey().withNumBuckets(reshuffleBucketSize))
                .apply(
                    "Convert retryable errors from source writer to DLQ format",
                    ParDo.of(new ConvertChangeStreamErrorRecordToFailsafeElementFn()))
                .setCoder(FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of()));
    
        retryErrors
            .apply(
                "DLQ: Write retryable Failures to GCS",
                MapElements.via(new StringDeadLetterQueueSanitizer()))
            .setCoder(StringUtf8Coder.of())
            .apply(
                "Write To DLQ for retryable errors",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqManager.getRetryDlqDirectoryWithDateTime())
                    .withTmpDirectory(options.getDeadLetterQueueDirectory() + "/tmp_retry/")
                    .setIncludePaneInfo(true)
                    .build());
    
        PCollection<FailsafeElement<String, String>> skippedRecords =
            sourceWriterOutput
                .skippedSourceWrites()
                .setCoder(StringUtf8Coder.of())
                .apply(
                    "Reshuffle5", Reshuffle.<String>viaRandomKey().withNumBuckets(reshuffleBucketSize))
                .apply(
                    "Convert skipped records from source writer to DLQ format",
                    ParDo.of(new ConvertChangeStreamErrorRecordToFailsafeElementFn()))
                .setCoder(FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of()));
    
        skippedRecords
            .apply(
                "Write skipped records to GCS", MapElements.via(new StringDeadLetterQueueSanitizer()))
            .setCoder(StringUtf8Coder.of())
            .apply(
                "Writing skipped records to GCS",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(
                        options.getDeadLetterQueueDirectory() + "/" + options.getSkipDirectoryName())
                    .withTmpDirectory(options.getDeadLetterQueueDirectory() + "/tmp_skip/")
                    .setIncludePaneInfo(true)
                    .build());
      }
    
      public static SpannerIO.ReadChangeStream getReadChangeStreamDoFn(
          SpannerToSourceDbOptions options, SpannerConfig spannerConfig) {
    
        [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html) startTime = [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[now](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_now__)();
        if (!options.getStartTimestamp().equals("")) {
          startTime = [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[parseTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_parseTimestamp_java_lang_String_)(options.getStartTimestamp());
        }
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) changeStreamMetadataDb = options.getChangeStreamMetadataDatabase();
        if (Strings.isNullOrEmpty(changeStreamMetadataDb)) {
          changeStreamMetadataDb = options.getMetadataDatabase();
        }
        LOG.info("Using database {} for change stream metadata.", changeStreamMetadataDb);
    
        SpannerIO.ReadChangeStream readChangeStreamDoFn =
            SpannerIO.[readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_)()
                .withSpannerConfig(spannerConfig)
                .withChangeStreamName(options.getChangeStreamName())
                .withMetadataInstance(options.getMetadataInstance())
                .withMetadataDatabase(changeStreamMetadataDb)
                .withInclusiveStartAt(startTime)
                .withRpcPriority(options.getSpannerPriority());
    
        if (options.getSpannerMetadataTableName() != null
            && !options.getSpannerMetadataTableName().isEmpty()) {
          readChangeStreamDoFn =
              readChangeStreamDoFn.withMetadataTable(options.getSpannerMetadataTableName());
        }
        if (!options.getEndTimestamp().equals("")) {
          return readChangeStreamDoFn.withInclusiveEndAt(
              [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[parseTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_parseTimestamp_java_lang_String_)(options.getEndTimestamp()));
        }
        return readChangeStreamDoFn;
      }
    
      static DeadLetterQueueManager buildDlqManager(SpannerToSourceDbOptions options) {
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tempLocation =
            options.as(DataflowPipelineOptions.class).getTempLocation().endsWith("/")
                ? options.as(DataflowPipelineOptions.class).getTempLocation()
                : options.as(DataflowPipelineOptions.class).getTempLocation() + "/";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) dlqDirectory =
            options.getDeadLetterQueueDirectory().isEmpty()
                ? tempLocation + "dlq/"
                : options.getDeadLetterQueueDirectory();
        LOG.info("Dead-letter queue directory: {}", dlqDirectory);
        options.setDeadLetterQueueDirectory(dlqDirectory);
        return DeadLetterQueueManager.create(dlqDirectory, options.getDlqMaxRetryCount(), true);
      }
    
      static int calculateConnectionPoolSizePerWorker(Long maxShardConnections, int maxNumWorkers) {
        int connectionPoolSizePerWorker = (int) (maxShardConnections / maxNumWorkers);
        if (connectionPoolSizePerWorker < 1) {
          throw new IllegalArgumentException(
              "Max Dataflow workers "
                  + maxNumWorkers
                  + " is more than max per shard connections: "
                  + maxShardConnections
                  + " this can lead to more"
                  + " database connections than desired. Either reduce the max allowed workers or"
                  + " incease the max shard connections");
        }
        return connectionPoolSizePerWorker;
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
