---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/onedrive/configure/
title: OneDrive \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:42.032451+00:00
---

# OneDrive  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/onedrive/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# OneDrive

The Onedrive connector lets you perform insert, delete, update, and read operations on OneDrive.

## Before you begin

Before using the OneDrive connector, do the following tasks:

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

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Onedrive** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 63 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. **Service Account** : Select a service account that has the required roles.
     6. **Verbosity Level** : Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates). 
     7. **Azure Tenant** : The Microsoft Online tenant that is used to access data. If not specified, your default tenant is used.
     8. **Drive ID** : The ID of the drive that you want to use.
     9. **List Group Drives** Optionally, you can choose to list your group drives when querying drives.
     10. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     11. Click **NEXT**.
     12. In the **Authorization** section, enter details of the client ID and client secret. 
        * **Client ID** : The client ID used for requesting access tokens. 
        * **Scope** : A comma-separated list of desired scopes from Microsoft Azure Portal. 
        * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created. 
        * **Secret version** : Secret version for the secret selected above. 
        * **Authorization URL** : The authorization URL that you generate when you create an OAuth client. Enter the URL in the following format: `https://login.microsoftonline.com/TENANT_IDENTIFIER/oauth2/v2.0/authorize?prompt=consent`. For example, `https://login.microsoftonline.com/9bxxxxxxxxx8112/oauth2/v2.0/authorize?prompt=consent`. 
     13. Click **NEXT**. 
     14. **Review** : Review your connection and authentication details.
     15. Click **Create**.

For the `Authorization code` authentication type, after creating the connection, you must perform a few additional steps for configuring authentication. For more information, see Additional steps after connection creation.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

**Note:** If you are using `Authorization code` authentication type and have made any cofiguration changes in your application, you must re-authorize your Onedrive connection. To understand how to re-authorize, see Re-authorization for Authorization code. 

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

If you are using `Authorization code` authentication type and have made any cofiguration changes in your application, you must re-authorize your Onedrive connection. To re-authorize a connection, perform the following steps:

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

The Onedrive connector can process can process a maximum of 15 transactions per _minute_ , per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit:

By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 
     * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
     * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).

The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Onedrive connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

     * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
     * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).

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

## Actions

The Onedrive connection supports the following actions:

### CopyResource action

The following table describes the input parameters of the CopyResource action.

#### Input parameters of the CopyResource action

Parameter name | Required | Data type | Description  
---|---|---|---  
ParentID | Yes | String | The ID of the folder you want to copy the resource to.  
ResourceId | Yes | String | Id of the resource.  
  
### CreateFolder action

The following table describes the input parameters of the CreateFolder action.

#### Input parameters of the CreateFolder action

Parameter name | Required | Data type | Description  
---|---|---|---  
FolderName | Yes | String | Name of the folder to be created.  
queueName | No | String | Message to be sent to the TIBCO EMS queue. The maximum message size supported is 10 MB.  
  
### DeleteResource action

The following table describes the input parameters of the DeleteResource action.

#### Input parameters of the DeleteResource action

Parameter name | Required | Data type | Description  
---|---|---|---  
ResourceId | Yes | String | Id of the resource.  
  
### MoveResource action

The following table describes the input parameters of the MoveResource action.

#### Input parameters of the MoveResource action

Parameter name | Required | Data type | Description  
---|---|---|---  
ResourceId | Yes | String | Id of the resource.  
DestinationID | Yes | String | The ID of the folder you want to move the resource to.  
  
### RenameResource action

The following table describes the input parameters of the RenameResource action.

#### Input parameters of the RenameResource action

Parameter name | Required | Data type | Description  
---|---|---|---  
ResourceId | Yes | String | Id of the resource.  
Name | Yes | String | The new name of the resource.  
  
### UploadFile action

The following table describes the input parameters of the UploadFile action.

#### Input parameters of the UploadFile action

Parameter name | Required | Data type | Description  
---|---|---|---  
ParentId | Yes | String | The parent to which to upload the file.  
FileName | Yes | String | Name of the file to which you'll upload content to.  



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
