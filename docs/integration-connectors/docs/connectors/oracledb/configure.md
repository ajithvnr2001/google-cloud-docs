---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/configure/
title: Oracle DB (version 2) \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:29:22.930646+00:00
---

# Oracle DB (version 2)  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Oracle DB (version 2)

The Oracle DB connector lets you connect to an Oracle database instance and perform the supported database operations.

## Supported versions

The minimum supported version for this connector is Oracle database version 11.2.

## Before you begin

Before using the Oracle DB connector, do the following tasks:

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

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Oracle DB** from the drop down list of available Connectors.
     2. **Connector version** : Select version 2 from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. Optionally, select **Enable Cloud Logging** to enable cloud logging.
     7. **Service Account** : Select a service account that has the required roles.
     8. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     9. Based on whether your Oracle DB connection uses server-based connection or TNS connectivity, specify either **ServiceName** or **DataSource** (TNS connect string). If you specify both, DataSource is used. 
        * **ServiceName** : If you use server-based authentication, specify the service name along with the destination details.
        * **DataSource** : If you use TNS connectivity, specify the Oracle Net Services Name, Connect Descriptor (also known as TNS connect string), or an easy connect naming that identifies the database to which to connect. Use the following format to specify the TNS connect string: `**(DESCRIPTION=(ADDRESS=(protocol_address_information))(CONNECT_DATA= (SERVICE_NAME=service_name)))**`. If you specify the data source, you must't specify the destination details again in the **Destinations** section. 
     10. Optionally, select **Include Synonyms**.
     11. **Abandoned Connection Timeout** : Enter the timeout value (in seconds) that specifies how long a borrowed connection can remain unused before it's considered as abandoned.
     12. **Inactive Connection Timeout** : Enter the connection timeout value (in seconds).
     13. **Max Connection Reuse Time** : Enter the connection reuse time (in seconds).
     14. **TTL Connection Timeout** : Enter the maximum time (in seconds) the connection may remain in-use.
     15. **Browsable Schemas** : Enter the comma-separated schema names to be used when fetching entities and actions. For example, `schemaA, schemaB, schemaC`.
     16. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     17. Click **NEXT**.
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

The following authentication types are supported by the Oracle DB connection:

     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

## Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Username of the Oracle account used for authentication
    * **Password** : Secret Manager Secret containing the password associated with the Oracle account username.



### Oracle DB basic authentication connection type

The following table describes the fields that you can configure for the Oracle DB basic authentication connection type.

Field Name | Details  
---|---  
Location | us-central1  
Connector | Oracle DB  
Connector version | 2  
Connection Name | google-oracledb-plsql-new  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Service Name | pdb1  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Host address | 198.51.100.0  
Port | 1521  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
  
### Oracle DB TNS connection type

The following table describes the fields that you can configure for the Oracle DB TNS connection type.

Field Name | Details  
---|---  
Location | us-central1  
Connector | Oracle DB  
Connector version | 2  
Connection Name | google-oracledb-plsql-tns  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Data Source | (DESCRIPTION=(ADDRESS=(PROTOCOL_ADDRESS_INFORMATION))(CONNECT_DATA= (SERVICE_NAME=service_name)))  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Username | USERNAME  
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

The Oracle DB connector can process a maximum of 70 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Supported data types

The following are the supported data types for this connector:

  * BIGINT
  * BINARY
  * BIT
  * BOOLEAN
  * CHAR
  * DATE
  * DECIMAL
  * DOUBLE
  * FLOAT
  * INTEGER
  * LONGN VARCHAR
  * LONG VARCHAR
  * NCHAR
  * NUMERIC
  * NVARCHAR
  * REAL
  * SMALL INT
  * TIME
  * TIMESTAMP
  * TINY INT
  * VARBINARY
  * VARCHAR



## Actions

The Oracle DB connector lets you execute your stored procedures, functions, and custom SQL queries in the format supported by your Oracle database. To execute custom SQL queries, the connector provides the **Execute custom query** action.

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




To understand how to use the custom query action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Execute a group by query

  1. In the **Configure connector task** dialog, select **Actions**.
  2. Select the **Execute custom query** action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click **Edit Custom Query**. The **Custom query** dialog opens.
  4. In the **Custom query** dialog, enter the following SQL query and click **Save** : 
         
         Select E.EMPLOYEE_ID, E.EMPLOYEE_NAME, E.CITY
               FROM EMPLOYEES E
               LEFT JOIN EMPLOYEE_DEPARTMENT ED ON E.EMPLOYEE_ID=ED.ID 
               WHERE E.EMPLOYEE_NAME = 'John'
               GROUP BY E.CITY,E.EMPLOYEE_ID,E.EMPLOYEE_NAME
             

This example selects the employee records from the `EMPLOYEES` and the `EMPLOYEE_DEPARTMENT` tables. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have the query result set.




### Example - Execute a parameterized query

  1. In the **Configure connector task** dialog, select **Actions**.
  2. Select the **Execute custom query** action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, set the following values for the field: 
     1. **Timeout after:** `10`
     2. **Maximum number of rows:** `3`
  4. Click **+Add Parameter name** to enter the following values: 
     1. **Type:** `VARCHAR`
     2. **Value:** `John`
  5. Click **Edit Custom Query**. The **Custom query** dialog opens.
  6. In the **Custom query** dialog, enter the following SQL query and click **Save** : 
         
         Select C.ID,C.NAME,C.CITY,C.O_DATE,E.EMPLOYEE_ID 
           FROM customqueries C,Employees E 
           WHERE C.ID=E.Employee_id and C.NAME=?

This example selects employee records where the name of the employee is `John`. Notice that the name of the employee is parameterized. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "NAME": "John",
    "O_DATE": "2023-06-01 00:00:00.0",
    "EMPLOYEE_ID": 1.0
    }, {
    "NAME": "John",
    "O_DATE": "2021-07-01 00:00:00.0",
    "EMPLOYEE_ID": 3.0
    }, {
    "NAME": "John",
    "O_DATE": "2022-09-01 00:00:00.0",
    "EMPLOYEE_ID": 4.0
    }]




### Example - Insert a record by using a sequence value

  1. In the **Configure connector task** dialog, select **Actions**.
  2. Select the **Execute custom query** action, and then click **Done**.
  3. In the **Custom query** dialog, enter the following SQL query and click **Save** : 
         
         INSERT INTO AUTHOR(id,title) VALUES(author_table_id_seq.NEXTVAL,'Sample_book_title')

This example inserts a record in the `AUTHOR` table, by using an existing `author_table_id_seq` sequence object. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]




### Example - Execute a query with an aggregate function

  1. In the **Configure connector task** dialog, select **Actions**.
  2. Select the **Execute custom query** action, and then click **Done**.
  3. In the **Custom query** dialog, enter the following SQL query and click **Save** : 
         
         SELECT SUM(SALARY) as Total FROM EMPLOYEES
           

This example calculates the aggregate value of salaries in the `EMPLOYEES` table. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "TOTAL": 13000.0
    }]  
      




### Example - Create a new table

  1. In the **Configure connector task** dialog, select **Actions**.
  2. Select the **Execute custom query** action, and then click **Done**.
  3. In the **Custom query** dialog, enter the following SQL query and click **Save** : 
         
         CREATE TABLE TEST1 (ID INT, NAME VARCHAR(40),DEPT VARCHAR(20),CITY VARCHAR(10))
          

This example creates the `TEST1` table. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]




## Entity operation examples

### Example - List all the employees

This example lists all the employees in the `Employee` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).



### Example - Get employee details

This example gets the details of the employee whose ID is 45, from the `Employee` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `45` in the **Default Value** field. 

Here, `45` is the primary key value of the `Employee` entity.




### Example - Create a employee record

This example adds a new employee record in the `Employee` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "EMPLOYEE_ID": 69.0,
         "EMPLOYEE_NAME": "John",
         "CITY": "Bangalore"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "ROWID": "AAAoU0AABAAAc3hAAF"
         }




### Example - Update an employee record

This example updates the employee record whose ID is 69 in the `Employee` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "EMPLOYEE_NAME": "John",
         "CITY": "Mumbai"
         }

  5. Click **entityId** , and then enter `69` in the **Default Value** field. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to `69`.

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         }




### Example - Delete an employee record

This example deletes the employee record whose ID is 35 in the `Employee` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `35` in the **Default Value** field. 



## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
service_name | STRING | False | The service name of the Oracle database.   
data_source | STRING | False | Oracle Net Services Name, Connect Descriptor (also known as TNS Connect String), or an easy connect naming that identifies the database to which to connect.   
include_synonyms | BOOLEAN | False | Query metadata for synonyms and make them available as entities. Setting the property to false can increase metadata performance.   
abandoned_connection_timeout | INTEGER | False | Abandoned connection timeout (in seconds) determines how long a borrowed connection can remain unused before it is considered as abandoned and reclaimed by the connection pool.   
inactive_connection_timeout | INTEGER | False | Inactive connection timeout (in seconds) determines how long an available connection remains in the connection pool before it is removed from the pool.   
max_connection_reuse_time | INTEGER | False | Maximum connection reuse time (in seconds) specifies the maximum time any connection can potentially be reused after which the pool removes and closes a connection.   
ttl_connection_timeout | INTEGER | False | Maximum time (in seconds) a connection may remain in-use.   
browsable_schemas | STRING | False | Comma-separated schemas (Eg. SchemaA, SchemaB) to be used when fetching entities and actions for the connection. Uses user's schema by default   
  
## Use the Oracle DB connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Known limitations

**Note:** Oracle RAC setup with SCAN IPs is currently not supported by Integration Connectors. 

The Application Integration Connector for Oracle does not support Oracle Single Client Access Name (SCAN) because its underlying infrastructure cannot process the IP redirection mechanism, resulting in intermittent connectivity failures and `java.lang.IllegalStateException` timeouts.

## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
