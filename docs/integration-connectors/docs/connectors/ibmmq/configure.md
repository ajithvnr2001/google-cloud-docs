---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/ibmmq/configure/
title: IBM MQ \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:51.488631+00:00
---

# IBM MQ  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/ibmmq/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IBM MQ

The IBM MQ connector provides connectivity to IBM MQ.

## Before you begin

Before using the IBM MQ connector, do the following tasks:

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

**Note:** The IBM MQ connector supports JMS (Java Message Service) protocol. Other protocols, such as MQTT and AMQP, are not supported.


## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **IBM MQ** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
        * For connectors that [support event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#enable-event-subscriptions-in-connections), the connection names cannot begin with the "goog" prefix. 
     4. Optionally, enter a **Description** for the connection instance.
     5. **Service Account** : Select a service account that has the required roles.
     6. To use the connection for event subscriptions, select **Enable event subscription**. Selecting this option, enables the event subscription with actions. **Note:** The `Enable only event subscription` option isn't supported for this connection.
     7. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. **Default Queue Name** : The name of the default queue, may be overridden when executing action. 
     9. **Queue Manager Name** : The name of the Queue Manager to connect to. 
     10. **Channel Name** : The channel to connect to the Queue Manager on. 
     11. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     12. Optionally, if you want to use SSL, select **Enable SSL**. This displays the SSL configuration details. 
        1. Select a trust store type. It can be either **Public** , **Private** , or **Insecure Connection**. 
        2. Select the certificates as displayed based on your trust store selection.
        3. If you are using mTLS, select the key store certificates in the **Key Store** section.
        4. Optionally, select the TLS version.
        5. Enter the supported cipher suite. Enter multiple cipher suites, as comma separated values. For more information, see Supported cipher suites. 
**Note:**
        * All your certificates must be X.509 certificates and must be in PEM (Privacy Enhanced Mail) format.
        * You can't directly select a certificate when configuring SSL. You must store all your certificates and private keys as a Secret Manager Secret, and then select the required secret during SSL configuration.
     13. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

**Note:** This connector supports only one destination.
  6. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the IBM MQ connection:

     * Anonymous 
     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **Next**.


* In the **Event Subscription Details** section, configure the event related details. 

  * Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
    1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
    2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Anonymous**

If you want to use anonymous login, select **Not Available**.



  * **Username and password**
    * **Username** : The IBM MQ username to use for the connection.
    * **Password** : Secret Manager Secret containing the password associated with the IBM MQ username.



### Supported cipher suites

TLS version | Supported cipher suites  
---|---  
1.2 | 

  * TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
  * TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
  * TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
  * TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
  * TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  * TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  * TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
  * TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
  * TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
  * TLS_DHE_RSA_WITH_AES_128_CBC_SHA
  * TLS_DHE_RSA_WITH_AES_256_CBC_SHA
  * TLS_DHE_RSA_WITH_AES_128_CBC_SHA256
  * TLS_DHE_RSA_WITH_AES_256_CBC_SHA256

  
1.3 | 

  * TLS_AES_256_GCM_SHA384
  * TLS_CHACHA20_POLY1305_SHA256
  * TLS_AES_128_GCM_SHA256

  
  
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

The IBM MQ connector can process the following number of transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit:

  * Maximum of 7 transactions if you predominantly use the `sendMessage` action.
  * 1 transaction if you predominantly use the `requestReply` action.



By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

The IBM MQ connection supports the following actions:

  * **sendMessage** Sends a message to a queue.
  * **requestReply** : Sends a message to a queue and also specifies the response queue where the replier should write the response.



### sendMessage action

The following tables describe the input and output parameters of the sendMessage action.

#### Input parameters of the sendMessage action

Parameter name | Required | Data type | Description  
---|---|---|---  
message | Yes | String | Message to be sent to the IBM MQ queue. Currently, the maximum message size supported is 10 MB.  
queueName | No | String | Name of the IBM MQ queue. If you don't specify a queue name, the default queue name specified during creating the connection is used.  
messageContentType | Yes | String | Message content type which you can specify either as `Text` or `Bytes`. You must set the type to `Bytes` if you are sending a binary data. To send a message in a binary format, you must do the following tasks:

  * Encode the binary message as a Base64 string, and then set the `message` parameter to the encoded value.
  * Set the `messageContentType` parameter's value to `Bytes`.

  
messageType | Yes | String | Message type which you can specify either as `Datagram` or `Reply`.  
topicName | No | String | Name of the IBM MQ topic. If you don't specify a topic name, the default queue name specified during creating the connection is used.  
  
#### Output parameters of the sendMessage action

Parameter name | Data type | Description  
---|---|---  
messageId | String | ID of the sent message.  
  
### requestReply action

The following tables describe the input and output parameters of the requestReply action.

#### Input parameters of the requestReply action

Parameter name | Required | Data type | Description  
---|---|---|---  
message | Yes | String | Message to be sent to the IBM MQ queue. The maximum message size supported is 10 MB.  
queueName | No | String | Name of the IBM MQ queue. If you don't specify a queue name, the default queue name specified during creating the connection is used.  
messageContentType | Yes | String | Message content type which you can specify either as `Text` or `Bytes`. You must set the type to `Bytes` if you are sending a binary data. To send a message in a binary format, you must do the following tasks:

  * Encode the binary message as a Base64 string, and then set the `message` parameter to the encoded value.
  * Set the `messageContentType` parameter's value to `Bytes`.

  
replyToQueue | Yes | String | Queue on which the replier should write the response.  
replyTimeout | Yes | String | Time (in milliseconds) till which the connector waits for the response in the response queue. The maximum supported value is 180000 milliseconds (3 minutes).   
If the response queue receives a message after the timeout period, then that message isn't processed by the connector. However, you can view the timed out message details in your integration's [execution logs](https://docs.cloud.google.com/application-integration/docs/viewing-logs). **Note:** Setting a higher timeout value might impact the connector performance.  
  
#### Output parameters of the requestReply action

Parameter name | Data type | Description  
---|---|---  
replyMessage | String | Response message from the replier.  
  
## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
default_queue_name | STRING | False | The name of the default queue, may be overridden when executing action.   
default_topic_name | STRING | False | The name of the default topic, may be overridden when executing action.   
queue_manager_name | STRING | True | The name of the Queue Manager to connect to.   
channel_name | STRING | True | The channel to connect to the Queue Manager on.   
  
## Use the IBM MQ connection in an integration

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
