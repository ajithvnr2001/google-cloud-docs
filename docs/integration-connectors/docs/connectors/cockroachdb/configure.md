---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/cockroachdb/configure/
title: CockroachDB \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:41.590087+00:00
---

# CockroachDB  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/cockroachdb/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CockroachDB

The CockroachDB connector lets you perform insert, delete, update, and read operations on a [CockroachDB database](https://www.cockroachlabs.com/docs/cockroachcloud/quickstart.html).

## Before you begin

Before using the CockroachDB connector, do the following tasks:

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




For more information about how to create a serverless cluster and utilise all the parameters of the created application, see [Creating a CockroachDB Serverless cluster on Cockroachlabs](https://www.cockroachlabs.com/docs/cockroachcloud/quickstart)

For information about how to create a self signed certificate , see [Cockroach cert](https://www.cockroachlabs.com/docs/stable/cockroach-cert)

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
     1. **Connector** : Select **CockroachDB** from the drop down list of available Connectors.
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
     8. **Database** : The name of the Cockroach database. 
     9. **Allow Prepared Statement** : Allow the preparation of a query statement before its execution. 
     10. **Fetch Result Set Metadata** : This field sets whether the provider is getting detailed information about resultset columns from the server. 
     11. **UseSSL** : This field sets whether SSL is enabled. 
     12. **SSLServerCert** : This field sets whether SSL is enabled. 
     13. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     14. Click **NEXT**.
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

The following authentication types are supported by the CockroachDB connection:

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

This section lists the sample values for the various fields that you configure when creating the CockroachDB connection.

### CockroachDB - Basic authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | CockroachDB  
Connector version | 1  
Connection Name | cockroach-db-cloud-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
SSL | Yes  
SSLServerCert  | cockroach-db-ssl-cert  
SecretVersion | 1  
Database | TestGCP  
Allow Prepared Statement | Yes  
Fetch Result Set Metadata | Yes  
Verbosity level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type(Server) | Host address  
Host address | googlecloud-bcone-cluster-13792.5xj.cockroachlabs.cloud. This is the name of the CockroachDB cloud cluster.  
Port | 26257  
Username | User name  
Password | password  
Secret version | 1  
  
### CockroachDB - PSC connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | CockroachDB  
Connector version | 1  
Connection Name | cockroach-db-cloud-conn-psc  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
SSL | Yes  
SSLServerCert  | gcp-bcone-crdb-hosted-node-crt  
SecretVersion | 1  
Database | bank  
Allow Prepared Statement | No  
Fetch Result Set Metadata | No  
Verbosity level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type(Server) | Host address  
Host address | 192.0.2.0/24 (this should be the endpoint attachment created based on the server ip hosting the cockroach db instance)  
Port | 26257  
Username | User name  
Password | password  
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

The CockroachDB connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

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

**Note:** The functions defined in the CockroachDB are listed as actions in the connector task. Therefore, you can execute a function by executing the corresponding action. For example on how to execute a function, see .

## Action examples

### Example - Find the greater value

This example shows how to execute a user-defined function. The `find_greater` function in this example, compares two integers and returns the integer which is greater.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `find_greater` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "$1": 1.0,
         "$2": 5.0
         }

If the action execution is successful, the connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    [{
    "bignum": 5.0
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all Employees records

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employees` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement.

The value for filter clause should be always passed within the single quotes (') in this format.   
It can be used to filter the records based on any column.




You can perform the List operation on the following entities:

Cockroach_Datatypes, Accounts, SpatialData, UNICODE, LANGUAGES, and View_Cockroach

### Example - Get a Employees record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employees` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to 5 which is the Key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `5` in the **Input Value** field and choose the EntityId as Local variable. 

Value for Entity Id should be passed directly. Here 5 is the unique primary key value, which should be passed.

There are certain cases, where passing single Entity Id would throw an error as there will be two composite keys.  
In such cases, you can make use of Filter Clause and pass the value such as, EmployeeId='5'.




You can perform the List operation on the following entities:

Cockroach_Datatypes, Accounts, SpatialData, UNICODE, and LANGUAGES

### Example - Delete an Employees record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employees` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to 2 which is the Key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `2` in the **Input Value** field and choose the EntityId as Local variable. 

If Entity has two Composite Business or Primary Keys instead of specifying the **entityId** , you can also set the **filterClause** to `EmployeeId='2'`.




You can perform the Delete operation on the following entities:

Cockroach_Datatypes, Accounts, SpatialData, UNICODE, and LANGUAGES

### Example - Create an Employees record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employees` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "id": 100.0,
           "gender": "Male",
           "firstname": "Charlie",
           "lastname": "Cruz",
           "designation": "Tester",
           "dept": "IT"
         }
         

If the integration is successful, the `Employees` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "id": 100.0,
           "gender": "Male",
           "firstname": "Charlie",
           "lastname": "Cruz",
           "designation": "Tester",
           "dept": "IT"
           }
           




### Example - Create a Cockroach_Datatypes record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Cockroach_Datatypes from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "col_int": 8.0,
           "col_date": "2016-03-26",
           "col_inet": "190.0.0.0",
           "col_collate": "Cruz",
           "col_string": "Charlie",
           "col_timestamp": "1992-10-05 12:12:12",
           "col_float": 12.12,
           "col_decimal": 10.1,
           "col_json": "{\"type\": \"account creation\", \"username\": \"harvestboy93\"}",
           "col_bool": true,
           "col_interval": "1 year 2 mons 3 days 04:05:06",
           "col_array": "{sky,road,car}",
           "col_uuid": "63616665-6630-3064-6465-616462656562",
           "col_time": "05:41:39",
           "col_bytes": "abc",
           "col_bit": "1",
           "col_name": "Charlie",
           "col_character": "A",
           "col_tsvector": "ts",
           "col_tsquery": "normal",
           "col_oid": "11",
           "col_bytea": "01100001"
         }
         

If the integration is successful, the `Cockroach_Datatypes` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "col_int": 8.0,
           "col_date": "2016-03-26",
           "col_inet": "190.0.0.0",
           "col_collate": "Cruz",
           "col_string": "Charlie",
           "col_timestamp": "1992-10-05 12:12:12",
           "col_float": 12.12,
           "col_decimal": 10.1,
           "col_json": "{\"type\": \"account creation\", \"username\": \"harvestboy93\"}",
           "col_bool": true,
           "col_interval": "1 year 2 mons 3 days 04:05:06",
           "col_array": "{sky,road,car}",
           "col_uuid": "63616665-6630-3064-6465-616462656562",
           "col_time": "05:41:39",
           "col_bytes": "abc",
           "col_bit": "1",
           "col_name": "Charlie",
           "col_character": "A",
           "col_tsvector": "ts",
           "col_tsquery": "normal",
           "col_oid": "11",
           "col_bytea": "01100001"
           }
           




### Example - Create an Entity LANGUAGES record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `LANGUAGES` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "id": 5.0,
           "hinditext": "नमस्ते",
           "englishtest": "Namaste",
           "arabictext": "مرحبا",
           "germantext": "Günther"
         } 
         

If the integration is successful, the `LANGUAGES` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "id": 6.0,
         "hinditext": "नमस्ते",
         "englishtest": "Namaste",
         "arabictext": "مرحبا",
         "germantext": "Günther"
         }
         




### Example - Create a UNICODE record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select UNICODE from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "id": 2.0,
           "unicodedata": "Unicode データ型はグローバル化されたデータの保存に使用されます",
           "test": "UnicodeTest"
         }
         

If the integration is successful, the `UNICODE` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "id": 2.0,
    "unicodedata": "Unicode データ型はグローバル化されたデータの保存に使用されます",
    "test": "UnicodeTest"
    }
    




### Example - Create a SpatialData record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select SpatialData from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "id": 10.0,
           "data": "01020000000500000070CE88D2DE3453C075029A081B164540984C158C4AEA52C0DC68006F81B4444009F9A067B36252C02DB29DEFA7864440FA7E6ABC747B52C0D122DBF97EDA444070CE88D2DE3453C075029A081B164548"
         }
         

This example will create the SpatialData Records. If the integration is successful, the `SpatialData` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "id": 10.0,
         "data": "01020000000500000070CE88D2DE3453C075029A081B164540984C158C4AEA52C0DC68006F81B4444009F9A067B36252C02DB29DEFA7864440FA7E6ABC747B52C0D122DBF97EDA444070CE88D2DE3453C075029A081B164548"
         }
         




### Example - Create an Accounts record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Accounts` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "balance": 2000.0,
           "status": "open",
           "id": 7.0
         }
         

This example will create the SpatialData Records. If the integration is successful, the `SpatialData` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "balance": 2000.0,
         "status": "open",
         "id": 7.0
         }
         




### Example - Update a Employees record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Employees from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
           "dept": "Comp",
           "designation": "QA"
         }
         

  5. Set the entity ID in Data Mapper to the entity of the Employees . To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to ` 1`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
         }
         




### Example - Update a LANGUAGES record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `LANGUAGES` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
           "englishtest": "UpdateTest_TEST"
         }
         

  5. Set the entity ID in Data Mapper to the entity of the Arrays. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `1`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
         }
         




### Example - Update a UNICODE record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `UNICODE` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
           "unicodedata": "ータ型はグロ",
           "test": "UpdateTest"
         }
         

  5. Set the entity ID in Data Mapper to the entity of the ObjectType . To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `3`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
         }
         




### Example - Update a SpatialData record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Spatialdata` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
         "data": "01020000000500000070CE88D2DE3453C075029A081B164540984C158C4AEA52C0DC68006F81B4444009F9A067B36252C02DB29DEFA7864440FA7E6ABC747B52C0D122DBF97EDA444070CE88D2DE3453C075029A081B164543"
         } 
         

  5. Set the entity ID in Data Mapper to the entity of the TableType . To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id= 1`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
         "id": 1,
         "data": "01020000000500000070CE88D2DE3453C075029A081B164540984C158C4AEA52C0DC68006F81B4444009F9A067B36252C02DB29DEFA7864440FA7E6ABC747B52C0D122DBF97EDA444070CE88D2DE3453C075029A081B164543"
         }
         




### Example - Update a Accounts record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Accounts` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
         "balance": 1500.0,
         "status": "open"
         }
         

  5. Set the entity ID in Data Mapper to the entity of the TableType . To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id= 1`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
         "id": 1,
         "balance": 1500,
         "status": "open"
         }
         




### Example - Update a Cockroach_Datatypes record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Cockroach_Datatypes` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
         "col_date": "2019-03-26",
         "col_collate": "Charlie",
         "col_string": "Cruz"
         }
         

  5. Set the entity ID in Data Mapper to the entity of the TableType . To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `2`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
         }
         




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
use_ssl | BOOLEAN | False | This field sets whether SSL is enabled.   
ssl_server_cert | SECRET | False | This field sets whether SSL is enabled.   
database | STRING | True | The name of the Cockroach database.   
allow_prepared_statement | BOOLEAN | False | Allow the preparation of a query statement before its execution.   
fetch_result_set_metadata | BOOLEAN | False | This field sets whether the provider is getting detailed information about resultset columns from the server.   
  
## Use the CockroachDB connection in an integration

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
