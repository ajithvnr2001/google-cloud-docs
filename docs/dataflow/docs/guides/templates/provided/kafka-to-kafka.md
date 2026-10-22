---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-kafka/
title: Apache Kafka to Kafka template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:34.455771+00:00
---

# Apache Kafka to Kafka template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Apache Kafka to Kafka template Stay organized with collections  Save and categorize content based on your preferences. 

The Apache Kafka to Apache Kafka template creates a streaming pipeline that ingests data as bytes from an Apache Kafka source, and then writes the bytes to an Apache Kafka sink. 

## Pipeline requirements

  * The Apache Kafka source topic must exist.
  * The Apache Kafka source and sink broker servers must be running and be reachable from the Dataflow worker machines.
  * If you are using [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs) as either a source or a sink, the topic must exist before launching the template.



## Kafka message format

The Apache Kafka source messages are read as bytes, and the bytes are written to the Apache Kafka sink. 

## Authentication

The Apache Kafka to Apache Kafka template supports [SASL/PLAIN](https://kafka.apache.org/documentation/#security_sasl_plain) and [TLS](https://kafka.apache.org/documentation/#security_ssl) authentication to Kafka brokers. 

## Template parameters

### Required parameters

  * **readBootstrapServerAndTopic** : Kafka Bootstrap server and topic to read the input from. For example, `localhost:9092;topic1,topic2`.
  * **kafkaReadAuthenticationMode** : The mode of authentication to use with the Kafka cluster. Use `NONE` for no authentication, `SASL_PLAIN` for SASL/PLAIN username and password, `SASL_SCRAM_512` for SASL_SCRAM_512 authentication and `TLS` for certificate-based authentication. `APPLICATION_DEFAULT_CREDENTIALS` should be used only for Google Cloud Managed Service for Apache Kafka cluster, it allows to authenticate using application default credentials.
  * **writeBootstrapServerAndTopic** : Kafka topic to write the output to.
  * **kafkaWriteAuthenticationMethod** : The mode of authentication to use with the Kafka cluster. Use NONE for no authentication, SASL_PLAIN for SASL/PLAIN username and password, SASL_SCRAM_512 for SASL_SCRAM_512 based authentication and TLS for certificate-based authentication. Defaults to: APPLICATION_DEFAULT_CREDENTIALS.



### Optional parameters

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
  * **kafkaWriteUsernameSecretId** : The Google Cloud Secret Manager secret ID that contains the Kafka username for SASL_PLAIN authentication with the destination Kafka cluster. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`. Defaults to empty.
  * **kafkaWritePasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the Kafka password to use for SASL_PLAIN authentication with the destination Kafka cluster. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`. Defaults to empty.
  * **kafkaWriteKeystoreLocation** : The Google Cloud Storage path to the Java KeyStore (JKS) file that contains the TLS certificate and private key for authenticating with the destination Kafka cluster. For example, `gs://<BUCKET>/<KEYSTORE>.jks`.
  * **kafkaWriteTruststoreLocation** : The Google Cloud Storage path to the Java TrustStore (JKS) file that contains the trusted certificates to use to verify the identity of the destination Kafka broker.
  * **kafkaWriteTruststorePasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the password to use to access the Java TrustStore (JKS) file for TLS authentication with the destination Kafka cluster. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.
  * **kafkaWriteKeystorePasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the password to access the Java KeyStore (JKS) file to use for TLS authentication with the destination Kafka cluster. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.
  * **kafkaWriteKeyPasswordSecretId** : The Google Cloud Secret Manager secret ID that contains the password to use to access the private key within the Java KeyStore (JKS) file for TLS authentication with the destination Kafka cluster. For example, `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>`.



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
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Kafka_to_Kafka \
        --parameters \
    readBootstrapServerAndTopic=READ_BOOTSTRAP_SERVER_AND_TOPIC,\
    kafkaReadAuthenticationMode=APPLICATION_DEFAULT_CREDENTIALS,\
    writeBootstrapServerAndTopic=WRITE_BOOTSTRAP_SERVER_AND_TOPIC,\
    kafkaWriteAuthenticationMethod=APPLICATION_DEFAULT_CREDENTIALS
      

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `READ_BOOTSTRAP_SERVER_AND_TOPIC`: the Apache Kafka bootstrap server address and topic to read from 
  * `WRITE_BOOTSTRAP_SERVER_AND_TOPIC`: the Apache Kafka bootstrap server address and topic to write to 

The format of the bootstrap server address and topic depends on the type of cluster:

    * Managed Service for Apache Kafka cluster: `projects/PROJECT_ID/locations/REGION_NAME/clusters/CLUSTER_NAME/topics/TOPIC_NAME`
    * External Kafka cluster: `BOOTSTRAP_SERVER_ADDRESS;TOPIC_NAME`



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "readBootstrapServerAndTopic": "READ_BOOTSTRAP_SERVER_AND_TOPIC",
              "kafkaReadAuthenticationMode": "APPLICATION_DEFAULT_CREDENTIALS",
              "writeBootstrapServerAndTopic": "WRITE_BOOTSTRAP_SERVER_AND_TOPIC",
              "kafkaWriteAuthenticationMethod": "APPLICATION_DEFAULT_CREDENTIALS
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Kafka_to_Kafka",
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
  * `READ_BOOTSTRAP_SERVER_AND_TOPIC`: the Apache Kafka bootstrap server address and topic to read from 
  * `WRITE_BOOTSTRAP_SERVER_AND_TOPIC`: the Apache Kafka bootstrap server address and topic to write to 

The format of the bootstrap server address and topic depends on the type of cluster:

    * Managed Service for Apache Kafka cluster: `projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME/topics/TOPIC_NAME`
    * External Kafka cluster: `BOOTSTRAP_SERVER_ADDRESS;TOPIC_NAME`



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
    
    import static org.apache.beam.vendor.guava.v32_1_2_jre.com.google.common.base.Preconditions.checkArgument;
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.kafka.options.KafkaReadOptions;
    import com.google.cloud.teleport.v2.kafka.options.KafkaWriteOptions;
    import com.google.cloud.teleport.v2.kafka.transforms.KafkaTransform;
    import com.google.cloud.teleport.v2.kafka.utils.FileAwareProducerFactoryFn;
    import com.google.cloud.teleport.v2.kafka.utils.KafkaConfig;
    import com.google.cloud.teleport.v2.kafka.utils.KafkaTopicUtils;
    import com.google.cloud.teleport.v2.kafka.values.KafkaAuthenticationMethod;
    import java.io.IOException;
    import java.util.Collections;
    import java.util.List;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.kafka.KafkaIO;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.kafka.common.serialization.ByteArraySerializer;
    
    @Template(
        name = "Kafka_to_Kafka",
        category = TemplateCategory.STREAMING,
        displayName = "Kafka to Kafka",
        description = "A pipeline that writes data to a kafka destination from another kafka source",
        optionsClass = KafkaToKafka.KafkaToKafkaOptions.class,
        flexContainerName = "kafka-to-kafka",
        contactInformation = "https://cloud.google.com/support")
    public class KafkaToKafka {
      public interface KafkaToKafkaOptions
          extends PipelineOptions, KafkaReadOptions, KafkaWriteOptions, DataflowPipelineOptions {}
    
      public static void main(String[] args) throws IOException {
        UncaughtExceptionLogger.register();
        KafkaToKafkaOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(KafkaToKafkaOptions.class);
        run(options);
      }
    
      public static PipelineResult run(KafkaToKafkaOptions options) {
    
        if (options.getKafkaReadAuthenticationMode().equals(KafkaAuthenticationMethod.SASL_PLAIN)) {
          checkArgument(
              options.getKafkaReadUsernameSecretId().trim().length() > 0,
              "KafkaReadUsernameSecretId required to access username for source Kafka");
          checkArgument(
              options.getKafkaReadPasswordSecretId().trim().length() > 0,
              "KafkaReadPasswordSecretId required to access password for source kafka");
        } else if (options.getKafkaReadAuthenticationMode().equals(KafkaAuthenticationMethod.TLS)) {
          checkArgument(
              options.getKafkaReadTruststoreLocation().trim().length() > 0,
              "KafkaReadTruststoreLocation for trust store certificate required for ssl authentication");
          checkArgument(
              options.getKafkaReadTruststorePasswordSecretId().trim().length() > 0,
              "KafkaReadTruststorePassword for trust store password required for accessing truststore");
          checkArgument(
              options.getKafkaReadKeystoreLocation().trim().length() > 0,
              "KafkaReadKeystoreLocation for key store location required for ssl authentication");
          checkArgument(
              options.getKafkaReadKeystorePasswordSecretId().trim().length() > 0,
              "KafkaReadKeystorePassword for key store password required to access key store");
          checkArgument(
              options.getKafkaReadKeyPasswordSecretId().trim().length() > 0,
              "KafkaReadKeyPasswordSecretId version for key password required for SSL authentication");
        } else if (options.getKafkaReadAuthenticationMode().equals(KafkaAuthenticationMethod.NONE)
            || (options
                .getKafkaReadAuthenticationMode()
                .equals(KafkaAuthenticationMethod.APPLICATION_DEFAULT_CREDENTIALS))) {
        } else {
          throw new UnsupportedOperationException(
              "Authentication method not supported: " + options.getKafkaReadAuthenticationMode());
        }
    
        if (options.getKafkaWriteAuthenticationMethod().equals(KafkaAuthenticationMethod.SASL_PLAIN)) {
          checkArgument(
              options.getKafkaWriteUsernameSecretId().trim().length() > 0,
              "KafkaWriteUsernameSecretId required to access username for source Kafka");
          checkArgument(
              options.getKafkaWritePasswordSecretId().trim().length() > 0,
              "KafkaWritePasswordSecretId required to access password for destination Kafka");
        } else if (options.getKafkaWriteAuthenticationMethod().equals(KafkaAuthenticationMethod.TLS)) {
          checkArgument(
              options.getKafkaWriteTruststoreLocation().trim().length() > 0,
              "KafkaWriteTruststoreLocation for trust store certificate required for ssl authentication");
          checkArgument(
              options.getKafkaWriteTruststorePasswordSecretId().trim().length() > 0,
              "KafkaWriteTruststorePasswordSecretId for trust store password required for accessing truststore");
          checkArgument(
              options.getKafkaWriteKeystoreLocation().trim().length() > 0,
              "KafkaWriteKeystoreLocation for key store location required for ssl authentication");
          checkArgument(
              options.getKafkaWriteKeystorePasswordSecretId().trim().length() > 0,
              "KafkaWriteKeystorePasswordSecretId for key store password required to access key store");
          checkArgument(
              options.getKafkaWriteKeyPasswordSecretId().trim().length() > 0,
              "KafkaWriteKeyPasswordSecretId for source key password secret id version required for SSL authentication");
        } else if (options.getKafkaWriteAuthenticationMethod().equals(KafkaAuthenticationMethod.NONE)
            || options
                .getKafkaWriteAuthenticationMethod()
                .equals(KafkaAuthenticationMethod.APPLICATION_DEFAULT_CREDENTIALS)) {
          // No additional validation is required for these auth mechanisms since they don't depend on
          // any specific pipeline options.
        } else {
          throw new UnsupportedOperationException(
              "Authentication method not supported: " + options.getKafkaWriteAuthenticationMethod());
        }
    
        String sourceTopic;
        String sourceBootstrapServers;
        if (options.getReadBootstrapServerAndTopic() != null) {
          List<String> sourceBootstrapServerAndTopicList =
              KafkaTopicUtils.getBootstrapServerAndTopic(
                  options.getReadBootstrapServerAndTopic(), options.getProject());
          sourceTopic = sourceBootstrapServerAndTopicList.get(1);
          sourceBootstrapServers = sourceBootstrapServerAndTopicList.get(0);
        } else {
          throw new IllegalArgumentException(
              "Please provide a valid bootstrap server which matches `[,:a-zA-Z0-9._-]+` and a topic which matches `[,a-zA-Z0-9._-]+`");
        }
    
        String destinationTopic;
        String destinationBootstrapServers;
        if (options.getWriteBootstrapServerAndTopic() != null) {
          List<String> destinationBootstrapServerAndTopicList =
              KafkaTopicUtils.getBootstrapServerAndTopic(
                  options.getWriteBootstrapServerAndTopic(), options.getProject());
          destinationBootstrapServers = destinationBootstrapServerAndTopicList.get(0);
          destinationTopic = destinationBootstrapServerAndTopicList.get(1);
        } else {
          throw new IllegalArgumentException(
              "Please provide a valid bootstrap server which matches `[,:a-zA-Z0-9._-]+` and a topic which matches `[,a-zA-Z0-9._-]+`");
        }
    
        Pipeline pipeline = Pipeline.create(options);
        pipeline
            .apply(
                "Read from Kafka",
                KafkaTransform.readBytesFromKafka(
                        sourceBootstrapServers,
                        Collections.singletonList(sourceTopic),
                        KafkaConfig.fromReadOptions(options),
                        options.getEnableCommitOffsets())
                    .withoutMetadata())
            .apply(
                "Write to Kafka",
                KafkaIO.<byte[], byte[]>write()
                    .withBootstrapServers(destinationBootstrapServers)
                    .withTopic(destinationTopic)
                    .withKeySerializer(ByteArraySerializer.class)
                    .withValueSerializer(ByteArraySerializer.class)
                    .withProducerConfigUpdates(KafkaConfig.fromWriteOptions(options))
                    .withProducerFactoryFn(new FileAwareProducerFactoryFn()));
    
        return pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
