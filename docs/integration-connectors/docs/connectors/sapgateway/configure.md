---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/sapgateway/configure/
title: SAP Gateway \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:06.808659+00:00
---

# SAP Gateway  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/sapgateway/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SAP Gateway

The SAP Gateway connector lets you perform insert, delete, update, and read operations on SAP Gateway database.

## Supported versions

This connector uses the SAP Gateway API to enable bidirectional access to SAP services that use the gateway. The following SAP editions are supported:

  * S/4 HANA Cloud
  * S/4 HANA
  * SAP ERP
  * Any other SAP editions that support the SAP Gateway API



## Before you begin

Before using the SAP Gateway connector, do the following tasks:

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




## Configure SAP OData Service on S/4HANA on-premise

To configure SAP OData Service on S/4HANA on-premise, do the following tasks:

  * Enable ICM Services
  * Activate SAP Gateway
  * Activate OData services
  * Test activated OData service on SAP server



### Enable ICM Services

The SAP OData service functions over HTTP or HTTPS protocols. Therefore, ensure that the relevant services are enabled in the Internet Communication Manager (ICM). Use HTTPS to protect data during transmission.

  1. Go to Transaction SMICM.
  2. Goto Services.
  3. Click **Service****>** **Create**.
  4. Define new service.

When you define service ports, some parameters are pre-populated based on the SAP system.

  5. Set the remaining parameters for HTTP and HTTPS protocols.



### Activate SAP Gateway

To activate SAP Gateway, perform the following steps:

  1. Go to transaction SPRO and select **SAP Reference IMG**.
  2. Expand the node SAP NetWeaver > SAP Gateway > OData Channel > Configuration > User Settings > Connection Settings > Activate or Deactivate SAP Gateway and then right-click and select **Edit Activity**.
  3. Click **Activate**. If the **SAP Gateway is currently active** message appears in the dialog, click **Cancel**.



### Activate OData services

To activate OData services, perform the following steps.

  1. Go to transaction **SICF**.
  2. Click **Execute** (or press F8).
  3. Skip **Filter** in selection screen.
  4. Navigate to tree node **default_host > sap > opu > OData** to activate all OData (V2, V4) services.
  5. Navigate to the corresponding node deeper in the tree to activate an individual service.
  6. Right-click on the OData service node and select **Activate**.



### Test the activated OData service on SAP server

Use the SAP Gateway Client tool to execute OData requests.

Call the following transaction to start the tool: **/n/IWFND/GW_CLIENT**

  1. Specify the OData request URI.
  2. Select the HTTP method, the protocol (HTTP or HTTPS), the request headers and the request body.
  3. Click **Execute** to send the request after you enter all necessary request data.

The response headers and response data are displayed after execution.




## Configure SAP OData Service on S/4HANA Cloud

To configure SAP OData Service on S/4HANA Cloud, do the following tasks:

  * Create communication user
  * Create communication system
  * Create communication arrangement



### Create communication user

**Communication user** is a special type of technical user used for external OData service calls. It is used for SAP communication with the external system only, it is not possible to log on using SAP GUI using communication user. The Maintain Communication Users app enables you to define these settings in Cloud.

  1. Go to **Maintain Communication Users** App.
  2. Click **New** to create a new user.
  3. Enter **user name** and **description** of your user.
  4. Enter the password. Use **propose password** to generate the password.
  5. Click **Create**.



### Create communication system

A **communication system** is a specification of a system that represents a communication partner and all the necessary technical information needed for the communication, such as hostname/IP-Address, identity, user information, and certificates. In S/4HANA Cloud systems, these entities are required for external communication. The Communication Systems app enables you to define these settings in Cloud.

  1. Go to **Communication Systems** App.
  2. Click **New** to create a new communication system.
  3. Enter **system ID** and **system name**.
  4. Click **+** to add the created communication user for inbound communication. Enter the details of communication user.

Inbound communication means that defined system is used from a communication partner to call from external into the SAP S/4HANA system.

  5. Click **Save**.



### Create communication arrangement

For information about communication arrangement, see [ Communication Arrangement](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/data-exchange-in-s-4hana-cloud-using-communication-scenarios/ba-p/13323892#:~:text=settings%20in%20Cloud.-,Communication%20Arrangements,ports%2C%20destinations%2C%20and%20URLs).

  1. Go to **Communication Arrangements** App.
  2. Click **New** to create a new communication arrangement.
  3. Select your **communication scenario** , enter **arrangement name** and click **Create**.

**Communication scenario** defines a set of inbound and outbound services for a business process.  
Inbound services are Web services that have been created based on an SAP or custom business object, or Web services provided by SAP.  
Outbound services are external Web services that have been integrated into your solution.  
Based on a communication scenario, a customer can create a communication arrangement in SAP cloud solution to exchange business documents electronically.  
For Example, Standard communication scenario SAP_COM_0053 is used for purchase order integration with SAP system.  
API API_PURCHASEORDER_PROCESS_SRV is exposed in this scenario to create, delete or update purchase order.

  4. Add your **communication system** and select the **communication user** to use in this communication arrangement.
  5. URL to call OData service can be found in Communication arrangement in this format:https://-api.s4hana.ondemand.com/sap/opu/odata/sap/
  6. Click **Save**



## Configure connection

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **SAP Gateway** from the drop down list of available Connectors.
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
     7. **Namespace** : Specify the service namespace you want to retrieve data from. This is required if the service is not specified in the URL. 
     8. **Service** : Specify the service you want to retrieve data from. This is required if the service is not specified in the URL. 
     9. **CustomUrlParams:** Specify custom query string parameters that are included with the HTTP request. The parameters must be encoded as a query string in the following format: `field1=value1&field2=value2`. The values in the query string must be URL encoded. 
     10. **Data Format** : The data format to retrieve data in. Select either XML or JSON. 
     11. **Use Display Names** : Boolean determining whether or not to use SAP labels. 
     12. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     13. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     14. Click **NEXT**.
  5. In the **Destinations** section, set the URL of your SAP Gateway environment or to the full URL of the OData service. For example format; `${ENVIRONMENT_URL}/sap/opu/odata/${NAMESPACE}/${SERVICE}/` and sample URL is `https://sapes5.sapdevcenter.com/sap/opu/odata/IWBEP/GWSAMPLE_BASIC/`. Add any additional properties using the **CustomUrlParams** property. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **NEXT**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the SAP Gateway connection:

     * Username and password
     * Anonymous
     * OAuth 2.0 auth code flow
     * SAP BTP (OAuth 2.0 - client credentials)

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.


  * **Anonymous**

If you want to use anonymous login, select **Not Available**.

    * **API Key** : The API key of the currently authenticated user.


  * **OAuth 2.0 auth code flow**
    * **Client ID** : Enter the client ID obtained from the API client page.
    * **Scopes** : Enter a comma-separated list of desired scopes.
    * **Client Secret** : Enter the client secret obtained from the API client page.
    * **Secret version** : Enter the secret version for the **Client Secret** selected.
    * **Authorization URL** : Enter the authorization URL generated when you create an OAuth client in your SAP Gateway instance.
    * **Enable Authentication Override** : Select to enable the connection to accept a different authentication dynamically during runtime.


  * **SAP BTP (OAuth 2.0 - client credentials)**
    * **Client ID** : Enter the client ID obtained from the API client page.
    * **Client Secret** : Enter the client secret obtained from the API client page.
    * **Secret version** : Enter the secret version for the secret selected above.
    * **OAuthAccessTokenURL** : Enter the URL of the OAuth access token.
    * **Destination Name** : Enter the name of the SAP BTP destination.
    * **Destination URL** : Enter the destination URL of the SAP BTP.
    * **Enable Authentication Override** : Select this option to enable the connection to accept a different authentication dynamically during runtime.



### Configure event subscription

If you have enabled the event subscription, enter the following values in the **Event Subscription Details** section:

  1. Select any one of the following authentication types for the event listener. **Note:** Before you configure authentication, ensure that you have the event listener endpoint, which is available to you after you create the connection. To view the endpoint, go to the [All connections](https://console.cloud.google.com/connectors/connections) page, and then click the connection that you wan to view. The endpoint is displayed in the **Connection Details** section.
     * [Google Authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt). If you enable this option, follow the steps in [Authenticate by using JSON Web Tokens](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt#configure-google-auth) to configure the authentication for ABAP SDK. Also, ensure that the service account has [roles/connectors.listener](https://cloud.google.com/iam/docs/roles-permissions/connectors) role whose access token is used for authentication.
     * [API Key Authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys). If you select this option, you must have created an API key, and then saved the key as a Secret Manager secret. For more information, see [Create an API key](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys#ssf-create-api-key).
  2. Enter the event type field name. This field identifies the type of event associated with the incoming event request. 
         
         {
         "event_type": "user.created",
         ...
         // other request fields
         ...
         }

  3. Select **Enable private connectivity** for secured connectivity between your backend application and your connection. If you select this option, you must perform additional configuration steps after creating the connection. For more information, see [Private connectivity for event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#psc-eventing). 
  4. Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
     1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
     2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.

**Tip:** To understand how you can use event subscription in your integrations, see [SAP Gateway trigger](https://docs.cloud.google.com/application-integration/docs/configure_sap_gateway_trigger). 

## Connection configuration samples

This section provides the sample values for the various fields that you configure when you create a SAP Gateway connector.

### Basic authentication - connection type

Field Name | Details  
---|---  
Region | us-central1  
Connector | SAP Gateway Connector  
Connector Version | 1  
Connector Name | sapgateway-basicauth-conn  
Service Account | SERVICE_ACCOUNT-compute@developer.gserviceaccount.com  
Data Format | JSON  
Verbosity Level | 5  
Host Address | http://192.0.2.0/sap/opu/odata/sap/HOST_ADDRESS  
Authentication: |  User Password  
Username | username  
Password | password  
versions | 1  
  
### API Token - connection type

Field Name | Details  
---|---  
Region | us-central1  
Connector |  SAP Gateway Connector  
Connector Version | 1  
Connector Name | sapgateway-api-token-conn  
Service Account | SERVICE_ACCOUNT-compute@developer.gserviceaccount.com  
Data Format | JSON  
Verbosity Level | 5  
Host Address | http://192.0.2.0/sap/opu/odata/sap/HOST_ADDRESS  
API Key | API_KEY-example-pet-store.com  
versions | 1  
  
### Proxy - connection type

Field Name | Details  
---|---  
Region | us-central1  
Connector |  SAP Gateway Connector  
Connector Version | 1  
Connector Name | sapgateway-basicauth-conn  
Service Account | SERVICE_ACCOUNT-compute@developer.gserviceaccount.com  
Data Format | JSON  
Verbosity Level | 5  
Host Address | http://192.0.2.0/sap/opu/odata/sap/HOST_ADDRESS  
Data Format: | JSON  
Verbosity Level: | 5  
Proxy | True  
Proxy SSL Type | Auto  
Proxy Server |  34.148.1.XX:XXXX  
Host Address: | http://192.0.2.0/sap/opu/odata/sap/HOST_ADDRESS  
Authentication: | User Password  
Username | username  
Password: | password  
Versions | 1  
  
### OAuth 2.0 auth code flow - connection type

Field Name | Details  
---|---  
Region | us-central1  
Connector | SAP Gateway Connector  
Connector Version | 1  
Namespace | sap  
Service | API_SALES_ORDER_SRV  
Data Format | JSON  
Host Address | https://Host:Port  
Authentication | OAuth 2.0  
Client ID | sb-cloneae083fa9a39742e88774df43216a5dbc!b366296|destination-xsappname!b62  
Client Secret | projects/617888503870/secrets/gateway-oauth/versions/1  
Scopes | ZAPI_SALES_ORDER_SRV_0001  
Authorization URL | https://HostIp:Port/sap/bc/sec/oauth2/authorize  
Versions | 1  
  
### SAP BTP (OAuth 2.0 - client credentials) - connection type

Field Name | Details  
---|---  
Region | us-central1  
Connector | SAP Gateway Connector  
Connector Version | 1  
Connector Name | sap-gateway-oauth-client-connection  
Service Account | SERVICE_ACCOUNT-compute@developer.gserviceaccount.com  
Data Format | JSON  
Host Address: | https://my-api.s4hana.cloud.sap/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV | Authentication: | SAP BTP  
Client ID | CLIENT_ID  
Client Secret | CLIENT_SECRET  
OAuthAccessTokenURL | https://atrial.authentication.us10.hana.ondemand.com/oauth/token  
Destination Name | DESTINATION_NAME  
Destination URL | https://destination-configuration.cfapps.us10.hana.ondemand.com/destination-configuration/v1/destinations/Google  
Versions | 1  
  
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

  * The SAP Gateway connector can process a maximum of 9 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg). 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 
    * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
    * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).

The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

  * The following features aren't supported: 
    * Etags
    * Deep insert
    * File based operations



## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all records

This example lists all the records in the `SalesOrderSet` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesOrderSet` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). For example, `City='Bangalore'`. You can also specify multiple filter conditions by using the logic operators. For example, `City='Bangalore' and region='asia-south2'`. 



### Example - Get a record

This example gets a record with the specified ID from the `SalesOrderSet` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesOrderSet` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `13` in the **Default Value** field. 

Here, `13` is a primary key value in the `SalesOrderSet` entity.




### Example - Create a record

This example creates a record in the `SalesOrderSet` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesOrderSet` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Vbeln":"999",
         "Erdat":"2020-08-25 00:00:00",
         "Erzet":"13:12:31",
         "Ernam":"Test"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Vbeln": "999"
         }




### Example - Create a record

This example creates a record in the `SalesPriceSet` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesPriceSet` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Vbeln": "129",
         "Posnr": "000000",
         "Knumh": "SUN25MAY",
         "Kpein": 1.0
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Posnr": "000000",
         "Vbeln": "129"
         }




### Example - Update a record

This example updates a record in the `SalesOrderSet` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesOrderSet` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Ernam": "Test123"
         }

  5. Click **entityId** , and then enter `99` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Vbeln": "999"
         }




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
namespace | STRING | False | Specify the service namespace you want to retrieve data from. This is required if the service is not specified in the URL.   
service | STRING | False | Specify the service you want to retrieve data from. This is required if the service is not specified in the URL.   
custom_url_params | STRING | False | The CustomUrlParams allow you to specify custom query string parameters that are included with the HTTP request. The parameters must be encoded as a query string in the form field1=value1&field2=value2. The values in the query string must be URL encoded.   
data_format | ENUM | False | The data format to retrieve data in. Select either XML or JSON. Supported values are: XML, JSON  
use_display_names | BOOLEAN | False | Boolean determining whether or not to use SAP labels.   
verbosity | STRING | False | Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates).   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the SAP Gateway connection in an integration

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
