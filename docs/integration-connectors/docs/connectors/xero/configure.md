---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/xero/configure/
title: Xero \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:36.054088+00:00
---

# Xero  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/xero/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Xero

This connector provides SQL access to your Xero backend.

## Before you begin

Before using the Xero connector, do the following tasks:

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




###  Xero configuration

The following tasks are required to configure Xero:

#### Set up a Xero account and Xero demo company

  1. Go to [Xero account](https://www.xero.com/signup/developers/) to signup for a free Xero account.
  2. Go to [Xero Demo Company](https://developer.xero.com/documentation/development-accounts) to enable the Xero demo company.



#### Generate OAuth2.0 client authentication details

  1. Login to the [Xero developer account](https://developer.xero.com/).
  2. Click **Sign Up** and follow the prompts. If you already have an account, log in with your credentials.

You will be directed to the Xero developer dashboard after logging in.

  3. Go to the [Xero developer portal](https://developer.xero.com/app/manage) from **My Apps** section in the Developer dashboard.
  4. Click **New App** or **Create a new app** to create a new app.
  5. Enter the required details for your app, such as the app name, description, company URL, privacy policy URL, terms of use URL, and callback URL.
  6. Make sure to select the appropriate app type and permissions required for your integration with Xero's demo company.

After you create your app, you will get the OAuth credentials, including a client ID and client secret.

  7. Store the client ID and client secret in a secured location for future use.

When you create your integration, select the necessary scopes carefully for each schema to ensure that your application has the appropriate permissions to access and utilize the required utilities.

For information about authentication and retrieving client ID and client secret, see [Retrieve client ID and client secret](https://developer.xero.com/documentation/guides/oauth2/client-credentials/#1-retrieve-your-client-id-and-client-secret).




#### Set up schema details

You can select the schema based on the module. The available schemas are ACCOUNTING, ASSETS, PAYROLLAUS, FILES, and PROJECTS. As we have five different modules, you have to create different connections for each module.

For information about scopes that you can specify when you create a connection, see [Scopes](https://developer.xero.com/documentation/guides/oauth2/scopes).

#### Set up authorization details

For information about setting up authorization URL, see [ Set up authorization URL](https://login.xero.com/{identity}/connect/authorize).

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
     1. **Connector** : Select **Xero** from the drop down list of available Connectors.
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
     8. **Schema** : The Xero API you want to access as a database schema. 
     9. **Tenant** : Sets the Xero organization to connect to. Can be a name or tenant ID. 
     10. **Verbosity Level** : Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates). 
     11. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     12. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Xero connection:

        * OAuth 2.0 Client Credentials 
        * OAuth 2.0 Auth Code Grant 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 Client Credentials**
    * **Client ID** : The client id provided by connector for the app you created.
    * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.


  * **OAuth 2.0 Auth Code Grant**
    * **Access token** : The access token used for authenticating requests with auth-code-flow-based connections.
    * **Client ID** : The client ID used for requesting access tokens.
    * **Client secret** : The client secret used for requesting access tokens.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.




## Connection configuration

This section lists the sample values for the various fields that you configure when creating the Xero connection.

### Accounting server connection type

Field name | Details  
---|---  
Region | us-central1  
Connector | Xero  
Connector version | 1  
Connection Name | google-cloud-xero-accounting-connection  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Schema | ACCOUNTING  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - Authorization code   
Client Id | CLIENT_ID   
Scopes | offline_access openid profile email accounting.transactions, accounting.reports.read, accounting.attachments, accounting.journals.read, accounting.settings, accounting.contacts, accounting.budgets.read   
Client secret | CLIENT_SECRET   
Secret Version | 1   
Authorization URL | https://login.xero.com/identity/connect/authorize   
  
### Assets server connection type

Field name | Details  
---|---  
Region | us-central1  
Connector | Xero  
Connector version | 1  
Connection Name | google-cloud-xero-assets-connection  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Schema | ASSETS  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - Authorization code   
Client Id | CLIENT_ID   
Scopes | assets.read, assets   
Client secret | CLIENT_SECRET   
Secret Version | 1   
Authorization URL | https://login.xero.com/identity/connect/authorize   
  
### Files server connection type

Field name | Details  
---|---  
Region | us-central1  
Connector | Xero  
Connector version | 1  
Connection Name | google-cloud-xero-files-connection  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Schema | FILES  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - Authorization code   
Client Id | CLIENT_ID   
Scopes | files, files.read   
Client secret | CLIENT_SECRET   
Secret Version | 1   
Authorization URL | https://login.xero.com/identity/connect/authorize   
  
### Payrollaus server connection type

Field name | Details  
---|---  
Region | us-central1  
Connector | Xero  
Connector version | 1  
Connection Name | google-cloud-xero-payroll-connection  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Schema | PAYROLLAUS  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - Authorization code   
Client Id | CLIENT_ID   
Scopes | payroll.employees, payroll.payruns, payroll.payslip, payroll.timesheets, payroll.settings   
Client secret | CLIENT_SECRET   
Secret Version | 1   
Authorization URL | https://login.xero.com/identity/connect/authorize   
  
### Projects server connection type

Field name | Details  
---|---  
Region | us-central1  
Connector | Xero  
Connector version | 1  
Connection Name | google-cloud-xero-projects-connection  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Schema | PROJECTS  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - Authorization code   
Client Id | CLIENT_ID   
Scopes | projects, projects.read   
Client secret | CLIENT_SECRET   
Secret Version | 1   
Authorization URL | https://login.xero.com/identity/connect/authorize   
  
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

## Use the Xero connection in an integration

## System limitations

The Xero connector can process 5 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. However, the number transactions that the Xero connector can process also depends on the constraints imposed by the Xero instance. For more information, see [Xero API rate limits](https://developer.xero.com/documentation/guides/oauth2/limits/#api-rate-limits). By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists some of the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### DownloadAttachment action

This action downloads an attachment.

#### Input parameters of the DownloadAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
Filename | String | No | Name of the attachment to download.  
Table | String | No | Name of the table from where we have to download the attachment.  
ObjectId | String | No | ObjectId of the attachment.  
  
#### Output parameters of the DownloadAttachment action

This action returns the status 200 (OK) if the download is successful.

To understand how to configure the `DownloadAttachment` action, see Action examples.

### UploadAttachment action

This action lets you upload an attachment.

#### Input parameters of the UploadAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
Filename | String | No | Name of the attachment to upload.  
ObjectId | String | No | ObjectId of the attachment.  
ContentType | String | No | Content type of the attachment.  
Table | String | No | Name of the table in which the attachment should be uploaded.  
Content | String | No | Content of the attachment  
  
#### Output parameters of the UploadAttachment action

This action returns the status 200 (OK) if the object upload is successful.

To understand how to configure the `UploadAttachment` action, see Action examples.

### ListAttachment Action

This action lets you list all the attachments of a table.

#### Input parameters of the ListAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
ObjectId | String | No | Object ID of the attachment.  
Table | String | No | Name of the table from which the attachments have to be listed.  
  
#### Output parameters of the ListAttachment action

This action returns the status 200 (OK) if the deletion is successful.

To understand how to configure the `ListAttachment` action, see Action examples.

### SendInvoiceMail action

This action let you send emails to an invoicer.

#### Input parameters of the SendInvoiceMail action

Parameter name | Data type | Required | Description  
---|---|---|---  
InvoiceId | String | No | Id of the invoice for which the mail should be sent.  
  
#### Output parameters of the SendInvoiceMail action

This action returns the status 200 (OK) if the move operation is successful.

To understand how to configure the `SendInvoiceMail` action, see Action examples.

### UploadFile action

This action lets you upload a file.

#### Input parameters of the UploadFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
Name | String | No | Name of the file to be uploaded.  
Content | String | No | File content to be uploaded.  
  
#### Output parameters of the UploadFile action

This action returns the status 200 (OK) if the object upload is successful.

To understand how to configure the `UploadFile` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Download an attachment

This example downloads an attachment.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Filename": "Xero_Test.txt",
         "Table": "Contacts",
         "ObjectId": "6a92a3ab-87cf-4f2f-8beb-ecb4f8ae4d41"
         }

If the action is successful, the `DownloadAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "Content": "Test content"
    }]




### Example - Upload an attachment

This example uploads an attachment.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Filename": "Xero_Test.txt",
         "ObjectId": "6a92a3ab-87cf-4f2f-8beb-ecb4f8ae4d41",
         "ContentType": "txt",
         "Table": "Contacts",
         "Content": "Test content upload attachment"
         }

If the action is successful, the `UploadAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": null,
    "AttachmentId": "5ba982a6-9294-45a7-bdda-5f134b0d69d5",
    "FileName": "Xero_Test.txt",
    "URL": "https://api.xero.com/api.xro/2.0/Contacts/6a92a3ab-87cf-4f2f-8bwb-fcb4f8ae4d41/Attachments/Xero_Test.txt",
    "MimeType": "text/plain",
    "ContentLength": "27",
    "IncludeOnline": null,
    "_": ""
    }, {
    "Success": null,
    "AttachmentId": null,
    "FileName": null,
    "URL": null,
    "MimeType": null,
    "ContentLength": null,
    "IncludeOnline": null,
    "_": null
    }]




### Example - List attachments

This example lists the attachments of the specified table.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ListAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ObjectId": "6a92a3ab-87cf-4f2f-8beb-ecb4f8ae4d41",
         "Table": "Contacts"
         }

If the action is successful, the `ListAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "AttachmentId": "5ba982a6-9294-45a7-bdda-5f134b0d69d5",
    "FileName": "Xero_Limit_Testing.txt",
    "URL": "https://api.xero.com/api.xro/2.0/Contacts/6a92a3ab-87cf-4f2f-8bwb-fcb4f8ae4d41/Attachments/Xero_Test.txt",
    "MimeType": "text/plain",
    "ContentLength": "27"
    }]




### Example - Send an invoice email

This example sends an email for the specified invoice.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendInvoiceMail` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "InvoiceId": "016a64c7-be0b-45a2-acae-13057fdf1566"
         }

If the action is successful, the `SendInvoiceMail` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Upload a file

This example uploads a file.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "Sample1.txt",
         "Content": "This is a sample file"
         }

If the action is successful, the `UploadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "FileId": "09039c7b-35a2-473d-aa79-16fe00b8d460",
    "Name": "Sample1.txt",
    "FolderId": "36e5115d-a9b6-4c22-baf3-40a8b28ee71d",
    "MimeType": "text/plain",
    "Size": 26.0,
    "User_Id": "c1e33cc9-eb61-45cb-9e46-3ea4121cbdc6",
    "User_Name": "test_user_1@test.com",
    "User_FirstName": "John",
    "User_LastName": "Smith",
    "User_FullName": "John Smith",
    "Created": "2023-12-18 17:38:53.01",
    "Updated": "2023-12-18 17:38:53.01"
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all records

This example lists all the records in the `Accounts` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Accounts` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). For example, `City='Bangalore'`. You can also specify multiple filter conditions by using the logic operators. For example, `City='Bangalore' and region='asia-south2'`. 



### Example - Get an invoice

This example gets an invoice with the specified ID from the `Invoices` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Invoices` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `1|016a64c7-be0b-45a2-acae-13057fdf1566` in the **Default Value** field. 

Here, `1|016a64c7-be0b-45a2-acae-13057fdf1566` is a primary key value in the `Invoices` entity.




### Example - Create an invoice

This example creates an invoice in the `Invoices` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Invoices` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Type": "ACCPAY",
         "ContactName": "ContactName1",
         "LineItem_Description": "LineItemDescription"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Id": "1|7b29efe9-dacd-47bb-85a6-0c0640ce25de"
         }




### Example - Update a record

This example updates a record in the `AssetTypes` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AssetTypes` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "BookDepreciationSetting_DepreciationRate": 10.0
         }

  5. Click **entityId** , and then enter `f8d43548-25b0-4cc3-8f59-d97106974fe8` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "AssetTypeId": "f8d43548-25b0-4cc3-8f59-d97106974fe8"
         }




### Example - Delete a file

This example deletes the file with the specified ID from the `Files` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Files` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `421c82f0-38fb-4074-a679-63b04c0d8832` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
