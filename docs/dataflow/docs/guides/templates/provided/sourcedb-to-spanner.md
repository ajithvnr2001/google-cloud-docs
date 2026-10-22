---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner/
title: Sourcedb to Spanner template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:09.071859+00:00
---

# Sourcedb to Spanner template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Sourcedb to Spanner template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The SourceDB to Spanner template is a batch pipeline that copies data from a relational database into an existing Spanner database. This pipeline uses JDBC to connect to the relational database. You can use this template to copy data from any relational database with available JDBC drivers into Spanner. This only supports a limited set of types of MySQL

For an extra layer of protection, you can also pass in a Cloud KMS key along with a Base64-encoded username, password, and connection string parameters encrypted with the Cloud KMS key. See the [Cloud KMS API encryption](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt) endpoint for additional details on encrypting your username, password, and connection string parameters.

**Note:** If you plan to validate this migration using the [Cloud Storage Avro files to Spanner Data Validation](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-spanner-dv) template, you must populate the `gcsOutputDirectory` parameter to generate the required Avro files. 

## Pipeline requirements

  * The JDBC drivers for the relational database must be available.
  * The Spanner tables must exist before pipeline execution.
  * The Spanner tables must have a compatible schema.
  * The relational database must be accessible from the subnet where Dataflow runs.



## Template parameters

### Required parameters

  * **sourceConfigURL** : The URL of the source connection config file. The file format is dependent on the source type. For Astra, it will point to an Astra connection config file ([sample](https://docs.cloud.google.com/static/dataflow/docs/guides/templates/provided/src/test/resources/SourceConfig/astra-connection-config.json)). For JDBC, it will point to a JDBC sharding config file ([sample](https://docs.cloud.google.com/static/dataflow/docs/guides/templates/provided/src/test/resources/SourceConfig/jdbc-shard-config.json)). For Cassandra, it will point to a Cassandra driver config file ([sample](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/src/test/resources/SourceConfig/cassandra-driver-config.conf)). This parameter is required. For example, `gs://your-bucket/source-config.json`. Defaults to empty.
  * **instanceId** : The destination Cloud Spanner instance.
  * **databaseId** : The destination Cloud Spanner database.
  * **projectId** : This is the name of the Cloud Spanner project.
  * **outputDirectory** : This directory is used to dump the failed/skipped/filtered records in a migration.



### Optional parameters

  * **sourceDbDialect** : Possible values are `CASSANDRA`, `MYSQL`, `POSTGRESQL`, `ORACLE` and `SQLSERVER`. Defaults to: MYSQL.
  * **jdbcDriverJars** : The comma-separated list of driver JAR files. For example, `gs://your-bucket/driver_jar1.jar,gs://your-bucket/driver_jar2.jar`. Defaults to empty.
  * **jdbcDriverClassName** : The JDBC driver class name. For example, `com.mysql.jdbc.Driver`. Defaults to: com.mysql.jdbc.Driver.
  * **tables** : Tables to migrate from source. Defaults to empty.
  * **numPartitions** : The number of partitions. This, along with the lower and upper bound, form partitions strides for generated WHERE clause expressions used to split the partition column evenly. When the input is less than 1, the number is set to 1. Defaults to: 0.
  * **fetchSize** : The number of rows to fetch per page read for JDBC source. If not set, it is auto-inferred from the worker machine type and the estimated row size, falling back to 50_000 rows if it cannot be inferred (for example, when the worker machine type is not specified). If source dialect is Mysql, please see the note below. This ultimately translated to Statement.setFetchSize call at Jdbc layer. It should ONLY be used if the default value throws memory errors.Note for MySql Source: FetchSize is ignored by the Mysql connector unless, `useCursorFetch=true` is also part of the connection properties. For MySql dialect, the pipeline will add `useCursorFetch=true` to the connection properties by default, unless the fetchSize parameter is explicitly set to 0.
  * **spannerHost** : The Cloud Spanner endpoint to call in the template. For example, `https://batch-spanner.googleapis.com`. Defaults to: <https://batch-spanner.googleapis.com>.
  * **maxConnections** : Configures the JDBC connection pool on each worker with maximum number of connections. Use a negative number for no limit. For example, `-1`. Defaults to: 0.
  * **sessionFilePath** : Session file path in Cloud Storage that contains mapping information from Spanner Migration Tool. Defaults to empty.
  * **transformationJarPath** : Custom jar location in Cloud Storage that contains the custom transformation logic for processing records. Defaults to empty.
  * **transformationClassName** : Fully qualified class name having the custom transformation logic. It is a mandatory field in case transformationJarPath is specified. Defaults to empty.
  * **transformationCustomParameters** : String containing any custom parameters to be passed to the custom transformation class. Defaults to empty.
  * **insertOnlyModeForSpannerMutations** : By default the pipeline uses Upserts to write rows to spanner. Which means existing rows would get overwritten. If InsertOnly mode is enabled, inserts would be used instead of upserts and existing rows won't be overwritten.
  * **batchSizeForSpannerMutations** : BatchSize in bytes for Spanner Mutations. if set less than 0, default of Apache Beam's SpannerIO is used, which is 1MB. Set this to 0 or 10, to disable batching mutations.
  * **spannerPriority** : The request priority for Cloud Spanner calls. The value must be one of: [`HIGH`,`MEDIUM`,`LOW`]. Defaults to `HIGH`.
  * **tableOverrides** : These are the table name overrides from source to spanner. They are written in thefollowing format: [{SourceTableName1, SpannerTableName1}, {SourceTableName2, SpannerTableName2}]This example shows mapping Singers table to Vocalists and Albums table to Records. For example, `[{Singers, Vocalists}, {Albums, Records}]`. Defaults to empty.
  * **columnOverrides** : These are the column name overrides from source to spanner. They are written in thefollowing format: [{SourceTableName1.SourceColumnName1, SourceTableName1.SpannerColumnName1}, {SourceTableName2.SourceColumnName1, SourceTableName2.SpannerColumnName1}]Note that the SourceTableName should remain the same in both the source and spanner pair. To override table names, use tableOverrides.The example shows mapping SingerName to TalentName and AlbumName to RecordName in Singers and Albums table respectively. For example, `[{Singers.SingerName, Singers.TalentName}, {Albums.AlbumName, Albums.RecordName}]`. Defaults to empty.
  * **schemaOverridesFilePath** : A file which specifies the table and the column name overrides from source to spanner. Defaults to empty.
  * **uniformizationStageCountHint** : Hint for number of uniformization stages. Currently Applicable only for jdbc based sources like MySQL or PostgreSQL. Leave 0 or default to disable uniformization. Set to -1 for a log(numPartition) number of stages. If your source primary key space is uniformly distributed (for example an auto-incrementing key with sparse holes), it's based to leave it disabled. If your keyspace is not uniform, you might encounter a laggard VM in your dataflow run. In such a case, you can set it to -1 to enable uniformization. Manually setting it to values other than 0 or -1 would help you fine tune the tradeoff of the overhead added by uniformization stages and the performance improvement due to better distribution of work.
  * **failureInjectionParameter** : Failure injection parameter. Only used for testing. Defaults to empty.
  * **maxCommitDelay** : Maximum commit delay time to optimize write throughput in Spanner. Reference <https://cloud.google.com/spanner/docs/throughput-optimized-writes.Set> -1 to let spanner choose the default. Set to a positive value to override for best suited tradeoff of throughput vs latency.Defaults to -1.
  * **gcsOutputDirectory** : This directory is used to write the AVRO files of the records read from source. For example, `gs://your-bucket/your-path`. Defaults to empty.
  * **disabledAlgorithms** : Comma separated algorithms to disable. If this value is set to `none`, no algorithm is disabled. Use this parameter with caution, because the algorithms disabled by default might have vulnerabilities or performance issues. For example, `SSLv3, RC4`.
  * **extraFilesToStage** : Comma separated Cloud Storage paths or Secret Manager secrets for files to stage in the worker. These files are saved in the /extra_files directory in each worker. For example, `gs://<BUCKET_NAME>/file.txt,projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<VERSION_ID>`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Sourcedb to Spanner** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud CLI

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Sourcedb_to_Spanner_Flex \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --parameters \
           sourceConfigURL=SOURCE_CONFIG_URL,\
           instanceId=INSTANCE_ID,\
           databaseId=DATABASE_ID,\
           projectId=PROJECT_ID,\
           outputDirectory=OUTPUT_DIRECTORY,\

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `SOURCE_CONFIG_URL`: the URL to connect to the source database host. It can be either of 1. The JDBC connection URL - which must contain the host, port and source db name and can optionally contain properties like autoReconnect, maxReconnects etc. Format: `jdbc:mysql://{host}:{port}/{dbName}?{parameters}`2. The shard config path
  * `INSTANCE_ID`: the Cloud Spanner Instance Id.
  * `DATABASE_ID`: the Cloud Spanner Database Id.
  * `PROJECT_ID`: the Cloud Spanner Project Id.
  * `OUTPUT_DIRECTORY`: the Output directory for failed/skipped/filtered events



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launchParameter": {
         "jobName": "JOB_NAME",
         "parameters": {
           "sourceConfigURL": "SOURCE_CONFIG_URL",
           "instanceId": "INSTANCE_ID",
           "databaseId": "DATABASE_ID",
           "projectId": "PROJECT_ID",
           "outputDirectory": "OUTPUT_DIRECTORY",
         },
         "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Sourcedb_to_Spanner_Flex",
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
  * `SOURCE_CONFIG_URL`: the URL to connect to the source database host. It can be either of 1. The JDBC connection URL - which must contain the host, port and source db name and can optionally contain properties like autoReconnect, maxReconnects etc. Format: `jdbc:mysql://{host}:{port}/{dbName}?{parameters}`2. The shard config path
  * `INSTANCE_ID`: the Cloud Spanner Instance Id.
  * `DATABASE_ID`: the Cloud Spanner Database Id.
  * `PROJECT_ID`: the Cloud Spanner Project Id.
  * `OUTPUT_DIRECTORY`: the Output directory for failed/skipped/filtered events



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
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.common.CommonTemplateJvmInitializer;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.SourceDbToSpannerOptions;
    import com.google.cloud.teleport.v2.source.ISrcToSpSourceConnector;
    import com.google.cloud.teleport.v2.source.SourceConnectorFactory;
    import com.google.cloud.teleport.v2.spanner.migrations.shard.Shard;
    import com.google.cloud.teleport.v2.spanner.migrations.source.config.JdbcShardConfig;
    import com.google.cloud.teleport.v2.spanner.migrations.source.config.SourceConnectionConfig;
    import com.google.cloud.teleport.v2.spanner.migrations.utils.DataflowWorkerMachineTypeUtils;
    import com.google.common.annotations.VisibleForTesting;
    import com.google.common.base.Preconditions;
    import java.util.Optional;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineWorkerPoolOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerConfig;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.commons.lang3.StringUtils;
    
    /**
     * A template that copies data from a relational database using JDBC to an existing Spanner
     * database.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/sourcedb-to-spanner/README_Sourcedb_to_Spanner_Flex.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Sourcedb_to_Spanner_Flex",
        category = TemplateCategory.BATCH,
        displayName = "Sourcedb to Spanner",
        description = {
          "The SourceDB to Spanner template is a batch pipeline that copies data from a relational"
              + " database into an existing Spanner database. This pipeline uses JDBC to connect to"
              + " the relational database. You can use this template to copy data from any relational"
              + " database with available JDBC drivers into Spanner. This currently only supports a limited set of types of MySQL",
        },
        optionsClass = SourceDbToSpannerOptions.class,
        flexContainerName = "source-db-to-spanner",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner",
        contactInformation = "https://cloud.google.com/support",
        preview = true,
        requirements = {
          "The JDBC drivers for the relational database must be available.",
          "The Spanner tables must exist before pipeline execution.",
          "The Spanner tables must have a compatible schema.",
          "The relational database must be accessible from the subnet where Dataflow runs."
        })
    public class SourceDbToSpanner {
    
      /**
       * Main entry point for executing the pipeline. This will run the pipeline asynchronously. If
       * blocking execution is required, use the {@link SourceDbToSpanner#run} method to start the
       * pipeline and invoke {@code result.waitUntilFinish()} on the {@link PipelineResult}.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        SourceDbToSpannerOptions options = getSourceDbToSpannerOptions(args);
        run(options);
      }
    
      @VisibleForTesting
      protected static SourceDbToSpannerOptions getSourceDbToSpannerOptions(String[] args) {
        // Parse the user options passed from the command-line
        SourceDbToSpannerOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(SourceDbToSpannerOptions.class);
        // Stage SSL certificates to extraFiles if required as per the pipeline options.
        // Ref https://cloud.google.com/dataflow/docs/guides/templates/ssl-certificates
        new CommonTemplateJvmInitializer().beforeProcessing(options);
        return options;
      }
    
      /**
       * Validates the provided pipeline options. TODO: move this to source connector.
       *
       * @param options The execution parameters to the pipeline.
       * @param sourceConnectionConfig Parsed source connection config.
       * @throws IllegalArgumentException if the provided options are invalid for the pipeline.
       */
      @VisibleForTesting
      static void validateOptions(
          SourceDbToSpannerOptions options, SourceConnectionConfig sourceConnectionConfig) {
        if (SourceDbToSpannerOptions.PG_SOURCE_DIALECT.equals(options.getSourceDbDialect())) {
          Preconditions.checkArgument(
              (sourceConnectionConfig instanceof JdbcShardConfig),
              "Postgresql dialect should have JDBC source config.");
          for (Shard shard : ((JdbcShardConfig) sourceConnectionConfig).getShardConfigs()) {
            if (StringUtils.isNotBlank(shard.getNamespace())
                && !shard.getNamespace().equals("public")) {
              throw new IllegalArgumentException(
                  "Non-public namespaces are currently unsupported for PostgreSQL migrations.");
            }
          }
        }
      }
    
      /**
       * Create the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      @VisibleForTesting
      static PipelineResult run(SourceDbToSpannerOptions options) {
        Pipeline pipeline = Pipeline.create(options);
        String workerMachineType =
            pipeline.getOptions().as(DataflowPipelineWorkerPoolOptions.class).getWorkerMachineType();
        Optional<Integer> resourceHintsMinCpus =
            DataflowWorkerMachineTypeUtils.getMinCpuResourceHint(pipeline.getOptions());
        if (!pipeline.getOptions().getRunner().getSimpleName().equals("DirectRunner")) {
          DataflowWorkerMachineTypeUtils.validateMachineSpecs(
              workerMachineType, 4, resourceHintsMinCpus);
        }
    
        SpannerConfig spannerConfig = createSpannerConfig(options);
        SourceConnectionConfig sourceConnectionConfig =
            PipelineController.getSourceConnectionConfig(
                options.getSourceDbDialect(), options.getSourceConfigURL());
    
        validateOptions(options, sourceConnectionConfig);
    
        // Decide type and source of migration
        ISrcToSpSourceConnector connector = SourceConnectorFactory.getSourceConnectorByDialect(options);
        return connector.executeMigration(options, sourceConnectionConfig, pipeline, spannerConfig);
      }
    
      @VisibleForTesting
      static SpannerConfig createSpannerConfig(SourceDbToSpannerOptions options) {
        SpannerConfig spannerConfig =
            SpannerConfig.create()
                .withProjectId(ValueProvider.StaticValueProvider.of(options.getProjectId()))
                .withHost(ValueProvider.StaticValueProvider.of(options.getSpannerHost()))
                .withInstanceId(ValueProvider.StaticValueProvider.of(options.getInstanceId()))
                .withDatabaseId(ValueProvider.StaticValueProvider.of(options.getDatabaseId()))
                .withRpcPriority(ValueProvider.StaticValueProvider.of(options.getSpannerPriority()));
        if (options.getMaxCommitDelay() >= 0) {
          spannerConfig = spannerConfig.withMaxCommitDelay(options.getMaxCommitDelay());
        }
        return spannerConfig;
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
