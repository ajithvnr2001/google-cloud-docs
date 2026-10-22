---
url: https://docs.cloud.google.com/application-integration/docs/configure-servicenow-trigger/
title: ServiceNow trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:02.909537+00:00
---

# ServiceNow trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-servicenow-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ServiceNow trigger

The **ServiceNow trigger** is a [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) that lets you invoke an integration based on the custom ServiceNow events that you've defined in your ServiceNow instance [business rule](https://docs.servicenow.com/bundle/sandiego-api-reference/page/script/business-rules/concept/c_BusinessRules.html).

**Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

If you plan to create or configure a new connection for the **ServiceNow trigger** , make sure that you have the following IAM role on the project:

  * Connector Admin (`roles/connectors.admin`) 

For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




Grant the following IAM roles to the service account that you want to use for the **ServiceNow trigger** :

  * Application Integration Invoker (`roles/integrations.integrationInvoker`) 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).




## Add the ServiceNow trigger

To add a **ServiceNow trigger** to your integration, perform the following steps: 

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
  5. Click and place the **ServiceNow trigger** element in the integration editor.

To configure the **ServiceNow trigger** , you can either use an existing ServiceNow connection available in Integration Connectors, or create a new ServiceNow connection using the inline connection creation option.




## Configure ServiceNow trigger using an existing connection

You can configure the **ServiceNow trigger** using an existing ServiceNow connection in Integration Connectors. Note that the **ServiceNow trigger** is an [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers), therefore you can only use a ServiceNow connection with event subscription enabled to configure the trigger. 

For information about how to configure a **ServiceNow trigger** using a new ServiceNow connection, See Configure ServiceNow trigger using a new connection

To configure a **ServiceNow trigger** using an existing ServiceNow connection, perform the following steps:

  1. Click the **ServiceNow trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Provide the following configuration details in the **Connector Event Trigger Editor** page: 
     1. **Region:** Select the region of your ServiceNow connection.
     2. **Connection:** Select the ServiceNow connection that you want to use. 

Application Integration only displays those ServiceNow connections that are active and have an [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) enabled. 

     3. **Event subscription type:** Enter the type of event that you want to use to trigger the integration. These event types must be defined in your ServiceNow instance [business rule](https://docs.servicenow.com/bundle/sandiego-api-reference/page/script/business-rules/concept/c_BusinessRules.html). 
     4. **Service Account** : Select a service account with the required IAM roles for the ServiceNow trigger.
  4. Click **Done** to complete the trigger configuration and close the page.



## Configure ServiceNow trigger using a new connection

To configure the **ServiceNow trigger** using a new ServiceNow connection, perform the following steps:

  1. Click the **ServiceNow trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Skip the **Region** field.
  4. Click **Connection** and select the **Create Connection** option from the drop-down menu.
  5. Complete the following steps in the **Create Connection** pane: 
     1. In the **Location** step, choose the location for the new ServiceNow connection: 
        1. **Region:** Select a region from the drop-down list. 
        2. Click **Next**.
     2. In the **Connection Details** step, provide details about the new ServiceNow connection: 
        1. **Connector version:** Choose an available version of the ServiceNow connector from the drop-down list. 
        2. **Connection Name:** Enter a name for the ServiceNow connection. **Note:** Connection names must meet the following criteria: 
           * Connection names can use letters, numbers, or hyphens.
           * Letters must be lower-case.
           * Connection names must begin with a letter and end with a letter or number.
           * Connection names cannot exceed 63 characters.
        3. (Optional) **Description:** Enter a description for the connection.
        4. (Optional) **Enable Cloud Logging:** Select this checkbox to store all log data of the connection.
        5. **Service Account** : Select a service account with the required IAM roles for the ServiceNow connection.
        6. **Enable event subscription:** Select to create and enable a new event subscription for the ServiceNow connection. You can either only enable event subscriptions or also include connection [entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action). **Note:** The following additional connection configuration steps are required if you choose to enable [entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) for the connection: 
           * Destinations
           * Authentication
        7. **Include system tables:** Select to report or include system tables in the connection.
        8. (Optional) **Filter tables:** Enter the list of system tables (beginning with "`sys_`", comma separated), that you want to include.
        9. (Optional) Expand **Advanced settings** to configure the connection node settings. 

For more information about the connection node settings for ServiceNow, see the [ServiceNow connection](https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure) documentation. 

        10. (Optional) Click **\+ Add label** to add a label to the connection in the form of a key-value pair.
        11. Click **Next**.
     3. In the **Destinations** step, provide the ServiceNow instance details: 
        1. **Destination Type:** Select **Host address**.
        2. **Host:** Enter the hostname or IP address of your ServiceNow instance.
        3. Click **Next**.
     4. In the **Authentication** step, provide the authentication details for the ServiceNow instance: 
        1. **Username:** Enter the username to access the provided destination address.
        2. **Password:** Select the Secret Manager secret containing the password associated with the ServiceNow username.
        3. **Secret version:** Select a secret version.

To know more about how to configure authentication, see [Configure authentication](https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure#configure-auth).

     5. Click **Next**.
  6. In the **Event subscription details** step, provide the authentication details that will be used to validate the ServiceNow token payload: 
     1. **Authentication Token:** (Optional) Select the Secret Manager secret of your authentication token, and the corresponding secret version from the **Secret Version** drop-down.
     2. **HMAC Algorithm:** (Optional) Select the HMAC algorithm for encrypting the response payload.
     3. **HMAC Secret Key:** If you have selected a **HMAC Algorithm** , select the Secret Manager secret of the HMAC key, and the corresponding secret version from the **Secret Version** drop-down.
     4. Click **Next**.
  7. **Review** : Review the provided ServiceNow connection details.
  8. Click **Create** to complete creating a new ServiceNow connection.


* Once the ServiceNow connection is created, you must go to your ServiceNow instance and manually create a business rule. **Note:** ServiceNow doesn't auto-create a business rule. Therefore you must manually create a business rule in your ServiceNow instance to enable event subscriptions. For information on how to create a business rule, see Create a business rule. 
* **Event subscription type:** Enter the type of event that you want to use to trigger the integration. These event types must be defined in your ServiceNow instance [business rule](https://docs.servicenow.com/bundle/sandiego-api-reference/page/script/business-rules/concept/c_BusinessRules.html).
* Click **Done** and close the page.

### Create a business rule

A ServiceNow business rule is a server-side logic that executes when a database record is queried, updated, inserted, or deleted in your ServiceNow instance. Application Integration uses these business rules to identify and listen to events that trigger an integration.

For information on how to create a business rule, see [ServiceNow documentation](https://docs.servicenow.com/en-US/bundle/utah-application-development/page/script/business-rules/concept/c_BusinessRules.html#title_t_CreatingABusinessRule).

**Key Points:**

  * Use the **Events listener endpoint** value from your ServiceNow connection in Integration Connectors to define the `request.setEndpoint` URL in your business rule.
  * Use `eventType` as the _key_ to define custom event types _values_ in `request.setRequestBody`.



The following image shows a sample ServiceNow business rule with the `update_ticket` event type:

![image showing sample ServiceNow business rule](https://docs.cloud.google.com/static/application-integration/images/servicenow_rule.png)![image showing sample ServiceNow business rule](https://docs.cloud.google.com/static/application-integration/images/servicenow_rule.png)

## Trigger output

The **ServiceNow trigger** takes a couple of minutes to complete the event subscription configuration. You can view the status of your event subscription in the trigger configuration pane under **Event Subscription details**.

The **ServiceNow trigger** indicates the status of an event subscription using the following states:

  * restart_alt `Creating`: Indicates that the trigger is subscribing to the event subscription. 
  * check_circle `Active`: Indicates that the trigger is successfully subscribed to an event subscription.
  * error `Error`: Indicates that the there is an issue with the configured event subscription. 



In addition to the event subscription status, the **Event Subscription details** section also displays other details such as connection region, connection name, event subscription name, and more.

The following image shows a sample layout of the ServiceNow trigger configuration pane:

![image showing ServiceNow trigger configuration pane](https://docs.cloud.google.com/static/application-integration/images/servicenow_trigger_1.png)![image showing ServiceNow trigger configuration pane](https://docs.cloud.google.com/static/application-integration/images/servicenow_trigger_1.png)

### Trigger output variable

For each event, the **ServiceNow trigger** generates a `ConnectorEventPayload` output variable which you can use in your downstream tasks. The output variable is in JSON format containing the output ServiceNow payload schema. 

### View event subscriptions

To view and manage all the event subscriptions associated with a connection in Integration Connectors, do the following:

  1. Go to **Integration Connectors > Connections** page. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

  2. Click the connection for which you want to view the subscriptions.
  3. Click the **Event subscriptions** tab. 

This displays all the event subscriptions for the connection.




## Edit ServiceNow trigger

You can edit a **ServiceNow trigger** to change or update the connection configuration and event subscription details.

**Important:** When you edit or modify a ServiceNow trigger, you can either retain the previously configured event subscription that is attached to the trigger, or you can delete it. Deleting an event subscription will affect all the published integrations using that event subscription. 

To edit a ServiceNow trigger, perform the following steps:

  1. Click the **ServiceNow trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure ServiceNow trigger**.
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
