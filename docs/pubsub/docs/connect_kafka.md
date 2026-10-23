---
url: https://docs.cloud.google.com/pubsub/docs/connect_kafka/
title: Connect Pub/Sub to Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:04.459650+00:00
---

# Connect Pub/Sub to Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/connect_kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Connect Pub/Sub to Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to integrate Apache Kafka and Pub/Sub by using the Pub/Sub Group Kafka Connector.

**Note:** You can also use this connector with Pub/Sub Lite. See [Connect Pub/Sub Lite to Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/lite_connect_kafka).

## About the Pub/Sub Group Kafka Connector

Apache Kafka is an open source platform for streaming events. It is commonly used in distributed architectures to enable communication between loosely coupled components. Pub/Sub is a managed service for sending and receiving messages asynchronously. As with Kafka, you can use Pub/Sub to communicate between components in your cloud architecture.

The Pub/Sub Group Kafka Connector allows you to integrate these two systems. The following connectors are packaged in the Connector JAR:

  * The **sink connector** reads records from one or more Kafka topics and publishes them to Pub/Sub.
  * The **source connector** reads messages from a Pub/Sub topic and publishes them to Kafka.



Here are some scenarios in which you might use the Pub/Sub Group Kafka Connector:

  * You are migrating a Kafka-based architecture to Google Cloud.
  * You have a frontend system that stores events in Kafka outside of Google Cloud, but you also use Google Cloud to run some of your backend services, which need to receive the Kafka events.
  * You collect logs from an on-premises Kafka solution and send them to Google Cloud for data analytics.
  * You have a frontend system that uses Google Cloud, but you also store data on-premises using Kafka.



The connector requires [Kafka Connect](https://kafka.apache.org/documentation.html#connect), which is a framework for streaming data between Kafka and other systems. To use the connector, you must run Kafka Connect alongside your Kafka cluster.

This document assumes that you are familiar with both Kafka and Pub/Sub. Before you read this document, it's a good idea to complete one of the [Pub/Sub quickstarts](https://docs.cloud.google.com/pubsub/docs/quickstarts).

The Pub/Sub connector does not support any integration between Google Cloud IAM and Kafka Connect ACLs.

## Get started with the connector

This section walks you through the following tasks: 

  1. Configure the Pub/Sub Group Kafka Connector.
  2. Send events from Kafka to Pub/Sub.
  3. Send messages from Pub/Sub to Kafka.

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

  7. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/pubsub.admin`
         
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

  13. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/pubsub.admin`
         
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
         




### Forward events from Kafka to Pub/Sub

This section describes how to start the sink connector, publish events to Kafka, and then read the forwarded messages from Pub/Sub.

  1. Use the Google Cloud CLI to create a Pub/Sub topic with a subscription.
         
         gcloud pubsub topics create PUBSUB_TOPIC
         gcloud pubsub subscriptions create PUBSUB_SUBSCRIPTION --topic=PUBSUB_TOPIC

Replace the following:

     * PUBSUB_TOPIC: The name of a Pub/Sub topic to receive the messages from Kafka.
     * PUBSUB_SUBSCRIPTION: The name of a Pub/Sub subscription for the topic.
  2. Open the file `/config/cps-sink-connector.properties` in a text editor. Add values for the following properties, which are marked `"TODO"` in the comments:
         
         topics=KAFKA_TOPICS
         cps.project=PROJECT_ID
         cps.topic=PUBSUB_TOPIC

Replace the following:

     * KAFKA_TOPICS: A comma-separated list of Kafka topics to read from.
     * PROJECT_ID: The Google Cloud project that contains your Pub/Sub topic.
     * PUBSUB_TOPIC: The Pub/Sub topic to receive the messages from Kafka.
  3. From the Kafka directory, run the following command:
         
         bin/connect-standalone.sh \
           config/connect-standalone.properties \
           config/cps-sink-connector.properties
         

  4. Follow the steps in the [Apache Kafka quickstart](https://kafka.apache.org/quickstart#quickstart_send) to write some events to your Kafka topic.

  5. Use the gcloud CLI to read the events from Pub/Sub.
         
         gcloud pubsub subscriptions pull PUBSUB_SUBSCRIPTION --auto-ack




### Forward messages from Pub/Sub to Kafka

This section describes how to start the source connector, publish messages to Pub/Sub, and read the forwarded messages from Kafka.

  1. Use the gcloud CLI to create a Pub/Sub topic with a subscription.
         
         gcloud pubsub topics create PUBSUB_TOPIC
         gcloud pubsub subscriptions create PUBSUB_SUBSCRIPTION --topic=PUBSUB_TOPIC

Replace the following:

     * PUBSUB_TOPIC: The name of a Pub/Sub topic.
     * PUBSUB_SUBSCRIPTION: The name of a Pub/Sub subscription.
  2. Open the file named `/config/cps-source-connector.properties` in a text editor. Add values for the following properties, which are marked `"TODO"` in the comments:
         
         kafka.topic=KAFKA_TOPIC
         cps.project=PROJECT_ID
         cps.subscription=PUBSUB_SUBSCRIPTION

Replace the following:

     * KAFKA_TOPIC: The Kafka topic to receive the Pub/Sub messages.
     * PROJECT_ID: The Google Cloud project that contains your Pub/Sub topic.
     * PUBSUB_TOPIC: The Pub/Sub topic.
  3. From the Kafka directory, run the following command:
         
         bin/connect-standalone.sh \
           config/connect-standalone.properties \
           config/cps-source-connector.properties
         

  4. Use the gcloud CLI to publish a message to Pub/Sub.
         
         gcloud pubsub topics publish PUBSUB_TOPIC --message="message 1"

  5. Read the message from Kafka. Follow the steps in the [Apache Kafka quickstart](https://kafka.apache.org/quickstart#quickstart_consume) to read the messages from the Kafka topic.




## Message conversion

A [Kafka record](https://kafka.apache.org/documentation/#record) contains a key and a value, which are variable-length byte arrays. Optionally, a Kafka record can also have headers, which are key-value pairs. A [Pub/Sub message](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage) has two main parts: the message body and zero or more key-value attributes.

Kafka Connect uses converters to serialize keys and values to and from Kafka. To control the serialization, set the following properties in the connector configuration files:

  * `key.converter`: The converter used to serialize record keys.
  * `value.converter`: The converter used to serialize record values.



The body of a Pub/Sub message is a `ByteString` object, so the most efficient conversion is to copy the payload directly. For that reason, we recommend using a converter that produces primitive data types (integer, float, string, or bytes schema) where possible, to prevent deserializing and reserializing the same message body.

### Conversion from Kafka to Pub/Sub

The sink connector converts Kafka records to Pub/Sub messages as follows:

  * The Kafka record key is stored as an attribute named `"key"` in the Pub/Sub message.
  * By default, the connector drops any headers in the Kafka record. However, if you set the `headers.publish` configuration option to `true`, the connector writes the headers as Pub/Sub attributes. The connector skips any headers that exceed the Pub/Sub [limits on message attributes](https://docs.cloud.google.com/pubsub/quotas#resource_limits).
  * For integer, float, string, and bytes schemas, the connector passes the bytes of the Kafka record value directly into the Pub/Sub message body.
  * For struct schemas, the connector writes each field as an attribute of the Pub/Sub message. For example, if the field is `{ "id"=123 }`, the resulting Pub/Sub message has an attribute `"id"="123"`. The field value is always converted to a string. Map and struct types are not supported as field types within a struct.
  * For map schemas, the connector writes each key-value pair as an attribute of the Pub/Sub message. For example, if the map is `{"alice"=1,"bob"=2}`, the resulting Pub/Sub message has two attributes, `"alice"="1"` and `"bob"="2"`. The keys and values are converted to strings.



Struct and map schemas have some additional behaviors:

  * Optionally, you can specify a particular struct field or map key to be the message body, by setting the `messageBodyName` configuration property. The value of the field or key is stored as a `ByteString` in the message body. If you don't set `messageBodyName`, then the message body is empty for struct and map schemas.

  * For array values, the connector supports only primitive array types. The sequence of values in the array is concatenated into a single `ByteString` object.




### Conversion from Pub/Sub to Kafka

The source connector converts Pub/Sub messages to Kafka records as follows:

  * **Kafka record key** : By default, the key is set to `null`. Optionally, you can specify a Pub/Sub message attribute to use as the key, by setting the `kafka.key.attribute` configuration option. In that case, the connector looks for an attribute with that name and sets the record key to the attribute value. If the specified attribute is not present, the record key is set to `null`.

  * **Kafka record value**. The connector writes the record value as follows:

    * If the Pub/Sub message has no custom attributes, the connector writes the Pub/Sub message body directly to the Kafka record value as a `byte[]` type, using the converter specified by `value.converter`.

    * If the Pub/Sub message has custom attributes and `kafka.record.headers` is `false`, the connector writes a struct to the record value. The struct contains one field for each attribute, and a field named `"message"` whose value is the Pub/Sub message body (stored as bytes):
          
          {
            "message": "<Pub/Sub message body>",
            "<attribute-1>": "<value-1>",
            "<attribute-2>": "<value-2>",
            ....
          }
          

In this case, you must use a `value.converter` that is compatible with `struct` schemas, such as `org.apache.kafka.connect.json.JsonConverter`.

    * If the Pub/Sub message has custom attributes and `kafka.record.headers` is `true`, the connector writes the attributes as Kafka record headers. It writes the Pub/Sub message body directly to the Kafka record value as a `byte[]` type, using the converter specified by `value.converter`.

  * **Kafka record headers**. By default, the headers are empty, unless you set `kafka.record.headers` to `true`.


**Note:** In your Kafka broker configuration, set `message.max.bytes` large enough to handle your Pub/Sub messages. Pub/Sub has a [maximum message size](https://docs.cloud.google.com/pubsub/quotas#resource_limits).

## Configuration options

In addition to the configurations provided by the Kafka Connect API, the Pub/Sub Group Kafka Connector supports the sink and source configuration as described in [Pub/Sub connector configs](https://github.com/googleapis/java-pubsub-group-kafka-connector?tab=readme-ov-file#pubsub-connector-configs).

## Getting support

If you need help, create a [support ticket](https://cloud.google.com/support-hub). For general questions and discussions, create an issue in the [GitHub repository](https://github.com/googleapis/java-pubsub-group-kafka-connector/issues).

## What's next

  * [Understand the differences between Kafka and Pub/Sub](https://docs.cloud.google.com/architecture/migrating-from-kafka-to-pubsub).
  * [Learn more about the Pub/Sub Group Kafka Connector](https://cloud.google.com/blog/products/data-analytics/pubsub-group-kafka-connector-is-now-ga).
  * See the Pub/Sub Group Kafka Connector [GitHub repository](https://github.com/googleapis/java-pubsub-group-kafka-connector).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
