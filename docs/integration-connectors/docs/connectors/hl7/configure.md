---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/hl7/configure/
title: HL7 \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:51.034037+00:00
---

# HL7  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/hl7/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# HL7 

The HL7 connector provides connectivity to HL7 TCP and REST endpoints.

## Before you begin

Before using the HL7 connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`
      * `role Healthcare HL7v2 Message Ingest`, required only if the selected **Destination Protocol** is REST (Google Cloud HealthCare API) for ingesting HL7 message into the HL7v2 Store.

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 

  * Create an [HL7 store](https://cloud.google.com/healthcare-api/docs/how-tos/hl7v2).
  * For using TCP(MLLP) as a **Destination Protocol** , ensure that there is an MLLP Server up and running to receive messages. Provide the server details while adding the destination.



## Configure the connector

Configuring the connector requires you to create a connection to your Healthcare System or the Google Cloud Healthcare API. A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following steps:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **HL7** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria:

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. **Service Account** : Select a service account that has the required roles. 
     6. To use the connection for event subscriptions, select **Enable event subscription**. Selecting this option, enables the event subscription with actions. **Note:** The `Enable only event subscription` option isn't supported for this connection.
     7. **Receive Timeout** :The SO_TIMEOUT value (in milliseconds) is used when waiting for the start of an MLLP frame. The default value is 15000 milliseconds. 
     8. **Destination Protocol** : Select a destination protocol from the dropdown.
        1. If TCP (MLLP) is selected as a **Destination Protocol** , then enter the hostname and port of the MLLP server while adding the **Destination**. 
        2. If REST (Google Cloud HealthCare API) is selected as a **Destination Protocol** , then specify the following details: 
           1. **Project ID** : The Google Cloud project ID where the HL7 store is located. 
           2. **Location** : The location of your dataset and HL7v2 store.
           3. **Dataset ID** : The ID for the dataset that holds the HL7v2 store.
           4. **HL7 Store ID** : The ID for the HL7v2 store where you store the HL7v2 message. 
     9. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     10. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair. 
     11. Click **Next**.
  5. If you selected TCP(MLLP) as the Destination protocol, then in the **Destinations** section, enter details of the remote host (MLLP Server) you want to connect. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

**Note:** This connector supports only one destination.
  6. Click **Next**.


* The HL7 connection doesn't require any authentication. Click **Next**. 
* If you have enabled the event subscription, the **Event Subscription Details** section appears on the connection creation page. To understand how to configure event subscription details, see Configure event subscription.
* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure event subscription

* In the **Event Subscription Details** section, configure the event related details. 

  * **Project Name** : The Google Cloud project where the Pub/Sub instance resides.
  * **Pub/Sub Topic Name** : The Pub/Sub topic name to be associated with the HL7v2 store to which the notification messages will be sent.
  * Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
    1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
    2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.


**Tip:** To understand how you can use event subscription in your integrations, see [HL7 trigger](https://docs.cloud.google.com/application-integration/docs/configure-hl7-trigger). 

## Entities, operations, and actions

All the Integration Connectors provide a layer of abstraction for the objects of the connected application. You can access an application's objects only through this abstraction. The abstraction is exposed to you as entities, operations, and actions.

**Note:** You can view the entities, operations, and actions of a connector in the [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).

  * **Entity:** An entity can be thought of as an object, or a collection of properties, in the connected application or service. The definition of an entity differs from a connector to a connector. For example, in a database connector, tables are the entities, in a file server connector, folders are the entities, and in a messaging system connector, queues are the entities. 

However, it is possible that a connector doesn't support or have any entities, in which case the `Entities` list will be empty.

  * **Operation:** An operation is the activity that you can perform on an entity. You can perform any of the following operations on an entity: 
    * [List](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Get](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Create](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Update](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Delete](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)

Selecting an entity from the available list, generates a list of operations available for the entity. For a detailed description of the operations, see the Connectors task's [entity operations](https://docs.cloud.google.com/application-integration/docs/connectors-task#config-prop). However, if a connector doesn't support any of the entity operations, such unsupported operations aren't listed in the `Operations` list.

  * **Action:** An action is a first class function that is made available to the integration through the connector interface. An action lets you make changes to an entity or entities, and vary from connector to connector. Normally, an action will have some input parameters, and an output parameter. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty. 

**Note:** All entities and actions will have a schema associated with them. For example, an action schema will have the parameter details such as; the parameter names, and its corresponding data type. The schema (metadata) for entities and actions is fetched by the connection at runtime from your backend. If there are any updates to the schema, such updates won't be automatically reflected in your existing connections; you must manually refresh the schema. To refresh the schema for a connection, open the **Connection details** page of the connection, and then click **Refresh connection schema**. 

## System limitations

The HL7 connector can process the following number of transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit:

  * Maximum of 39 transactions if you predominantly use the `sendMessage` action using **TCP(MLLP)**.
  * Maximum of 40 transactions if you predominantly use the `sendMessage` action using **REST(Google Cloud HealthCare API)**.



By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

The HL7 connection supports the following actions:

  * **sendMessage** Sends a message to a **TCP(MLLP)** or **REST(Google Cloud HealthCare API)**.
  * **transformHl7ToJson** Sends a valid HL7 message to a **TCP(MLLP)** or **REST(Google Cloud HealthCare API)** and get a JSON formatted message in return.
  * **transformJsonToHl7** Sends a valid JSON message to a **TCP(MLLP)** or **REST(Google Cloud HealthCare API)** and get a HL7 formatted message in return.
  * **transformAndSendHl7BatchMessage** Transforms HL7 batch messages to a list of HL7 messages.
  * **Transform HL7 to XML** Transformation from HL7 message to XML.
  * **Transform XML to HL7** Transformation from XML message to HL7.



### sendMessage action

The following tables describe the input and output parameters of the sendMessage action.

#### Input parameters of the sendMessage action

Parameter name | Required | Data type | Description  
---|---|---|---  
message | Yes | String | Message to send to the TCP(MLLP) server or REST(Google Cloud HealthCare API).  
messageContentType | Yes | String | Message content type which you can specify either as `Text` or `Bytes`. You must set the type to `Bytes` if you are sending a binary data. To send a message in a binary format, you must do the following tasks:

  * Encode the binary message as a Base64 string, and then set the `message` parameter to the encoded value.
  * Set the `messageContentType` parameter's value to `Bytes`.

  
validateMessage | No | Boolean | Flag if message validation is performed or not.  
hl7Version | No | String | Version of hl7 message (i.e. - 2.3, 2.4, etc.).  
hl7MessageType | No | String | Type of hl7 message (i.e. - ADT^A01, ADT^A02 etc.).  
  
#### Output parameters of the sendMessage action using TCP(MLLP)

Parameter name | Data type | Description  
---|---|---  
messageId | String | ID of the sent message.  
status | String | Status of the sent message.  
  
#### Output parameters of the sendMessage action using REST(Google Cloud HealthCare API)

Parameter name | Data type | Description  
---|---|---  
ack | String | Acknowledged message from the Google Cloud HealthCare API.  
status | String | Status of the sent message.  
  
### transformhl7tojson action

The following tables describe the input and output parameters of the transformhl7tojson action.

#### Input parameters of the transformhl7tojson action

Parameter name | Required | Data type | Description  
---|---|---|---  
hl7Message | Yes | String | HL7 message to be transformed to JSON.  
  
#### Output parameters of the transformhl7tojson action

Parameter name | Data type | Description  
---|---|---  
hl7Json | String | JSON transformed from HL7 message.  
  
### transformJsonToHl7 action

The following tables describe the input and output parameters of the transformJsonToHl7 action.

#### Input parameters of the transformJsonToHl7 action

Parameter name | Required | Data type | Description  
---|---|---|---  
hl7Json | Yes | String | JSON to be transformed to HL7 message.  
  
#### Output parameters of the transformJsonToHl7 action

Parameter name | Data type | Description  
---|---|---  
hl7Message | String | HL7 message transformed from JSON.  
  
### transformAndSendHl7BatchMessage action

The following tables describe the input and output parameters of the transformAndSendHl7BatchMessage action.

#### Input parameters of the Transform and send HL7 Batch Message to Healthcare System action

Parameter name | Required | Data type | Description  
---|---|---|---  
hl7BatchMessage | Yes | String | HL7 batch message to be transformed and sent.  
hl7BatchMessageDelimiter | No | String | HL7 batch message segment delimiter. Default value is `\r`.  
hl7BatchMessageContentType | Yes | String | HL7 batch message content type(Text/Bytes).  
  
#### Output parameters of the Transform and send HL7 Batch Message to Healthcare System action

Parameter name | Data type | Description  
---|---|---  
sendHl7BatchMessageResponse | String | Response from sending HL7 batch message to Healthcare System.  
  
### Transform HL7 to XML action

The following tables describe the input and output parameters of the Transform HL7 to XML action.

#### Input parameters of the Transform HL7 to XML action

Parameter name | Required | Data type | Description  
---|---|---|---  
hl7Message | Yes | String | HL7 message to be transformed to XML.  
  
#### Output parameters of the Transform HL7 to XML action

Parameter name | Data type | Description  
---|---|---  
hl7Xml | String | XML transformed from HL7 message.  
  
### Transform XML to HL7 action

The following tables describe the input and output parameters of the Transform XML to HL7 action.

#### Input parameters of the Transform XML to HL7 action

Parameter name | Required | Data type | Description  
---|---|---|---  
hl7Xml | Yes | String | XML message to be transformed to HL7.  
  
#### Output parameters of the Transform XML to HL7 action

Parameter name | Data type | Description  
---|---|---  
hl7Message | String | XML transformed from HL7 message.  
  
## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
Project ID | STRING | True | The ID of the Project where HL7 Data store is created, required only when connection is made through REST(Google Cloud Healthare API).   
Location | STRING | True | The location of your dataset and HL7v2 store, required only when connection is made through REST(Google Cloud Healthare API).   
Dataset ID | STRING | True | The ID for the dataset that holds the HL7v2 store, required only when connection is made through REST(Google Cloud Healthare API).   
HL7 Store ID | STRING | True | The ID for the HL7v2 store where you are storing the HL7v2 message, required only when connection is made through REST(Google Cloud Healthare API).   
  
## Use the HL7 connection in an integration

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
