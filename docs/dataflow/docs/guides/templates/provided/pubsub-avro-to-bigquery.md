---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-avro-to-bigquery/
title: Pub/Sub Avro to BigQuery template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:27.336718+00:00
---

# Pub/Sub Avro to BigQuery template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-avro-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Pub/Sub Avro to BigQuery template Stay organized with collections  Save and categorize content based on your preferences. 

The Pub/Sub Avro to BigQuery template is a streaming pipeline that ingests Avro data from a Pub/Sub subscription into a BigQuery table. Any errors which occur while writing to the BigQuery table are streamed into a Pub/Sub unprocessed topic. 

Before running a Dataflow pipeline for this scenario, consider whether a [Pub/Sub BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/bigquery) with a [UDF](https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview) meets your requirements.

## Pipeline requirements

  * The input Pub/Sub subscription must exist.
  * The schema file for the Avro records must exist on Cloud Storage.
  * The unprocessed Pub/Sub topic must exist.
  * The output BigQuery dataset must exist.



## Template parameters

### Required parameters

  * **schemaPath** : The Cloud Storage location of the Avro schema file. For example, `gs://path/to/my/schema.avsc`.
  * **inputSubscription** : The Pub/Sub input subscription to read from. For example, `projects/<PROJECT_ID>/subscriptions/<SUBSCRIPTION_ID>`.
  * **outputTableSpec** : The BigQuery output table location to write the output to. For example, `<PROJECT_ID>:<DATASET_NAME>.<TABLE_NAME>`.Depending on the `createDisposition` specified, the output table might be created automatically using the user provided Avro schema.
  * **outputTopic** : The Pub/Sub topic to use for unprocessed records. For example, `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.



### Optional parameters

  * **useStorageWriteApiAtLeastOnce** : When using the Storage Write API, specifies the write semantics. To use at-least-once semantics (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics>), set this parameter to true. To use exactly-once semantics, set the parameter to `false`. This parameter applies only when `useStorageWriteApi` is `true`. The default value is `false`.
  * **writeDisposition** : The BigQuery WriteDisposition (<https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationload>) value. For example, `WRITE_APPEND`, `WRITE_EMPTY`, or `WRITE_TRUNCATE`. Defaults to `WRITE_APPEND`.
  * **createDisposition** : The BigQuery CreateDisposition (<https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationload>). For example, `CREATE_IF_NEEDED` and `CREATE_NEVER`. Defaults to `CREATE_IF_NEEDED`.
  * **useStorageWriteApi** : If true, the pipeline uses the BigQuery Storage Write API (<https://cloud.google.com/bigquery/docs/write-api>). The default value is `false`. For more information, see Using the Storage Write API (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#storage-write-api>).
  * **numStorageWriteApiStreams** : When using the Storage Write API, specifies the number of write streams. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter. Defaults to: 0.
  * **storageWriteApiTriggeringFrequencySec** : When using the Storage Write API, specifies the triggering frequency, in seconds. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Pub/Sub Avro to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/PubSub_Avro_to_BigQuery \
        --parameters \
    schemaPath=SCHEMA_PATH,\
    inputSubscription=SUBSCRIPTION_NAME,\
    outputTableSpec=BIGQUERY_TABLE,\
    outputTopic=DEADLETTER_TOPIC
      

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `SCHEMA_PATH`: the Cloud Storage path to the Avro schema file (for example, `gs://MyBucket/file.avsc`)
  * `SUBSCRIPTION_NAME`: the Pub/Sub input subscription name
  * `BIGQUERY_TABLE`: the BigQuery output table name
  * `DEADLETTER_TOPIC`: the Pub/Sub topic to use for the unprocessed queue



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/PubSub_Avro_to_BigQuery",
          "parameters": {
              "schemaPath": "SCHEMA_PATH",
              "inputSubscription": "SUBSCRIPTION_NAME",
              "outputTableSpec": "BIGQUERY_TABLE",
              "outputTopic": "DEADLETTER_TOPIC"
          }
       }
    }
      

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `SCHEMA_PATH`: the Cloud Storage path to the Avro schema file (for example, `gs://MyBucket/file.avsc`)
  * `SUBSCRIPTION_NAME`: the Pub/Sub input subscription name
  * `BIGQUERY_TABLE`: the BigQuery output table name
  * `DEADLETTER_TOPIC`: the Pub/Sub topic to use for the unprocessed queue



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2020 Google LLC
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
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.BigQueryCommonOptions.WriteOptions;
    import com.google.cloud.teleport.v2.options.BigQueryStorageApiStreamingOptions;
    import com.google.cloud.teleport.v2.options.PubsubCommonOptions.ReadSubscriptionOptions;
    import com.google.cloud.teleport.v2.options.PubsubCommonOptions.WriteTopicOptions;
    import com.google.cloud.teleport.v2.templates.PubsubAvroToBigQuery.PubsubAvroToBigQueryOptions;
    import com.google.cloud.teleport.v2.transforms.BigQueryConverters;
    import com.google.cloud.teleport.v2.transforms.ErrorConverters;
    import com.google.cloud.teleport.v2.utils.BigQueryIOUtils;
    import com.google.cloud.teleport.v2.utils.SchemaUtils;
    import org.apache.avro.Schema;
    import org.apache.avro.generic.GenericRecord;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.extensions.avro.coders.AvroCoder;
    import org.apache.beam.sdk.io.gcp.bigquery.WriteResult;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.schemas.transforms.Convert;
    import org.apache.beam.sdk.values.Row;
    
    /**
     * A Dataflow pipeline to stream <a href="https://avro.apache.org/">Apache Avro</a> records from
     * Pub/Sub into a BigQuery table.
     *
     * <p>Any persistent failures while writing to BigQuery will be written to a Pub/Sub dead-letter
     * topic.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/pubsub-binary-to-bigquery/README_PubSub_Avro_to_BigQuery.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "PubSub_Avro_to_BigQuery",
        category = TemplateCategory.STREAMING,
        displayName = "Pub/Sub Avro to BigQuery",
        description =
            "The Pub/Sub Avro to BigQuery template is a streaming pipeline that ingests Avro data from a Pub/Sub "
                + "subscription into a BigQuery table. Any errors which occur while writing to the BigQuery table are streamed into a Pub/Sub unprocessed topic.",
        optionsClass = PubsubAvroToBigQueryOptions.class,
        flexContainerName = "pubsub-binary-to-bigquery",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-avro-to-bigquery",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The input Pub/Sub subscription must exist.",
          "The schema file for the Avro records must exist on Cloud Storage.",
          "The unprocessed Pub/Sub topic must exist.",
          "The output BigQuery dataset must exist."
        },
        streaming = true,
        supportsAtLeastOnce = true)
    public final class PubsubAvroToBigQuery {
      /**
       * Validates input flags and executes the Dataflow pipeline.
       *
       * @param args command line arguments to the pipeline
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        PubsubAvroToBigQueryOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(PubsubAvroToBigQueryOptions.class);
    
        run(options);
      }
    
      /**
       * Provides custom {@link org.apache.beam.sdk.options.PipelineOptions} required to execute the
       * {@link PubsubAvroToBigQuery} pipeline.
       */
      public interface PubsubAvroToBigQueryOptions
          extends ReadSubscriptionOptions,
              WriteOptions,
              WriteTopicOptions,
              BigQueryStorageApiStreamingOptions {
    
        @TemplateParameter.GcsReadFile(
            order = 1,
            description = "Cloud Storage path to the Avro schema file",
            helpText =
                "The Cloud Storage location of the Avro schema file. For example, `gs://path/to/my/schema.avsc`.")
        @Required
        String getSchemaPath();
    
        void setSchemaPath(String schemaPath);
    
        // Hide the UseStorageWriteApiAtLeastOnce in the UI, because it will automatically be turned
        // on when pipeline is running on ALO mode and using the Storage Write API
        @TemplateParameter.Boolean(
            order = 2,
            optional = true,
            parentName = "useStorageWriteApi",
            parentTriggerValues = {"true"},
            description = "Use at at-least-once semantics in BigQuery Storage Write API",
            helpText =
                " When using the Storage Write API, specifies the write semantics. To use"
                    + " at-least-once semantics (https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics), set this parameter to true. To use exactly-once"
                    + " semantics, set the parameter to `false`. This parameter applies only when `useStorageWriteApi` is `true`. The default value is `false`.",
            hiddenUi = true)
        @Default.Boolean(false)
        @Override
        Boolean getUseStorageWriteApiAtLeastOnce();
    
        void setUseStorageWriteApiAtLeastOnce(Boolean value);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options execution parameters to the pipeline
       * @return result of the pipeline execution as a {@link PipelineResult}
       */
      private static PipelineResult run(PubsubAvroToBigQueryOptions options) {
        BigQueryIOUtils.validateBQStorageApiOptionsStreaming(options);
    
        // Create the pipeline.
        Pipeline pipeline = Pipeline.create(options);
    
        Schema schema = SchemaUtils.getAvroSchema(options.getSchemaPath());
    
        WriteResult writeResults =
            pipeline
                .apply(
                    "Read Avro records",
                    PubsubIO.readAvroGenericRecords(schema)
                        .fromSubscription(options.getInputSubscription())
                        .withDeadLetterTopic(options.getOutputTopic()))
                // Workaround for BEAM-12256. Eagerly convert to rows to avoid
                // the RowToGenericRecord function that doesn't handle all data
                // types.
                // TODO: Remove this workaround when a fix for BEAM-12256 is
                // released.
                .apply(Convert.toRows())
                .apply(
                    "Write to BigQuery",
                    BigQueryConverters.<Row>createWriteTransform(options).useBeamSchema());
    
        BigQueryIOUtils.writeResultToBigQueryInsertErrors(writeResults, options)
            .apply(
                "Create error payload",
                ErrorConverters.BigQueryInsertErrorToPubsubMessage.<GenericRecord>newBuilder()
                    .setPayloadCoder(AvroCoder.of(schema))
                    .setTranslateFunction(BigQueryConverters.TableRowToGenericRecordFn.of(schema))
                    .build())
            .apply("Write failed records", PubsubIO.writeMessages().to(options.getOutputTopic()));
    
        // Execute the pipeline and return the result.
        return pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
