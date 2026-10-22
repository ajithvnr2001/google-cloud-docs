---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/postgresql-to-bigquery/
title: PostgreSQL to BigQuery template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:28.348288+00:00
---

# PostgreSQL to BigQuery template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/postgresql-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  PostgreSQL to BigQuery template Stay organized with collections  Save and categorize content based on your preferences. 

The PostgreSQL to BigQuery template is a batch pipeline that copies data from a PostgreSQL table into an existing BigQuery table. This pipeline uses JDBC to connect to PostgreSQL. For an extra layer of protection, you can also pass in a Cloud KMS key along with Base64-encoded username, password, and connection string parameters encrypted with the Cloud KMS key. For more information about encrypting your username, password, and connection string parameters, see the [Cloud KMS API encryption endpoint](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt). 

## Pipeline requirements

  * The BigQuery table must exist before pipeline execution.
  * The BigQuery table must have a compatible schema.
  * The relational database must be accessible from the subnet where Dataflow runs.



## Template parameters

### Required parameters

  * **connectionURL** : The JDBC connection URL string. Can be passed in as a string that's Base64-encoded and then encrypted with a Cloud KMS key. For example, `jdbc:postgresql://some-host:5432/sampledb`.
  * **outputTable** : The BigQuery output table location. For example, `<PROJECT_ID>:<DATASET_NAME>.<TABLE_NAME>`.
  * **bigQueryLoadingTemporaryDirectory** : The temporary directory for the BigQuery loading process. For example, `gs://your-bucket/your-files/temp_dir`.



### Optional parameters

  * **connectionProperties** : The properties string to use for the JDBC connection. The format of the string must be `[propertyName=property;]*`.For more information, see Configuration Properties (<https://dev.mysql.com/doc/connector-j/en/connector-j-reference-configuration-properties.html>) in the MySQL documentation. For example, `unicode=true;characterEncoding=UTF-8`.
  * **username** : The username to use for the JDBC connection. Can be passed in as a string that's encrypted with a Cloud KMS key, or can be a Secret Manager secret in the form projects/{project}/secrets/{secret}/versions/{secret_version}.
  * **password** : The password to use for the JDBC connection. Can be passed in as a string that's encrypted with a Cloud KMS key, or can be a Secret Manager secret in the form projects/{project}/secrets/{secret}/versions/{secret_version}.
  * **query** : The query to run on the source to extract the data. Note that some JDBC SQL and BigQuery types, although sharing the same name, have some differences. Some important SQL -> BigQuery type mappings to keep in mind are `DATETIME --> TIMESTAMP`. Type casting may be required if your schemas do not match. For example, `select * from sampledb.sample_table`.
  * **KMSEncryptionKey** : The Cloud KMS encryption key to use to decrypt the username, password, and connection string. If you pass in a Cloud KMS key, you must also encrypt the username, password, and connection string. For example, `projects/your-project/locations/global/keyRings/your-keyring/cryptoKeys/your-key`.
  * **useColumnAlias** : If set to `true`, the pipeline uses the column alias (`AS`) instead of the column name to map the rows to BigQuery. Defaults to `false`.
  * **isTruncate** : If set to `true`, the pipeline truncates before loading data into BigQuery. Defaults to `false`, which causes the pipeline to append data.
  * **partitionColumn** : If `partitionColumn` is specified along with the `table`, JdbcIO reads the table in parallel by executing multiple instances of the query on the same table (subquery) using ranges. Currently, supports `Long` and `DateTime` partition columns. Pass the column type through `partitionColumnType`.
  * **partitionColumnType** : The type of the `partitionColumn`, accepts either `long` or `datetime`. Defaults to: long.
  * **table** : The table to read from when using partitions. This parameter also accepts a subquery in parentheses. For example, `(select id, name from Person) as subq`.
  * **numPartitions** : The number of partitions. With the lower and upper bound, this value forms partition strides for generated `WHERE` clause expressions that are used to split the partition column evenly. When the input is less than `1`, the number is set to `1`.
  * **lowerBound** : The lower bound to use in the partition scheme. If not provided, this value is automatically inferred by Apache Beam for the supported types. `datetime` partitionColumnType accepts lower bound in the format `yyyy-MM-dd HH:mm:ss.SSSZ`. For example, `2024-02-20 07:55:45.000+03:30`.
  * **upperBound** : The upper bound to use in the partition scheme. If not provided, this value is automatically inferred by Apache Beam for the supported types. `datetime` partitionColumnType accepts upper bound in the format `yyyy-MM-dd HH:mm:ss.SSSZ`. For example, `2024-02-20 07:55:45.000+03:30`.
  * **fetchSize** : The number of rows to be fetched from database at a time. Not used for partitioned reads. Defaults to: 50000.
  * **createDisposition** : The BigQuery CreateDisposition to use. For example, `CREATE_IF_NEEDED` or `CREATE_NEVER`. Defaults to: CREATE_NEVER.
  * **bigQuerySchemaPath** : The Cloud Storage path for the BigQuery JSON schema. If `createDisposition` is set to `CREATE_IF_NEEDED`, this parameter must be specified. For example, `gs://your-bucket/your-schema.json`.
  * **outputDeadletterTable** : The BigQuery table to use for messages that failed to reach the output table, formatted as `"PROJECT_ID:DATASET_NAME.TABLE_NAME"`. If the table doesn't exist, it is created when the pipeline runs. If this parameter is not specified, the pipeline will fail on write errors.This parameter can only be specified if `useStorageWriteApi` or `useStorageWriteApiAtLeastOnce` is set to true.
  * **disabledAlgorithms** : Comma separated algorithms to disable. If this value is set to `none`, no algorithm is disabled. Use this parameter with caution, because the algorithms disabled by default might have vulnerabilities or performance issues. For example, `SSLv3, RC4`.
  * **extraFilesToStage** : Comma separated Cloud Storage paths or Secret Manager secrets for files to stage in the worker. These files are saved in the /extra_files directory in each worker. For example, `gs://<BUCKET_NAME>/file.txt,projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<VERSION_ID>`.
  * **useStorageWriteApi** : If `true`, the pipeline uses the BigQuery Storage Write API (<https://cloud.google.com/bigquery/docs/write-api>). The default value is `false`. For more information, see Using the Storage Write API (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#storage-write-api>).
  * **useStorageWriteApiAtLeastOnce** : When using the Storage Write API, specifies the write semantics. To use at-least-once semantics (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics>), set this parameter to `true`. To use exactly-once semantics, set the parameter to `false`. This parameter applies only when `useStorageWriteApi` is `true`. The default value is `false`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **PostgreSQL to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/PostgreSQL_to_BigQuery \
        --parameters \
    connectionURL=JDBC_CONNECTION_URL,\
    query=SOURCE_SQL_QUERY,\
    outputTable=PROJECT_ID:DATASET.TABLE_NAME,
    bigQueryLoadingTemporaryDirectory=PATH_TO_TEMP_DIR_ON_GCS,\
    connectionProperties=CONNECTION_PROPERTIES,\
    username=CONNECTION_USERNAME,\
    password=CONNECTION_PASSWORD,\
    KMSEncryptionKey=KMS_ENCRYPTION_KEY

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `JDBC_CONNECTION_URL`: the JDBC connection URL
  * `SOURCE_SQL_QUERY`: the SQL query to run on the source database
  * `DATASET`: your BigQuery dataset
  * `TABLE_NAME`: your BigQuery table name
  * `PATH_TO_TEMP_DIR_ON_GCS`: your Cloud Storage path to the temp directory
  * `CONNECTION_PROPERTIES`: the JDBC connection properties, if needed
  * `CONNECTION_USERNAME`: the JDBC connection username
  * `CONNECTION_PASSWORD`: the JDBC connection password
  * `KMS_ENCRYPTION_KEY`: the Cloud KMS encryption key



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
      "launchParameter": {
        "jobName": "JOB_NAME",
        "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/PostgreSQL_to_BigQuery"
        "parameters": {
          "connectionURL": "JDBC_CONNECTION_URL",
          "query": "SOURCE_SQL_QUERY",
          "outputTable": "PROJECT_ID:DATASET.TABLE_NAME",
          "bigQueryLoadingTemporaryDirectory": "PATH_TO_TEMP_DIR_ON_GCS",
          "connectionProperties": "CONNECTION_PROPERTIES",
          "username": "CONNECTION_USERNAME",
          "password": "CONNECTION_PASSWORD",
          "KMSEncryptionKey":"KMS_ENCRYPTION_KEY"
        },
        "environment": { "zone": "us-central1-f" }
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
  * `JDBC_CONNECTION_URL`: the JDBC connection URL
  * `SOURCE_SQL_QUERY`: the SQL query to run on the source database
  * `DATASET`: your BigQuery dataset
  * `TABLE_NAME`: your BigQuery table name
  * `PATH_TO_TEMP_DIR_ON_GCS`: your Cloud Storage path to the temp directory
  * `CONNECTION_PROPERTIES`: the JDBC connection properties, if needed
  * `CONNECTION_USERNAME`: the JDBC connection username
  * `CONNECTION_PASSWORD`: the JDBC connection password
  * `KMS_ENCRYPTION_KEY`: the Cloud KMS encryption key



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2018 Google LLC
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
    
    import static com.google.cloud.teleport.v2.transforms.BigQueryConverters.wrapBigQueryInsertError;
    import static com.google.cloud.teleport.v2.utils.GCSUtils.getGcsFileAsString;
    import static com.google.cloud.teleport.v2.utils.KMSUtils.maybeDecrypt;
    
    import com.google.api.services.bigquery.model.ErrorProto;
    import com.google.api.services.bigquery.model.TableRow;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.JdbcToBigQueryOptions;
    import com.google.cloud.teleport.v2.transforms.ErrorConverters;
    import com.google.cloud.teleport.v2.utils.BigQueryIOUtils;
    import com.google.cloud.teleport.v2.utils.GCSAwareValueProvider;
    import com.google.cloud.teleport.v2.utils.JdbcConverters;
    import com.google.cloud.teleport.v2.utils.ResourceUtils;
    import com.google.cloud.teleport.v2.utils.SecretManagerUtils;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.annotations.VisibleForTesting;
    import com.google.common.base.Strings;
    import java.util.List;
    import java.util.Objects;
    import java.util.stream.Collectors;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.FileSystems;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryInsertError;
    import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy;
    import org.apache.beam.sdk.io.gcp.bigquery.TableRowJsonCoder;
    import org.apache.beam.sdk.io.gcp.bigquery.WriteResult;
    import org.apache.beam.sdk.io.jdbc.JdbcIO;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider.StaticValueProvider;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.TypeDescriptor;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.joda.time.DateTime;
    import org.joda.time.format.DateTimeFormat;
    import org.joda.time.format.DateTimeFormatter;
    
    /**
     * A template that copies data from a relational database using JDBC to an existing BigQuery table.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/jdbc-and-googlecloud/README_Jdbc_to_BigQuery_Flex.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Jdbc_to_BigQuery_Flex",
        category = TemplateCategory.BATCH,
        displayName = "JDBC to BigQuery with BigQuery Storage API support",
        description = {
          "The JDBC to BigQuery template is a batch pipeline that copies data from a relational database table into an existing BigQuery table. "
              + "This pipeline uses JDBC to connect to the relational database. You can use this template to copy data from any relational database with available JDBC drivers into BigQuery.",
          "For an extra layer of protection, you can also pass in a Cloud KMS key along with a Base64-encoded username, password, and connection string parameters encrypted with the Cloud KMS key. "
              + "See the <a href=\"https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt\">Cloud KMS API encryption endpoint</a> for additional details on encrypting your username, password, and connection string parameters."
        },
        optionsClass = JdbcToBigQueryOptions.class,
        flexContainerName = "jdbc-and-googlecloud",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/jdbc-to-bigquery",
        contactInformation = "https://cloud.google.com/support",
        preview = true,
        requirements = {
          "The JDBC drivers for the relational database must be available.",
          "If BigQuery table already exist before pipeline execution, it must have a compatible schema.",
          "The relational database must be accessible from the subnet where Dataflow runs."
        })
    public class JdbcToBigQuery {
    
      /** Coder for FailsafeElement. */
      private static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      /**
       * Main entry point for executing the pipeline. This will run the pipeline asynchronously. If
       * blocking execution is required, use the {@link JdbcToBigQuery#run} method to start the pipeline
       * and invoke {@code result.waitUntilFinish()} on the {@link PipelineResult}.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        // Parse the user options passed from the command-line
        JdbcToBigQueryOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(JdbcToBigQueryOptions.class);
    
        run(options, writeToBQTransform(options));
      }
    
      /**
       * Create the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @param writeToBQ the transform that outputs {@link TableRow}s to BigQuery.
       * @return The result of the pipeline execution.
       */
      @VisibleForTesting
      static PipelineResult run(JdbcToBigQueryOptions options, Write<TableRow> writeToBQ) {
        // Validate BQ STORAGE_WRITE_API options
        BigQueryIOUtils.validateBQStorageApiOptionsBatch(options);
        if (!options.getUseStorageWriteApi()
            && !options.getUseStorageWriteApiAtLeastOnce()
            && !Strings.isNullOrEmpty(options.getOutputDeadletterTable())) {
          throw new IllegalArgumentException(
              "outputDeadletterTable can only be specified if BigQuery Storage Write API is enabled either with useStorageWriteApi or useStorageWriteApiAtLeastOnce.");
        }
    
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        /*
         * Steps: 1) Read records via JDBC and convert to TableRow via RowMapper
         *        2) Append TableRow to BigQuery via BigQueryIO
         */
        JdbcIO.DataSourceConfiguration dataSourceConfiguration =
            JdbcIO.DataSourceConfiguration.create(
                    StaticValueProvider.of(options.getDriverClassName()),
                    maybeDecrypt(
                        maybeParseSecret(options.getConnectionURL()), options.getKMSEncryptionKey()))
                .withUsername(
                    maybeDecrypt(
                        maybeParseSecret(options.getUsername()), options.getKMSEncryptionKey()))
                .withPassword(
                    maybeDecrypt(
                        maybeParseSecret(options.getPassword()), options.getKMSEncryptionKey()));
    
        if (options.getDriverJars() != null) {
          dataSourceConfiguration = dataSourceConfiguration.withDriverJars(options.getDriverJars());
        }
    
        if (options.getConnectionProperties() != null) {
          dataSourceConfiguration =
              dataSourceConfiguration.withConnectionProperties(options.getConnectionProperties());
        }
    
        /*
         * Step 1: Read records via JDBC and convert to TableRow
         *         via {@link org.apache.beam.sdk.io.jdbc.JdbcIO.RowMapper}
         */
        PCollection<TableRow> rows;
        if (options.getPartitionColumn() != null && options.getTable() != null) {
          // Read with Partitions
          JdbcIO.ReadWithPartitions<TableRow, ?> readIO = null;
          final String partitionColumnType = options.getPartitionColumnType();
          if (partitionColumnType == null || "long".equals(partitionColumnType)) {
            JdbcIO.ReadWithPartitions<TableRow, Long> longTypeReadIO =
                JdbcIO.<TableRow, Long>readWithPartitions(TypeDescriptors.longs())
                    .withDataSourceConfiguration(dataSourceConfiguration)
                    .withTable(options.getTable())
                    .withPartitionColumn(options.getPartitionColumn())
                    .withRowMapper(JdbcConverters.getResultSetToTableRow(options.getUseColumnAlias()));
            if (options.getLowerBound() != null && options.getUpperBound() != null) {
              // Check if lower bound and upper bound are long type.
              try {
                longTypeReadIO =
                    longTypeReadIO
                        .withLowerBound(Long.valueOf(options.getLowerBound()))
                        .withUpperBound(Long.valueOf(options.getUpperBound()));
              } catch (NumberFormatException e) {
                throw new NumberFormatException(
                    "Expected Long values for lowerBound and upperBound, received : " + e.getMessage());
              }
            }
            readIO = longTypeReadIO;
          } else if ("datetime".equals(partitionColumnType)) {
            JdbcIO.ReadWithPartitions<TableRow, DateTime> dateTimeReadIO =
                JdbcIO.<TableRow, DateTime>readWithPartitions(TypeDescriptor.of(DateTime.class))
                    .withDataSourceConfiguration(dataSourceConfiguration)
                    .withTable(options.getTable())
                    .withPartitionColumn(options.getPartitionColumn())
                    .withRowMapper(JdbcConverters.getResultSetToTableRow(options.getUseColumnAlias()));
            if (options.getLowerBound() != null && options.getUpperBound() != null) {
              DateTimeFormatter dateFormatter =
                  DateTimeFormat.forPattern("yyyy-MM-dd HH:mm:ss.SSSZ").withOffsetParsed();
              // Check if lowerBound and upperBound are DateTime type.
              try {
                dateTimeReadIO =
                    dateTimeReadIO
                        .withLowerBound(dateFormatter.parseDateTime(options.getLowerBound()))
                        .withUpperBound(dateFormatter.parseDateTime(options.getUpperBound()));
              } catch (IllegalArgumentException e) {
                throw new IllegalArgumentException(
                    "Expected DateTime values in the format for lowerBound and upperBound, received : "
                        + e.getMessage());
              }
            }
            readIO = dateTimeReadIO;
          } else {
            throw new IllegalStateException("Received unsupported partitionColumnType.");
          }
          if (options.getNumPartitions() != null) {
            readIO = readIO.withNumPartitions(options.getNumPartitions());
          }
          if (options.getFetchSize() != null && options.getFetchSize() > 0) {
            readIO = readIO.withFetchSize(options.getFetchSize());
          }
    
          rows = pipeline.apply("Read from JDBC with Partitions", readIO);
        } else {
          if (options.getQuery() == null) {
            throw new IllegalArgumentException(
                "Either 'query' or both 'table' AND 'PartitionColumn' must be specified to read from JDBC");
          }
          JdbcIO.Read<TableRow> readIO =
              JdbcIO.<TableRow>read()
                  .withDataSourceConfiguration(dataSourceConfiguration)
                  .withQuery(new GCSAwareValueProvider(options.getQuery()))
                  .withCoder(TableRowJsonCoder.of())
                  .withRowMapper(JdbcConverters.getResultSetToTableRow(options.getUseColumnAlias()));
    
          if (options.getFetchSize() != null && options.getFetchSize() > 0) {
            readIO = readIO.withFetchSize(options.getFetchSize());
          }
    
          rows = pipeline.apply("Read from JdbcIO", readIO);
        }
    
        /*
         * Step 2: Append TableRow to an existing BigQuery table
         */
        WriteResult writeResult = rows.apply("Write to BigQuery", writeToBQ);
    
        /*
         * Step 3.
         * If using Storage Write API, capture failed inserts and either
         *   a) write error rows to DLQ
         *   b) fail the pipeline
         */
        if (options.getUseStorageWriteApi() || options.getUseStorageWriteApiAtLeastOnce()) {
          PCollection<BigQueryInsertError> insertErrors =
              BigQueryIOUtils.writeResultToBigQueryInsertErrors(writeResult, options);
    
          if (!Strings.isNullOrEmpty(options.getOutputDeadletterTable())) {
            /*
             * Step 3a.
             * Elements that failed inserts into BigQuery are extracted and converted to FailsafeElement
             */
            PCollection<FailsafeElement<String, String>> failedInserts =
                insertErrors
                    .apply(
                        "WrapInsertionErrors",
                        MapElements.into(FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor())
                            .via((BigQueryInsertError e) -> wrapBigQueryInsertError(e)))
                    .setCoder(FAILSAFE_ELEMENT_CODER);
    
            /*
             * Step 3a Contd.
             * Insert records that failed insert into deadletter table
             */
            failedInserts.apply(
                "WriteFailedRecords",
                ErrorConverters.WriteStringMessageErrors.newBuilder()
                    .setErrorRecordsTable(options.getOutputDeadletterTable())
                    .setErrorRecordsTableSchema(ResourceUtils.getDeadletterTableSchemaJson())
                    .setUseWindowedTimestamp(false)
                    .build());
          } else {
            /*
             * Step 3b.
             * Fail pipeline upon write errors if no DLQ was specified
             */
            insertErrors.apply(ParDo.of(new ThrowWriteErrorsDoFn()));
          }
        }
    
        // Execute the pipeline and return the result.
        return pipeline.run();
      }
    
      static class ThrowWriteErrorsDoFn extends DoFn<BigQueryInsertError, Void> {
        @ProcessElement
        public void processElement(ProcessContext c) {
          BigQueryInsertError insertError = Objects.requireNonNull(c.element());
          List<String> errorMessages =
              insertError.getError().getErrors().stream()
                  .map(ErrorProto::getMessage)
                  .collect(Collectors.toList());
          String stackTrace = String.join("\nCaused by:", errorMessages);
    
          throw new IllegalStateException(
              String.format(
                  "Failed to insert row %s.\nCaused by: %s", insertError.getRow(), stackTrace));
        }
      }
    
      /**
       * Create the {@link Write} transform that outputs the collection to BigQuery as per input option.
       */
      @VisibleForTesting
      static Write<TableRow> writeToBQTransform(JdbcToBigQueryOptions options) {
        // Needed for loading GCS filesystem before Pipeline.Create call
        FileSystems.setDefaultPipelineOptions(options);
        Write<TableRow> write =
            BigQueryIO.writeTableRows()
                .withoutValidation()
                .withCreateDisposition(Write.CreateDisposition.valueOf(options.getCreateDisposition()))
                .withWriteDisposition(
                    options.getIsTruncate()
                        ? Write.WriteDisposition.WRITE_TRUNCATE
                        : Write.WriteDisposition.WRITE_APPEND)
                .withCustomGcsTempLocation(
                    StaticValueProvider.of(options.getBigQueryLoadingTemporaryDirectory()))
                .withExtendedErrorInfo()
                .to(options.getOutputTable());
    
        if (Write.CreateDisposition.valueOf(options.getCreateDisposition())
            != Write.CreateDisposition.CREATE_NEVER) {
          write = write.withJsonSchema(getGcsFileAsString(options.getBigQuerySchemaPath()));
        }
        if (options.getUseStorageWriteApi() || options.getUseStorageWriteApiAtLeastOnce()) {
          write = write.withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors());
        }
    
        return write;
      }
    
      /**
       * Retrieves a secret value from SecretManagerUtils if the input string matches the specified
       * pattern.
       *
       * @param secret The input string representing a potential secret.
       * @return The secret value if the input matches the pattern and the secret is found, otherwise
       *     the original input string.
       */
      private static String maybeParseSecret(String secret) {
        // Check if the input string is not null.
        if (secret != null) {
          // Check if the input string matches the pattern for secrets stored in SecretManagerUtils.
          if (secret.matches("projects/.*/secrets/.*/versions/.*")) { // Use .* to match any characters
            // Retrieve the secret value from SecretManagerUtils.
            return SecretManagerUtils.getSecret(secret);
          }
        }
        // If the input is null or doesn't match the pattern, return the original input.
        return secret;
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
