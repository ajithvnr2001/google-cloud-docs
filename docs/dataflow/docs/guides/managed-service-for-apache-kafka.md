---
url: https://docs.cloud.google.com/dataflow/docs/guides/managed-service-for-apache-kafka/
title: Use Dataflow with Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:15.393084+00:00
---

# Use Dataflow with Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/managed-service-for-apache-kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Dataflow with Managed Service for Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview) as a source or sink in a Dataflow pipeline.

You can use either of the following approaches:

  * Use a Google-provided template.
  * Run a custom Apache Beam pipeline.



## Requirements

  * Enable the Cloud Storage, Dataflow, and Managed Service for Apache Kafka APIs in your project. See [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) or run the following Google Cloud CLI command:
        
        gcloud services enable dataflow.googleapis.com managedkafka.googleapis.com storage-component.googleapis.com
        

  * The Dataflow [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) must have the Managed Kafka Client (`roles/managedkafka.client`) Identity and Access Management (IAM) role.

  * The Dataflow worker VMs must have network access to the Kafka bootstrap server. For more information, see [Configure Managed Service for Apache Kafka networking](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka).




## Get the bootstrap server address

To run a pipeline that connects to a Managed Service for Apache Kafka cluster, first get the cluster's bootstrap server address. You need this address when you configure the pipeline.

You can use the Google Cloud console or the Google Cloud CLI, as follows:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the cluster name.

  3. Click the **Configurations** tab.

  4. Copy the bootstrap server address from **Bootstrap URL**.




### gcloud

Use the [`managed-kafka clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/describe) command.
    
    
    gcloud managed-kafka clusters describe CLUSTER_ID \
      --location=LOCATION \
      --format="value(bootstrapAddress)"
    

Replace the following:

  * CLUSTER_ID: the ID or name of the cluster
  * LOCATION: the location of the cluster



For more information, see [View a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster).

## Use Managed Service for Apache Kafka with a Dataflow template

Google provides several Dataflow templates that read from Apache Kafka:

  * [Kafka to Kafka](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-kafka)
  * [Kafka to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-bigquery)
  * [Kafka to Cloud Storage](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-gcs)



These templates can be used with Managed Service for Apache Kafka. If one of them matches your use case, consider using it rather than writing custom pipeline code.

### Console

  1. Go to the **Dataflow** > **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Click **Create job from template**.

  3. In the **Job name** , enter a name for the job.

  4. From the **Dataflow** template drop-down menu, select the template to run.

  5. In the **Kafka bootstrap server** box, enter the bootstrap server address.

  6. In the **Kafka topic** box, enter the name of the topic.

  7. For **Kafka authentication mode** , select **APPLICATION_DEFAULT_CREDENTIALS**.

  8. For **Kafka message format** , select the format of the Apache Kafka messages.

  9. Enter other parameters as needed. The supported parameters are documented for each template.

  10. **Run job**.




### gcloud

Use the [`gcloud dataflow jobs run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run) command.
    
    
    gcloud dataflow jobs run JOB_NAME \
      --gcs-location gs://TEMPLATE_FILE \
      --region REGION_NAME \
      --parameters \
    readBootstrapServerAndTopic=projects/PROJECT_NAME/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC,\
    kafkaReadAuthenticationMode=APPLICATION_DEFAULT_CREDENTIALS\,
    # Other parameters, depending on the template
    # ...
    

Replace the following:

  * JOB_NAME: a name for the job
  * TEMPLATE_FILE: the location of the template file in Cloud Storage
  * REGION_NAME: the region where you want to deploy your job
  * PROJECT_NAME: the name of your Google Cloud project
  * LOCATION: the location of the cluster
  * CLUSTER_ID: the ID or name of the cluster
  * TOPIC: the name of the Kafka topic



For other templates, such as the [Kafka to Apache Iceberg YAML](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/yaml/README_Kafka_To_Iceberg_Yaml.md#running-the-template) template, you must set the `bootstrapServers` parameter to the cluster's bootstrap address. In addition, you must configure authentication by setting the `consumerConfigUpdates` parameter, as shown in the following shortened command line:

### gcloud
    
    
    gcloud dataflow flex-template run "kafka-to-iceberg-yaml-job" \
      --project "PROJECT_NAME" \
      --region "REGION_NAME" \
      --template-file-gcs-location "gs://REGION_NAME/templates/flex/Kafka_To_Iceberg_Yaml" \
      --parameters "bootstrapServers=BOOTSTRAP_ADDRESS" \
      --parameters "consumerConfigUpdates='{\"security.protocol\": \"SASL_SSL\",\"sasl.mechanism\": \"OAUTHBEARER\",\"sasl.login.callback.handler.class\": \"com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler\",\"sasl.jaas.config\": \"org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;\"}'"
    

Replace BOOTSTRAP_ADDRESS with the [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address) of the Kafka cluster. For a complete command line, see the template [README file](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/yaml/README_Kafka_To_Iceberg_Yaml.md#running-the-template).

## Use Managed Service for Apache Kafka with a Beam pipeline

This section describes how to use the Apache Beam SDK to create and run a Dataflow pipeline that connects to Managed Service for Apache Kafka.

For most scenarios, use the [managed I/O transform](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka) as your Kafka source or sink. If you need more advanced performance tuning, consider using the [`KafkaIO`](https://beam.apache.org/documentation/io/connectors/) connector. For more information about the benefits of using managed I/O, see [ Dataflow managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).

### Requirements

  * Kafka Client version 3.6.0 or later.

  * Apache Beam SDK version 2.61.0 or later.

  * The machine where you start the Dataflow job must have network access to the Apache Kafka bootstrap server. For example, start the job from a Compute Engine instance that can access the VPC where the cluster is reachable.

  * The principal that creates the job must have the following IAM roles:

    * Managed Kafka Client (`roles/managedkafka.client`) to access the Apache Kafka cluster.
    * Service Account User (`roles/iam.serviceAccountUser`) to act as the Dataflow worker service account.
    * Storage Admin (`roles/storage.admin`) to upload job files to Cloud Storage.
    * Dataflow Admin (`roles/dataflow.admin`) to create the job.

If you start the job from a Compute Engine instance, you can grant these roles to a [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) that is attached to the VM. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

You can also use Application Default Credentials (ADC) with [service account impersonation](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#sa-impersonation) when you create the job.




### Configure Managed I/O

If your pipeline uses [Managed I/O for Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka), set the following configuration options to authenticate with Managed Service for Apache Kafka:

  * `"security.protocol"`: `"SASL_SSL"`
  * `"sasl.mechanism"`: `"OAUTHBEARER"`
  * `"sasl.login.callback.handler.class"`: `"com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler"`
  * `"sasl.jaas.config"`: `"org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;"`



The follow examples show how to configure managed I/O for Managed Service for Apache Kafka:

### Java
    
    
        // Create configuration parameters for the Managed I/O transform.
        ImmutableMap<String, Object> config = ImmutableMap.<String, Object>builder()
          .put("bootstrap_servers", options.getBootstrapServer())
          .put("topic", options.getTopic())
          .put("data_format", "RAW")
          // Set the following fields to authenticate with Application Default
          // Credentials (ADC):
          .put("security.protocol", "SASL_SSL")
          .put("sasl.mechanism", "OAUTHBEARER")
          .put("sasl.login.callback.handler.class",
              "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler")
          .put("sasl.jaas.config",   "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;")
          .build();
    

### Python
    
    
    pipeline
    | beam.managed.Read(
        beam.managed.KAFKA,
        config={
          "bootstrap_servers": options.bootstrap_server,
          "topic": options.topic,
          "data_format": "RAW",
          # Set the following fields to authenticate with Application Default
          # Credentials (ADC):
          "security.protocol": "SASL_SSL",
          "sasl.mechanism": "OAUTHBEARER",
          "sasl.login.callback.handler.class":
              "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler",
          "sasl.jaas.config":
              "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;"
        }
    )
    

### Configure the `KafkaIO` connector

The follow examples show how to configure the `KafkaIO` connector for Managed Service for Apache Kafka:

### Java
    
    
    String bootstap = options.getBootstrap();
    String topicName = options.getTopic();
    
    // Read from Kafka
    pipeline.apply(KafkaIO.<String, String>read()
        .withBootstrapServers(bootstap)
        .withTopic(topicName)
        .withKeyDeserializer(IntegerSerializer.class)
        .withValueDeserializer(StringDeserializer.class)
        .withGCPApplicationDefaultCredentials())
    
    // Write to Kafka
    pipeline.apply(KafkaIO.<Integer, String>write()
        .withBootstrapServers(bootstrap)
        .withTopic(topicName)
        .withKeySerializer(IntegerSerializer.class)
        .withValueSerializer(StringSerializer.class)
        .withGCPApplicationDefaultCredentials());
    

### Python
    
    
    WriteToKafka(
      producer_config={
        "bootstrap.servers": options.bootstrap_servers,
        "security.protocol": 'SASL_SSL',
        "sasl.mechanism": "OAUTHBEARER",
        "sasl.login.callback.handler.class": "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler",
        "sasl.jaas.config": "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;"
      },
      topic=options.topic,
      key_serializer=("org.apache.kafka.common.serialization." "LongSerializer"),
      value_serializer=("org.apache.kafka.common.serialization." "StringSerializer")
    )
    

## What's next

  * Learn more about [Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview).
  * [Write data from Managed Service for Apache Kafka to BigQuery](https://docs.cloud.google.com/dataflow/docs/kafka-dataflow).
  * [Read from Apache Kafka to Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka).
  * [Write from Dataflow to Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/write-to-kafka).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
