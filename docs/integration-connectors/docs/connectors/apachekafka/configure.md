---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/apachekafka/configure/
title: Apache Kafka \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:29.929895+00:00
---

# Apache Kafka  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/apachekafka/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Apache Kafka

Use the Kafka connector to integrate with Apache Kafka and publish messages to specific topics. The Kafka connector also supports event subscription, which allows the creation of triggers when messages are received in a topic.

## Supported versions

The Apache Kafka connector leverages the native client libraries to establish a connection to a given Kafka cluster, and the connector works with client version 3.3.1. However, the connector can establish connectivity to Kafka clusters from versions 3.0 to 3.3.1.

## Before you begin

Before using the Apache Kafka connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** step, choose the location for the new Apache Kafka connection: 
     1. **Region:** Select a region from the list. 
     2. Click **Next**.
  4. In the **Connection Details** step, provide details about the new Apache Kafka connection: 
     1. **Connector version:** Choose an available version of the Apache Kafka connector from the list. 
     2. **Connection Name:** Enter a name for the Apache Kafka connection. **Note:** Connection names must meet the following criteria: 
        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
        * For connectors that [support event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#enable-event-subscriptions-in-connections), the connection names cannot begin with the "goog" prefix. 
     3. (Optional) **Description:** Enter a description for the connection.
     4. (Optional) **Enable Cloud Logging:** Select this checkbox to store all log data of the connection.
     5. **Service Account** : Select a service account with the required IAM roles for the Apache Kafka connection.
     6. The **Enable event subscription, entity and actions** option is selected by default for the Apache Kafka connection. **Note:** This connector doesn't support the `Enable only event subscription` option.
     7. **Type Detection Scheme:** Select `MessageOnly`.
     8. **Registry Service** : The Schema Registry service used for working with topic schemas. 
     9. **Registry Type** : Type of the schema specified for the a specific topic. 
     10. **Registry Version** : Version of the schema read from `RegistryUrl` for the specified topic. 
     11. **Registry User** : Username or Access Key value to authorize with the server specified in `RegistryUrl`. 
     12. **Registry Password** : Secret Manager Secret containing the password/secret Key value to authorize with the server specified in `RegistryUrl`. 
     13. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     14. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key and value pair.
     15. **Enable SSL** : This field sets whether SSL is enabled. 
     16. Click **Next**.
  5. In the **Destinations** section, enter details of the Kafka bootstrap server you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To specify additional Kafka bootstrap servers, click **\+ ADD DESTINATION**.

  6. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Apache Kafka connection:

     * **Username and password**
       * **Username** : The Apache Kafka username to use for the connection.
       * **Password** : Secret Manager Secret containing the password associated with the Apache Kafka username.
       * **Auth Scheme** : The scheme used for authentication. 

The following Auth Scheme are supported by the Apache Kafka connection:

         * **Plain**
         * **SCRAM-SHA-1**
         * **SCRAM-SHA-256**
     * **Not Available**

If you want to use anonymous login, select **Not Available**.

  2. Click **Next**.


* Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 

  1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
  2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.


* Click **Next**.
* **Review** : Review your connection and authentication details.
* Click **Create**.

## System limitations

The Apache Kafka connector can process a maximum of 50 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

### PublishMessage action

This [action](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) publishes a message to a Apache Kafka topic. The following tables describes the input and output parameters of the `PublishMessage` action.

#### Input parameters

Parameter name | Required | Data type | Description  
---|---|---|---  
Topic | Yes | String | Name of the topic to which you want to publish the message.  
Partition | No | String | The partition to which the message is assigned. The value must be valid for the given topic. If you don't set this value, it is automatically set by the native client.  
Key | No | String | The message key.  
Message | Yes | String | The message you want to publish. The message should be a stringified JSON and the maximum message size supported is 10MB.  
HasBytes | No | Boolean | Specifies if the message is in binary format.  
MessageBytes | No | String | The message in the form of a Base64 encoded string.  
Validate | No | Boolean | Specifies if the message to be published must be validated against the message schema defined in the schema registry for the topic. If you have specified the schema registry when creating a connection, then the topic's schema definition from the registry is used for the purpose of validation. The default value for this field is `false`.  
  
#### Output parameters

Parameter name | Data type | Description  
---|---|---  
PartitionWritten | Integer | The partition that the message was written to.  
OffsetWritten | Long | The position in the partition that the message was written to.  
TimestampWritten | Long | The time (Unix timestamp) at which the message was committed to the partition.  
KeyWritten | String | The value of the message key that was written. The value is NULL if no message key was provided when writing the message.  
Success | Boolean | Specifies if the message was published.  
**Note:** The results of all the entity operations and actions will be available as a JSON response in the [Connectors task's](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) `connectorOutputPayload` response parameter after you run your integration.

A sample response of the `PublishMessage` action is as follows:
    
    
    {Success: true,
    PartitionWritten: 1,
    OffsetWritten: 22301,
    KeyWritten: "dGVzdA==",
    TimestampWritten: 1690806748}

## Configuration for Confluent Cloud

Configuration for the Confluent Cloud differs slightly from the previously documented steps for Apache Kafka. Consider the following points when creating a connection for Confluent Cloud: 

  * The Confluent Cloud cluster API key is used as the username, and the key's Secret Manager Secret is used as the password for connecting to the bootstrap servers. You need to create an API key in Confluent Cloud if you don't have it already. 
  * Select **Use SSL** in the `Connection Details` section.
  * If you are using schema registry, configure the following values: 
    * In the `Connection Details` section: 
      * **Registry Version:** Enter the registry version number. If you want to use the latest version, enter `latest`.
      * **Registry User:** Enter the schema registry API key. You need to create a schema registry API key if you don't have it already.
      * **Registry Password:** Enter the Secret Manager Secret of the registry password.
      * **Secret Version:** Select the secret version number.
      * **Registry Type:** Select `Confluent`.
      * **Type Detection Scheme:** Select `MessageOnly`
    * In the `Destinations` section, enter the registry URL in the hostname field. 

## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
type_detection_scheme | ENUM | True | The scheme used for authentication with the Apache Kafka broker. Supported values are: MessageOnly  
registry_service | ENUM | False | The Schema Registry service used for working with topic schemas. Supported values are: Confluent  
registry_type | ENUM | False | Type of the schema specified for the a specific topic. Supported values are: AVRO, JSON  
registry_version | STRING | False | Version of the schema read from RegistryUrl for the specified topic. Valid values for registry version are between [1,2^31-1] or the string "latest", which returns the last registered schema.   
registry_user | STRING | False | Username to authorize with the server specified in RegistryUrl .   
registry_password | SECRET | False | Secret Manager Secret containing the password/secret Key value to authorize with the server specified in RegistryUrl.   
usessl | BOOLEAN | False | This field sets whether SSL is enabled.   
  
## Use the Apache Kafka connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

    * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
    * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).

## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

    * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
    * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
    * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
