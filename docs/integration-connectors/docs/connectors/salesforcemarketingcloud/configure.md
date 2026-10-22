---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforcemarketingcloud/configure/
title: Salesforce Marketing Cloud \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:28.518509+00:00
---

# Salesforce Marketing Cloud  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforcemarketingcloud/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Salesforce Marketing Cloud

The Salesforce Marketing Cloud connector lets you perform insert, delete, update, and read operations on a Salesforce Marketing Cloud dataset.

## Before you begin

Before using the Salesforce Marketing Cloud connector, do the following tasks:

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
     1. **Connector** : Select **Salesforce Marketing Cloud** from the drop down list of available Connectors.
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
     8. **API Integration Type** : The grant type for the OAuth flow. Accepted entries are Server-to-Server and Web-App. 
     9. **Account Id** : The account identifier, or MID, of the target business unit. 
     10. **Display Child Data Extensions** : Displays the Data Extensions of Child Accounts if set. 
     11. **Instance** : The instance of the Salesforce Marketing Cloud API used. 
     12. **List Data Extensions** : A boolean determining if data extensions should be listed as tables or not. 
     13. **Query All Accounts** : Queries all accounts, including parent and all children, regarding an event. 
     14. **Schema** : Specify the Salesforce Marketing Cloud server version to connect with. 
     15. **Subdomain** : The subdomain of the Salesforce Marketing Cloud API. 
     16. **Use Legacy Authentication** : A boolean determining if the connection should be made to Salesforce Marketing Cloud REST API using the legacy authentication or not. 
     17. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     18. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     19. Click **NEXT**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Salesforce Marketing Cloud connection:

        * Username and password
        * OAuth 2.0 - Client Credentials
        * OAuth 2.0 - Authorization Code

To understand how to configure these authentication types, see Configure authentication.

     2. Click **NEXT**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



## Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.
  * **OAuth 2.0 - Client Credentials**
    * **Client ID** : The client ID for the app you created.
    * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.
    * **Secret version** : The version of the client secret.
  * **OAuth 2.0 - Authorization Code**
    * **Client ID** : The client ID used for requesting access tokens.
    * **Scopes** : A comma-separated list of desired scopes.
    * **Client secret** : The client secret used for requesting access tokens.
    * **Secret version** : The version of the client secret.
    * **Authorization URL** : The authorization URL generated when creating client.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.




### Configure Salesforce Marketing Cloud

To configure Salesforce Marketing Cloud, log into your existing account or create a new account using the [Salesforce Marketing Cloud Login](https://mc.s11.exacttarget.com/cloud/login.html#app). For information about community support and additional information, see [Trailblazer Community](https://trailblazercommunitygroups.com/salesforce-marketing-cloud-developers-group/). For information about Salesforce Marketing Cloud REST APIs, see [Salesforce Marketing Cloud REST API](https://developer.salesforce.com/docs/marketing-cloud/marketing-cloud-rest-api/reference/index). For information about Salesforce Marketing Cloud SOAP API, see [SOAP APIs](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/web_service_guide.html). 

#### Create an API client

  1. On your Salesforce Marketing Cloud profile page, click **Setup**. 
  2. In the left panel, select **Installed Packages** and then click **New**.
  3. Enter a name and description for your integration.
  4. Choose **Server-to-Server** as the Integration type.
  5. Click **Save**.

You can view the client ID, client secret, SOAP base URL, REST base URL, and other details.




### Basic authentication - Connection type

The following table lists the sample configuration values for the Basic authentication connection type.

Field name | Details  
---|---  
Location | us-east1  
Connector | Salesforce Marketing cloud  
Connector version | 1  
Connection Name | sfmcconn1  
Description | SOAP - User Password  
Enable Cloud Logging | Yes  
Service Account | service-account@my-project.iam.gserviceaccount.com  
API Integration Type | Server to Server  
Schema | SOAP  
Account ID | ACCOUNT_ID  
Display Child Data Extensions | Yes  
Instance | s11  
List Data Extensions | Yes  
Verbosity Level | 5  
Subdomain | SUBDOMAIN  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
  
### OAuth 2.0 - Connection type

The following table lists the sample configuration values for the OAuth 2.0 client credentials connection type.

Field name | Details  
---|---  
Location | us-east1  
Connector | Salesforce Marketing cloud  
Connector version | 1  
Connection Name | sfmc-rest-conn  
Enable Cloud Logging | No  
Service Account | service-account@my-project.iam.gserviceaccount.com  
API Integration Type | Server to Server  
Schema | REST  
Account ID | ACCOUNT_ID  
Display Child Data Extensions | Yes  
Instance | s11  
List Data Extensions | Yes  
Query All Accounts | Yes  
Verbosity Level | 4  
Subdomain | SUBDOMAIN  
Client ID | CLIENT_ID | Client Secret | CLIENT_SECRET  
Secret version | 1  
  
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

The Salesforce Marketing Cloud connector can process a maximum of 7 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists all the actions supported by the Salesforce Marketing Cloud connection.

### GetJourneyPublicationStatus action

This action gets the status of a journey publication.

#### Input parameters of the GetJourneyPublicationStatus action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
StatusId | string | True | The status ID of a journey publication.  
  
#### Output parameters of the GetJourneyPublicationStatus action

This action returns the status 200 (OK) with a response body indicating all results.

For example on how to configure the `GetJourneyPublicationStatus` action, see Examples.

### FireEntryEvent action

Fire the entry event that initiates the journey.

#### Input parameters of the FireEntryEvent action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ContactKey | String | True | The ID that uniquely identifies a subscriber or contact  
EventDefinitionKey | String | True | Find the EventDefinitionKey in Event Administration after the event is created and saved. This is true for both standard and custom events. Don't include a period in the event definition key.  
Data | String | False | Properties of the event. Only required if defined in a custom event or by the event.  
  
#### Output parameters of the FireEntryEvent action

This action returns the status 200 (OK) with a response body indicating all results

For example on how to configure the `FireEntryEvent` action, see Examples.

### StopJourney action

Stops a running journey

#### Input parameters of the StopJourney action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
JourneyId | String | True | The ID of the journey to stop, expressed in the form of a GUID (UUID)  
JourneyVersion | Integer | True | The version number of the journey to stop  
  
#### Output parameters of the StopJourney action

This action returns the status 200 (OK) with a response body indicating all results

For example on how to configure the `StopJourney` action, see Examples.

### PublishJourney action

PublishJourney Action Publishes a journey version asynchronously

#### Input parameters of the PublishJourney action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
JourneyId | String | True | The ID of the journey to stop, expressed in the form of a GUID (UUID).  
JourneyVersion | Integer | True | The version number of the journey to stop.  
  
#### Output parameters of the PublishJourney action

This action returns the status 200 (OK) with a response body indicating all results

For example on how to configure the `PublishJourney` action, see Examples.

### CreateTriggeredSend action

CreateTriggeredSend Action Creates a triggered send object which represents a specific instance of a triggered email send

#### Input parameters of the CreateTriggeredSend action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Key | String | False | Defines associated triggered send definition for triggered send. This property corresponds to the external key assigned to an object in Marketing Cloud.  
SendId | String | False | ID of the entry event send definition that comes from the response when creating a TriggeredSendDefinition. Either this or the external key is required.  
FromAddress | String | False | Email address that will show as the sender.  
FromName | String | False | Name of the sender  
ToAddress | String | True | Email address of the message recipient.  
SubscriberKey | String | True | Unique identifier defined for the message recipient.  
SubscriberAttributes | String | False | Name and value pairs for subscriber attributes defined for the message.  
RequestType | String | False | Valid values ASYNC and SYNC. Default value when not defined is ASYNC. Determines if the request is processed asynchronously.  
  
#### Output parameters of the CreateTriggeredSend action

This action returns the status 200 (OK) with a response body indicating all results

For example on how to configure the `CreateTriggeredSend` action, see Examples.

### SendTransactionalMessageToRecipient action

SendTransactionalMessageToRecipient Action Sends a message to a single recipient via a send definition

#### Input parameters of the SendTransactionalMessageToRecipient action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
MessageKey | String | True | User-defined message identifier.  
DefinitionKey | String | True | Unique identifier of the definition.  
RecipientContactKey | String | True | Unique identifier for a subscriber in Marketing Cloud. Each request must include a contactKey. You can use an existing subscriber key or create one at send time by using the recipient's email address  
RecipientTo | String | False | Channel address of the recipient. For email, it's the recipient's email address  
Attributes | String | False | Information used to personalize the message for the recipient. Written as key pairs. The attributes match profile attributes, content attributes, or triggered send data extension attributes  
  
#### Output parameters of the SendTransactionalMessageToRecipient action

This action returns the status 200 (OK) with a response body indicating all results

For example on how to configure the `SendTransactionalMessageToRecipient` action, see Examples.

## Action Examples

This section describes how to perform some of the actions in this connector.

### Example - Get the status of a journey publication

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetJourneyPublicationStatus` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "StatusId": "3acf1f54-5c9e-4719-b7f7-bfc2e5caf10a"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
      "Status": "PublishCompleted",
      "Message": null
    }]
    




### Example - Fire an entry event to initiate a journey

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `FireEntryEvent` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ContactKey": "Email",
           "EventDefinitionKey": "APIEvent-4d84e619-a629-6b17-945f-9a6e78a1982c",
           "Data": "{\"Email\": \"usr1@test.com\"}"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
      "EventInstanceId": "0d6f6dd1-1aaa-4eec-9727-f99550ab68f9"
    }]
    




### Example - Stop a running journey

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `StopJourney` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "JourneyId": "37D2789E-2B1D-433E-8E18-8F47E4D8E865",
           "JourneyVersion": 1.0
         }
         

If the action is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
      "Success": true
    }] 
    




### Example - Publish a journey version

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `PublishJourney` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "JourneyId": "0868BF36-3107-460E-9EF1-09633A0592E8",
           "JourneyVersion": 1.0
         }
         

If the action is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
      "StatusId": "acb1734d-483e-400a-97d7-0501b94f03b2"
    }]  
    




### Example - Create a trigger to initiate a journey

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateTriggeredSend` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Key": "BU27_SendDefinition1",
           "ToAddress": "usr1@test.com",
           "SubscriberKey": "107",
           "SubscriberAttributes": "{\"FirstName\": \"John\", \"LastName\": \"P\"}"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
      "Success": "True",
      "RecipientSendId": "5d06edb1-d07c-48ad-a1f2-d6350eb863f8",
      "Messages": "Queued"
    }]
    




### Example - Send a message to a single recipient

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendTransactionalMessageToRecipient` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "MessageKey": "T9999009",
           "DefinitionKey": "Send-Definition-SFMC-Demo-2",
           "RecipientContactKey": "107",
           "RecipientTo": "usr1@test.com",
           "Attributes": "FirstName :John"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
      "RequestId": "d8fb9e9e-3ae2-412f-b01e-d198433cfc16"
    }] 




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

## Supported entity operations

This section lists the entity operations supported by the Salesforce Marketing Cloud connector and shows how to perform some of the [entity operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

Entity | Operation  
---|---  
**DataExtensionObject_Custom** | List, Get, Delete, Create, Update  
**Campaign** | List, Get, Delete  
**CampaignAssets** | List, Get, Delete  
**Journeys** | List, Get, Delete, Create, Update  
**List** | List, Create, Update  
**Publication** | List  
**Subscriber** | List, Create  
**SubscriberList** | List  
**ListSubscriber** | List  
**JourneyActivities** | Get, Delete  
**Campaigns** | Create  
**Assets** | List, Get, Delete, Create, Update  
  
### Example - List all Assets

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Assets` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement.

You must use single quotes (') to enclose the value for a filter clause and it must be passed directly, such as `CategoryName='Content Builder'`. Here, CategoryName is the column name and Content Builder is the value.

You can use the filter clause to filter records based on the columns. For example, to filter records, use the following filter clause: `Location='US'` and `region='us-east1'`

In certain cases, passing an Entity ID might throw an error. In such cases, you can use the filter clause, such as id=172.




### Example - Get an Assets record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Assets` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to 49851.0 which is the Key to be passed. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `49851.0` in the **Default Value** field. 

The value for Entity ID should be passed directly, such as Id= 49851.0. Here, 49851.0 is the unique primary key value, which should be passed.




### Example - Delete an Assets record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Assets` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to 49851.0 which is the Key to be passed.. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `49851.0` in the **Default Value** field. 

The value for Entity ID should be passed directly, such as ID= 49851.0. Here, 49851.0 is the unique primary key value, which should be passed.




### Example - Create a DataExtensionObject_Custom record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `DataExtensionObject_Custom` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "StudentName":"Cruz",
         "StudentID":"1",
         "Rank":"1"}
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "StudentID": 1
         } 




### Example - Create an Assets record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Assets` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "Googlecloud_Created_HTMLEmail_Testing_V1",
           "TypeName": "htmlemail",
           "TypeId": 208.0
         }

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": 60188.0
         }




### Example - Create a Campaigns record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Campaigns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "Campaigns - Tested via Googlecloud",
           "CampaignCode": "annual2023",
           "Color": "0000ff",
           "Favorite": false
         }

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": 247.0
         } 




### Example - Create a Journeys record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Journeys` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Version": 1.0,
           "Name": "API_Journey_Googlecloud_Retest_1",
           "CreatedDate": "2023-04-26 04:20:29.87",
           "ModifiedDate": "2023-05-10 07:45:06.04",
           "LastPublishedDate": "2023-04-26 04:37:18.0",
           "Description": "API_Journey_Googlecloud_Retest_1",
           "WorkFlowApiVersion": 1.0,
           "Tags": null,
           "Goals": "",
           "Triggers": "[{\"id\": \"c79154a3-a0d2-435e-a6ad-bed46474620a\", \"key\": \"TRIGGER\", \"name\": \"API_Journey_Googlecloud\", \"description\": \"\", \"type\": \"APIEvent\", \"outcomes\": [], \"arguments\": {\"startActivityKey\": \"{Context.StartActivityKey}\", \"dequeueReason\": \"{Context.DequeueReason}\", \"lastExecutedActivityKey\": \"{Context.LastExecutedActivityKey}\", \"filterResult\": \"true\"}, \"configurationArguments\": {\"schemaVersionId\": 0, \"criteria\": \"\", \"filterDefinitionId\": \"00000000-0000-0000-0000-000000000000\"}, \"metaData\": {\"sourceInteractionId\": \"00000000-0000-0000-0000-000000000000\", \"eventDefinitionId\": \"8153cf00-ebf6-4c18-b52f-573eb724df87\", \"eventDefinitionKey\": \"APIEvent-4d84e619-a629-6b17-945f-9a6e78a1982c\", \"chainType\": \"None\", \"configurationRequired\": false, \"iconUrl\": \"/images/icon_journeyBuilder-event-api-blue.svg\", \"title\": \"\", \"entrySourceGroupConfigUrl\": \"jb:///data/entry/api-event/entrysourcegroupconfig.json\"}}",
           "Defaults": "[{\"email\": [\"{Event.APIEvent-4d84e619-a629-6b17-945f-9a6e78a1982c.\"Email"}\"], \"properties\": {\"analyticsTracking\": {\"enabled\": false, \"analyticsType\": \"google\", \"urlDomainsToTrack\": []}}}]"
         }

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "aa03afe4-6a28-481f-bec4-564712127414"
         }




### Example - Create a List record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `List` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ID": "04052023.0",
           "ObjectID": "82349658-b482-404f-8c67-e555aadee0f4",
           "PartnerKey": "null",
           "CreatedDate": "2023-03-16 10:52:48.097",
           "ModifiedDate": "2023-03-17 10:30:34.497",
           "Client_ID": "5.14012689E8",
           "Client_PartnerClientKey": null,
           "ListName": "Googlecloud_Created_Subscriber_List",
           "Description": "null",
           "Category": "15449.0",
           "Type": "Public",
           "CustomerKey": "Googlecloud_BCONE",
           "ListClassification": "ExactTargetList",
           "AutomatedEmail_ID": "null"
         }

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": 4052023.0
         }




### Example - Create a Subscriber record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Subscriber` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "EmailAddress": "baklavainthebalkans@gmail.com",
           "SubscriberKey": "KB1"
         }

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Success": true
         }




### Example - Update a DataExtensionObject_Custom record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `DataExtensionObject_Custom` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "StudentName":"Charlie",
         "Rank":"1"
         }
         

  5. Set the entity ID to For ex: 103032 which is the Primary Key to be passed. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **entityId** and then enter `10` in the **Default Value** field. 

If entity has composite business or primary keys, instead of specifying the **entityId** , you can also set the **filterClause** to `Rank='1' and StudentID='10'`.

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
        "StudentID": 1
    }
    




### Example - Update an Assets record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Assets from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Description": "June2023-Updated"
         }
         

  5. Set the entity ID to the entity of the Assets . To set the entity ID, click **entityId** and then enter `52080` in the **Default Value** field. 

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": 52080.0
         }
         




### Example - Update a Journeys record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Journeys` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "SFMC_CRETAE_JOURNEY_FROM_Googlecloud_Updated_V1"
         }
         

  5. Set the entity ID to the entity of the Journeys . To set the entity ID, click **entityId** and then enter ` 0868BF36-3107-460E-9EF1-09633A0592E8` in the **Default Value** field. 

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "0868bf36-3107-460e-9ef1-09633a0592e8"
         }
         




### Example - Update a List record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `List` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Description": "UpdatedDescription"
         }
         

  5. Set the entity ID to the entity of the List . To set the entity ID, click **entityId** and then enter `1234` in the **Default Value** field. 

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "ID": 1234.0
         }
         




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
apiintegration_type | ENUM | False | The grant type for the OAuth flow. Accepted entries are Server-to-Server and Web-App. Supported values are: Server-to-Server, Web-App  
schema | ENUM | True | Specify the Salesforce Marketing Cloud APIs to connect with. Supported values are: REST, SOAP  
account_id | STRING | False | The account identifier, or MID, of the target business unit.   
display_child_data_extensions | BOOLEAN | False | Displays the Data Extensions of Child Accounts if set.   
instance | STRING | False | The instance of the Salesforce Marketing Cloud API used. Note: If the instance is greater than s10, then Subdomain must be specified.   
list_data_extensions | BOOLEAN | False | A boolean determining if data extensions should be listed as tables or not.   
query_all_accounts | BOOLEAN | False | Queries all accounts, including parent and all children, regarding an event.   
verbosity | STRING | False | Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates).   
subdomain | STRING | False | The subdomain of the Salesforce Marketing Cloud API.   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the Salesforce Marketing Cloud connection in an integration

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

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


