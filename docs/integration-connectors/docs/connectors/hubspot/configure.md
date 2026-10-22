---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/hubspot/configure/
title: HubSpot \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:09.352064+00:00
---

# HubSpot  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/hubspot/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HubSpot

The HubSpot connector lets you perform insert, delete, update, and read operations on HubSpot datasets.

## Supported versions

This connector supports the following HubSpot API versions:

  * HubSpot
  * HubSpotV3
  * HubSpotV4



## Before you begin

Before using the HubSpot connector, do the following tasks:

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
     1. **Connector** : Select **HubSpot** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
        * For connectors that [support event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#enable-event-subscriptions-in-connections), the connection names cannot begin with the "goog" prefix. 
     4. Optionally, enter a **Description** for the connection instance.
     5. **Service Account** : Select a service account that has the required roles.
     6. To use the connection for event subscriptions, select **Enable event subscription**. Selecting this, displays the following options: 
        * **Enable event subscription with entity and actions** : Select this option to use the connection for both event subscription and connector operations (entities and actions).
        * **Enable only event subscription** : Select this option to use the connection only for event subscription. If you select this option, click **Next** , and then configure event subscription.
     7. **Schema** : Specify the HubSpot API version to use. HubSpotV4 is the new API. 
     8. **BrowsableSchemas** : This property restricts the schemas reported to a subset of the available schemas. For example, BrowsableSchemas=SchemaA,SchemaB,SchemaC. 
     9. **Contacts Properties** : Enter the comma separated field names of the `Contacts` entity that you want to select from the `List` entity operation. For example, `fieldA, fieldB, fieldC`
     10. **Companies Properties** : Enter the comma separated field names of the `Companies` entity that you want to select from the `List` entity operation. For example, `fieldA, fieldB, fieldC`
     11. **Deals Properties** : Enter the comma separated field names of the `Deals` entity that you want to select from the `List` entity operation. For example, `fieldA, fieldB, fieldC`
     12. **Use proxy** : Select this checkbox to configure a proxy server for the connection. 
     13. **Proxy Auth Scheme** : The authentication type to use to authenticate to the ProxyServer proxy. 
     14. **Proxy User** : A user name to be used to authenticate to the ProxyServer proxy. 
     15. **Proxy Password** : A password to be used to authenticate to the ProxyServer proxy. 
     16. **Proxy SSL Type** : The SSL type to use when connecting to the ProxyServer proxy. 
     17. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     18. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     19. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : You can specify the destination details either as a host address or a service attachment. Select any of the following destination types: 
        * **Host address** : If you want to specify the hostname or IP address of the destination.
        * **Service attachment** : If you want to specify the private endpoint for your internal IP addresses. The service attachment, lets you hide your internal IP addresses from the external network. You can create a service attachment in Google Cloud, by using the Private Service Connect feature. For information on configuring a Private Service Connect, see [Publish managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

Based on your selection of destination type, enter the host address or the service attachment name.

To enter additional destinations, click **+Add destination**.

     2. Click **Next**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the HubSpot connection:

        * **Private App Access Token:** Select the Secret Manager Secret containing the private app access token. 

Private apps allow you to use HubSpot's APIs to access specific data from your HubSpot account. You can authorize what each private app can request or change in your account, which will generate an access token that's unique to your private app. In your private app, ensure you have provided the read permission at least to the following scopes:

          * crm.schemas.line_items.read
          * crm.schemas.quotes.read
          * crm.schemas.deals.read
          * crm.schemas.companies.read
          * crm.schemas.custom.read
          * crm.schemas.contacts.read

For more information, see [Private apps](https://developers.hubspot.com/docs/api/private-apps).

     2. Click **Next**.
  7. If you have enabled event subscription, the **Event Subscription Details** section appears on the connection creation page. In the **Event subscription details** step, provide the authentication details that will be used to validate the HubSpot token payload: 
     1. **Client Secret:** (Optional) Select the Secret Manager secret of your private app's client secret, and the corresponding secret version from the **Secret Version** drop-down.

For more information, see [Private apps](https://developers.hubspot.com/docs/api/private-apps).

     2. Select **Enable private connectivity** for secured connectivity between your backend application and your connection. If you select this option, you must perform additional configuration steps after creating the connection. For more information, see [Private connectivity for event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#psc-eventing). 
     3. Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
        1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
        2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.
     4. Click **Next**.
  8. **Review** : Review your connection and authentication details.
  9. Click **Create**.



#### HubSpot V1 server connection type

The following table lists the sample values for the various fields that you configure when creating the HubSpot connection. Field name | Details  
---|---  
Region | us-central1  
Connector | HubSpot  
Connector version | 1  
Connection Name | hub-spot-conn  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com/td>  
Schema | Hubspot  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Private App Access Token | PRIVATE_APP_ACCESS_TOKEN  | Secret Version | 1 

### Create a private app access token in HubSpot

  1. Create a new HubSpot account and login to [HubSpot](https://app.hubspot.com/login).
  2. Click **Settings** and then navigate to **Integrations > Private Apps**.
  3. Click **Create private app**.
  4. On the **Basic Info** tab, configure the details of your application, such as name, logo, and description.
  5. On the **Scopes** tab, select **Read** or **Write** for each scope you want your private application to be able to access.
  6. After you configure your application, click **Create app**.
  7. Review the information about your application's access token, and then click **Continue creating** , and then **Show token**.
Use this token value to specify the private app access token when you configure the connection in Google Cloud. 


## Entities, operations, and actions

All the Integration Connectors provide a layer of abstraction for the objects of the connected application. You can access an application's objects only through this abstraction. The abstraction is exposed to you as entities, operations, and actions. **Note:** You can view the entities, operations, and actions of a connector in the [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).

  * **Entity:** An entity can be thought of as an object, or a collection of properties, in the connected application or service. The definition of an entity differs from a connector to a connector. For example, in a database connector, tables are the entities, in a file server connector, folders are the entities, and in a messaging system connector, queues are the entities. However, it is possible that a connector doesn't support or have any entities, in which case the `Entities` list will be empty.
  * **Operation:** An operation is the activity that you can perform on an entity. You can perform any of the following operations on an entity: 
    * [List](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Get](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Create](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Update](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Delete](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
Selecting an entity from the available list, generates a list of operations available for the entity. For a detailed description of the operations, see the Connectors task's [entity operations](https://docs.cloud.google.com/application-integration/docs/connectors-task#config-prop). However, if a connector doesn't support any of the entity operations, such unsupported operations aren't listed in the `Operations` list.
  * **Action:** An action is a first class function that is made available to the integration through the connector interface. An action lets you make changes to an entity or entities, and vary from connector to connector. Normally, an action will have some input parameters, and an output parameter. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty. 

**Note:** All entities and actions will have a schema associated with them. For example, an action schema will have the parameter details such as; the parameter names, and its corresponding data type. The schema (metadata) for entities and actions is fetched by the connection at runtime from your backend. If there are any updates to the schema, such updates won't be automatically reflected in your existing connections; you must manually refresh the schema. To refresh the schema for a connection, open the **Connection details** page of the connection, and then click **Refresh connection schema**. 

## Known issues

  * The update operation on some of the entities returns an empty response even though the update is successful. In such cases, it's recommended to verify the update in your HubSpot instance.
  * In HubSpot, you can potentially have many custom fields for the following entities: 
    * Contacts
    * Companies
    * Deals
For these entities, selecting all the fields at once in the `List` entity operation, may cause the HubSpot connector to return an error. In the scenarios where you want to limit the number of custom fields from the `List` operation, specify the required field names (as comma separated values) in the HubSpot connector configuration. For example, to limit the fields of the `Contacts` entity, specify the required field names in the connector configuration's `Contacts Properties` field. Similarly, for the `Companies` entity, specify the required field names in the `Companies Properties` field, and for the `Deals` entity, specify the required field names in the `Deals Properties` field.  You can specify the fields during the connection creation step. However, if you already have an existing connection, you must edit the connection, and then specify the required fields. 
  * If you have a very large result set, the `List` operation might fail because of a connection timeout. In such a scenario, you can explore the option of limiting your result set by specifying the [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter) for the List operation.



## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the contacts

This example lists all the records in the `Contacts` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Contacts` from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.



### Example - Get a deal record

This example gets a record whose ID is `45` from the `Deals` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Deals` from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `45` in the **Default Value** field. Here, `45` is a primary key value in the `Deals` entity.



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

This example updates the record whose ID is 97 in the `Contacts` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Deals` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Description": "New description"
         }

  5. Click **entityId** , and then enter `97` in the **Default Value** field. Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to `97`.



### Example - Delete a form

This example deletes the record whose ID is 78 in the `Forms` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Forms` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `78` in the **Default Value** field. 



## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection. To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template). When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file: | Parameter name | Data type | Required | Description  
---|---|---|---  
schema | ENUM | True | Specify the HubSpot API version to use. HubSpotV4 is the new API. Supported values are: HubSpot, HubSpotV3, HubSpotV4  
browsable_schemas | STRING | False | This property restricts the schemas reported to a subset of the available schemas. For example, BrowsableSchemas=SchemaA,SchemaB,SchemaC.   
contacts_columns | STRING | False | Comma separated list of properties to select from HubSpot for the Contacts entity.   
companies_columns | STRING | False | Comma separated list of properties to select from HubSpot for the Companies entity.   
deals_columns | STRING | False | Comma separated list of properties to select from HubSpot for the Deals entity.   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the HubSpot connection in an integration

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
