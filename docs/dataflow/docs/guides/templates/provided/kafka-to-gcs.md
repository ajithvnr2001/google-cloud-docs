---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-gcs/
title: Apache Kafka to Cloud Storage template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:08.782215+00:00
---

# Apache Kafka to Cloud Storage template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Apache Kafka to Cloud Storage template Stay organized with collections  Save and categorize content based on your preferences. 

The Apache Kafka to Cloud Storage template is a streaming pipeline that ingests text data from [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs) and outputs the records to Cloud Storage. 

You can also use the Apache Kafka to Cloud Storage template with self-managed or external Kafka. 

## Pipeline requirements

  * The output Cloud Storage bucket must exist.
  * The Apache Kafka broker server must be running and be reachable from the Dataflow worker machines.
  * The Apache Kafka topics must exist.



## Kafka message format

This template supports reading messages from Kafka in the following formats:

  * JSON
  * Avro binary encoding
  * Confluent Schema Registry–encoded Avro



### JSON format

To read JSON messages, set the `messageFormat` template parameter to `"JSON"`.

### Avro binary encoding

To read binary Avro messages, set the following template parameters:

  * `messageFormat`: `"AVRO_BINARY_ENCODING"`.
  * `binaryAvroSchemaPath`: The location of an Avro schema file in Cloud Storage. Example: `gs://BUCKET_NAME/message-schema.avsc`. 



For more information about Avro binary format, see [Binary encoding](https://avro.apache.org/docs/1.8.1/spec.html#binary_encoding) in the Apache Avro documentation.

### Confluent Schema Registry–encoded Avro

To read messages in Confluent Schema Registry–encoded Avro, set the following template parameters:

  * `messageFormat`: `"AVRO_CONFLUENT_WIRE_FORMAT"`. 
  * `schemaFormat`: One of the following values: 
    * `"SINGLE_SCHEMA_FILE"`: The message schema is defined in an Avro schema file. Specify the Cloud Storage location of the schema file in the `confluentAvroSchemaPath` parameter.
    * `"SCHEMA_REGISTRY"`: The messages are encoded using Confluent Schema Registry. Specify the URL of the Confluent Schema Registry instance in the `schemaRegistryConnectionUrl` parameter, and specify the authentication mode in the `schemaRegistryAuthenticationMode` parameter. 



For more information about this format, see [ Wire format](https://docs.confluent.io/platform/current/schema-registry/fundamentals/serdes-develop/index.html#wire-format) in the Confluent documentation.

## Output file format

The output file format is the same format as the input Kafka message. For example, if you select **JSON** for the Kafka message format, JSON files are written to the output Cloud Storage bucket. 

## Authentication

The Apache Kafka to Cloud Storage template supports [SASL/PLAIN](https://kafka.apache.org/documentation/#security_sasl_plain) authentication to Kafka brokers. 

## Template parameters

### Required parameters

  * **readBootstrapServerAndTopic** : Kafka Topic to read the input from.
  * **outputDirectory** : The path and filename prefix for writing output files. Must end with a slash. For example, `gs://your-bucket/your-path/`.
  * **kafkaReadAuthenticationMode** : The mode of authentication to use with the Kafka cluster. Use `NONE` for no authentication, `SASL_PLAIN` for SASL/PLAIN username and password, `SASL_SCRAM_512` for SASL_SCRAM_512 authentication and `TLS` for certificate-based authentication. `APPLICATION_DEFAULT_CREDENTIALS` should be used only for Google Cloud Managed Service for Apache Kafka cluster, it allows to authenticate using application default credentials.
  * **messageFormat** : The format of the Kafka messages to read. The supported values are `AVRO_CONFLUENT_WIRE_FORMAT` (Confluent Schema Registry encoded Avro), `AVRO_BINARY_ENCODING` (Plain binary Avro), and `JSON`. Defaults to: AVRO_CONFLUENT_WIRE_FORMAT.
  * **useBigQueryDLQ** : If true, failed messages will be written to BigQuery with extra error information. Defaults to: false.



### Optional parameters

  * **windowDuration** : The window duration/size in which data will be written to Cloud Storage. Allowed formats are: Ns (for seconds, example: 5s), Nm (for minutes, example: 12m), Nh (for hours, example: 2h). For example, `5m`. Defaults to: 5m.
  * **outputFilenamePrefix** : The prefix to place on each windowed file. For example, `output-`. Defaults to: output.
  * **numShards** : The maximum number of output shards produced when writing. A higher number of shards means higher throughput for writing to Cloud Storage, but potentially higher data aggregation cost across shards when processing output Cloud Storage files. Default value is decided by Dataflow.
  * **enableCommitOffsets** : Commit offsets of processed messages to Kafka. If enabled, this will minimize the gaps or duplicate processing of messages when restarting the pipeline. Requires specifying the Consumer Group ID. Defaults to: false.
  * **consumerGroupId** : The unique identifier for the consumer group that this pipeline belongs to. Required if Commit Offsets to Kafka is enabled. Defaults to empty.
  * **kafkaReadOffset** : The starting point for reading messages when no committed offsets exist. The earliest starts from the beginning, the latest from the newest message. Defaults to: latest.
  * **kafkaReadUsernameSecretId** : The Google Cloud Secret Manager secret ID that contains the Kafka username to use with `SASL_PLAIN` authentication. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`. Defaults to empty.
  * **kafkaReadPasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the Kafka password to use with `SASL_PLAIN` authentication. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`. Defaults to empty.
  * **kafkaReadKeystoreLocation** : The Google Cloud Storage path to the Java KeyStore (JKS) file that contains the TLS certificate and private key to use when authenticating with the Kafka cluster. For example, `gs://your-bucket/keystore.jks`.
  * **kafkaReadTruststoreLocation** : The Google Cloud Storage path to the Java TrustStore (JKS) file that contains the trusted certificates to use to verify the identity of the Kafka broker.
  * **kafkaReadTruststorePasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the password to use to access the Java TrustStore (JKS) file for Kafka TLS authentication For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.
  * **kafkaReadKeystorePasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the password to use to access the Java KeyStore (JKS) file for Kafka TLS authentication. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.
  * **kafkaReadKeyPasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the password to use to access the private key within the Java KeyStore (JKS) file for Kafka TLS authentication. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.
  * **kafkaReadSaslScramUsernameSecretId** : The Google Cloud Secret Manager secret ID that contains the Kafka username to use with `SASL_SCRAM` authentication. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.
  * **kafkaReadSaslScramPasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the Kafka password to use with `SASL_SCRAM` authentication. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.
  * **kafkaReadSaslScramTruststoreLocation** : The Google Cloud Storage path to the Java TrustStore (JKS) file that contains the trusted certificates to use to verify the identity of the Kafka broker.
  * **kafkaReadSaslScramTruststorePasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the password to use to access the Java TrustStore (JKS) file for Kafka SASL_SCRAM authentication For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.
  * **schemaFormat** : The Kafka schema format. Can be provided as `SINGLE_SCHEMA_FILE` or `SCHEMA_REGISTRY`. If `SINGLE_SCHEMA_FILE` is specified, use the schema mentioned in the avro schema file for all messages. If `SCHEMA_REGISTRY` is specified, the messages can have either a single schema or multiple schemas. Defaults to: SINGLE_SCHEMA_FILE.
  * **confluentAvroSchemaPath** : The Google Cloud Storage path to the single Avro schema file used to decode all of the messages in a topic. Defaults to empty.
  * **schemaRegistryConnectionUrl** : The URL for the Confluent Schema Registry instance used to manage Avro schemas for message decoding. Defaults to empty.
  * **binaryAvroSchemaPath** : The Google Cloud Storage path to the Avro schema file used to decode binary-encoded Avro messages. Defaults to empty.
  * **schemaRegistryAuthenticationMode** : The mode of authentication to use with the Schema Registry. Use `NONE` for no authentication, `TLS` for certificate-based authentication and `OAUTH` for OAuth2 authentication. `APPLICATION_DEFAULT_CREDENTIALS` should be used only for Google Cloud Managed Service for Apache Kafka Schema Registry, it allows to authenticate using application default credentials.
  * **schemaRegistryTruststoreLocation** : Location of the SSL certificate where the trust store for authentication to Schema Registry are stored. For example, `/your-bucket/truststore.jks`.
  * **schemaRegistryTruststorePasswordSecretId** : SecretId in secret manager where the password to access secret in truststore is stored. For example, `projects/your-project-number/secrets/your-secret-name/versions/your-secret-version`.
  * **schemaRegistryKeystoreLocation** : Keystore location that contains the SSL certificate and private key. For example, `/your-bucket/keystore.jks`.
  * **schemaRegistryKeystorePasswordSecretId** : SecretId in secret manager where the password to access the keystore file For example, `projects/your-project-number/secrets/your-secret-name/versions/your-secret-version`.
  * **schemaRegistryKeyPasswordSecretId** : SecretId of password required to access the client's private key stored within the keystore For example, `projects/your-project-number/secrets/your-secret-name/versions/your-secret-version`.
  * **schemaRegistryOauthClientId** : Client ID used to authenticate the Schema Registry client in OAUTH mode. Required for AVRO_CONFLUENT_WIRE_FORMAT message format.
  * **schemaRegistryOauthClientSecretId** : The Google Cloud Secret Manager secret ID that contains the Client Secret to use to authenticate the Schema Registry client in OAUTH mode. Required for AVRO_CONFLUENT_WIRE_FORMAT message format. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.
  * **schemaRegistryOauthScope** : The access token scope used to authenticate the Schema Registry client in OAUTH mode. This field is optional, as the request can be made without a scope parameter passed. For example, `openid`.
  * **schemaRegistryOauthTokenEndpointUrl** : The HTTP(S)-based URL for the OAuth/OIDC identity provider used to authenticate the Schema Registry client in OAUTH mode. Required for AVRO_CONFLUENT_WIRE_FORMAT message format.
  * **outputDeadletterTable** : Fully Qualified BigQuery table name for failed messages. Messages failed to reach the output table for different reasons (e.g., mismatched schema, malformed json) are written to this table.The table will be created by the template. For example, `your-project-id:your-dataset.your-table-name`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Kafka to Cloud Storage** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Optional: To switch from exactly-once processing to [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes), select **At Least Once**.
  7. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Kafka_to_Gcs_Flex \
        --parameters \
    readBootstrapServerAndTopic=BOOTSTRAP_SERVER_AND_TOPIC,\
    kafkaReadAuthenticationMode=APPLICATION_DEFAULT_CREDENTIALS,\
    messageFormat=JSON,\
    outputDirectory=gs://STORAGE_BUCKET_NAME,\
    useBigQueryDLQ=false
      

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `BOOTSTRAP_SERVER_AND_TOPIC`: the Apache Kafka bootstrap server address and topic 

The format of the bootstrap server address and topic depends on the type of cluster:

    * Managed Service for Apache Kafka cluster: `projects/PROJECT_ID/locations/REGION_NAME/clusters/CLUSTER_NAME/topics/TOPIC_NAME`
    * External Kafka cluster: `BOOTSTRAP_SERVER_ADDRESS;TOPIC_NAME`
  * `STORAGE_BUCKET_NAME`: the Cloud Storage bucket where the output is written



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "readBootstrapServerAndTopic": "BOOTSTRAP_SERVER_AND_TOPIC",
              "kafkaReadAuthenticationMode": "APPLICATION_DEFAULT_CREDENTIALS",
              "messageFormat": "JSON",
              "outputDirectory": "gs://STORAGE_BUCKET_NAME",
              "useBigQueryDLQ": "false"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Kafka_to_Gcs_Flex",
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
  * `BOOTSTRAP_SERVER_AND_TOPIC`: the Apache Kafka bootstrap server address and topic 

The format of the bootstrap server address and topic depends on the type of cluster:

    * Managed Service for Apache Kafka cluster: `projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME/topics/TOPIC_NAME`
    * External Kafka cluster: `BOOTSTRAP_SERVER_ADDRESS;TOPIC_NAME`
  * `STORAGE_BUCKET_NAME`: the Cloud Storage bucket where the output is written



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
    package com.google.cloud.teleport.v2.templates;
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.kafka.dlq.BigQueryDeadLetterQueue;
    import com.google.cloud.teleport.v2.kafka.dlq.BigQueryDeadLetterQueueOptions;
    import com.google.cloud.teleport.v2.kafka.options.KafkaReadOptions;
    import com.google.cloud.teleport.v2.kafka.options.SchemaRegistryOptions;
    import com.google.cloud.teleport.v2.kafka.transforms.KafkaTransform;
    import com.google.cloud.teleport.v2.kafka.utils.KafkaConfig;
    import com.google.cloud.teleport.v2.kafka.utils.KafkaTopicUtils;
    import com.google.cloud.teleport.v2.transforms.WriteTransform;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.kafka.KafkaIO;
    import org.apache.beam.sdk.io.kafka.KafkaRecord;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.errorhandling.BadRecord;
    import org.apache.beam.sdk.transforms.errorhandling.BadRecordRouter;
    import org.apache.beam.sdk.transforms.errorhandling.ErrorHandler;
    import org.apache.beam.sdk.values.PCollection;
    
    @Template(
        name = "Kafka_to_Gcs_Flex",
        category = TemplateCategory.STREAMING,
        displayName = "Kafka to Cloud Storage",
        description =
            "A streaming pipeline which ingests data from Kafka and writes to a pre-existing Cloud"
                + " Storage bucket with a variety of file types.",
        optionsClass = KafkaToGcsFlex.KafkaToGcsOptions.class,
        flexContainerName = "kafka-to-gcs",
        contactInformation = "https://cloud.google.com/support",
        requirements = {"The output Google Cloud Storage directory must exist."})
    public class KafkaToGcsFlex {
    
      public interface KafkaToGcsOptions
          extends PipelineOptions,
              DataflowPipelineOptions,
              KafkaReadOptions,
              SchemaRegistryOptions,
              BigQueryDeadLetterQueueOptions {
    
        // This is a duplicate option that already exist in KafkaReadOptions but keeping it here
        // so the KafkaTopic appears above the authentication enum on the Templates UI.
        @TemplateParameter.KafkaReadTopic(
            order = 1,
            name = "readBootstrapServerAndTopic",
            groupName = "Source",
            description = "Source Kafka Topic",
            helpText = "Kafka Topic to read the input from.")
        String getReadBootstrapServerAndTopic();
    
        void setReadBootstrapServerAndTopic(String value);
    
        @TemplateParameter.Duration(
            order = 20,
            optional = true,
            groupName = "Destination",
            description = "Window duration",
            helpText =
                "The window duration/size in which data will be written to Cloud Storage. Allowed formats are: Ns (for "
                    + "seconds, example: 5s), Nm (for minutes, example: 12m), Nh (for hours, example: 2h).",
            example = "5m")
        @Default.String("5m")
        String getWindowDuration();
    
        void setWindowDuration(String windowDuration);
    
        @TemplateParameter.GcsWriteFolder(
            order = 21,
            groupName = "Destination",
            description = "Output file directory in Cloud Storage",
            helpText = "The path and filename prefix for writing output files. Must end with a slash.",
            example = "gs://your-bucket/your-path/")
        String getOutputDirectory();
    
        void setOutputDirectory(String outputDirectory);
    
        @TemplateParameter.Text(
            order = 22,
            optional = true,
            groupName = "Destination",
            description = "Output filename prefix of the files to write",
            helpText = "The prefix to place on each windowed file.",
            example = "output-")
        @Default.String("output")
        String getOutputFilenamePrefix();
    
        void setOutputFilenamePrefix(String outputFilenamePrefix);
    
        @TemplateParameter.Integer(
            order = 23,
            optional = true,
            description = "Maximum output shards",
            groupName = "Destination",
            helpText =
                "The maximum number of output shards produced when writing. A higher number of "
                    + "shards means higher throughput for writing to Cloud Storage, but potentially higher "
                    + "data aggregation cost across shards when processing output Cloud Storage files. "
                    + "Default value is decided by Dataflow.")
        @Default.Integer(0)
        Integer getNumShards();
    
        void setNumShards(Integer numShards);
      }
    
      public static PipelineResult run(KafkaToGcsOptions options) throws Exception {
        // Create the Pipeline
        Pipeline pipeline = Pipeline.create(options);
        String bootstrapServes;
        List<String> topicsList;
        if (options.getReadBootstrapServerAndTopic() != null) {
          List<String> bootstrapServerAndTopicList =
              KafkaTopicUtils.getBootstrapServerAndTopic(
                  options.getReadBootstrapServerAndTopic(), options.getProject());
          topicsList = List.of(bootstrapServerAndTopicList.get(1));
          bootstrapServes = bootstrapServerAndTopicList.get(0);
        } else {
          throw new IllegalArgumentException(
              "Please provide a valid bootstrap server which matches `[,:a-zA-Z0-9._-]+` and a topic which matches `[,a-zA-Z0-9._-]+`");
        }
    
        options.setStreaming(true);
    
        Map<String, Object> kafkaConfig = new HashMap<>(KafkaConfig.fromReadOptions(options));
    
        // Configure dead letter queue params
        ErrorHandler<BadRecord, ?> errorHandler = new ErrorHandler.DefaultErrorHandler<>();
        // Throwing Router throws the error instead of sending it to the DLQ. This will be the case
        // when no DLQ is configured and the pipeline will retry the failed error.
        BadRecordRouter badRecordRouter = BadRecordRouter.THROWING_ROUTER;
    
        if (options.getUseBigQueryDLQ()) {
          if (options.getOutputDeadletterTable() == null
              || options.getOutputDeadletterTable().isBlank()) {
            throw new IllegalArgumentException(
                "Please provide a Fully Qualified BigQuery table name when BigQuery Dead Letter"
                    + "Queue is enabled");
          }
          badRecordRouter = BadRecordRouter.RECORDING_ROUTER;
          errorHandler =
              pipeline.registerBadRecordErrorHandler(
                  BigQueryDeadLetterQueue.newBuilder()
                      .setTableName(options.getOutputDeadletterTable())
                      .build());
        }
    
        PCollection<KafkaRecord<byte[], byte[]>> kafkaRecord;
        // Step 1: Read from Kafka as bytes.
        KafkaIO.Read<byte[], byte[]> kafkaTransform =
            KafkaTransform.readBytesFromKafka(
                bootstrapServes, topicsList, kafkaConfig, options.getEnableCommitOffsets());
        kafkaRecord = pipeline.apply(kafkaTransform);
    
        kafkaRecord.apply(
            WriteTransform.newBuilder()
                .setOptions(options)
                .setBadRecordErrorHandler(errorHandler)
                .setBadRecordRouter(badRecordRouter)
                .build());
        if (options.getUseBigQueryDLQ()) {
          errorHandler.close();
        }
        return pipeline.run();
      }
    
      public static void main(String[] args) throws Exception {
        KafkaToGcsOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(KafkaToGcsOptions.class);
    
        run(options);
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
