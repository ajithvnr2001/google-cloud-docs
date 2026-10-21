---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-elasticsearch/
title: Pub/Sub to Elasticsearch template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:17.999844+00:00
---

# Pub/Sub to Elasticsearch template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-elasticsearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Pub/Sub to Elasticsearch template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Pub/Sub to Elasticsearch template is a streaming pipeline that reads messages from a Pub/Sub subscription, executes a user-defined function (UDF), and writes them to Elasticsearch as documents. The Dataflow template uses Elasticsearch's [data streams](https://www.elastic.co/guide/en/elasticsearch/reference/current/data-streams.html) feature to store time series data across multiple indices while giving you a single named resource for requests. Data streams are well-suited for logs, metrics, traces, and other continuously generated data stored in Pub/Sub. 

The template creates a data stream named `logs-gcp.DATASET-NAMESPACE`, where:

  * DATASET is the value of the `dataset` template parameter, or `pubsub` if not specified.
  * NAMESPACE is the value of the `namespace` template parameter, or `default` if not specified.



## Pipeline requirements

  * The source Pub/Sub subscription must exist and the messages must be encoded in a valid JSON format.
  * A publicly reachable Elasticsearch host on a Google Cloud instance or on Elastic Cloud with Elasticsearch version 7.0 or higher. See [Google Cloud Integration for Elastic](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-elasticsearch/docs/PubSubToElasticsearch/README.md#google-cloud-integration-for-elastic) for more details.
  * A Pub/Sub topic for error output.



## Template parameters

### Required parameters

  * **inputSubscription** : Pub/Sub subscription to consume the input from. For example, `projects/<PROJECT_ID>/subscriptions/<SUBSCRIPTION_NAME>`.
  * **errorOutputTopic** : The Pub/Sub output topic for publishing failed records, in the format of `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.
  * **connectionUrl** : The Elasticsearch URL in the format `https://hostname:[port]`. If using Elastic Cloud, specify the CloudID. For example, `https://elasticsearch-host:9200`.
  * **apiKey** : The Base64-encoded API key to use for authentication.



### Optional parameters

  * **dataset** : The type of logs sent using Pub/Sub, for which we have an out-of-the-box dashboard. Known log types values are `audit`, `vpcflow`, and `firewall`. Defaults to: `pubsub`.
  * **namespace** : An arbitrary grouping, such as an environment (dev, prod, or qa), a team, or a strategic business unit. Defaults to: `default`.
  * **elasticsearchTemplateVersion** : Dataflow Template Version Identifier, usually defined by Google Cloud. Defaults to: 1.0.0.
  * **javascriptTextTransformGcsPath** : The Cloud Storage URI of the .js file that defines the JavaScript user-defined function (UDF) to use. For example, `gs://my-bucket/my-udfs/my_file.js`.
  * **javascriptTextTransformFunctionName** : The name of the JavaScript user-defined function (UDF) to use. For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see UDF Examples (<https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples>).
  * **javascriptTextTransformReloadIntervalMinutes** : Specifies how frequently to reload the UDF, in minutes. If the value is greater than 0, Dataflow periodically checks the UDF file in Cloud Storage, and reloads the UDF if the file is modified. This parameter allows you to update the UDF while the pipeline is running, without needing to restart the job. If the value is `0`, UDF reloading is disabled. The default value is `0`.
  * **elasticsearchUsername** : The Elasticsearch username to authenticate with. If specified, the value of `apiKey` is ignored.
  * **elasticsearchPassword** : The Elasticsearch password to authenticate with. If specified, the value of `apiKey` is ignored.
  * **batchSize** : The batch size in number of documents. Defaults to `1000`.
  * **batchSizeBytes** : The batch size in number of bytes. Defaults to `5242880` (5mb).
  * **maxRetryAttempts** : The maximum number of retry attempts. Must be greater than zero. Defaults to `5`.
  * **maxRetryDuration** : The maximum retry duration in milliseconds. Must be greater than zero. Defaults to `60000` (1 minute).
  * **propertyAsIndex** : The property in the document being indexed whose value specifies `_index` metadata to include with the document in bulk requests. Takes precedence over an `_index` UDF. Defaults to `none`.
  * **javaScriptIndexFnGcsPath** : The Cloud Storage path to the JavaScript UDF source for a function that specifies `_index` metadata to include with the document in bulk requests. Defaults to `none`.
  * **javaScriptIndexFnName** : The name of the UDF JavaScript function that specifies `_index` metadata to include with the document in bulk requests. Defaults to `none`.
  * **propertyAsId** : A property in the document being indexed whose value specifies `_id` metadata to include with the document in bulk requests. Takes precedence over an `_id` UDF. Defaults to `none`.
  * **javaScriptIdFnGcsPath** : The Cloud Storage path to the JavaScript UDF source for the function that specifies `_id` metadata to include with the document in bulk requests. Defaults to `none`.
  * **javaScriptIdFnName** : The name of the UDF JavaScript function that specifies the `_id` metadata to include with the document in bulk requests. Defaults to `none`.
  * **javaScriptTypeFnGcsPath** : The Cloud Storage path to the JavaScript UDF source for a function that specifies `_type` metadata to include with documents in bulk requests. Defaults to `none`.
  * **javaScriptTypeFnName** : The name of the UDF JavaScript function that specifies the `_type` metadata to include with the document in bulk requests. Defaults to `none`.
  * **javaScriptIsDeleteFnGcsPath** : The Cloud Storage path to the JavaScript UDF source for the function that determines whether to delete the document instead of inserting or updating it. The function returns a string value of `true` or `false`. Defaults to `none`.
  * **javaScriptIsDeleteFnName** : The name of the UDF JavaScript function that determines whether to delete the document instead of inserting or updating it. The function returns a string value of `true` or `false`. Defaults to `none`.
  * **usePartialUpdate** : Whether to use partial updates (update rather than create or index, allowing partial documents) with Elasticsearch requests. Defaults to `false`.
  * **bulkInsertMethod** : Whether to use `INDEX` (index, allows upserts) or `CREATE` (create, errors on duplicate _id) with Elasticsearch bulk requests. Defaults to `CREATE`.
  * **trustSelfSignedCerts** : Whether to trust self-signed certificate or not. An Elasticsearch instance installed might have a self-signed certificate, Enable this to true to by-pass the validation on SSL certificate. (Defaults to: `false`).
  * **disableCertificateValidation** : If `true`, trust the self-signed SSL certificate. An Elasticsearch instance might have a self-signed certificate. To bypass validation for the certificate, set this parameter to `true`. Defaults to `false`.
  * **apiKeyKMSEncryptionKey** : The Cloud KMS key to decrypt the API key. This parameter is required if the `apiKeySource` is set to `KMS`. If this parameter is provided, pass in an encrypted `apiKey` string. Encrypt parameters using the KMS API encrypt endpoint. For the key, use the format `projects/<PROJECT_ID>/locations/<KEY_REGION>/keyRings/<KEY_RING>/cryptoKeys/<KMS_KEY_NAME>`. See: <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt> For example, `projects/your-project-id/locations/global/keyRings/your-keyring/cryptoKeys/your-key-name`.
  * **apiKeySecretId** : The Secret Manager secret ID for the apiKey. If the `apiKeySource` is set to `SECRET_MANAGER`, provide this parameter. Use the format `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>. For example, `projects/your-project-id/secrets/your-secret/versions/your-secret-version`.
  * **apiKeySource** : The source of the API key. Allowed values are `PLAINTEXT`, `KMS` orand `SECRET_MANAGER`. This parameter is required when you use Secret Manager or KMS. If `apiKeySource` is set to `KMS`, `apiKeyKMSEncryptionKey` and encrypted apiKey must be provided. If `apiKeySource` is set to `SECRET_MANAGER`, `apiKeySecretId` must be provided. If `apiKeySource` is set to `PLAINTEXT`, `apiKey` must be provided. Defaults to: PLAINTEXT.
  * **socketTimeout** : If set, overwrites the default max retry timeout and default socket timeout (30000ms) in the Elastic RestClient.



## User-defined functions

This template supports user-defined functions (UDFs) at several points in the pipeline, described below. For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

### Text transform function

Transforms the Pub/Sub message into an Elasticsearch document.

Template parameters:

  * `javascriptTextTransformGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javascriptTextTransformFunctionName`: the name of the JavaScript function.



Function specification:

  * **Input** : the Pub/Sub message data field, serialized as a JSON string.
  * **Output** : a stringified JSON document to insert into Elasticsearch.



### Index function

Returns the index to which the document belongs.

Template parameters:

  * `javaScriptIndexFnGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javaScriptIndexFnName`: the name of the JavaScript function. 



Function specification:

  * **Input** : the Elasticsearch document, serialized as a JSON string.
  * **Output** : the value of the document's `_index` metadata field.



### Document ID function

Returns the document ID.

Template parameters:

  * `javaScriptIdFnGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javaScriptIdFnName`: the name of the JavaScript function.



Function specification:

  * **Input** : the Elasticsearch document, serialized as a JSON string.
  * **Output** : the value of the document's `_id` metadata field.



### Document deletion function

Specifies whether to delete a document. To use this function, set the bulk insert mode to `INDEX` and provide a document ID function.

Template parameters:

  * `javaScriptIsDeleteFnGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javaScriptIsDeleteFnName`: the name of the JavaScript function.



Function specification:

  * **Input** : the Elasticsearch document, serialized as a JSON string.
  * **Output** : return the string `"true"` to delete the document, or `"false"` to upsert the document.



### Mapping type function

Returns the document's mapping type.

**Caution:** Mapping types were removed in Elasticsearch 8.0. 

Template parameters:

  * `javaScriptTypeFnGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javaScriptTypeFnName`: the name of the JavaScript function. 



Function specification:

  * **Input** : the Elasticsearch document, serialized as a JSON string.
  * **Output** : the value of the document's `_type` metadata field.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Pub/Sub to Elasticsearch** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/PubSub_to_Elasticsearch_Flex \
        --parameters \
    inputSubscription=SUBSCRIPTION_NAME,\
    connectionUrl=CONNECTION_URL,\
    dataset=DATASET,\
    namespace=NAMESPACE,\
    apiKey=APIKEY,\
    errorOutputTopic=ERROR_OUTPUT_TOPIC
      

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `ERROR_OUTPUT_TOPIC`: your Pub/Sub topic for error output
  * `SUBSCRIPTION_NAME`: your Pub/Sub subscription name
  * `CONNECTION_URL`: your Elasticsearch URL
  * `DATASET`: your log type
  * `NAMESPACE`: your namespace for dataset
  * `APIKEY`: your base64 encoded API key for authentication



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "inputSubscription": "SUBSCRIPTION_NAME",
              "connectionUrl": "CONNECTION_URL",
              "dataset": "DATASET",
              "namespace": "NAMESPACE",
              "apiKey": "APIKEY",
              "errorOutputTopic": "ERROR_OUTPUT_TOPIC"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/PubSub_to_Elasticsearch_Flex",
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
  * `ERROR_OUTPUT_TOPIC`: your Pub/Sub topic for error output
  * `SUBSCRIPTION_NAME`: your Pub/Sub subscription name
  * `CONNECTION_URL`: your Elasticsearch URL
  * `DATASET`: your log type
  * `NAMESPACE`: your namespace for dataset
  * `APIKEY`: your base64 encoded API key for authentication



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2021 Google LLC
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
    package com.google.cloud.teleport.v2.elasticsearch.templates;
    
    import com.google.cloud.teleport.metadata.MultiTemplate;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.elasticsearch.options.PubSubToElasticsearchOptions;
    import com.google.cloud.teleport.v2.elasticsearch.transforms.FailedPubsubMessageToPubsubTopicFn;
    import com.google.cloud.teleport.v2.elasticsearch.transforms.ProcessEventMetadata;
    import com.google.cloud.teleport.v2.elasticsearch.transforms.PubSubMessageToJsonDocument;
    import com.google.cloud.teleport.v2.elasticsearch.transforms.WriteToElasticsearch;
    import com.google.cloud.teleport.v2.elasticsearch.utils.ElasticsearchIndex;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.CoderRegistry;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessageWithAttributesCoder;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.TupleTag;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.apache.commons.lang3.StringUtils;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link PubSubToElasticsearch} pipeline is a streaming pipeline which ingests data in JSON
     * format from PubSub, applies a Javascript UDF if provided and writes the resulting records to
     * Elasticsearch. If the element fails to be processed then it is written to an error output table
     * in BigQuery.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-elasticsearch/README_PubSub_to_Elasticsearch.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @MultiTemplate({
      @Template(
          name = "PubSub_to_Elasticsearch_Flex",
          category = TemplateCategory.STREAMING,
          displayName = "Pub/Sub to Elasticsearch",
          description = {
            "The Pub/Sub to Elasticsearch template is a streaming pipeline that reads messages from a Pub/Sub subscription, executes a user-defined function (UDF), and writes them to Elasticsearch as documents. "
                + "The Dataflow template uses Elasticsearch's <a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/master/data-streams.html\">data streams</a> feature to store time series data across multiple indices while giving you a single named resource for requests. "
                + "Data streams are well-suited for logs, metrics, traces, and other continuously generated data stored in Pub/Sub.\n",
            "The template creates a datastream named <code>logs-gcp.DATASET-NAMESPACE</code>, where:\n"
                + "- <code>DATASET</code> is the value of the <code>dataset</code> template parameter, or <code>pubsub</code> if not specified.\n"
                + "- <code>NAMESPACE</code> is the value of the <code>namespace</code> template parameter, or <code>default</code> if not specified."
          },
          optionsClass = PubSubToElasticsearchOptions.class,
          skipOptions = {
            "index",
            "pythonExternalTextTransformGcsPath",
            "pythonExternalTextTransformFunctionName",
          }, // Template just ignores what is sent as "index"
          flexContainerName = "googlecloud-to-elasticsearch",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-elasticsearch",
          contactInformation = "https://cloud.google.com/support",
          preview = true,
          requirements = {
            "The source Pub/Sub subscription must exist and the messages must be encoded in a valid JSON format.",
            "A publicly reachable Elasticsearch host on a Google Cloud instance or on Elastic Cloud with Elasticsearch version 7.0 or above. See <a href=\"https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-elasticsearch/docs/PubSubToElasticsearch/README.md#google-cloud-integration-for-elastic\">Google Cloud Integration for Elastic</a> for more details.",
            "A Pub/Sub topic for error output.",
          },
          streaming = true,
          supportsAtLeastOnce = true),
      @Template(
          name = "PubSub_to_Elasticsearch_Xlang",
          category = TemplateCategory.STREAMING,
          displayName = "Pub/Sub to Elasticsearch With Python UDFs",
          type = Template.TemplateType.XLANG,
          description = {
            "The Pub/Sub to Elasticsearch template is a streaming pipeline that reads messages from a Pub/Sub subscription, executes a Python user-defined function (UDF), and writes them to Elasticsearch as documents. "
                + "The Dataflow template uses Elasticsearch's <a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/master/data-streams.html\">data streams</a> feature to store time series data across multiple indices while giving you a single named resource for requests. "
                + "Data streams are well-suited for logs, metrics, traces, and other continuously generated data stored in Pub/Sub.\n",
            "The template creates a datastream named <code>logs-gcp.DATASET-NAMESPACE</code>, where:\n"
                + "- <code>DATASET</code> is the value of the <code>dataset</code> template parameter, or <code>pubsub</code> if not specified.\n"
                + "- <code>NAMESPACE</code> is the value of the <code>namespace</code> template parameter, or <code>default</code> if not specified."
          },
          optionsClass = PubSubToElasticsearchOptions.class,
          skipOptions = {
            "index",
            "javascriptTextTransformGcsPath",
            "javascriptTextTransformFunctionName",
            "javascriptTextTransformReloadIntervalMinutes"
          }, // Template just ignores what is sent as "index" and javascript udf as this is for python
          // udf only.
          flexContainerName = "googlecloud-to-elasticsearch-xlang",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-elasticsearch",
          contactInformation = "https://cloud.google.com/support",
          preview = true,
          requirements = {
            "The source Pub/Sub subscription must exist and the messages must be encoded in a valid JSON format.",
            "A publicly reachable Elasticsearch host on a Google Cloud instance or on Elastic Cloud with Elasticsearch version 7.0 or above. See <a href=\"https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-elasticsearch/docs/PubSubToElasticsearch/README.md#google-cloud-integration-for-elastic\">Google Cloud Integration for Elastic</a> for more details.",
            "A Pub/Sub topic for error output.",
          },
          streaming = true,
          supportsAtLeastOnce = true)
    })
    public class PubSubToElasticsearch {
    
      /** The tag for the main output of the json transformation. */
      public static final TupleTag<FailsafeElement<PubsubMessage, String>> TRANSFORM_OUT =
          new TupleTag<FailsafeElement<PubsubMessage, String>>() {};
    
      /** The tag for the error output table of the json to table row transform. */
      public static final TupleTag<FailsafeElement<PubsubMessage, String>> TRANSFORM_ERROR_OUTPUT_OUT =
          new TupleTag<FailsafeElement<PubsubMessage, String>>() {};
    
      /** Pubsub message/string coder for pipeline. */
      public static final FailsafeElementCoder<PubsubMessage, String> CODER =
          FailsafeElementCoder.of(PubsubMessageWithAttributesCoder.of(), StringUtf8Coder.of());
    
      /** String/String Coder for FailsafeElement. */
      public static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      /** The log to output status messages to. */
      private static final Logger LOG = LoggerFactory.getLogger(PubSubToElasticsearch.class);
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        // Parse the user options passed from the command-line.
        PubSubToElasticsearchOptions pubSubToElasticsearchOptions =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(PubSubToElasticsearchOptions.class);
    
        pubSubToElasticsearchOptions.setIndex(
            new ElasticsearchIndex(
                    pubSubToElasticsearchOptions.getDataset(),
                    pubSubToElasticsearchOptions.getNamespace())
                .getIndex());
    
        validateOptions(pubSubToElasticsearchOptions);
        run(pubSubToElasticsearchOptions);
      }
    
      public static void validateOptions(PubSubToElasticsearchOptions options) {
        switch (options.getApiKeySource()) {
          case "PLAINTEXT":
            return;
          case "KMS":
            // validate that the encryption key is provided.
            if (StringUtils.isEmpty(options.getApiKeyKMSEncryptionKey())) {
              throw new IllegalArgumentException(
                  "If apiKeySource is set to KMS, apiKeyKMSEncryptionKey should be provided.");
            }
            return;
          case "SECRET_MANAGER":
            // validate that secretId is provided.
            if (StringUtils.isEmpty(options.getApiKeySecretId())) {
              throw new IllegalArgumentException(
                  "If apiKeySource is set to SECRET_MANAGER, apiKeySecretId should be provided.");
            }
        }
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      public static PipelineResult run(PubSubToElasticsearchOptions options) {
    
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        // Register the coders for pipeline
        CoderRegistry coderRegistry = pipeline.getCoderRegistry();
    
        coderRegistry.registerCoderForType(
            FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor(), FAILSAFE_ELEMENT_CODER);
    
        coderRegistry.registerCoderForType(CODER.getEncodedTypeDescriptor(), CODER);
    
        /*
         * Steps: 1) Read PubSubMessage with attributes from input PubSub subscription.
         *        2) Apply Javascript UDF if provided.
         *        3) Index Json string to output ES index.
         *
         */
        LOG.info("Reading from subscription: " + options.getInputSubscription());
    
        PCollectionTuple convertedPubsubMessages =
            pipeline
                /*
                 * Step #1: Read from a PubSub subscription.
                 */
                .apply(
                    "ReadPubSubSubscription",
                    PubsubIO.readMessagesWithAttributes()
                        .fromSubscription(options.getInputSubscription()))
                /*
                 * Step #2: Transform the PubsubMessages into Json documents.
                 */
                .apply(
                    "ConvertMessageToJsonDocument",
                    PubSubMessageToJsonDocument.newBuilder()
                        .setJavascriptTextTransformFunctionName(
                            options.getJavascriptTextTransformFunctionName())
                        .setJavascriptTextTransformGcsPath(options.getJavascriptTextTransformGcsPath())
                        .setPythonExternalTextTransformGcsPath(
                            options.getPythonExternalTextTransformGcsPath())
                        .setPythonExternalTextTransformFunctionName(
                            options.getPythonExternalTextTransformFunctionName())
                        .build());
    
        /*
         * Step #3a: Write Json documents into Elasticsearch using {@link ElasticsearchTransforms.WriteToElasticsearch}.
         */
        convertedPubsubMessages
            .get(TRANSFORM_OUT)
            .apply(
                "GetJsonDocuments",
                MapElements.into(TypeDescriptors.strings()).via(FailsafeElement::getPayload))
            .apply("Insert metadata", new ProcessEventMetadata())
            .apply(
                "WriteToElasticsearch",
                WriteToElasticsearch.newBuilder()
                    .setUserAgent("dataflow-pubsub-to-elasticsearch-template/v2")
                    .setOptions(options.as(PubSubToElasticsearchOptions.class))
                    .build());
    
        /*
         * Step 3b: Write elements that failed processing to error output PubSub topic via {@link PubSubIO}.
         */
        convertedPubsubMessages
            .get(TRANSFORM_ERROR_OUTPUT_OUT)
            .apply(ParDo.of(new FailedPubsubMessageToPubsubTopicFn()))
            .apply("writeFailureMessages", PubsubIO.writeMessages().to(options.getErrorOutputTopic()));
    
        // Execute the pipeline and return the result.
        return pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
