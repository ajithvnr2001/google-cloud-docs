---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-csv-to-bigquery/
title: Cloud Storage CSV files to BigQuery template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:46.545694+00:00
---

# Cloud Storage CSV files to BigQuery template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-csv-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Cloud Storage CSV files to BigQuery template Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage CSV files to BigQuery pipeline is a batch pipeline that lets you read data from CSV files stored in Cloud Storage and append the result to a BigQuery table. The CSV files can be uncompressed or compressed in formats listed in the [`Compression` Enum SDK page](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/Compression.html). 

**Note:** If you want to overwrite data in the BigQuery table instead of appending, in the template source code, update `WriteDisposition` from `WRITE_APPEND` to `WRITE_TRUNCATE`.

## Pipeline requirements

To use this template, your pipeline must meet the following requirements.

### BigQuery schema JSON file

Create a JSON file that describes your BigQuery schema. Ensure that the schema has a top-level JSON array titled `BigQuery Schema` and that its contents follow the pattern `{"name": "COLUMN_NAME", "type": "DATA_TYPE"}`.

The Cloud Storage CSV files to BigQuery batch template doesn't support importing data into [`STRUCT` (Record)](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type) fields in the target BigQuery table.

The following JSON describes an example BigQuery schema:
    
    
    {
      "BigQuery Schema": [
        {
          "name": "location",
          "type": "STRING"
        },
        {
          "name": "name",
          "type": "STRING"
        },
        {
          "name": "age",
          "type": "STRING"
        },
        {
          "name": "color",
          "type": "STRING"
        },
        {
          "name": "coffee",
          "type": "STRING"
        }
      ]
    }

### Error table schema

The BigQuery table that stores the rejected records from CSV files must match the table schema defined here.
    
    
    {
      "BigQuery Schema": [
        {
          "name": "RawContent",
          "type": "STRING"
        },
        {
          "name": "ErrorMsg",
          "type": "STRING"
        }
      ]
    }

## Template parameters

### Required parameters

  * **inputFilePattern** : The Cloud Storage path to the CSV file that contains the text to process. For example, `gs://your-bucket/path/*.csv`.
  * **schemaJSONPath** : The Cloud Storage path to the JSON file that defines your BigQuery schema.
  * **outputTable** : The name of the BigQuery table that stores your processed data. If you reuse an existing BigQuery table, the data is appended to the destination table.
  * **bigQueryLoadingTemporaryDirectory** : The temporary directory to use during the BigQuery loading process. For example, `gs://your-bucket/your-files/temp_dir`.
  * **badRecordsOutputTable** : The name of the BigQuery table to use to store the rejected data when processing the CSV files. If you reuse an existing BigQuery table, the data is appended to the destination table. The schema of this table must match the error table schema (<https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-csv-to-bigquery#GcsCSVToBigQueryBadRecordsSchema>).
  * **delimiter** : The column delimiter that the CSV file uses. For example, `,`.
  * **csvFormat** : The CSV format according to Apache Commons CSV format. Defaults to: `Default`.



### Optional parameters

  * **containsHeaders** : Whether headers are included in the CSV file. Defaults to: `false`.
  * **csvFileEncoding** : The CSV file character encoding format. Allowed Values are `US-ASCII`, `ISO-8859-1`, `UTF-8`, and `UTF-16`. Defaults to: UTF-8.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **CSV files on Cloud Storage to BigQuery** (Batch) template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/GCS_CSV_to_BigQuery \
        --region REGION_NAME \
        --parameters \
    inputFilePattern=PATH_TO_CSV_DATA,\
    schemaJSONPath=PATH_TO_BIGQUERY_SCHEMA_JSON,\
    outputTable=BIGQUERY_DESTINATION_TABLE,\
    badRecordsOutputTable=BIGQUERY_BAD_RECORDS_TABLE,\
    csvFormat=CSV_FORMAT,\
    delimiter=DELIMITER,\
    bigQueryLoadingTemporaryDirectory=PATH_TO_TEMP_DIR_ON_GCS,\
    containsHeaders=CONTAINS_HEADERS,\
    csvFileEncoding=CSV_FILE_ENCODING

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `PATH_TO_CSV_DATA`: the Cloud Storage path to your CSV files
  * `PATH_TO_BIGQUERY_SCHEMA_JSON`: the Cloud Storage path to the JSON file containing the schema definition
  * `BIGQUERY_DESTINATION_TABLE`: the BigQuery destination table name
  * `BIGQUERY_BAD_RECORDS_TABLE`: the BigQuery bad records table name
  * `PATH_TO_TEMP_DIR_ON_GCS`: the Cloud Storage path to the temp directory
  * `DELIMITER`: CSV file delimiter
  * `CSV_FORMAT`: CSV format specification for parsing records
  * `CONTAINS_HEADERS`: whether the CSV files contains headers
  * `CSV_FILE_ENCODING`: encoding in the CSV files



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/GCS_CSV_to_BigQuery
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "inputFilePattern":"PATH_TO_CSV_DATA",
           "schemaJSONPath": "PATH_TO_BIGQUERY_SCHEMA_JSON",
           "outputTable":"BIGQUERY_DESTINATION_TABLE",
           "badRecordsOutputTable":"BIGQUERY_BAD_RECORDS_TABLE",
           "csvFormat":"CSV_FORMAT",
           "delimiter":"DELIMITER",
           "bigQueryLoadingTemporaryDirectory": "PATH_TO_TEMP_DIR_ON_GCS",
           "containsHeaders": "CONTAINS_HEADERS",
           "csvFileEncoding": "CSV_FILE_ENCODING"
       },
       "environment": { "zone": "us-central1-f" }
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
  * `PATH_TO_CSV_DATA`: the Cloud Storage path to your CSV files
  * `PATH_TO_BIGQUERY_SCHEMA_JSON`: the Cloud Storage path to the JSON file containing the schema definition
  * `BIGQUERY_DESTINATION_TABLE`: the BigQuery destination table name
  * `BIGQUERY_BAD_RECORDS_TABLE`: the BigQuery bad records table name
  * `PATH_TO_TEMP_DIR_ON_GCS`: the Cloud Storage path to the temp directory
  * `DELIMITER`: CSV file delimiter
  * `CSV_FORMAT`: CSV format specification for parsing records
  * `CONTAINS_HEADERS`: whether the CSV files contains headers
  * `CSV_FILE_ENCODING`: encoding in the CSV files



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
    package com.google.cloud.teleport.templates;
    
    import com.google.api.services.bigquery.model.TableFieldSchema;
    import com.google.api.services.bigquery.model.TableRow;
    import com.google.api.services.bigquery.model.TableSchema;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.templates.CSVToBigQuery.Options;
    import com.google.cloud.teleport.templates.common.CsvConverters;
    import com.google.cloud.teleport.templates.common.CsvConverters.CsvPipelineOptions;
    import com.google.common.collect.ImmutableList;
    import java.util.ArrayList;
    import java.util.List;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.WriteDisposition;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.options.ValueProvider.NestedValueProvider;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.TupleTag;
    import org.apache.beam.sdk.values.TupleTagList;
    import org.json.JSONArray;
    import org.json.JSONObject;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * Templated pipeline to read CSV files from Cloud Storage, and write it to BigQuery.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_GCS_CSV_to_BigQuery.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "GCS_CSV_to_BigQuery",
        category = TemplateCategory.BATCH,
        displayName = "CSV Files on Cloud Storage to BigQuery",
        description =
            "The Cloud Storage CSV to BigQuery pipeline is a batch pipeline that allows you to read CSV files stored in "
                + "Cloud Storage, and append the result to a BigQuery table. The CSV files can be uncompressed or compressed in formats listed in https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/Compression.html.",
        optionsClass = Options.class,
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "Create a JSON file that describes your {{bigquery_name_short}} schema.\n"
              + "    <p>Ensure that there is a top-level JSON array titled <code>BigQuery Schema</code> and that its\n"
              + "      contents follow the pattern <code>{\"name\": \"COLUMN_NAME\", \"type\": \"DATA_TYPE\"}</code>.</p>\n"
              + "    <p>The following JSON describes an example BigQuery schema:</p>\n"
              + "<pre class=\"prettyprint lang-json\">\n"
              + "{\n"
              + "  \"BigQuery Schema\": [\n"
              + "    {\n"
              + "      \"name\": \"location\",\n"
              + "      \"type\": \"STRING\"\n"
              + "    },\n"
              + "    {\n"
              + "      \"name\": \"name\",\n"
              + "      \"type\": \"STRING\"\n"
              + "    },\n"
              + "    {\n"
              + "      \"name\": \"age\",\n"
              + "      \"type\": \"STRING\"\n"
              + "    },\n"
              + "    {\n"
              + "      \"name\": \"color\",\n"
              + "      \"type\": \"STRING\"\n"
              + "    },\n"
              + "    {\n"
              + "      \"name\": \"coffee\",\n"
              + "      \"type\": \"STRING\"\n"
              + "    }\n"
              + "  ]\n"
              + "}\n"
        })
    public class CSVToBigQuery {
    
      /** Options supported by {@link CSVToBigQuery}. */
      public interface Options extends DataflowPipelineOptions, CsvPipelineOptions {
    
        @TemplateParameter.Text(
            order = 1,
            groupName = "Source",
            description = "Cloud Storage Input File(s)",
            helpText = "The Cloud Storage path to the CSV file that contains the text to process.",
            regexes = {"^gs:\\/\\/[^\\n\\r]+$"},
            example = "gs://your-bucket/path/*.csv")
        ValueProvider<String> getInputFilePattern();
    
        void setInputFilePattern(ValueProvider<String> value);
    
        @TemplateParameter.GcsReadFile(
            order = 2,
            groupName = "Target",
            description = "Cloud Storage location of your BigQuery schema file, described as a JSON",
            helpText = "The Cloud Storage path to the JSON file that defines your BigQuery schema.")
        ValueProvider<String> getSchemaJSONPath();
    
        void setSchemaJSONPath(ValueProvider<String> value);
    
        @TemplateParameter.BigQueryTable(
            order = 3,
            groupName = "Target",
            description = "BigQuery output table",
            helpText =
                "The name of the BigQuery table that stores your processed data. If you reuse an existing "
                    + "BigQuery table, the data is appended to the destination table.")
        ValueProvider<String> getOutputTable();
    
        void setOutputTable(ValueProvider<String> value);
    
        @TemplateParameter.GcsWriteFolder(
            order = 4,
            description = "Temporary directory for BigQuery loading process",
            helpText = "The temporary directory to use during the BigQuery loading process.",
            example = "gs://your-bucket/your-files/temp_dir")
        @Validation.Required
        ValueProvider<String> getBigQueryLoadingTemporaryDirectory();
    
        void setBigQueryLoadingTemporaryDirectory(ValueProvider<String> directory);
    
        @TemplateParameter.BigQueryTable(
            order = 5,
            description = "BigQuery output table for bad records",
            helpText =
                "The name of the BigQuery table to use to store the rejected data when processing the"
                    + " CSV files. If you reuse an existing BigQuery table, the data is appended to the"
                    + " destination table. The schema of this table must match the"
                    + " error table schema (https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-csv-to-bigquery#GcsCSVToBigQueryBadRecordsSchema).")
        ValueProvider<String> getBadRecordsOutputTable();
    
        void setBadRecordsOutputTable(ValueProvider<String> value);
      }
    
      private static final Logger LOG = LoggerFactory.getLogger(CSVToBigQuery.class);
    
      private static final String BIGQUERY_SCHEMA = "BigQuery Schema";
      private static final String NAME = "name";
      private static final String TYPE = "type";
      private static final String MODE = "mode";
      private static final String RECORD_TYPE = "RECORD";
      private static final String FIELDS_ENTRY = "fields";
    
      /** The tag for the headers of the CSV if required. */
      private static final TupleTag<Iterable<String>> CSV_HEADERS = new TupleTag<Iterable<String>>() {};
    
      /** The tag for the lines of the CSV. */
      private static final TupleTag<Iterable<String>> CSV_LINES = new TupleTag<Iterable<String>>() {};
    
      /** The tag for the line of the CSV that matches destination table schema. */
      private static final TupleTag<TableRow> GOOD_RECORDS = new TupleTag<TableRow>() {};
    
      /** The tag for the lines of the CSV that does not match destination table schema. */
      private static final TupleTag<TableRow> BAD_RECORDS = new TupleTag<TableRow>() {};
    
      /** The schema of the BigQuery table for the bad records. */
      private static final TableSchema errorTableSchema =
          new TableSchema()
              .setFields(
                  ImmutableList.of(
                      new TableFieldSchema().setName("RawContent").setType("STRING"),
                      new TableFieldSchema().setName("ErrorMsg").setType("STRING")));
    
      private static class StringListToTableRowFn extends DoFn<Iterable<String>, TableRow> {
        private final ValueProvider<String> delimiter;
        private final NestedValueProvider<List<String>, String> fields;
    
        public StringListToTableRowFn(
            NestedValueProvider<List<String>, String> schemaFields, ValueProvider<String> delimiter) {
          this.delimiter = delimiter;
          this.fields = schemaFields;
        }
    
        @ProcessElement
        public void processElement(ProcessContext context) throws IllegalArgumentException {
          TableRow outputTableRow = new TableRow();
          String[] rowValue = ImmutableList.copyOf(context.element()).toArray(new String[0]);
          if (rowValue.length != fields.get().size()) {
            LOG.error("Number of fields in the schema and number of Csv headers do not match.");
            outputTableRow.set("RawContent", String.join(delimiter.get(), rowValue));
            outputTableRow.set(
                "ErrorMsg", "Number of fields in the schema and number of Csv headers do not match.");
            context.output(BAD_RECORDS, outputTableRow);
          } else {
            for (int i = 0; i < fields.get().size(); ++i) {
              outputTableRow.set(fields.get().get(i), rowValue[i]);
            }
            context.output(GOOD_RECORDS, outputTableRow);
          }
        }
      }
    
      public static void main(String[] args) {
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        Pipeline pipeline = Pipeline.create(options);
    
        PCollectionTuple tableRows =
            pipeline
                .apply(
                    "ReadCsvFile",
                    CsvConverters.ReadCsv.newBuilder()
                        .setInputFileSpec(options.getInputFilePattern())
                        .setHasHeaders(options.getContainsHeaders())
                        .setHeaderTag(CSV_HEADERS)
                        .setLineTag(CSV_LINES)
                        .setCsvFormat(options.getCsvFormat())
                        .setDelimiter(options.getDelimiter())
                        .setFileEncoding(options.getCsvFileEncoding())
                        .build())
                .get(CSV_LINES)
                .apply(
                    "ConvertToTableRow",
                    ParDo.of(
                            new StringListToTableRowFn(
                                NestedValueProvider.of(
                                    options.getSchemaJSONPath(),
                                    jsonPath -> {
                                      List<String> fields = new ArrayList<>();
                                      SchemaParser schemaParser = new SchemaParser();
    
                                      try {
                                        JSONObject jsonSchema = schemaParser.parseSchema(jsonPath);
                                        JSONArray bqSchemaJsonArray =
                                            jsonSchema.getJSONArray(BIGQUERY_SCHEMA);
    
                                        for (int i = 0; i < bqSchemaJsonArray.length(); i++) {
                                          JSONObject inputField = bqSchemaJsonArray.getJSONObject(i);
                                          fields.add(inputField.getString(NAME));
                                        }
    
                                      } catch (Exception e) {
                                        throw new RuntimeException(
                                            "Error parsing schema " + jsonPath, e);
                                      }
                                      return fields;
                                    }),
                                options.getDelimiter()))
                        .withOutputTags(GOOD_RECORDS, TupleTagList.of(BAD_RECORDS)));
    
        tableRows
            .get(GOOD_RECORDS)
            .apply(
                "Insert good records into Bigquery",
                BigQueryIO.writeTableRows()
                    .withSchema(
                        NestedValueProvider.of(
                            options.getSchemaJSONPath(),
                            schemaPath -> {
                              TableSchema tableSchema = new TableSchema();
                              List<TableFieldSchema> fields = new ArrayList<>();
                              SchemaParser schemaParser = new SchemaParser();
    
                              try {
                                JSONObject jsonSchema = schemaParser.parseSchema(schemaPath);
                                JSONArray bqSchemaJsonArray = jsonSchema.getJSONArray(BIGQUERY_SCHEMA);
    
                                for (int i = 0; i < bqSchemaJsonArray.length(); i++) {
                                  JSONObject inputField = bqSchemaJsonArray.getJSONObject(i);
                                  fields.add(convertToTableFieldSchema(inputField));
                                }
                                tableSchema.setFields(fields);
    
                              } catch (Exception e) {
                                throw new RuntimeException("Error parsing schema " + schemaPath, e);
                              }
                              return tableSchema;
                            }))
                    .to(options.getOutputTable())
                    .withCreateDisposition(CreateDisposition.CREATE_IF_NEEDED)
                    .withWriteDisposition(WriteDisposition.WRITE_APPEND)
                    .withCustomGcsTempLocation(options.getBigQueryLoadingTemporaryDirectory()));
    
        tableRows
            .get(BAD_RECORDS)
            .apply(
                "Insert bad records into Bigquery",
                BigQueryIO.writeTableRows()
                    .withSchema(errorTableSchema)
                    .to(options.getBadRecordsOutputTable())
                    .withCreateDisposition(CreateDisposition.CREATE_IF_NEEDED)
                    .withWriteDisposition(WriteDisposition.WRITE_APPEND)
                    .withCustomGcsTempLocation(options.getBigQueryLoadingTemporaryDirectory()));
    
        pipeline.run();
      }
    
      /**
       * Convert a JSONObject from the Schema JSON to a TableFieldSchema. In case of RECORD, it handles
       * the conversion recursively.
       *
       * @param inputField Input field to convert.
       * @return TableFieldSchema instance to populate the schema.
       */
      private static TableFieldSchema convertToTableFieldSchema(JSONObject inputField) {
        TableFieldSchema field =
            new TableFieldSchema()
                .setName(inputField.getString(NAME))
                .setType(inputField.getString(TYPE));
    
        if (inputField.has(MODE)) {
          field.setMode(inputField.getString(MODE));
        }
    
        if (inputField.getString(TYPE) != null && inputField.getString(TYPE).equals(RECORD_TYPE)) {
          List<TableFieldSchema> nestedFields = new ArrayList<>();
          JSONArray fieldsArr = inputField.getJSONArray(FIELDS_ENTRY);
          for (int i = 0; i < fieldsArr.length(); i++) {
            JSONObject nestedJSON = fieldsArr.getJSONObject(i);
            nestedFields.add(convertToTableFieldSchema(nestedJSON));
          }
          field.setFields(nestedFields);
        }
    
        return field;
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
