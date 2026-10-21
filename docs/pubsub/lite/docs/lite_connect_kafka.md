---
url: https://docs.cloud.google.com/pubsub/lite/docs/lite_connect_kafka/
title: Connect Pub/Sub Lite to Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:10.099389+00:00
---

# Connect Pub/Sub Lite to Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/lite_connect_kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Connect Pub/Sub Lite to Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

This document describes how to integrate Apache Kafka and Pub/Sub Lite by using the Pub/Sub Group Kafka Connector.

**Note:** You can also use this connector with Pub/Sub. See [Connect Pub/Sub to Apache Kafka](https://docs.cloud.google.com/pubsub/docs/connect_kafka). 

## About the Pub/Sub Group Kafka Connector

Apache Kafka is an open source platform for streaming events. It is commonly used in distributed architectures to enable communication between loosely coupled components. Pub/Sub Lite is a managed service for sending and receiving messages asynchronously. As with Kafka, you can use Pub/Sub Lite to communicate between components in your cloud architecture.

The Pub/Sub Group Kafka Connector allows you to integrate these two systems. The following connectors are packaged in the Connector JAR:

  * The **sink connector** reads records from one or more Kafka topics and publishes them to Pub/Sub Lite.
  * The **source connector** reads messages from a Pub/Sub Lite topic and publishes them to Kafka.



Here are some scenarios in which you might use the Pub/Sub Group Kafka Connector:

  * You are migrating a Kafka-based architecture to Google Cloud.
  * You have a frontend system that stores events in Kafka outside of Google Cloud, but you also use Google Cloud to run some of your backend services, which need to receive the Kafka events.
  * You collect logs from an on-premises Kafka solution and send them to Google Cloud for data analytics.
  * You have a frontend system that uses Google Cloud, but you also store data on-premises using Kafka.



The connector requires [Kafka Connect](https://kafka.apache.org/documentation.html#connect), which is a framework for streaming data between Kafka and other systems. To use the connector, you must run Kafka Connect alongside your Kafka cluster.

This document assumes that you are familiar with both Kafka and Pub/Sub Lite. To get started with Pub/Sub Lite, see [Publish and receive messages in Pub/Sub Lite by using the Google Cloud console](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console).

## Get started with the Pub/Sub Group Kafka Connector

This section walks you through the following tasks: 

  1. Configure the Pub/Sub Group Kafka Connector.
  2. Send events from Kafka to Pub/Sub Lite.
  3. Send messages from Pub/Sub Lite to Kafka.

**Note:** This section uses Kafka Connect in standalone mode, which is suitable for testing. For production systems, distributed mode is recommended. For information about running Kafka Connect in distributed mode, see [Running Kafka Connect](https://kafka.apache.org/documentation.html#connect_running) in the Apache Kafka documentation.

### Prerequisites

#### Install Kafka

Follow the [Apache Kafka quickstart](https://kafka.apache.org/quickstart) to install a single-node Kafka on your local machine. Complete these steps in the quickstart:

  1. Download the latest Kafka release and extract it.
  2. Start the Kafka environment.
  3. Create a Kafka topic.



#### Authenticate

The Pub/Sub Group Kafka Connector must authenticate with Pub/Sub in order to send and receive Pub/Sub messages. To set up authentication, perform the following steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/pubsublite.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/pubsublite.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.


**Note:** For production workloads, we recommend using [Workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) to authenticate.

#### Download the connector JAR

Download the connector JAR file to your local machine. For more information, see [Acquire the connector](https://github.com/googleapis/java-pubsub-group-kafka-connector#acquire-the-connector) in the GitHub readme.

#### Copy the connector configuration files

  1. Clone or download the [GitHub repository](https://github.com/googleapis/java-pubsub-group-kafka-connector) for the connector.
         
         git clone https://github.com/googleapis/java-pubsub-group-kafka-connector.git
         cd java-pubsub-group-kafka-connector
         

  2. Copy the contents of the `config` directory into the `config` subdirectory of your Kafka installation.
         
         cp config/* [path to Kafka installation]/config/
         




These files contain configuration settings for the connector.

### Update your Kafka Connect configuration

  1. Navigate to the directory that contains the Kafka Connect binary that you downloaded.
  2. In the Kafka Connect binary directory, open the file named `config/connect-standalone.properties` in a text editor.
  3. If the `plugin.path property` is commented out, uncomment it.
  4. Update the `plugin.path property` to include the path to the connector JAR.

Example:
         
         plugin.path=/home/PubSubKafkaConnector/pubsub-group-kafka-connector-1.0.0.jar
         

  5. Set the `offset.storage.file.filename` property to a local file name. In standalone mode, Kafka uses this file to store offset data.

Example:
         
         offset.storage.file.filename=/tmp/connect.offsets
         




### Forward events from Kafka to Pub/Sub Lite

This section describes how to start the sink connector, publish events to Kafka, and then read the forwarded messages from Pub/Sub Lite.

  1. Use the Google Cloud CLI to create a Pub/Sub Lite reservation.
         
         gcloud pubsub lite-reservations create RESERVATION_NAME \
         --location=LOCATION \
         --throughput-capacity=4

Replace the following:

     * RESERVATION_NAME: The name of the Pub/Sub Lite reservation.
     * LOCATION: The [location](https://docs.cloud.google.com/pubsub/lite/docs/locations) of the reservation.
  2. Use the Google Cloud CLI to create a Pub/Sub Lite topic with a subscription.
         
         gcloud pubsub lite-topics create LITE_TOPIC \
         --location=LOCATION \
         --partitions=2 \
         --per-partition-bytes=30GiB \
         --throughput-reservation=RESERVATION_NAME
         
         gcloud pubsub lite-subscriptions create LITE_SUBSCRIPTION \
         --location=LOCATION \
         --topic=LITE_TOPIC

Replace the following:

     * LITE_TOPIC: The name of the Pub/Sub Lite topic to receive messages from Kafka.
     * LOCATION: The location of the topic. The value must match the location of the reservation.
     * RESERVATION_NAME: The name of the Pub/Sub Lite reservation.
     * LITE_SUBSCRIPTION: The name of a Pub/Sub Lite subscription for the topic.
  3. Open the file `/config/pubsub-lite-sink-connector.properties` in a text editor. Add values for the following properties, which are marked `"TODO"` in the comments:
         
         topics=KAFKA_TOPICS
         pubsublite.project=PROJECT_ID
         pubsublite.location=LOCATION
         pubsublite.topic=LITE_TOPIC

Replace the following:

     * KAFKA_TOPICS: A comma-separated list of Kafka topics to read from.
     * PROJECT_ID: The Google Cloud project that contains your Pub/Sub Lite topic.
     * LOCATION: The location of the Pub/Sub Lite topic.
     * LITE_TOPIC: The Pub/Sub Lite topic to receive messages from Kafka.
  4. From the Kafka directory, run the following command:
         
         bin/connect-standalone.sh \
           config/connect-standalone.properties \
           config/pubsub-lite-sink-connector.properties
         

  5. Follow the steps in the [Apache Kafka quickstart](https://kafka.apache.org/quickstart#quickstart_send) to write some events to your Kafka topic.

  6. Subscribe to the Pub/Sub Lite subscription by using any of the methods shown in [Receiving messages from Lite subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/subscribing).




### Forward messages from Pub/Sub Lite to Kafka

This section describes how to start the source connector, publish messages to Pub/Sub Lite, and read the forwarded messages from Kafka.

  1. Use the Google Cloud CLI to create a Pub/Sub Lite reservation.
         
         gcloud pubsub lite-reservations create RESERVATION_NAME \
         --location=LOCATION \
         --throughput-capacity=4

Replace the following:

     * RESERVATION_NAME: The name of the Pub/Sub Lite reservation.
     * LOCATION: The [location](https://docs.cloud.google.com/pubsub/lite/docs/locations) of the reservation.
  2. Use the Google Cloud CLI to create a Pub/Sub Lite topic with a subscription.
         
         gcloud pubsub lite-topics create LITE_TOPIC \
         --location=LOCATION \
         --partitions=2 \
         --per-partition-bytes=30GiB \
         --throughput-reservation=RESERVATION_NAME
         
         gcloud pubsub lite-subscriptions create LITE_SUBSCRIPTION \
         --location=LOCATION \
         --topic=LITE_TOPIC

Replace the following:

     * LITE_TOPIC: The name of the Pub/Sub Lite topic.
     * LOCATION: The location of the topic. The value must match the location of the reservation.
     * RESERVATION_NAME: The name of the Pub/Sub Lite reservation.
     * LITE_SUBSCRIPTION: The name of a Pub/Sub Lite subscription for the topic.
  3. Open the file named `/config/pubsub-lite-source-connector.properties` in a text editor. Add values for the following properties, which are marked `"TODO"` in the comments:
         
         topic=KAFKA_TOPIC
         pubsublite.project=PROJECT_ID
         pubsublite.location=LOCATION
         pubsublite.subscription=LITE_SUBSCRIPTION

Replace the following:

     * KAFKA_TOPIC: The Kafka topics to receive the Pub/Sub messages.
     * PROJECT_ID: The Google Cloud project that contains your Pub/Sub topic.
     * LOCATION: The location of the Pub/Sub Lite topic.
     * LITE_SUBSCRIPTION: The Pub/Sub Lite topic.
  4. From the Kafka directory, run the following command:
         
         bin/connect-standalone.sh \
           config/connect-standalone.properties \
           config/pubsub-lite-source-connector.properties
         

  5. Publish messages to the Pub/Sub Lite topic by using any of the methods shown in [Publishing messages to Lite topics](https://docs.cloud.google.com/pubsub/lite/docs/publishing).

  6. Read the message from Kafka. Follow the steps in the [Apache Kafka quickstart](https://kafka.apache.org/quickstart#quickstart_consume) to read the messages from the Kafka topic.




## Message conversion

A [Kafka record](https://kafka.apache.org/documentation/#record) contains a key and a value, which are variable-length byte arrays. Optionally, a Kafka record can also have headers, which are key-value pairs. A [Pub/Sub Lite message](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PubSubMessage) has the following fields:

  * `key`: Message key (`bytes`)
  * `data`: Message data (`bytes`)
  * `attributes`: Zero or more attributes. Each attribute is a `(key,values[])` map. A single attribute can have multiple values.
  * `event_time`: An optional user-provided event timestamp.



Kafka Connect uses converters to serialize keys and values to and from Kafka. To control the serialization, set the following properties in the connector configuration files:

  * `key.converter`: The converter used to serialize record keys.
  * `value.converter`: The converter used to serialize record values.



### Conversion from Kafka to Pub/Sub Lite

The sink connector converts Kafka records to Pub/Sub Lite messages as follows.

Kafka record ([`SinkRecord`](https://www.javadoc.io/doc/org.apache.kafka/connect-api/latest/org/apache/kafka/connect/sink/SinkRecord.html)) | Pub/Sub Lite message  
---|---  
Key | `key`  
Value | `data` | Headers | `attributes`  
Timestamp | `eventTime`  
[Timestamp type](https://kafka.apache.org/documentation/#topicconfigs_message.timestamp.type) | `attributes["x-goog-pubsublite-source-kafka-event-time-type"]`  
Topic | `attributes["x-goog-pubsublite-source-kafka-topic"]`  
Partition | `attributes["x-goog-pubsublite-source-kafka-offset"]`  
Offset | `attributes["x-goog-pubsublite-source-kafka-partition"]`  
  
Keys, values, and headers are encoded to as follows:

  * Null schemas are treated as string schemas.
  * Bytes payloads are written directly with no conversion.
  * String, integer, and floating-point payloads are encoded into a sequence of UTF-8 bytes.
  * All other payloads are encoded into a Protocol buffer [`Value`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value) type and then converted to a byte string. 
    * Nested string fields are encoded into a protobuf `Value`.
    * Nested bytes fields are encoded to a protobuf `Value` holding the base64-encoded bytes.
    * Nested numeric fields are encoded as a double into a protobuf `Value`.
    * Maps with array, map, or struct keys are not supported.



### Conversion from Pub/Sub Lite to Kafka

The source connector converts Pub/Sub Lite messages to Kafka records as follows:

Pub/Sub Lite message | Kafka record ([`SourceRecord`](https://www.javadoc.io/doc/org.apache.kafka/connect-api/latest/org/apache/kafka/connect/source/SourceRecord.html))   
---|---  
`key` | Key  
`data` | Value  
`attributes` | Headers  
`event_time` | Timestamp. If `event_time` is not present, the publish time is used.  
  
## Configuration options

In addition to the configurations provided by the Kafka Connect API, the connector supports the following Pub/Sub Lite configurations.

### Sink connector configuration options

The sink connector supports the following configuration options.

Setting | Data type | Description  
---|---|---  
`connector.class` | `String` | **Required.** The Java class for the connector. For the Pub/Sub Lite sink connector, the value must be `com.google.pubsublite.kafka.sink.PubSubLiteSinkConnector`.   
`gcp.credentials.file.path` | `String` | Optional. The path to a file that stores Google Cloud credentials for authenticating Pub/Sub Lite.  
`gcp.credentials.json` | `String` | Optional. A JSON blob that contains Google Cloud for authenticating Pub/Sub Lite.  
`pubsublite.location` | `String` | **Required**. The location of the Pub/Sub Lite topic.  
`pubsublite.project` | `String` | **Required**. The Google Cloud that contains the Pub/Sub Lite topic.  
`pubsublite.topic` | `String` | **Required**. The Pub/Sub Lite topic to publish Kafka records to.  
`topics` | `String` | **Required**. A comma-separated list of Kafka topics to read from.  
  
### Source connector configuration options

The source connector supports the following configuration options.

Setting | Data type | Description  
---|---|---  
`connector.class` | `String` | **Required.** The Java class for the connector. For the Pub/Sub Lite source connector, the value must be `com.google.pubsublite.kafka.source.PubSubLiteSourceConnector`.   
`gcp.credentials.file.path` | `String` | Optional. The path to a file that stores Google Cloud credentials for authenticating Pub/Sub Lite.  
`gcp.credentials.json` | `String` | Optional. A JSON blob that contains Google Cloud for authenticating Pub/Sub Lite.  
`kafka.topic` | `String` | **Required**. The Kafka topic that receives messages from Pub/Sub Lite.  
`pubsublite.location` | `String` | **Required**. The location of the Pub/Sub Lite topic.  
`pubsublite.partition_flow_control.bytes` | `Long` | The maximum number of outstanding bytes per Pub/Sub Lite partition. Default: 20,000,000  
`pubsublite.partition_flow_control.messages` | `Long` |  The maximum number of outstanding messages per Pub/Sub Lite partition. Default: `Long.MAX_VALUE`  
`pubsublite.project` | `String` | **Required.** The Google Cloud project that contains the Pub/Sub Lite topic.  
`pubsublite.subscription` | `String` | **Required**. The name of the Pub/Sub Lite subscription to pull messages from.  
  
## What's next

  * [Understand the differences between Kafka and Pub/Sub](https://docs.cloud.google.com/architecture/migrating-from-kafka-to-pubsub).
  * [Learn more about the Pub/Sub Group Kafka Connector](https://cloud.google.com/blog/products/data-analytics/pubsub-group-kafka-connector-is-now-ga).
  * See the Pub/Sub Group Kafka Connector [GitHub repository](https://github.com/googleapis/java-pubsub-group-kafka-connector). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
