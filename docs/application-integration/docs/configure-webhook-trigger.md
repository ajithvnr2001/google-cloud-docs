---
url: https://docs.cloud.google.com/application-integration/docs/configure-webhook-trigger/
title: Webhook trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:42.104817+00:00
---

# Webhook trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-webhook-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Webhook trigger

**Preview — Webhook trigger**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Webhook trigger** is a [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#connector-event-triggers-preview) that lets you invoke an integration based on any events from the backend that supports webhooks. The Webhook trigger receives events from third-party SaaS-based applications that support webhook eventing capability. This trigger supports multiple authentication types for your event listener and accepts only JSON payloads.

**Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

If you plan to create or configure a new connection for the **Webhook trigger** , make sure that you have the following Identity and Access Management (IAM) role on the project:

  * Connector Admin (`roles/connectors.admin`) 

For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




Grant the following IAM roles to the service account that you want to use for the **Webhook trigger** :

  * Application Integration Invoker (`roles/integrations.integrationInvoker`) 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).




## Add the Webhook trigger

To add a **Webhook trigger** to your integration, perform the following steps: 

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
  5. Click and place the **Webhook trigger** element in the integration editor.

To configure the **Webhook trigger** , you can either use an existing Webhook connection available in Integration Connectors, or create a new Webhook connection using the inline connection creation option.




## Configure Webhook trigger using an existing connection

You can configure the **Webhook trigger** using an existing Webhook connection in Integration Connectors. Note that the **Webhook trigger** is an [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers), therefore you can only use a Webhook connection with event subscription enabled to configure the trigger. 

For information about how to configure a **Webhook trigger** using a new Webhook connection, see Configure Webhook trigger using a new connection

To configure a **Webhook trigger** using an existing Webhook connection, perform the following steps:

  1. Click the **Webhook trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Provide the following configuration details in the **Connector Event Trigger Editor** page: 
     1. **Region:** Select the region of your Webhook connection.
     2. **Connection:** Select the Webhook connection that you want to use. 

Application Integration only displays those Webhook connections that are active and have an [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) enabled. 

     3. **Event subscription type:** Enter the type of event that you want to use to trigger the integration.
     4. **Service Account** : Select a service account with the required IAM roles for the Webhook trigger.
  4. Click **Done** to complete the trigger configuration and close the page.

For more information, see the [Webhook connection](https://docs.cloud.google.com/integration-connectors/docs/connectors/webhook/configure) documentation. 

## Configure Webhook trigger using a new connection

To configure the **Webhook trigger** using a new Webhook connection, perform the following steps:

  1. Click the **Webhook trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Skip the **Region** field.
  4. Click **Connection** and select the **Create Connection** option from the menu.
  5. Complete the following steps in the **Create Connection** pane: 
     1. In the **Location** section, choose the location for the connection. 
        1. **Region** : Select a location from the list. 

Supported regions for connectors include: 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

        2. Click **Next**.
     2. In the **Connection Details** section, complete the following: 
        1. **Connector** : Select **Webhook** from the drop down list of available Connectors.
        2. **Connector version** : Select the Connector version from the drop down list of available versions. 
        3. **Connection Name** : Enter a name for the Connection instance. 

Connection names must meet the following criteria: 

           * Connection names can use letters, numbers, or hyphens.
           * Letters must be lower-case.
           * Connection names must begin with a letter and end with a letter or number.
           * Connection names cannot exceed 49 characters.
           * For connectors that [support event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#enable-event-subscriptions-in-connections), the connection names cannot begin with the "goog" prefix. 
        4. **Description** : Optionally, enter a description for the connection instance.
        5. **Service Account** : Select a service account that has the required roles.
        6. **Event Subscription** : Event subscription will be enabled by default and is mandatory for webhook connector. **Note:** The `Enable event subscription, entity and actions` option isn't supported for this connection.
        7. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
        8. Click **Next**.
     3. In the **Event Subscription Details** section, complete the following: 
        1. **Listener Authentication** : Select an authentication type for event listener and enter the relevant details. 

The following authentication types are supported by the webhook listener:

           * No Authentication
           * [Google Authentication](https://docs.cloud.google.com/iam/docs/workload-identities): Ensure that the service account has [roles/connectors.listener](https://cloud.google.com/iam/docs/roles-permissions/connectors) role whose access token is used for authentication.
           * API Key Authentication
           * [Basic Authentication](https://www.rfc-editor.org/rfc/rfc7617)
        2. **Event Type Field Location** : Mandatory field which denotes the location (Header, Query Param or Request Body) where event type associated with the incoming event request will be present.
        3. **Event Type Field Name** : Mandatory field in the configured location identifies the type of event associated with the incoming event request.
    
    {
    "event_type": "user.created",
    ...
    // other request fields
    ...
    }

In the example above, the **event_type** field in **request body** signifies that the request pertains to a "user.created" event. 
        4. Select **Enable private connectivity** for secured connectivity between your backend application and your connection. If you select this option, you must perform additional configuration steps after creating the connection. For more information, see [Private connectivity for event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#psc-eventing). 
        5. Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
           1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
           2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.
        6. Click **Next**.
     4. **Review** : Review your connection and listener authentication details.
     5. Click **Create**.



## Trigger output

The **Webhook trigger** takes a couple of minutes to complete the event subscription configuration. You can view the status of your event subscription in the trigger configuration pane under **Event Subscription details**.

The **Webhook trigger** indicates the status of an event subscription using the following states:

  * restart_alt `Creating`: Indicates that the trigger is subscribing to the event subscription. 
  * check_circle `Active`: Indicates that the trigger is successfully subscribed to an event subscription.
  * error `Error`: Indicates that the there is an issue with the configured event subscription. 



In addition to the event subscription status, the **Event Subscription details** section also displays other details such as connection region, connection name, event subscription name, and more.

### Trigger output variable

For each event, the **Webhook trigger** generates a `ConnectorEventPayload` output variable which you can use in your downstream tasks. The output variable is in JSON format containing the output Webhook payload schema. The Webhook trigger accepts only JSON payloads. 

### View event subscriptions

To view and manage all the event subscriptions associated with a connection in Integration Connectors, do the following:

  1. Go to **Integration Connectors > Connections** page. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

  2. Click the connection for which you want to view the subscriptions.
  3. Click the **Event subscriptions** tab. 

This displays all the event subscriptions for the connection.




## Edit Webhook trigger

You can edit a **Webhook trigger** to change or update the connection configuration and event subscription details.

**Important:** When you edit or modify a Webhook trigger, you can either retain the previously configured event subscription that is attached to the trigger, or you can delete it. Deleting an event subscription will affect all the published integrations using that event subscription. 

To edit a Webhook trigger, perform the following steps:

  1. Click the **Webhook trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure Webhook trigger**.
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
