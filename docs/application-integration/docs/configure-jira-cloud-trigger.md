---
url: https://docs.cloud.google.com/application-integration/docs/configure-jira-cloud-trigger/
title: Jira Cloud trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:11.661581+00:00
---

# Jira Cloud trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-jira-cloud-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Jira Cloud trigger

The **Jira Cloud trigger** is a [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) that lets you invoke an integration based on the Jira Cloud events that you've subscribed to in your Jira Cloud connection.

**Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

If you plan to create or configure a new connection for the **Jira Cloud trigger** , make sure that you have the following IAM role on the project:

  * Connector Admin (`roles/connectors.admin`) 

For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




Grant the following IAM roles to the service account that you want to use for the **Jira Cloud trigger** :

  * Application Integration Invoker (`roles/integrations.integrationInvoker`) 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).




## Add the Jira Cloud trigger

To add a **Jira Cloud trigger** to your integration, perform the following steps: 

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
  5. Click and place the **Jira Cloud trigger** element in the integration editor.

To configure the **Jira Cloud trigger** , you can either use an existing Jira Cloud connection available in Integration Connectors, or create a new Jira Cloud connection using the inline connection creation option.




## Configure Jira Cloud trigger using an existing connection

You can configure the **Jira Cloud trigger** using an existing Jira Cloud connection in Integration Connectors. Note that the **Jira Cloud trigger** is an [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers), therefore you can only use a Jira Cloud connection with event subscription enabled to configure the trigger. 

For information about how to configure a **Jira Cloud trigger** using a new Jira Cloud connection, See Configure Jira Cloud trigger using a new connection

To configure a **Jira Cloud trigger** using an existing Jira Cloud connection, perform the following steps:

  1. Click the **Jira Cloud trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Provide the following configuration details in the **Connector Event Trigger Editor** page: 
     1. **Region:** Select the region of your Jira Cloud connection.
     2. **Connection:** Select the Jira Cloud connection that you want to use. 

Application Integration only displays those Jira Cloud connections that are active and have an [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) enabled. 

     3. **Event subscription type:** Select the type of event subscription that triggers the integration. For information about the supported event subscription types for this trigger, see Supported event subscription types.
     4. **Service Account** : Select a service account with the required IAM roles for the Jira Cloud trigger.
  4. Click **Done** to complete the trigger configuration and close the page.



## Configure Jira Cloud trigger using a new connection

To configure the **Jira Cloud trigger** using a new Jira Cloud connection, perform the following steps:

  1. Click the **Jira Cloud trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Skip the **Region** field.
  4. Click **Connection** and select the **Create Connection** option from the drop-down menu.
  5. Complete the following steps in the **Create Connection** pane: 
     1. In the **Location** step, choose the location for the new Jira Cloud connection: 
        1. **Region:** Select a region from the drop-down list. 
        2. Click **Next**.
     2. In the **Connection Details** step, provide details about the new Jira Cloud connection: 
        1. **Connector version:** Choose an available version of the Jira Cloud connector from the drop-down list. 
        2. **Connection Name:** Enter a name for the Jira Cloud connection. **Note:** Connection names must meet the following criteria: 
           * Connection names can use letters, numbers, or hyphens.
           * Letters must be lower-case.
           * Connection names must begin with a letter and end with a letter or number.
           * Connection names cannot exceed 63 characters.
        3. (Optional) **Description:** Enter a description for the connection.
        4. (Optional) **Enable Cloud Logging:** Select this checkbox to store all log data of the connection.
        5. **Service Account** : Select a service account with the required IAM roles for the Jira Cloud connection.
        6. **Enable event subscription:** Select to create and enable a new event subscription for the Jira Cloud connection. You can either only enable event subscriptions or also include connection [entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action). **Note:** The following additional connection configuration steps are required if you choose to enable [entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) for the connection: 
           * Destinations
           * Authentication
        7. (Optional) Expand **Advanced settings** to configure the connection node settings. 

For more information about the connection node settings for Jira Cloud, see the [Jira Cloud connection](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure) documentation. 

        8. (Optional) Click **\+ Add label** to add a label to the connection in the form of a key-value pair.
        9. Click **Next**.
     3. In the **Destinations** step, provide the Jira Cloud account details: 
        1. **Destination Type:** Select **Host address**.
        2. **Host:** Enter the hostname or IP address of your Jira Cloud account.
        3. Click **Next**.
     4. In the **Authentication** step, provide the authentication details for the Jira Cloud account: 
        1. **Username:** Enter the username to access the provided destination address.
        2. **API token:** Select the Secret Manager secret containing the API Token associated with the Jira Cloud username.
        3. **Secret version:** Select a secret version.

To know more about how to configure authentication, see [Configure authentication](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure#configure-auth).

     5. Click **Next**.
  6. In the **Event subscription details** step, provide details of the Jira Cloud account where the event subscriptions will be created. 
     1. **Destination Type:** Select **Host address**.
     2. **Host:** Enter the registration URL of your Jira Cloud account. Event subscriptions will be created for this URL.
     3. **Username:** Enter the username to access the provided registration URL.
     4. **API token:** Select the Secret Manager secret containing the API token associated with the username.
     5. **Secret version:** Select a secret version.
     6. Click **Next**.
  7. **Review** : Review the provided Jira Cloud connection details.
  8. Click **Create** to complete creating a new Jira Cloud connection.


* **Event subscription type:** Select the type of event subscription that triggers the integration. For information about the supported event subscription types for this trigger, see Supported event subscription types.
* Click **Done** and close the page.

## Trigger output

The **Jira Cloud trigger** takes a couple of minutes to complete the event subscription configuration. You can view the status of your event subscription in the trigger configuration pane under **Event Subscription details**.

The **Jira Cloud trigger** indicates the status of an event subscription using the following states:

  * restart_alt `Creating`: Indicates that the trigger is subscribing to the event subscription. 
  * check_circle `Active`: Indicates that the trigger is successfully subscribed to an event subscription.
  * error `Error`: Indicates that the there is an issue with the configured event subscription. 



In addition to the event subscription status, the **Event Subscription details** section also displays other details such as connection region, connection name, event subscription name, and more.

The following image shows a sample layout of the Jira Cloud trigger configuration pane:

![image showing Jira Cloud trigger configuration pane](https://docs.cloud.google.com/static/application-integration/images/jiracloud_trigger_1.png)![image showing Jira Cloud trigger configuration pane](https://docs.cloud.google.com/static/application-integration/images/jiracloud_trigger_1.png)

### Trigger output variable

For each event, the **Jira Cloud trigger** generates a `ConnectorEventPayload` output variable which you can use in your downstream tasks. The output variable is in JSON format containing the output Jira Cloud payload schema. 

### View event subscriptions

To view and manage all the event subscriptions associated with a connection in Integration Connectors, do the following:

  1. Go to **Integration Connectors > Connections** page. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

  2. Click the connection for which you want to view the subscriptions.
  3. Click the **Event subscriptions** tab. 

This displays all the event subscriptions for the connection.




## Edit Jira Cloud trigger

You can edit a **Jira Cloud trigger** to change or update the connection configuration and event subscription details.

**Important:** When you edit or modify a Jira Cloud trigger, you can either retain the previously configured event subscription that is attached to the trigger, or you can delete it. Deleting an event subscription will affect all the published integrations using that event subscription. 

To edit a Jira Cloud trigger, perform the following steps:

  1. Click the **Jira Cloud trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure Jira Cloud trigger**.
  3. Do the following in the **Connector Event Trigger Editor** page: 
     1. To retain the previously configured event subscription, click **Retain** , else click **Delete**. **Warning:** Deleting an event subscription will affect all the published integrations using the event subscription. This task cannot be undone.
     2. Update the connection configuration and event subscription details as desired.
     3. Click **Done**.

You can view the updated connection and event subscription details in the trigger configuration pane under **Event Subscription details**.




## Supported event subscription types

You can use the **Jira Cloud trigger** to invoke an integration for the following event subscription types:

Event subscription types | Description  
---|---  
`attachment_created` | An attachment is created for a Jira ticket.   
`attachment_deleted` | The attachment assiciated with a Jira ticket is deleted.   
`board_created` | A new Jira board is created.   
`board_deleted` | A Jira board is deleted.   
`comment_created` | A comment is added to the Jira ticket.   
`comment_deleted` | A comment in a Jira ticket is deleted.   
`comment_updated` | An existing comment in a Jira ticket is updated.   
`filter_created` | A new Jira filter is created.   
`filter_deleted` | A Jira filter is deleted.   
`filter_updated` | An existing Jira filter is updated.   
`issue_created` | A new Jira issue is created.   
`issue_deleted` | A Jira issue is deleted.   
`issue_updated` | An existing Jira issue is updated.   
`issuelink_created` | A new issue link is created for a Jira instance.   
`issuelink_deleted` | The issue link for a Jira instance is deleted.   
`option_issuelinks_changed` | An existing issue link for a Jira instance is changed or updated.   
`option_subtasks_changed` | The subtasks for an issue is updated or changed.   
`option_voting_changed` | The number of votes for a Jira issue is changed.   
`option_watching_changed` | The watchers or list of users who are added to watch a Jira issue have changed.   
`project_created` | A new project is created.   
`project_deleted` | A project is deleted.   
`project_restored_deleted` | A deleted project is restored.   
`project_soft_deleted` | A project is deleted such that it is not visible to any users, including admins using either the product interface or the API.   
`project_updated` | The project details are updated.   
`sprint_closed` | The sprint is closed.   
`sprint_created` | A sprint is created.   
`sprint_deleted` | A sprint is deleted.   
`sprint_updated` | The details of a sprint are changed or updated.   
`user_created` |  A user is created.   
`user_updated` | The details of a user are changed or updated.   
`worklog_created` | A worklog entry is added.   
`worklog_deleted` | A worklog entry is deleted.   
`worklog_updated` | A worklog entry is changed or updated.   
  
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
