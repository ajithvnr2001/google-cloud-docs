---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/slack/configure/
title: Slack \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:01.893597+00:00
---

# Slack  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/slack/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Slack

The Slack connector lets you perform insert, delete, update, and read operations on Slack data.

## Before you begin

Before using the Slack connector, do the following tasks:

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

  * For information about how to create a Slack workspace, see [Quickstart with Slack](https://slack.com/intl/en-in/help/categories/360000049043-Getting-started). For information about Slack platform, see [Slack platform overview](https://api.slack.com/docs).



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
     1. **Connector** : Select **Slack** from the drop down list of available Connectors.
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
     8. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
        * **Proxy Auth Scheme** : Select the authentication type to authenticate with the proxy server. The following authentication types are supported: 
          * **Basic** : Basic HTTP authentication.
          * **Digest** : Digest HTTP authentication.
        * **Proxy User** : A user name to be used to authenticate with the proxy server. 
        * **Proxy Password** : The Secret manager secret of the user's password. 
        * **Proxy SSL Type** : The SSL type to use when connecting to the proxy server. The following authentication types are supported: 
          * **Auto** : Default setting. If the URL is an HTTPS URL, then the Tunnel option is used. If the URL is an HTTP URL, then the NEVER option is used.
          * **Always** : The connection is always SSL enabled.
          * **Never** : The connection is not SSL enabled.
          * **Tunnel** : The connection is through a tunneling proxy. The proxy server opens a connection to the remote host and traffic flows back and forth through the proxy.
        * In the **Proxy Server** section, enter details of the proxy server. 
          1. Click **\+ Add destination**.
          2. Select a **Destination Type**. 
             * **Host address** : Specify the hostname or IP address of the destination. 

If you want to establish a private connection to your backend system, do the following:

               * Create a [PSC service attachment](https://docs.cloud.google.com/integration-connectors/docs/configure-psc).
               * Create an [endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/create-ep-attachment) and then enter the details of the endpoint attachment in the **Host address** field.
     9. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     10. Click **NEXT**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Slack connection:

        * OAuth2.0 - Authorization Code 
        * User Token Authentication 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **NEXT**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the required details for your chosen authentication method. Connections to Slack use SSL by default and are validated using the public trust store and accepts both root certificates and certificate chains.

  * **OAuth2.0 - Authorization Code**

To authenticate using OAuth2.0, enter the following details:

    * **Client ID** : The client id provided by connector for the app you created.
    * **Scopes** : A comma-separated list of desired scope.
    * **Client Secret** : Secret manager secret containing the client secret for the connected app you created.
    * **Secret Version** : Secret version for the secret selected above.


  * **User Token Authentication**

To authenticate using user token, enter the following details:

    * **User Token** : The user token used to authenticate the user.
    * **Secret Version** : Secret version for the secret selected above.



For the `Authorization code` authentication type, after creating the connection, you must perform a few additional steps for configuring authentication. For more information, see Additional steps after connection creation.

**Note:** If you are using `Authorization code` authentication type and have made any configuration changes in your application, you must re-authorize your Onedrive connection. To understand how to re-authorize, see Re-authorization for Authorization code. 

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

If you are using `Authorization code` authentication type and have made any configuration changes in your application, you must re-authorize your Onedrive connection. To re-authorize a connection, perform the following steps:

  1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

  2. Click **Edit** to edit the connection details. 
  3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

  4. Click **Save**. This takes you to the connection details page.
  5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
  6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

###  Slack - UserToken authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Slack  
Connector version | 1  
Connection Name | slack-usertoken-connection  
Enable Cloud Logging | Yes  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
User Token Authentication | Yes  
User Token | USER_TOKEN  
Secret version | 1  
  
### Slack - OAuth 2.0 authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Slack  
Connector version | 1  
Connection Name | slack-google-cloud-oauth-conn  
Enable Cloud Logging | Yes  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
OAuth 2.0 - Authorization code | Yes  
Client ID | CLIENT_ID  
Scopes | channels:read, groups:read, im:read, mpim:read, channels:write, groups:write,   
im:write,mpim:write, channels:history, groups:history, im:history, mpim:history,   
search:read, chat:write:user, chat:write:bot, files:read, files:write:user, pins:read,   
pins:write,usergroups:read, usergroups:write, reminders:read, reminders:write,   
users:read, users.profile:write   
Client Secret | CLIENT_SECRET  
Secret version | 2  
  
## System limitations

The Slack connector can process a maximum of 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Slack connection in an integration

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

This section lists the actions supported by the Slack connector. To understand how to configure the actions, see Action examples.

### InviteUser action

This action invites users to a channel.

#### Input parameters of the InviteUser action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ChannelId | String | True | The Id of the public or private channel to invite user(s).  
Users | String | True | A comma separated list of user Ids. You can specify up to 30 users IDs.  
  
For an example about how to configure the `InviteUser` action, see InviteUser Example.

### CloseChannel action

This action closes a direct message or multiperson direct message.

#### Input parameters of CloseChannel

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ChannelId | String | True | Id of the conversation to close.  
  
For an example about how to configure the `CloseChannel` action, see CloseChannel Example.

### JoinChannel action

This action allows a user to join an existing conversation.

#### Input parameters of JoinChannel

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ChannelId | String | True | The Id of the channel to join.  
  
For an example about how to configure the `JoinChannel` action, see JoinChannel Example.

### LeaveChannel action

This action allows a user to leave a conversation.

#### Input parameters of LeaveChannel

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ChannelId | String | True | Id of the conversation to leave.  
  
For an example about how to configure the `LeaveChannel` action, see LeaveChannel Example.

### OpenChannel action

This action opens or resumes a direct message or multiperson direct message.

#### Input parameters of OpenChannel

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ChannelId | String | True | Resume a conversation by supplying the ID of the instant message or multiperson instant message, or specify the user IDs.  
Users | String | True | Comma-separated lists of users. If only one user is specified, a 1:1 direct message is created. If you don't specify any users, specify a channel ID to resume a conversation.  
  
For an example about how to configure the `OpenChannel` action, see OpenChannel Example.

### DownloadFile action

This action downloads a file.

#### Input parameters of DownloadFile

Parameter Name | Data Type | Accepts Output Streams | Description  
---|---|---|---  
FileId | String | False | The Id of the file to be downloaded  
FileLocation | String | False | The location where file is to be downloaded  
FileStream | String | True | An instance of an output stream where to which to write the file data. This field is used if the FileLocation is not specified.  
Encoding | String | False | The encoding type of the FileData. You can specify BASE64 or NONE. The default value is BASE64.  
  
For an example about how to configure the `DownloadFile` action, see DownloadFile Example.

### EndDnd action

This action ends the do not disturb mode of a user.

#### Input parameters of the EndDnd action

Pass an empty json, such as `{}`.

For an example about how to configure the `EndDnd` action, see EndDnd Example.

### SetSnooze action

This action turns on the do not disturb mode for the user or changes its duration.

#### Input parameters of the SetSnooze action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
NumOfMinutes | String | 60 | Number of minutes to snooze the user.  
  
For an example about how to configure the `SetSnooze` action, see SetSnooze Example.

### EndSnooze action

This action ends the user's snooze mode.

#### Input parameters of the EndSnooze action

Pass an empty json, such as `{}`.

For an example about how to configure the `EndSnooze` action, see EndSnooze Example.

### SendScheduleMessage action

This action schedules a message to be sent to a channel.

#### Input parameters of the SendScheduleMessage action

Pass an empty json, such as `{}`.

For an example about how to configure the `SendScheduleMessage` action, see SendScheduleMessage Example.

### RemoveProfilePhoto action

This action removes the user's profile photo.

#### Input parameters of the RemoveProfilePhoto action

Pass an empty json, such as `{}`.

For an example about how to configure the `RemoveProfilePhoto` action, see RemoveProfilePhoto Example.

### SendEphemeralMessage action

This action sends an ephemeral message to a user in a channel.

#### Input parameters of the SendEphemeralMessage action

Pass an empty json, such as `{}`.

For an example about how to configure the `SendEphemeralMessage` action, see SendEphemeralMessage Example.

### GetPermaLink action

This action retrieves a permalink URL to a specific message within a conversation or channel.

#### Input parameters of the GetPermaLink action

Parameter name | Data type | Required | Description  
---|---|---|---  
ChannelId | String | True | The unique ID of the channel.  
MessageId | String | True | The ID of the message.  
  
For an example about how to configure the `GetPermaLink` action, see GetPermaLink Example.

### SetReadCursor action

This action sets the read position in a channel to mark messages up to a specific point as read.

#### Input parameters of the SetReadCursor action

Parameter name | Data type | Required | Description  
---|---|---|---  
ChannelId | String | True | The unique ID of the channel.  
MessageId | String | True | The ID of the message.  
  
For an example about how to configure the `SetReadCursor` action, see SetReadCursor Example.

### GetTeamBillableInfo action

This action retrieves billing details for a workspace, including the current plan and billable user information.

#### Input parameters of the GetTeamBillableInfo action

Pass an empty json, such as `{}`.

For an example about how to configure the `GetTeamBillableInfo` action, see GetTeamBillableInfo Example.

### EnableUserGroup action

This action enables a user group.

#### Input parameters of the EnableUserGroup action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserGroup | String | True | The ID of the user group.  
TeamId | String | True | The ID of the team associated with the user group.  
  
For an example about how to configure the `EnableUserGroup` action, see EnableUserGroup Example.

### DisableUserGroup action

This action disables a user group.

#### Input parameters of the DisableUserGroup action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserGroup | String | True | The ID of the user group.  
TeamId | String | True | The ID of the team associated with the user group.  
  
For an example about how to configure the `DisableUserGroup` action, see DisableUserGroup Example.

## Action examples

### Example - InviteUser

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `InviteUser` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ChannelId": "C06Q6NTRNA2",
           "Users": "U070MCLRREW"
         }

If the action is successful, the `InviteUser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "Success": "true"
    }] 




### Example - CloseChannel

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CloseChannel` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ChannelId": "C075U92TU4U"
         }

If the action is successful, the `CloseChannel` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "Success": "true"
    }] 




### Example - JoinChannel

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `JoinChannel` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ChannelId": "C06UMDTL1EH"
         }

If the action is successful, the `JoinChannel` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "Success": "true"
    }] 




### Example - LeaveChannel

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `LeaveChannel` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ChannelId": "C06UME4PM2R"
         }

If the action is successful, the `LeaveChannel` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "Success": "true"
    }]




### Example - OpenChannel

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `OpenChannel` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Users": "U06VCS3NDNC,U06NE4KAL0G",
         "ChannelId": "C071CU9UXFF"
         }

If the action is successful, the `OpenChannel` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
    "Success": "true"
    }]




### Example - DownloadFile

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "FileId": "F075UHEMSN8",
           "HasBytes": true
         }

If the action is successful, the `DownloadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": "True",
      "ContentBytes": "JVBERi0xLjMKJcTl8uXrp/Og0MTGCjQgMCBvYmoKPDwgL0xlbmd0aCA1IDAgUiAvRmlsdGVyIC9GbGF0ZURlY29kZSA"
    }]




#### Additional considerations

  * Set "HasBytes" as "True" to download other file formats, such as PDF or xlsx, which provide the contents in Base 64 encoded format.
  * To download a file in txt format, set "HasBytes" to "True" and download file content as bytes. To download the actual contents of the file, set "HasBytes" to "False".



### Example - EndDnd

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `EndDnd` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {}

If the action is successful, the `EndDnd` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "Success": "true"
    }]  




### Example - SetSnooze

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SetSnooze` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "NumOfMinutes": "60"
         }

If the action is successful, the `SetSnooze` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "Success": "true",
      "SnoozeEnabled": "true",
      "SnoozeEndTime": "1722842455",
      "SnoozeRemaining": "3600",
      "SnoozeIsIndefinite": "false"
    }]




### Example - EndSnooze

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `EndSnooze` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {}

If the action is successful, the `EndSnooze` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
      [{
      "Success": "true",
      "DndEnabled": "true",
      "NextDndStartTime": "1722875400",
      "NextDndEndTime": "1722911400",
      "SnoozeEnabled": "false"
    }]




### Example - SendScheduleMessage

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendScheduleMessage` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Channel": "C07AMLB39JN",
           "PostAt": "2024-08-27 14:15:00.0",
           "Text": "Hello, World!",
           "ReplyBroadCast": false
          }

If the action is successful, the `SendScheduleMessage` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
       [{
      "Success": "true",
      "ok": "true",
      "scheduled_message_id": "Q07KD4YSG72",
      "channel": "C07AMLB39JN",
      "post_at": "1724768100",
      "message_user": "U071FD3TS8P",
      "message_type": "message",
      "message_bot_id": "B076304QR9V",
      "message_app_id": "A076HCDGHT5",
      "message_text": "Hello, World!",
      "message_team": "T071W04MGV8",
      "message_bot_profile_id": "B076304QR9V",
      "message_bot_profile_deleted": "false",
      "message_bot_profile_name": "Googlecloud_OAuth_Slack",
      "message_bot_profile_updated": "1717513424",
      "message_bot_profile_app_id": "A076HCDGHT5",
      "message_bot_profile_icons_image_36": "https://a.slack-edge.com/80588/img/plugins/app/bot_36.png",
      "message_bot_profile_icons_image_48": "https://a.slack-edge.com/80588/img/plugins/app/bot_48.png",
      "message_bot_profile_icons_image_72": "https://a.slack-edge.com/80588/img/plugins/app/service_72.png",
      "message_bot_profile_team_id": "T071W04MGV8",
      "message_blocks_type": "rich_text",
      "message_blocks_block_id": "MYA",
      "message_blocks_elements_type": "rich_text_section",
      "message_blocks_elements_elements_type": "text",
      "message_blocks_elements_elements_text": "Hello, World!"
    }]




### Example - RemoveProfilePhoto

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveProfilePhoto` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {}
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": "true"
     }]
    




### Example - SendEphemeralMessage

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendEphemeralMessage` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {}
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": "true"
     }]
    
    




### Example - GetPermaLink

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetPermaLink` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ChannelId": "C071W04P682",
           "MessageId": "1734939860.333379"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "Success": "true",
        "ChannelId": "C071W04P682",
        "PermaLink": "https://altostrat-ic97757.slack.com/archives/C071W04P682/p1734939860333379"
      }
    ]
    




### Example - SetReadCursor

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SetReadCursor` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ChannelId": "C07AMLB39JN",
           "MessageId": "1724767860.360739"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "Success": "true"
      }
    ]
    




### Example - GetTeamBillableInfo

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetTeamBillableInfo` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {}
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "Success": "true",
        "Plan": "std"
      }
    ]
    




### Example - EnableUserGroup

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `EnableUserGroup` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserGroup": "S08696VPXPC",
           "TeamId": "T071W04MGV8"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "Success": "true"
      }
    ]
    




### Example - DisableUserGroup

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DisableUserGroup` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserGroup": "S08696VPXPC",
           "TeamId": "T071W04MGV8"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "Success": "true"
      }
    ]
    




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List records of the Messages entity

This example lists the records of the `Messages` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Messages` from the `Entity` List.
  3. Select the `List` operation, and then click **Done**.



You can perform list operation on the following entities as well: Files, MessageReplies, Pins, Reactions, Reminders,TeamInfo, UserGroups, Users, Channels, DND, Teams, UserProfile, ScheduledMessages, TeamProfileFields, and TeamProfileSections.

### Example - Get records of the Calls entity

This example fetches the records of the `Calls` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Calls` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to R070LKL3YKX which is the Key to be passed. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `R070LKL3YKX` in the **Default Value** field. 



The value for Entity Id must be passed directly. In this example R070LKL3YKX is the unique primary key value and it is passed directly.

You can perform get operations on the following entities as well: Calls, MessageReplies, Messages, Reactions,TeamInfo, Reminders, Users, and Channels

### Example - Delete records of the Calls entity

This example deletes the records of the `Calls` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Calls` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to R074DSKVDSS which is the Key to be passed. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `R074DSKVDSS` in the **Default Value** field. 

If the entity has two composite business or primary keys, you can set the **filterClause** to `Id='R074DSKVDSS'`.




You can perform delete operations on the following entities as well: Files, MessageReplies, Messages, Pins, Reactions, and Reminders.

### Example - Create records of the Calls entity

This example creates records of the `Calls` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Calls` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ExternalUniqueId": "c249a48c-a154-43d6-a286-791df11927a4",
           "JoinURL": "https://example55.com/call"
         }

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         
         {
           "Id": "R074LBCFBU3"
         } 




### Example - Create records of the Messages entity

This example creates records of the `Messages` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Messages` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ChannelId": "C06UF15CB0V",
           "Text": "This is google cloud created Message"
         }

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the :
         
         
         {
         "Id": "1723008314.867479",
         "ChannelId": "C06UF15CB0V"
         }   




### Example - Create a record of the Pins entity

This example creates a record of the `Pins` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Pins` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ChannelId": "C06UF15CB0V",
         "Id": "1723008314.867479",
         "Type": "message"
         }

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the :
         
         
         {
         "Id": "1723008314.867479",
         "Type": "message",
         "ChannelId": "C06UF15CB0V"
         }




### Example - Create a record of the Reactions entity

This example creates a record of the `Reactions` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Reactions` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ChannelId": "C06UPA4KRD0",
           "Id": "1716375032.038669",
           "Type": "message",
           "Name": "raised_hands"
         }

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         
         {
           "Success": true
         }   




### Example - Create a record of the Reminders entity

This example creates a record of the `Reminders` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Reminders` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Text": "this is a reminder",
           "Time": "2025-10-15 14:30:00"
         }

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         
         {
           "Id": "Rm074P0X9JCV"
         } 
          




### Example - Create a record of the Channels entity

This example creates a record of the `Channels` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Channels` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "googlecloudcreatedchannel",
         "IsPublic": true
         } 

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         
         {
         "Id": "C074MBW5N2G"
         } 
           




### Example - Create a record of the MessageReplies entity

This example creates a record of the `MessageReplies` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `MessageReplies` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ChannelId": "C076HCY07UN",
         "Text": "This is generated text",
         "ParentMessageId": "1717659095.881619"
         }

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         
         {
         "Id": "1717659183.033599",
         "ChannelId": C076HCY07UN,
         "ParentMessageId": "1717659095.881619"
         }
          




### Example - Update a record of the Calls entity

This example updates a record of the `Calls` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Calls` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "JoinURL": "https://example55.com/call/google-cloud",
           "Title": "title"
         }

  5. Set the entity ID to R074LB76Q5R. To set the entity ID, click **entityId** and then enter `R074LB76Q5R` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `R074LB76Q5R`.

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "null"
         }  




### Example - Update a record of the Messages entity

This example updates a record of the `Messages` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Messages` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Text": "Google Cloud Updated Message"
         }  

  5. Set the filterClause to ChannelId = 'C06UPA4KRD0' and Id = '1716369465.000129'. To set the filterClause, click **filterClause** and then enter `ChannelId = 'C06UPA4KRD0' and Id = '1716369465.000129'` in the **Default Value** field. 

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": null,
           "ChannelId": null
         }  




### Example - Update a record of the Users entity

This example updates a record of the `Users` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ProfileDisplayName": "Vaibhav"
         } 

  5. Set the entity ID to U06Q6VDJYSU. To set the entity ID, click **entityId** and then enter `U06Q6VDJYSU` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `U06Q6VDJYSU`.

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Id": null
         } 




### Example - Update a record of the Channels entity

This example updates a record of the `Channels` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Channels` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Purpose": "This is the one channel that will always include everyone."
         }

  5. Set the entity ID to C06MAP1JDSB. To set the entity ID, click **entityId** and then enter `C06MAP1JDSB` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `C06MAP1JDSB`.

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Id": "C06MAP1JDSB"
         }




### Example - Update a record of the MessageReplies entity

This example updates a record of the `MessageReplies` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `MessageReplies` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Text": "Updated Text"
         }

  5. Set the filterClause to ChannelId = 'C06UPA4KRD0' and Id = '1716369465.000129'. To set the filterClause, click **filterClause** and then enter `ChannelId = 'C06UPA4KRD0' and Id = '1716369465.000129'` in the **Default Value** field. 

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Id": null,
         "ChannelId": null,
         "ParentMessageId": null
         }   




### Example - Updates a record of the UserProfile entity

This example updates a record of the `UserProfile` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `UserProfile` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "CustomFields": "{\"Xf079082Q70B\": {\"value\": \"Patna Bihar\",\"alt\": \"\"}}",
           "Phone": "8767787654",
           "StatusText": "Long train Journey to work"
          }

If the integration is successful, the `Connector` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         
         }
         




## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
