---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-bigquery/
title: Apache Kafka to BigQuery template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:27.826599+00:00
---

# Apache Kafka to BigQuery template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Apache Kafka to BigQuery template Stay organized with collections  Save and categorize content based on your preferences. 

The Apache Kafka to BigQuery template is a streaming pipeline that ingests text data from [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs) clusters, and then outputs the resulting records to BigQuery tables. Any errors that occur while inserting data into the output table are inserted into a separate errors table in BigQuery.

You can also use the Apache Kafka to BigQuery template with self-managed or external Kafka.

## Pipeline requirements

  * The Apache Kafka broker server must be running and be reachable from the Dataflow worker machines.
  * The Apache Kafka topics must exist.
  * You must enable the Dataflow, BigQuery, and Cloud Storage APIs. If authentication is required, you must also enable the Secret Manager API.
  * Create a BigQuery dataset and table with the appropriate schema for your Kafka input topic. If you're using multiple schemas in the same topic and want to write to multiple tables, you don't need to create the table before configuring the pipeline.
  * When the dead-letter (unprocessed messages) queue for the template is enabled, create an empty table that doesn't have a schema for the dead-letter queue.
  * If you are connecting to a [Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs) cluster, the pipeline must also meet the requirements listed in [ Use Dataflow with Managed Service for Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/managed-service-for-apache-kafka#requirements).



##  Kafka message format

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

## Authentication

The Apache Kafka to BigQuery template supports [SASL/PLAIN](https://kafka.apache.org/documentation/#security_sasl_plain) authentication to Kafka brokers.

## Template parameters

### Required parameters

  * **readBootstrapServerAndTopic** : Kafka Topic to read the input from.
  * **writeMode** : Write records to one table or multiple tables (based on schema). The `DYNAMIC_TABLE_NAMES` mode is supported only for `AVRO_CONFLUENT_WIRE_FORMAT` Source Message Format and `SCHEMA_REGISTRY` Schema Source. The target table name is auto-generated based on the Avro schema name of each message, it could either be a single schema (creating a single table) or multiple schemas (creating multiple tables). The `SINGLE_TABLE_NAME` mode writes to a single table (single schema) specified by the user. Defaults to `SINGLE_TABLE_NAME`.
  * **kafkaReadAuthenticationMode** : The mode of authentication to use with the Kafka cluster. Use `NONE` for no authentication, `SASL_PLAIN` for SASL/PLAIN username and password, `SASL_SCRAM_512` for SASL_SCRAM_512 authentication and `TLS` for certificate-based authentication. `APPLICATION_DEFAULT_CREDENTIALS` should be used only for Google Cloud Managed Service for Apache Kafka cluster, it allows to authenticate using application default credentials.
  * **messageFormat** : The format of the Kafka messages to read. The supported values are `AVRO_CONFLUENT_WIRE_FORMAT` (Confluent Schema Registry encoded Avro), `AVRO_BINARY_ENCODING` (Plain binary Avro), and `JSON`. Defaults to: AVRO_CONFLUENT_WIRE_FORMAT.
  * **useBigQueryDLQ** : If true, failed messages will be written to BigQuery with extra error information. Defaults to: false.



### Optional parameters

  * **outputTableSpec** : BigQuery table location to write the output to. The name should be in the format `<project>:<dataset>.<table_name>`. The table's schema must match input objects.
  * **persistKafkaKey** : If true, the pipeline will persist the Kafka message key in the BigQuery table, in a `_key` field of type `BYTES`. Default is `false` (Key is ignored).
  * **outputProject** : BigQuery output project in wehich the dataset resides. Tables will be created dynamically in the dataset. Defaults to empty.
  * **outputDataset** : BigQuery output dataset to write the output to. Tables will be created dynamically in the dataset. If the tables are created beforehand, the table names should follow the specified naming convention. The name should be `bqTableNamePrefix + Avro Schema FullName` , each word will be separated by a hyphen `-`. Defaults to empty.
  * **bqTableNamePrefix** : Naming prefix to be used while creating BigQuery output tables. Only applicable when using schema registry. Defaults to empty.
  * **createDisposition** : BigQuery CreateDisposition. For example: `CREATE_IF_NEEDED`, `CREATE_NEVER`. Defaults to: CREATE_IF_NEEDED.
  * **writeDisposition** : BigQuery WriteDisposition. For example: `WRITE_APPEND`, `WRITE_EMPTY` or `WRITE_TRUNCATE`. Defaults to: WRITE_APPEND.
  * **useAutoSharding** : If true, the pipeline uses auto-sharding when writng to BigQueryThe default value is `true`.
  * **numStorageWriteApiStreams** : Specifies the number of write streams, this parameter must be set. Default is `0`.
  * **storageWriteApiTriggeringFrequencySec** : Specifies the triggering frequency in seconds, this parameter must be set. Default is 5 seconds.
  * **useStorageWriteApiAtLeastOnce** : This parameter takes effect only if "Use BigQuery Storage Write API" is enabled. If enabled the at-least-once semantics will be used for Storage Write API, otherwise exactly-once semantics will be used. Defaults to: false.
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
  * **javascriptTextTransformGcsPath** : The Cloud Storage URI of the .js file that defines the JavaScript user-defined function (UDF) to use. For example, `gs://my-bucket/my-udfs/my_file.js`.
  * **javascriptTextTransformFunctionName** : The name of the JavaScript user-defined function (UDF) to use. For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see UDF Examples (<https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples>).
  * **javascriptTextTransformReloadIntervalMinutes** : Specifies how frequently to reload the UDF, in minutes. If the value is greater than 0, Dataflow periodically checks the UDF file in Cloud Storage, and reloads the UDF if the file is modified. This parameter allows you to update the UDF while the pipeline is running, without needing to restart the job. If the value is `0`, UDF reloading is disabled. The default value is `0`.



## User-defined function

Optionally, you can extend this template by writing a user-defined function (UDF). The template calls the UDF for each input element. Element payloads are serialized as JSON strings. For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

The template supports UDFs only for JSON-formatted Kafka messages. If the Kafka messages use Avro format, the UDF isn't invoked. 

### Function specification

The UDF has the following specification:

  * **Input** : the Kafka record value, serialized as a JSON string
  * **Output** : a JSON string that matches the schema of the BigQuery destination table



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Kafka to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Optional: To switch from exactly-once processing to [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes), select **At Least Once**.
  7. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Kafka_to_BigQuery_Flex \
        --parameters \
    readBootstrapServerAndTopic=BOOTSTRAP_SERVER_AND_TOPIC,\
    kafkaReadAuthenticationMode=APPLICATION_DEFAULT_CREDENTIALS,\
    messageFormat=JSON,\
    writeMode=SINGLE_TABLE_NAME,\
    outputTableSpec=PROJECT_ID:DATASET_NAME.TABLE_NAME,\
    useBigQueryDLQ=true,\
    outputDeadletterTable=PROJECT_ID:DATASET_NAME.ERROR_TABLE_NAME
      

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
  * `DATASET_NAME`: the name of your BigQuery dataset
  * `TABLE_NAME`: the name of the BigQuery output table
  * `ERROR_TABLE_NAME`: the name of the BigQuery table to write error records



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
              "writeMode": "SINGLE_TABLE_NAME",
              "outputTableSpec": "PROJECT_ID:DATASET_NAME.TABLE_NAME",
              "useBigQueryDLQ": "true",
              "outputDeadletterTable": "PROJECT_ID:DATASET_NAME.ERROR_TABLE_NAME"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Kafka_to_BigQuery_Flex",
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
  * `DATASET_NAME`: the name of your BigQuery dataset
  * `TABLE_NAME`: the name of the BigQuery output table
  * `ERROR_TABLE_NAME`: the name of the BigQuery table to write error records



For more information, see [Write data from Kafka to BigQuery with Dataflow](https://docs.cloud.google.com/dataflow/docs/kafka-dataflow).

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
    
    import com.google.api.services.bigquery.model.TableRow;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.kafka.dlq.BigQueryDeadLetterQueue;
    import com.google.cloud.teleport.v2.kafka.transforms.AvroDynamicTransform;
    import com.google.cloud.teleport.v2.kafka.transforms.AvroTransform;
    import com.google.cloud.teleport.v2.kafka.transforms.KafkaRecordErrorConverters.WriteKafkaRecordMessageErrors;
    import com.google.cloud.teleport.v2.kafka.transforms.KafkaTransform;
    import com.google.cloud.teleport.v2.kafka.utils.KafkaConfig;
    import com.google.cloud.teleport.v2.kafka.utils.KafkaTopicUtils;
    import com.google.cloud.teleport.v2.kafka.values.KafkaTemplateParameters.MessageFormatConstants;
    import com.google.cloud.teleport.v2.kafka.values.KafkaTemplateParameters.SchemaFormat;
    import com.google.cloud.teleport.v2.options.KafkaToBigQueryFlexOptions;
    import com.google.cloud.teleport.v2.transforms.BigQueryWriteUtils;
    import com.google.cloud.teleport.v2.transforms.ErrorConverters;
    import com.google.cloud.teleport.v2.transforms.StringMessageToTableRow;
    import com.google.cloud.teleport.v2.utils.BigQueryIOUtils;
    import com.google.cloud.teleport.v2.utils.MetadataValidator;
    import com.google.cloud.teleport.v2.utils.SchemaUtils;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.base.Strings;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Map;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.ByteArrayCoder;
    import org.apache.beam.sdk.coders.CoderRegistry;
    import org.apache.beam.sdk.coders.NullableCoder;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.WriteDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryInsertError;
    import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy;
    import org.apache.beam.sdk.io.gcp.bigquery.WriteResult;
    import org.apache.beam.sdk.io.kafka.KafkaRecord;
    import org.apache.beam.sdk.io.kafka.KafkaRecordCoder;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.Flatten;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.errorhandling.BadRecord;
    import org.apache.beam.sdk.transforms.errorhandling.BadRecordRouter;
    import org.apache.beam.sdk.transforms.errorhandling.ErrorHandler;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionList;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.TupleTag;
    import org.apache.commons.lang3.ObjectUtils;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link KafkaToBigQueryFlex} pipeline is a streaming pipeline which ingests text data from
     * Kafka, and outputs the resulting records to BigQuery. Any errors which occur in the
     * transformation of the data, or inserting into the output table will be inserted into a separate
     * errors table in BigQuery. Both output and error tables are specified by the user as parameters.
     *
     * <p><b>Pipeline Requirements</b>
     *
     * <ul>
     *   <li>The Kafka topic exists and the message is encoded in a valid JSON format.
     *   <li>The BigQuery output table exists.
     *   <li>The Kafka brokers are reachable from the Dataflow worker machines.
     * </ul>
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/kafka-to-bigquery/README_Kafka_to_BigQuery.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Kafka_to_BigQuery_Flex",
        category = TemplateCategory.STREAMING,
        displayName = "Kafka to BigQuery",
        description =
            "The Apache Kafka to BigQuery template is a streaming pipeline which ingests text data from Apache Kafka, and outputs the resulting records to BigQuery. "
                + "Any errors which occur in the transformation of the data, or inserting into the output table are inserted into a separate errors table in BigQuery. "
                + "For any errors which occur in the transformation of the data, the original records can be inserted into a separate Kafka topic. The template supports "
                + "reading a Kafka topic which contains single/multiple schema(s). It can write to a single or multiple BigQuery tables, depending on the schema of records. ",
        optionsClass = KafkaToBigQueryFlexOptions.class,
        flexContainerName = "kafka-to-bigquery",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-bigquery",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The output BigQuery table must exist.",
          "The Apache Kafka broker server must be running and be reachable from the Dataflow worker machines.",
          "The Apache Kafka topics must exist and the messages must be encoded in a valid JSON format."
        },
        skipOptions = {"useStorageWriteApi"})
    public class KafkaToBigQueryFlex {
    
      /* Logger for class. */
      private static final Logger LOG = LoggerFactory.getLogger(KafkaToBigQueryFlex.class);
    
      /** The tag for the main output of the json transformation. */
      public static final TupleTag<TableRow> TRANSFORM_OUT = new TupleTag<>() {};
    
      /** The tag for the dead-letter output of the json to table row transform. */
      public static final TupleTag<FailsafeElement<KafkaRecord<String, String>, String>>
          TRANSFORM_DEADLETTER_OUT = new TupleTag<>() {};
    
      /** String/String Coder for FailsafeElement. */
      private static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(
              NullableCoder.of(StringUtf8Coder.of()), NullableCoder.of(StringUtf8Coder.of()));
    
      private static ErrorHandler<BadRecord, ?> errorHandler = new ErrorHandler.DefaultErrorHandler<>();
      private static BadRecordRouter badRecordRouter = BadRecordRouter.THROWING_ROUTER;
    
      /**
       * The main entry-point for pipeline execution. This method will start the pipeline but will not
       * wait for its execution to finish. If blocking execution is required, use the {@link
       * KafkaToBigQueryFlex#run(KafkaToBigQueryFlexOptions)} method to start the pipeline and invoke
       * {@code result.waitUntilFinish()} on the {@link PipelineResult}.
       *
       * @param args The command-line args passed by the executor.
       */
      public static void main(String[] args) throws Exception {
        UncaughtExceptionLogger.register();
    
        KafkaToBigQueryFlexOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(KafkaToBigQueryFlexOptions.class);
    
        run(options);
      }
    
      public static Boolean useErrorHandler(KafkaToBigQueryFlexOptions options) {
        return options.getUseBigQueryDLQ();
      }
    
      public static WriteResult processKafkaRecords(
          PCollection<KafkaRecord<byte[], byte[]>> kafkaRecords, KafkaToBigQueryFlexOptions options) {
    
        // Validate the pipeline options for MessageFormat and SchemaFormat.
        if (options.getMessageFormat().equals(MessageFormatConstants.AVRO_BINARY_ENCODING)
            && (options.getBinaryAvroSchemaPath() != null
                && options.getBinaryAvroSchemaPath().isBlank())) {
          throw new IllegalArgumentException(
              "Binary Avro Schema Path cannot be empty for AVRO_BINARY_ENCODING.");
        }
    
        if (options.getMessageFormat().equals(MessageFormatConstants.AVRO_CONFLUENT_WIRE_FORMAT)) {
    
          if ((options.getSchemaRegistryConnectionUrl() != null
                  && options.getSchemaRegistryConnectionUrl().isBlank())
              && (options.getConfluentAvroSchemaPath() != null
                  && options.getConfluentAvroSchemaPath().isBlank())) {
            throw new IllegalArgumentException(
                "Either Schema Registry Connection URL or Confluent Avro Schema Path must be provided for AVRO_CONFLUENT_WIRE_FORMAT.");
          }
    
          if (options.getSchemaFormat().equals(SchemaFormat.SINGLE_SCHEMA_FILE)) {
            if (!options.getConfluentAvroSchemaPath().isBlank()
                && (options.getOutputTableSpec() != null && options.getOutputTableSpec().isBlank())) {
              throw new IllegalArgumentException(
                  "The outputTableSpec parameter is required when using the SINGLE_SCHEMA_FILE schema format.");
            }
          } else if (options.getSchemaFormat().equals(SchemaFormat.SCHEMA_REGISTRY)) {
            if (options.getSchemaRegistryConnectionUrl() != null
                && (options.getOutputDataset() != null && options.getOutputDataset().isBlank())) {
              throw new IllegalArgumentException(
                  "An output BigQuery dataset is required. It will be used to create tables per schema.");
            }
          } else {
            throw new IllegalArgumentException(
                "Unsupported schemaFormat parameter value: " + options.getSchemaFormat());
          }
        }
    
        if (options.getMessageFormat().equals(MessageFormatConstants.AVRO_BINARY_ENCODING)
            && (!options.getBinaryAvroSchemaPath().isBlank())) {
          return handleAvroBinaryEncoding(kafkaRecords, options);
        } else if (options.getMessageFormat().equals(MessageFormatConstants.AVRO_CONFLUENT_WIRE_FORMAT)
            && (!options.getSchemaRegistryConnectionUrl().isBlank()
                || !options.getConfluentAvroSchemaPath().isBlank())) {
          return handleAvroConfluentWireFormat(kafkaRecords, options);
        } else {
          throw new IllegalArgumentException(
              "Message format " + options.getMessageFormat() + " is unsupported.");
        }
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
      public static PipelineResult run(KafkaToBigQueryFlexOptions options) throws Exception {
    
        // Enable Streaming Engine
        options.setEnableStreamingEngine(true);
    
        List<String> dataflowServiceOptions = options.getDataflowServiceOptions();
        if (dataflowServiceOptions == null) {
          dataflowServiceOptions = new ArrayList<>();
        }
        dataflowServiceOptions.add("enable_streaming_engine_resource_based_billing");
        options.setDataflowServiceOptions(dataflowServiceOptions);
    
        // Validate BQ STORAGE_WRITE_API options
        options.setUseStorageWriteApi(true);
        if (options.getStorageWriteApiTriggeringFrequencySec() == null) {
          options.setStorageWriteApiTriggeringFrequencySec(5);
        }
        BigQueryIOUtils.validateBQStorageApiOptionsStreaming(options);
        MetadataValidator.validate(options);
    
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        List<String> topicsList;
        String bootstrapServers;
        if (options.getReadBootstrapServerAndTopic() != null) {
          List<String> bootstrapServerAndTopicList =
              KafkaTopicUtils.getBootstrapServerAndTopic(
                  options.getReadBootstrapServerAndTopic(), options.getProject());
          topicsList = List.of(bootstrapServerAndTopicList.get(1));
          bootstrapServers = bootstrapServerAndTopicList.get(0);
        } else {
          throw new IllegalArgumentException(
              "Please provide a valid bootstrap server which matches `[,:a-zA-Z0-9._-]+` and a topic which matches `[,a-zA-Z0-9._-]+`");
        }
    
        // Configure error handler for Dead letter queue
        if (options.getUseBigQueryDLQ()) {
          if (options.getOutputDeadletterTable() == null
              || options.getOutputDeadletterTable().isBlank()) {
            throw new IllegalArgumentException(
                "Please provide a valid BigQuery full qualified table name when using BigQuery"
                    + "Dead letter queue");
          }
          badRecordRouter = BadRecordRouter.RECORDING_ROUTER;
          errorHandler =
              pipeline.registerBadRecordErrorHandler(
                  BigQueryDeadLetterQueue.newBuilder()
                      .setTableName(options.getOutputDeadletterTable())
                      .build());
        }
    
        // Get the Kafka config
        Map<String, Object> kafkaConfig = KafkaConfig.fromReadOptions(options);
    
        /*
         * Steps:
         *  1) Read messages in from Kafka
         *  2) Transform the messages into TableRows
         *     - Transform message payload via UDF
         *     - Convert UDF result to TableRow objects
         *  3) Write successful records out to BigQuery
         *  4) Write failed records out to BigQuery
         */
    
        if (options.getMessageFormat() == null
            || options.getMessageFormat().equals(MessageFormatConstants.JSON)) {
    
          pipeline = runJsonPipeline(pipeline, options, topicsList, bootstrapServers, kafkaConfig);
    
        } else if (options.getMessageFormat().equals(MessageFormatConstants.AVRO_CONFLUENT_WIRE_FORMAT)
            || options.getMessageFormat().equals(MessageFormatConstants.AVRO_BINARY_ENCODING)) {
          pipeline = runAvroPipeline(pipeline, options, topicsList, bootstrapServers, kafkaConfig);
    
        } else {
          throw new IllegalArgumentException("Invalid format specified: " + options.getMessageFormat());
        }
        if (useErrorHandler(options)) {
          errorHandler.close();
        }
        return pipeline.run();
      }
    
      private static WriteResult handleAvroBinaryEncoding(
          PCollection<KafkaRecord<byte[], byte[]>> kafkaRecords, KafkaToBigQueryFlexOptions options) {
        WriteResult writeResult;
        BigQueryWriteUtils.BigQueryWrite bigQueryWrite;
        if (useErrorHandler(options)) {
          // BigQueryIO sets the BadRecordRouter to RecordingRouter even when the errorHandler is
          // DefaultErrorHandler(which is a no op). In this case, when the BadRecordRouter is
          // ThrowingRouter,
          // don't pass errorHandler to BigQueryIO.
          bigQueryWrite =
              BigQueryWriteUtils.BigQueryWrite.of(
                  SchemaUtils.getAvroSchema(options.getBinaryAvroSchemaPath()),
                  options.getOutputTableSpec(),
                  options.getWriteDisposition(),
                  options.getCreateDisposition(),
                  options.getNumStorageWriteApiStreams(),
                  options.getStorageWriteApiTriggeringFrequencySec(),
                  options.getPersistKafkaKey(),
                  options.getUseAutoSharding(),
                  errorHandler);
        } else {
          bigQueryWrite =
              BigQueryWriteUtils.BigQueryWrite.of(
                  SchemaUtils.getAvroSchema(options.getBinaryAvroSchemaPath()),
                  options.getOutputTableSpec(),
                  options.getWriteDisposition(),
                  options.getCreateDisposition(),
                  options.getNumStorageWriteApiStreams(),
                  options.getStorageWriteApiTriggeringFrequencySec(),
                  options.getPersistKafkaKey(),
                  options.getUseAutoSharding());
        }
        writeResult =
            kafkaRecords
                .apply(
                    AvroTransform.of(
                        options.getMessageFormat(),
                        options.getBinaryAvroSchemaPath(),
                        errorHandler,
                        badRecordRouter))
                .apply(bigQueryWrite);
        return writeResult;
      }
    
      private static WriteResult handleAvroConfluentWireFormat(
          PCollection<KafkaRecord<byte[], byte[]>> kafkaRecords, KafkaToBigQueryFlexOptions options) {
        if (options.getSchemaFormat().equals(SchemaFormat.SINGLE_SCHEMA_FILE)) {
          return handleSingleSchemaFileFormat(kafkaRecords, options);
        } else if (options.getSchemaFormat().equals(SchemaFormat.SCHEMA_REGISTRY)) {
          return handleSchemaRegistryFormat(kafkaRecords, options);
        } else {
          throw new IllegalArgumentException(
              "Message format " + options.getSchemaFormat() + " is unsupported.");
        }
      }
    
      private static WriteResult handleSingleSchemaFileFormat(
          PCollection<KafkaRecord<byte[], byte[]>> kafkaRecords, KafkaToBigQueryFlexOptions options) {
        if (!(options.getConfluentAvroSchemaPath() != null && options.getOutputTableSpec() != null)) {
          // TODO: Add error.
          throw new RuntimeException("");
        }
        WriteResult writeResult;
        BigQueryWriteUtils.BigQueryWrite bigQueryWrite;
        if (useErrorHandler(options)) {
          bigQueryWrite =
              BigQueryWriteUtils.BigQueryWrite.of(
                  SchemaUtils.getAvroSchema(options.getConfluentAvroSchemaPath()),
                  options.getOutputTableSpec(),
                  options.getWriteDisposition(),
                  options.getCreateDisposition(),
                  options.getNumStorageWriteApiStreams(),
                  options.getStorageWriteApiTriggeringFrequencySec(),
                  options.getPersistKafkaKey(),
                  options.getUseAutoSharding(),
                  errorHandler);
        } else {
          bigQueryWrite =
              BigQueryWriteUtils.BigQueryWrite.of(
                  SchemaUtils.getAvroSchema(options.getConfluentAvroSchemaPath()),
                  options.getOutputTableSpec(),
                  options.getWriteDisposition(),
                  options.getCreateDisposition(),
                  options.getNumStorageWriteApiStreams(),
                  options.getStorageWriteApiTriggeringFrequencySec(),
                  options.getPersistKafkaKey(),
                  options.getUseAutoSharding());
        }
        writeResult =
            kafkaRecords
                .apply(
                    AvroTransform.of(
                        options.getMessageFormat(),
                        options.getConfluentAvroSchemaPath(),
                        errorHandler,
                        badRecordRouter))
                .apply(bigQueryWrite);
        return writeResult;
      }
    
      private static WriteResult handleSchemaRegistryFormat(
          PCollection<KafkaRecord<byte[], byte[]>> kafkaRecords, KafkaToBigQueryFlexOptions options) {
        if (!(options.getSchemaRegistryConnectionUrl() != null && options.getOutputDataset() != null)) {
          throw new RuntimeException(
              "Missing required parameters: Schema Registry URL and/or Output Dataset");
        }
        WriteResult writeResult;
        BigQueryWriteUtils.BigQueryDynamicWrite bigQueryWrite;
        if (useErrorHandler(options)) {
          bigQueryWrite =
              BigQueryWriteUtils.BigQueryDynamicWrite.of(
                  options.getOutputProject(),
                  options.getOutputDataset(),
                  options.getBqTableNamePrefix(),
                  options.getWriteDisposition(),
                  options.getCreateDisposition(),
                  options.getNumStorageWriteApiStreams(),
                  options.getStorageWriteApiTriggeringFrequencySec(),
                  options.getPersistKafkaKey(),
                  options.getUseAutoSharding(),
                  errorHandler);
        } else {
          bigQueryWrite =
              BigQueryWriteUtils.BigQueryDynamicWrite.of(
                  options.getOutputProject(),
                  options.getOutputDataset(),
                  options.getBqTableNamePrefix(),
                  options.getWriteDisposition(),
                  options.getCreateDisposition(),
                  options.getNumStorageWriteApiStreams(),
                  options.getStorageWriteApiTriggeringFrequencySec(),
                  options.getPersistKafkaKey(),
                  options.getUseAutoSharding());
        }
        writeResult =
            kafkaRecords
                .apply(
                    AvroDynamicTransform.of(
                        options.getSchemaRegistryConnectionUrl(),
                        KafkaConfig.fromSchemaRegistryOptions(options),
                        errorHandler,
                        badRecordRouter))
                .apply(bigQueryWrite);
        return writeResult;
      }
    
      public static Pipeline runAvroPipeline(
          Pipeline pipeline,
          KafkaToBigQueryFlexOptions options,
          List<String> topicsList,
          String bootstrapServers,
          Map<String, Object> kafkaConfig)
          throws Exception {
    
        if (options.getMessageFormat().equals(MessageFormatConstants.AVRO_BINARY_ENCODING)
            && options.getBinaryAvroSchemaPath() == null) {
          throw new IllegalArgumentException(
              "Avro schema is needed in order to read non confluent wire format messages.");
        }
        if (options.getMessageFormat().equals(MessageFormatConstants.AVRO_CONFLUENT_WIRE_FORMAT)
            && options.getSchemaRegistryConnectionUrl() == null
            && options.getConfluentAvroSchemaPath() == null) {
          throw new IllegalArgumentException(
              "Schema Registry Connection URL or Avro schema is needed in order to read confluent wire format messages.");
        }
        if (!Strings.isNullOrEmpty(options.getJavascriptTextTransformGcsPath())
            && !Strings.isNullOrEmpty(options.getJavascriptTextTransformFunctionName())) {
          LOG.warn(
              "JavaScript UDF parameters are set while using Avro message format. "
                  + "UDFs are supported for JSON format only. No UDF transformation will be applied.");
        }
    
        PCollection<KafkaRecord<byte[], byte[]>> kafkaRecords;
    
        kafkaRecords =
            pipeline
                /*
                 * Step #1: Read messages in from Kafka and convert to GenericRecords wrap in FailsafeElement
                 */
                .apply(
                    "ReadBytesFromKafka",
                    KafkaTransform.readBytesFromKafka(
                        bootstrapServers, topicsList, kafkaConfig, options.getEnableCommitOffsets()))
                .setCoder(
                    KafkaRecordCoder.of(NullableCoder.of(ByteArrayCoder.of()), ByteArrayCoder.of()));
    
        WriteResult writeResult = processKafkaRecords(kafkaRecords, options);
        return pipeline;
      }
    
      public static Pipeline runJsonPipeline(
          Pipeline pipeline,
          KafkaToBigQueryFlexOptions options,
          List<String> topicsList,
          String bootstrapServers,
          Map<String, Object> kafkaConfig) {
    
        // Register the coder for pipeline
        FailsafeElementCoder<KafkaRecord<String, String>, String> coder =
            FailsafeElementCoder.of(
                KafkaRecordCoder.of(
                    NullableCoder.of(StringUtf8Coder.of()), NullableCoder.of(StringUtf8Coder.of())),
                NullableCoder.of(StringUtf8Coder.of()));
    
        CoderRegistry coderRegistry = pipeline.getCoderRegistry();
        coderRegistry.registerCoderForType(coder.getEncodedTypeDescriptor(), coder);
    
        PCollectionTuple convertedTableRows;
        convertedTableRows =
            pipeline
                /*
                 * Step #1: Read messages in from Kafka
                 */
                .apply(
                    "ReadFromKafka",
                    KafkaTransform.readStringFromKafka(
                        bootstrapServers, topicsList, kafkaConfig, options.getEnableCommitOffsets()))
    
                /*
                 * Step #2: Transform the Kafka Messages into TableRows
                 */
                .apply(
                    "ConvertMessageToTableRow",
                    StringMessageToTableRow.newBuilder()
                        .setFileSystemPath(options.getJavascriptTextTransformGcsPath())
                        .setFunctionName(options.getJavascriptTextTransformFunctionName())
                        .setReloadIntervalMinutes(
                            options.getJavascriptTextTransformReloadIntervalMinutes())
                        .setSuccessTag(TRANSFORM_OUT)
                        .setFailureTag(TRANSFORM_DEADLETTER_OUT)
                        .build());
        /*
         * Step #3: Write the successful records out to BigQuery
         */
        WriteResult writeResult =
            convertedTableRows
                .get(TRANSFORM_OUT)
                .apply(
                    "WriteSuccessfulRecords",
                    BigQueryIO.writeTableRows()
                        .withoutValidation()
                        .withCreateDisposition(CreateDisposition.CREATE_NEVER)
                        .withWriteDisposition(WriteDisposition.WRITE_APPEND)
                        .withExtendedErrorInfo()
                        .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors())
                        .to(options.getOutputTableSpec()));
    
        /*
         * Step 3 Contd.
         * Elements that failed inserts into BigQuery are extracted and converted to FailsafeElement
         */
        PCollection<FailsafeElement<String, String>> failedInserts =
            BigQueryIOUtils.writeResultToBigQueryInsertErrors(writeResult, options)
                .apply(
                    "WrapInsertionErrors",
                    MapElements.into(FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor())
                        .via(KafkaToBigQueryFlex::wrapBigQueryInsertError))
                .setCoder(FAILSAFE_ELEMENT_CODER);
    
        if (options.getOutputDeadletterTable() != null) {
          /*
           * Step #4: Write failed records out to BigQuery
           */
          PCollectionList.of(convertedTableRows.get(TRANSFORM_DEADLETTER_OUT))
              .apply("Flatten", Flatten.pCollections())
              .apply(
                  "WriteTransformationFailedRecords",
                  WriteKafkaRecordMessageErrors.newBuilder()
                      .setErrorRecordsTable(
                          ObjectUtils.firstNonNull(options.getOutputDeadletterTable()))
                      .setErrorRecordsTableSchema(SchemaUtils.DEADLETTER_SCHEMA)
                      .build());
        } else {
          PCollectionList.of(convertedTableRows.get(TRANSFORM_DEADLETTER_OUT))
              .apply("Flatten", Flatten.pCollections())
              .apply("PrintInsertionFailedRecords", ParDo.of(new ThrowErrorFn<>()));
        }
    
        if (options.getOutputDeadletterTable() != null) {
          /*
           * Step #5: Insert records that failed BigQuery inserts into a dead-letter table.
           */
          failedInserts.apply(
              "WriteInsertionFailedRecords",
              ErrorConverters.WriteStringMessageErrors.newBuilder()
                  .setErrorRecordsTable(ObjectUtils.firstNonNull(options.getOutputDeadletterTable()))
                  .setErrorRecordsTableSchema(SchemaUtils.DEADLETTER_SCHEMA)
                  .build());
        } else {
          failedInserts.apply(
              "PrintInsertionFailedRecords", ParDo.of(new ThrowErrorFn<String, String>()));
        }
    
        return pipeline;
      }
    
      /**
       * Method to wrap a {@link BigQueryInsertError} into a {@link FailsafeElement}.
       *
       * @param insertError BigQueryInsert error.
       * @return FailsafeElement object.
       */
      protected static FailsafeElement<String, String> wrapBigQueryInsertError(
          BigQueryInsertError insertError) {
    
        FailsafeElement<String, String> failsafeElement;
        try {
    
          failsafeElement =
              FailsafeElement.of(
                  insertError.getRow().toPrettyString(), insertError.getRow().toPrettyString());
          failsafeElement.setErrorMessage(insertError.getError().toPrettyString());
    
        } catch (IOException e) {
          LOG.error("Failed to wrap BigQuery insert error.");
          throw new RuntimeException(e);
        }
        return failsafeElement;
      }
    
      static class ThrowErrorFn<T, W> extends DoFn<FailsafeElement<T, W>, FailsafeElement<T, W>> {
    
        @ProcessElement
        public void processElement(ProcessContext context) {
          FailsafeElement<T, W> element = context.element();
          // TODO: Logging every exception might overload Google Cloud Logging API. Find a better way to
          // log these errors.
          LOG.error(element.toString() + element.getErrorMessage() + element.getStacktrace());
          context.output(element);
        }
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
