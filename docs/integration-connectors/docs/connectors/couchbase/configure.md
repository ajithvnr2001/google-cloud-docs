---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/couchbase/configure/
title: Couchbase \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:17.158067+00:00
---

# Couchbase  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/couchbase/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Couchbase

The Couchbase connector lets you connect to a Couchbase database instance and perform the supported database operations.

## Supported versions

  * Couchbase Server versions 4.0 and up (Enterprise Edition or Community Edition).

  * Couchbase Capella




## Before you begin

Before using the Couchbase connector, do the following tasks:

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

  * If required, create a Couchbase server. For more information, see [Quickstart Couchbase Server](https://docs.couchbase.com/home/server.html).
For information about Couchbase APIs, see [Couchbase REST API Doc](https://docs.couchbase.com/server/current/rest-api/rest-intro.html). 
  * If required, download the SSL certificate. For more information, see [Secure Connection with TLS](https://docs.couchbase.com/kotlin-sdk/current/howtos/secure-connections.html). 



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
     1. **Connector** : Select **Couchbase** from the drop down list of available Connectors.
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
     8. **Allow JSON Parameters** : Allows raw JSON to be used in parameters when QueryPassthrough is enabled. 
     9. **Analytics Port** : The port for connecting to the Couchbase Analytics Endpoint. 
     10. **Child Separator** : The character or characters used to denote child tables. 
     11. **Couchbase Service** : Determines the Couchbase service to connect to. Default is N1QL. Available options are N1QL and Analytics. 
     12. **Create Table Ram Quota** : The default RAM quota, in megabytes, to use when inserting buckets via the CREATE TABLE syntax. 
     13. **Dataverse Separator** : The character or characters used to denote Analytics dataverses and scopes/collections. 
     14. **Flavor Separator** : The character or characters used to denote flavors. 
     15. **N1QL Port** : The port for connecting to the Couchbase N1QL Endpoint. 
     16. **Periods Separator** : The character or characters used to denote hierarchy. 
     17. **Query Execution Timeout** : This sets the server-side timeout for the query, which governs how long Couchbase will execute the query before returning a timeout error. 
     18. **Strict Comparison** : Adjusts how precisely to translate filters on SQL input queries into Couchbase queries. This can be set to a comma-separated list of values, where each value can be one of: date, number, boolean, or string. 
     19. **Transaction Durability** : Specifies how a document must be stored for a transaction to succeed. Specifies whether to use N1QL transactions when executing queries. 
     20. **Transaction Timeout** : This sets the amount of time a transaction may execute before it is timed out by Couchbase. 
     21. **Use Collections For DDL** : Whether to assume that CREATE TABLE statements use collections instead of flavors. Only takes effect when connecting to Couchbase v7+ and GenerateSchemaFiles is set to OnCreate. 
     22. **Use Transactions** : Specifies whether to use N1QL transactions when executing queries. 
     23. **Validate JSON Parameters** : Allows the provider to validate that string parameters are valid JSON before sending the query to Couchbase. 
     24. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     25. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     26. Click **NEXT**.
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

The following authentication types are supported by the Couchbase connection:

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
    * **UseSSL** : This field sets whether SSL is enabled.
    * **SSLServerCert** : SSLServerCert for Couchbase Connector
    * **Auth scheme** : Auth scheme for Couchbase Connector
    * **Connection Mode** : Determines how to connect to the Couchbase server. Must be either `Direct` or `Cloud`. For `Cloud`, SSL is mandatory. For more information, see [Secure connections with TLS](https://docs.couchbase.com/kotlin-sdk/current/howtos/secure-connections.html).
    * **DNS Server** : Determines what DNS server to use when retrieving Couchbase Cloud information. For example, `8.8.8.8`.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Couchbase Connector.

### SSL - Certificate connection type

Field Name | Details  
---|---  
Region | us-central1  
Connector | Couchbase  
Connector Version | 1  
Connector Name | Couchbase-basic-auth-conn  
Service Account | NAME-compute@developer.gserviceaccount.com  
Verbosity Level | 5  
Connection node settings: Min/Max number of nodes | 2/50  
SSL Configuration Enable SSL | True  
Trust Store | Private  
Custom Trust Store |  A full PEM Certificate (-----BEGIN CERTIFICATE----- MIIChTCCAe4CAQAwDQYJKoZIhv......Qw== -----END CERTIFICATE-----)  
Secret version | 1  
Host Address | xx.1HOST_NAME.cloud.couchbase.com:18xxx  
Authentication |  User Password  
Username | username  
Password | password | versions | 1  
vConnection Mode | Cloud  
DNS Server | 192.0.2.0  
OAuth scheme | Basic  
  
### Analytics Couchbase connection type

Field Name | Details  
---|---  
Region | us-central1  
Connector | Couchbase  
Connector Version | 1  
Connector Name | Couchbase-basic-auth-Analytics-conn  
Service Account | NAME-compute@developer.gserviceaccount.com  
Analytics Port | 18095  
Couchbase Service | Analytics  
Verbosity Level | 5  
Connection node settings: Min/Max number of nodes | 2/50  
Host Address | xx.1HOST_NAME.cloud.couchbase.com:18095  
Authentication | User Password  
Username | username  
Password | password  
versions | 1  
vConnection Mode | Cloud  
DNS Server | 192.0.2.0  
OAuth scheme |  Basic  
  
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

This connector supports execution of the following actions: 

  * **User-defined stored procedures and functions.** If you have any stored procedures and functions in your backend, those are listed in the `Actions` column of the `Configure connector task` dialog.
  * **Custom SQL queries.** To execute custom SQL queries, the connector provides the **Execute custom query** action. 

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




## System limitations

The Couchbase connector can process 25 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### AddDocument action

This action add documets in couchbase.

#### Input parameters of the AddDocument action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
BucketName | String | Yes | The bucket to insert the document into.  
SourceTable | Object | No | The name of the temp table containing ID and Document columns. Required if no ID is specified.  
ID | String | No | The primary key to insert the document under. Required if no SourceTable is specified.  
Document | String | No | The JSON text of the document to insert. Required if not SourceTable is specified.  
  
#### Output parameters of the AddDocument action

This action returns the status 200 (OK) if the action is successful.

For example on how to configure the `AddDocument` action, see Action examples.

### CreateCollection action

This action creates a collection in an existing scope.

#### Input parameters of the CreateCollection action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Bucket | String | Yes | The name of the bucket containing the collection.  
Scope | String | Yes | The name of the scope containing the collection.  
Name | String | Yes | The name of the collection to create.  
  
#### Output parameters of the CreateCollection action

This action returns the status 200 (OK) if the action is successful.

For example on how to configure the `CreateCollection` action, see Action examples.

### DeleteCollection action

This action deletes a collection in an existing scope.

#### Input parameters of the DeleteCollection action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Bucket | string | True | The name of the bucket containing the collection.  
Scope | String | True | The name of the scope containing the collection.  
Name | string | True | The name of the collection to delete.  
  
#### Output parameters of the DeleteCollection action

This action returns the status 200 (OK) if the action is successful.

For example on how to configure the `DeleteCollection` action, see Action examples.

### CreateScope action

This action creates a scope in an existing bucket.

#### Input parameters of the CreateScope action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Bucket | String | Yes | The name of the bucket containing the scope  
Name | String | Yes | The name of the scope to create.  
  
#### Output parameters of the CreateScope action

This action returns the status 200 (OK) if the action is successful.

For example on how to configure the `CreateScope` action, see Action examples.

### DeleteScope action

This action deletes a scope and all its collections.

#### Input parameters of the DeleteScope action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Bucket | String | Yes | The name of the bucket containing the scope.  
Name | String | Yes | The name of the scope to delete.  
  
#### Output parameters of the DeleteScope action

This action returns the status 200 (OK) if the action is successful.

For example on how to configure the `DeleteScope` action, see Action examples.

### ListIndices action

This action lists all indices available in Couchbase.

#### Input parameters of the ListIndices action

N/A 

#### Output parameters of the ListIndices action

This action returns the status 200 (OK) if the action is successful.

For example on how to configure the `ListIndices` action, see Action examples.

### ManageIndices action

This action creates or drops an index in a bucket.

#### Input parameters of the ManageIndices action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
BucketName | String | Yes | The target bucket to create or drop the index from.  
ScopeName | object | No | The target scope to create or drop the index from (Couchbase version 7 and later)  
CollectionName | String | No | The target collection to create or drop the index from (Couchbase version 7 and later)  
Action | String | Yes | Specifies which action to perform on the index, can be Create or Drop.  
Expressions | String | No | A list of expressions or functions, encoded as JSON, that the index will be based off of. At least one is required if IsPrimary is set to false and the action is Create.  
Name | String | No | The name of the index to create or drop, required if IsPrimary is set to false.  
IsPrimary | String | No | Specifies if the index should be a primary index.The default value is true.  
Filters | String | No | A list of filters, encoded as JSON, to apply on the index.  
IndexType | String | No | The type of index to create, can be GSI or View, only used if the action is Create. The default value is GSI.  
ViewName | String | No | Deprecated, included for compatibility only. Does nothing.  
Nodes | String | No | A list, encoded as JSON, of nodes to contain the index, must contain the port. Only used if the action is Create.  
NumReplica | String | No | How many replicas to create among the index nodes in the cluster.  
  
#### Output parameters of the ManageIndices action

This action returns the status 200 (OK) if the action is successful.

For example on how to configure the `ManageIndices` action, see Action examples.

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

### Example - Add a document

This example adds a document in a Couchbase bucket.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Document": "{\"ID\":10,\"Name\":\"TestDoc\"}",
         "BucketName": "CouchbaseTestBucket",
         "ID": "Test"
         }

If the action is successful, the `AddDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "RowsAffected": "1"
    }]




### Example - Create a collection

This example creates a collection.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateCollection` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "bucket": "CouchbaseTestBucket",
         "scope": "TestScope",
         "name": "CollectionFromGoogleCloud"
         }

This example creates a collection under the `TestScope`. If the action is successful, the `CreateCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true,
    "scope": null,
    "uid": null,
    "collection": null,
    "collections.uid": null,
    "maxTTL": null,
    "history": null
    }]




### Example - Delete a collection

This example deletes a collection.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteCollection` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "bucket": "CouchbaseTestBucket",
         "scope": "TestScope",
         "name": "CollectionFromGoogleCloud"
         }

This example deletes a collection under the `TestScope`. If the action is successful, the `CreateCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true,
    "uid": "12"
    }]




### Example - Create a scope

This example creates a scope.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateScope` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "bucket": "CouchbaseTestBucket",
         "name": "ScopeFromGoogleCloud"
         }

This example creates a scope under `CouchbaseTestBucket`. If the action is successful, the `CreateScope` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true,
    "name": null,
    "uid": null,
    "collections": null,
    "collections.name": null,
    "collections.uid": null,
    "collections.maxTTL": null,
    "collections.history": null
    }]




### Example - Delete a scope

This example deletes a scope.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteScope` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "bucket": "CouchbaseTestBucket",
         "name": "ScopeFromGoogleCloud"
         }

This example deletes the `ScopeFromGoogleCloud` scope. If the action is successful, the `DeleteScope` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true,
    "uid": "10"
    }]




### Example - List indices

This example lists all indices available in Couchbase.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ListIndices` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         }

If the action is successful, the `ListIndices` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "id": "3d8a78cd2e302ac2",
    "datastore_id": "http://127.0.0.1:8091",
    "namespace_id": "default",
    "bucket_id": null,
    "scope_id": null,
    "keyspace_id": "CouchbaseTestBucket",
    "index_key": "",
    "condition": null,
    "is_primary": "false",
    "name": "test",
    "state": "online",
    "using": "gsi"
    }, {
    "id": "d6ce8c103b97a00d",
    "datastore_id": "http://127.0.0.1:8091",
    "namespace_id": "default",
    "bucket_id": "CouchbaseTestBucket",
    "scope_id": "TestScope",
    "keyspace_id": "CouchBaseDatatypes",
    "index_key": "",
    "condition": null,
    "is_primary": "true",
    "name": "#primary",
    "state": "online",
    "using": "gsi"
    },
    {
    "id": "58c25aef49dd32b3",
    "datastore_id": "http://127.0.0.1:8091",
    "namespace_id": "default",
    "bucket_id": "CouchbaseTestBucket",
    "scope_id": "TestScope",
    "keyspace_id": "TestCollection",
    "index_key": "",
    "condition": null,
    "is_primary": "false",
    "name": "SearchIndexTest_1",
    "state": "online",
    "using": "fts"
    }]




### Example - Manage indices

This example deletes an index in the specified bucket.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ManageIndices` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "BucketName": "CouchbaseTestBucket",
         "Action": "DROP",
         "Name": "CouchBaseTestIndex"
         }

If the action is successful, the `ManageIndices` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the records

This example lists all the records in the `TestCollection` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestCollection` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 

**Note:** To filter apply filter on a nested field, enclose the field name within double quotes ("). For example, to filter on a nested field `geo.accuracy`, use the filter clause `"geo.accuracy" IN ("RANGE_INTERPOLATED", "ROOFTOP")`.

### Example - Get a record from an entity

This example gets a record with the specified ID from the `TestCollection` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestCollection` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `120` in the **Default Value** field. 

Here, `120` is a unique record ID in the `TestCollection` entity.




### Example - Update a record in an entity

This example updates a record in the `TestCollection` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestCollection` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "COL_TEXT": "CouchBase Update"
         }

  5. Click **entityId** , and then enter `120` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
         "Document.Id": "120"
         }]




### Example - Delete a record from an entity

This example deletes the record with the specified ID in the `TestCollection` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestCollection` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `20` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

## Known issues

The `create` operation on entities isn't supported.

## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
allow_jsonparameters | BOOLEAN | False | Allows raw JSON to be used in parameters when QueryPassthrough is enabled.   
analytics_port | STRING | False | The port for connecting to the Couchbase Analytics Endpoint.   
child_separator | STRING | False | The character or characters used to denote child tables.   
couchbase_service | ENUM | False | Determines the Couchbase service to connect to. Default is N1QL. Available options are N1QL and Analytics. Supported values are: N1QL, Analytics  
create_table_ram_quota | STRING | False | The default RAM quota, in megabytes, to use when inserting buckets via the CREATE TABLE syntax.   
dataverse_separator | STRING | False | The character or characters used to denote Analytics dataverses and scopes/collections.   
flavor_separator | STRING | False | The character or characters used to denote flavors.   
n1_qlport | STRING | False | The port for connecting to the Couchbase N1QL Endpoint.   
periods_separator | STRING | False | The character or characters used to denote hierarchy.   
query_execution_timeout | STRING | False | This sets the server-side timeout for the query, which governs how long Couchbase will execute the query before returning a timeout error.   
strict_comparison | STRING | False | Adjusts how precisely to translate filters on SQL input queries into Couchbase queries. This can be set to a comma-separated list of values, where each value can be one of: date, number, boolean, or string.   
transaction_durability | STRING | False | Specifies how a document must be stored for a transaction to succeed. Specifies whether to use N1QL transactions when executing queries.   
transaction_timeout | STRING | False | This sets the amount of time a transaction may execute before it is timed out by Couchbase.   
use_collections_for_ddl | BOOLEAN | False | Whether to assume that CREATE TABLE statements use collections instead of flavors. Only takes effect when connecting to Couchbase v7+ and GenerateSchemaFiles is set to OnCreate.   
use_transactions | STRING | False | Specifies whether to use N1QL transactions when executing queries.   
validate_jsonparameters | BOOLEAN | False | Allows the provider to validate that string parameters are valid JSON before sending the query to Couchbase.   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
verbosity | STRING | False | Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates).   
  
## Use the Couchbase connection in an integration

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
