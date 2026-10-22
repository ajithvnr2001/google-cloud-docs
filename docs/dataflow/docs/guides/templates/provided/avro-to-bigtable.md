---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-bigtable/
title: Cloud Storage Avro to Bigtable template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:08.219752+00:00
---

# Cloud Storage Avro to Bigtable template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-bigtable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Cloud Storage Avro to Bigtable template Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage Avro to Bigtable template is a pipeline that reads data from Avro files in a Cloud Storage bucket and writes the data to a Bigtable table. You can use the template to copy data from Cloud Storage to Bigtable.

## Pipeline requirements

  * The Bigtable table must exist and have the same column families as exported in the Avro files.
  * The input Avro files must exist in a Cloud Storage bucket before running the pipeline.
  * Bigtable expects a specific [ schema](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/src/main/resources/schema/avro/bigtable.avsc) from the input Avro files.



## Template parameters

### Required parameters

  * **bigtableProjectId** : The ID of the Google Cloud project that contains the Bigtable instance that you want to write data to.
  * **bigtableInstanceId** : The ID of the Bigtable instance that contains the table.
  * **bigtableTableId** : The ID of the Bigtable table to import.
  * **inputFilePattern** : The Cloud Storage path pattern where data is located. For example, `gs://<BUCKET_NAME>/FOLDER/PREFIX*`.



### Optional parameters

  * **splitLargeRows** : The flag for enabling splitting of large rows into multiple MutateRows requests. Note that when a large row is split between multiple API calls, the updates to the row are not atomic.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Avro Files on Cloud Storage to Cloud Bigtable** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/GCS_Avro_to_Cloud_Bigtable \
        --region REGION_NAME \
        --parameters \
    bigtableProjectId=BIGTABLE_PROJECT_ID,\
    bigtableInstanceId=INSTANCE_ID,\
    bigtableTableId=TABLE_ID,\
    inputFilePattern=INPUT_FILE_PATTERN

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
  * `INPUT_FILE_PATTERN`: the Cloud Storage path pattern where data is located, for example, `gs://mybucket/somefolder/prefix*`



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/GCS_Avro_to_Cloud_Bigtable
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "bigtableProjectId": "BIGTABLE_PROJECT_ID",
           "bigtableInstanceId": "INSTANCE_ID",
           "bigtableTableId": "TABLE_ID",
           "inputFilePattern": "INPUT_FILE_PATTERN",
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
  * `INPUT_FILE_PATTERN`: the Cloud Storage path pattern where data is located, for example, `gs://mybucket/somefolder/prefix*`



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
    
    import com.google.bigtable.v2.Mutation;
    import com.google.bigtable.v2.Mutation.SetCell;
    import com.google.cloud.teleport.bigtable.AvroToBigtable.Options;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.common.base.MoreObjects;
    import com.google.common.collect.ImmutableList;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.nio.ByteBuffer;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.[extensions](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.ExtendableMessage.html#com_google_protobuf_GeneratedMessageLite_ExtendableMessage_extensions).avro.io.AvroIO;
    import org.apache.beam.sdk.io.gcp.bigtable.BigtableIO;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.options.ValueProvider.StaticValueProvider;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.KV;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * Dataflow pipeline that imports data from Avro files in GCS to a Cloud Bigtable table. The Cloud
     * Bigtable table must be created before running the pipeline and must have a compatible table
     * schema. For example, if {@link BigtableCell} from the Avro files has a 'family' of "f1", the
     * Bigtable table should have a column family of "f1".
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_GCS_Avro_to_Cloud_Bigtable.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "GCS_Avro_to_Cloud_Bigtable",
        category = TemplateCategory.BATCH,
        displayName = "Avro Files on Cloud Storage to Cloud Bigtable",
        description =
            "The Cloud Storage Avro to Bigtable template is a pipeline that reads data from Avro files in a Cloud Storage bucket and writes the data to a Bigtable table. "
                + "You can use the template to copy data from Cloud Storage to Bigtable.",
        optionsClass = Options.class,
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-bigtable",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The Bigtable table must exist and have the same column families as exported in the Avro files.",
          "The input Avro files must exist in a Cloud Storage bucket before running the pipeline.",
          "Bigtable expects a specific <a href=\"https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/src/main/resources/schema/avro/bigtable.avsc\">schema</a> from the input Avro files.",
        })
    public final class AvroToBigtable {
      private static final Logger LOG = LoggerFactory.getLogger(AvroToBigtable.class);
    
      /** Maximum number of mutations allowed per row by Cloud bigtable. */
      private static final int MAX_MUTATIONS_PER_ROW = 100000;
    
      private static final Boolean DEFAULT_SPLIT_LARGE_ROWS = false;
    
      /** Options for the import pipeline. */
      public interface Options extends PipelineOptions {
        @TemplateParameter.ProjectId(
            order = 1,
            groupName = "Target",
            description = "Project ID",
            helpText =
                "The ID of the Google Cloud project that contains the Bigtable instance that you want to write data to.")
        ValueProvider<String> getBigtableProjectId();
    
        @SuppressWarnings("unused")
        void setBigtableProjectId(ValueProvider<String> projectId);
    
        @TemplateParameter.Text(
            order = 2,
            groupName = "Target",
            regexes = {"[a-z][a-z0-9\\-]+[a-z0-9]"},
            description = "Instance ID",
            helpText = "The ID of the Bigtable instance that contains the table.")
        ValueProvider<String> getBigtableInstanceId();
    
        @SuppressWarnings("unused")
        void setBigtableInstanceId(ValueProvider<String> instanceId);
    
        @TemplateParameter.Text(
            order = 4,
            groupName = "Target",
            regexes = {"[_a-zA-Z0-9][-_.a-zA-Z0-9]*"},
            description = "Table ID",
            helpText = "The ID of the Bigtable table to import.")
        ValueProvider<String> getBigtableTableId();
    
        @SuppressWarnings("unused")
        void setBigtableTableId(ValueProvider<String> tableId);
    
        @TemplateParameter.GcsReadFile(
            order = 5,
            groupName = "Source",
            description = "Input Cloud Storage File(s)",
            helpText = "The Cloud Storage path pattern where data is located.",
            example = "gs://<BUCKET_NAME>/FOLDER/PREFIX*")
        ValueProvider<String> getInputFilePattern();
    
        @SuppressWarnings("unused")
        void setInputFilePattern(ValueProvider<String> inputFilePattern);
    
        @TemplateParameter.Boolean(
            order = 6,
            optional = true,
            description = "If true, large rows will be split into multiple MutateRows requests",
            helpText =
                "The flag for enabling splitting of large rows into multiple MutateRows requests. Note that when a large row is split between multiple API calls, the updates to the row are not atomic.")
        ValueProvider<Boolean> getSplitLargeRows();
    
        void setSplitLargeRows(ValueProvider<Boolean> splitLargeRows);
      }
    
      /**
       * Runs a pipeline to import Avro files in GCS to a Cloud Bigtable table.
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
    
        BigtableIO.Write write =
            BigtableIO.write()
                .withProjectId(options.getBigtableProjectId())
                .withInstanceId(options.getBigtableInstanceId())
                .withTableId(options.getBigtableTableId());
    
        pipeline
            .apply("Read from Avro", AvroIO.read(BigtableRow.class).from(options.getInputFilePattern()))
            .apply(
                "Transform to Bigtable",
                ParDo.of(
                    AvroToBigtableFn.createWithSplitLargeRows(
                        options.getSplitLargeRows(), MAX_MUTATIONS_PER_ROW)))
            .apply("Write to Bigtable", write);
    
        return pipeline.[run](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.RpcCallback.html#com_google_protobuf_RpcCallback_run_ParameterType_)();
      }
    
      /**
       * Translates {@link BigtableRow} to {@link Mutation}s along with a row key. The mutations are
       * {@link SetCell}s that set the value for specified cells with family name, column qualifier and
       * timestamp.
       */
      static class AvroToBigtableFn extends DoFn<BigtableRow, KV<ByteString, Iterable<Mutation>>> {
        private final ValueProvider<Boolean> splitLargeRowsFlag;
        private Boolean splitLargeRows;
        private final int maxMutationsPerRow;
    
        public static AvroToBigtableFn create() {
          return new AvroToBigtableFn(StaticValueProvider.of(false), MAX_MUTATIONS_PER_ROW);
        }
    
        public static AvroToBigtableFn createWithSplitLargeRows(
            ValueProvider<Boolean> splitLargeRowsFlag, int maxMutationsPerRequest) {
          return new AvroToBigtableFn(splitLargeRowsFlag, maxMutationsPerRequest);
        }
    
        private AvroToBigtableFn(
            ValueProvider<Boolean> splitLargeRowsFlag, int maxMutationsPerRequest) {
          this.splitLargeRowsFlag = splitLargeRowsFlag;
          this.maxMutationsPerRow = maxMutationsPerRequest;
        }
    
        @Setup
        public void setup() {
          if (splitLargeRowsFlag != null) {
            splitLargeRows = splitLargeRowsFlag.get();
          }
          splitLargeRows = MoreObjects.firstNonNull(splitLargeRows, DEFAULT_SPLIT_LARGE_ROWS);
          LOG.info("splitLargeRows set to: " + splitLargeRows);
        }
    
        @ProcessElement
        public void processElement(
            @Element BigtableRow row, OutputReceiver<KV<ByteString, Iterable<Mutation>>> out) {
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) key = toByteString(row.getKey());
          // BulkMutation doesn't split rows. Currently, if a single row contains more than 100,000
          // mutations, the service will fail the request.
          ImmutableList.Builder<Mutation> mutations = ImmutableList.[builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.html#com_google_protobuf_TextFormatParseInfoTree_builder__)();
          int cellsProcessed = 0;
          for (BigtableCell cell : row.getCells()) {
            SetCell setCell =
                SetCell.newBuilder()
                    .setFamilyName(cell.getFamily().toString())
                    .setColumnQualifier(toByteString(cell.getQualifier()))
                    .setTimestampMicros(cell.getTimestamp())
                    .setValue(toByteString(cell.getValue()))
                    .build();
    
            mutations.add(Mutation.newBuilder().setSetCell(setCell).build());
            cellsProcessed++;
    
            if (this.splitLargeRows && cellsProcessed % maxMutationsPerRow == 0) {
              // Send a MutateRow request when we have accumulated max mutations per row.
              out.output(KV.of(key, mutations.build()));
              mutations = ImmutableList.[builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.html#com_google_protobuf_TextFormatParseInfoTree_builder__)();
            }
          }
    
          // Flush any remaining mutations.
          ImmutableList remainingMutations = mutations.build();
          if (!remainingMutations.isEmpty()) {
            out.output(KV.of(key, remainingMutations));
          }
        }
      }
    
      /** Copies the content in {@code byteBuffer} into a {@link ByteString}. */
      protected static [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) toByteString(ByteBuffer byteBuffer) {
        return [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(byteBuffer.array());
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
