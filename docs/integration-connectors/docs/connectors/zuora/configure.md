---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/zuora/configure/
title: Zuora \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:33.461934+00:00
---

# Zuora  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/zuora/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Zuora

The Zuora connector lets you connect to a [Zuora](https://www.zuora.com/) instance and access Zuora data as a traditional database.

## Supported versions

This connector leverages the Zuora API version v1 to enable bidirectional access to Zuora.

## Before you begin

Before using the Zuora connector, do the following tasks:

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
     1. **Connector** : Select **Zuora** from the drop down list of available Connectors.
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
     8. **Tenant** : Set this to your Zuora tenant. By default we use "USProduction" tenant. 
     9. **URL** : This is required only in case you have a US Production Copy environment. If this property is provided, the value of Tenant property has no effect in authentication process. 
     10. **ZuoraService** : Specifies which execution service or schema to use 
     11. **Use Client Side Paging** : Whether or not the CData ADO.NET Provider for SAP Cloud for Customer should use client side paging. 
     12. **Use Custom Service** : Indicates if the custom SAP Cloud for Customer OData service should be used. 
     13. **User Defined Views** : A filepath pointing to the JSON configuration file containing your custom views. 
     14. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     15. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Zuora connection:

        * OAuth 2.0 Client Credentials 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



## Configure authentication

To enable OAuth 2.0 Client Credentials authentication, follow these steps:

  1. Create client credentials in Zuora and get the client ID and client secret.
  2. Specify the credentials in Google Cloud.



### Create client credentials in Zuora

  1. On the OneID portal, click on your avatar and then click **Settings**.
  2. Click **Manage OAuth 2.0 Clients**.
  3. On the **Manage OAuth 2.0 Clients** page, click **New**.
  4. In the **New OAuth 2.0 Client** window, specify the following fields: 
     * **Name** : Enter a name for the client.
     * **Type** : Select **Client Credentials** from the list.
  5. Click **Save**. After the client is created successfully, a window with the client ID and client secret appears. 

Save the client ID and client secret for later use. For more information, see [Manage OAuth 2.0 clients ](https://knowledgecenter.zuora.com/Zuora_Central_Platform/Zuora_OneID/13_OneID_settings/01_Manage_OAuth_2.0_clients).




#### Specify the credentials in Google Cloud

When you create the connection in Integration Connectors , you must specify the following details: 

In the **Authentication** section, enter the following details:

  * **Client ID** : The client ID for the app you created.
  * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.



#### Web connection type

The following table lists the sample configuration values for the Zuora web connection type: 

Field name  | Details  
---|---  
Location  | us-central1  
Connector  | Zuora  
Connector version  | 1  
Connection Name  | zuora-con  
Service Account  | account@my-project.iam.gserviceaccount.com  
Tenant  | TENANT  
Minimum number of nodes  | 2  
Maximum number of nodes  | 4  
Client ID  | CLIENT_ID  
Client Secret  | CLIENT_SECRET  
Secret Version  | 1  
  
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

## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the records in Refunds

This example lists all the records in the `Refunds` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Refunds` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).



### Example - Get a debit memo record

This example gets a record whose ID is `45` from the `Debit_Memo` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Debit_Memo` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `45` in the **Default Value** field. 

Here, `45` is a primary key value in the `Debit_Memo` entity.




### Example - Create a ticket

This example creates a ticket in the `Ticket` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Tickets` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "Test735362767",
         "Label": "Test735362767",
         "Type": "String",
         "FieldType": "Insert ticket1",
         "GroupName": "ticketinformation",
         "Description": "Test ticket"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Name": "Test1695971640609"
         }




### Example - Update a deals entry

This example updates the record whose ID is 97 in the `Deals` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Deals` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Description": "New description"
         }

  5. Click **entityId** , and then enter `97` in the **Default Value** field. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to `97`.




### Example - Delete a form

This example deletes the record whose ID is 78 in the `Forms` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Forms` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `78` in the **Default Value** field. 



## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
tenant | ENUM | False | Set this to your Zuora tenant. By default we use "USProduction" tenant. Supported values are: USProduction, USAPISandbox, USPerformanceTest, EUProduction, EUSandbox, EUCentralSandbox, USCloudProduction, USCloudAPISandbox, USCentralSandbox  
url | STRING | False | This is required only in case you have a US Production Copy environment. If this property is provided, the value of Tenant property has no effect in authentication process.   
zuora_service | ENUM | False | Specifies which execution service or schema to use Supported values are: DataQuery, AQuADataExport  
use_client_side_paging | BOOLEAN | False | Whether or not the CData ADO.NET Provider for SAP Cloud for Customer should use client side paging.   
use_custom_service | BOOLEAN | False | Indicates if the custom SAP Cloud for Customer OData service should be used.   
user_defined_views | STRING | False | A filepath pointing to the JSON configuration file containing your custom views.   
  
## Use the Zuora connection in an integration

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
