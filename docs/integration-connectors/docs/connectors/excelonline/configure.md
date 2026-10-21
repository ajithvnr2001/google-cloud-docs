---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/excelonline/configure/
title: Excel Online \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:20.737026+00:00
---

# Excel Online  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/excelonline/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Excel Online

Use the Excel Online connector to perform operations on Excel Online.

## Before you begin

Configure your Google Cloud project, create your OAuth application and grant the required permissions. 

### Configure your Google Cloud project

Before using the Excel Online connector, do the following tasks in your Google Cloud project:

  * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
  * Enable the following services: 
    * `secretmanager.googleapis.com` (Secret Manager API)
    * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).




If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 

### Create Custom OAuth Application - Azure AD

  1. Log in to [Azure Portal](https://portal.azure.com).
  2. In the left-hand navigation pane, select Azure Active Directory, then applicationRegistrations.
  3. Click New registration.
  4. Enter a name for the application.
  5. Select the desired tenant setup: single or multi-tenant, and public or private use.
     * If you select the default option, "Accounts in this organizational directory only", you must set the AzureTenant connection property to the Id of the Azure AD Tenant when establishing a connection with the CData JDBC Driver for Microsoft Excel Online. Otherwise, the authentication attempt fails with an error.
     * If your application is for private use only, specify Accounts in this organization directory only.
     * If you want to distribute your application, choose one of the multi-tenant options.
  6. Set the redirect url to http://localhost:33333 (the driver's default) OR specify a different port and set CallbackURL to the exact reply URL you defined.
  7. Click Register to register the new application. An application management screen displays. Note the value in Application (client) ID as the OAuthClientId and the Directory (tenant) ID as the AzureTenant.
  8. Navigate to Certificates & Secrets and define the application authentication type. There are two types of authentication available: certificate (recommended) or client secret.
     * For certificate authentication: In Certificates & Secrets, select Upload certificate, then upload the certificate from your local machine.
     * For creating a new client secret: In Certificates & Secrets, select New Client Secret for the application and specify its duration. After the client secret is saved, Microsoft Excel Online displays the key value. Copy this value, as it is displayed only once. This value becomes the OAuthClientSecret.
  9. Select API Permissions > Add > Delegated permissions.
  10. Add the following application permissions: Sites.Read.All, Files.Read, Files.Read.All, Files.Read.Selected, Files.ReadWrite, Files.ReadWrite.All, Files.ReadWrite.AppFolder, Files.ReadWrite.Selected, and offline_access.
  11. Save your changes.
  12. If you have specified the use of permissions that require admin consent (such as the Application Permissions), you can grant them from the current tenant on the API Permissions page.



### Create Custom OAuth Application - Azure Service Principal

  1. Use the search bar to search for the Subscriptions service.
  2. Open the Subscriptions page.
  3. Select the subscription to which to assign the application.
  4. Open the Access control (IAM).
  5. Select Add > Add role assignment. Microsoft Excel Online opens the Add role assignment page.
  6. Assign your custom Azure AD application the role of Owner.



### Assign a role to the application

  1. To access resources in your subscription, you must assign a role to the application.
  2. Open the Subscriptions page by searching and selecting the Subscriptions service from the search bar.
  3. Select the subscription to assign the application to.
  4. Open the Access control (IAM) and select Add > Add role assignment to open the Add role assignment page.
  5. Select Owner as the role to assign to your created Azure AD app.



### Grant admin consent

  1. Log in to [Azure Portal](https://portal.azure.com)
  2. Navigate to App Registrations and find the custom OAuth application you created.
  3. Under API Permissions, click Grant Consent.



### Grant permissions for client credentials

  1. Log in to [Azure Portal](https://portal.azure.com)
  2. Navigate to App Registrations.
  3. Find the application you just created, and open API Permissions.
  4. Select the Microsoft Graph permissions. There are two distinct sets of permissions: Delegated and Application.
  5. Under Application Permissions, select the permissions you require for your integration. 



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
     1. **Connector** : Select **Excel Online** from the drop down list of available Connectors.
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
     8. **Azure Tenant** : The Microsoft Online tenant being used to access data. If not specified, your default tenant is used. 
     9. **Drive** : The ID of the drive. You can use the Drives and SharePointSites views to view all the sites and drives you have access to. 
     10. **Sharepoint URL** : The base URL of your Sharepoint Server. 
     11. **Show Shared Documents** : Whether or not to show shared documents. 
     12. **Workbook** : The name or Id of the workbook. 
     13. **Header** : Indicates whether or not the column names should be detected from the first row. 
     14. **Table** : Restricts the connection to a table containing a range of cells of a worksheet. Format: [{Workbook Name}_{Worksheet Name}!{Range}] 
     15. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     16. Click **Next**.
  5.      1. In the **Authentication** section, enter the authentication details. To understand how to configure these authentication details, see Configure authentication.
     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **Client ID** : The client ID used for requesting access tokens.
  * **Scope** : A comma-separated list of desired scopes.
  * **Client secret** : The client secret used for requesting access tokens.
  * **Authorization URL** : The authorization URL that you generate when you create an OAuth client. Enter the URL in the following format: `https://login.microsoftonline.com/AZURE_TENANT/oauth2/v2.0/authorize?prompt=consent`



### Excel Online - Web connection type

This section lists the sample values for the various fields that you configure when creating the Excel Online connection.

Fieldname | Details  
---|---  
Location | us-central1  
Connector | Excelonline  
Connector version | 1  
Connection Name | excelonline-gcp  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
Azure Tenant | 9b******-****-****-****-*********12  
Drive | b!p_648NCXwk6hJ1pfyn0SeFaithFnRM1JmYNur9asmHAs2k8qe5UsR5a1cX6luuD0  
Sharepoint URL | https://*****.sharepoint.com/  
Show Shared Documents | True  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Client ID | e89*****-****-****-****-*********b6  
Scopes | https://graph.microsoft.com/.default  
Client secret | CLIENT_SECRET  
Secret version | 1  
Authorization URL | https://login.microsoftonline.com/AZURE_TENANT/oauth2/v2.0/authorize?prompt=consent  
  
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

If you are using `Authorization code` authentication type and have made any configuration changes in your Azure Synapse application, you must re-authorize your Azure Synapse connection. To re-authorize a connection, perform the following steps:

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

The maximum Excel file size that the Excel Online connector can process is 25 MB.

The Excel Online connector can process 3 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Excel Online connection in an integration

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

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### Add Worksheet action

Adds a worksheet to an existing Excel Online workbook.

#### Input parameters of the AddWorksheet Action

Parameter Name  | Data Type | Required | Description  
---|---|---|---  
Title | String | True | Name of the worksheet.  
WorkbookId | String | True | The Id of the workbook. This ID must belong to the drive accessible with current connection properties.  
  
#### Output parameters of the AddWorksheet action

For example on how to configure the `AddWorksheet` action, see Examples.

## Examples

This section describes how to perform some of the actions in this connector.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Perform AddWorksheet action

This example adds a worksheet to an existing Excel Online workbook.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddWorksheet ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {   
         "WorkbookId": "01M7ENMYA2QJVY77NPOFD3WQIJ6PNNX5VL",
         "Title": "Worksheet_SP1"
         }

If the action is successful, the `AddWorksheet` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": "true",
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#workbookWorksheet",
      "@odata.type": "#microsoft.graph.workbookWorksheet",
      "@odata.id": "/drives('b%21p_648NCXwk6hJ1pfyn0SeFaithFnRM1JmYNur9asmHAs2k8qe5UsR5a1cX6luuD0')/items('01M7ENMYA2QJVY77NPOFD3WQIJ6PNNX5VL')/workbook/worksheets(%27%7BD9372F53-CB1B-4082-9E13-02E65C2FC233%7D%27)",
      "id": "{D9372F53-CB1B-4082-9E13-02E65C2FC233}",
      "name": "Worksheet_SP1",
      "position": "1",
      "visibility": "Visible"
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all Drives

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Drives from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all SharedDocuments

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select SharedDocuments from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all Workbooks

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Workbooks from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - Get Drives

  1. In the `Configure connector task` dialog, click `Entities`.
ect Drives from the `Entity` list. 
  2. Select the `Get` operation, and then click **Done**.
  3. Set the entity ID to Get single Drives. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `b!ZETdEU1T_UOBEzbgDmsvcubxvUaXbcJNrrNPM4LqokkwLC3zCRPiQLi2PBfCs9-v ` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Get SharedDocument

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select SharedDocuments from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to Get single SharedDocument. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `01BDTL6TS3OQ3HDXCKGREILDYKY47S7LEI` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Get Workbooks

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Workbooks from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to Get single Workbooks. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `01M7ENMYA2QJVY77NPOFD3WQIJ6PNNX5VL` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Delete data from Book

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Book 4567_Sheet1 from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to Delete Book 4567_Sheet1. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `5.0` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Create a Formula for Formulae_Sheet_List

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Formulae_Sheet_List from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
           "Excel_Sheet": "Old_Excel",
           "B": "=SUM(C8:D8)",
           "C": "6",
           "D": "6"
           }
           
         
         Running this example, returns a response similar to the following in the Connector
           task's connectorOutputPayload output variable:
         
         
           
         
         {
           "Id": 8.0
           } 
           




### Example - Create With_Headers

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Book 4567_Book4567_Sheet1 from the `Entity` list.
  3. Select the `Create` operation, and then click **Do ne**.
  4. In the **Da ta mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         

{ "Name": "workbooknew", "Type": "newly created", "Sl no": 5.0 }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": 6.0
           }
           




### Example - Create Without_Headers

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Book 4567_Book4567_Sheet1 from the `Entity` list.
  3. Select the `Create` operation, and then click **Do ne**.
  4. In the **Da ta mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         

{ "A": "6", "B": "Halo", "C": "Stardust" }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": 7.0
           } 
           




### Example - Update an Formula for Formulae_Sheet_List

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Formulae_Sheet_List from the `Entity` list.
  3. Select the `Update` operation, and then click **Do ne**.
  4. Set the entity ID to Update a Formulae_Sheet_List. To set the entity ID, in the **Da ta mapper** section of the **Tasks** , click **e ntityId** and then enter `8.0` in the given field.
  5. In the **Da ta mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         

{ "B": "=MAX(C8:D8)", "C": "7", "D": "10" }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    
      {   
      "Id": 8.0
      }
      




### Example - Update Without_Header

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Book 4567_Book4567_Sheet1 from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to Update a Book 4567_Book4567_Sheet1. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `7.0` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         
            {
             "B": "cosmically",
             "C": "interlinked"
           }  
           

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    
      {   
      "Id": 7.0
      }
      




### Example - Update_With_Header

  1. In the `Configure connector task` dialog, click `Entities`.
li>Select Book 4567_Book4567_Sheet1 from the `Entity` list. 
  2. Select the `Update` operation, and then click **Done**.
  3. Set the entity ID to Update a Book 4567_Book4567_Sheet1 To set the entity ID, in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `6.0` in the given field. 
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         
            {
             "Name": "updated",
             "Type": "newupdate"
           }
           

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    
      {   
      "Id": 6.0
      }
      




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
