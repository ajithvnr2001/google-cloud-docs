---
url: https://docs.cloud.google.com/application-integration/docs/configure-hubspot-trigger/
title: HubSpot trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:25.836777+00:00
---

# HubSpot trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-hubspot-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HubSpot trigger

**Preview — HubSpot trigger**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **HubSpot trigger** is a [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) that lets you invoke an integration based on the custom HubSpot events that you've defined in your HubSpot instance.

**Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

If you plan to create or configure a new connection for the **HubSpot trigger** , make sure that you have the following Identity and Access Management (IAM) role on the project:

  * Connector Admin (`roles/connectors.admin`) 

For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




Grant the following IAM roles to the service account that you want to use for the **HubSpot trigger** :

  * Application Integration Invoker (`roles/integrations.integrationInvoker`) 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).




## Supported event types

With webhook subscriptions you can select which events your app would receive. The following subscription types are supported:

  * `deal.creation`
  * `deal.propertyChange`
  * `deal.deletion`
  * `contact.creation`
  * `contact.propertyChange`
  * `contact.deletion`



## Add the HubSpot trigger

To add a **HubSpot trigger** to your integration, follow these steps: 

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
  5. Click and place the **HubSpot trigger** element in the integration editor.

To configure the **HubSpot trigger** , you can either use an existing HubSpot connection available in Integration Connectors, or create a new HubSpot connection using the inline connection creation option.




## Configure HubSpot trigger using an existing connection

You can configure the **HubSpot trigger** using an existing HubSpot connection in Integration Connectors. The **HubSpot trigger** is an [connector event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers), therefore you can only use a HubSpot connection with event subscription enabled to configure the trigger. 

For information about how to configure a **HubSpot trigger** using a new HubSpot connection, see Configure HubSpot trigger using a new connection

To configure a **HubSpot trigger** using an existing HubSpot connection, follow these steps:

  1. Click the **HubSpot trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Provide the following configuration details in the **Connector Event Trigger Editor** page: 
     1. **Region:** Select the region of your HubSpot connection.
     2. **Connection:** Select the HubSpot connection that you want to use. 

Application Integration only displays those HubSpot connections that are active and have an [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) enabled. 

     3. **Event type:** Select the type of event that you want to use to trigger the integration. For a list of supported event types, see supported event types.
     4. **Service Account** : Select a service account with the required IAM roles for the HubSpot trigger.
  4. Click **Done** to complete the trigger configuration and close the page.



## Configure HubSpot trigger using a new connection

To configure the **HubSpot trigger** using a new HubSpot connection, follow these steps:

  1. Click the **HubSpot trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Skip the **Region** field.
  4. Click **Connection** and select the **Create Connection** option from the drop-down menu.
  5. Complete the following steps in the **Create Connection** pane: 
     1. In the **Location** step, choose the location for the new HubSpot connection: 
        1. **Region:** Select a region from the drop-down list. 
        2. Click **Next**.
     2. In the **Connection Details** section, complete the following: 
        1. **Connector** : Select **HubSpot** from the drop down list of available Connectors.
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
        6. To use the connection for event subscriptions, select **Enable event subscription**. Selecting this, displays the following options: 
           * **Enable event subscription with entity and actions** : Select this option to use the connection for both event subscription and connector operations (entities and actions).
           * **Enable only event subscription** : Select this option to use the connection only for event subscription. If you select this option, click **Next** , and then configure event subscription.
        7. **Schema** : Specify the HubSpot API version to use. HubSpotV4 is the new API. 
        8. **BrowsableSchemas** : This property restricts the schemas reported to a subset of the available schemas. For example, BrowsableSchemas=SchemaA,SchemaB,SchemaC. 
        9. **Contacts Properties** : Enter the comma separated field names of the `Contacts` entity that you want to select from the `List` entity operation. For example, `fieldA, fieldB, fieldC`
        10. **Companies Properties** : Enter the comma separated field names of the `Companies` entity that you want to select from the `List` entity operation. For example, `fieldA, fieldB, fieldC`
        11. **Deals Properties** : Enter the comma separated field names of the `Deals` entity that you want to select from the `List` entity operation. For example, `fieldA, fieldB, fieldC`
        12. **Use proxy** : Select this checkbox to configure a proxy server for the connection. 
        13. **Proxy Auth Scheme** : The authentication type to use to authenticate to the ProxyServer proxy. 
        14. **Proxy User** : A user name to be used to authenticate to the ProxyServer proxy. 
        15. **Proxy Password** : A password to be used to authenticate to the ProxyServer proxy. 
        16. **Proxy SSL Type** : The SSL type to use when connecting to the ProxyServer proxy. 
        17. Optionally, configure the **Connection node settings** : 

           * **Minimum number of nodes** : Enter the minimum number of connection nodes.
           * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
        18. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
        19. Click **Next**.
     3. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
        1. **Destination Type** : You can specify the destination details either as a host address or a service attachment. Select any of the following destination types: 
           * **Host address** : If you want to specify the hostname or IP address of the destination.
           * **Service attachment** : If you want to specify the private endpoint for your internal IP addresses. The service attachment, lets you hide your internal IP addresses from the external network. You can create a service attachment in Google Cloud, by using the Private Service Connect feature. For information on configuring a Private Service Connect, see [Publish managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

Based on your selection of destination type, enter the host address or the service attachment name.

To enter additional destinations, click **+Add destination**.

        2. Click **Next**.
     4. In the **Authentication** section, enter the authentication details. 
        1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the HubSpot connection:

           * **Private App Access Token:** Select the Secret Manager Secret containing the private app access token. 

Private apps allow you to use HubSpot's APIs to access specific data from your HubSpot account. You can authorize what each private app can request or change in your account, which will generate an access token that's unique to your private app. In your private app, ensure you have provided the read permission at least to the following scopes:

             * crm.schemas.line_items.read
             * crm.schemas.quotes.read
             * crm.schemas.deals.read
             * crm.schemas.companies.read
             * crm.schemas.custom.read
             * crm.schemas.contacts.read

For more information, see [Private apps](https://developers.hubspot.com/docs/api/private-apps).

        2. Click **Next**.
     5. If you have enabled event subscription, the **Event Subscription Details** section appears on the connection creation page. In the **Event subscription details** step, provide the authentication details that will be used to validate the HubSpot token payload: 
        1. **Client Secret:** (Optional) Select the Secret Manager secret of your private app's client secret, and the corresponding secret version from the **Secret Version** drop-down.

For more information, see [Private apps](https://developers.hubspot.com/docs/api/private-apps).

        2. Select **Enable private connectivity** for secured connectivity between your backend application and your connection. If you select this option, you must perform additional configuration steps after creating the connection. For more information, see [Private connectivity for event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#psc-eventing). 
        3. Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
           1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
           2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.
        4. Click **Next**.
     6. **Review** : Review your connection and authentication details.
     7. Click **Create**.



### Create and edit webhook subscriptions

To complete the event subscription configuration, you must register the webhook URL with your HubSpot application. Therefore, after the connection creation is successful, perform the following additional steps:

  1. Go the connection details page of the newly created connection, and copy the webhook URL for event subscription. The webhook URL is required when you create a webhook subscription in the next step. 

The following image shows the **Events listener endpoint** field in the HubSpot connection details page:

![image showing HubSpot connection details page](https://docs.cloud.google.com/static/application-integration/images/hubspot-webhook-url.png)![image showing HubSpot connection details page](https://docs.cloud.google.com/static/application-integration/images/hubspot-webhook-url.png)
  2. Follow the steps to [create and edit webhook subscriptions](https://developers.hubspot.com/docs/api/create-and-edit-webhook-subscriptions-in-private-apps) in HubSpot.



## Trigger output

The **HubSpot trigger** takes a couple of minutes to complete the event subscription configuration. You can view the status of your event subscription in the trigger configuration pane under **Event Subscription details**.

The **HubSpot trigger** indicates the status of an event subscription using the following states:

  * restart_alt `Creating`: Indicates that the trigger is subscribing to the event subscription. 
  * check_circle `Active`: Indicates that the trigger is successfully subscribed to an event subscription.
  * error `Error`: Indicates that the there is an issue with the configured event subscription. 



In addition to the event subscription status, the **Event Subscription details** section also displays other details such as connection region, connection name, event subscription name, and more.

The following image shows a sample layout of the HubSpot trigger configuration pane:

![image showing HubSpot trigger configuration pane](https://docs.cloud.google.com/static/application-integration/images/hubspot_trigger.png)![image showing HubSpot trigger configuration pane](https://docs.cloud.google.com/static/application-integration/images/hubspot_trigger.png)

### Trigger output variable

For each event, the **HubSpot trigger** generates a `ConnectorEventPayload` output variable which you can use in your downstream tasks. The output variable is in JSON format containing the output HubSpot payload schema. 

### View event subscriptions

To view and manage all the event subscriptions associated with a connection in Integration Connectors, do the following:

  1. Go to **Integration Connectors > Connections** page. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

  2. Click the connection for which you want to view the subscriptions.
  3. Click the **Event subscriptions** tab. 

This displays all the event subscriptions for the connection.




## Edit HubSpot trigger

You can edit a **HubSpot trigger** to change or update the connection configuration and event subscription details.

**Important:** When you edit or modify a HubSpot trigger, you can either retain the previously configured event subscription that is attached to the trigger, or you can delete it. Deleting an event subscription will affect all the published integrations using that event subscription. 

To edit a HubSpot trigger, follow these steps:

  1. Click the **HubSpot trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure HubSpot trigger**.
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
