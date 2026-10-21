---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-change-streams-to-pubsub/
title: Spanner change streams to Pub/Sub template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:43:23.166617+00:00
---

# Spanner change streams to Pub/Sub template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-change-streams-to-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Spanner change streams to Pub/Sub template Stay organized with collections  Save and categorize content based on your preferences. 

The Spanner change streams to the Pub/Sub template is a streaming pipeline that streams Spanner data change records and writes them into Pub/Sub topics [using the Dataflow Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner).

**Note:** The Spanner change streams connector doesn't support draining a job. To stop the pipeline, [cancel the job](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel) instead of draining it. Draining a job with the Spanner change streams connector can cause it to become stuck in a draining state. For more information, see [Draining](https://docs.cloud.google.com/spanner/docs/change-streams/use-dataflow#draining) in the Spanner documentation. 

To output your data to a new Pub/Sub topic, you need to first create the topic. After creation, Pub/Sub automatically generates and attaches a subscription to the new topic. If you try to output data to a Pub/Sub topic that doesn't exist, the dataflow pipeline throws an exception, and the pipeline gets stuck as it continuously tries to make a connection. 

If the necessary Pub/Sub topic already exists, you can output data to that topic.

For more information, see [About change streams](https://docs.cloud.google.com/spanner/docs/change-streams), [Build change streams connections with Dataflow](https://docs.cloud.google.com/spanner/docs/change-streams/use-dataflow), and [Change streams best practices](https://docs.cloud.google.com/spanner/docs/change-streams/use-dataflow#best_practices).

## Pipeline requirements

  * The Spanner instance must exist before running the pipeline. 
  * The Spanner database must exist prior to running the pipeline. 
  * The Spanner metadata instance must exist prior to running the pipeline.
  * The Spanner metadata database must exist prior to running the pipeline.
  * The Spanner change stream must exist prior to running the pipeline.
  * The Pub/Sub topic must exist prior to running the pipeline.



## Template parameters

### Required parameters

  * **spannerInstanceId** : The Spanner instance to read change streams from.
  * **spannerDatabase** : The Spanner database to read change streams from.
  * **spannerMetadataInstanceId** : The Spanner instance to use for the change streams connector metadata table.
  * **spannerMetadataDatabase** : The Spanner database to use for the change streams connector metadata table.
  * **spannerChangeStreamName** : The name of the Spanner change stream to read from.
  * **pubsubTopic** : The Pub/Sub topic for change streams output.



### Optional parameters

  * **spannerProjectId** : The project to read change streams from. This project is also where the change streams connector metadata table is created. The default for this parameter is the project where the Dataflow pipeline is running.
  * **spannerDatabaseRole** : The Spanner database role to use when running the template. This parameter is required only when the IAM principal who is running the template is a fine-grained access control user. The database role must have the `SELECT` privilege on the change stream and the `EXECUTE` privilege on the change stream's read function. For more information, see Fine-grained access control for change streams (<https://cloud.google.com/spanner/docs/fgac-change-streams>).
  * **spannerMetadataTableName** : The Spanner change streams connector metadata table name to use. If not provided, Spanner automatically creates the streams connector metadata table during the pipeline flow change. You must provide this parameter when updating an existing pipeline. Don't use this parameter for other cases.
  * **startTimestamp** : The starting DateTime (<https://tools.ietf.org/html/rfc3339>), inclusive, to use for reading change streams. For example, ex- 2021-10-12T07:20:50.52Z. Defaults to the timestamp when the pipeline starts, that is, the current time.
  * **endTimestamp** : The ending DateTime (<https://tools.ietf.org/html/rfc3339>), inclusive, to use for reading change streams. For example, ex- 2021-10-12T07:20:50.52Z. Defaults to an infinite time in the future.
  * **spannerHost** : The Cloud Spanner endpoint to call in the template. Only used for testing. For example, `https://spanner.googleapis.com`. Defaults to: <https://spanner.googleapis.com>.
  * **outputDataFormat** : The format of the output. Output is wrapped in many PubsubMessages and sent to a Pub/Sub topic. Allowed formats are JSON and AVRO. Default is JSON.
  * **pubsubAPI** : The Pub/Sub API used to implement the pipeline. Allowed APIs are `pubsubio` and `native_client`. For a small number of queries per second (QPS), `native_client` has less latency. For a large number of QPS, `pubsubio` provides better and more stable performance. The default is `pubsubio`.
  * **pubsubProjectId** : Project of Pub/Sub topic. The default for this parameter is the project where the Dataflow pipeline is running.
  * **rpcPriority** : The request priority for Spanner calls. Allowed values are HIGH, MEDIUM, and LOW. Defaults to: HIGH).
  * **includeSpannerSource** : Whether or not to include the spanner database id and instance id to read the change stream from in the output message data. Defaults to: false.
  * **outputMessageMetadata** : The string value for the custom field outputMessageMetadata in output pub/sub message. Defaults to empty and the field outputMessageMetadata is only populated if this value is non-empty. Please escape any special characters when entering the value here(ie: double quotes).
  * **useSpannerEmulatorHost** : Whether to use the Spanner host configured in getSpannerHost() as the Emulator host. Defaults to: false.
  * **spannerChangeStreamTvfNameList** : Semicolon-separated list of Spanner Change Stream TVF names to query and union. Defaults to empty.
  * **spannerDirectedReadOptions** : Directed read options for Cloud Spanner Change Stream reads. The value must be a JSON string format of DirectedReadOptions (e.g. {"includeReplicas":{"replicaSelections":[{"location":"us-central1","type":"READ_ONLY"}]}}). For more information, see Directed reads (<https://docs.cloud.google.com/spanner/docs/directed-reads>). Defaults to empty.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Cloud Spanner change streams to Pub/Sub** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
        gcloud dataflow flex-template run JOB_NAME \
            --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Spanner_Change_Streams_to_PubSub \
            --region REGION_NAME \
            --parameters \
        spannerInstanceId=SPANNER_INSTANCE_ID,\
        spannerDatabase=SPANNER_DATABASE,\
        spannerMetadataInstanceId=SPANNER_METADATA_INSTANCE_ID,\
        spannerMetadataDatabase=SPANNER_METADATA_DATABASE,\
        spannerChangeStreamName=SPANNER_CHANGE_STREAM,\
        pubsubTopic=PUBSUB_TOPIC
        

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `SPANNER_INSTANCE_ID`: Spanner instance ID
  * `SPANNER_DATABASE`: Spanner database
  * `SPANNER_METADATA_INSTANCE_ID`: Spanner metadata instance ID
  * `SPANNER_METADATA_DATABASE`: Spanner metadata database
  * `SPANNER_CHANGE_STREAM`: Spanner change stream
  * `PUBSUB_TOPIC`: The Pub/Sub topic for change streams output



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
      POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
      {
        "launch_parameter": {
            "jobName": "JOB_NAME",
            "parameters": {
                "spannerInstanceId": "SPANNER_INSTANCE_ID",
                "spannerDatabase": "SPANNER_DATABASE",
                "spannerMetadataInstanceId": "SPANNER_METADATA_INSTANCE_ID",
                "spannerMetadataDatabase": "SPANNER_METADATA_DATABASE",
                "spannerChangeStreamName": "SPANNER_CHANGE_STREAM",
                "pubsubTopic": "PUBSUB_TOPIC"
            },
            "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Spanner_Change_Streams_to_PubSub",
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
  * `SPANNER_INSTANCE_ID`: Spanner instance ID
  * `SPANNER_DATABASE`: Spanner database
  * `SPANNER_METADATA_INSTANCE_ID`: Spanner metadata instance ID
  * `SPANNER_METADATA_DATABASE`: Spanner metadata database
  * `SPANNER_CHANGE_STREAM`: Spanner change stream
  * `PUBSUB_TOPIC`: The Pub/Sub topic for change streams output



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2022 Google LLC
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
    
    import com.google.cloud.[Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html);
    import com.google.cloud.spanner.[Options](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.html).[RpcPriority](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.RpcPriority.html);
    import com.google.cloud.teleport.metadata.[Template](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.Template.html);
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.SpannerChangeStreamsToPubSubOptions;
    import com.google.cloud.teleport.v2.transforms.FileFormatFactorySpannerChangeStreamsToPubSub;
    import java.nio.charset.StandardCharsets;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    import java.util.stream.Collectors;
    import org.apache.beam.sdk.[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html);
    import org.apache.beam.sdk.[PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html);
    import org.apache.beam.sdk.io.gcp.spanner.SpannerConfig;
    import org.apache.beam.sdk.io.gcp.spanner.SpannerIO;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link SpannerChangeStreamsToPubSub} pipeline streams change stream record(s) and stores to
     * pubsub topic in user specified format. The sink data can be stored in a JSON Text or Avro data
     * format.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-googlecloud/README_Spanner_Change_Streams_to_PubSub.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Spanner_Change_Streams_to_PubSub",
        category = TemplateCategory.STREAMING,
        displayName = "Cloud Spanner change streams to Pub/Sub",
        description = {
          "The Cloud Spanner change streams to the Pub/Sub template is a streaming pipeline that streams Cloud Spanner data change records and writes them into Pub/Sub topics using Dataflow Runner V2.\n",
          "To output your data to a new Pub/Sub topic, you need to first create the topic. After creation, Pub/Sub automatically generates and attaches a subscription to the new topic. "
              + "If you try to output data to a Pub/Sub topic that doesn't exist, the dataflow pipeline throws an exception, and the pipeline gets stuck as it continuously tries to make a connection.\n",
          "If the necessary Pub/Sub topic already exists, you can output data to that topic.",
          "Learn more about <a href=\"https://cloud.google.com/spanner/docs/change-streams\">change streams</a>, <a href=\"https://cloud.google.com/spanner/docs/change-streams/use-dataflow\">how to build change streams Dataflow pipelines</a>, and <a href=\"https://cloud.google.com/spanner/docs/change-streams/use-dataflow#best_practices\">best practices</a>."
        },
        optionsClass = SpannerChangeStreamsToPubSubOptions.class,
        flexContainerName = "googlecloud-to-googlecloud",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-change-streams-to-pubsub",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The Cloud Spanner instance must exist before running the pipeline.",
          "The Cloud Spanner database must exist prior to running the pipeline.",
          "The Cloud Spanner metadata instance must exist prior to running the pipeline.",
          "The Cloud Spanner metadata database must exist prior to running the pipeline.",
          "The Cloud Spanner change stream must exist prior to running the pipeline.",
          "The Pub/Sub topic must exist prior to running the pipeline."
        },
        streaming = true,
        supportsAtLeastOnce = true)
    public class SpannerChangeStreamsToPubSub {
      private static final Logger LOG = LoggerFactory.getLogger(SpannerChangeStreamsToPubSub.class);
      private static final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) USE_RUNNER_V2_EXPERIMENT = "use_runner_v2";
    
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) {
        UncaughtExceptionLogger.register();
    
        LOG.info("Starting Input Messages to Pub/Sub");
    
        SpannerChangeStreamsToPubSubOptions options =
            PipelineOptionsFactory.fromArgs(args).as(SpannerChangeStreamsToPubSubOptions.class);
    
        run(options);
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getSpannerProjectId(SpannerChangeStreamsToPubSubOptions options) {
        return options.getSpannerProjectId().isEmpty()
            ? options.getProject()
            : options.getSpannerProjectId();
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getPubsubProjectId(SpannerChangeStreamsToPubSubOptions options) {
        return options.getPubsubProjectId().isEmpty()
            ? options.getProject()
            : options.getPubsubProjectId();
      }
    
      public static boolean isValidAsciiString([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) outputMessageMetadata) {
        if (outputMessageMetadata != null
            && !StandardCharsets.US_ASCII.newEncoder().canEncode(outputMessageMetadata)) {
          return false;
        }
        return true;
      }
    
      public static [PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html) run(SpannerChangeStreamsToPubSubOptions options) {
        LOG.info("Requested Message Format is " + options.getOutputDataFormat());
        options.setStreaming(true);
        options.setEnableStreamingEngine(true);
    
        final [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html) pipeline = [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html).create(options);
        // Get the Spanner project, instance, database, metadata instance, metadata database
        // change stream, pubsub topic, and pubsub api parameters.
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) spannerProjectId = getSpannerProjectId(options);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) instanceId = options.getSpannerInstanceId();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) databaseId = options.getSpannerDatabase();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) metadataInstanceId = options.getSpannerMetadataInstanceId();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) metadataDatabaseId = options.getSpannerMetadataDatabase();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) changeStreamName = options.getSpannerChangeStreamName();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) pubsubProjectId = getPubsubProjectId(options);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) pubsubTopicName = options.getPubsubTopic();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) pubsubAPI = options.getPubsubAPI();
        Boolean includeSpannerSource = options.getIncludeSpannerSource();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) outputMessageMetadata = options.getOutputMessageMetadata();
    
        // Ensure outputMessageMetadata only contains valid ascii characters
        if (!isValidAsciiString(outputMessageMetadata)) {
          throw new RuntimeException("outputMessageMetadata contains non ascii characters.");
        }
    
        // Retrieve and parse the start / end timestamps.
        [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html) startTimestamp =
            options.getStartTimestamp().isEmpty()
                ? [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[now](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_now__)()
                : [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[parseTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_parseTimestamp_java_lang_String_)(options.getStartTimestamp());
        [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html) endTimestamp =
            options.getEndTimestamp().isEmpty()
                ? [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).MAX_VALUE
                : [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[parseTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_parseTimestamp_java_lang_String_)(options.getEndTimestamp());
    
        // Add use_runner_v2 to the experiments option, since Change Streams connector is only supported
        // on Dataflow runner v2.
        List<String> experiments = options.getExperiments();
        if (experiments == null) {
          experiments = new ArrayList<>();
        }
        if (!experiments.contains(USE_RUNNER_V2_EXPERIMENT)) {
          experiments.add(USE_RUNNER_V2_EXPERIMENT);
        }
        options.[setExperiments](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListExperimentsResponse.Builder.html#com_google_cloud_dialogflow_cx_v3_ListExperimentsResponse_Builder_setExperiments_int_com_google_cloud_dialogflow_cx_v3_Experiment_)(experiments);
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) metadataTableName =
            options.getSpannerMetadataTableName() == null
                ? null
                : options.getSpannerMetadataTableName();
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tvfNameListString = options.getSpannerChangeStreamTvfNameList();
        List<String> tvfNameList = null;
        if (tvfNameListString != null && !tvfNameListString.isEmpty()) {
          tvfNameList =
              Arrays.stream(tvfNameListString.[split](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_split_com_google_cloud_firestore_pipeline_expressions_Expression_)(";"))
                  .filter(name -> !name.[trim](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_trim__)().isEmpty())
                  .collect(Collectors.toList());
        }
    
        final [RpcPriority](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.RpcPriority.html) rpcPriority = options.getRpcPriority();
        SpannerConfig spannerConfig =
            SpannerConfig.create()
                .withProjectId(spannerProjectId)
                .withInstanceId(instanceId)
                .withDatabaseId(databaseId);
    
        if (options.getUseSpannerEmulatorHost() != null && options.getUseSpannerEmulatorHost()) {
          spannerConfig =
              spannerConfig.withEmulatorHost(
                  ValueProvider.StaticValueProvider.of(options.getSpannerHost()));
        } else {
          spannerConfig =
              spannerConfig.withHost(ValueProvider.StaticValueProvider.of(options.getSpannerHost()));
        }
    
        // Propagate database role for fine-grained access control on change stream.
        if (options.getSpannerDatabaseRole() != null) {
          spannerConfig =
              spannerConfig.withDatabaseRole(
                  ValueProvider.StaticValueProvider.of(options.getSpannerDatabaseRole()));
        }
        [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__)
            .apply(
                SpannerIO.[readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_)()
                    .withSpannerConfig(spannerConfig)
                    .withMetadataInstance(metadataInstanceId)
                    .withMetadataDatabase(metadataDatabaseId)
                    .withChangeStreamName(changeStreamName)
                    .withInclusiveStartAt(startTimestamp)
                    .withInclusiveEndAt(endTimestamp)
                    .withRpcPriority(rpcPriority)
                    .withMetadataTable(metadataTableName)
                    .withTvfNameList(tvfNameList)
                    .withDirectedReadOptions(options.getSpannerDirectedReadOptions()))
            .apply(
                "Convert each record to a PubsubMessage",
                FileFormatFactorySpannerChangeStreamsToPubSub.newBuilder()
                    .setOutputDataFormat(options.getOutputDataFormat())
                    .setProjectId(pubsubProjectId)
                    .setPubsubAPI(pubsubAPI)
                    .setPubsubTopicName(pubsubTopicName)
                    .setIncludeSpannerSource(includeSpannerSource)
                    .setSpannerDatabaseId(databaseId)
                    .setSpannerInstanceId(instanceId)
                    .setOutputMessageMetadata(outputMessageMetadata)
                    .build());
        return [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
