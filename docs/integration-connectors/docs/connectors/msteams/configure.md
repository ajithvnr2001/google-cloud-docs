---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/msteams/configure/
title: Microsoft Teams \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:25.495061+00:00
---

# Microsoft Teams  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/msteams/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Microsoft Teams

The Microsoft Teams connector provides connectivity to Microsoft Teams application.

## Before you begin

Before using the Microsoft Teams connector, do the following tasks:

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
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Microsoft Teams** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 63 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. **Service Account** : Select a service account that has the required roles.
     6. Enter the **Azure-Tenant** for the connection instance.
     7. Optionally,select **Include All Groups** to include all the groups in your organization
     8. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     9. **SSL Configuration** : Select **Public(Default)** from the trust models.
     10. Click **Next**.
     11. In the **Authentication** section, complete the following: 
        1. **Client ID** : The client ID used for requesting access tokens.
        2. **Scopes** : A comma-separated list of desired scopes
        3. **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.
        4. **Secret version** : The version of the secret that contains the client secret.
        5. **Authorization URL** : The authorization URL that you generate when you create an OAuth client. Enter the URL in the following format: `https://login.microsoftonline.com/TENANT_IDENTIFIER/oauth2/v2.0/authorize?prompt=consent`. For example, `https://login.microsoftonline.com/9bxxxxxxxxx8112/oauth2/v2.0/authorize?prompt=consent`. 
        6. Click **Next**.
     12. **Review** : Review your connection and authentication details.
     13. Click **Create**.

For the `Authorization code` authentication type, after creating the connection, you must perform a few additional steps for configuring authentication. For more information, see Additional steps after connection creation.

**Note:** If you are using `Authorization code` authentication type and have made any cofiguration changes in your application, you must re-authorize your Microsoft Teams connection. To understand how to re-authorize, see Re-authorization for Authorization code. 

### Additional steps after connection creation

If you selected `OAuth 2.0 - Authorization code` for authentication, you must do the following additional steps after creating the connection:

     1. In the [Connections page](https://console.cloud.google.com/connectors/connections), locate the newly created connection. 

Notice that the **Status** for the new connector will be **Authorization required**.

     2. Click **Authorization required**. 

This shows the **Edit authorization** pane.

     3. Copy the **Redirect URI** value to your external application.
     4. Verify the authorization details.
     5. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com/connectors/connections).

## Re-authorization for authorization code

If you are using `Authorization code` authentication type and have made any cofiguration changes in your application, you must re-authorize your Microsoft Teams connection. To re-authorize a connection, perform the following steps:

     1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

     2. Click **Edit** to edit the connection details. 
     3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

     4. Click **Save**. This takes you to the connection details page.
     5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
     6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).

## System limitations

The Microsoft Teams connector can process 30 transactions per _minute_ , per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg) for the List Operation for `Team Members, Times Off, Channels, and Chats` entities, and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit.

By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 
     * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
     * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).

The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

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

## Action examples

This section shows how to perform some of the actions operations in this connector.

### Example - Actions

This example sends a message to a specific`Chat` entity.

     1. In the `Configure connector task` dialog, click `Actions`.
     2. Select `SendMessage` from the `Actions` list.
     3. Select the `Actions` operation, and then click **Done**.
     4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
            
            {
                    "TeamId": "cc110f3f-3088-4b4c-b965-e1f3e0a2dfab",
                    "ChannelId": "19%3a7680178ef3ab4b1eb762a7078b990083%40thread.tacv2",
                    "Content": "Hello Guys Lets play"
                  }

## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all records

This example lists all the records in the `Channel Members` entity.

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Channel Members` from the `Entity` list.
     3. Select the `List` operation, and then click **Done**.
     4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). For example, `Id='13b1724a91ce448bad2f1986321fc70f'`. You can also specify multiple filter conditions by using the logic operators. For example, `Id='13b1724a91ce448bad2f1986321fc70f' and Inactive=false`.

### Example - Get a record

This example gets a record with the specified ID from the `Chats` entity.

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Chats` from the `Entity` list.
     3. Select the `Get` operation, and then click **Done**.
     4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `19:1956432abc05491bb26f51f9f7263020@thread.v2` in the **Default Value** field. 

Here, `19:1956432abc05491bb26f51f9f7263020@thread.v2` is a primary key value in the `Chats` entity.

### Example - Create a record

This example creates a record in the `Group Owners` entity.

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Group Owners` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
            
            {
              "GroupId": "1356c566-d799-4d49-86c0-b09ab6afdb47",
              "MemberId": "caf19b29-3af1-4191-b455-16468e6aba4b"
            }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
            
            {
            "Id": "c3c68bc9a1343242443ca8e5ddcaa0000"
            }

### Example - Update a record

This example updates the record with the specified ID in the `Teams` entity.

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Teams` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
            
            {
                  "displayName": "My Team Name Changed",
                  "description": "Changed the description for my team"
                }

     5. Click **filterClause** , and then enter `id = '953933bc-1024-4ce7-84dc-bae7f24dc2ca'` in the **Default Value** field. 

### Example - Delete a record

This example deletes the record with the specified ID in the `Group Owners` entity.

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Group Owners` from the `Entity` list.
     3. Select the `Delete` operation, and then click **Done**.
**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). For example, `GroupId='cc110f3f-3088-4b4c-b965-e1f3e0a2dfab' AND OwnerId='c2e29127-839a-49b5-bd15-a592be4a997e'`.

## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
default_queue_name | STRING | False | The name of the default queue, may be overridden when executing action.   
default_topic_name | STRING | False | The name of the default topic, may be overridden when executing action.   
Bucket | STRING | True | The name of the bucket inside the project where tibjms.jar resides.   
Object ID | STRING | True | The name of the .jar file inside the bucket.   
  
## Use the Microsoft Teams connection in an integration

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
