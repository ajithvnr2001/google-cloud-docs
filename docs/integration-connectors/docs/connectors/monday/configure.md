---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/monday/configure/
title: Monday \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:31:19.552829+00:00
---

# Monday  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/monday/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monday

Use the Monday connector to perform insert, delete, update, and read operations on Monday.com.

## Before you begin

Before using the Monday connector, do the following tasks:

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

  * For information about how to get the API token for authentication, see [ API Token](https://developer.monday.com/api-reference/docs/authentication).
  * For information about authenticating Monday apps with OAuth 2.0, see [OAuth 2.0](https://developer.monday.com/apps/docs/oauth).



## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

Supported regions for connectors include: 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Monday** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. **Use proxy** : Select this checkbox to configure a proxy server for the connection. 
        * **Proxy Auth Scheme** : The authentication type to use to authenticate to the ProxyServer proxy. 
        * **Proxy User** : A user name to be used to authenticate to the ProxyServer proxy. 
        * **Proxy Password** : A password to be used to authenticate to the ProxyServer proxy. 
        * **Proxy SSL Type** : The SSL type to use when connecting to the ProxyServer proxy. 
     9. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     10. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : You can specify the destination details either as a host address or a service attachment. Select any of the following destination types: 
        * **Host address** : If you want to specify the hostname or IP address of the destination.
        * **Service attachment** : If you want to specify the private endpoint for your internal IP addresses. The service attachment, lets you hide your internal IP addresses from the external network. You can create a service attachment in Google Cloud, by using the Private Service Connect feature. For information on configuring a Private Service Connect, see [Publish managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

Based on your selection of destination type, enter the host address or the service attachment name.

To enter additional destinations, click **+Add destination**.

     2. Click **Next**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Monday connection:

        * OAuth 2.0 
        * API Token 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  7. **Review** : Review your connection and authentication details.
  8. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0**
    * **Client ID** : The client ID used for requesting access tokens.
    * **Client secret** : The client secret used for requesting access tokens.
    * **OAuth Access token** : The access token used for authenticating requests with auth-code-flow-based connections.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.



  * **API Token**

If you want to use anonymous login, select **Not Available**.

    * **API Token** : The API token obtained from your Monday account.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### API token connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Monday  
Connector version | 1  
Connection Name | monday-new-connector  
Enable Cloud Logging | Yes  
Log Level | Debug  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2 | Maximum number of nodes | 50  
Destination Type | Host Address  
Host 1 | https://your-domain.monday.com/  
Authentication | Yes  
API Token | API_TOKEN  
Secret version | 1The resource name of the secret version has the following format: projects/PROJECT_NUMBER/secrets/CONNECTOR/versions/1  
  
### OAuth 2.0 connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Monday  
Connector version | 1  
Connection Name | monday-oauth-conn  
Enable Cloud Logging | Yes  
Log Level | Error  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host Address  
Host 1 | https://your-domain.monday.com/  
Authentication | Yes  
Client ID | CLIENT_ID  
Client Secret | CLIENT_SECRET  
Secret version | 1The resource name of the secret version has the following format: projects/PROJECT_NUMBER/secrets/CONNECTOR/versions/1  
Scope | account:read, users:read, assets:read, boards:read, boards:write, docs:read, docs:write, me:read, notifications:write, tags:read, teams:read, updates:read, updates:write, users:read, users:write, workspaces:read, workspaces:write  
  
## System limitations

The Monday connector can process a maximum of 1 query per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Monday connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).



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

This section lists the actions supported by the Monday connector. To understand how to configure the actions, see Action examples.

### CreateNotification action

This action creates a new notification.

#### Input parameters of the CreateNotification action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserId | String | Yes | The users unique identifier  
TargetType | String | Yes | The targets type(Project/Post).  
TargetId | String | Yes | The targets unique identifier  
Text | String | Yes | The notification text  
  
For example on how to configure the `CreateNotification` action, see  Examples.

### MoveItemToBoard action

This action moves or transfers the boards/files from one instance to another.

#### Input parameters of the MoveItemToBoard action

Parameter name | Data type | Required | Description  
---|---|---|---  
BoardId | String | Yes | The unique identifier of target board.  
GroupId | String | Yes | The unique identifier of target group.  
ItemId | String | Yes | The unique identifier of the item to move.  
  
For example on how to configure the `MoveItemToBoard` action, see  Examples.

### DuplicateItem action

This action duplicates an existing item.

#### Input parameters of the DuplicateItem action

Parameter name | Data type | Required | Description  
---|---|---|---  
ItemId | String | Yes | The unique identifier of the item.  
BoardId | String | Yes | The unique identifier of the board.  
WithUpdates | Boolean | Yes | Duplicate with the item updates.  
  
For example on how to configure the `DuplicateItem` action, see Examples.

### LikeUpdate action

This action enables you to like a post.

#### Input parameters of the LikeUpdate action

Parameter name | Data type | Required | Description  
---|---|---|---  
UpdateId | String | Yes | The update identifier  
  
For example on how to configure the `LikeUpdate` action, see  Examples.

### AddFileToColumn action

This action adds a file to a column.

#### Input parameters of the AddFileToColumn action

Parameter name | Data type | Required | Description  
---|---|---|---  
ItemId | String | Yes | The unique identifier of the item.  
ColumnId | String | Yes | The unique identifier of the column.  
Content | String | Yes | String content to upload a file.  
  
For example on how to configure the `AddFileToColumn` action, see  Examples.

### AddFileToUpdate action

This action adds a file to update.

#### Input parameters of the AddFileToUpdate action

Parameter name | Data type | Required | Description  
---|---|---|---  
UpdateId | String | Yes | The update identifier  
Content | String | Yes | String content to upload a file.  
  
For example on how to configure the `AddFileToUpdate` action, see  Examples.

### DuplicateBoard action

This action duplicates data for a particular action.

#### Input parameters of the DuplicateBoard action

Parameter name | Data type | Required | Description  
---|---|---|---  
BoardId | String | Yes | The unique identifier of the board  
DuplicateType | String | Yes | The duplication type.  
  
For example on how to configure the `DuplicateBoard` action, see  Examples.

### DuplicateGroup action

This action duplicates data for a group.

#### Input parameters of the DuplicateGroup action

Parameter name | Data type | Required | Description  
---|---|---|---  
BoardId | String | Yes | The unique identifier of the board  
GroupId | String | Yes | The unique identifier of Group.  
AddToTop | Boolean | Yes | Indicates whether the new group is added to the top.  
GroupTitle | String | Yes | The group title.  
  
For example on how to configure the `DuplicateGroup` action, see  Examples.

## Action Examples

This section describes how to perform some of the actions in this connector.

### Example - CreateNotification

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateNotification` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "UserId": "64384966",
               "TargetType": "Project",
               "TargetId": "1899350039",
               "Text": "This is notification from google Cloud."
             }
             

If the action is successful, the `CreateNotification` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
          "notificationid": "-1"
        }] 
        




### Example - MoveItemToBoard

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MoveItemToBoard` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "BoardId": "1900739644",
               "GroupId": "topics",
               "ItemId": "1901835960"
             }
             

If the action is successful, the `MoveItemToBoard` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
          "itemid": "1901835960"
        }]
        




### Example - DuplicateItem

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DuplicateItem` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "ItemId": "1901835811",
             "BoardId": "1899350039",
             "WithUpdates": true
           }
           

If the action is successful, the `DuplicateItem` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "itemid": "1901835960"
      }]
      




### Example - LikeUpdate

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `LikeUpdate` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UpdateId": "18397960"
           }
           

If the action is successful, the `LikeUpdate` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "updateid": "690939"
      }] 
      




### Example - AddFileToColumn

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddFileToColumn` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "ItemId": "1901866680",
             "ColumnId": "files",
             "Content": "HI Team"
           }
           

If the action is successful, the `AddFileToColumn` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "assetid": "13325557"
      }]
      




### Example - AddFileToUpdate

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddFileToUpdate` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UpdateId": "18397903",
             "Content": "Integration Testing File Updated."
           }
           

If the action is successful, the `AddFileToUpdate` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "assetid": "13325933"
      }]
    




### Example - DuplicateGroup

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DuplicateGroup` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "BoardId": "1899350039",
             "GroupId": "new_demo_group4869__1",
             "AddToTop": true,
             "GroupTitle": "Duplicate Group"
           }
         

If the action is successful, the `DuplicateGroup` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "assetid": "13325933"
      }]
    




### Example - DuplicateBoard

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DuplicateBoard` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "BoardId": "1900733069",
             "DuplicateType": "duplicate_board_with_structure"
           }
           

If the action is successful, the `DuplicateBoard` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "assetid": "13325933"
      }]
      




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List operation for Workspaces

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Workspaces` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement. You can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



You can perform List operation on the following entities:

Folders, Boards, BoardViews, BoardUsers, BoardTeams, ActivityLogs, Webhook, Tags, Users, Doc, DocBlocks, Teams, MoveItemToBoard, Groups, Updates, WorkspaceTeams, WorkspaceUsers, TeamUsers, Columns

GoogleTestingProject entity is a dynamically exposed entity. Using this entity, you can perform CRUD operations on Items and any column type.

### Example - Get a single record from Workspaces

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Workspaces` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to "961430" which is the Key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"961430"` in the **Input Value** field and choose the EntityId as Local variable. 



If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

You can perform Get operation on the following entities:

Boards, BoardViews, ActivityLogs, WebHook, Tags, Asset, Users, Doc, DocBlock, Team, Updates, Columns

### Example - Delete a record from the entity Workspaces

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Workspaces` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to "961430" which is the Key to be passed.To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"961430"` in the **Input Value** field and choose the EntityId as Local variable. 

Alternately, if the entity has two composite business or primary keys instead of specifying the **entityId** , you can also set the **filterClause** to ` id='961430'`.




You can perform Delete operation on the following entities:

Folders, Boards, WebHook, Groups, SubItem, DocBlock, TeamUser, WorkspaceUser, Boards, BoardTeams, BoardUsers, Updates, Columns

### Example - Create entity Workspace

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Workspace` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "Name": "Riky's Workspace",
           "Kind": "open",
           "Description": "This is Riky's Workspace"
         }
         

This example will create the Workspace. If the integration is successful, the `Workspace` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "964218"
         }
         




### Example - Create entity Workspaceuser (Single User)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Workspaceuser` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "WorkspaceId": "952743",
           "Kind": "subscriber",
           "Id": "'64427450'"
         }

This example demonstrates how to add a single user in a Workspace and if the integration is successful, the `Workspaceuser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Success": true
         }
         




### Example - Create entity Workspaceuser (Multiple Users)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Workspaceuser` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "WorkspaceId": "1027130",
           "Kind": "subscriber",
           "Id": "64427450,64426103,65189599"
         }

This example demonstrates how to add multiple users in a workspace. If the integration is successful, the `Workspaceuser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "64426103",
           "WorkspaceId": "1027130"
         }
         




### Example - Create entity WorkspaceTeams (Single Team)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `WorkspaceTeams` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "WorkspaceId": "1027130",
           "Kind": "subscriber",
           "Id": "16516"
         }

This example demonstrates how to add a single team in a workspace. If the integration is successful, the `WorkspaceTeams` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "16516",
           "WorkspaceId": "1027130"
         }
         




### Example - Create entity WorkspaceTeams (Multiple Teams)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `WorkspaceTeams` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "WorkspaceId": "1027130",
           "Kind": "subscriber",
           "Id": "16516,15056,14926"
         }

This example demonstrates how to add multiple teams in a workspace. If the integration is successful, the `WorkspaceTeams` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "16516",
           "WorkspaceId": "1027130"
         }




### Example - Create entity TeamUser (Single User)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TeamUser` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "TeamId": "15056",
           "Id": "64427450"
         }

This example demonstrates how to add a single user in a team and if the integration is successful, the `TeamUser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "64427450",
           "TeamId": 15056
         }




### Example - Create entity TeamUser (MultipleUsers)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TeamUser` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "TeamId": "16516",
           "Id": "64427450,64426103,65189599"
         }

This example demonstrates how to add multiple users in a team and if the integration is successful, the `TeamUser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "64427450",
           "TeamId": "16516"
         }




### Example - Create entity Boards

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Boards` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "Name": "New Demo Board",
           "BoardKind": "public"
         }

This example will create the Boards. If the integration is successful, the `Boards` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "1900733069"
         }
         




### Example - Create entity Boardusers (Single User)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Boardusers` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1900739644",
           "Id": "64385055",
           "Kind": "subscriber"
         }

This example demonstrates how to add a single user to a board and if the integration is successful, the `Boardusers` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "64385055",
           "BoardId": null
         } 
         




### Example - Create entity Boardusers (Multiple Users)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Boardusers` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1899350039",
           "Id": "64427450,64426103,65189599",
           "Kind": "subscriber"
         }
         

This example demonstrates how to add multiple users to a board and if the integration is successful, the `Boardusers` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Id": "64426103",
         "BoardId": "1899350039"
         }
         




### Example - Create entity BoardTeam (Single Team)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `BoardTeam` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1899350039",
           "Id": "14926",
           "Kind": "subscriber"
          }

This example demonstrates how to add a single team to a board. If the integration is successful, the `BoardTeam` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "14926",
           "BoardId": null
         }
         




### Example - Create entity BoardTeam (Multiple Team)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `BoardTeam` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1919494280",
           "Id": "16516,15056,14926",
           "Kind": "subscriber"
         }
         

This example demonstrates how to add multiple teams to a board and if the integration is successful, the `BoardTeam` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "16516",
           "BoardId": "1919494280"
         } 
         




### Example - Create entity Group

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Group` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1899350039",
           "Title": "New Demo Group",
           "RelativeTo": "mohit group",
           "PositionRelativeMethod": "after_at",
           "Color": "#FFCB00"
         }
         

This example will create the Group. If the integration is successful, the `Group` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "new_demo_group29615__1",
           "BoardId": "1899350039"
         }
         




### Example - Create entity Columns

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "people",
           "Title": "PeopleInfo",
           "Id": "people1"
         }
         

This example will create the Column and if the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "people1",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Date)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "Title": "Date",
           "Type": "date",
           "BoardId": "1922602090",
           "Id": "date"
         }
          

This example will create the Date column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "date",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Dropdown)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "dropdown",
           "Title": "Dropdown",
           "Id": "dropdown_1"
         }
         

This example will create the Dropdown column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "dropdown_1",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Email)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "email",
           "Title": "Mail",
           "Id": "mail_11"
         }
         

This example will create the Email column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "mail_11",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(LongText)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "long_text",
           "Title": "Longtext",
           "Id": "longtext1"
         }
         

This example will create the LongText column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "longtext1",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Number)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "numbers",
           "Title": "Number",
           "Id": "number"
         }
         

This example will create the Number column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "number",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Phone)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "phone",
           "Title": "PhoneNumber",
           "Id": "phone43"
         }
         

This example will create the Phone column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "phone43",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Text)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "text",
           "Title": "Text",
           "Id": "text18"
         }
         

This example will create the Text column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "text18",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns (Dependency)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "dependency",
           "Title": "Dependency",
           "Id": "dependency_1"
         }
          

This example will create the Dependency column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "dependency_1",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns (People)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "people",
           "Title": "PeopleInfo",
           "Id": "people123"
         }
          

This example will create the People column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "people123",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns (Country)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "country",
           "Title": "Country",
           "Id": "country"
         }
         

This example will create the Country column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "country",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns (Hour)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "hour",
           "Title": "Hour",
           "Id": "hour"
         }
          

This example will create the Hour column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "hour",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Link)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "link",
           "Title": "LINK",
           "Id": "linkurl"
         }
          

This example will create the Link column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "linkurl",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns (Location)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "location",
           "Title": "Location",
           "Id": "location"
         }
          

This example will create the Location column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "location",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Rating)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "rating",
           "Title": "Rating",
           "Id": "rating123"
         }
          

This example will create the Rating column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "rating123",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Timeline)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "timeline",
           "Title": "Timeline",
           "Id": "timeline"
         }
          

This example will create the Timeline column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "timeline",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(Week)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "week",
           "Title": "Week",
           "Id": "week_12"
         }
         

This example will create the Week column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "week_12",
           "BoardId": "1922602090"
         }
         




### Example - Create entity Columns(WorldClock)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "BoardId": "1922602090",
           "Type": "world_clock",
           "Title": "World Clock",
           "Id": "world_clock1"
         }
         

This example will create the World Clock column. If the integration is successful, the `Columns` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "world_clock1",
           "BoardId": "1922602090"
         }
         




### Example - Create entity GoogleTestingProject(SubItem)

GoogleTestingProject entity is a dynamically exposed entity. Using this entity, you can perform CRUD operations on Items and any column type. 

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `GoogleTestingProject` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "ParentItemId": "1901835811",
           "Subitem": "Cloud_Sub-Item NAme"
         }
          

This example will create the SubItem. If the integration is successful, the `GoogleTestingProject` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "ItemId": "1901893886"
         }
         




### Example - Update entity Workspaces

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Workspaces` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
           "Description": "Updated Workspace",
           "Name": "Riky's Updated Workspace"
         }
         

  5. Instead of specifying the **entityId** , you can also set the **filterClause** to `964218`.

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
           "Id": "964218"
         }
         




### Example - Update entity Boards

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Boards` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
           "State": "archived"
         }
         

  5. Instead of specifying the **entityId** , you can also set the **filterClause** to `1899875405`.

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
           "Id": "1899875405"
         }
         




### Example - Update entity Group

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Group` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
           "Color": "#FFCB00"
         }
         

  5. Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='new_demo_group4301__1'` and `BoardId='1899350039'`.

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
           "Id": "new_demo_group4301__1",
           "BoardId": "1899350039"
         }
         




### Example - Update entity Columns

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Columns` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
           "Description": "People Information"
         } 
         

  5. Instead of specifying the **entityId** , you can also set the **filterClause** to `1922602090`.

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
           "Id": "people1",
           "BoardId": "1922602090"
         }
         




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

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
