---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/dynamics365/configure/
title: Dynamics 365 \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:19.833764+00:00
---

# Dynamics 365  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/dynamics365/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Dynamics 365

The Dynamics 365 connector lets you connect to the live data from Dynamics 365 from your applications. You can access the Dynamics 365 data similar to how you access a database, and perform read, write, and update operations on the data. 

## Before you begin

Before using the Dynamics365 connector, do the following tasks:

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
     1. **Connector** : Select **Dynamics 365** from the drop down list of available Connectors.
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
     8. **Azure Tenant** : The Microsoft Online tenant being used to access data. If not specified, your default tenant will be used. 
     9. **Organization URL** : The URL to your Dynamics 365 organization. For instance, https://abc123.cloudax.dynamics.com/. 
     10. **ADFS Server** : The ADFS Server used for authentication. Only used with FinOpsOnPremise edition. 
     11. **Api Version** : Default Value is 9.0. This can be specified to access a new version of the API once it is released. This property only applies when Edition is set to either CustomerService, FieldService, Marketing, ProjectOperations or Sales. 
     12. **Cross Company** : Whether to pull data for all companies or just the user's default company. 
     13. **Edition** : The edition of Dynamics 365 being used. 
     14. **Include Formatted Values** : Indicates if columns that hold formatted values should be exposed. 
     15. **Include Navigation Properties** : Indicates if navigation properties should be included in the column listing. 
     16. **Use Dynamic Stored Procedures** : Indicating if dynamic stored procedures should be exposed. 
     17. **Verbosity Level** : Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates). 
     18. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     19. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Dynamics 365 connection:

        * OAuth 2.0 Auth Code Grant 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



## Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 Auth Code Grant**
    * **Access token** : The access token used for authenticating requests with auth-code-flow-based connections.
    * **Client ID** : The client ID used for requesting access tokens.
    * **Client secret** : The client secret used for requesting access tokens.



### Dynamics365 configuration

Complete the following steps to configure Dynamics365.

#### Create a user

  1. Log in to the Azure portal. 
  2. Create a new user and assign the system admin role. 



#### Create an application

  1. In the Azure portal, go to **Azure Active Directory** > **Application Registrations**. 
  2. Click **New registration**. 
  3. Enter a name for the application. 
  4. Specify **Single** > as the tenant setup. 
  5. Set the redirect URL to `http://localhost:33333` or a different port and set CallbackURL to the reply URL you defined. 
  6. Click **Register**. 
  7. Navigate to **Certificates & Secrets** and define the application authentication type. 
  8. Select a new client secret for the application and specify its duration. After the client secret is saved, Microsoft Office 365 displays the key value. 
  9. Copy the kay value, which you use as the client secret. 



#### Organization URL, edition, scope, and authorization URL

The following are the values for the organization URL, edition, scope, and authorization URL: 

  * Organization URL is the instance URL. 
  * You can select one of the following editions: Marketing, Sales, or Customer service. 
  * Scope: [org url]/.default 
  * Authorization URL: https://login.microsoftonline.com/TENANT_ID/oauth2/v2.0/authorize?prompt=consent 



#### Configure the redirect URL for connection authorization

  1. In the Azure portal, select the application from **App Registrations**. 
  2. In **Essentials** , add a redirect URL. 
  3. Add a platform, select **web** , and paste the redirect URL. 



### Dynamics365 Customerservice Edition connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Dynamics365  
Connector version | 1  
Connection Name | google-cloud-dynamic365-rest-customerservice  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Azure Tenant | AZURE_TENANT  
Organization URL | https://orgurl.com  
Edition | Customer Service  
Include Navigation Properties | True  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 2  
Client ID | CLIENT_ID  
Scopes | [Organization URL]/.default  
Client secret | SECRET  
Secret Version | 5  
Authorization URL | https://login.microsoftonline.com/TENANT_ID/oauth2/v2.0/authorize?prompt=consent   
  
### Dynamics365 Sales Edition connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Dynamics365  
Connector version | 1  
Connection Name | googlecloud-dynamic365-rest-sales  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Azure Tenant | AZURE_TENANT  
Organization URL | https://orgurl.com  
Edition | Sales  
Include Navigation Properties | True  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 2  
Client ID | CLIENT_ID  
Scopes | [Organization URL]/.default  
Client secret | SECRET|   
Secret Version | 5  
Authorization URL | https://login.microsoftonline.com/TENANT_ID/oauth2/v2.0/authorize?prompt=consent  
  
### Dynamics365 Marketing Edition connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Dynamics365  
Connector version | 1  
Connection Name | google-dynamic365-rest-marketing  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Azure Tenant | AZURE_TENANT  
Organization URL | https://orgurl.com  
Edition | Marketing  
Include Navigation Properties | True  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 2  
Client ID | CLIENT_ID  
Scopes | [Organization URL]/.default  
Client secret | SECRET  
Secret Version | 5  
Authorization URL | https://login.microsoftonline.com/TENANT_ID/oauth2/v2.0/authorize?prompt=consent  
  
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

The Dynamics 365 connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the products

This example lists all the products in the `Products` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Products` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



### Example - Get a lead

This example gets a lead with the specified ID from the `Leads` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Leads` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `c5233ad8-a1a4-ee11-a568-000d3ac9f67f` in the **Default Value** field. 

Here, `c5233ad8-a1a4-ee11-a568-000d3ac9f67f` is a unique record ID in the `Leads` entity.




### Example - Create a lead

This example creates a lead in the `Leads` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Leads` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "fullname": "nameadded1703832358758",   
         "subject": "test subject",   
         "firstname": "firstname1703832358766",   
         "lastname": "lastname1703832358767"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
         "leadid": "220166e8-15a6-ee11-a569-002248d5dd6b"
         }]




### Example - Update an order

This example updates a record in the `SalesOrder` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesOrder` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "name": "Nameupdated1704863189087"
          }

  5. Click **entityId** , and then enter `580775a4-17aa-ee11-a568-000d3ac9f67f` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
         "salesorderid": "580775a4-17aa-ee11-a568-000d3ac9f67f"
         }]




### Example - Delete a contact

This example deletes the contact with the specified ID in the `Contacts` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Contacts` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `524f543b-3ea5-ee11-a568-000d3ac9f67f` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

## Use the Dynamics 365 connection in an integration

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
