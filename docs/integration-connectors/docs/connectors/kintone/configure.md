---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/kintone/configure/
title: Kintone \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:33.577942+00:00
---

# Kintone  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/kintone/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Kintone

The Kintone connector lets you perform insert, delete, update, and read operations on Kintone database.

## Before you begin

Before using the Kintone connector, do the following tasks:

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
     1. **Connector** : Select **Kintone** from the drop down list of available Connectors.
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
     8. **Allow Special Characters** : Determines whether or not to allow special characters. If true special characters will not be replaced. 
     9. **Check For Subtables In** : A comma-separated list of Kintone apps to retrieve subtables from. 
     10. **Guest Space Id** : Restrict query results to a guest space. 
     11. **Number Map To Double** : Determines whether or not to change the datatype of number fields from decimal to double. 
     12. **Subtable Separator Character** : The character used for dividing tables from subtables in the format tablename + char + subtable. 
     13. **Use Code For Field Name** : Determines whether to use Label or Code for Field Name. 
     14. **Use Cursor** : Boolean determining if cursors should be used to retrieve records. 
     15. **User Defined Views** : A filepath pointing to the JSON configuration file containing your custom views. 
     16. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     17. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     18. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **NEXT**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Kintone connection:

     * Username and password 
     * API Token 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.
    * **Basic Auth Password** : The additional password required for domains using basic authentication.
    * **Basic Auth User** : The additional username required for domains using basic authentication.


  * **API Token**
    * **API Token** : Secret Manager Secret containing the API Token for authentication.
    * **App Id** : The AppId used along with the APIToken for authentication.



### Connection configuration samples

This section lists the sample values for the various fields that you configure when you create a Kintone connection.

#### Basic auth connection type

For the basic authentication connection type, use the username and password that you get when you create the new Kintone instance.

Field name | Details  
---|---  
Location | europe-west1  
Connector | Kintone  
Connector version | 1  
Connection Name | kintone-conn-free-trial  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Check For Subtables in | *  
Use Code For Field Name | Yes  
Use Cursor | Yes  
Minimum number of nodes | 2  
Maximum number of nodes | 2  
Destination Type(Server) | Host address  
Host address | https://tx3tdonei8na.kintone.com  
Username | USERNAME  
Password | PASSWORD  
Secret version | 2  
  
#### API token connection type

For information about how to get the API token, see [API access token](https://get.kintone.help/k/en/user/app_settings/api_token.html). 

Field name | Details  
---|---  
Location | europe-west1  
Connector | Kintone  
Connector version | 1  
Connection Name | kintone-api-token-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Check For Subtables in | *  
Subtable Separator Character | _  
Use Code For Field Name | Yes  
Use Cursor | Yes  
Minimum number of nodes | 2  
maximum number of nodes | 50  
Destination Type(Server) | Host address  
Host address | https://tx3tdonei8na.kintone.com  
API Token | API_Token_PostmanApplication  
AppId | 4  
Secret version | 1  
  
#### OAuth connection type

This section lists the sample values for the various fields that you configure when you create a Kintone connection using OAuth and provides information about how to create a Kintone account and configure it.

##### Kintone account creation and configuration

  * For information about how to create a Kintone account, see [Create a free Kintone Instance](https://get.kintone.help/store/en/trial/first.html).
  * For information about how to add an OAuth client, see [Adding OAuth client](https://kintone.dev/en/docs/common/authentication/how-to-add-oauth-clients/).
  * For information about how to create a new Space, see [Create a Space](https://get.kintone.help/k/en/user/space/add_space.html).
  * For information about how to create an app, see [Create an app from scratch](https://get.kintone.help/k/en/user/create_app/tutorial.html).
  * For information about how to create a thread, see [Create a thread](https://get.kintone.help/k/en/user/space/add_thread.html).

Field name | Details  
---|---  
Location | europe-west1  
Connector | Kintone  
Connector version | 1  
Connection Name | kintone-oauth-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Check For Subtables in | *  
Subtable Separator Character | _  
Use Code For Field Name | Yes  
Use Cursor | Yes  
Minimum number of nodes | 2  
maximum number of nodes | 50  
Destination Type(Server) | Host address  
Host address | https://tx3tdonei8na.kintone.com  
Client ID | CLIENT_ID  
Scopes | k:app_settings:write k:app_settings:read k:app_record:read k:app_record:write k:file:read k:file:write  
Client Secret | CLIENT_SECRET  
Secret version | 2  
  
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

The Kintone connector can process 5 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### AppsDeployStatus action

This action gets app deployment statuses

#### Input parameters of the AppsDeployStatus action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
AppIds | String | Yes | The Id of the app. This can be a list of comma-separated Ids.  
GuestSpaceId | String | No | This parameter is used for apps that are in the guest space. Do not add this parameter if the connection property GuestSpaceId is specified in the connection string.  
  
For example on how to configure the `AppsDeployStatus` action, see Action examples.

### CreateApp action

This action creates apps.

#### Input parameters of the CreateApp action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Name | String | Yes | Specify the name of the application in less than 64 characters.  
Space | String | No | The Id of the space. Do not specify this if the connection property GuestSpaceId is set in the connection string.  
ThreadId | String | No | The Id of the space. Do not specify this if the connection property GuestSpaceId is set in the connection string.  
IsGuestSpace | Boolean | No | This is a boolean value that indicates whether the Space parameter is a normal space or a guest space. Set this value to true for guest spaces. The default value is false.  
  
For example on how to configure the `CreateApp` action, see Action examples.

### DeleteGuests action

This action let users Delete Guests.

#### Input parameters of the DeleteGuests action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Guests | String | Yes | A list of email addresses of Guest users. Up to 100 Guests can be deleted.  
  
For example on how to configure the `DeleteGuests` action, see Action examples.

### DeployApps action

This action lets you deploy apps.

#### Input parameters of the DeployApps action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
AppId | String | Yes | The App Id. This can be a list of comma-separated Ids.  
Revision | String | No | Specify the revision of the setting that reflects the operational environment. If the specified revision is not up to date, the request will fail.  
Revert | Boolean | No | If you want to cancel the change to the application settings, set this to true. The default value is false.  
GuestSpaceId | String | No | This parameter is used for apps that are in the guest space. Do not add this parameter if the connection property GuestSpaceid is specified in the connection string.  
  
For example on how to configure the `DeployApps` action, see Action examples.

### DownloadFile action

This action let users download files from an attachment field in an app.

#### Input parameters of the DownloadFile action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
FileKey | String | Yes | The Id of the file.  
HasBytes | Boolean | No | Whether to download content as bytes. The valid values are `true` or `false`. If set to `true`, the file is downloaded as a `Base64` encoded string. By default, the `HasBytes` field is set to `false`.  
  
For example on how to configure the `DownloadFile` action, see Action examples.

### UpdateAssignees action

This action let users update assignees.

#### Input parameters of the UpdateAssignees action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
AppId | String | Yes | The App Id.  
RecordId | String | Yes | RecordId  
Assignees | String | Yes | The user codes of the assignees. If empty, no users will be assigned. The maximum number of assignees is 100.  
Revision | String | No | The revision number of the record before updating the assignees. If the specified revision is not the latest revision, the request will result in an error.  
GuestSpaceId | String | No | This parameter is used for apps that are in the guest space. Do not add this parameter if the connection property GuestSpaceId is specified in the connection string.  
  
For example on how to configure the `UpdateAssignees` action, see Action examples.

### AddGuests action

This action let users add Guests.

#### Input parameters of the AddGuests action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Name | String | false | The display name of the user. Must be between 1 - 128 characters.  
Code | String | No | The email address (log in name) of the Guest user.  
Password | String | No | The log in password of the Guest user. It must be alphanumeric.  
Timezone | String | No | The timezone of the Guest user.  
Locale | String | No | The language settings of the Guest user. Available values are auto, en, zh, ja. If not provided, auto will be set as default.  
Image | String | No | The profile image of the Guest user. Specify a fileKey of an uploaded file.  
SurNameReading | String | No | The Phonetic Surname settings of the Guest User. The maximum limit is 64 characters.  
GivenNameReading | String | No | The Phonetic Given Name settings of the Guest User. The maximum limit is 64 characters.  
Company | String | No | The Company name to display on the Guest User's profile.  
Division | String | No | The Department name to display on the Guest User's profile.  
Phone | String | No | The Phone number to display on the Guest User's profile.  
CallTo | String | No | The Skype Name of the Guest user.  
GuestsAggregate | String | No | The Guests Aggregate.  
  
For example on how to configure the `AddGuests` action, see Action examples.

### UploadFile action

This action lets you upload a file.

#### Input parameters of the UploadFile action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
FileName | String | Yes | The name you would like to give the document. If none is specified, the file name specified in the FullPath input will be used.  
Content | String | No | The content as InputStream to be uploaded when FullPath is not specified.  
ContentBytes | String | No | Bytes content (as a Base64 string) to upload as a file. Use this to upload binary data.  
AppId | String | No | The Kintone App Id. This is required when AttachToApp set to true.  
HasBytes | Boolean | No | Whether to upload content as bytes. The valid values are `true` or `false`. If set to `true`, the file content should be `Base64` encoded string. By default, the `HasBytes` field is set to `false`.  
  
### AddThreadComment action

This action let users add comments in thread

#### Input parameters of the AddThreadComment action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
SpaceId | Integer | Yes | The Id of the space.  
ThreadId | Integer | Yes | The Id of the thread.  
Text | String | No | The comment contents. A line break can be specified by LF. The maximum characters of the comment is 65535. Required, if files is not set.  
Mentions | String | No | An array including mentions, that notify other Kintone users.  
Files | String | No | An array including data of attachment files. The maximum number of the files is 5. Required, if text is not set.  
  
For example on how to configure the `AddThreadComment` action, see Action examples.

### UpdateThread action

This action let you update a thread

#### Input parameters of the UpdateThread action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ThreadId | Integer | Yes | The Thread ID. The Thread ID can be found in the URL of the Thread.  
Name | String | No | The new name of the Thread. Must be between 1 - 128 characters. The name will not be updated if this parameter is ignored. The Thread name of single threaded Spaces cannot be updated.  
Body | String | No | The contents of the Thread body.  
  
For example on how to configure the `UpdateThread` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Get app deployment status

This example gets the app deployment status.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AppsDeployStatus` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "AppIds": "4"
         }

If the action is successful, the `AppsDeployStatus` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "AppId": "4",   "Status": "SUCCESS",   "success": "true"
    }




### Example - Create an app

This example creates a new app.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateApp` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "NewApp"
         }

If the action is successful, the `CreateApp` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "AppId": "20",   "Revision": "2",   "Success": "true"
    }]




### Example - Deploy an app

This example deploys an app

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeployApps` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "AppId": "19",   "Revision": "2"
         }

If the action is successful, the `DeployApps` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Download a file

This example downloads a file present in an app.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "FileKey": "2024022706351283F683AABB3A4FA09AF1D28049"
         }

If the action is successful, the `DownloadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "Content": "Record number, Number, Text\n49, 162, Hello"
    }]




### Example - Update an assignee

This example updates an assignee.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateAssignees` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "FileKey": "2024022706351283F683AABB3A4FA09AF1D28049"
         }

If the action is successful, the `UpdateAssignees` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "Content": "Record number, Number, Text\n49, 162, Hello"
    }]




### Example - Add a guest

This example adds a guest.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddGuests` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "GuestsAggregate": "[{\"name\":\"Testuser\",\"code\":\"testuser1@test.com\",
         \"password\":\"test@123\",\"timezone\":\"America/Los_Angeles\",
         \"company\":\"Company Name\",\"division\": \"Sales\",
         \"callto\":\"SkypeCallTo\",\"locale\":\"en\"}]"
         }

If the action is successful, the `AddGuests` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Delete a guest

This example deletes a guest.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteGuests` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Guests": "[\"testuser1@test.com\"]"
         }

If the action is successful, the `DeleteGuests` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Upload a file

This example shows how to upload a file.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "FileName": "GoogleCloud_Upload_File.txt",
         "AppId": "9",
         "Content": "Hello"
         }

If the action is successful, the `UploadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "FileKey": "4e3b6ca9-0028-41c6-9662-53b151ef9b35",
    "Success": "true",
    "Id": null,
    "Revision": null
    }]




### Example - Add a thread comment

This example shows how to add a thread comment.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddThreadComment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "SpaceId": 1.0,
         "ThreadId": 1.0,
         "Text": "Test Comment"
         }

If the action is successful, the `AddThreadComment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Id": "3",
    "Success": "true"
    }]




### Example - Update a thread

This example shows how to update a thread.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateThread` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ThreadId": 1.0,
         "Name": "updated thread"
         }

If the action is successful, the `UpdateThread` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all apps

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Apps` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



You can perform the List operation on the Record and Comments entities as well.

### Example - Get an app

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Apps` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `4` in the **Default Value** field. 

Here, `4` is a unique record ID in the `Apps` entity.




You can perform the Get operation on the following entities as well: Deploy, Record, FormFields, FormLayout, Views, GeneralSettings, ProcessManagement, AppPermission, RecordPermission, FieldPermission, GeneralNotification, PerRecordNotification, ReminderNotification, GraphSettings, ActionSettings, Space, SpaceMembers

### Example - Delete a record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Record` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `6` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

You can perform the Delete operation on the Comments entities as well.

### Example - Create a record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Record` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Text": "HelloDemo"
         }

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
         "RecordId": 29.0
         }




### Example - Update a record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Record` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Text_area": "updatedemo"
         }

  5. Click **entityId** , and then enter `22` in the **Default Value** field. 

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
         "RecordId": "22"
         }




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
allow_special_characters | BOOLEAN | False | Determines whether or not to allow special characters. If true special characters will not be replaced.   
check_for_subtables_in | STRING | True | A comma-separated list of Kintone apps to retrieve subtables from.   
guest_space_id | STRING | False | Restrict query results to a guest space.   
number_map_to_double | BOOLEAN | False | Determines whether or not to change the datatype of number fields from decimal to double.   
subtable_separator_character | STRING | True | The character used for dividing tables from subtables in the format tablename + char + subtable.   
use_code_for_field_name | BOOLEAN | False | Determines whether to use Label or Code for Field Name.   
use_cursor | BOOLEAN | False | Boolean determining if cursors should be used to retrieve records.   
user_defined_views | STRING | False | A filepath pointing to the JSON configuration file containing your custom views.   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the Kintone connection in an integration

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
