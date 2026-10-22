---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-proto-to-bigquery-python-udf/
title: Pub/Sub Proto to BigQuery with Python UDF template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:42.746831+00:00
---

# Pub/Sub Proto to BigQuery with Python UDF template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-proto-to-bigquery-python-udf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Pub/Sub Proto to BigQuery with Python UDF template Stay organized with collections  Save and categorize content based on your preferences. 

The Pub/Sub proto to BigQuery template is a streaming pipeline that ingests proto data from a Pub/Sub subscription into a BigQuery table. Any errors that occur while writing to the BigQuery table are streamed into a Pub/Sub unprocessed topic.  
  
A Python user-defined function (UDF) can be provided to transform data. Errors while executing the UDF can be sent to either a separate Pub/Sub topic or the same unprocessed topic as the BigQuery errors. 

Before running a Dataflow pipeline for this scenario, consider whether a [Pub/Sub BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/bigquery) with a [UDF](https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview) meets your requirements.

## Pipeline requirements

  * The input Pub/Sub subscription must exist.
  * The schema file for the Proto records must exist on Cloud Storage.
  * The output Pub/Sub topic must exist.
  * The output BigQuery dataset must exist.
  * If the BigQuery table exists, it must have a schema matching the proto data regardless of the `createDisposition` value.



## Template parameters

Parameter | Description  
---|---  
`protoSchemaPath` | The Cloud Storage location of the self-contained proto schema file. For example, `gs://path/to/my/file.pb`. This file can be generated with the `--descriptor_set_out` flag of the `protoc` command. The `--include_imports` flag guarantees that the file is self-contained.  
`fullMessageName` | The full proto message name. For example, `package.name.MessageName`, where `package.name` is the value provided for the `package` statement and not the `java_package` statement.  
`inputSubscription` | The Pub/Sub input subscription to read from. For example, `projects/<project>/subscriptions/<subscription>`.  
`outputTopic` | The Pub/Sub topic to use for unprocessed records. For example, `projects/<project-id>/topics/<topic-name>`.  
`outputTableSpec` | The BigQuery output table location. For example, `my-project:my_dataset.my_table`. Depending on the **createDisposition** specified, the output table might be created automatically using the input schema file.  
`preserveProtoFieldNames` | Optional: `true` to preserve the original Proto field name in JSON. `false` to use more standard JSON names. For example, `false` would change `field_name` to `fieldName`. (Default: `false`)  
`bigQueryTableSchemaPath` | Optional: Cloud Storage path to BigQuery schema path. For example, `gs://path/to/my/schema.json`. If this is not provided, then the schema is inferred from the Proto schema.  
`pythonExternalTextTransformGcsPath` | Optional: The Cloud Storage URI of the Python code file that defines the user-defined function (UDF) you want to use. For example, `gs://my-bucket/my-udfs/my_file.py`.   
`pythonExternalTextTransformFunctionName` | Optional: The name of the Python user-defined function (UDF) that you want to use.   
`udfOutputTopic` | Optional: The Pub/Sub topic storing the UDF errors. For example, `projects/<project-id>/topics/<topic-name>`. If this is not provided, UDF errors are sent to the same topic as `outputTopic`.  
`writeDisposition` | Optional: The BigQuery `WriteDisposition`. For example, `WRITE_APPEND`, `WRITE_EMPTY` or `WRITE_TRUNCATE`. Default: `WRITE_APPEND`.  
`createDisposition` | Optional: The BigQuery `CreateDisposition`. For example, `CREATE_IF_NEEDED`, `CREATE_NEVER`. Default: `CREATE_IF_NEEDED`.  
`useStorageWriteApi` | Optional: If `true`, the pipeline uses the [ BigQuery Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api). The default value is `false`. For more information, see [ Using the Storage Write API (gRPC)](https://beam.apache.org/documentation/io/built-in/google-bigquery/#storage-write-api).   
`useStorageWriteApiAtLeastOnce` | Optional: When using the Storage Write API (gRPC), specifies the write semantics. To use [ at-least-once semantics](https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics), set this parameter to `true`. To use exactly-once semantics, set the parameter to `false`. This parameter applies only when `useStorageWriteApi` is `true`. The default value is `false`.   
`numStorageWriteApiStreams` | Optional: When using the Storage Write API (gRPC), specifies the number of write streams. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter.   
`storageWriteApiTriggeringFrequencySec` | Optional: When using the Storage Write API (gRPC), specifies the triggering frequency, in seconds. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter.   
  
## User-defined function

Optionally, you can extend this template by writing a user-defined function (UDF). The template calls the UDF for each input element. Element payloads are serialized as JSON strings. For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

### Function specification

The UDF has the following specification:

* **Input** : the Pub/Sub message data field, serialized as a JSON string.
* **Output** : a JSON string that matches the schema of the BigQuery destination table.

## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Pub/Sub Proto to BigQuery with Python UDF** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/PubSub_Proto_to_BigQuery_Xlang \
        --parameters \
    schemaPath=SCHEMA_PATH,\
    fullMessageName=PROTO_MESSAGE_NAME,\
    inputSubscription=SUBSCRIPTION_NAME,\
    outputTableSpec=BIGQUERY_TABLE,\
    outputTopic=UNPROCESSED_TOPIC
      

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `SCHEMA_PATH`: the Cloud Storage path to the Proto schema file (for example, `gs://MyBucket/file.pb`)
  * `PROTO_MESSAGE_NAME`: the Proto message name (for example, `package.name.MessageName`)
  * `SUBSCRIPTION_NAME`: the Pub/Sub input subscription name
  * `BIGQUERY_TABLE`: the BigQuery output table name
  * `UNPROCESSED_TOPIC`: the Pub/Sub topic to use for the unprocessed queue



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/PubSub_Proto_to_BigQuery_Xlang",
          "parameters": {
              "schemaPath": "SCHEMA_PATH",
              "fullMessageName": "PROTO_MESSAGE_NAME",
              "inputSubscription": "SUBSCRIPTION_NAME",
              "outputTableSpec": "BIGQUERY_TABLE",
              "outputTopic": "UNPROCESSED_TOPIC"
          }
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
  * `SCHEMA_PATH`: the Cloud Storage path to the Proto schema file (for example, `gs://MyBucket/file.pb`)
  * `PROTO_MESSAGE_NAME`: the Proto message name (for example, `package.name.MessageName`)
  * `SUBSCRIPTION_NAME`: the Pub/Sub input subscription name
  * `BIGQUERY_TABLE`: the BigQuery output table name
  * `UNPROCESSED_TOPIC`: the Pub/Sub topic to use for the unprocessed queue



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
    package com.google.cloud.teleport.v2.templates;
    
    import static com.google.cloud.teleport.v2.transforms.PythonExternalTextTransformer.FailsafeRowPythonExternalUdf.stringMappingFunction;
    import static java.nio.charset.StandardCharsets.UTF_8;
    
    import com.google.cloud.teleport.metadata.MultiTemplate;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.BigQueryCommonOptions.WriteOptions;
    import com.google.cloud.teleport.v2.options.BigQueryStorageApiStreamingOptions;
    import com.google.cloud.teleport.v2.options.PubsubCommonOptions.ReadSubscriptionOptions;
    import com.google.cloud.teleport.v2.options.PubsubCommonOptions.WriteTopicOptions;
    import com.google.cloud.teleport.v2.templates.PubsubProtoToBigQuery.PubSubProtoToBigQueryOptions;
    import com.google.cloud.teleport.v2.transforms.BigQueryConverters;
    import com.google.cloud.teleport.v2.transforms.ErrorConverters;
    import com.google.cloud.teleport.v2.transforms.FailsafeElementTransforms.ConvertFailsafeElementToPubsubMessage;
    import com.google.cloud.teleport.v2.transforms.JavascriptTextTransformer.FailsafeJavascriptUdf;
    import com.google.cloud.teleport.v2.transforms.PythonExternalTextTransformer;
    import com.google.cloud.teleport.v2.transforms.PythonExternalTextTransformer.RowToStringFailsafeElementFn;
    import com.google.cloud.teleport.v2.utils.BigQueryIOUtils;
    import com.google.cloud.teleport.v2.utils.GCSUtils;
    import com.google.cloud.teleport.v2.utils.SchemaUtils;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.annotations.VisibleForTesting;
    import com.google.common.base.Strings;
    import com.google.protobuf.[Descriptors](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.html).[Descriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html);
    import com.google.protobuf.[DynamicMessage](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DynamicMessage.html);
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.NullableCoder;
    import org.apache.beam.sdk.coders.RowCoder;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write;
    import org.apache.beam.sdk.io.gcp.bigquery.WriteResult;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO.Read;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.PTransform;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.TupleTag;
    import org.apache.beam.sdk.values.TupleTagList;
    import org.apache.beam.sdk.values.TypeDescriptor;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.apache.commons.lang3.ArrayUtils;
    
    /**
     * A template for writing <a href="https://developers.google.com/protocol-buffers">Protobuf</a>
     * records from Pub/Sub to BigQuery.
     *
     * <p>Persistent failures are written to a Pub/Sub unprocessed topic.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/pubsub-binary-to-bigquery/README_PubSub_Proto_to_BigQuery.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @MultiTemplate({
      @Template(
          name = "PubSub_Proto_to_BigQuery_Flex",
          category = TemplateCategory.STREAMING,
          displayName = "Pub/Sub Proto to BigQuery",
          description = {
            "The Pub/Sub proto to BigQuery template is a streaming pipeline that ingests proto data from a Pub/Sub subscription into a BigQuery table. "
                + "Any errors that occur while writing to the BigQuery table are streamed into a Pub/Sub unprocessed topic.\n",
            "A JavaScript user-defined function (UDF) can be provided to transform data. "
                + "Errors while executing the UDF can be sent to either a separate Pub/Sub topic or the same unprocessed topic as the BigQuery errors."
          },
          skipOptions = {
            "pythonExternalTextTransformGcsPath",
            "pythonExternalTextTransformFunctionName"
          },
          optionsClass = PubSubProtoToBigQueryOptions.class,
          flexContainerName = "pubsub-binary-to-bigquery",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-proto-to-bigquery",
          contactInformation = "https://cloud.google.com/support",
          requirements = {
            "The input Pub/Sub subscription must exist.",
            "The schema file for the Proto records must exist on Cloud Storage.",
            "The output Pub/Sub topic must exist.",
            "The output BigQuery dataset must exist.",
            "If the BigQuery table exists, it must have a schema matching the proto data regardless of the <code>createDisposition</code> value."
          },
          streaming = true,
          supportsAtLeastOnce = true),
      @Template(
          name = "PubSub_Proto_to_BigQuery_Xlang",
          category = TemplateCategory.STREAMING,
          displayName = "Pub/Sub Proto to BigQuery with Python UDF",
          type = Template.TemplateType.XLANG,
          description = {
            "The Pub/Sub proto to BigQuery template is a streaming pipeline that ingests proto data from a Pub/Sub subscription into a BigQuery table. "
                + "Any errors that occur while writing to the BigQuery table are streamed into a Pub/Sub unprocessed topic.\n",
            "A Python user-defined function (UDF) can be provided to transform data. "
                + "Errors while executing the UDF can be sent to either a separate Pub/Sub topic or the same unprocessed topic as the BigQuery errors."
          },
          skipOptions = {
            "javascriptTextTransformGcsPath",
            "javascriptTextTransformFunctionName",
            "javascriptTextTransformReloadIntervalMinutes"
          },
          optionsClass = PubSubProtoToBigQueryOptions.class,
          flexContainerName = "pubsub-binary-to-bigquery-xlang",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-proto-to-bigquery",
          contactInformation = "https://cloud.google.com/support",
          requirements = {
            "The input Pub/Sub subscription must exist.",
            "The schema file for the Proto records must exist on Cloud Storage.",
            "The output Pub/Sub topic must exist.",
            "The output BigQuery dataset must exist.",
            "If the BigQuery table exists, it must have a schema matching the proto data regardless of the <code>createDisposition</code> value."
          },
          streaming = true,
          supportsAtLeastOnce = true)
    })
    public final class PubsubProtoToBigQuery {
      private static final TupleTag<FailsafeElement<String, String>> UDF_SUCCESS_TAG = new TupleTag<>();
      private static final TupleTag<FailsafeElement<String, String>> UDF_FAILURE_TAG = new TupleTag<>();
    
      private static final FailsafeElementCoder<String, String> FAILSAFE_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
        run(PipelineOptionsFactory.fromArgs(args).as(PubSubProtoToBigQueryOptions.class));
      }
    
      /** {@link org.apache.beam.sdk.options.PipelineOptions} for {@link PubsubProtoToBigQuery}. */
      public interface PubSubProtoToBigQueryOptions
          extends ReadSubscriptionOptions,
              WriteOptions,
              WriteTopicOptions,
              PythonExternalTextTransformer.PythonExternalTextTransformerOptions,
              BigQueryStorageApiStreamingOptions {
    
        @TemplateParameter.GcsReadFile(
            order = 1,
            description = "Cloud Storage Path to the Proto Schema File",
            helpText =
                "The Cloud Storage location of the self-contained proto schema file. For example,"
                    + " `gs://path/to/my/file.pb`. You can generate this file with"
                    + " the `--descriptor_set_out` flag of the protoc command."
                    + " The `--include_imports` flag guarantees that the file is self-contained.")
        @Required
        String getProtoSchemaPath();
    
        void setProtoSchemaPath(String value);
    
        @TemplateParameter.Text(
            order = 2,
            regexes = {"^.+([a-zA-Z][a-zA-Z0-9_]+\\.?)+[a-zA-Z0-9_]$"},
            description = "Full Proto Message Name",
            helpText =
                "The full proto message name. For example, `package.name`."
                    + " `MessageName`, where `package.name` is the value provided for the"
                    + " `package` statement and not the `java_package` statement.")
        @Required
        String getFullMessageName();
    
        void setFullMessageName(String value);
    
        @TemplateParameter.Boolean(
            order = 3,
            optional = true,
            description = "Preserve Proto Field Names",
            helpText =
                "To preserve the original proto field name in JSON, set this property to `true`. "
                    + "To use more standard JSON names, set to `false`."
                    + " For example, `false` would change `field_name` to `fieldName`. Defaults to: `false`.")
        @Default.Boolean(false)
        Boolean getPreserveProtoFieldNames();
    
        void setPreserveProtoFieldNames(Boolean value);
    
        @TemplateParameter.GcsReadFile(
            order = 4,
            optional = true,
            description = "BigQuery Table Schema Path",
            helpText =
                "The Cloud Storage path to the BigQuery schema path. "
                    + "If this value isn't provided, then the schema is inferred from the Proto schema.",
            example = "gs://MyBucket/bq_schema.json")
        String getBigQueryTableSchemaPath();
    
        void setBigQueryTableSchemaPath(String value);
    
        @TemplateParameter.PubsubTopic(
            order = 5,
            optional = true,
            description = "Pub/Sub output topic for UDF failures",
            helpText =
                "The Pub/Sub topic storing the UDF errors."
                    + " If this value isn't provided, UDF errors are sent to the same topic as `outputTopic`.",
            example = "projects/your-project-id/topics/your-topic-name")
        String getUdfOutputTopic();
    
        void setUdfOutputTopic(String udfOutputTopic);
    
        // Hide the UseStorageWriteApiAtLeastOnce in the UI, because it will automatically be turned
        // on when pipeline is running on ALO mode and using the Storage Write API
        @TemplateParameter.Boolean(
            order = 6,
            optional = true,
            parentName = "useStorageWriteApi",
            parentTriggerValues = {"true"},
            description = "Use at at-least-once semantics in BigQuery Storage Write API",
            helpText =
                "When using the Storage Write API, specifies the write semantics."
                    + " To use at-least-once semantics (https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics), set this parameter to true`. To use exactly-once semantics, set the parameter to `false`."
                    + " This parameter applies only when `useStorageWriteApi` is `true`. The default value is `false`.",
            hiddenUi = true)
        @Default.Boolean(false)
        @Override
        Boolean getUseStorageWriteApiAtLeastOnce();
    
        void setUseStorageWriteApiAtLeastOnce(Boolean value);
      }
    
      /** Runs the pipeline and returns the results. */
      private static PipelineResult run(PubSubProtoToBigQueryOptions options) {
        BigQueryIOUtils.validateBQStorageApiOptionsStreaming(options);
    
        Pipeline pipeline = Pipeline.create(options);
    
        [Descriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html) descriptor = getDescriptor(options);
        PCollection<String> maybeForUdf =
            pipeline
                .apply("Read From Pubsub", readPubsubMessages(options, descriptor))
                .apply("Dynamic Message to TableRow", new ConvertDynamicProtoMessageToJson(options));
    
        WriteResult writeResult =
            runUdf(maybeForUdf, options)
                .apply("Write to BigQuery", writeToBigQuery(options, descriptor));
        BigQueryIOUtils.writeResultToBigQueryInsertErrors(writeResult, options)
            .apply(
                "Create Error Payload",
                ErrorConverters.BigQueryInsertErrorToPubsubMessage.<String>newBuilder()
                    .setPayloadCoder(StringUtf8Coder.of())
                    .setTranslateFunction(BigQueryConverters::tableRowToJson)
                    .build())
            .apply("Write Failed BQ Records", PubsubIO.writeMessages().to(options.getOutputTopic()));
    
        return pipeline.[run](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.RpcCallback.html#com_google_protobuf_RpcCallback_run_ParameterType_)();
      }
    
      /** Gets the {@link Descriptor} for the message type in the Pub/Sub topic. */
      @VisibleForTesting
      static [Descriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html) getDescriptor(PubSubProtoToBigQueryOptions options) {
        String schemaPath = options.getProtoSchemaPath();
        String messageName = options.getFullMessageName();
        [Descriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html) descriptor = SchemaUtils.getProtoDomain(schemaPath).getDescriptor(messageName);
    
        if (descriptor == null) {
          throw new IllegalArgumentException(
              messageName + " is not a recognized message in " + schemaPath);
        }
    
        return descriptor;
      }
    
      /** Returns the {@link PTransform} for reading Pub/Sub messages. */
      private static Read<DynamicMessage> readPubsubMessages(
          PubSubProtoToBigQueryOptions options, [Descriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html) descriptor) {
        return PubsubIO.readProtoDynamicMessages(descriptor)
            .fromSubscription(options.getInputSubscription())
            .withDeadLetterTopic(options.getOutputTopic());
      }
    
      /**
       * Writes messages to BigQuery, creating the table if necessary and allowed in {@code options}.
       *
       * <p>The BigQuery schema will be inferred from {@code descriptor} unless a JSON schema path is
       * specified in {@code options}.
       */
      @VisibleForTesting
      static Write<String> writeToBigQuery(
          PubSubProtoToBigQueryOptions options, [Descriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html) descriptor) {
        Write<String> write =
            BigQueryConverters.<String>createWriteTransform(options)
                .withFormatFunction(BigQueryConverters::convertJsonToTableRow);
    
        String schemaPath = options.getBigQueryTableSchemaPath();
        if (Strings.isNullOrEmpty(schemaPath)) {
          return write.withSchema(
              SchemaUtils.createBigQuerySchema(descriptor, options.getPreserveProtoFieldNames()));
        } else {
          return write.withJsonSchema(GCSUtils.getGcsFileAsString(schemaPath));
        }
      }
    
      /** {@link PTransform} that handles converting {@link PubsubMessage} values to JSON. */
      private static class ConvertDynamicProtoMessageToJson
          extends PTransform<PCollection<DynamicMessage>, PCollection<String>> {
        private final boolean preserveProtoName;
    
        private ConvertDynamicProtoMessageToJson(PubSubProtoToBigQueryOptions options) {
          this.preserveProtoName = options.getPreserveProtoFieldNames();
        }
    
        @Override
        public PCollection<String> expand(PCollection<DynamicMessage> input) {
          return input.apply(
              "Map to JSON",
              MapElements.into(TypeDescriptors.strings())
                  .via(
                      message -> {
                        try {
                          JsonFormat.Printer printer = [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).printer();
                          return preserveProtoName
                              ? printer.preservingProtoFieldNames().print(message)
                              : printer.print(message);
                        } catch (InvalidProtocolBufferException e) {
                          throw new RuntimeException(e);
                        }
                      }));
        }
      }
    
      /**
       * Handles running the UDF.
       *
       * <p>If {@code options} is configured so as not to run the UDF, then the UDF will not be called.
       *
       * <p>This may add a branch to the pipeline for outputting failed UDF records to an unprocessed
       * topic.
       *
       * @param jsonCollection {@link PCollection} of JSON strings for use as input to the UDF
       * @param options the options containing info on running the UDF
       * @return the {@link PCollection} of UDF output as JSON or {@code jsonCollection} if UDF not
       *     called
       */
      @VisibleForTesting
      static PCollection<String> runUdf(
          PCollection<String> jsonCollection, PubSubProtoToBigQueryOptions options) {
    
        boolean useJavascriptUdf = !Strings.isNullOrEmpty(options.getJavascriptTextTransformGcsPath());
        boolean usePythonUdf = !Strings.isNullOrEmpty(options.getPythonExternalTextTransformGcsPath());
    
        // In order to avoid generating a graph that makes it look like a UDF was called when none was
        // intended, simply return the input as "success" output.
        if (!useJavascriptUdf && !usePythonUdf) {
          return jsonCollection;
        }
    
        // For testing purposes, we need to do this check before creating the PTransform rather than
        // in `expand`. Otherwise, we get a NullPointerException due to the PTransform not returning
        // a value.
        if (useJavascriptUdf
            && Strings.isNullOrEmpty(options.getJavascriptTextTransformFunctionName())) {
          throw new IllegalArgumentException(
              "JavaScript function name cannot be null or empty if file is set");
        }
        if (usePythonUdf
            && Strings.isNullOrEmpty(options.getPythonExternalTextTransformFunctionName())) {
          throw new IllegalArgumentException(
              "Python function name cannot be null or empty if file is set");
        }
        if (usePythonUdf && useJavascriptUdf) {
          throw new IllegalArgumentException(
              "Either javascript or Python gcs path must be provided, but not both.");
        }
    
        PCollectionTuple maybeSuccess;
        if (usePythonUdf) {
          maybeSuccess = jsonCollection.apply("Run UDF", new RunPythonUdf(options));
        } else {
          maybeSuccess = jsonCollection.apply("Run UDF", new RunUdf(options));
        }
    
        maybeSuccess
            .get(UDF_FAILURE_TAG)
            .setCoder(FAILSAFE_CODER)
            .apply(
                "Get UDF Failures",
                ConvertFailsafeElementToPubsubMessage.<String, String>builder()
                    .setOriginalPayloadSerializeFn(s -> ArrayUtils.toObject(s.getBytes(UTF_8)))
                    .setErrorMessageAttributeKey("udfErrorMessage")
                    .build())
            .apply("Write Failed UDF", writeUdfFailures(options));
    
        return maybeSuccess
            .get(UDF_SUCCESS_TAG)
            .setCoder(FAILSAFE_CODER)
            .apply(
                "Get UDF Output",
                MapElements.into(TypeDescriptors.strings()).via(FailsafeElement::getPayload))
            .setCoder(NullableCoder.of(StringUtf8Coder.of()));
      }
    
      /** {@link PTransform} that calls a UDF and returns both success and failure output. */
      private static class RunUdf extends PTransform<PCollection<String>, PCollectionTuple> {
        private final PubSubProtoToBigQueryOptions options;
    
        RunUdf(PubSubProtoToBigQueryOptions options) {
          this.options = options;
        }
    
        @Override
        public PCollectionTuple expand(PCollection<String> input) {
          return input
              .apply("Prepare Failsafe UDF", makeFailsafe())
              .setCoder(FAILSAFE_CODER)
              .apply(
                  "Call UDF",
                  FailsafeJavascriptUdf.<String>newBuilder()
                      .setFileSystemPath(options.getJavascriptTextTransformGcsPath())
                      .setFunctionName(options.getJavascriptTextTransformFunctionName())
                      .setReloadIntervalMinutes(
                          options.getJavascriptTextTransformReloadIntervalMinutes())
                      .setSuccessTag(UDF_SUCCESS_TAG)
                      .setFailureTag(UDF_FAILURE_TAG)
                      .build());
        }
    
        private static MapElements<String, FailsafeElement<String, String>> makeFailsafe() {
          return MapElements.into(new TypeDescriptor<FailsafeElement<String, String>>() {})
              .via((String json) -> FailsafeElement.of(json, json));
        }
      }
    
      /** {@link PTransform} that calls a python UDF and returns both success and failure output. */
      private static class RunPythonUdf extends PTransform<PCollection<String>, PCollectionTuple> {
        private final PubSubProtoToBigQueryOptions options;
    
        RunPythonUdf(PubSubProtoToBigQueryOptions options) {
          this.options = options;
        }
    
        @Override
        public PCollectionTuple expand(PCollection<String> input) {
          return input
              .apply("Prepare Failsafe row", stringMappingFunction())
              .setCoder(
                  RowCoder.of(PythonExternalTextTransformer.FailsafeRowPythonExternalUdf.ROW_SCHEMA))
              .apply(
                  "InvokeUDF",
                  PythonExternalTextTransformer.FailsafePythonExternalUdf.newBuilder()
                      .setFileSystemPath(options.getPythonExternalTextTransformGcsPath())
                      .setFunctionName(options.getPythonExternalTextTransformFunctionName())
                      .build())
              .apply(
                  "MapRowsToFailsafeElements",
                  ParDo.of(new RowToStringFailsafeElementFn(UDF_SUCCESS_TAG, UDF_FAILURE_TAG))
                      .withOutputTags(UDF_SUCCESS_TAG, TupleTagList.of(UDF_FAILURE_TAG)));
        }
      }
    
      /**
       * Returns a {@link PubsubIO.Write} configured to write UDF failures to the appropriate output
       * topic.
       */
      private static PubsubIO.Write<PubsubMessage> writeUdfFailures(
          PubSubProtoToBigQueryOptions options) {
        PubsubIO.Write<PubsubMessage> write = PubsubIO.writeMessages();
        return Strings.isNullOrEmpty(options.getUdfOutputTopic())
            ? write.to(options.getOutputTopic())
            : write.to(options.getUdfOutputTopic());
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
