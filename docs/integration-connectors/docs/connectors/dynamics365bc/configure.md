---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/dynamics365bc/configure/
title: Dynamics 365 Business Central \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:40.209017+00:00
---

# Dynamics 365 Business Central  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/dynamics365bc/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Dynamics 365 Business Central

The Dynamics 365 Business Central connector lets you perform insert, delete, update, and read operations on Dynamics 365 Business Central Data.

## Supported versions

This connector supports the following versions: 

* Dynamics 365 Business Central Cloud, Production Environment Version - 24.5.23489.26544
* Dynamics 365 Business Central, On-premise Version - Dynamics.365.BC.25445.IN.DVD

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
     1. **Connector** : Select **Dynamics 365 Business Central** from the drop down list of available Connectors.
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
     7. (Optional) Configure the **Connection node settings**.
        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. **Azure Tenant** : Specify the Microsoft Online tenant being used to access data. If not specified, your default tenant will be used. 
     9. **Company** : Specify the company name that you have set up in Dynamics 365. You can find this information in the **Company Information** page on Dynamics 365 Business Central. 
     10. **Endpoint type** : Specify the type of endpoint the OrganizationUrl must resolve to. 
     11. **Include Navigation Properties** : Specify whether the column listing must include navigation properties. Navigation properties provide a way to navigate an association between two entity types. 
     12. **Use Sandbox** : Specify whether a sandbox is used. 
     13. **User Defined Views** : Specify a filepath to a JSON configuration file that defines custom views. 
     14. Click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     15. (Optional) If you want to use SSL, select **Enable SSL**. This displays the SSL configuration details.
        1. Select a trust store type. It can be either **Public** , **Private** , or **Insecure Connection**. 
        2. Select the certificates as displayed based on your trust store selection.
        3. If you are using mTLS, select the key store certificates in the **Key Store** section.
**Note:**
        * All your certificates must be X.509 certificates and must be in PEM (Privacy Enhanced Mail) format.
        * You can't directly select a certificate when configuring SSL. You must store all your certificates and private keys as a Secret Manager Secret, and then select the required secret during SSL configuration.
     16. Click **Next**.
  5. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Dynamics 365 Business Central connection:

     * Access Key
     * OAuth 2.0 - Client credentials
     * Azure AD

To understand how to configure these authentication types, see Configure authentication.

  6. Click **Next**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

## Configure authentication

Enter the details based on the authentication you want to use.

  * **Access Key**
    * **Username** : Specify the username of the Dynamics 365 OnPremise account used to authenticate to the Microsoft Dynamics 365 Business Central server.
    * **Password** : Select secret containing the password of the Dynamics 365 OnPremise account.
    * **Secret version** : Select the version of the secret.
    * **Access Key** : Specify the access key used to authenticate to Microsoft Dynamics 365 Business Central.
  * **OAuth 2.0 Client Credentials**
    * **Client ID** : Specify the client ID of the app you created.
    * **Client Secret** : Specify the Secret Manager Secret containing the client secret for the connected app you created.
    * **Secret version** : Select the version of the client secret.
  * **Azure AD**
    * **Client ID** : Specify the client ID used for requesting access tokens. This can be found in the overview of the connected app created in the Azure portal. 
    * **Scope** : Specify a comma-separated list of desired scopes.
    * **Client Secret** : Specify the Secret Manager Secret containing the account access key.
    * **Authorization URL** : Enter the authorization URL that you generate when you create an OAuth client. Enter the URL in the following format: `https://login.microsoftonline.com/TENANT_IDENTIFIER/oauth2/v2.0/authorize?prompt=consent`. For example, `https://login.microsoftonline.com/9bxxxxxxxxx8112/oauth2/v2.0/authorize?prompt=consent`. 



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### OAuth 2.0 - Client credentials connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Dynamics365BusinessCentral  
Connector version | 1  
Connection Name | dynamics-businesscentral-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Azure Tenant | c9f472d9-7d8a-44cf-8ee0-458d32e26bce  
Company | Organization_Name  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Organization URL | https://api.businesscentral.dynamics.com/v2.0/c9f472d9-7d8a-44cf-8ee0-458d32e26bce/production/api/v2.0  
Authentication | OAuth 2.0 - Client credentials  
Client ID | fd04bae4-c30c-4faf-bbae-9263d4d96d61  
Client Secret | projects/617888503870/secrets/businesscentral-client-secret  
Secret version | 1  
  
### Access key connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Dynamics365BusinessCentral  
Connector version | 1  
Connection Name | dynamics-businesscentral-on-prem-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Azure Tenant | BC250  
Company | Altostart Ltd.  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Organization URL | http://10.128.0.78:7059/BC250/ODataV4  
Authentication | Access Key  
Username | businesscentral  
Password | PASSWORD  
Secret version | 1  
Access Key | OQq9qggeWxt9iZPSWrs8wgfNjsAq06PT2uls7Luhbp8=  
Secret version | 1  
  
### Azure AD connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Dynamics365BusinessCentral  
Connector version | 1  
Connection Name | d365-business-central-oauth  
Enable Cloud Logging | Yes  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Azure Tenant | c9f472d9-7d8a-44cf-8ee0-458d32e26bce  
Company | Altostart Ltd.  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Organization URL | https://api.businesscentral.dynamics.com/v2.0/c9f472d9-7d8a-44cf-8ee0-458d32e26bce/production/api/v2.0  
Authentication | AzureAD  
Client ID | fd04bae4-c30c-4faf-bbae-9263d4d96d61  
Scopes | https://api.businesscentral.dynamics.com/.default  
Client Secret | projects/617888503870/secrets/d365bc-secret  
Secret version | 3  
Authorization URL | https://login.microsoftonline.com/c9f472d9-7d8a-44cf-8ee0-458d32e26bce/oauth2/v2.0/authorize  
  
For information about how to create a Dynamics 365 Business Central Workspace, see [Welcome to Dynamics 365 Business Central](https://learn.microsoft.com/en-us/dynamics365/business-central/welcome).

For information about the Dynamics 365 Business Central API, see [Dynamics365BusinessCentral API Reference](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/).

## System limitations

The Dynamics 365 Business Central connector can process a maximum of 25 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Dynamics 365 Business Central connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all sales orders

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `salesOrders` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause**.

You must use single quotes (') to enclose the value for a filter clause. You can use the filter clause to filter records based on the columns.




### Example - Get a sales order

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `salesOrders` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to "841c04f9-3391-ef11-8a6b-002248d4e29e", which is the key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"841c04f9-3391-ef11-8a6b-002248d4e29e"` in the **Input Value** field and choose the EntityId as the local variable. 

Value for Entity Id should be passed directly, such as "841c04f9-3391-ef11-8a6b-002248d4e29e". Here, "841c04f9-3391-ef11-8a6b-002248d4e29e" is the unique primary key value.

If passing a single Entity ID throws an error due to the presence of two composite keys, you can use the filter clause to pass the value.




### Example - Delete a sales order

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `salesOrders` from the `Entity` list.
  3. Select the `DELETE` operation, and then click **Done**.
  4. Set the entity ID to "841c04f9-3391-ef11-8a6b-002248d4e29e", which is the key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"841c04f9-3391-ef11-8a6b-002248d4e29e"` in the **Input Value** field and choose the EntityId as the local variable. 

If the entity has two composite business or primary keys instead of specifying the **entityId** , you can also set the **filterClause** to `id='841c04f9-3391-ef11-8a6b-002248d4e29e'`.




### Example - Create a sales order

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `salesOrders` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         {
              "orderDate": "2024-10-30",
              "customerNumber": "10000",
              "currencyCode": "INR",
              "paymentTermsId": "590d75c5-f26e-ef11-a678-6045bdc89b07"
              }
              

If the integration is successful, the `salesOrders` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
              "id": "2e048d8a-a796-ef11-8a6b-6045bdae882d"
              }
              




### Example - Create a sales order line

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `salesOrderLines` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         {
              "documentId": "b747cc93-c37f-ef11-ac23-7c1e523b4365",
              "sequence": 10014,
              "itemId": "8b0f75c5-f26e-ef11-a678-6045bdc89b07",
              "lineType": "Item",
              "lineObjectNumber": "1996-S"
              }
              

If the integration is successful, the `salesOrderLines` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
              "id": "35535130-d09d-ef11-8a6b-002248d4cc93"
              }
              




### Example - Create a sales quote

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `salesQuotes` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         {
              "paymentTermsId": "590d75c5-f26e-ef11-a678-6045bdc89b07",
              "currencyCode": "INR",
              "customerNumber": "30000"
              }
              

If the integration is successful, the `salesQuotes` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
              "id": "2116bd4e-3ba3-ef11-8a6b-6045bdacfb5e"
              }
              




### Example - Create a purchase order

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `purchaseOrders` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         {
              "vendorId": "7e0f75c5-f26e-ef11-a678-6045bdc89b07",
              "vendorNumber": "10000"
              }
              

If the integration is successful, the `purchaseOrders` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
              "id": "53389ee7-a796-ef11-8a6b-6045bdae882d"
              }
              




### Example - Create an item

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `items` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         {
              "number": "4000-D",
              "displayName": "Charlie Altostrat",
              "type": "Inventory",
              "itemCategoryId": "d61672cb-f26e-ef11-a678-6045bdc89b07",
              "baseUnitOfMeasureCode": "PCS"
              }
              

If the integration is successful, the `items` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
              "id": "fad09437-8d9e-ef11-8a6b-000d3af0e092"
              }
              




### Example - Update a sales order

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `salesOrders` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         {
              "phoneNumber": "7764872993"
              }
              

  5. Set the entity ID in Data Mapper to the entity of the salesOrders. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='5e9226d3-1c7b-ef11-a671-6045bdaef76c'`.




### Example - Update a sales order line

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `salesOrderLines` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         {
              "description": "Test from Altostrat"
              }
              

  5. Set the entity ID in Data Mapper to the entity of the salesOrderLines To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='35535130-d09d-ef11-8a6b-002248d4cc93'`.




### Example - Update a sales quote

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `salesQuotes` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         {
              "currencyCode": "USD"
              }
              

  5. Set the entity ID in Data Mapper to the entity of the salesQuotes To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id='2116bd4e-3ba3-ef11-8a6b-6045bdacfb5e'`.




### Example - Update a purchase order

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `purchaseOrders` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         {
              "shipToName": "Charlie Cruz"
              }
              

  5. Set the entity ID in Data Mapper to the entity of the purchaseOrders To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='6b88738e-3891-ef11-8a6b-002248d4e29e'`.




### Example - Update an item

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `items` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         {
              "displayName": "Updates Altostrat name"
              }
              

  5. Set the entity ID in Data Mapper to the entity of the items To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='fad09437-8d9e-ef11-8a6b-000d3af0e092'`.




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
