---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-datadog/
title: Pub/Sub to Datadog template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:54.640953+00:00
---

# Pub/Sub to Datadog template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-datadog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Pub/Sub to Datadog template Stay organized with collections  Save and categorize content based on your preferences. 

The Pub/Sub to Datadog template is a streaming pipeline that reads messages from a Pub/Sub subscription and writes the message payload to Datadog by using a Datadog endpoint. The most common use case for this template is to export log files to Datadog.

Before writing to Datadog, you can apply a JavaScript user-defined function to the message payload. Any messages that experience processing failures are forwarded to a Pub/Sub unprocessed topic for further troubleshooting and reprocessing.

As an extra layer of protection for your API keys and secrets, you can also pass in a Cloud KMS key along with the base64-encoded API key parameter encrypted with the Cloud KMS key. For additional details about encrypting your API key parameter, see the [Cloud KMS API encryption endpoint](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt).

## Pipeline requirements

  * The source Pub/Sub subscription must exist prior to running the pipeline.
  * The Pub/Sub unprocessed topic must exist prior to running the pipeline.
  * The Datadog URL must be accessible from the network of the Dataflow workers.
  * The Datadog API key must be generated and available.



## Template parameters

### Required parameters

  * **inputSubscription** : The Pub/Sub subscription to read the input from. For example, `projects/your-project-id/subscriptions/your-subscription-name`.
  * **url** : The Datadog Logs API URL. This URL must be routable from the VPC that the pipeline runs in. See Send logs (<https://docs.datadoghq.com/api/latest/logs/#send-logs>) in the Datadog documentation for more information. For example, `https://http-intake.logs.datadoghq.com`.
  * **outputDeadletterTopic** : The Pub/Sub topic to forward undeliverable messages to. For example, `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.



### Optional parameters

  * **apiKey** : The Datadog API key. You must provide this value if the `apiKeySource` is set to `PLAINTEXT` or `KMS`. For more information, see API and Application Keys (<https://docs.datadoghq.com/account_management/api-app-keys/>) in the Datadog documentation.
  * **batchCount** : The batch size for sending multiple events to Datadog. The default is `100`.
  * **parallelism** : The maximum number of parallel requests. The default is `1` (no parallelism).
  * **includePubsubMessage** : Whether to include the full Pub/Sub message in the payload. The default is `true` (all elements, including the data element, are included in the payload).
  * **apiKeyKMSEncryptionKey** : The Cloud KMS key to use to decrypt the API Key. You must provide this parameter if the `apiKeySource` is set to `KMS`. If the Cloud KMS key is provided, you must pass in an encrypted API Key. For example, `projects/your-project-id/locations/global/keyRings/your-keyring/cryptoKeys/your-key-name`.
  * **apiKeySecretId** : The Secret Manager secret ID for the API Key. You must provide this parameter if the `apiKeySource` is set to `SECRET_MANAGER`. For example, `projects/your-project-id/secrets/your-secret/versions/your-secret-version`.
  * **apiKeySource** : The source of the API key. The following values are supported: `PLAINTEXT`, `KMS`, and `SECRET_MANAGER`. You must provide this parameter if you're using Secret Manager. If `apiKeySource` is set to `KMS`, you must also provide `apiKeyKMSEncryptionKey` and encrypted `API Key`. If `apiKeySource` is set to `SECRET_MANAGER`, you must also provide `apiKeySecretId`. If `apiKeySource` is set to `PLAINTEXT`, you must also provide `apiKey`.
  * **javascriptTextTransformGcsPath** : The Cloud Storage URI of the .js file that defines the JavaScript user-defined function (UDF) to use. For example, `gs://my-bucket/my-udfs/my_file.js`.
  * **javascriptTextTransformFunctionName** : The name of the JavaScript user-defined function (UDF) to use. For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see UDF Examples (<https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples>).
  * **javascriptTextTransformReloadIntervalMinutes** : Define the interval that workers may check for JavaScript UDF changes to reload the files. Defaults to: 0.



## User-defined function

Optionally, you can extend this template by writing a user-defined function (UDF). The template calls the UDF for each input element. Element payloads are serialized as JSON strings. For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

### Function specification

The UDF has the following specification:

  * **Input** : the Pub/Sub message data field, serialized as a JSON string.
  * **Output** : the event data to be sent to the Datadog Log endpoint. The output must be a string or a stringified JSON object. 



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Pub/Sub to Datadog** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/Cloud_PubSub_to_Datadog \
        --region REGION_NAME \
        --staging-location STAGING_LOCATION \
        --parameters \
    inputSubscription=projects/PROJECT_ID/subscriptions/INPUT_SUBSCRIPTION_NAME,\
    apiKey=API_KEY,\
    url=URL,\
    outputDeadletterTopic=projects/PROJECT_ID/topics/DEADLETTER_TOPIC_NAME,\
    javascriptTextTransformGcsPath=PATH_TO_JAVASCRIPT_UDF_FILE,\
    javascriptTextTransformFunctionName=JAVASCRIPT_FUNCTION,\
    batchCount=BATCH_COUNT,\
    parallelism=PARALLELISM

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `STAGING_LOCATION`: the location for staging local files (for example, `gs://your-bucket/staging`)
  * `INPUT_SUBSCRIPTION_NAME`: the Pub/Sub subscription name
  * `API_KEY`: Datadog's API Key
  * `URL`: the URL for Datadog's endpoint (for example, `https://http-intake.logs.datadoghq.com`)
  * `DEADLETTER_TOPIC_NAME`: the Pub/Sub topic name
  * `JAVASCRIPT_FUNCTION`: the name of the JavaScript user-defined function (UDF) that you want to use 

For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see [UDF Examples](https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples). 

  * `PATH_TO_JAVASCRIPT_UDF_FILE`: the Cloud Storage URI of the `.js` file that defines the JavaScript user-defined function (UDF) you want to use—for example, `gs://my-bucket/my-udfs/my_file.js`
  * `BATCH_COUNT`: the batch size to use for sending multiple events to Datadog
  * `PARALLELISM`: the number of parallel requests to use for sending events to Datadog



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/Cloud_PubSub_to_Datadog
    {
       "jobName": "JOB_NAME",
       "environment": {
           "ipConfiguration": "WORKER_IP_UNSPECIFIED",
           "additionalExperiments": []
       },
       "parameters": {
           "inputSubscription": "projects/PROJECT_ID/subscriptions/INPUT_SUBSCRIPTION_NAME",
           "apiKey": "API_KEY",
           "url": "URL",
           "outputDeadletterTopic": "projects/PROJECT_ID/topics/DEADLETTER_TOPIC_NAME",
           "javascriptTextTransformGcsPath": "PATH_TO_JAVASCRIPT_UDF_FILE",
           "javascriptTextTransformFunctionName": "JAVASCRIPT_FUNCTION",
           "batchCount": "BATCH_COUNT",
           "parallelism": "PARALLELISM"
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
  * `STAGING_LOCATION`: the location for staging local files (for example, `gs://your-bucket/staging`)
  * `INPUT_SUBSCRIPTION_NAME`: the Pub/Sub subscription name
  * `API_KEY`: Datadog's API Key
  * `URL`: the URL for Datadog's endpoint (for example, `https://http-intake.logs.datadoghq.com`)
  * `DEADLETTER_TOPIC_NAME`: the Pub/Sub topic name
  * `JAVASCRIPT_FUNCTION`: the name of the JavaScript user-defined function (UDF) that you want to use 

For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see [UDF Examples](https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples). 

  * `PATH_TO_JAVASCRIPT_UDF_FILE`: the Cloud Storage URI of the `.js` file that defines the JavaScript user-defined function (UDF) you want to use—for example, `gs://my-bucket/my-udfs/my_file.js`
  * `BATCH_COUNT`: the batch size to use for sending multiple events to Datadog
  * `PARALLELISM`: the number of parallel requests to use for sending events to Datadog



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
    package com.google.cloud.teleport.templates;
    
    import com.google.cloud.teleport.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.datadog.DatadogEvent;
    import com.google.cloud.teleport.datadog.DatadogEventCoder;
    import com.google.cloud.teleport.datadog.DatadogIO;
    import com.google.cloud.teleport.datadog.DatadogWriteError;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.templates.PubSubToDatadog.PubSubToDatadogOptions;
    import com.google.cloud.teleport.templates.common.DatadogConverters;
    import com.google.cloud.teleport.templates.common.DatadogConverters.DatadogOptions;
    import com.google.cloud.teleport.templates.common.ErrorConverters;
    import com.google.cloud.teleport.templates.common.JavascriptTextTransformer.FailsafeJavascriptUdf;
    import com.google.cloud.teleport.templates.common.JavascriptTextTransformer.JavascriptTextTransformerOptions;
    import com.google.cloud.teleport.templates.common.PubsubConverters.PubsubReadSubscriptionOptions;
    import com.google.cloud.teleport.templates.common.PubsubConverters.PubsubWriteDeadletterTopicOptions;
    import com.google.cloud.teleport.util.DatadogApiKeyNestedValueProvider;
    import com.google.cloud.teleport.values.FailsafeElement;
    import com.google.common.annotations.VisibleForTesting;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import com.google.gson.JsonSyntaxException;
    import java.nio.charset.StandardCharsets;
    import java.util.Map;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.CoderRegistry;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
    import org.apache.beam.sdk.metrics.Counter;
    import org.apache.beam.sdk.metrics.Metrics;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.Flatten;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.PTransform;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.PBegin;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionList;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.TupleTag;
    import org.apache.beam.vendor.guava.v32_1_2_jre.com.google.common.base.MoreObjects;
    import org.apache.beam.vendor.guava.v32_1_2_jre.com.google.common.collect.ImmutableList;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link PubSubToDatadog} pipeline is a streaming pipeline which ingests data from Cloud
     * Pub/Sub, executes a UDF, converts the output to {@link DatadogEvent}s and writes those records
     * into Datadog's Logs API. Any errors which occur in the execution of the UDF, conversion to {@link
     * DatadogEvent} or writing to Logs API will be streamed into a Pub/Sub topic.
     *
     * <p><b>Pipeline Requirements</b>
     *
     * <ul>
     *   <li>The source Pub/Sub subscription exists.
     *   <li>Logs API is routable from the VPC where the Dataflow job executes.
     *   <li>Deadletter topic exists.
     * </ul>
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Cloud_PubSub_to_Datadog.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Cloud_PubSub_to_Datadog",
        category = TemplateCategory.STREAMING,
        displayName = "Pub/Sub to Datadog",
        description = {
          "The Pub/Sub to Datadog template is a streaming pipeline that reads messages from a Pub/Sub subscription and writes the message payload to Datadog by using a Datadog endpoint. The most common use case for this template is to export log files to Datadog. "
              + "For more information check out <a href=\"https://docs.datadoghq.com/integrations/google_cloud_platform/?tab=project#log-collection\">Datadog's log collection process</a>.\n",
          "Before writing to Datadog, you can apply a JavaScript user-defined function to the message payload. "
              + "Any messages that experience processing failures are forwarded to a Pub/Sub unprocessed topic for further troubleshooting and reprocessing.\n",
          "As an extra layer of protection for your API keys and secrets, you can also pass in a Cloud KMS key along with the base64-encoded API key parameter encrypted with the Cloud KMS key. For additional details about encrypting your API key parameter, see the <a href=\"https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt\">Cloud KMS API encryption endpoint</a>."
        },
        optionsClass = PubSubToDatadogOptions.class,
        optionsOrder = {
          PubsubReadSubscriptionOptions.class,
          DatadogOptions.class,
          JavascriptTextTransformerOptions.class,
          PubsubWriteDeadletterTopicOptions.class
        },
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-datadog",
        contactInformation = "https://cloud.google.com/support",
        preview = true,
        requirements = {
          "The source Pub/Sub subscription must exist prior to running the pipeline.",
          "The Pub/Sub unprocessed topic must exist prior to running the pipeline.",
          "The Datadog URL must be accessible from the network of the Dataflow workers.",
          "The Datadog API key must be generated and available."
        },
        streaming = true,
        supportsAtLeastOnce = true)
    public class PubSubToDatadog {
    
      /** String/String Coder for FailsafeElement. */
      public static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      /** Counter to track inbound messages from source. */
      private static final Counter INPUT_MESSAGES_COUNTER =
          Metrics.counter(PubSubToDatadog.class, "inbound-pubsub-messages");
    
      /** The tag for successful {@link DatadogEvent} conversion. */
      private static final TupleTag<DatadogEvent> DATADOG_EVENT_OUT = new TupleTag<DatadogEvent>() {};
    
      /** The tag for failed {@link DatadogEvent} conversion. */
      private static final TupleTag<FailsafeElement<String, String>> DATADOG_EVENT_DEADLETTER_OUT =
          new TupleTag<FailsafeElement<String, String>>() {};
    
      /** The tag for the main output for the UDF. */
      private static final TupleTag<FailsafeElement<String, String>> UDF_OUT =
          new TupleTag<FailsafeElement<String, String>>() {};
    
      /** The tag for the dead-letter output of the udf. */
      private static final TupleTag<FailsafeElement<String, String>> UDF_DEADLETTER_OUT =
          new TupleTag<FailsafeElement<String, String>>() {};
    
      /** GSON to process a {@link PubsubMessage}. */
      private static final Gson GSON = new Gson();
    
      /** Logger for class. */
      private static final Logger LOG = LoggerFactory.getLogger(PubSubToDatadog.class);
    
      private static final Boolean DEFAULT_INCLUDE_PUBSUB_MESSAGE = true;
    
      @VisibleForTesting protected static final String PUBSUB_MESSAGE_ATTRIBUTE_FIELD = "attributes";
      @VisibleForTesting protected static final String PUBSUB_MESSAGE_DATA_FIELD = "data";
      private static final String PUBSUB_MESSAGE_ID_FIELD = "messageId";
    
      /**
       * The main entry-point for pipeline execution. This method will start the pipeline but will not
       * wait for it's execution to finish. If blocking execution is required, use the {@link
       * PubSubToDatadog#run(PubSubToDatadogOptions)} method to start the pipeline and invoke {@code
       * result.waitUntilFinish()} on the {@link PipelineResult}.
       *
       * @param args The command-line args passed by the executor.
       */
      public static void main(String[] args) {
    
        PubSubToDatadogOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(PubSubToDatadogOptions.class);
    
        run(options);
      }
    
      /**
       * Runs the pipeline to completion with the specified options. This method does not wait until the
       * pipeline is finished before returning. Invoke {@code result.waitUntilFinish()} on the result
       * object to block until the pipeline is finished running if blocking programmatic execution is
       * required.
       *
       * @param options The execution options.
       * @return The pipeline result.
       */
      public static PipelineResult run(PubSubToDatadogOptions options) {
    
        Pipeline pipeline = Pipeline.create(options);
    
        // Register coders.
        CoderRegistry registry = pipeline.getCoderRegistry();
        registry.registerCoderForClass(DatadogEvent.class, DatadogEventCoder.of());
        registry.registerCoderForType(
            FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor(), FAILSAFE_ELEMENT_CODER);
    
        /*
         * Steps:
         *  1) Read messages in from Pub/Sub
         *  2) Convert message to FailsafeElement for processing.
         *  3) Apply user provided UDF (if any) on the input strings.
         *  4) Convert successfully transformed messages into DatadogEvent objects
         *  5) Write DatadogEvents to Datadog's Logs API.
         *  5a) Wrap write failures into a FailsafeElement.
         *  6) Collect errors from UDF transform (#3), DatadogEvent transform (#4)
         *     and writing to Datadog Logs API (#5) and stream into a Pub/Sub deadletter topic.
         */
    
        // 1) Read messages in from Pub/Sub
        PCollection<String> stringMessages =
            pipeline.apply(
                "ReadMessages",
                new ReadMessages(options.getInputSubscription(), options.getIncludePubsubMessage()));
    
        // 2) Convert message to FailsafeElement for processing.
        PCollectionTuple transformedOutput =
            stringMessages
                .apply(
                    "ConvertToFailsafeElement",
                    MapElements.into(FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor())
                        .via(input -> FailsafeElement.of(input, input)))
    
                // 3) Apply user provided UDF (if any) on the input strings.
                .apply(
                    "ApplyUDFTransformation",
                    FailsafeJavascriptUdf.<String>newBuilder()
                        .setFileSystemPath(options.getJavascriptTextTransformGcsPath())
                        .setFunctionName(options.getJavascriptTextTransformFunctionName())
                        .setReloadIntervalMinutes(
                            options.getJavascriptTextTransformReloadIntervalMinutes())
                        .setLoggingEnabled(ValueProvider.StaticValueProvider.of(true))
                        .setSuccessTag(UDF_OUT)
                        .setFailureTag(UDF_DEADLETTER_OUT)
                        .build());
    
        // 4) Convert successfully transformed messages into DatadogEvent objects
        PCollectionTuple convertToEventTuple =
            transformedOutput
                .get(UDF_OUT)
                .apply(
                    "ConvertToDatadogEvent",
                    DatadogConverters.failsafeStringToDatadogEvent(
                        DATADOG_EVENT_OUT, DATADOG_EVENT_DEADLETTER_OUT));
    
        // 5) Write DatadogEvents to Datadog's Logs API.
        PCollection<DatadogWriteError> writeErrors =
            convertToEventTuple
                .get(DATADOG_EVENT_OUT)
                .apply(
                    "WriteToDatadog",
                    DatadogIO.writeBuilder()
                        .withApiKey(
                            new DatadogApiKeyNestedValueProvider(
                                options.getApiKeySecretId(),
                                options.getApiKeyKMSEncryptionKey(),
                                options.getApiKey(),
                                options.getApiKeySource()))
                        .withUrl(options.getUrl())
                        .withBatchCount(options.getBatchCount())
                        .withParallelism(options.getParallelism())
                        .build());
    
        // 5a) Wrap write failures into a FailsafeElement.
        PCollection<FailsafeElement<String, String>> wrappedDatadogWriteErrors =
            writeErrors.apply(
                "WrapDatadogWriteErrors",
                ParDo.of(
                    new DoFn<DatadogWriteError, FailsafeElement<String, String>>() {
    
                      @ProcessElement
                      public void processElement(ProcessContext context) {
                        DatadogWriteError error = context.element();
                        FailsafeElement<String, String> failsafeElement =
                            FailsafeElement.of(error.payload(), error.payload());
    
                        if (error.statusMessage() != null) {
                          failsafeElement.setErrorMessage(error.statusMessage());
                        }
    
                        if (error.statusCode() != null) {
                          failsafeElement.setErrorMessage(
                              String.format("Datadog write status code: %d", error.statusCode()));
                        }
                        context.output(failsafeElement);
                      }
                    }));
    
        // 6) Collect errors from UDF transform (#4), DatadogEvent transform (#5)
        //     and writing to Datadog Logs API (#6) and stream into a Pub/Sub deadletter topic.
        PCollectionList.of(
                ImmutableList.of(
                    convertToEventTuple.get(DATADOG_EVENT_DEADLETTER_OUT),
                    wrappedDatadogWriteErrors,
                    transformedOutput.get(UDF_DEADLETTER_OUT)))
            .apply("FlattenErrors", Flatten.pCollections())
            .apply(
                "WriteFailedRecords",
                ErrorConverters.WriteStringMessageErrorsToPubSub.newBuilder()
                    .setErrorRecordsTopic(options.getOutputDeadletterTopic())
                    .build());
    
        return pipeline.run();
      }
    
      /**
       * The {@link PubSubToDatadogOptions} class provides the custom options passed by the executor at
       * the command line.
       */
      public interface PubSubToDatadogOptions
          extends DatadogOptions,
              PubsubReadSubscriptionOptions,
              PubsubWriteDeadletterTopicOptions,
              JavascriptTextTransformerOptions {}
    
      /**
       * A {@link PTransform} that reads messages from a Pub/Sub subscription, increments a counter and
       * returns a {@link PCollection} of {@link String} messages.
       */
      private static class ReadMessages extends PTransform<PBegin, PCollection<String>> {
        private final ValueProvider<String> subscriptionName;
        private final ValueProvider<Boolean> inputIncludePubsubMessageFlag;
        private Boolean includePubsubMessage;
    
        ReadMessages(
            ValueProvider<String> subscriptionName,
            ValueProvider<Boolean> inputIncludePubsubMessageFlag) {
          this.subscriptionName = subscriptionName;
          this.inputIncludePubsubMessageFlag = inputIncludePubsubMessageFlag;
        }
    
        @Override
        public PCollection<String> expand(PBegin input) {
          return input
              .apply(
                  "ReadPubsubMessage",
                  PubsubIO.readMessagesWithAttributes().fromSubscription(subscriptionName))
              .apply(
                  "ExtractMessageIfRequired",
                  ParDo.of(
                      new DoFn<PubsubMessage, String>() {
    
                        @Setup
                        public void setup() {
                          if (inputIncludePubsubMessageFlag != null) {
                            includePubsubMessage = inputIncludePubsubMessageFlag.get();
                          }
                          includePubsubMessage =
                              MoreObjects.firstNonNull(
                                  includePubsubMessage, DEFAULT_INCLUDE_PUBSUB_MESSAGE);
                          LOG.info("includePubsubMessage set to: {}", includePubsubMessage);
                        }
    
                        @ProcessElement
                        public void processElement(ProcessContext context) {
                          if (includePubsubMessage) {
                            context.output(formatPubsubMessage(context.element()));
                          } else {
                            context.output(
                                new String(context.element().getPayload(), StandardCharsets.UTF_8));
                          }
                        }
                      }))
              .apply(
                  "CountMessages",
                  ParDo.of(
                      new DoFn<String, String>() {
                        @ProcessElement
                        public void processElement(ProcessContext context) {
                          INPUT_MESSAGES_COUNTER.inc();
                          context.output(context.element());
                        }
                      }));
        }
      }
    
      /**
       * Utility method that formats {@link org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage} according
       * to the model defined in {@link com.google.pubsub.v1.PubsubMessage}.
       *
       * @param pubsubMessage {@link org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage}
       * @return JSON String that adheres to the model defined in {@link
       *     com.google.pubsub.v1.PubsubMessage}
       */
      @VisibleForTesting
      protected static String formatPubsubMessage(PubsubMessage pubsubMessage) {
        JsonObject messageJson = new JsonObject();
    
        String payload = new String(pubsubMessage.getPayload(), StandardCharsets.UTF_8);
        try {
          JsonObject data = GSON.fromJson(payload, JsonObject.class);
          messageJson.add(PUBSUB_MESSAGE_DATA_FIELD, data);
        } catch (JsonSyntaxException e) {
          messageJson.addProperty(PUBSUB_MESSAGE_DATA_FIELD, payload);
        }
    
        JsonObject attributes = getAttributesJson(pubsubMessage.getAttributeMap());
        messageJson.add(PUBSUB_MESSAGE_ATTRIBUTE_FIELD, attributes);
    
        if (pubsubMessage.getMessageId() != null) {
          messageJson.addProperty(PUBSUB_MESSAGE_ID_FIELD, pubsubMessage.getMessageId());
        }
    
        return messageJson.toString();
      }
    
      /**
       * Constructs a {@link JsonObject} from a {@link Map} of Pub/Sub attributes.
       *
       * @param attributesMap {@link Map} of Pub/Sub attributes
       * @return {@link JsonObject} of Pub/Sub attributes
       */
      private static JsonObject getAttributesJson(Map<String, String> attributesMap) {
        JsonObject attributesJson = new JsonObject();
        for (String key : attributesMap.keySet()) {
          attributesJson.addProperty(key, attributesMap.get(key));
        }
    
        return attributesJson;
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
