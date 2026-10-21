---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-clickhouse/
title: BigQuery to Clickhouse template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:07.139628+00:00
---

# BigQuery to Clickhouse template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-clickhouse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  BigQuery to Clickhouse template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The BigQuery to Clickhouse template is a batch pipeline that copies data from a BigQuery table into an existing Clickhouse table. The template can either read the entire table or read specific records using a supplied query. 

## Pipeline requirements

  * The source BigQuery table must exist.
  * The Clickhouse table must exist.



## Template parameters

### Required parameters

  * **jdbcUrl** : The target ClickHouse JDBC URL in the format `jdbc:clickhouse://host:port/schema`. Any JDBC option could be added at the end of the JDBC URL. For example, `jdbc:clickhouse://localhost:8123/default`.
  * **clickHouseUsername** : The ClickHouse username to authenticate with.
  * **clickHouseTable** : The target ClickHouse table name to insert the data to.



### Optional parameters

  * **inputTableSpec** : The BigQuery table to read from. If you specify `inputTableSpec`, the template reads the data directly from BigQuery storage by using the BigQuery Storage Read API (<https://cloud.google.com/bigquery/docs/reference/storage>). For information about limitations in the Storage Read API, see <https://cloud.google.com/bigquery/docs/reference/storage#limitations>. You must specify either `inputTableSpec` or `query`. If you set both parameters, the template uses the `query` parameter. For example, `<BIGQUERY_PROJECT>:<DATASET_NAME>.<INPUT_TABLE>`.
  * **outputDeadletterTable** : The BigQuery table for messages that failed to reach the output table. If a table doesn't exist, it is created during pipeline execution. If not specified, `<outputTableSpec>_error_records` is used. For example, `<PROJECT_ID>:<DATASET_NAME>.<DEADLETTER_TABLE>`.
  * **query** : The SQL query to use to read data from BigQuery. If the BigQuery dataset is in a different project than the Dataflow job, specify the full dataset name in the SQL query, for example: <PROJECT_ID>.<DATASET_NAME>.<TABLE_NAME>. By default, the `query` parameter uses GoogleSQL (<https://cloud.google.com/bigquery/docs/introduction-sql>), unless `useLegacySql` is `true`. You must specify either `inputTableSpec` or `query`. If you set both parameters, the template uses the `query` parameter. For example, `select * from sampledb.sample_table`.
  * **useLegacySql** : Set to `true` to use legacy SQL. This parameter only applies when using the `query` parameter. Defaults to `false`.
  * **queryLocation** : Needed when reading from an authorized view without underlying table's permission. For example, `US`.
  * **queryTempDataset** : With this option, you can set an existing dataset to create the temporary table to store the results of the query. For example, `temp_dataset`.
  * **KMSEncryptionKey** : If reading from BigQuery using query source, use this Cloud KMS key to encrypt any temporary tables created. For example, `projects/your-project/locations/global/keyRings/your-keyring/cryptoKeys/your-key`.
  * **clickHousePassword** : The ClickHouse password to authenticate with.
  * **maxInsertBlockSize** : The maximum block size for insertion, if we control the creation of blocks for insertion (ClickHouseIO option).
  * **insertDistributedSync** : If setting is enabled, insert query into distributed waits until data will be sent to all nodes in cluster. (ClickHouseIO option).
  * **insertQuorum** : For INSERT queries in the replicated table, wait writing for the specified number of replicas and linearize the addition of the data. 0 - disabled. This setting is disabled in default server settings (ClickHouseIO option).
  * **insertDeduplicate** : For INSERT queries in the replicated table, specifies that deduplication of inserting blocks should be performed.
  * **maxRetries** : Maximum number of retries per insert.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **BigQuery to Clickhouse** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/BigQuery_to_Clickhouse \
        --parameters \
    jdbcUrl=JDBC_URL,\
    clickHouseUsername=CLICKHOUSE_USERNAME,\
    clickHouseTable=CLICKHOUSE_TABLE

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `JDBC_URL`: your jdbc url.
  * `CLICKHOUSE_USERNAME`: your Clickhouse username.
  * `CLICKHOUSE_TABLE`: your Clickhouse table.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "jdbcUrl": "JDBC_URL",
              "clickHouseUsername": "CLICKHOUSE_USERNAME",
              "clickHouseTable": "CLICKHOUSE_TABLE"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/BigQuery_to_Clickhouse",
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
  * `JDBC_URL`: your jdbc url.
  * `CLICKHOUSE_USERNAME`: your Clickhouse username.
  * `CLICKHOUSE_TABLE`: your Clickhouse table.



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2025 Google LLC
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
    package com.google.cloud.teleport.v2.clickhouse.templates;
    
    import static org.apache.beam.vendor.guava.v32_1_2_jre.com.google.common.base.Preconditions.checkArgument;
    
    import com.google.api.services.bigquery.model.TableRow;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.clickhouse.options.BigQueryToClickHouseOptions;
    import com.google.cloud.teleport.v2.clickhouse.utils.ClickHouseUtils;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.transforms.BigQueryConverters;
    import java.util.ArrayList;
    import java.util.Map;
    import java.util.Objects;
    import java.util.stream.Collectors;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.clickhouse.ClickHouseIO;
    import org.apache.beam.sdk.io.clickhouse.TableSchema;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.schemas.Schema;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.Row;
    import org.joda.time.DateTime;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    @Template(
        name = "BigQuery_to_ClickHouse",
        category = TemplateCategory.BATCH,
        displayName = "BigQuery to ClickHouse",
        description =
            "The BigQuery to ClickHouse template is a batch pipeline that ingests data from a BigQuery table into ClickHouse table. "
                + "The template can either read the entire table or read specific records using a supplied query.",
        optionsClass = BigQueryToClickHouseOptions.class,
        skipOptions = {
          "javascriptTextTransformReloadIntervalMinutes",
          "pythonExternalTextTransformGcsPath",
          "pythonExternalTextTransformFunctionName"
        },
        flexContainerName = "googlecloud-to-clickhouse",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-clickhouse",
        contactInformation = "https://cloud.google.com/support",
        preview = true,
        requirements = {
          "The source BigQuery table must exist.",
          "The ClickHouse target table must exist prior running.",
          "This ClickHouse target table must have the exact same column names as the the source table/query."
        })
    public class BigQueryToClickHouse {
    
      private static final Logger log = LoggerFactory.getLogger(BigQueryToClickHouse.class);
    
      /**
       * Main entry point for pipeline execution.
       *
       * @param args Command line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        BigQueryToClickHouseOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(BigQueryToClickHouseOptions.class);
    
        run(options);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      private static PipelineResult run(BigQueryToClickHouseOptions options) {
        try {
          checkArgument(
              !options.getJdbcUrl().isEmpty(),
              "The ClickHouse JDBC url must have the following template: `jdbc:clickhouse://host:port/schema`");
          checkArgument(
              !options.getClickHouseTable().isEmpty(),
              "ClickHouse target table name is empty. Please provide a valid table name.");
    
          String clickHouseJDBCURL =
              ClickHouseUtils.setJDBCCredentials(
                  options.getJdbcUrl(),
                  options.getClickHouseUsername(),
                  options.getClickHousePassword());
          TableSchema clickHouseSchema =
              ClickHouseIO.getTableSchema(clickHouseJDBCURL, options.getClickHouseTable());
          Schema beamSchema = TableSchema.getEquivalentSchema(clickHouseSchema);
    
          // Create the pipeline.
          Pipeline pipeline = Pipeline.create(options);
    
          /*
           * Step #1: Read from BigQuery. If a query is provided then it is used to get the TableRows.
           */
          PCollection<TableRow> tableRows =
              pipeline.apply(
                  "Read From Big Query",
                  BigQueryConverters.ReadBigQueryTableRows.newBuilder()
                      .setOptions(options.as(BigQueryToClickHouseOptions.class))
                      .build());
    
          // Step 2: Transform TableRow to Row
          PCollection<Row> rows =
              tableRows
                  .apply(
                      "Convert to Beam Row",
                      ParDo.of(new TableRowToBeamRowFn(beamSchema, clickHouseSchema)))
                  .setRowSchema(beamSchema);
    
          ClickHouseIO.Write clickHouseWriter =
              ClickHouseIO.write(clickHouseJDBCURL, options.getClickHouseTable());
    
          if (options.getMaxInsertBlockSize() != null) {
            clickHouseWriter.withMaxInsertBlockSize(options.getMaxInsertBlockSize());
          }
          if (options.getInsertDistributedSync() != null) {
            clickHouseWriter.withInsertDistributedSync(options.getInsertDistributedSync());
          }
          if (options.getInsertQuorum() != null) {
            clickHouseWriter.withInsertQuorum(options.getInsertQuorum());
          }
          if (options.getInsertDeduplicate() != null) {
            clickHouseWriter.withInsertDeduplicate(options.getInsertDeduplicate());
          }
          if (options.getMaxRetries() != null) {
            clickHouseWriter.withMaxRetries(options.getMaxRetries());
          }
    
          // Step 3: Write data to ClickHouse
          rows.apply("Write to ClickHouse", clickHouseWriter);
    
          return pipeline.run();
        } catch (Exception e) {
          log.error("Error occurred during the BigQuery to ClickHouse template execution: ", e);
          throw new RuntimeException(e);
        }
      }
    }
    
    class TableRowToBeamRowFn extends DoFn<TableRow, Row> {
      private Map<String, TableSchema.Column> columnMap;
      private final Schema beamSchema;
      private final TableSchema clickHouseSchema;
    
      public TableRowToBeamRowFn(Schema beamSchema, TableSchema clickHouseSchema) {
        this.beamSchema = beamSchema;
        this.clickHouseSchema = clickHouseSchema;
      }
    
      @Setup
      public void setup() {
        columnMap =
            clickHouseSchema.columns().stream()
                .collect(Collectors.toMap(TableSchema.Column::name, column -> column));
      }
    
      @ProcessElement
      public void processElement(@Element TableRow tableRow, OutputReceiver<Row> out) {
        Row.Builder rowBuilder = Row.withSchema(beamSchema);
    
        for (Schema.Field field : beamSchema.getFields()) {
          String fieldName = field.getName();
          Object value = tableRow.get(fieldName);
          TableSchema.ColumnType columnType =
              columnMap.get(fieldName) != null ? columnMap.get(fieldName).columnType() : null;
    
          if (columnType == null) {
            throw new IllegalArgumentException("Couldn't infer type for field: " + fieldName);
          }
    
          if (value != null) {
            if (columnType.typeName() == TableSchema.ColumnType.FLOAT32.typeName()) {
              rowBuilder.addValue(Float.valueOf(value.toString()));
            } else if (columnType.typeName() == TableSchema.ColumnType.FLOAT64.typeName()) {
              rowBuilder.addValue(Double.valueOf(value.toString()));
            } else if (columnType.typeName() == TableSchema.ColumnType.DATETIME.typeName()
                || columnType.typeName() == TableSchema.ColumnType.DATE.typeName()) {
              rowBuilder.addValue(new DateTime(value.toString()));
            } else if (Objects.equals(columnType.typeName().toString(), "ARRAY")) {
              if (((ArrayList<?>) value).isEmpty()) {
                rowBuilder.addValue(value);
              } else {
                TableSchema.ColumnType finalColumnType = columnType;
                rowBuilder.addValue(
                    ((ArrayList<?>) value)
                        .stream()
                            .map(
                                v ->
                                    TableSchema.ColumnType.parseDefaultExpression(
                                        finalColumnType.arrayElementType(), v.toString()))
                            .collect(Collectors.toList()));
              }
            } else {
              rowBuilder.addValue(
                  TableSchema.ColumnType.parseDefaultExpression(columnType, value.toString()));
            }
          } else {
            rowBuilder.addValue(null);
          }
        }
    
        Row row = rowBuilder.build();
        out.output(row);
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
