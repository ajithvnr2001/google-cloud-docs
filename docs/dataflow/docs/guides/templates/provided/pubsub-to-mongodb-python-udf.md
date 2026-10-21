---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-mongodb-python-udf/
title: Pub/Sub to MongoDB with Python UDFs template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:19.252395+00:00
---

# Pub/Sub to MongoDB with Python UDFs template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-mongodb-python-udf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Pub/Sub to MongoDB with Python UDFs template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Pub/Sub to MongoDB with Python UDFs template is a streaming pipeline that reads JSON-encoded messages from a Pub/Sub subscription and writes them to MongoDB as documents. If required, this pipeline supports additional transforms that can be included using a Python user-defined function (UDF).

If errors occur while processing records, the template writes them to a BigQuery table, along with the input message. For example, errors might occur due to schema mismatch, malformed JSON, or while executing transforms. Specify the table name in the `deadletterTable` parameter. If the table doesn't exist, the pipeline automatically creates it. 

## Pipeline requirements

  * The Pub/Sub Subscription must exist and the messages must be encoded in a valid JSON format.
  * The MongoDB cluster must exist and should be accessible from the Dataflow worker machines.



## Template parameters

Parameter | Description  
---|---  
`inputSubscription` | Name of the Pub/Sub subscription. For example: ``projects/my-project-id/subscriptions/my-subscription-id``  
`mongoDBUri` | Comma separated list of MongoDB servers. For example: `192.285.234.12:27017,192.287.123.11:27017`  
`database` | Database in MongoDB to store the collection. For example: `my-db`.  
`collection` | Name of the collection inside MongoDB database. For example: `my-collection`.  
`deadletterTable` | BigQuery table that store messages due to failures (mismatched schema, malformed JSON etc). For example: `project-id:dataset-name.table-name`.  
`pythonExternalTextTransformGcsPath` | Optional: The Cloud Storage URI of the Python code file that defines the user-defined function (UDF) you want to use. For example, `gs://my-bucket/my-udfs/my_file.py`.   
`pythonExternalTextTransformFunctionName` | Optional: The name of the Python user-defined function (UDF) that you want to use.   
`batchSize` | Optional: Batch size used for batch insertion of documents into MongoDB. Default: `1000`.  
`batchSizeBytes` | Optional: Batch size in bytes. Default: `5242880`.  
`maxConnectionIdleTime` | Optional: Maximum idle time allowed in seconds before connection timeout occurs. Default: `60000`.  
`sslEnabled` | Optional: Boolean value indicating whether connection to MongoDB is SSL enabled. Default: `true`.  
`ignoreSSLCertificate` | Optional: Boolean value indicating if SSL certificate should be ignored. Default: `true`.  
`withOrdered` | Optional: Boolean value enabling ordered bulk insertions into MongoDB. Default: `true`.  
`withSSLInvalidHostNameAllowed` | Optional: Boolean value indicating if invalid hostname is allowed for SSL connection. Default: `true`.  
  
## User-defined function

Optionally, you can extend this template by writing a user-defined function (UDF). The template calls the UDF for each input element. Element payloads are serialized as JSON strings. For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

### Function specification

The UDF has the following specification:

  * **Input** : a single line from an input CSV file.
  * **Output** : a stringified JSON document to insert into MongoDB.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Pub/Sub to MongoDB with Python UDFs** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Cloud_PubSub_to_MongoDB_Xlang \
        --parameters \
    inputSubscription=INPUT_SUBSCRIPTION,\
    mongoDBUri=MONGODB_URI,\
    database=DATABASE,
    collection=COLLECTION,
    deadletterTable=UNPROCESSED_TABLE
      

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `INPUT_SUBSCRIPTION`: the Pub/Sub subscription (for example, ``projects/my-project-id/subscriptions/my-subscription-id``)
  * `MONGODB_URI`: the MongoDB server addresses (for example, `192.285.234.12:27017,192.287.123.11:27017`)
  * `DATABASE`: the name of the MongoDB database (for example, `users`)
  * `COLLECTION`: the name of the MongoDB collection (for example, `profiles`)
  * `UNPROCESSED_TABLE`: the name of the BigQuery table (for example, `your-project:your-dataset.your-table-name`)



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "inputSubscription": "INPUT_SUBSCRIPTION",
              "mongoDBUri": "MONGODB_URI",
              "database": "DATABASE",
              "collection": "COLLECTION",
              "deadletterTable": "UNPROCESSED_TABLE"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Cloud_PubSub_to_MongoDB_Xlang",
       }
    }
      

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `INPUT_SUBSCRIPTION`: the Pub/Sub subscription (for example, ``projects/my-project-id/subscriptions/my-subscription-id``)
  * `MONGODB_URI`: the MongoDB server addresses (for example, `192.285.234.12:27017,192.287.123.11:27017`)
  * `DATABASE`: the name of the MongoDB database (for example, `users`)
  * `COLLECTION`: the name of the MongoDB collection (for example, `profiles`)
  * `UNPROCESSED_TABLE`: the name of the BigQuery table (for example, `your-project:your-dataset.your-table-name`)



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
    package com.google.cloud.teleport.v2.templates;
    
    import com.google.auto.value.AutoValue;
    import com.google.cloud.teleport.metadata.MultiTemplate;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.templates.PubSubToMongoDB.Options;
    import com.google.cloud.teleport.v2.transforms.ErrorConverters;
    import com.google.cloud.teleport.v2.transforms.JavascriptTextTransformer;
    import com.google.cloud.teleport.v2.transforms.PythonExternalTextTransformer;
    import com.google.cloud.teleport.v2.utils.SchemaUtils;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.base.Strings;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import com.google.gson.JsonSyntaxException;
    import java.nio.charset.StandardCharsets;
    import javax.annotation.Nullable;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.CoderRegistry;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessageWithAttributesCoder;
    import org.apache.beam.sdk.io.mongodb.MongoDbIO;
    import org.apache.beam.sdk.metrics.Counter;
    import org.apache.beam.sdk.metrics.Metrics;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.PTransform;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.Row;
    import org.apache.beam.sdk.values.TupleTag;
    import org.apache.beam.sdk.values.TupleTagList;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.apache.beam.vendor.guava.v32_1_2_jre.com.google.common.base.Throwables;
    import org.bson.Document;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link PubSubToMongoDB} pipeline is a streaming pipeline which ingests data in JSON format
     * from PubSub, applies a Javascript UDF if provided and inserts resulting records as Bson Document
     * in MongoDB. If the element fails to be processed then it is written to a deadletter table in
     * BigQuery.
     *
     * <p><b>Pipeline Requirements</b>
     *
     * <ul>
     *   <li>The PubSub topic and subscriptions exist
     *   <li>The MongoDB is up and running
     * </ul>
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/pubsub-to-mongodb/README_Cloud_PubSub_to_MongoDB.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @MultiTemplate({
      @Template(
          name = "Cloud_PubSub_to_MongoDB",
          category = TemplateCategory.STREAMING,
          displayName = "Pub/Sub to MongoDB",
          description =
              "The Pub/Sub to MongoDB template is a streaming pipeline that reads JSON-encoded messages from a Pub/Sub subscription and writes them to MongoDB as documents. "
                  + "If required, this pipeline supports additional transforms that can be included using a JavaScript user-defined function (UDF). "
                  + "Any errors occurred due to schema mismatch, malformed JSON, or while executing transforms are recorded in a BigQuery table for unprocessed messages along with input message. "
                  + "If a table for unprocessed records does not exist prior to execution, the pipeline automatically creates this table.",
          skipOptions = {
            "pythonExternalTextTransformGcsPath",
            "pythonExternalTextTransformFunctionName"
          },
          optionsClass = Options.class,
          flexContainerName = "googlecloud-and-mongodb",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-mongodb",
          contactInformation = "https://cloud.google.com/support",
          preview = true,
          requirements = {
            "The Pub/Sub Subscription must exist and the messages must be encoded in a valid JSON format.",
            "The MongoDB cluster must exist and should be accessible from the Dataflow worker machines."
          },
          streaming = true,
          supportsAtLeastOnce = true),
      @Template(
          name = "Cloud_PubSub_to_MongoDB_Xlang",
          category = TemplateCategory.STREAMING,
          type = Template.TemplateType.XLANG,
          displayName = "Pub/Sub to MongoDB with Python UDFs",
          description =
              "The Pub/Sub to MongoDB template is a streaming pipeline that reads JSON-encoded messages from a Pub/Sub subscription and writes them to MongoDB as documents. "
                  + "If required, this pipeline supports additional transforms that can be included using a Python user-defined function (UDF). "
                  + "Any errors occurred due to schema mismatch, malformed JSON, or while executing transforms are recorded in a BigQuery table for unprocessed messages along with input message. "
                  + "If a table for unprocessed records does not exist prior to execution, the pipeline automatically creates this table.",
          skipOptions = {
            "javascriptTextTransformGcsPath",
            "javascriptTextTransformFunctionName",
            "javascriptTextTransformReloadIntervalMinutes"
          },
          optionsClass = Options.class,
          flexContainerName = "googlecloud-and-mongodb-xlang",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-mongodb",
          contactInformation = "https://cloud.google.com/support",
          preview = true,
          requirements = {
            "The Pub/Sub Subscription must exist and the messages must be encoded in a valid JSON format.",
            "The MongoDB cluster must exist and should be accessible from the Dataflow worker machines."
          },
          streaming = true,
          supportsAtLeastOnce = true)
    })
    public class PubSubToMongoDB {
      /**
       * Options supported by {@link PubSubToMongoDB}
       *
       * <p>Inherits standard configuration options.
       */
    
      /** The tag for the main output of the json transformation. */
      public static final TupleTag<FailsafeElement<PubsubMessage, String>> TRANSFORM_OUT =
          new TupleTag<FailsafeElement<PubsubMessage, String>>() {};
    
      /** The tag for the dead-letter output of the json to table row transform. */
      public static final TupleTag<FailsafeElement<PubsubMessage, String>> TRANSFORM_DEADLETTER_OUT =
          new TupleTag<FailsafeElement<PubsubMessage, String>>() {};
    
      /** Pubsub message/string coder for pipeline. */
      public static final FailsafeElementCoder<PubsubMessage, String> CODER =
          FailsafeElementCoder.of(PubsubMessageWithAttributesCoder.of(), StringUtf8Coder.of());
    
      /** String/String Coder for FailsafeElement. */
      public static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      /** The log to output status messages to. */
      private static final Logger LOG = LoggerFactory.getLogger(PubSubToMongoDB.class);
    
      /**
       * The {@link Options} class provides the custom execution options passed by the executor at the
       * command-line.
       *
       * <p>Inherits standard configuration options, options from {@link
       * PythonExternalTextTransformer.PythonExternalTextTransformerOptions}.
       */
      public interface Options
          extends PythonExternalTextTransformer.PythonExternalTextTransformerOptions, PipelineOptions {
        @TemplateParameter.PubsubSubscription(
            order = 1,
            groupName = "Source",
            description = "Pub/Sub input subscription",
            helpText = "Name of the Pub/Sub subscription.",
            example = "projects/your-project-id/subscriptions/your-subscription-name")
        @Validation.Required
        String getInputSubscription();
    
        void setInputSubscription(String inputSubscription);
    
        @TemplateParameter.Text(
            order = 2,
            groupName = "Target",
            description = "MongoDB Connection URI",
            helpText = "Comma separated list of MongoDB servers.",
            example = "host1:port,host2:port,host3:port")
        @Validation.Required
        String getMongoDBUri();
    
        void setMongoDBUri(String mongoDBUri);
    
        @TemplateParameter.Text(
            order = 3,
            groupName = "Target",
            description = "MongoDB Database",
            helpText = "Database in MongoDB to store the collection.",
            example = "my-db")
        @Validation.Required
        String getDatabase();
    
        void setDatabase(String database);
    
        @TemplateParameter.Text(
            order = 4,
            groupName = "Target",
            description = "MongoDB collection",
            helpText = "Name of the collection in the MongoDB database.",
            example = "my-collection")
        @Validation.Required
        String getCollection();
    
        void setCollection(String collection);
    
        @TemplateParameter.BigQueryTable(
            order = 5,
            description = "The dead-letter table name to output failed messages to BigQuery",
            helpText =
                "The BigQuery table that stores messages caused by failures, such as mismatched schema, malformed JSON, and so on.",
            example = "your-project-id:your-dataset.your-table-name")
        @Validation.Required
        String getDeadletterTable();
    
        void setDeadletterTable(String deadletterTable);
    
        @TemplateParameter.Long(
            order = 6,
            optional = true,
            description = "Batch Size",
            helpText = "Batch size used for batch insertion of documents into MongoDB.")
        @Default.Long(1000)
        Long getBatchSize();
    
        void setBatchSize(Long batchSize);
    
        @TemplateParameter.Long(
            order = 7,
            optional = true,
            description = "Batch Size in Bytes",
            helpText = "Batch size in bytes.")
        @Default.Long(5242880)
        Long getBatchSizeBytes();
    
        void setBatchSizeBytes(Long batchSizeBytes);
    
        @TemplateParameter.Integer(
            order = 8,
            optional = true,
            description = "Max Connection idle time",
            helpText = "Maximum idle time allowed in seconds before connection timeout occurs.")
        @Default.Integer(60000)
        int getMaxConnectionIdleTime();
    
        void setMaxConnectionIdleTime(int maxConnectionIdleTime);
    
        @TemplateParameter.Boolean(
            order = 9,
            optional = true,
            description = "SSL Enabled",
            helpText = "Boolean value indicating whether the connection to MongoDB is SSL enabled.")
        @Default.Boolean(true)
        Boolean getSslEnabled();
    
        void setSslEnabled(Boolean sslEnabled);
    
        @TemplateParameter.Boolean(
            order = 10,
            optional = true,
            description = "Ignore SSL Certificate",
            helpText = "Boolean value indicating whether to ignore the SSL certificate.")
        @Default.Boolean(true)
        Boolean getIgnoreSSLCertificate();
    
        void setIgnoreSSLCertificate(Boolean ignoreSSLCertificate);
    
        @TemplateParameter.Boolean(
            order = 11,
            optional = true,
            description = "withOrdered",
            helpText = "Boolean value enabling ordered bulk insertions into MongoDB.")
        @Default.Boolean(true)
        Boolean getWithOrdered();
    
        void setWithOrdered(Boolean withOrdered);
    
        @TemplateParameter.Boolean(
            order = 12,
            optional = true,
            description = "withSSLInvalidHostNameAllowed",
            helpText =
                "Boolean value indicating whether an invalid hostname is allowed for the SSL connection.")
        @Default.Boolean(true)
        Boolean getWithSSLInvalidHostNameAllowed();
    
        void setWithSSLInvalidHostNameAllowed(Boolean withSSLInvalidHostNameAllowed);
      }
    
      /** DoFn that will parse the given string elements as Bson Documents. */
      private static class ParseAsDocumentsFn extends DoFn<String, Document> {
    
        @ProcessElement
        public void processElement(ProcessContext context) {
          context.output(Document.parse(context.element()));
        }
      }
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        // Parse the user options passed from the command-line.
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        run(options);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      public static PipelineResult run(Options options) {
    
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        // Register the coders for pipeline
        CoderRegistry coderRegistry = pipeline.getCoderRegistry();
    
        coderRegistry.registerCoderForType(
            FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor(), FAILSAFE_ELEMENT_CODER);
    
        coderRegistry.registerCoderForType(CODER.getEncodedTypeDescriptor(), CODER);
    
        boolean usePythonUdf = !Strings.isNullOrEmpty(options.getPythonExternalTextTransformGcsPath());
        boolean useJavascriptUdf = !Strings.isNullOrEmpty(options.getJavascriptTextTransformGcsPath());
    
        if (usePythonUdf && useJavascriptUdf) {
          throw new IllegalArgumentException(
              "Either javascript or Python gcs path must be provided, but not both.");
        }
        /*
         * Steps: 1) Read PubSubMessage with attributes from input PubSub subscription.
         *        2) Apply Javascript or Python UDF if provided.
         *        3) Write to MongoDB
         *
         */
    
        LOG.info("Reading from subscription: " + options.getInputSubscription());
    
        PCollection<PubsubMessage> readMessagesFromPubsub =
            pipeline
                /*
                 * Step #1: Read from a PubSub subscription.
                 */
                .apply(
                "Read PubSub Subscription",
                PubsubIO.readMessagesWithAttributes().fromSubscription(options.getInputSubscription()));
    
        PCollectionTuple convertedPubsubMessages;
        if (usePythonUdf) {
          convertedPubsubMessages =
              readMessagesFromPubsub
                  /*
                   * Step #2: Apply Python Transform and transform, if provided and transform
                   *          the PubsubMessages into Json documents.
                   */
                  .apply(
                  "Apply Python UDF",
                  PubSubMessageToJsonDocument.newBuilder()
                      .setPythonExternalTextTransformFunctionName(
                          options.getPythonExternalTextTransformFunctionName())
                      .setPythonExternalTextTransformGcsPath(
                          options.getPythonExternalTextTransformGcsPath())
                      .build());
        } else {
          convertedPubsubMessages =
              readMessagesFromPubsub
                  /*
                   * Step #2: Apply Javascript Transform and transform, if provided and transform
                   *          the PubsubMessages into Json documents.
                   */
                  .apply(
                  "Apply Javascript UDF",
                  PubSubMessageToJsonDocument.newBuilder()
                      .setJavascriptTextTransformFunctionName(
                          options.getJavascriptTextTransformFunctionName())
                      .setJavascriptTextTransformGcsPath(options.getJavascriptTextTransformGcsPath())
                      .setJavascriptTextTransformReloadIntervalMinutes(
                          options.getJavascriptTextTransformReloadIntervalMinutes())
                      .build());
        }
    
        /*
         * Step #3a: Write Json documents into MongoDB using {@link MongoDbIO.write}.
         */
        convertedPubsubMessages
            .get(TRANSFORM_OUT)
            .apply(
                "Get Json Documents",
                MapElements.into(TypeDescriptors.strings()).via(FailsafeElement::getPayload))
            .apply("Parse as BSON Document", ParDo.of(new ParseAsDocumentsFn()))
            .apply(
                "Put to MongoDB",
                MongoDbIO.write()
                    .withBatchSize(options.getBatchSize())
                    .withUri(prefixMongoDb(options.getMongoDBUri()))
                    .withDatabase(options.getDatabase())
                    .withCollection(options.getCollection())
                    .withIgnoreSSLCertificate(options.getIgnoreSSLCertificate())
                    .withMaxConnectionIdleTime(options.getMaxConnectionIdleTime())
                    .withOrdered(options.getWithOrdered())
                    .withSSLEnabled(options.getSslEnabled())
                    .withSSLInvalidHostNameAllowed(options.getWithSSLInvalidHostNameAllowed()));
    
        /*
         * Step 3b: Write elements that failed processing to deadletter table via {@link BigQueryIO}.
         */
        convertedPubsubMessages
            .get(TRANSFORM_DEADLETTER_OUT)
            .apply(
                "Write Transform Failures To BigQuery",
                ErrorConverters.WritePubsubMessageErrors.newBuilder()
                    .setErrorRecordsTable(options.getDeadletterTable())
                    .setErrorRecordsTableSchema(SchemaUtils.DEADLETTER_SCHEMA)
                    .build());
    
        // Execute the pipeline and return the result.
        return pipeline.run();
      }
    
      /** Add the MongoDB protocol prefix only if the given uri doesn't have it. */
      private static String prefixMongoDb(String mongoDBUri) {
        if (mongoDBUri.startsWith("mongodb://") || mongoDBUri.startsWith("mongodb+srv://")) {
          return mongoDBUri;
        }
        return String.format("mongodb://%s", mongoDBUri);
      }
    
      /**
       * The {@link PubSubMessageToJsonDocument} class is a {@link PTransform} which transforms incoming
       * {@link PubsubMessage} objects into JSON objects for insertion into MongoDB while applying an
       * optional UDF to the input. The executions of the UDF and transformation to Json objects is done
       * in a fail-safe way by wrapping the element with it's original payload inside the {@link
       * FailsafeElement} class. The {@link PubSubMessageToJsonDocument} transform will output a {@link
       * PCollectionTuple} which contains all output and dead-letter {@link PCollection}.
       *
       * <p>The {@link PCollectionTuple} output will contain the following {@link PCollection}:
       *
       * <ul>
       *   <li>{@link PubSubToMongoDB#TRANSFORM_OUT} - Contains all records successfully converted to
       *       JSON objects.
       *   <li>{@link PubSubToMongoDB#TRANSFORM_DEADLETTER_OUT} - Contains all {@link FailsafeElement}
       *       records which couldn't be converted to table rows.
       * </ul>
       */
      @AutoValue
      public abstract static class PubSubMessageToJsonDocument
          extends PTransform<PCollection<PubsubMessage>, PCollectionTuple> {
    
        public static Builder newBuilder() {
          return new AutoValue_PubSubToMongoDB_PubSubMessageToJsonDocument.Builder();
        }
    
        @Nullable
        public abstract String javascriptTextTransformGcsPath();
    
        @Nullable
        public abstract String javascriptTextTransformFunctionName();
    
        @Nullable
        public abstract String pythonExternalTextTransformGcsPath();
    
        @Nullable
        public abstract String pythonExternalTextTransformFunctionName();
    
        @Nullable
        public abstract Integer javascriptTextTransformReloadIntervalMinutes();
    
        @Override
        public PCollectionTuple expand(PCollection<PubsubMessage> input) {
    
          // Check for python UDF first. If the pipeline is not using Python UDF, proceed as normal.
          if (pythonExternalTextTransformGcsPath() != null) {
            PCollection<Row> failsafeElements =
                input
                    // Map the incoming messages into FailsafeElements, so we can recover from failures
                    // across multiple transforms.
                    .apply(
                        "MapToRecord",
                        PythonExternalTextTransformer.FailsafeRowPythonExternalUdf
                            .pubSubMappingFunction())
                    .setRowSchema(
                        PythonExternalTextTransformer.FailsafeRowPythonExternalUdf.ROW_SCHEMA);
            return failsafeElements
                .apply(
                    "InvokeUDF",
                    PythonExternalTextTransformer.FailsafePythonExternalUdf.newBuilder()
                        .setFileSystemPath(pythonExternalTextTransformGcsPath())
                        .setFunctionName(pythonExternalTextTransformFunctionName())
                        .build())
                .apply(
                    "MapRowsToFailsafeElements",
                    ParDo.of(
                            new PythonExternalTextTransformer.RowToPubSubFailsafeElementFn(
                                TRANSFORM_OUT, TRANSFORM_DEADLETTER_OUT))
                        .withOutputTags(TRANSFORM_OUT, TupleTagList.of(TRANSFORM_DEADLETTER_OUT)));
          }
          // If we don't have Python UDF, we proceed as normal checking for Javascript UDF.
          // Map the incoming messages into FailsafeElements so we can recover from failures
          // across multiple transforms.
          PCollection<FailsafeElement<PubsubMessage, String>> failsafeElements =
              input.apply("MapToRecord", ParDo.of(new PubsubMessageToFailsafeElementFn()));
    
          // If a Udf is supplied then use it to parse the PubSubMessages.
          if (javascriptTextTransformGcsPath() != null) {
            return failsafeElements.apply(
                "InvokeUDF",
                JavascriptTextTransformer.FailsafeJavascriptUdf.<PubsubMessage>newBuilder()
                    .setFileSystemPath(javascriptTextTransformGcsPath())
                    .setFunctionName(javascriptTextTransformFunctionName())
                    .setReloadIntervalMinutes(javascriptTextTransformReloadIntervalMinutes())
                    .setSuccessTag(TRANSFORM_OUT)
                    .setFailureTag(TRANSFORM_DEADLETTER_OUT)
                    .build());
          } else {
            return failsafeElements.apply(
                "ProcessPubSubMessages",
                ParDo.of(new ProcessFailsafePubSubFn())
                    .withOutputTags(TRANSFORM_OUT, TupleTagList.of(TRANSFORM_DEADLETTER_OUT)));
          }
        }
    
        /** Builder for {@link PubSubMessageToJsonDocument}. */
        @AutoValue.Builder
        public abstract static class Builder {
          public abstract Builder setJavascriptTextTransformGcsPath(
              String javascriptTextTransformGcsPath);
    
          public abstract Builder setJavascriptTextTransformFunctionName(
              String javascriptTextTransformFunctionName);
    
          public abstract Builder setPythonExternalTextTransformGcsPath(
              String pythonExternalTextTransformGcsPath);
    
          public abstract Builder setPythonExternalTextTransformFunctionName(
              String pythonExternalTextTransformFunctionName);
    
          public abstract Builder setJavascriptTextTransformReloadIntervalMinutes(
              Integer javascriptTextTransformReloadIntervalMinutes);
    
          public abstract PubSubMessageToJsonDocument build();
        }
      }
    
      /**
       * The {@link ProcessFailsafePubSubFn} class processes a {@link FailsafeElement} containing a
       * {@link PubsubMessage} and a String of the message's payload {@link PubsubMessage#getPayload()}
       * into a {@link FailsafeElement} of the original {@link PubsubMessage} and a JSON string that has
       * been processed with {@link Gson}.
       *
       * <p>If {@link PubsubMessage#getAttributeMap()} is not empty then the message attributes will be
       * serialized along with the message payload.
       */
      static class ProcessFailsafePubSubFn
          extends DoFn<FailsafeElement<PubsubMessage, String>, FailsafeElement<PubsubMessage, String>> {
    
        private static final Counter successCounter =
            Metrics.counter(PubSubMessageToJsonDocument.class, "successful-json-conversion");
    
        private static Gson gson = new Gson();
    
        private static final Counter failedCounter =
            Metrics.counter(PubSubMessageToJsonDocument.class, "failed-json-conversion");
    
        @ProcessElement
        public void processElement(ProcessContext context) {
          PubsubMessage pubsubMessage = context.element().getOriginalPayload();
    
          JsonObject messageObject = new JsonObject();
    
          try {
            if (pubsubMessage.getPayload().length > 0) {
              messageObject =
                  gson.fromJson(
                      new String(pubsubMessage.getPayload(), StandardCharsets.UTF_8), JsonObject.class);
            }
    
            // If message attributes are present they will be serialized along with the message payload
            if (pubsubMessage.getAttributeMap() != null) {
              pubsubMessage.getAttributeMap().forEach(messageObject::addProperty);
            }
    
            context.output(FailsafeElement.of(pubsubMessage, messageObject.toString()));
            successCounter.inc();
    
          } catch (JsonSyntaxException e) {
            context.output(
                TRANSFORM_DEADLETTER_OUT,
                FailsafeElement.of(context.element())
                    .setErrorMessage(e.getMessage())
                    .setStacktrace(Throwables.getStackTraceAsString(e)));
            failedCounter.inc();
          }
        }
      }
    
      /**
       * The {@link PubsubMessageToFailsafeElementFn} wraps an incoming {@link PubsubMessage} with the
       * {@link FailsafeElement} class so errors can be recovered from and the original message can be
       * output to a error records table.
       */
      static class PubsubMessageToFailsafeElementFn
          extends DoFn<PubsubMessage, FailsafeElement<PubsubMessage, String>> {
        @ProcessElement
        public void processElement(ProcessContext context) {
          PubsubMessage message = context.element();
          context.output(
              FailsafeElement.of(message, new String(message.getPayload(), StandardCharsets.UTF_8)));
        }
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
