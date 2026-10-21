---
url: https://docs.cloud.google.com/application-integration/docs/configure-solace-trigger/
title: Solace trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:39.874717+00:00
---

# Solace trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-solace-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Solace trigger

**Preview — Solace trigger**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Solace trigger** is a [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) that lets you invoke an integration based on the Solace events that you've subscribed to in your Solace connection.

**Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

If you plan to create or configure a new connection for the **Solace trigger** , make sure that you have the following IAM role on the project:

  * Connector Admin (`roles/connectors.admin`) 

For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




Grant the following IAM roles to the service account that you want to use for the **Solace trigger** :

  * Application Integration Invoker (`roles/integrations.integrationInvoker`) 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).


**Note:** The Solace trigger supports JMS (Java Message Service) protocol. Other protocols, such as MQTT and AMQP, are not supported.

## Add the Solace trigger

To add a **Solace trigger** to your integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**

The **Integrations List** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**.

The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Triggers** to view the list of available triggers. 
  5. Click and place the **Solace trigger** element in the integration editor.

To configure the **Solace trigger** , you can either use an existing Solace connection available in Integration Connectors, or create a new Solace connection using the inline connection creation option.




## Configure Solace trigger using an existing connection

You can configure the **Solace trigger** using an existing Solace connection in Integration Connectors. Note that the **Solace trigger** is an [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers), therefore you can only use a Solace connection with event subscription enabled to configure the trigger. 

For information about how to configure a **Solace trigger** using a new Solace connection, See Configure Solace trigger using a new connection

To configure a **Solace trigger** using an existing Solace connection, perform the following steps:

  1. Click the **Solace trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Provide the following configuration details in the **Connector Event Trigger Editor** page: 
     1. **Region:** Select the region of your Solace connection.
     2. **Connection:** Select the Solace connection that you want to use. 

Application Integration only displays those Solace connections that are active and have an event subscription enabled. 

     3. Select `Queue` or Topic as the `JMS Source Type`. 
        * If you select `Queue`, provide the Solace queue name in the `JMS Source Name` column.
        * If you select `Topic`, provide the Solace topic name in the JMS Source Name column.
     4. **Service Account** : Select a service account with the required IAM roles for the Solace trigger.
  4. Click **Done** to complete the trigger configuration and close the page.



## Configure Solace trigger using a new connection

To configure the **Solace trigger** using a new Solace connection, perform the following steps:

  1. Click the **Solace trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Skip the **Region** field.
  4. Click **Connection** and select the **Create Connection** option from the drop-down menu.
  5. Complete the following steps in the **Create Connection** pane: 
     1. In the **Location** step, choose the location for the new Solace connection: 
        1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

        2. Click **Next**.
     2. In the **Connection Details** section, complete the following: 
        1. **Connector** : Select **Solace** from the drop down list of available Connectors.
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
        7. **Message VPN** : The Solace Pub/Sub+ message router Message VPN that you want to connect to. A connection is specific to a Message VPN. If you have many message VPN, you must create a separate connection for each message VPN.
        8. **Default Queue Name** : The name of the default queue, may be overridden when executing action. 
        9. **Default Topic Name** : The name of the topic to connect to. 
        10. (Optional) To use SSL, select **Enable SSL** and specify the SSL configuration details.
           1. Select a trust store type. You can specify **Public** , **Private** , or **Insecure Connection**. 
           2. Select the certificates based on your trust store selection. For example, if you select **Private** , specify a custom trust store.
           3. If you are using mTLS, select the key store certificates in the **Key Store** section.
           4. Optionally, select the TLS version.
           5. Enter the supported cipher suite. Enter multiple cipher suites, as comma separated values. For more information, see Supported cipher suites. 
**Note:**
              * All your certificates must be X.509 certificates and must be in PEM (Privacy Enhanced Mail) format.
              * You can't directly select a certificate when configuring SSL. You must store all your certificates and private keys as a Secret Manager Secret, and then select the required secret during SSL configuration.
        11. (Optional) Configure the **Connection node settings**.
           * **Minimum number of nodes** : Enter the minimum number of connection nodes.
           * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
        12. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
        13. Click **Next**.
     3. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
        1. **Destination Type** : Select a **Destination Type**. 
           * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
           * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

**Note:** This connector supports only one destination.
     4. Click **Next**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Solace connection:

        * Anonymous 
        * Username and password 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  7. In the **Event Subscription Details** section, configure the event related details. 
     * Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
       1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
       2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.
  8. **Review** : Review your connection and authentication details.
  9. Click **Create**.



## Trigger output

The **Solace trigger** takes a couple of minutes to complete the event subscription configuration. You can view the status of your event subscription in the trigger configuration pane under **Event Subscription details**.

The **Solace trigger** indicates the status of an event subscription using the following states:

  * restart_alt `Creating`: Indicates that the trigger is subscribing to the event subscription. 
  * check_circle `Active`: Indicates that the trigger is successfully subscribed to an event subscription.
  * error `Error`: Indicates that the there is an issue with the configured event subscription. 



In addition to the event subscription status, the **Event Subscription details** section also displays other details such as connection region, connection name, and event subscription name.

### Trigger output variable

For each event, the **Solace trigger** generates a `ConnectorEventPayload` output variable (in JSON format) which you can use in your downstream tasks. The output variable will have the payload from your Solace event. For example: 
    
    
    {
    "message": "Hello world",
    "messageContentType": "Text"
    }

### View event subscriptions

To view and manage all the event subscriptions associated with a connection in Integration Connectors, do the following:

  1. Go to **Integration Connectors > Connections** page. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

  2. Click the connection for which you want to view the subscriptions.
  3. Click the **Event subscriptions** tab. 

This displays all the event subscriptions for the connection.




## Edit Solace trigger

You can edit a **Solace trigger** to change or update the connection configuration and event subscription details.

**Important:** When you edit or modify a Solace trigger, you can either retain the previously configured event subscription that is attached to the trigger, or you can delete it. Deleting an event subscription will affect all the published integrations using that event subscription. 

To edit a Solace trigger, perform the following steps:

  1. Click the **Solace trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure Solace trigger**.
  3. Do the following in the **Connector Event Trigger Editor** page: 
     1. To retain the previously configured event subscription, click **Retain** , else click **Delete**. **Warning:** Deleting an event subscription will affect all the published integrations using the event subscription. This task cannot be undone.
     2. Update the connection configuration and event subscription details as desired.
     3. Click **Done**.

You can view the updated connection and event subscription details in the trigger configuration pane under **Event Subscription details**.




## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
