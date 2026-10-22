---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-parquet/
title: BigQuery export to Parquet (via Storage API) template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:25.067616+00:00
---

# BigQuery export to Parquet (via Storage API) template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-parquet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  BigQuery export to Parquet (via Storage API) template Stay organized with collections  Save and categorize content based on your preferences. 

The BigQuery export to Parquet template is a batch pipeline that reads data from a BigQuery table and writes it to a Cloud Storage bucket in Parquet format. This template utilizes the [BigQuery Storage API](https://docs.cloud.google.com/bigquery/docs/reference/storage) to export the data.

## Pipeline requirements

  * The input BigQuery table must exist before running the pipeline.
  * The output Cloud Storage bucket must exist before running the pipeline.



## Template parameters

### Required parameters

  * **tableRef** : The BigQuery input table location. For example, `your-project:your-dataset.your-table-name`.
  * **bucket** : The Cloud Storage folder to write the Parquet files to. For example, `gs://your-bucket/export/`.



### Optional parameters

  * **numShards** : The number of output file shards. The default value is `1`.
  * **fields** : A comma-separated list of fields to select from the input BigQuery table.
  * **rowRestriction** : Read only rows which match the specified filter, which must be a SQL expression compatible with Google standard SQL (<https://cloud.google.com/bigquery/docs/reference/standard-sql>). If no value is specified, then all rows are returned.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **BigQuery export to Parquet (via Storage API)** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/BigQuery_to_Parquet \
        --region=REGION_NAME \
        --parameters \
    tableRef=BIGQUERY_TABLE,\
    bucket=OUTPUT_DIRECTORY,\
    numShards=NUM_SHARDS,\
    fields=FIELDS

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `BIGQUERY_TABLE`: your BigQuery table name
  * `OUTPUT_DIRECTORY`: your Cloud Storage folder for output files
  * `NUM_SHARDS`: the desired number of output file shards
  * `FIELDS`: the comma-separated list of fields to select from the input BigQuery table



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "tableRef": "BIGQUERY_TABLE",
              "bucket": "OUTPUT_DIRECTORY",
              "numShards": "NUM_SHARDS",
              "fields": "FIELDS"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/BigQuery_to_Parquet",
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
  * `BIGQUERY_TABLE`: your BigQuery table name
  * `OUTPUT_DIRECTORY`: your Cloud Storage folder for output files
  * `NUM_SHARDS`: the desired number of output file shards
  * `FIELDS`: the comma-separated list of fields to select from the input BigQuery table



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2019 Google LLC
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
    
    import com.google.api.gax.rpc.[InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html);
    import com.google.api.services.bigquery.model.TableReference;
    import com.google.cloud.bigquery.storage.v1beta1.BigQueryStorageClient;
    import com.google.cloud.bigquery.storage.v1beta1.ReadOptions.TableReadOptions;
    import com.google.cloud.bigquery.storage.v1beta1.Storage.CreateReadSessionRequest;
    import com.google.cloud.bigquery.storage.v1beta1.Storage.ReadSession;
    import com.google.cloud.bigquery.storage.v1beta1.TableReferenceProto;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.templates.BigQueryToParquet.BigQueryToParquetOptions;
    import com.google.common.base.Splitter;
    import com.google.common.base.Strings;
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    import org.apache.avro.Schema;
    import org.apache.avro.generic.GenericRecord;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.extensions.avro.coders.AvroCoder;
    import org.apache.beam.sdk.io.FileIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryHelpers;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.TypedRead;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.TypedRead.Method;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryOptions;
    import org.apache.beam.sdk.io.gcp.bigquery.SchemaAndRecord;
    import org.apache.beam.sdk.io.parquet.ParquetIO;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link BigQueryToParquet} pipeline exports data from a BigQuery table to Parquet file(s) in a
     * Google Cloud Storage bucket.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/bigquery-to-parquet/README_BigQuery_to_Parquet.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "BigQuery_to_Parquet",
        category = TemplateCategory.BATCH,
        displayName = "BigQuery export to Parquet (via Storage API)",
        description =
            "The BigQuery export to Parquet template is a batch pipeline that reads data from a BigQuery table and writes it to a Cloud Storage bucket in Parquet format. "
                + "This template utilizes the <a href=\"https://cloud.google.com/bigquery/docs/reference/storage\">BigQuery Storage API</a> to export the data.",
        optionsClass = BigQueryToParquetOptions.class,
        flexContainerName = "bigquery-to-parquet",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-parquet",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The input BigQuery table must exist before running the pipeline.",
          "The output Cloud Storage bucket must exist before running the pipeline."
        })
    public class BigQueryToParquet {
    
      /* Logger for class. */
      private static final Logger LOG = LoggerFactory.getLogger(BigQueryToParquet.class);
    
      /** File suffix for file to be written. */
      private static final String FILE_SUFFIX = ".parquet";
    
      /** Factory to create BigQueryStorageClients. */
      static class BigQueryStorageClientFactory {
    
        /**
         * Creates BigQueryStorage client for use in extracting table schema.
         *
         * @return BigQueryStorageClient
         */
        static BigQueryStorageClient create() {
          try {
            return BigQueryStorageClient.create();
          } catch (IOException e) {
            LOG.error("Error connecting to BigQueryStorage API: " + e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
            throw new RuntimeException(e);
          }
        }
      }
    
      /** Factory to create ReadSessions. */
      static class ReadSessionFactory {
    
        /**
         * Creates ReadSession for schema extraction.
         *
         * @param client BigQueryStorage client used to create ReadSession.
         * @param options BigQueryToParquetOptions options.
         * @param tableReadOptions TableReadOptions that specify any fields in the table to filter on.
         * @return session ReadSession object that contains the schema for the export.
         */
        static ReadSession create(
            BigQueryStorageClient client,
            BigQueryToParquetOptions options,
            TableReadOptions tableReadOptions) {
          String tableString = options.getTableRef();
          TableReference tableReference = BigQueryHelpers.parseTableSpec(tableString);
          BigQueryOptions bigQueryOptions = options.as(BigQueryOptions.class);
          String parentProjectId =
              bigQueryOptions.getBigQueryProject() == null
                  ? bigQueryOptions.getProject()
                  : bigQueryOptions.getBigQueryProject();
          String parentProjectIdResource = "projects/" + parentProjectId;
    
          TableReferenceProto.TableReference storageTableRef =
              TableReferenceProto.TableReference.newBuilder()
                  .setProjectId(tableReference.getProjectId())
                  .setDatasetId(tableReference.getDatasetId())
                  .setTableId(tableReference.getTableId())
                  .build();
    
          CreateReadSessionRequest.Builder builder =
              CreateReadSessionRequest.newBuilder()
                  .setParent(parentProjectIdResource)
                  .setReadOptions(tableReadOptions)
                  .setTableReference(storageTableRef);
          try {
            return client.createReadSession([builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails_builder__).build());
          } catch ([InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html) iae) {
            LOG.error("Error creating ReadSession: " + iae.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
            throw new RuntimeException(iae);
          }
        }
      }
    
      /**
       * The {@link BigQueryToParquetOptions} class provides the custom execution options passed by the
       * executor at the command-line.
       */
      public interface BigQueryToParquetOptions extends PipelineOptions {
        @TemplateParameter.BigQueryTable(
            order = 1,
            description = "BigQuery table to export",
            groupName = "Source",
            helpText = "The BigQuery input table location.",
            example = "your-project:your-dataset.your-table-name")
        @Required
        String getTableRef();
    
        void setTableRef(String tableRef);
    
        @TemplateParameter.GcsWriteFile(
            order = 2,
            description = "Output Cloud Storage file(s)",
            groupName = "Target",
            helpText = "The Cloud Storage folder to write the Parquet files to.",
            example = "gs://your-bucket/export/")
        @Required
        String getBucket();
    
        void setBucket(String bucket);
    
        @TemplateParameter.Integer(
            order = 3,
            optional = true,
            description = "Maximum output shards",
            helpText = "The number of output file shards. The default value is `1`.")
        @Default.Integer(0)
        Integer getNumShards();
    
        void setNumShards(Integer numShards);
    
        @TemplateParameter.Text(
            order = 4,
            optional = true,
            description = "List of field names",
            helpText = "A comma-separated list of fields to select from the input BigQuery table.")
        String getFields();
    
        void setFields(String fields);
    
        @TemplateParameter.Text(
            order = 5,
            optional = true,
            description = "Row restrictions/filter.",
            helpText =
                "Read only rows which match the specified filter, which must be a SQL expression"
                    + " compatible with Google standard SQL"
                    + " (https://cloud.google.com/bigquery/docs/reference/standard-sql). If no value is"
                    + " specified, then all rows are returned.")
        String getRowRestriction();
    
        void setRowRestriction(String restriction);
      }
    
      /**
       * The {@link BigQueryToParquet#getTableSchema(ReadSession)} method gets Avro schema for table
       * using from the {@link ReadSession} object.
       *
       * @param session ReadSession that contains schema for table, filtered by fields if any.
       * @return avroSchema Avro schema for table. If fields are provided then schema will only contain
       *     those fields.
       */
      private static Schema getTableSchema(ReadSession session) {
        Schema avroSchema;
    
        avroSchema = new Schema.Parser().parse(session.getAvroSchema().getSchema());
        LOG.info("Schema for export is: " + avroSchema.toString());
    
        return avroSchema;
      }
    
      /**
       * Main entry point for pipeline execution.
       *
       * @param args Command line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        BigQueryToParquetOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(BigQueryToParquetOptions.class);
    
        run(options);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      private static PipelineResult run(BigQueryToParquetOptions options) {
    
        // Create the pipeline.
        Pipeline pipeline = Pipeline.create(options);
    
        TableReadOptions.Builder builder = TableReadOptions.newBuilder();
    
        /* Add fields to filter export on, if any. */
        if (options.getFields() != null) {
          [builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails_builder__).addAllSelectedFields(Arrays.asList(options.getFields().split(",\\s*")));
        }
    
        // Add row restrictions/filter if any.
        if (!Strings.isNullOrEmpty(options.getRowRestriction())) {
          [builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails_builder__).setRowRestriction(options.getRowRestriction());
        }
    
        TableReadOptions tableReadOptions = [builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails_builder__).build();
        BigQueryStorageClient client = BigQueryStorageClientFactory.create();
        ReadSession session = ReadSessionFactory.create(client, options, tableReadOptions);
    
        // Extract schema from ReadSession
        Schema schema = getTableSchema(session);
        client.[close](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Watchdog.html#com_google_api_gax_rpc_Watchdog_close__)();
    
        TypedRead<GenericRecord> readFromBQ =
            BigQueryIO.read(SchemaAndRecord::getRecord)
                .from(options.getTableRef())
                .withTemplateCompatibility()
                .withMethod(Method.DIRECT_READ)
                .withCoder(AvroCoder.of(schema));
    
        if (options.getFields() != null) {
          List<String> selectedFields = Splitter.on(",").splitToList(options.getFields());
          readFromBQ =
              selectedFields.[isEmpty](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html#com_google_api_gax_rpc_LibraryMetadata_isEmpty__)() ? readFromBQ : readFromBQ.withSelectedFields(selectedFields);
        }
    
        // Add row restrictions/filter if any.
        if (!Strings.isNullOrEmpty(options.getRowRestriction())) {
          readFromBQ = readFromBQ.withRowRestriction(options.getRowRestriction());
        }
    
        /*
         * Steps: 1) Read records from BigQuery via BigQueryIO.
         *        2) Write records to Google Cloud Storage in Parquet format.
         */
        pipeline
            /*
             * Step 1: Read records via BigQueryIO using supplied schema as a PCollection of
             *         {@link GenericRecord}.
             */
            .[apply](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestMutator.html#com_google_api_gax_rpc_RequestMutator_apply_RequestT_)("ReadFromBigQuery", readFromBQ)
            /*
             * Step 2: Write records to Google Cloud Storage as one or more Parquet files
             *         via {@link ParquetIO}.
             */
            .[apply](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestMutator.html#com_google_api_gax_rpc_RequestMutator_apply_RequestT_)(
                "WriteToParquet",
                FileIO.<GenericRecord>write()
                    .via(ParquetIO.sink(schema))
                    .to(options.getBucket())
                    .withNumShards(options.getNumShards())
                    .withSuffix(FILE_SUFFIX));
    
        // Execute the pipeline and return the result.
        return pipeline.[run](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Watchdog.html#com_google_api_gax_rpc_Watchdog_run__)();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
