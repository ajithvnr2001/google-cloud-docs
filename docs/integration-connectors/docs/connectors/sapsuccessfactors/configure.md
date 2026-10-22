---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/sapsuccessfactors/configure/
title: SAP SuccessFactors \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:58.584803+00:00
---

# SAP SuccessFactors  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/sapsuccessfactors/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SAP SuccessFactors

The SAP SuccessFactors connector lets you perform insert, delete, update, and read operations on [SAP SuccessFactors](https://www.sap.com/products/hcm.html/) data.

## Before you begin

Before using the SAP SuccessFactors connector, do the following tasks:

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

  * To create a paid SuccessFactors account using SAP ID, see [Quickstart with SAP SuccessFactors](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM).



## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **SAP SuccessFactors** from the drop down list of available Connectors.
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
     8. **Company Id** : Unique identifier of your company. This is required to authenticate. 
     9. **Data Format** : The data format to retrieve data in. Select either ATOM or JSON. 
     10. **Include Navigation Properties** : A boolean indicating if navigation properties should be included in the column listing. 
     11. **Purge Type** : PurgeType is an optional parameter that determines whether an incremental or full update will be performed on an entity. 
     12. **Use Client Side Paging** : Whether or not the CData ADO.NET Provider for SAP SuccessFactors should use client side paging. 
     13. **Use Display Names** : Boolean determining whether or not to use SAP labels. 
     14. **Use proxy** : This indicates whether to use the system proxy settings or not. This takes precedence over other proxy settings, so you'll need to set ProxyAutoDetect to FALSE in order use custom proxy settings. 
     15. **Proxy Auth Scheme** : The authentication type to use to authenticate to the ProxyServer proxy. 
     16. **Proxy User** : A user name to be used to authenticate to the ProxyServer proxy. 
     17. **Proxy Password** : A password to be used to authenticate to the ProxyServer proxy. 
     18. **Proxy SSL Type** : The SSL type to use when connecting to the ProxyServer proxy. 
     19. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     20. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     21. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+Add destination**.

  6. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the SAP SuccessFactors connection:

     * Username and password
     * OAuth SAML2

To understand how to configure these authentication types, see Configure authentication.

  2. Optional: Select **Enable authentication override** to dynamically use different authentication details at runtime.
  3. Click **Next**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : The username for the connector.
    * **Password** : The _Secret Manager Secret_ containing the password associated with the connector.
    * **Secret version** : The version of the _Secret Manager Secret_ containing the password.
    * **Auth scheme** : The scheme used for authentication.
  * **OAuth SAML2**
    * **Private key** : The private key part of the **X.509 certificate** downloaded from SAP SuccessFactors.
    * **Client ID** : The client ID (API key) generated during SAP SuccessFactors OAuth client app registration.
    * **User** : The SuccessFactors user ID bound to the OAuth client.

For details on how to obtain the Client ID and Private key, see Obtain Client ID and Private key.




### Basic authentication connection type sample

The following table lists the sample configuration values for the basic authentication connection type. Refer to the connection creation interface in the console to know the mandatory and optional fields.

Field name | Sample value  
---|---  
Region | us-central1 | Connector | SAP SuccessFactors  
Connector version | 1  
Connection name | sapsf-basicauth-conn  
Description | SuccessFactors connection  
Service account | SERVICE_ACCOUNT_NAME@developer.gserviceaccount.com  
Company ID | SFPART068178  
Host address | https://HOST_NAME.successfactors.eu/  
Username | sfadmin  
Password | PASSWORD  
Auth scheme | Basic  
  
### Obtain Client ID and Private key

To obtain the Client ID and Private Key, follow these steps in your SAP SuccessFactors instance:

**Note:** This is a third party configuration. Google doesn't manage your SAP SuccessFactors instance.

  1. Log in as an administrator to your SuccessFactors account.
  2. Navigate to **Admin center**.
  3. In the **Tools** pane, search for and click **Manage OAuth2 client applications**.
  4. On the **Manage OAuth2 client applications** page, click **Register client application**.
  5. On the app registration page, enter the following mandatory details: 
     1. **Application name** : A unique name of your OAuth client.
     2. **Application URL** : A unique URL of the page that the client wants to display to the end user. The URL must begin with `https://`.
  6. Click **Generate X.509 certificate**.
  7. On the certificate generation page, enter a **Common name (CN)** and click **Generate**.
  8. You are redirected to the app registration page. Click **Download** to download the generated certificate bundle (often a `.pem` file, for example, `certificate.pem`), which contains the public certificate and the private key. 
  9. Click **Register** to register the client application.
  10. Return to the OAuth client application list, click **View** on the newly created application, and copy the **API key** , which is your **Client ID**.
  11. Open the downloaded `.pem` file in a text editor and copy the portion between `-----BEGIN ENCRYPTED PRIVATE KEY-----` and `-----END ENCRYPTED PRIVATE KEY-----`, which is your **Private key**.



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

The SAP SuccessFactors connector can process 10 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists all the actions supported by the SuccessFactors connection.

### UpsertEntity action

This action lets you upsert a record for an entity.

#### Input parameters of the UpsertEntity action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
entityType | string | True | Entity type to be upserted.  
payload | object | True | Upsert payload in the json format.  
  
#### Output parameters of the UpsertEntity action

This action returns the status 200 (OK) with a response body indicating all Upsert results.

For example on how to configure the `UpsertEntity` action, see Examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Update a record in the PerPersonal entity

The following example updates a record in the `PerPersonal` entity.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpsertEntity` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "entityType": "PerPersonal",
         "payload": {
           "personIdExternal": "109031",
           "startDate": "1800-01-01 00:00:00.0",
           "firstName": "John",
           "lastName": "Job",
           "nationality": "IND"
           }
         }

If the action is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
      "personIdExternal": "109031",
      "startDate": "1989-12-31 23:00:00.0"
    }]




### Example - Update a record in the PaymentInformationDetailV3 entity

The following example updates a record in the `PaymentInformationDetailV3` entity.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpsertEntity` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "entityType": "PaymentInformationDetailV3",
           "payload": {
             "PaymentInformationV3_effectiveStartDate": "2015-01-21 00:00:00.0",
             "PaymentInformationV3_worker": "82096",
             "externalCode": 563.0,
             "currency": "EUR"
           }
         }

If the action is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
      "externalCode": 563.0,
      "PaymentInformationV3_effectiveStartDate": "2015-01-20 23:00:00.0",
      "PaymentInformationV3_worker": "82096"
    }]




### Example - Create a record in an entity

The following example creates a record in the `TodoEntryV2` entity.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpsertEntity` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "entityType": "TodoEntryV2",
           "payload": {
             "todoEntryName": "Finish Your Tasks",
             "status": 1.0,
             "categoryId": "41",
             "LinkeduserNav": {
               "__metadata": {
                 "uri": "https://apisalesdemo2.successfactors.eu/odata/v2/User('613577712')",
                 "type": "SFOData.User"
               }
             }
           }
         }

If the action execution is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
      "todoEntryId": 221443.0
    }] 




## Entity examples

### Example - List records of an entity

This example lists the records of the `FOCompany` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `FOCompany` from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per your requirement. 

For example, setting the filter clause to `externalCode='5100' and startDate='1900-01-01 00:00:00'`, lists only those records whose externalCode is 5100 and startDate is 1900-01-01 00:00:00.




### Example - Get a record from an entity

This example fetches a record from the `User` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `User` from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `103032` in the **Default Value** field. 

Here, `103032` is the primary key of the `Users` entity.




### Example - Delete a record from an entity

This example deletes a record from the `FOCompany` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `FOCompany` from the `Entity` list.
  3. Select the `DELETE` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `113132` in the **Default Value** field. 

Alternately, if the entity has composite primary Keys instead of specifying the **entityId** , you can set the **filterClause**. For example, `externalCode='5100' and startDate='1900-01-01 00:00:00'`.




### Example - Create a record in an entity

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `FOCompany` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "externalCode": "1000",
         "startDate": "1900-01-01 00:00:00.0",
         "standardHours": 40.0,
         "status": "I",
         "currency": "EUR",
         "country": "DEU"
         }

If the integration is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "externalCode": "1000",
         "startDate": "1900-01-01 00:00:00.0"
         }




### Example - Create a record in the TimeZone entity

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TimeZone` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "effectiveStartDate": "2023-08-16 00:00:00.0",
         "externalCode": "10013",
         "effectiveStatus": "A",
         "utcDstOffset": "UTC+01:00",
         "utcOffset": "+0100"
         }

If the integration is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "effectiveStartDate": "2023-08-16 00:00:00.0",
         "externalCode": "10013"
         }




### Example - Update a record in an entity

This example updates a record in the `FOCompany` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `FOCompany` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "description": "BestRun India"
         }

  5. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `103032` in the **Default Value** field. 

Alternately, if the entity has composite primary Keys instead of specifying the **entityId** , you can set the **filterClause**. For example, `externalCode='5100' and startDate='1900-01-01 00:00:00'`.

If the integration is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    {
    "externalCode": "5100",
    "startDate": "1900-01-01 00:00:00.0"
    }




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
company_id | STRING | True | Unique identifier of your company. This is required to authenticate.   
purge_type | STRING | False | PurgeType is an optional parameter that determines whether an incremental or full update will be performed on an entity.   
use_client_side_paging | BOOLEAN | False | Whether or not the CData ADO.NET Provider for SAP SuccessFactors should use client side paging.   
use_display_names | BOOLEAN | False | Boolean determining whether or not to use SAP labels.   
verbosity | STRING | False | Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates).   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the SAP SuccessFactors connection in an integration

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
