---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/elasticsearch/configure/
title: Elasticsearch \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:20.212484+00:00
---

# Elasticsearch  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/elasticsearch/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Elasticsearch

The Elasticsearch connector lets you connect to a [Elasticsearch](https://www.elastic.co/webinars/getting-started-elasticsearch) search engine and perform the supported search engine operations.

## Before you begin

Before using the Elasticsearch connector, do the following tasks:

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

  * For information about installing Elasticsearch on Linux, see [Install Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html).
  * For information about configuring SSL to secure Elasticsearch, see [Configure SSL](https://www.elastic.co/blog/configuring-ssl-tls-and-https-to-secure-elasticsearch-kibana-beats-and-logstash).



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
     1. **Connector** : Select **Elasticsearch** from the drop down list of available Connectors.
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
     8. **Client Side Evaluation** : Set ClientSideEvaluation to true to perform Evaluation client side on nested objects. 
     9. **Data Model** : Specifies the data model to use when parsing Elasticsearch documents and generating the database metadata. 
     10. **Max Results** : The maximum number of total results to return from Elasticsearch when using the default Search API. 
     11. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     12. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     13. Click **NEXT**.
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

The following authentication types are supported by the Elasticsearch connection:

     * Anonymous 
     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Anonymous**

If you want to use anonymous login, select **Not Available**.



  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.



### Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Elasticsearch connection.

#### SSL connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Elasticsearch  
Connector version | 1  
Connection Name | elastic-search-service-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Data Model | Relational  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Enable SSL | Yes  
Trust store Insecure Connection | Yes  
Key Store | Yes  
Client Certificate | CLIENT_CERTIFICATE  
Secret version | 1  
Client Private Key | CLIENT_PRIVATE_KEY  
Secret version | 1  
Destination Type(Server) | Host address  
Host address | https://192.0.2.0  
Port | 9200  
Authentication | Yes  
User Password | Yes  
Username | USERNAME  
Password | PASSWORD  
Secret version | 4  
  
#### PSC connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Elasticsearch  
Connector version | 1  
Connection Name | elasticsearch-psc-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Data Model | Relational  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type(Server) | Host address  
Host address | 192.0.2.0  
Port | PORT  
Authentication | Yes  
User Password | Yes  
Username | USERNAME/td>  
Password | PASSWORD  
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

The Elasticsearch connector can process 10 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### CreateIndex action

This action creates an index.

#### Input parameters of the CreateIndex action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
AliasFilter | String | No | Query DSL object used to limit documents that the alias can access.  
NumberOfShards | String | No | The number of primary shards that the created index should have.  
AliasIsWriteIndex | Boolean | No | Specifies if the alias index is writable.  
Alias | String | No | An alias for the index.  
AliasIndexRouting | String | No | Value used for the alias to route indexing operations to a specific shard. If specified, this overwrites the routing value for indexing operations.  
Index | String | Yes | The name of the index.  
NumberOfRoutingShards | String | No | Number used by Elasticsearch internally with the value from NumberOfShards to route documents to a primary shard.  
OtherSettings | String | No | A JSON object of settings. This setting can't be used in conjunction with NumberOfRoutingShards or NumberOfShards.  
Mappings | String | No | A JSON object specifying the mapping for the index.  
AliasIsHidden | Boolean | No | Specifies if the alias is hidden. All indices for the alias must have the same `is_hidden` value.  
AliasRouting | String | No | Value used for the alias to route indexing and search operations to a specific shard. May be overwritten by AliasIndexRouting or AliasSearchRouting for certain operations.  
  
#### Output parameters of the CreateIndex action

This action returns the status 200 (OK) if the action is successful.

To understand how to configure the `CreateIndex` action, see Action examples.

### ModifyIndexAliases action

This action modifies an index alias.

#### Input parameters of the ModifyIndexAliases action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Alias | String | No | The name of the alias. Multiple aliases are semi-colon separated.  
Filter | String | No | A filter to use when creating the alias. This takes the raw JSON filter using Query DSL. Multiple filters are semi-colon separated.  
Routing | String | No | The routing value to associate with the alias. Multiple routing values are semi-colon separated.  
SearchRouting | String | No | The routing value to associate with the alias for searching operations. Multiple search routing values are semi-colon separated.  
IndexRouting | String | No | The routing value to associate with the alias for indexing operations. Multiple index routing values are semi-colon separated.  
Action | String | Yes | The action to perform such as `add`, `remove`, or `remove_index`. Multiple actions are semi-colon separated.  
Index | String | Yes | The name of the index. Multiple indexes are semi-colon separated.  
  
#### Output parameters of the ModifyIndexAliases action

This action returns the status 200 (OK) if the action is successful.

To understand how to configure the `ModifyIndexAliases` action, see Action examples.

### ExecuteCustomQuery action

This action lets you execute a custom query.

To create a custom query, follow these steps: 

  1. Follow the detailed instructions to [ add a connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#add-a-connectors-task).
  2. When you [configure the connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#configure-the-connectors-task), in the type of action you want to perform, select **Actions**.
  3. In the **Action** list, select **Execute custom query** , and then click **Done**. 

![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)

  4. Expand the **Task input** section, and then do the following: 
     1. In the **Timeout after** field, enter the number of seconds to wait till the query executes. 

Default value: `180` seconds.

     2. In the **Maximum number of rows** field, enter the maximum number of rows to be returned from the database.

Default value: `25`.

     3. To update the custom query, click **Edit Custom Script**. The **Script editor** dialog opens. 

![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)

     4. In the **Script editor** dialog, enter the SQL query and click **Save**. 

You can use a question mark (?) in a SQL statement to represent a single parameter that must be specified in the query parameters list. For example, the following SQL query selects all rows from the `Employees` table that matches the values specified for the `LastName` column: 
            
            SELECT * FROM Employees where LastName=?

**Note:** Data manipulation language (DML) and data definition language (DDL) statements are supported.
     5. If you've used question marks in your SQL query, you must add the parameter by clicking **\+ Add Parameter Name** for each question mark. While executing the integration, these parameters replace the question marks (?) in the SQL query sequentially. For example, if you have added three question marks (?), then you must add three parameters in order of sequence. 

![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)

To add query parameters, do the following:

        1. From the **Type** list, select the data type of the parameter.
        2. In the **Value** field, enter the value of the parameter.
        3. To add multiple parameters, click **\+ Add Query Parameter**.

The **Execute custom query** action does not support array variables.




On successful execution, this action returns the status 200 (OK) with a response body that has the query results.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Create an index

This example creates an index.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateIndex` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Index": "new_index_1"
         }

If the action is successful, the `CreateIndex` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "CompletedBeforeTimeout": "true",
    "ShardsAcknowledged": "true",
    "IndexName": "new_index_1"
    }]




### Example - Modify an index alias

This example shows how to modify an index alias.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ModifyIndexAliases` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Action": "remove_index",
         "Index": "postmanindex"
         }

If the action is successful, the `ModifyIndexAliases` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the records

This example lists all the records in the `Demoindex` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Demoindex` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



### Example - Get a record from an entity

This example gets a record with the specified ID from the `Demoindex` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Demoindex` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `23` in the **Default Value** field. 

Here, `23` is a unique record ID in the `Demoindex` entity.




### Example - Create a record in an entity

This example creates a record in the `Demoindex` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Demoindex` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "message": "GET /search HTTP/1.1 200 1070000",
         "@timestamp": "2099-11-15 13:12:00.0"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
         "_id": "23"
         }]




### Example - Update a record

This example updates the record with the specified ID in the `Demoindex` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Demoindex` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "message": "GET /search HTTP/1.1 200 1070000",
         "@timestamp": "2099-11-15 13:12:00.0",
         "name": "GoogleCloud_Update_docs",
         "price": 10.0}

  5. Click **entityId** , and then enter `23` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
         "_id": "23"
         }]




### Example - Delete a record from an entity

This example deletes the record with the specified ID in the `Demoindex` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Demoindex` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `pcqT4wB4uQNUCuamh4N` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
client_side_evaluation | BOOLEAN | False | Set ClientSideEvaluation to true to perform Evaluation client side on nested objects.   
data_model | ENUM | False | Specifies the data model to use when parsing Elasticsearch documents and generating the database metadata. Supported values are: Document, FlattenedDocuments, Relational  
max_results | STRING | False | The maximum number of total results to return from Elasticsearch when using the default Search API.   
verbosity | STRING | False | Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates).   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the Elasticsearch connection in an integration

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
