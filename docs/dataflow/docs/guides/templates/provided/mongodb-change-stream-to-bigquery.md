---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/mongodb-change-stream-to-bigquery/
title: MongoDB to BigQuery template (Stream) \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:35.121926+00:00
---

# MongoDB to BigQuery template (Stream)  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/mongodb-change-stream-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  MongoDB to BigQuery template (Stream) Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This template creates a streaming pipeline that works with MongoDB [ change streams](https://www.mongodb.com/docs/manual/changeStreams/). To use this template, publish the change stream data to Pub/Sub. The pipeline reads the JSON records from Pub/Sub and writes them to BigQuery. The records written to BigQuery have the same format as the [ MongoDB to BigQuery batch template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/mongodb-to-bigquery).

## Pipeline requirements

  * The target BigQuery dataset must exist.
  * The source MongoDB instance must be accessible from the Dataflow worker machines.
  * You must create a Pub/Sub topic to read the change stream. While the pipeline is running, listen for change data capture (CDC) events on the MongoDB change stream and publish them to Pub/Sub as JSON records. For more information about publishing messages to Pub/Sub, see [Publish messages to topics](https://docs.cloud.google.com/pubsub/docs/publisher).
  * This template uses MongoDB [ change streams](https://www.mongodb.com/docs/manual/changeStreams/). It doesn't support BigQuery change data capture.



## Template parameters

### Required parameters

  * **mongoDbUri** : The MongoDB connection URI in the format `mongodb+srv://:@.`.
  * **database** : Database in MongoDB to read the collection from. For example, `my-db`.
  * **collection** : Name of the collection inside MongoDB database. For example, `my-collection`.
  * **userOption** : `FLATTEN`, `JSON`, or `NONE`. `FLATTEN` flattens the documents to the single level. `JSON` stores document in BigQuery JSON format. `NONE` stores the whole document as a JSON-formatted STRING. Defaults to: NONE.
  * **inputTopic** : The Pub/Sub input topic to read from, in the format of `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.
  * **outputTableSpec** : The BigQuery table to write to. For example, `bigquery-project:dataset.output_table`.



### Optional parameters

  * **useStorageWriteApiAtLeastOnce** : When using the Storage Write API, specifies the write semantics. To use at-least-once semantics (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics>), set this parameter to `true`. To use exactly- once semantics, set the parameter to `false`. This parameter applies only when `useStorageWriteApi` is `true`. The default value is `false`.
  * **KMSEncryptionKey** : Cloud KMS Encryption Key to decrypt the mongodb uri connection string. If Cloud KMS key is passed in, the mongodb uri connection string must all be passed in encrypted. For example, `projects/your-project/locations/global/keyRings/your-keyring/cryptoKeys/your-key`.
  * **filter** : Bson filter in json format. For example, `{ "val": { $gt: 0, $lt: 9 }}`.
  * **useStorageWriteApi** : If true, the pipeline uses the BigQuery Storage Write API (<https://cloud.google.com/bigquery/docs/write-api>). The default value is `false`. For more information, see Using the Storage Write API (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#storage-write-api>).
  * **numStorageWriteApiStreams** : When using the Storage Write API, specifies the number of write streams. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter. Defaults to: 0.
  * **storageWriteApiTriggeringFrequencySec** : When using the Storage Write API, specifies the triggering frequency, in seconds. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter.
  * **bigQuerySchemaPath** : The Cloud Storage path for the BigQuery JSON schema. For example, `gs://your-bucket/your-schema.json`.
  * **javascriptDocumentTransformGcsPath** : The Cloud Storage URI of the `.js` file that defines the JavaScript user-defined function (UDF) to use. For example, `gs://your-bucket/your-transforms/*.js`.
  * **javascriptDocumentTransformFunctionName** : The name of the JavaScript user-defined function (UDF) to use. For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is myTransform. For sample JavaScript UDFs, see UDF Examples (<https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples>). For example, `transform`.



## User-defined function

Optionally, you can extend this template by writing a user-defined function (UDF) in JavaScript. The template calls the UDF for each input element. Element payloads are serialized as JSON strings.

To use a UDF, upload the JavaScript file to Cloud Storage and set the following template parameters:

Parameter| Description  
---|---  
`javascriptDocumentTransformGcsPath` | The Cloud Storage location of the JavaScript file.  
`javascriptDocumentTransformFunctionName` | The name of the JavaScript function.  
  
For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

### Function specification

The UDF has the following specification:

* **Input** : a MongoDB document.
* **Output** : an object serialized as a JSON string.

## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **MongoDB (CDC) to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/MongoDB_to_BigQuery_CDC \
        --parameters \
    outputTableSpec=OUTPUT_TABLE_SPEC,\
    mongoDbUri=MONGO_DB_URI,\
    database=DATABASE,\
    collection=COLLECTION,\
    userOption=USER_OPTION,\
    inputTopic=INPUT_TOPIC

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `OUTPUT_TABLE_SPEC`: your target BigQuery table name.
  * `MONGO_DB_URI`: your MongoDB URI.
  * `DATABASE`: your MongoDB database.
  * `COLLECTION`: your MongoDB collection.
  * `USER_OPTION`: FLATTEN, JSON, or NONE.
  * `INPUT_TOPIC`: your Pub/Sub input topic.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "inputTableSpec": "INPUT_TABLE_SPEC",
              "mongoDbUri": "MONGO_DB_URI",
              "database": "DATABASE",
              "collection": "COLLECTION",
              "userOption": "USER_OPTION",
              "inputTopic": "INPUT_TOPIC"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/MongoDB_to_BigQuery_CDC",
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
  * `OUTPUT_TABLE_SPEC`: your target BigQuery table name.
  * `MONGO_DB_URI`: your MongoDB URI.
  * `DATABASE`: your MongoDB database.
  * `COLLECTION`: your MongoDB collection.
  * `USER_OPTION`: FLATTEN, JSON, or NONE.
  * `INPUT_TOPIC`: your Pub/Sub input topic.



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
    package com.google.cloud.teleport.v2.mongodb.templates;
    
    import static com.google.cloud.teleport.v2.utils.KMSUtils.maybeDecrypt;
    
    import com.google.api.services.bigquery.model.TableRow;
    import com.google.api.services.bigquery.model.TableSchema;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.mongodb.options.MongoDbToBigQueryOptions.BigQueryWriteOptions;
    import com.google.cloud.teleport.v2.mongodb.options.MongoDbToBigQueryOptions.JavascriptDocumentTransformerOptions;
    import com.google.cloud.teleport.v2.mongodb.options.MongoDbToBigQueryOptions.MongoDbOptions;
    import com.google.cloud.teleport.v2.mongodb.options.MongoDbToBigQueryOptions.PubSubOptions;
    import com.google.cloud.teleport.v2.mongodb.templates.MongoDbCdcToBigQuery.Options;
    import com.google.cloud.teleport.v2.options.BigQueryStorageApiStreamingOptions;
    import com.google.cloud.teleport.v2.transforms.JavascriptDocumentTransformer.TransformDocumentViaJavascript;
    import com.google.cloud.teleport.v2.utils.BigQueryIOUtils;
    import java.io.IOException;
    import javax.script.ScriptException;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.bson.Document;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link MongoDbCdcToBigQuery} pipeline is a streaming pipeline which reads data pushed to
     * PubSub from MongoDB Changestream and outputs the resulting records to BigQuery.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/mongodb-to-googlecloud/README_MongoDB_to_BigQuery_CDC.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "MongoDB_to_BigQuery_CDC",
        category = TemplateCategory.STREAMING,
        displayName = "MongoDB (CDC) to BigQuery",
        description =
            "The MongoDB CDC (Change Data Capture) to BigQuery template is a streaming pipeline that works together with MongoDB change streams. "
                + "The pipeline reads the JSON records pushed to Pub/Sub via a MongoDB change stream and writes them to BigQuery as specified by the <code>userOption</code> parameter.",
        optionsClass = Options.class,
        flexContainerName = "googlecloud-and-mongodb",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/mongodb-change-stream-to-bigquery",
        contactInformation = "https://cloud.google.com/support",
        preview = true,
        requirements = {
          "The target BigQuery dataset must exist.",
          "The source MongoDB instance must be accessible from the Dataflow worker machines.",
          "The change stream pushing changes from MongoDB to Pub/Sub should be running."
        },
        streaming = true,
        supportsAtLeastOnce = true)
    public class MongoDbCdcToBigQuery {
    
      private static final Logger LOG = LoggerFactory.getLogger(MongoDbCdcToBigQuery.class);
    
      /** Options interface. */
      public interface Options
          extends PipelineOptions,
              MongoDbOptions,
              PubSubOptions,
              BigQueryWriteOptions,
              JavascriptDocumentTransformerOptions,
              BigQueryStorageApiStreamingOptions {
    
        // Hide the UseStorageWriteApiAtLeastOnce in the UI, because it will automatically be turned
        // on when pipeline is running on ALO mode and using the Storage Write API
        @TemplateParameter.Boolean(
            order = 1,
            optional = true,
            parentName = "useStorageWriteApi",
            parentTriggerValues = {"true"},
            description = "Use at at-least-once semantics in BigQuery Storage Write API",
            helpText =
                "When using the Storage Write API, specifies the write semantics. To"
                    + " use at-least-once semantics (https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics), set this parameter to `true`. To use exactly-"
                    + " once semantics, set the parameter to `false`. This parameter applies only when"
                    + " `useStorageWriteApi` is `true`. The default value is `false`.",
            hiddenUi = true)
        @Default.Boolean(false)
        @Override
        Boolean getUseStorageWriteApiAtLeastOnce();
    
        void setUseStorageWriteApiAtLeastOnce(Boolean value);
      }
    
      /** class ParseAsDocumentsFn. */
      private static class ParseAsDocumentsFn extends DoFn<String, Document> {
    
        @ProcessElement
        public void processElement(ProcessContext context) {
          context.output(Document.parse(context.element()));
        }
      }
    
      /**
       * Main entry point for pipeline execution.
       *
       * @param args Command line arguments to the pipeline.
       */
      public static void main(String[] args)
          throws ScriptException, IOException, NoSuchMethodException {
        UncaughtExceptionLogger.register();
    
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        BigQueryIOUtils.validateBQStorageApiOptionsStreaming(options);
        run(options);
      }
    
      /** Pipeline to read data from PubSub and write to MongoDB. */
      public static boolean run(Options options)
          throws ScriptException, IOException, NoSuchMethodException {
        options.setStreaming(true);
        Pipeline pipeline = Pipeline.create(options);
        String userOption = options.getUserOption();
        String inputOption = options.getInputTopic();
    
        TableSchema bigquerySchema;
    
        // Get MongoDbUri
        String mongoDbUri = maybeDecrypt(options.getMongoDbUri(), options.getKMSEncryptionKey()).get();
    
        if (options.getJavascriptDocumentTransformFunctionName() != null
            && options.getJavascriptDocumentTransformGcsPath() != null) {
          bigquerySchema =
              MongoDbUtils.getTableFieldSchemaForUDF(
                  mongoDbUri,
                  options.getDatabase(),
                  options.getCollection(),
                  options.getJavascriptDocumentTransformGcsPath(),
                  options.getJavascriptDocumentTransformFunctionName(),
                  options.getUserOption());
        } else {
          bigquerySchema =
              MongoDbUtils.getTableFieldSchema(
                  mongoDbUri, options.getDatabase(), options.getCollection(), options.getUserOption());
        }
    
        pipeline
            .apply("Read PubSub Messages", PubsubIO.readStrings().fromTopic(inputOption))
            .apply(
                "RTransform string to document",
                ParDo.of(
                    new DoFn<String, Document>() {
                      @ProcessElement
                      public void process(ProcessContext c) {
                        Document document = Document.parse(c.element());
                        c.output(document);
                      }
                    }))
            .apply(
                "UDF",
                TransformDocumentViaJavascript.newBuilder()
                    .setFileSystemPath(options.getJavascriptDocumentTransformGcsPath())
                    .setFunctionName(options.getJavascriptDocumentTransformFunctionName())
                    .build())
            .apply(
                "Read and transform data",
                ParDo.of(
                    new DoFn<Document, TableRow>() {
                      @ProcessElement
                      public void process(ProcessContext c) {
                        Document document = c.element();
                        TableRow row = MongoDbUtils.getTableSchema(document, userOption);
                        c.output(row);
                      }
                    }))
            .apply(
                BigQueryIO.writeTableRows()
                    .to(options.getOutputTableSpec())
                    .withSchema(bigquerySchema)
                    .withCreateDisposition(BigQueryIO.Write.CreateDisposition.CREATE_IF_NEEDED)
                    .withWriteDisposition(BigQueryIO.Write.WriteDisposition.WRITE_APPEND));
        pipeline.run();
        return true;
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
