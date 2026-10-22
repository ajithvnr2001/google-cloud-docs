---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-to-avro/
title: Bigtable to Cloud Storage Avro template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:46.964762+00:00
---

# Bigtable to Cloud Storage Avro template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-to-avro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Bigtable to Cloud Storage Avro template Stay organized with collections  Save and categorize content based on your preferences. 

The Bigtable to Cloud Storage Avro template is a pipeline that reads data from a Bigtable table and writes it to a Cloud Storage bucket in Avro format. You can use the template to move data from Bigtable to Cloud Storage.

## Pipeline requirements

  * The Bigtable table must exist.
  * The output Cloud Storage bucket must exist before running the pipeline.



## Template parameters

### Required parameters

  * **bigtableProjectId** : The ID of the Google Cloud project that contains the Bigtable instance that you want to read data from.
  * **bigtableInstanceId** : The ID of the Bigtable instance that contains the table.
  * **bigtableTableId** : The ID of the Bigtable table to export.
  * **outputDirectory** : The Cloud Storage path where data is written. For example, `gs://mybucket/somefolder`.
  * **filenamePrefix** : The prefix of the Avro filename. For example, `output-`. Defaults to: part.



### Optional parameters

  * **bigtableAppProfileId** : The ID of the Bigtable application profile to use for the export. If you don't specify an app profile, Bigtable uses the instance's default app profile: <https://cloud.google.com/bigtable/docs/app-profiles#default-app-profile>.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Cloud Bigtable to Avro Files on Cloud Storage** template .
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/Cloud_Bigtable_to_GCS_Avro \
        --region REGION_NAME \
        --parameters \
    bigtableProjectId=BIGTABLE_PROJECT_ID,\
    bigtableInstanceId=INSTANCE_ID,\
    bigtableTableId=TABLE_ID,\
    outputDirectory=OUTPUT_DIRECTORY,\
    filenamePrefix=FILENAME_PREFIX

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `BIGTABLE_PROJECT_ID`: the ID of the Google Cloud project of the Bigtable instance that you want to read data from
  * `INSTANCE_ID`: the ID of the Bigtable instance that contains the table
  * `TABLE_ID`: the ID of the Bigtable table to export
  * `OUTPUT_DIRECTORY`: the Cloud Storage path where data is written, for example, `gs://mybucket/somefolder`
  * `FILENAME_PREFIX`: the prefix of the Avro filename, for example, `output-`



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/Cloud_Bigtable_to_GCS_Avro
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "bigtableProjectId": "BIGTABLE_PROJECT_ID",
           "bigtableInstanceId": "INSTANCE_ID",
           "bigtableTableId": "TABLE_ID",
           "outputDirectory": "OUTPUT_DIRECTORY",
           "filenamePrefix": "FILENAME_PREFIX",
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
  * `BIGTABLE_PROJECT_ID`: the ID of the Google Cloud project of the Bigtable instance that you want to read data from
  * `INSTANCE_ID`: the ID of the Bigtable instance that contains the table
  * `TABLE_ID`: the ID of the Bigtable table to export
  * `OUTPUT_DIRECTORY`: the Cloud Storage path where data is written, for example, `gs://mybucket/somefolder`
  * `FILENAME_PREFIX`: the prefix of the Avro filename, for example, `output-`



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
    package com.google.cloud.teleport.bigtable;
    
    import com.google.bigtable.v2.Cell;
    import com.google.bigtable.v2.Column;
    import com.google.bigtable.v2.Family;
    import com.google.bigtable.v2.Row;
    import com.google.cloud.teleport.bigtable.BigtableToAvro.Options;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.util.DualInputNestedValueProvider;
    import com.google.cloud.teleport.util.DualInputNestedValueProvider.TranslatorInput;
    import com.google.protobuf.[ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.protobuf.[UnsafeByteOperations](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnsafeByteOperations.html);
    import java.io.IOException;
    import java.nio.ByteBuffer;
    import java.util.ArrayList;
    import java.util.List;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.[extensions](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.ExtendableMessage.html#com_google_protobuf_GeneratedMessageLite_ExtendableMessage_extensions).avro.io.AvroIO;
    import org.apache.beam.sdk.io.FileSystems;
    import org.apache.beam.sdk.io.fs.ResolveOptions.StandardResolveOptions;
    import org.apache.beam.sdk.io.gcp.bigtable.BigtableIO;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.SerializableFunction;
    import org.apache.beam.sdk.transforms.SimpleFunction;
    
    /**
     * Dataflow pipeline that exports data from a Cloud Bigtable table to Avro files in GCS. Currently,
     * filtering on Cloud Bigtable table is not supported.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Cloud_Bigtable_to_GCS_Avro.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Cloud_Bigtable_to_GCS_Avro",
        category = TemplateCategory.BATCH,
        displayName = "Cloud Bigtable to Avro Files in Cloud Storage",
        description =
            "The Bigtable to Cloud Storage Avro template is a pipeline that reads data from a Bigtable table and writes it to a Cloud Storage bucket in Avro format. "
                + "You can use the template to move data from Bigtable to Cloud Storage.",
        optionsClass = Options.class,
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-to-avro",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The Bigtable table must exist.",
          "The output Cloud Storage bucket must exist before running the pipeline."
        })
    public class BigtableToAvro {
    
      /** Options for the export pipeline. */
      public interface Options extends PipelineOptions {
        @TemplateParameter.ProjectId(
            order = 1,
            groupName = "Source",
            description = "Project ID",
            helpText =
                "The ID of the Google Cloud project that contains the Bigtable instance that you want to read data from.")
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
            helpText = "The ID of the Bigtable table to export.")
        ValueProvider<String> getBigtableTableId();
    
        @SuppressWarnings("unused")
        void setBigtableTableId(ValueProvider<String> tableId);
    
        @TemplateParameter.GcsWriteFolder(
            order = 4,
            groupName = "Target",
            description = "Output file directory in Cloud Storage",
            helpText = "The Cloud Storage path where data is written.",
            example = "gs://mybucket/somefolder")
        ValueProvider<String> getOutputDirectory();
    
        @SuppressWarnings("unused")
        void setOutputDirectory(ValueProvider<String> outputDirectory);
    
        @TemplateParameter.Text(
            order = 5,
            groupName = "Target",
            description = "Avro file prefix",
            helpText = "The prefix of the Avro filename. For example, `output-`.")
        @Default.String("part")
        ValueProvider<String> getFilenamePrefix();
    
        @SuppressWarnings("unused")
        void setFilenamePrefix(ValueProvider<String> filenamePrefix);
    
        @TemplateParameter.Text(
            order = 6,
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
       * Runs a pipeline to export data from a Cloud Bigtable table to Avro files in GCS.
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
    
        pipeline
            .apply("Read from Bigtable", read)
            .apply("Transform to Avro", MapElements.via(new BigtableToAvroFn()))
            .apply(
                "Write to Avro in GCS",
                AvroIO.write(BigtableRow.class).to(filePathPrefix).withSuffix(".avro"));
    
        return pipeline.[run](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.RpcCallback.html#com_google_protobuf_RpcCallback_run_ParameterType_)();
      }
    
      /** Translates Bigtable {@link Row} to Avro {@link BigtableRow}. */
      static class BigtableToAvroFn extends SimpleFunction<Row, BigtableRow> {
        @Override
        public BigtableRow apply(Row row) {
          ByteBuffer key = ByteBuffer.[wrap](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DiscardUnknownFieldsParser.html#com_google_protobuf_DiscardUnknownFieldsParser__T_wrap_com_google_protobuf_Parser_T__)(toByteArray(row.getKey()));
          List<BigtableCell> cells = new ArrayList<>();
          for (Family family : row.getFamiliesList()) {
            String familyName = family.getName();
            for (Column column : family.getColumnsList()) {
              ByteBuffer qualifier = ByteBuffer.[wrap](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DiscardUnknownFieldsParser.html#com_google_protobuf_DiscardUnknownFieldsParser__T_wrap_com_google_protobuf_Parser_T__)(toByteArray(column.getQualifier()));
              for (Cell cell : column.getCellsList()) {
                long timestamp = cell.getTimestampMicros();
                ByteBuffer value = ByteBuffer.[wrap](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DiscardUnknownFieldsParser.html#com_google_protobuf_DiscardUnknownFieldsParser__T_wrap_com_google_protobuf_Parser_T__)(toByteArray(cell.getValue()));
                cells.add(new BigtableCell(familyName, qualifier, timestamp, value));
              }
            }
          }
          return new BigtableRow(key, cells);
        }
      }
    
      /**
       * Extracts the byte array from the given {@link ByteString} without copy.
       *
       * @param byteString A {@link ByteString} from which to extract the array.
       * @return an array of byte.
       */
      protected static byte[] toByteArray(final [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) byteString) {
        try {
          ZeroCopyByteOutput byteOutput = new ZeroCopyByteOutput();
          [UnsafeByteOperations](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnsafeByteOperations.html).[unsafeWriteTo](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnsafeByteOperations.html#com_google_protobuf_UnsafeByteOperations_unsafeWriteTo_com_google_protobuf_ByteString_com_google_protobuf_ByteOutput_)(byteString, byteOutput);
          return byteOutput.bytes;
        } catch (IOException e) {
          return byteString.[toByteArray](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_toByteArray__)();
        }
      }
    
      private static final class ZeroCopyByteOutput extends [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput.html) {
        private byte[] bytes;
    
        @Override
        public void writeLazy(byte[] value, int offset, int length) {
          if (offset != 0 || length != value.length) {
            throw new UnsupportedOperationException();
          }
          bytes = value;
        }
    
        @Override
        public void write(byte value) {
          throw new UnsupportedOperationException();
        }
    
        @Override
        public void write(byte[] value, int offset, int length) {
          throw new UnsupportedOperationException();
        }
    
        @Override
        public void write(ByteBuffer value) {
          throw new UnsupportedOperationException();
        }
    
        @Override
        public void writeLazy(ByteBuffer value) {
          throw new UnsupportedOperationException();
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
