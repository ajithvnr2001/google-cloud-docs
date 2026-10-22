---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-change-streams-to-vector-search/
title: Bigtable change streams to Vector Search template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:05.550831+00:00
---

# Bigtable change streams to Vector Search template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-change-streams-to-vector-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Bigtable change streams to Vector Search template Stay organized with collections  Save and categorize content based on your preferences. 

This template creates a streaming pipeline to stream Bigtable data change records and write them to Vertex AI Vector Search using the Dataflow Portable Runner. 

## Pipeline requirements

  * The Bigtable source instance must exist.
  * The Bigtable source table must exist, and the table must have change streams enabled.
  * The Bigtable application profile must exist.
  * The Vector Search index path must exist.



## Template parameters

### Required parameters

  * **embeddingColumn** : The fully qualified column name where the embeddings are stored. In the format cf:col.
  * **embeddingByteSize** : The byte size of each entry in the embeddings array. Use 4 for Float, and 8 for Double. Defaults to: 4.
  * **vectorSearchIndex** : The Vector Search Index where changes will be streamed, in the format 'projects/{projectID}/locations/{region}/indexes/{indexID}' (no leading or trailing spaces) For example, `projects/123/locations/us-east1/indexes/456`.
  * **bigtableChangeStreamAppProfile** : The Bigtable application profile ID. The application profile must use single-cluster routing and allow single-row transactions.
  * **bigtableReadInstanceId** : The source Bigtable instance ID.
  * **bigtableReadTableId** : The source Bigtable table ID.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Bigtable Change Streams to Vector Search** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud CLI

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Bigtable_Change_Streams_to_Vector_Search \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --parameters \
           embeddingColumn=EMBEDDING_COLUMN,\
           embeddingByteSize=EMBEDDING_BYTE_SIZE,\
           vectorSearchIndex=VECTOR_SEARCH_INDEX,\
           bigtableChangeStreamAppProfile=BIGTABLE_CHANGE_STREAM_APP_PROFILE,\
           bigtableReadInstanceId=BIGTABLE_READ_INSTANCE_ID,\
           bigtableReadTableId=BIGTABLE_READ_TABLE_ID,\

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `EMBEDDING_COLUMN`: the Embedding column
  * `EMBEDDING_BYTE_SIZE`: the byte size of the embeddings array. Can be 4 or 8.
  * `VECTOR_SEARCH_INDEX`: the Vector Search index Path
  * `BIGTABLE_CHANGE_STREAM_APP_PROFILE`: the Bigtable application profile ID
  * `BIGTABLE_READ_INSTANCE_ID`: the source Bigtable Instance ID
  * `BIGTABLE_READ_TABLE_ID`: the source Bigtable table ID



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launchParameter": {
         "jobName": "JOB_NAME",
         "parameters": {
           "embeddingColumn": "EMBEDDING_COLUMN",
           "embeddingByteSize": "EMBEDDING_BYTE_SIZE",
           "vectorSearchIndex": "VECTOR_SEARCH_INDEX",
           "bigtableChangeStreamAppProfile": "BIGTABLE_CHANGE_STREAM_APP_PROFILE",
           "bigtableReadInstanceId": "BIGTABLE_READ_INSTANCE_ID",
           "bigtableReadTableId": "BIGTABLE_READ_TABLE_ID",
         },
         "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Bigtable_Change_Streams_to_Vector_Search",
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
  * `EMBEDDING_COLUMN`: the Embedding column
  * `EMBEDDING_BYTE_SIZE`: the byte size of the embeddings array. Can be 4 or 8.
  * `VECTOR_SEARCH_INDEX`: the Vector Search index Path
  * `BIGTABLE_CHANGE_STREAM_APP_PROFILE`: the Bigtable application profile ID
  * `BIGTABLE_READ_INSTANCE_ID`: the source Bigtable Instance ID
  * `BIGTABLE_READ_TABLE_ID`: the source Bigtable table ID



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
    package com.google.cloud.teleport.v2.templates.bigtablechangestreamstovectorsearch;
    
    import com.google.cloud.[Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html);
    import com.google.cloud.aiplatform.v1.[IndexDatapoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexDatapoint.html);
    import com.google.cloud.teleport.metadata.[Template](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.Template.html);
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).options.BigtableCommonOptions.ReadChangeStreamOptions;
    import com.google.cloud.teleport.v2.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).options.BigtableCommonOptions.ReadOptions;
    import com.google.cloud.teleport.v2.cdc.dlq.DeadLetterQueueManager;
    import com.google.cloud.teleport.v2.options.BigtableChangeStreamsToVectorSearchOptions;
    import com.google.cloud.teleport.v2.transforms.DLQWriteTransform;
    import com.google.cloud.teleport.v2.utils.DurationUtils;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html);
    import org.apache.beam.sdk.[PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html);
    import org.apache.beam.sdk.io.gcp.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).BigtableIO;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.GroupIntoBatches;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.Values;
    import org.apache.beam.sdk.transforms.WithKeys;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.TupleTagList;
    import org.apache.commons.lang3.StringUtils;
    import org.joda.time.[Duration](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Duration.html);
    import org.joda.time.Instant;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    @Template(
        name = "Bigtable_Change_Streams_to_Vector_Search",
        category = TemplateCategory.STREAMING,
        displayName = "Bigtable Change Streams to Vector Search",
        description =
            "Streaming pipeline. Streams Bigtable data change records and writes them into Vertex AI Vector Search using Dataflow Runner V2.",
        optionsClass = BigtableChangeStreamsToVectorSearchOptions.class,
        optionsOrder = {
          BigtableChangeStreamsToVectorSearchOptions.class,
          ReadChangeStreamOptions.class,
          ReadOptions.class
        },
        skipOptions = {
          "bigtableReadAppProfile",
          "bigtableAdditionalRetryCodes",
          "bigtableRpcAttemptTimeoutMs",
          "bigtableRpcTimeoutMs"
        },
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-change-streams-to-vector-search",
        flexContainerName = "googlecloud-to-googlecloud",
        contactInformation = "https://cloud.google.com/support",
        streaming = true)
    public final class BigtableChangeStreamsToVectorSearch {
      private static final Logger LOG =
          LoggerFactory.getLogger(BigtableChangeStreamsToVectorSearch.class);
    
      private static final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) USE_RUNNER_V2_EXPERIMENT = "use_runner_v2";
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) throws Exception {
        LOG.info("Starting replication from Cloud Bigtable Change Streams to Vector Search");
    
        BigtableChangeStreamsToVectorSearchOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(BigtableChangeStreamsToVectorSearchOptions.class);
    
        run(options);
      }
    
      public static [PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html) run(BigtableChangeStreamsToVectorSearchOptions options)
          throws IOException {
        options.setStreaming(true);
        options.setEnableStreamingEngine(true);
    
        List<String> experiments = options.getExperiments();
        if (experiments == null) {
          experiments = new ArrayList<>();
        }
        boolean hasUseRunnerV2 = false;
        for ([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) experiment : experiments) {
          if (experiment.equalsIgnoreCase(USE_RUNNER_V2_EXPERIMENT)) {
            hasUseRunnerV2 = true;
            break;
          }
        }
        if (!hasUseRunnerV2) {
          experiments.add(USE_RUNNER_V2_EXPERIMENT);
        }
        options.[setExperiments](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListExperimentsResponse.Builder.html#com_google_cloud_dialogflow_cx_v3_ListExperimentsResponse_Builder_setExperiments_int_com_google_cloud_dialogflow_cx_v3_Experiment_)(experiments);
    
        Instant startTimestamp =
            options.getBigtableChangeStreamStartTimestamp().isEmpty()
                ? Instant.[now](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_now__)()
                : toInstant([Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[parseTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_parseTimestamp_java_lang_String_)(options.getBigtableChangeStreamStartTimestamp()));
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigtableProjectId = getBigtableProjectId(options);
    
        LOG.info("  - startTimestamp {}", startTimestamp);
        LOG.info("  - bigtableReadInstanceId {}", options.getBigtableReadInstanceId());
        LOG.info("  - bigtableReadTableId {}", options.getBigtableReadTableId());
        LOG.info("  - bigtableChangeStreamAppProfile {}", options.getBigtableChangeStreamAppProfile());
        LOG.info("  - embeddingColumn {}", options.getEmbeddingColumn());
        LOG.info("  - crowdingTagColumn {}", options.getCrowdingTagColumn());
        LOG.info("  - project {}", options.getProject());
        LOG.info("  - indexName {}", options.getVectorSearchIndex());
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) indexName = options.getVectorSearchIndex();
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) vertexRegion = Utils.extractRegionFromIndexName(indexName);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) vertexEndpoint = vertexRegion + "-aiplatform.googleapis.com:443";
    
        final [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html) pipeline = [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html).create(options);
    
        DeadLetterQueueManager dlqManager = buildDlqManager(options);
    
        BigtableIO.ReadChangeStream readChangeStream =
            BigtableIO.[readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_)()
                .withChangeStreamName(options.getBigtableChangeStreamName())
                .withExistingPipelineOptions(
                    options.getBigtableChangeStreamResume()
                        ? BigtableIO.ExistingPipelineOptions.RESUME_OR_FAIL
                        : BigtableIO.ExistingPipelineOptions.FAIL_IF_EXISTS)
                .withProjectId(bigtableProjectId)
                .withAppProfileId(options.getBigtableChangeStreamAppProfile())
                .withInstanceId(options.getBigtableReadInstanceId())
                .withTableId(options.getBigtableReadTableId())
                .withMetadataTableInstanceId(options.getBigtableChangeStreamMetadataInstanceId())
                .withMetadataTableTableId(options.getBigtableMetadataTableTableId())
                .withStartTime(startTimestamp);
    
        PCollectionTuple results =
            [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__)
                .apply("Read from Cloud Bigtable Change Streams", readChangeStream)
                .apply("Create Values", Values.create())
                .apply(
                    "Converting to Vector Search Datapoints",
                    ParDo.of(
                            new ChangeStreamMutationToDatapointOperationFn(
                                options.getEmbeddingColumn(),
                                options.getEmbeddingByteSize(),
                                options.getCrowdingTagColumn(),
                                Utils.parseColumnMapping(options.getAllowRestrictsMappings()),
                                Utils.parseColumnMapping(options.getDenyRestrictsMappings()),
                                Utils.parseColumnMapping(options.getIntNumericRestrictsMappings()),
                                Utils.parseColumnMapping(options.getFloatNumericRestrictsMappings()),
                                Utils.parseColumnMapping(options.getDoubleNumericRestrictsMappings())))
                        .withOutputTags(
                            ChangeStreamMutationToDatapointOperationFn.UPSERT_DATAPOINT_TAG,
                            TupleTagList.of(
                                ChangeStreamMutationToDatapointOperationFn.REMOVE_DATAPOINT_TAG)));
        [results](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.spi.v1.DnsRpc.ListResult.html#com_google_cloud_dns_spi_v1_DnsRpc_ListResult_results__)
            .get(ChangeStreamMutationToDatapointOperationFn.UPSERT_DATAPOINT_TAG)
            .apply("Add placeholer keys", WithKeys.of("placeholder"))
            .apply(
                "Batch Contents",
                GroupIntoBatches.<String, IndexDatapoint>ofSize(
                        bufferSizeOption(options.getUpsertMaxBatchSize()))
                    .withMaxBufferingDuration(
                        bufferDurationOption(options.getUpsertMaxBufferDuration())))
            .apply("Map to Values", Values.create())
            .apply(
                "Upsert Datapoints to VectorSearch",
                ParDo.of(new UpsertDatapointsFn(vertexEndpoint, indexName)))
            .apply(
                "Write errors to DLQ",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqManager.getSevereDlqDirectory() + "YYYY/MM/dd/HH/mm/")
                    .withTmpDirectory(dlqManager.getSevereDlqDirectory() + "tmp/")
                    .setIncludePaneInfo(true)
                    .build());
    
        [results](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.spi.v1.DnsRpc.ListResult.html#com_google_cloud_dns_spi_v1_DnsRpc_ListResult_results__)
            .get(ChangeStreamMutationToDatapointOperationFn.REMOVE_DATAPOINT_TAG)
            .apply("Add placeholder keys", WithKeys.of("placeholer"))
            .apply(
                "Batch Contents",
                GroupIntoBatches.<String, String>ofSize(
                        bufferSizeOption(options.getDeleteMaxBatchSize()))
                    .withMaxBufferingDuration(
                        bufferDurationOption(options.getDeleteMaxBufferDuration())))
            .apply("Map to Values", Values.create())
            .apply(
                "Remove Datapoints From VectorSearch",
                ParDo.of(new RemoveDatapointsFn(vertexEndpoint, indexName)))
            .apply(
                "Write errors to DLQ",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqManager.getSevereDlqDirectory() + "YYYY/MM/dd/HH/mm/")
                    .withTmpDirectory(dlqManager.getSevereDlqDirectory() + "tmp/")
                    .setIncludePaneInfo(true)
                    .build());
    
        return [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).run();
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getBigtableProjectId(BigtableChangeStreamsToVectorSearchOptions options) {
        return StringUtils.isEmpty(options.getBigtableReadProjectId())
            ? options.getProject()
            : options.getBigtableReadProjectId();
      }
    
      private static Instant toInstant([Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html) timestamp) {
        if (timestamp == null) {
          return null;
        } else {
          return Instant.ofEpochMilli(timestamp.[getSeconds](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_getSeconds__)() * 1000 + timestamp.[getNanos](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_getNanos__)() / 1000000);
        }
      }
    
      private static int bufferSizeOption(int size) {
        if (size < 1) {
          size = 1;
        }
    
        return size;
      }
    
      private static [Duration](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Duration.html) bufferDurationOption([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) duration) {
        if (duration.isEmpty()) {
          return [Duration](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Duration.html).standardSeconds(1);
        }
    
        return DurationUtils.parseDuration(duration);
      }
    
      private static DeadLetterQueueManager buildDlqManager(
          BigtableChangeStreamsToVectorSearchOptions options) {
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) dlqDirectory = options.getDlqDirectory();
        if (dlqDirectory.isEmpty()) {
          LOG.info("Falling back to temp dir for DLQ");
    
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tempLocation = options.as(DataflowPipelineOptions.class).getTempLocation();
    
          LOG.info("Have temp location {}", tempLocation);
          if (tempLocation == null || tempLocation.isEmpty()) {
            tempLocation = "/";
          } else if (!tempLocation.endsWith("/")) {
            tempLocation += "/";
          }
    
          dlqDirectory = tempLocation + "dlq";
        }
    
        LOG.info("Writing dead letter queue to: {}", dlqDirectory);
    
        return DeadLetterQueueManager.create(dlqDirectory, 1);
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
