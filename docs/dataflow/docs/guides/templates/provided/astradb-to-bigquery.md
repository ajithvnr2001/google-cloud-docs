---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/astradb-to-bigquery/
title: AstraDB to BigQuery template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:23.711108+00:00
---

# AstraDB to BigQuery template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/astradb-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  AstraDB to BigQuery template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The AstraDB to BigQuery template is a batch pipeline that reads records from AstraDB and writes them to BigQuery.

If the destination table doesn't exist in BigQuery, the pipeline creates a table with the following values: 

  * The `Dataset ID`, which is inherited from the Cassandra keyspace.
  * The `Table ID`, which is inherited from the Cassandra table.



The schema of the destination table is inferred from the source Cassandra table. 

  * `List` and `Set` are mapped to BigQuery `REPEATED` fields.
  * `Map` are mapped to BigQuery `RECORD` fields.
  * All other types are mapped to BigQuery fields with the corresponding types.
  * Cassandra user-defined types (UDTs) and tuple data types are not supported.



## Pipeline requirements

  * AstraDB account with a token



## Template parameters

### Required parameters

  * **astraToken** : The token value or secret resource ID. For example, `AstraCS:abcdefghij`.
  * **astraDatabaseId** : The database unique identifier (UUID). For example, `cf7af129-d33a-498f-ad06-d97a6ee6eb7`.
  * **astraKeyspace** : The name of the Cassandra keyspace inside of the Astra database.
  * **astraTable** : The name of the table inside of the Cassandra database. For example, `my_table`.



### Optional parameters

  * **astraQuery** : The query to use to filter rows instead of reading the whole table.
  * **astraDatabaseRegion** : If not provided, a default is chosen, which is useful with multi-region databases.
  * **minTokenRangesCount** : The minimal number of splits to use to distribute the query.
  * **outputTableSpec** : The BigQuery table location to write the output to. Use the format `<PROJECT_ID>:<DATASET_NAME>.<TABLE_NAME>`. The table's schema must match the input objects.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **AstraDB to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/AstraDB_To_BigQuery \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --parameters \
           astraToken=ASTRA_TOKEN,\
           astraDatabaseId=ASTRA_DATABASE_ID,\
           astraKeyspace=ASTRA_KEYSPACE,\
           astraTable=ASTRA_TABLE,\

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `ASTRA_TOKEN`: the Astra token
  * `ASTRA_DATABASE_ID`: the database identifier
  * `ASTRA_KEYSPACE`: the Cassandra keyspace
  * `ASTRA_TABLE`: the Cassandra table



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launchParameter": {
         "jobName": "JOB_NAME",
         "parameters": {
           "astraToken": "ASTRA_TOKEN",
           "astraDatabaseId": "ASTRA_DATABASE_ID",
           "astraKeyspace": "ASTRA_KEYSPACE",
           "astraTable": "ASTRA_TABLE",
         },
         "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/AstraDB_To_BigQuery",
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
  * `ASTRA_TOKEN`: the Astra token
  * `ASTRA_DATABASE_ID`: the database identifier
  * `ASTRA_KEYSPACE`: the Cassandra keyspace
  * `ASTRA_TABLE`: the Cassandra table



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
    package com.google.cloud.teleport.v2.astradb.templates;
    
    import com.datastax.oss.driver.api.core.CqlSession;
    import com.dtsx.astra.sdk.db.DbOpsClient;
    import com.google.api.services.bigquery.model.[TableReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.TableReference.html);
    import com.google.api.services.bigquery.model.[TableSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableSchema.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId.html);
    import com.google.cloud.bigquery.[DatasetInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo.html);
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.astradb.options.AstraDbToBigQueryOptions;
    import com.google.cloud.teleport.v2.astradb.transforms.AstraDbToBigQueryMappingFn;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.utils.SecretManagerUtils;
    import java.util.AbstractMap;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.coders.SerializableCoder;
    import org.apache.beam.sdk.io.astra.db.AstraDbIO;
    import org.apache.beam.sdk.io.astra.db.CqlSessionHolder;
    import org.apache.beam.sdk.io.astra.db.mapping.AstraDbMapper;
    import org.apache.beam.sdk.io.astra.db.mapping.BeamRowDbMapperFactoryFn;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryUtils;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.SerializableFunction;
    import org.apache.beam.sdk.values.Row;
    import org.apache.commons.lang3.StringUtils;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link AstraDbToBigQuery} pipeline is a batch pipeline which ingests data from AstraDB and
     * outputs the resulting records to BigQuery.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/astradb-to-bigquery/README_AstraDB_to_BigQuery.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "AstraDB_To_BigQuery",
        category = TemplateCategory.BATCH,
        displayName = "AstraDB to BigQuery",
        description = {
          "The AstraDB to BigQuery template is a batch pipeline that reads records from AstraDB and writes them to BigQuery.",
          "If the destination table doesn't exist in BigQuery, the pipeline creates a table with the following values:\n"
              + "- The `Dataset ID` is inherited from the Cassandra keyspace.\n"
              + "- The `Table ID` is inherited from the Cassandra table.\n",
          "The schema of the destination table is inferred from the source Cassandra table.\n"
              + "- `List` and `Set` are mapped to BigQuery `REPEATED` fields.\n"
              + "- `Map` are mapped to BigQuery `RECORD` fields.\n"
              + "- All other types are mapped to BigQuery fields with the corresponding types.\n"
              + "- Cassandra user-defined types (UDTs) and tuple data types are not supported."
        },
        optionsClass = AstraDbToBigQuery.Options.class,
        flexContainerName = "astradb-to-bigquery",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/astradb-to-bigquery",
        contactInformation = "https://cloud.google.com/support",
        preview = true,
        requirements = {"AstraDB account with a token"})
    public class AstraDbToBigQuery {
    
      /** Logger for the class. */
      private static final Logger LOGGER = LoggerFactory.getLogger(AstraDbToBigQuery.class);
    
      /** If not provided, it is the default token range value. */
      public static final int DEFAULT_TOKEN_RANGE = 18;
    
      /**
       * Options for the sample
       *
       * <p>Inherits standard configuration options.
       */
      public interface Options
          extends PipelineOptions,
              AstraDbToBigQueryOptions.AstraDbSourceOptions,
              AstraDbToBigQueryOptions.BigQueryWriteOptions {}
    
      /** Main operations. */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
        LOGGER.info("Starting pipeline");
    
        try {
    
          Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
          LOGGER.debug("Pipeline Arguments (options) validated");
    
          // --------------------------------
          // AstraDbIO.Read<Row>
          // --------------------------------
    
          // Credentials are read from secrets manager
          AbstractMap.SimpleImmutableEntry<String, byte[]> astraCredentials =
              parseAstraCredentials(options);
          LOGGER.debug("Astra Credentials parsed");
    
          // Map Cassandra Table Schema into BigQuery Table Schema
          SerializableFunction<AstraDbIO.Read<?>, TableSchema> bigQuerySchemaFactory =
              new AstraDbToBigQueryMappingFn(options.getAstraKeyspace(), options.getAstraTable());
          LOGGER.debug("Schema Mapper has been initialized");
    
          // Map Cassandra Rows into (Apache) Beam Rows (DATA)
          SerializableFunction<CqlSession, AstraDbMapper<Row>> beamRowMapperFactory =
              new BeamRowDbMapperFactoryFn(options.getAstraKeyspace(), options.getAstraTable());
          LOGGER.debug("Row Mapper has been initialized");
    
          // Distribute reads across all available Cassandra nodes
          int minimalTokenRangesCount =
              (options.getMinTokenRangesCount() == null)
                  ? DEFAULT_TOKEN_RANGE
                  : options.getMinTokenRangesCount();
    
          // Source: AstraDb
          AstraDbIO.Read<Row> astraSource =
              AstraDbIO.<Row>read()
                  .withToken(astraCredentials.getKey())
                  .withSecureConnectBundle(astraCredentials.getValue())
                  .withKeyspace(options.getAstraKeyspace())
                  .withTable(options.getAstraTable())
                  .withMinNumberOfSplits(minimalTokenRangesCount)
                  .withMapperFactoryFn(beamRowMapperFactory)
                  .withCoder(SerializableCoder.of(Row.class))
                  .withEntity(Row.class);
          LOGGER.debug("AstraDb Source initialization [OK]");
    
          // --------------------------------
          //  BigQueryIO.Write<Row>
          // --------------------------------
    
          TableReference bqTableRef = parseBigQueryDestinationTable(options);
          createBigQueryDestinationTableIfNotExist(options, bqTableRef);
          LOGGER.debug("BigQuery Sink Table has been initialized");
    
          // Sink: BigQuery
          BigQueryIO.Write<Row> bigQuerySink =
              BigQueryIO.<Row>write()
                  .to(bqTableRef)
                  // Specialized function reading cassandra source table and mapping to BigQuery Schema
                  .withSchema(bigQuerySchemaFactory.apply(astraSource))
                  // Provided by google, convert a Beam Row to a BigQuery TableRow
                  .withFormatFunction(row -> row != null ? BigQueryUtils.toTableRow(row) : null)
                  // Table Will be created if not exist
                  .withCreateDisposition(BigQueryIO.Write.CreateDisposition.CREATE_IF_NEEDED)
                  .withWriteDisposition(BigQueryIO.Write.WriteDisposition.WRITE_APPEND);
          LOGGER.debug("BigQuery Sink initialization [OK]");
    
          // --------------------------------
          //  Pipeline
          // --------------------------------
    
          Pipeline astraDbToBigQueryPipeline = Pipeline.create(options);
          astraDbToBigQueryPipeline
              .apply("Read From Astra", astraSource)
              .apply("Write To BigQuery", bigQuerySink);
          astraDbToBigQueryPipeline.run();
    
        } finally {
          // Cassandra Connection is stateful and needs to be closed
          CqlSessionHolder.cleanup();
        }
      }
    
      /**
       * Parse Astra Credentials from secrets in secret Manager. - SecretManagerUtils is not used as
       * only applied to String secrets
       *
       * @param options pipeline options
       * @return a pair with the token and the secure bundle
       */
      private static AbstractMap.SimpleImmutableEntry<String, byte[]> parseAstraCredentials(
          Options options) {
    
        String astraToken = options.getAstraToken();
        if (!astraToken.startsWith("AstraCS")) {
          astraToken = SecretManagerUtils.getSecret(options.getAstraToken());
        }
        LOGGER.info("Astra Token is parsed, value={}", astraToken.substring(0, 10) + "...");
        /*
         * Accessing the devops Api to retrieve the secure bundle.
         */
        DbOpsClient astraDbClient = new DbOpsClient(astraToken, options.getAstraDatabaseId());
        if (!astraDbClient.exist()) {
          throw new RuntimeException(
              "Astra Database does not exist, please check your Astra Token and Database ID");
        }
        byte[] astraSecureBundle = astraDbClient.downloadDefaultSecureConnectBundle();
        if (!StringUtils.isEmpty(options.getAstraDatabaseRegion())) {
          astraSecureBundle =
              astraDbClient.downloadSecureConnectBundle(options.getAstraDatabaseRegion());
        }
        LOGGER.info("Astra Bundle is parsed, length={}", astraSecureBundle.length);
        return new AbstractMap.SimpleImmutableEntry<>(astraToken, astraSecureBundle);
      }
    
      /**
       * Create the Bog Query table Reference (provided or based on Cassandra table name).
       *
       * @param options pipeline options
       * @return the big query table reference
       */
      private static TableReference parseBigQueryDestinationTable(Options options) {
        /*
         * bigQueryOutputTableSpec argument is the Big Query table specification. This is parameter
         * is optional. If not set, the table specification is built from the cassandra source table
         * attributes: keyspace=dataset name, table=table name.
         */
        String bigQueryOutputTableSpec = options.getOutputTableSpec();
        if (StringUtils.isEmpty(bigQueryOutputTableSpec)) {
          bigQueryOutputTableSpec =
              options.getProject() + ":" + options.getAstraKeyspace() + "." + options.getAstraTable();
        }
        TableReference bigQueryTableReference = BigQueryUtils.toTableReference(bigQueryOutputTableSpec);
        LOGGER.info("Big Query table spec has been set to {}", bigQueryOutputTableSpec);
        return bigQueryTableReference;
      }
    
      /**
       * Create destination dataset and tables if needed (schema mapped from Cassandra).
       *
       * @param options pipeline options
       * @param bqTableRef big query table reference
       */
      private static void createBigQueryDestinationTableIfNotExist(
          Options options, TableReference bqTableRef) {
        BigQuery bigquery =
            BigQueryOptions.newBuilder().setProjectId(options.getProject()).build().getService();
        if (null
            == bigquery.getDataset(
                DatasetId.of(bqTableRef.getProjectId(), bqTableRef.getDatasetId()))) {
          LOGGER.info(
              "Dataset was not found: creating DataSet {} in region {}",
              bqTableRef.getDatasetId(),
              options.getWorkerRegion());
          bigquery.create(
              DatasetInfo.newBuilder(bqTableRef.getDatasetId())
                  .setLocation(options.getWorkerRegion())
                  .build());
          LOGGER.debug("Dataset has been created [OK]");
        } else {
          LOGGER.info("Dataset {} already exist", bqTableRef.getDatasetId());
        }
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
