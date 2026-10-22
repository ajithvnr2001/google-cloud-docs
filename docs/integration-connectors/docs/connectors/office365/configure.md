---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/office365/configure/
title: Office365 \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:06.268618+00:00
---

# Office365  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/office365/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Office365

The Office365 connector lets you connect to a Office365 instance and perform the supported operations.

## Before you begin

Before using the Office365 connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




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
     1. **Connector** : Select **Office365** from the drop-down list of available connectors.
     2. **Connector version** : Select the connector version from the drop-down list of available versions.
     3. In the **Connection Name** field, enter a name for the connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lowercase.
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
     8. **Azure Tenant** : The Microsoft Online tenant being used to access data. If not specified, your default tenant will be used. 
     9. Optionally, click **\+ Add label** to add a label to the connection in the form of a key/value pair.
     10. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Office365 connection:

        * OAuth 2.0 Auth Code Grant

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

To generate client credentials and authorize the connection, you must complete the following steps: 

  1. Register your app and obtain the client ID and client secret.
  2. Specify the credentials in Google Cloud.
  3. Authorize the connection in Google Cloud.
  4. Add the redirect URL to your app.



#### Register your app and obtain the clientId and client secret

  1. Log in to the [Azure Portal](https://portal.azure.com/).
  2. In **Azure Services** , select **App Registrations** and then **New registration**.
  3. Enter an application name.
  4. Specify who can use the application or access the API.
  5. Set the redirect url to `http://localhost:33333` or specify a different port and set `CallbackURL` to the reply URL you defined.
  6. Click **Register**.
  7. Save the Application (client) ID and the Directory (tenant) ID for later use.
  8. Navigate to **Certificates & Secrets** section and define the application authentication type. 
     * For certificate authentication, select **Upload certificate** , and then upload the certificate from your local machine.
     * For client secret authentication, select **New Client Secret** and specify its duration. After the client secret is saved, copy the key value, which you will use as the client secret.
  9. In **API Permissions** , select **Microsoft Graph API** and then select the required application permissions and delegated permissions. 
  10. Click **Save**.



#### Provide owner access to the application

If the access token expires frequently, you can provide owner access to the application. This allows you to refresh the access token without having to reauthorize the connection.

  1. Log in to the [Azure Portal](https://portal.azure.com/).
  2. In **Azure Active Directory** , select **App registrations**.
  3. Click on the application name.
  4. Naviage to the **Owners** section.
  5. Click **Add owners** and select the owner to be added.



#### Specify the credentials in Google Cloud

When you create the connection in Integration Connectors , you must specify the following details: 

In the **Authentication** section, enter the following details:

  * **Client ID** : Enter the client ID that is used for requesting access tokens.
  * **Scopes** : Enter a comma-separated list of desired scopes.
  * **Client secret** : Enter the secret that contains the client secret for the connected app that you created.
  * **Secret version** : Secret version for the secret selected.
  * **Authorization URL** : The authorization URL that you generate when you create an OAuth client. Enter the URL in the following format: `https://login.microsoftonline.com/TENANT_IDENTIFIER/oauth2/v2.0/authorize?prompt=consent`. For example, `https://login.microsoftonline.com/9bxxxxxxxxx8112/oauth2/v2.0/authorize?prompt=consent`. 



#### Authorize the connection in Google Cloud

  1. In the [Connections page](https://console.cloud.google.com//connectors/connections), locate the newly created connection. 

The **Status** for the new connector will be **Authorization required**.

  2. Click **Authorization required**. 

This shows the **Edit authorization** pane.

  3. Copy the **Redirect URI** value to your external application. For more information, see Add the redirect URL to your app.
  4. Verify the authorization details.
  5. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




#### Add the redirect URL to your app

  1. In the Azure portal, click **Azure services > App registrations**.
  2. Click on your App name.
  3. Click add redirect URI.
  4. Click **Add a platform**.
  5. In the **Web** dialog, paste the redirect URI that you copied when you authorized the connection in Google Cloud.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

#### Connection example

The following table lists the sample configuration values for the Office365 connection:

Field name  | Details   
---|---  
Region  | us-central1   
Connector  | Office 365   
Connector version  | 1   
Connection Name  | office365-google-cloud-con   
Service Account  | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com   
AzureTenant | AZURE_TENANTID  
Minimum number of nodes  | 2   
Maximum number of nodes  | 2   
Client ID  | CLIENT_ID   
Scopes  | offline_access   
Group.Read.All   
Group.ReadWrite.All   
user.read   
user.readwrite.all   
calendars.readwrite   
contacts.readwrite   
mail.readwrite   
Files.ReadWrite.All   
Client secret  | CLIENT_SECRET   
Secret Version  | 1   
Authorization URL  | https://login.microsoftonline.com/9bxxxxxxxxx8112/oauth2/v2.0/authorize   
  
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

The Office365 connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### CancelEvent action

This action lets you cancel an event.

#### Input parameters of the CancelEvent action

Parameter name | Data type | Required | Description  
---|---|---|---  
EventId | String | Yes | ID of the event.  
UserId | String | No | ID of the user.  
UserPrincipalName | String | No | The username for which the license needs to be assigned.  
Comment | String | No | A comment to include.  
  
For example on how to configure the `CancelEvent` action, see Action examples.

### MoveMail action

This action lets you move an email.

#### Input parameters of the MoveMail action

Parameter name | Data type | Required | Description  
---|---|---|---  
MessageId | String | Yes | The Email Id.  
DestinationId | String | Yes | ID of the destination folder where the email will be moved to.  
  
For example on how to configure the `MoveMail` action, see Action examples.

### AssignLicense action

This action lets you assign a license.

#### Input parameters of the AssignLicense action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserId | String | No | The ID of the user for which license need to be assigned.  
UserPrincipalName | String | No | The username for which the license needs to be assigned.  
AddLicenseSkuId | String | No | The unique identifier for the SKU.  
DisabledPlans | String | No | A collection of the comma separated unique identifiers for plans that have been disabled.  
RemoveLicenses | String | No | A collection of comma separated IDs that identify the licenses to remove.  
  
For example on how to configure the `AssignLicense` action, see Action examples.

### ForwardEvent action

This action lets you forward an event.

#### Input parameters of the ForwardEvent action

Parameter name | Data type | Required | Description  
---|---|---|---  
EventId | String | Yes | The ID of the event.  
UserId | String | No | ID of the user.  
UserPrincipalName | String | No | The username for which license needs to be assigned.  
Comment | String | No | A comment to include.  
ToRecipients | String | Yes | A semicolon separated list of recipient emails.  
  
For example on how to configure the `ForwardEvent` action, see Action examples.

### UploadFile action

This action lets you upload a file.

#### Input parameters of the UploadFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
FileName | String | No | Name of the file you need to upload content to.  
LocalFile | String | No | Local file containing the content to be uploaded.|   
ContentStream | String | No | The content as input stream to be uploaded when localpath or folderpath isn't specified.  
ParentId | String | Yes | ID of the folder where the current item is.  
Content | String | No | File content to be uploaded.  
  
For example on how to configure the `UploadFile` action, see Action examples.

### DownloadFile action

This action lets you download a file.

#### Input parameters of the DownloadFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
FileId | String | Yes | The ID of the file which you want to download.  
DownloadTo | String | No | Where to store the file.  
Encoding | String | No | The FileData input encoding type. The allowed values are NONE, BASE64, and the default value is BASE64.  
FileStream | String | No | An instance of an output stream where file data is written to. Only used if DownloadTo isn't specified.  
  
For example on how to configure the `DownloadFile` action, see Action examples.

### CreateFolder action

This action lets you create a folder.

#### Input parameters of the CreateFolder action

Parameter name | Data type | Required | Description  
---|---|---|---  
ParentId | String | No | The ID of the folder where the current item is.  
FolderName | String | Yes | Name of the folder to be created.  
  
For example on how to configure the `CreateFolder` action, see Action examples.

### SendMail action

This action lets you send an email.

#### Input parameters of the SendMail action

Parameter name | Data type | Required | Description  
---|---|---|---  
ToRecipients | String | No | The recipients for whom the email should be sent.  
Content | String | No | Email Content.  
Subject | String | No | The Email subject.  
Id | String | No | The ID of the message to be sent (this is optional). The user can either use an existing email ID or send a new email by optionally filling the other fields.  
Attachments | String | No | The file attachments. Specify file attachments in the following format:  `filename1,filecontent1;filename2,filecontent2`. Each file content can be either be a BASE64 data, or the path of a local file with the @ character before it.  
FileName | String | No | The Recipients Specify recipients in the following order.  
LocalFile | String | No | The file containing the content of the attachment.  
ContentBytes | String | No | Content of the attachment encoded to BASE64.  
CCRecipients | String | No | A semicolon separated values of the recipients in CC.  
SenderEmail | String | No | The email address on who's behalf email needs to be sent. Set this if you want to send email on behalf of another user's account.  
FromEmail | String | No | The email address of the User from which email needs to be sent. Set this if you want to send email from other user's account.  
ContentType | String | No | The content type of the email body.The allowed values are text, html. The default value is text.  
  
For example on how to configure the `SendMail` action, see Action examples.

### ForwardMail action

This action lets you forward an email.

#### Input parameters of the ForwardMail action

Parameter name | Data type | Required | Description  
---|---|---|---  
MessageId | String | Yes | ID of the email.  
ToRecipients | String | Yes | A semicolon separated list of recipients emails.  
Comment | String | No | Content in addition to the original message.  
  
For example on how to configure the `ForwardMail` action, see Action examples.

### DownloadEmail action

This action lets you download an email.

#### Input parameters of the DownloadEmail action

Parameter name | Data type | Required | Description  
---|---|---|---  
MessageId | String | Yes | Id of the message which you want to download.  
Encoding | String | No | The file data input encoding type.  
DownloadTo | String | No | Where to store the file.  
FileStream | String | No | An instance of an output stream where file data should be written to. This value is used only if `DownloadTo` isn't provided.  
  
For example on how to configure the `DownloadMail` action, see Action examples.

### DownloadAttachments action

This action lets you download the attachments of an email.

#### Input parameters of the DownloadAttachments action

Parameter name | Data type | Required | Description  
---|---|---|---  
MessageId | String | Yes | Id of the email from which you want to get the attachments.  
Encoding | String | No | The FileData input encoding type. The allowed values are NONE, BASE64.  
DownloadTo | String | No | Where to store the attachments. If not specified, it returns the content bytes of the attachment. This value is required if `MessageId` is specified.  
AttachmentId | String | No | Id of the attachment you want to download. Returns all the attachments of the email if not specified.  
UserId | String | No | Id of the User. This will work only if the authenticated user has Admin permissions.  
FileStream | String | No | An instance of an output stream where file data is written to. Only used if `DownloadTo` isn't provided.  
  
For example on how to configure the `DownloadAttachments` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Cancel an event

This example cancels an event with the specified ID.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CancelEvent` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "EventId": "AAMkAGQ2NGQwNWU0LTU2MjUtNDZmNy04NGQzLTY4ZmU4Y2E4Y2JiNgBGAAAAAACvzgT4b7T_Qav2LM_bB-GAAA=",   
         "Comment": "Canceled due to rain"
         }

If the action is successful, the `CancelEvent` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Assign and remove a license

This example assigns and removes licenses for the specified user.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AssignLicense` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "UserID": "ee58217f-b22e-4300-a876-53db3c71a87b",   
         "AddLicenseSkuId": "c42b9cae-ea4f-4ab7-9717-81576235ccac",   
         "RemoveLicenses": "c42b9cae-ea4f-4ab7-9717-81576235ccac"
         }

If the action is successful, the `AssignLicense` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Forward an event

This example forwards an event.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ForwardEvent` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "EventId": "AAMkAGQ2NGQwNWU0LTU2MjUtNDZmNy04NGQzLTY4ZmU4Y2E4Y2JiNgBGAAAAAACvzgT4b7T_Qav2LM_bB-PKBwAhfASdetQfTZ3pESzwWnAbAAAAAAENAAAhfASdetQfTZ3pESzwWnAbAAA_CxGjAAA=",   
         "Comment": "forwarded due to rain",   
         "ToRecipients": "test99@example.com"
         }

If the action is successful, the `ForwardEvent` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Upload a file

This example uploads a file.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "FileName": "Document1234.docx",   
         "ParentId": "01VCU572N6Y2GOVW7725BZO354PWSELRRZ",   
         "Content": "test"
         }

If the action is successful, the `UploadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Id": "01VCU572JX6F3L3NKLQVB2BXETRHLEAUAY",   
    "@test.context": "https://example.com/v1.0/$metadata#users('7954f490-5a43-083fc215362a')/drive/items('01VCU5BZO354PWSELRRZ')/test/$entity",   
    "@example.downloadurl": "https://example.com/test/admin123/_layouts/15/download.aspx?UniqueId=bd76224r7-4........
    "Status": "Success"
    }] 




### Example - Download a file

This example downloads a file.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "FileId": "01VCU572LDCGQYZOSMHZDZGN5HCXS5P6EP"
         }

If the action is successful, the `DownloadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success",
    "FileData": "UEsDBBQAAAAIAEoTdVdSWj6GTAEAABoFAAATAAAAWNdLnhtbLWUTU7DMBCFr2J"
    }]




### Example - Create a folder

This example creates a folder.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateFolder` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ParentId": "01VCU572N6Y2GOVW7725BZO354PWSELRRZ",   
         "FolderName": "outbox1234"
         }

If the action is successful, the `CreateFolder` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Send an email

This example sends an email to the specified recipients.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendMail` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ToRecipients": "test097@example.com",   
         "Content": "Testing",   
         "Subject": "Test subject",   
         "FileName": "Google"
         }

If the action is successful, the `SendMail` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Forward an email

This example forwards an email.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ForwardMail` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "MessageId": "AAMkAGQ2NGQwNWU0LTU2MjUtNDZmNy04NGQzLTY4ZmU4Y2E4Y2JiNgBGAAAAAACvzgT4b7T_Qav2LM_bB-PKBwAhfASdetQfTpESzwWnAbAAA0sITVAAA=",   
         "ToRecipients": "test097@example.com",   
         "Comment": "forwarded message"
         }

If the action is successful, the `ForwardMail` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Download an email

This example downloads an email.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadEmail` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "MessageId": "fTZ3pESzwWnAbAAAAAAEJAAAhfASdetQfTZ3pESzwWnAbAAA0sITVAAA="
         }

If the action is successful, the `DownloadEmail` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success",   
    "FileData": "RnJvbTogRk5VIExOVSA8YWRtaW4xMjNANzNzY21nLm9ubWljcm9zb2Z0LmNvbT4NClRvOiB0ZXN0IDx0ZXN0.......
    }]




### Example - Download attachments

This example downloads attachments.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadAttachments` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         {"MessageId": "PKBwAhfASdetQfTZ3pESzwWnAbAAAAAAEJAAAhfASdetQfTZ3pESzwWnAbAAA0sITWAAA=",   
         "DownloadTo": "My files/Office355/reports/"}
         }

If the action is successful, the `DownloadAttachments` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Id": "AAMkAGQ2NGQwNWU0LTU2MjUtNDZmNy04NGQzLTY4ZmU4Y2E4Y2JiNgBGTWAAABEgAQAF3EBDrnTc1Cj8akAYrJjdM=",
    "Name": "demoattachment.docx",
    "ContentBytes": "UEsDBBQAAAAIALskYlcppqeszQEAAHQJAAATAAAAWAAAI3RyYXNoXS8wMDAwLmRhdP........",
    "LastmodifiedDatetime": "2023-11-21T10:09:09Z",
    "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "FileData": null,
    "json:repeatelementorder#": null,
    "size": "23575",
    "isinline": "false
    }]




## Use the Office365 connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).



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
