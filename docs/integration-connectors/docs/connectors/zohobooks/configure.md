---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/zohobooks/configure/
title: ZohoBooks \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:46.773171+00:00
---

# ZohoBooks  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/zohobooks/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ZohoBooks

The ZohoBooks connector lets you perform SQL operations on the ZohoBooks system.

## Supported versions

The connector leverages the Zoho Books API V3 to enable bidirectional access to Zoho Books data.

## Before you begin

Before using the Zoho Books connector, do the following tasks:

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

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

Supported regions for connectors include: 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Zoho Books** from the drop down list of available Connectors.
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
     8. **Accounts Server** : The full Account Server URL. 
     9. **Organization Id** : The Id associated with the specific Zoho Books organization. 
     10. **Verbosity Level** : Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates). 
     11. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     12. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Zoho Books connection:

        * OAuth 2.0 Auth Code Grant 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 Auth Code Grant**
    * **Client ID** : The client id provided by connector for the app you created.
    * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.
    * **Access Token** : Secret Manager Secret containing oauth access token provided for the connected app you created.



## Configure ZohoBooks authentication

The following sections describe how to configure the ZohoBooks connector.

### Set up a ZohoBooks account

For more information about setting up the ZohoBooks account, see [Account creation](https://www.zoho.com/in/books/help/getting-started/access-zb.html#sign-up).

### Set up a developer account and create a client app

For information about ZohoBooks developer account and client app creation, see [Client App creation](https://www.zoho.com/creator/help/api/v2.1/register-client.html).

### Set up authentication

To set up authentication, do the following:

  1. Go to the **Integration Connectors** page in the [Cloud console](https://console.cloud.google.com/).
  2. To view the details of a specific connection, click on a connection name in the table of existing connections.
  3. In the **Authentication** section, click **Authorize connection** to begin the authorization process.
  4. Copy the redirect URI.
  5. Go to the [ZohoBooks Developer Console](https://api-console.zoho.in/).
  6. In the Service based application client authorized redirect URI's section, add the redirect URI.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

  7. In the **Integration Connectors** page, go to the ZohoBooks connection page from where you copied the redirect URI and click **Authorize**.

You are redirected to the ZohoBooks site to authorize.




## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Zoho Books connection.

### Web connection type

Field name | Details  
---|---  
Region | us-east4  
Connector | ZohoBooks  
Connector version | 1  
Connection Name | zohobooks-google-cloud-conn  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Accounts Server | https://books.zoho.in  
Organization Id | ORGANIZATION_ID  
Verbosity | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Client Id | CLIENT_ID  
Scopes | ZohoBooks.fullaccess.all  
Client Secret | CLIENT_SECRET  
Secret version | 1  
  
## Use the ZohoBooks connection in an integration

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

This section lists some of the actions supported by the Zoho Books connection. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### ImportCreditCardStatement action

This action lets you import credit cart statements.

#### Input parameters of the ImportCreditCardStatement action

Parameter name | Data type | Required | Description  
---|---|---|---  
AccountId | String | No | Id of the Bank/Credit Card account  
TransactionsTransactionDebitOrCredit | String | No | Indicates if transaction is Debit or Credit.  
TransactionsTransactionAmount | String | No | Amount involved in the transaction.  
TransactionsTransactionDescription | String | No | Transaction description.  
TransactionsTransactionDate | String | No | Date of the Transaction.  
  
To understand how to configure the `ImportCreditCardStatement` action, see Examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Import a credit card statement

This example imports a credit card statement.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ImportCreditCardStatement` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "AccountId": "1470449000000023015",
           "TransactionsTransactionDebitOrCredit": "credit",
           "TransactionsTransactionAmount": "200",
           "TransactionsTransactionDescription": "Transaction done from Google account",
           "TransactionsTransactionDate": "2023-05-05"
         }

If the action is successful, the `ImportCreditCardStatement` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Your bank statement has been imported."
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all estimates

This example lists all records in the `Estimates` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Estimates` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). You can also specify multiple filter conditions by using the logic operators.



### Example - Get a sales order

This example gets the specified sales order from the `SalesOrder` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesOrder` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `1470449000000043003` in the **Default Value** field. 

Here, `1470449000000043003` is a primary key value in the `SalesOrder` entity.




### Example - Create a bank transaction

This example creates a bank transaction record in the `BankTransactions` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `BankTransactions` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "TransactionType": "transfer_fund",
         "FromAccountId": "1470449000000000459",
         "ToAccountId": "1470449000000110001",
         "Amount": 45.0,
         "CurrencyId": "1470449000000000064"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "TransactionId": "1470449000000231005"
         }




### Example - Update customer contact details

This example updates the specified customer record in the `CustomerContacts` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `CustomerContacts` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Department": "Development",
         "ContactId": "1470449000000038003"
         }

  5. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `1470449000000038005` in the **Default Value** field. 

If the integration is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    {
    "CustomerContactId": "1470449000000038005"
    }




### Example - Delete an invoice record

This example deletes the specified invoice record in the `InvoiceDetails` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `InvoiceDetails` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `1470449000000184001` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

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
