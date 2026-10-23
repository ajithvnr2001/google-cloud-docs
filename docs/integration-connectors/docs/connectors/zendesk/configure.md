---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure/
title: Zendesk \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:36.817091+00:00
---

# Zendesk  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Zendesk

The Zendesk connector lets you perform insert, delete, update, and read operations on Zendesk database.

## Supported versions

This connector supports Zendesk's Version 2 APIs.

## Before you begin

Before using the Zendesk connector, do the following tasks:

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

  * If you are using API token as your authentication method to access the Zendesk API, obtain an API token from your Zendesk admin center. Once generated, save your API token securely in the key management of Google Cloud. For more information, see [Managing API token access to the Zendesk API](https://support.zendesk.com/hc/en-us/articles/4408889192858-Managing-API-token-access-to-the-Zendesk-API).
  * For information about creating a Zendesk account, see [Create a Zendesk Account](https://support.zendesk.com/hc/en-us/articles/4408823799962-How-do-I-create-a-Support-trial-account).
  * To create a Zendesk event subscription, you must have an admin role in your Zendesk account. Your Zendesk account must have a `Suite growth and above` or `Support professional and above` plan, as this feature is not available for trial accounts.

**Note:** Zendesk deprecated username and password authentication as of July 31, 2024.

## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Zendesk** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
        * For connectors that [support event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#enable-event-subscriptions-in-connections), the connection names cannot begin with the "goog" prefix. 
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. To use the connection for event subscriptions, select **Enable event subscription**. Selecting this, displays the following options: 
        * **Enable event subscription with entity and actions** : Select this option to use the connection for both event subscription and connector operations (entities and actions).
        * **Enable only event subscription** : Select this option to use the connection only for event subscription. If you select this option, click **Next** , and then configure event subscription.
     8. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     9. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
**Note:** Enable proxy authentication to route API requests through a proxy server, enhance security, and manage traffic. For more information about benefits of using a proxy server, see [Benefits of using a Zendesk proxy server](https://developer.zendesk.com/documentation/apps/app-developer-guide/making-api-requests-from-a-zendesk-app/#benefits-of-using-a-zendesk-proxy-server).
     10. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     11. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Zendesk connection:

     * Username and password (Deprecated)
     * API token
     * OAuth 2.0 - Authorization code

To understand how to configure these authentication types, see Configure authentication.

  2. Click **Next**.


* If you have enabled the event subscription, the **Event Subscription Details** section appears on the connection creation page. To understand how to configure event subscription details, see Configure event subscription.
* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password (Deprecated)**
    * **Username** : The Zendesk username to use for the connection.
    * **Password** : Secret Manager secret containing the password associated with the Zendesk username.
  * **API token**
    * **User** : The Zendesk user account used to authenticate.
    * **API token** : The API token of the authenticated user.
    * **Secret version** : Secret version for the secret.
  * **OAuth 2.0 - Authorization code**
    * **Client ID** : The client id provided by connector for the app you created.
    * **Scopes** : A comma-separated list of desired scopes.
    * **Client secret** : Secret Manager Secret containing the client secret for the connected app you created.
    * **Secret version** : Secret version for the secret.
    * **Authorization URL** : Authorization URL generated when creating client in Zendesk instance.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.




### Configure event subscription

If you have enabled the event subscription, enter the following values in the **Event Subscription Details** section:

  1. Select a **Destination Type**. 
     * **Host address** : Enter the registration URL of your backend system in the **host** field.
  2. Select **API Token** as the authentication type. Do not select **Username and password**.
  3. Enter the authentication details. 
     1. **User** : The Zendesk user account used to authenticate.
     2. **API token** : The API token of the authenticated user. 
     3. **Secret version** : Secret version for the secret.
  4. Optionally, select **Enable data enrichment** if you want additional information to be appended to the backend system's response. 

The additional information is specific to the entity for which you have configured the event. For more information, see [Data enrichment in event notifications](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#data-enrichment-in-event-notifications). 

**Note:** If you have configured this connection for only event subscription, you can't enable this option. To enable data enrichment, you must configure the connection for both event subscription and connector operations (entities and actions).
  5. Select **Enable private connectivity** for secured connectivity between your backend application and your connection. If you select this option, you must perform additional configuration steps after creating the connection. For more information, see [Private connectivity for event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#psc-eventing). 
  6. Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
     1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
     2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.
  7. If you want to use a proxy to connect to your backend (for event subscription), enter the following details: 
     1. **Proxy SSL Type** : The SSL type to use when connecting to the proxy server. Select any of the following authentication types: 
        * **Always** : The connection is always SSL enabled for event subscription.
        * **Never** : The connection is not SSL enabled for event subscription.
     2. **Proxy Auth Scheme** : Select the authentication type to authenticate with the proxy server. The following authentication types are supported: 
        * **Basic** : Basic HTTP authentication.
     3. **Proxy User** : Enter the user name to be used to authenticate with the proxy server.
     4. **Proxy Password** : Select the Secret Manager secret of the user's password.
     5. **Secret version** : Select the secret version. 
     6. In the **Proxy Server** section, enter details of the proxy server. 
        1. Click **\+ Add destination** , and then select the **Destination Type** as **Host address**.
        2. Enter the proxy server's hostname or IP address, and the proxy server's port number.

**Tip:** To understand how you can use event subscription in your integrations, see [Zendesk trigger](https://docs.cloud.google.com/application-integration/docs/configure-zendesk-trigger). 

### Connection configuration samples

### Basic authentication connection type (Deprecated)

Field name | Details  
---|---  
Location | us-east4  
Connector | Zendesk  
Connector version | 1  
Connection Name | CONNECTION_NAME  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Host | HOST_ADDRESS  
UserPassword | Yes  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
  
### API Token connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Zendesk  
Connector version | 1  
Connection Name | zendesk-apitoken  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host Address  
Host1 | https://yoursubdomain.zendesk.com  
Authentication | Api Token  
User | UserName  
API Token | Api Token provided by your app  
Secret version | 1  
  
### OAuth 2.0 - Authorization code connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Zendesk  
Connector version | 1  
Connection Name | zendesk-auth-code  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host Address  
Host1 | https://yoursubdomain.zendesk.com  
Authentication | OAuth 2.0 - Authorization code  
Client Id | CLIENT_ID  
Scopes | Required Scopes as your use-case  
Client Secret | CLIENT_SECRET  
Secret version | 1  
Authorization URL | https://d3v2one1625553311.zendesk.com/oauth/authorizations/new  
  
Connection to Zendesk uses SSL by default, and no additional configuration is needed if you're using the standard Zendesk URL, such as https://yoursubdomain.zendesk.com.

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

The Zendesk connector can process 5 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

The Zendesk connector provides actions to manage your tickets based on the `ticket ID`. To understand how to configure the actions, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Delete a ticket

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteTicketsPermanently` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Id": "18"
         }

This example deletes the ticket permanently. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": "true"
    }] 


**Note:** The `DeleteTicketsPermanently` operation permanently deletes a record. If you want to perform a soft delete, use the Entity delete operation.

### Example - Merge tickets

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MergeTickets` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Id": "25",
           "Id": "26"
         }

This example merges the two tickets. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": null,
      "Message": null
    }] 




### Example - Restore a ticket

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RestoreTicket` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "id": "20"
         }

This example restores a ticket. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": "true"
    }] 




### Example - Recover a suspended ticket

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RecoverSuspendedTicket` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "id": "18726501985809"
         }

This example recovers the suspended ticket. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Id": "60921"
    }]




## Entity operation examples

### Example - List operation on Tickets

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Tickets` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.

You can perform List operation on the following entities:

Attachments, Ticket Comments, Ticket Forms, Ticket Fields, Requests, Ticket Audits, Ticket Metrics, Suspended Tickets, Sharing Agreements, Users, UserIdentities, UserRelatedInformation, UserFields, OrganizationFields, and JobStatus




### Example - Get operation on Tickets

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Tickets` from the `Entity` list.
  3. Select the `Get` operation, and then click**Done**.
  4. Here, the entityId is set to 34.0. To set the entityId, in the **Task Input** section of the **Connectors** task, click `entityId` and then enter 34.0 in the `Default Value` field.

You can perform Get operation on the following entities:

Ticket Forms, Ticket Fields, Requests, Ticket Audits, Suspended Tickets, User Fields, UserIdentities, and Users




### Example - Create operation on Tickets

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Tickets` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Subject": "Zendesk_Create_Ticket",
             "RawSubject": "Zendesk_Create",
             "Description": "this ticket is related to application integration Create operation",
             "Type": "incident",
             "Priority": "urgent",
             "Status": "open",
             "Recipient": null,
             "HasIncidents": false,
             "DueAt": null,
             "RequesterId": 3.84625885158E11,
             "SubmitterId": 3.84625883418E11,
             "AssigneeId": 3.84625883418E11,
             "OrganizationId": "16665992392721",
             "GroupId": 3.60008282358E11,
             "TicketFormId": 3.60001719218E11,
             "BrandId": 3.60003285058E11,
             "Tags": null,
             "ViaChannel": "web",
             "ViaSource": "{\r\n  \"from\": null,\r\n  \"to\": null,\r\n  \"rel\": null\r\n}",
             "CustomFields": null,
             "SatisfactionRating": null,
             "SharingAgreementIds": null,
             "AllowChannelback": false,
             "IsPublic": true,
             "Url": "https://altostrat.zendesk.com/api/v2/tickets/1.json"
           }
           

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
             "Id": 38.0
           }
           




### Example - Create operation on TicketForms

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TicketForms` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Name": "Altostrat_Zendesk1",
             "RawName": "Altostrat_Zendesk1",
             "DisplayName": "Altostrat_Issues1",
             "RawDisplayName": "Altostrat_Issues1",
             "Position": 2.0,
             "Active": true,
             "EndUserVisible": true,
             "Default": false,
             "InAllBrands": true,
             "RestrictedBrandIds": null,
             "FallbackToDefault": null,
             "AssociatedToBrand": null
           }
           

If the integration is successful, the `TicketForms` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id":1.8104712053393E13
           }
           




### Example - Create operation on TicketFields

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TicketFields` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Type": "text",
             "Title": "New field created",
             "RawTitle": null,
             "Description": "Please create the new field",
             "RawDescription": null,
             "Position": 2.0,
             "Active": true,
             "Required": false,
             "CollapsedForAgents": false,
             "RegexpForValidation": null,
             "VisibleInPortal": true,
             "EditableInPortal": true,
             "Tag": null,
             "CreatedAt": "2021-07-06 06:35:19.0",
             "UpdatedAt": "2021-07-06 06:35:19.0",
             "SystemFieldOptions": null,
             "CustomFieldOptions": null,
             "Removable": false
           }
           

If the integration is successful, the `TicketFields` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id": 1.7139061374865E13
           }
           




### Example - Create operation on SharingAgreements

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SharingAgreements` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Name": "altostrat.zendesk.com",
             "RemoteSubdomain": "altostrat"
           }
           

If the integration is successful, the `SharingAgreements` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id": 1.7142672288273E13
           }
           




### Example - Create operation on Users

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Email": "cloudysanfrancisco@gmail.com",
             "Name": "Altostrat Team"
           }
           

If the integration is successful, the `Users` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id": 1.7156912480273E13
           }
           




### Example - Create operation on UserIdentities

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `UserIdentities` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UserId": 3.84637722338E11,
             "Type": "email",
             "Value": "cloudysanfrancisco@gmail.com",
             "Verified": false,
             "Primary": true,
             "DeliverableState": "reserved_example",
             "Url": "https://d3valtostrat1625553311.zendesk.com/api/v2/users/384637722338/identities/368240277818.json"
           }
           

If the integration is successful, the `UserIdentities` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id": 1.6961185982353E13
           } 
           




### Example - Create operation on UserFields

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `UserFields` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Title": "Support description",
             "Type": "text",
             "Key": "support_description"
           }
           

If the integration is successful, the `UserFields` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id": 1.7157236761873E13
           }
           




### Example - Update operation on Tickets

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Tickets` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Subject": "Google_Altostrat_Zendesk Update",
             "RawSubject": "Google_Altostrat_Zendesk Update",
             "Description": "this ticket is related to googlecloud application integration update check",
             "RequesterId": 1.6854335860497E13
           }
           

  5. Here, the entityId is set to 35.0. To set the entityId, click **entityId** , and then enter `35` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `35`.

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
               Id": 35.0
           }
           




### Example - Update operation on TicketForms

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TicketForms` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Name": "Ticketforms Updated",
             "DisplayName": "Altostrat_Issues1",
             "RawDisplayName": "Altostrat_Issues1"
           }
           

  5. Here, the entityId is set to 1.7137314972689E13. To set the entityId, click **entityId** and then enter `1.7137314972689E13` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `1.7137314972689E13`.

Running This example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               Id": 1.7137314972689E13
           }
           




### Example - Update operation on TicketFields

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TicketFields` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Description": "Updated description for testing"
           }
           

  5. Here, the entityId is set to 3.60022990118E11. To set the entityId, click **entityId** and then enter `3.60022990118E11` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `3.60022990118E11`.

Running This example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               Id": 3.60022990118E11
           }
           




### Example - Update operation on Users

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Name": "The Customer update",
             "Last Name": "Alex",
             "First Name": "Charlie"
           }
           

  5. Here, the entityId is set to 3.84625885158E11. To set the entityId, click **entityId** and then enter `3.84625885158E11` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `3.84625885158E11`.

Running This example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               Id": 3.84625885158E11
           }
           




### Example - Update operation on UserFields

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `UserFields` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Title": "Support description updated",
             "Type": "text",
             "Key": "support_description"
           }
           

  5. Here, the entityId is set to 1.7157236761873E13. To set the entityId, click **entityId** and then enter `1.7157236761873E13` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `1.7157236761873E13`.

Running This example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               Id": 1.7157236761873E13
           }
           




### Example - Update operation on UserIdentities

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `UserIdentities` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Verified": true
           }
           

  5. In this entity, the Update operation can be performed by using filter clause and composite primary keys hence entityId is not required.

Instead of specifying the **entityId** , you can also set the **filterClause** as ` UserId='384625885158' and Id='368234205078'` .

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    {
        "Id": 3.68234205078E11
      }
      




### Example - Delete operation on Tickets

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Tickets` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Here, the entityId is set to 35.0. To set the entityId, in **Task Input** section of the **Connectors** task, click **entityId** and then enter `35` in the **Default Value** field.

You can perform Delete operation on the following entities:

Ticket Fields, Suspended Tickets, UserIdentities, User Fields, and Users




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the Zendesk connection in an integration

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
