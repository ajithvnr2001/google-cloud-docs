---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-to-json/
title: Bigtable to JSON template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:48.032955+00:00
---

# Bigtable to JSON template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-to-json/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Bigtable to JSON template Stay organized with collections  Save and categorize content based on your preferences. 

The Bigtable to JSON template is a pipeline that reads data from a Bigtable table and writes it to a Cloud Storage bucket in the JSON format.

## Pipeline requirements

  * The Bigtable table must exist.
  * The output Cloud Storage bucket must exist before you run the pipeline.



## Template parameters

### Required parameters

  * **bigtableProjectId** : The ID for the Google Cloud project that contains the Bigtable instance that you want to read data from.
  * **bigtableInstanceId** : The ID of the Bigtable instance that contains the table.
  * **bigtableTableId** : The ID of the Bigtable table to read from.
  * **outputDirectory** : The Cloud Storage path where the output JSON files are stored. For example, `gs://your-bucket/your-path/`.



### Optional parameters

  * **filenamePrefix** : The prefix of the JSON file name. For example, `table1-`. If no value is provided, defaults to `part`.
  * **userOption** : Possible values are `FLATTEN` or `NONE`. `FLATTEN` flattens the row to the single level. `NONE` stores the whole row as a JSON string. Defaults to `NONE`.
  * **columnsAliases** : A comma-separated list of columns that are required for the Vertex AI Vector Search index. The columns `id` and `embedding` are required for Vertex AI Vector Search. You can use the notation `fromfamily:fromcolumn;to`. For example, if the columns are `rowkey` and `cf:my_embedding`, where `rowkey` has a different name than the embedding column, specify `cf:my_embedding;embedding` and, `rowkey;id`. Only use this option when the value for `userOption` is `FLATTEN`.
  * **bigtableAppProfileId** : The ID of the Bigtable application profile to use for the export. If you don't specify an app profile, Bigtable uses the instance's default app profile: <https://cloud.google.com/bigtable/docs/app-profiles#default-app-profile>.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Bigtable to JSON** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud CLI

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location=gs://dataflow-templates/VERSION/Cloud_Bigtable_to_GCS_Json \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --parameters \
           bigtableProjectId=BIGTABLE_PROJECT_ID,\
           bigtableInstanceId=BIGTABLE_INSTANCE_ID,\
           bigtableTableId=BIGTABLE_TABLE_ID,\
           filenamePrefix=FILENAME_PREFIX,\

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `BIGTABLE_PROJECT_ID`: the Project ID
  * `BIGTABLE_INSTANCE_ID`: the Instance ID
  * `BIGTABLE_TABLE_ID`: the Table ID
  * `FILENAME_PREFIX`: the JSON file prefix



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/Cloud_Bigtable_to_GCS_Json
    {
       "jobName": "JOB_NAME",
       "parameters": {
         "bigtableProjectId": "BIGTABLE_PROJECT_ID",
         "bigtableInstanceId": "BIGTABLE_INSTANCE_ID",
         "bigtableTableId": "BIGTABLE_TABLE_ID",
         "filenamePrefix": "FILENAME_PREFIX",
       },
       "environment": { "maxWorkers": "10" }
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
  * `BIGTABLE_PROJECT_ID`: the Project ID
  * `BIGTABLE_INSTANCE_ID`: the Instance ID
  * `BIGTABLE_TABLE_ID`: the Table ID
  * `FILENAME_PREFIX`: the JSON file prefix



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
    package com.google.cloud.teleport.bigtable;
    
    import com.google.bigtable.v2.Cell;
    import com.google.bigtable.v2.Column;
    import com.google.bigtable.v2.Family;
    import com.google.bigtable.v2.Row;
    import com.google.cloud.teleport.bigtable.BigtableToJson.Options;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.metadata.TemplateParameter.TemplateEnumOption;
    import com.google.cloud.teleport.util.DualInputNestedValueProvider;
    import com.google.cloud.teleport.util.DualInputNestedValueProvider.TranslatorInput;
    import com.google.gson.stream.JsonWriter;
    import java.io.IOException;
    import java.io.StringWriter;
    import java.util.HashMap;
    import java.util.Map;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.FileSystems;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.io.fs.ResolveOptions.StandardResolveOptions;
    import org.apache.beam.sdk.io.gcp.bigtable.BigtableIO;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.SerializableFunction;
    import org.apache.beam.sdk.transforms.SimpleFunction;
    import org.apache.commons.lang3.StringUtils;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * Dataflow pipeline that exports data from a Cloud Bigtable table to JSON files in GCS. Currently,
     * filtering on Cloud Bigtable table is not supported.
     *
     * <p>Check out <a href=
     * "https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Cloud_Bigtable_to_GCS_JSON.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Cloud_Bigtable_to_GCS_Json",
        category = TemplateCategory.BATCH,
        displayName = "Cloud Bigtable to JSON",
        description =
            "The Bigtable to JSON template is a pipeline that reads data from a Bigtable table and writes it to a Cloud Storage bucket in JSON format",
        optionsClass = Options.class,
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-to-json",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The Bigtable table must exist.",
          "The output Cloud Storage bucket must exist before running the pipeline."
        })
    public class BigtableToJson {
      private static final Logger LOG = LoggerFactory.getLogger(BigtableToJson.class);
    
      /** Options for the export pipeline. */
      public interface Options extends PipelineOptions {
        @TemplateParameter.ProjectId(
            order = 1,
            groupName = "Source",
            description = "Project ID",
            helpText =
                "The ID for the Google Cloud project that contains the Bigtable instance that you want to read data from.")
        ValueProvider<String> getBigtableProjectId();
    
        @SuppressWarnings("unused")
        void setBigtableProjectId(ValueProvider<String> projectId);
    
        @TemplateParameter.Text(
            order = 2,
            groupName = "Source",
            regexes = {"[a-z][a-z0-9\\-]+[a-z0-9]"},
            description = "Instance ID",
            helpText = "The ID of the Bigtable instance that contains the table.")
        ValueProvider<String> getBigtableInstanceId();
    
        @SuppressWarnings("unused")
        void setBigtableInstanceId(ValueProvider<String> instanceId);
    
        @TemplateParameter.Text(
            order = 3,
            groupName = "Source",
            regexes = {"[_a-zA-Z0-9][-_.a-zA-Z0-9]*"},
            description = "Table ID",
            helpText = "The ID of the Bigtable table to read from.")
        ValueProvider<String> getBigtableTableId();
    
        @SuppressWarnings("unused")
        void setBigtableTableId(ValueProvider<String> tableId);
    
        @TemplateParameter.GcsWriteFolder(
            order = 4,
            groupName = "Target",
            description = "Cloud Storage directory for storing JSON files",
            helpText = "The Cloud Storage path where the output JSON files are stored.",
            example = "gs://your-bucket/your-path/")
        @Required
        ValueProvider<String> getOutputDirectory();
    
        @SuppressWarnings("unused")
        void setOutputDirectory(ValueProvider<String> outputDirectory);
    
        @TemplateParameter.Text(
            order = 5,
            groupName = "Target",
            optional = true,
            description = "JSON file prefix",
            helpText =
                "The prefix of the JSON file name. For example, `table1-`. If no value is provided, defaults to `part`.")
        @Default.String("part")
        ValueProvider<String> getFilenamePrefix();
    
        @SuppressWarnings("unused")
        void setFilenamePrefix(ValueProvider<String> filenamePrefix);
    
        @TemplateParameter.Enum(
            order = 6,
            groupName = "Target",
            optional = true,
            enumOptions = {@TemplateEnumOption("FLATTEN"), @TemplateEnumOption("NONE")},
            description = "User option",
            helpText =
                "Possible values are `FLATTEN` or `NONE`. `FLATTEN` flattens the row to the single level. `NONE` stores the whole row as a JSON string. Defaults to `NONE`.")
        @Default.String("NONE")
        String getUserOption();
    
        @SuppressWarnings("unused")
        void setUserOption(String userOption);
    
        @TemplateParameter.Text(
            order = 7,
            groupName = "Target",
            optional = true,
            parentName = "userOption",
            parentTriggerValues = {"FLATTEN"},
            description = "Columns aliases",
            helpText =
                "A comma-separated list of columns that are required for the Vertex AI Vector Search index. The"
                    + " columns `id` and `embedding` are required for Vertex AI Vector Search. You can use the notation"
                    + " `fromfamily:fromcolumn;to`. For example, if the columns are `rowkey` and `cf:my_embedding`, where"
                    + " `rowkey` has a different name than the embedding column, specify `cf:my_embedding;embedding` and,"
                    + " `rowkey;id`. Only use this option when the value for `userOption` is `FLATTEN`.")
        ValueProvider<String> getColumnsAliases();
    
        @SuppressWarnings("unused")
        void setColumnsAliases(ValueProvider<String> value);
    
        @TemplateParameter.Text(
            order = 8,
            groupName = "Source",
            optional = true,
            regexes = {"[_a-zA-Z0-9][-_.a-zA-Z0-9]*"},
            description = "Application profile ID",
            helpText =
                "The ID of the Bigtable application profile to use for the export. If you don't specify an app profile, Bigtable uses the instance's default app profile: https://cloud.google.com/bigtable/docs/app-profiles#default-app-profile.")
        @Default.String("default")
        ValueProvider<String> getBigtableAppProfileId();
    
        @SuppressWarnings("unused")
        void setBigtableAppProfileId(ValueProvider<String> appProfileId);
      }
    
      /**
       * Runs a pipeline to export data from a Cloud Bigtable table to JSON files in GCS in JSON format.
       *
       * @param args arguments to the pipeline
       */
      public static void main(String[] args) {
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
    
        PipelineResult result = run(options);
    
        // Wait for pipeline to finish only if it is not constructing a template.
        if (options.as(DataflowPipelineOptions.class).getTemplateLocation() == null) {
          result.waitUntilFinish();
        }
        LOG.info("Completed pipeline setup");
      }
    
      public static PipelineResult run(Options options) {
        Pipeline pipeline = Pipeline.create(PipelineUtils.tweakPipelineOptions(options));
    
        BigtableIO.Read read =
            BigtableIO.read()
                .withProjectId(options.getBigtableProjectId())
                .withInstanceId(options.getBigtableInstanceId())
                .withAppProfileId(options.getBigtableAppProfileId())
                .withTableId(options.getBigtableTableId());
    
        // Do not validate input fields if it is running as a template.
        if (options.as(DataflowPipelineOptions.class).getTemplateLocation() != null) {
          read = read.withoutValidation();
        }
    
        ValueProvider<String> filePathPrefix =
            DualInputNestedValueProvider.of(
                options.getOutputDirectory(),
                options.getFilenamePrefix(),
                new SerializableFunction<TranslatorInput<String, String>, String>() {
                  @Override
                  public String apply(TranslatorInput<String, String> input) {
                    return FileSystems.matchNewResource(input.getX(), true)
                        .resolve(input.getY(), StandardResolveOptions.RESOLVE_FILE)
                        .toString();
                  }
                });
    
        String userOption = options.getUserOption();
        pipeline
            .apply("Read from Bigtable", read)
            .apply(
                "Transform to JSON",
                MapElements.via(
                    new BigtableToJsonFn(userOption.equals("FLATTEN"), options.getColumnsAliases())))
            .apply("Write to storage", TextIO.write().to(filePathPrefix).withSuffix(".json"));
    
        return pipeline.run();
      }
    
      /** Translates Bigtable {@link Row} to JSON. */
      static class BigtableToJsonFn extends SimpleFunction<Row, String> {
        private boolean flatten;
        private ValueProvider<String> columnsAliases;
    
        public BigtableToJsonFn(boolean flatten, ValueProvider<String> columnsAliases) {
          this.flatten = flatten;
          this.columnsAliases = columnsAliases;
        }
    
        @Override
        public String apply(Row row) {
          StringWriter stringWriter = new StringWriter();
          JsonWriter jsonWriter = new JsonWriter(stringWriter);
          try {
            if (flatten) {
              serializeFlattented(row, jsonWriter);
            } else {
              serializeUnFlattented(row, jsonWriter);
            }
          } catch (IOException e) {
            throw new RuntimeException(e);
          }
          return stringWriter.toString();
        }
    
        private void serializeUnFlattented(Row row, JsonWriter jsonWriter) throws IOException {
          jsonWriter.beginObject();
          jsonWriter.name(row.getKey().toStringUtf8());
          jsonWriter.beginObject();
          for (Family family : row.getFamiliesList()) {
            String familyName = family.getName();
            jsonWriter.name(familyName);
            jsonWriter.beginObject();
            for (Column column : family.getColumnsList()) {
              for (Cell cell : column.getCellsList()) {
                jsonWriter
                    .name(column.getQualifier().toStringUtf8())
                    .value(cell.getValue().toStringUtf8());
              }
            }
            jsonWriter.endObject();
          }
          jsonWriter.endObject();
          jsonWriter.endObject();
        }
    
        private void serializeFlattented(Row row, JsonWriter jsonWriter) throws IOException {
          jsonWriter.beginObject();
          Map<String, String> columnsWithAliases = extractColumnsAliases();
    
          maybeAddToJson(jsonWriter, columnsWithAliases, "rowkey", row.getKey().toStringUtf8());
          for (Family family : row.getFamiliesList()) {
            String familyName = family.getName();
            for (Column column : family.getColumnsList()) {
              for (Cell cell : column.getCellsList()) {
                maybeAddToJson(
                    jsonWriter,
                    columnsWithAliases,
                    familyName + ":" + column.getQualifier().toStringUtf8(),
                    cell.getValue().toStringUtf8());
              }
            }
          }
          jsonWriter.endObject();
        }
    
        private void maybeAddToJson(
            JsonWriter jsonWriter, Map<String, String> columnsWithAliases, String key, String value)
            throws IOException {
          if (!columnsWithAliases.isEmpty() && !columnsWithAliases.containsKey(key)) {
            return;
          }
          jsonWriter.name(columnsWithAliases.getOrDefault(key, key)).value(value);
        }
    
        private Map<String, String> extractColumnsAliases() {
          Map<String, String> columnsWithAliases = new HashMap<>();
          if (StringUtils.isBlank(columnsAliases.get())) {
            return columnsWithAliases;
          }
          String[] columnsList = columnsAliases.get().split(",");
    
          for (String columnsWithAlias : columnsList) {
            String[] columnWithAlias = columnsWithAlias.split(";");
            if (columnWithAlias.length == 2) {
              columnsWithAliases.put(columnWithAlias[0], columnWithAlias[1]);
            }
          }
          return columnsWithAliases;
        }
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
