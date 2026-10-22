---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/apachecouchdb/configure/
title: Apache CouchDB \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:29.379019+00:00
---

# Apache CouchDB  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/apachecouchdb/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Apache CouchDB

The Apache CouchDB connector lets you perform insert, delete, update, and read operations on a [CouchDB database](https://couchdb.apache.org/).

## Before you begin

Before using the Apache CouchDB connector, do the following tasks:

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
     1. **Connector** : Select **Apache CouchDB** from the drop down list of available Connectors.
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
     8. **Flexible Schema** : Set FlexibleSchema to true to scan for additional metadata on the query result set. Otherwise, the metadata will remain the same. 
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
     10. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     11. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **NEXT**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Apache CouchDB connection:

     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Apcache CouchDB connection.

Ensure that you have an admin user role to authenticate to Apache CouchDB.

For information about Apache CouchDB, see [Quickstart with Apache CouchDB](https://docs.couchdb.org/en/stable/intro/index.html). For more information about Apache CouchDB platform, see [Apache CouchDB platform overview](https://docs.couchdb.org/en/stable/api/index.html). For information about Apache CouchDB SSL configuration, see [Apache CouchDB 3.5.2. HTTPS (SSL/TLS) Options](https://docs.couchdb.org/en/stable/config/http.html) and [How Do I Configure SSL (HTTPS) in Apache CouchDB?](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=48203146).

### Basic authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Apache CouchDB  
Connector version | 1  
Connection Name | couchdb-vm-connection  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
List Views | Yes  
Flexible Schema | Yes  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type(Server) | Host address  
Host address | http://198.51.100.0  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
  
### Proxy connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Apache CouchDB  
Connector version | 1  
Connection Name | couchdb-proxy-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
List Views | No  
Flexible Schema | No  
Proxy | use proxy  
Proxy Auth Scheme | Digest  
Proxy User | PROXY_USER  
Proxy Password | PROXY_PASSWORD  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type(Server) | Host address  
Host address | http://198.51.100.0  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
  
### SSL connection (insecure) connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Apache CouchDB  
Connector version | 1  
Connection Name | couchdb-ssl-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
List Views | No  
Flexible Schema | No  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Trust store (choose the trust model) | Insecure Connection  
Destination Type(Server) | Host address | Host address | http://198.51.100.0  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
  
### SSL connection (private) connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Apache CouchDB  
Connector version | 1  
Connection Name | couchdb-proxy-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
List Views | No  
Flexible Schema | No  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Trust store (choose the trust model) | Private  
Custom Trust store | Self-signed certificate.  
Secret Version | 1 | Destination Type(Server) | Host address | Host address | https://198.51.100.0  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
  
### JWT Authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Apache CouchDB  
Connector version | 1  
Connection Name | couchdb-vm-jwt-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
List Views | No  
Flexible Schema | No  
Proxy | No  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type(Server) | Host address  
Host address | http://203.0.113.0  
JWT Subject | admin  
JWT Algorithm | HS256  
JWT Key Type | Symmetric  
JWT Key | JWT_KEY  
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

The Apache CouchDB connector can process a maximum of 5 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Entity operation examples

### Example - List all customer records

This example lists all customer records in the `Customer` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.
  4. Optionally, you can enter values in the [filterClause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter) to filter the result set.



### Example - Get a customer record

This example gets a specific customer record from the `Customers` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customers` from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `cust-2` in the **Default Value** field. 

Here, `cust-2` is the primary key value of the `Customers` entity.




### Example - Add a customer

This example creates a customer record in the `Customers` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customers` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "name": "John",
         "_id": "cust-3"
         }

If the integration is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "_id": cust-3
         }




### Example - Update a customer record

This example updates the specified customer record in the `Customers` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customers` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "name": "Jason",
             }
             

  5. Click **entityId** , and then enter `cust-5` in the **Default Value** field. 

Alternately, instead of specifying the **entityId** , you can also set the [filterClause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter) to `cust-5`.

If the integration is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "_id": cust-5
         }
             




### Example - Delete a customer record

This example deletes the specified customer record from the `Customers` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customers` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `cust-6` in the **Default Value** field. 



## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
flexible_schema | BOOLEAN | False | Set FlexibleSchema to true to scan for additional metadata on the query result set. Otherwise, the metadata will remain the same.   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the Apache CouchDB connection in an integration

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
