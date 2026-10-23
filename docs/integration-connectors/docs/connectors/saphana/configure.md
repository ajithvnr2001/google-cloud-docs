---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/saphana/configure/
title: SAP HANA \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:23.054437+00:00
---

# SAP HANA  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/saphana/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SAP HANA

The SAP Hana connector lets you perform insert, delete, update, and read operations on SAP Hana database.

## Supported versions

SAP HANA version 2.0 SPS04 and later

## Before you begin

Before using the SAP Hana connector, do the following tasks:

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


For information about creating a SAP HANA database, see [Quickstart with SAP HANA](https://help.sap.com/docs/SLTOOLSET/3aa4caa3bd634a22bdc572d82d1311ec/de681a8057a34bbfbf465b69feb910f9.html?version=CURRENT_VERSION) For more information about SAP HANA, see [SAP HANA platform overview](https://help.sap.com/docs/)

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
     1. **Connector** : Select **SAP Hana** from the drop down list of available Connectors.
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
     8. **Database** : The name of the SAP HANA database. 
     9. **BrowsableSchemas** : This property restricts the schemas reported to a subset of the available schemas. For example, BrowsableSchemas=SchemaA,SchemaB,SchemaC. 
     10. **Include System Objects** : Set IncludeSystemObjects to True to fetch Hana System schema and tables. 
     11. **Include Table Types** : If set to true, the provider will report the types of individual tables and views. 
     12. **Session Variables** : A comma-separated list of session variables to set on the current connection. 
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

The following authentication types are supported by the SAP Hana connection:

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



### Basic authentication connection type

The following table lists the sample configuration values for the basic authentication connection type. Refer to the connection creation interface in the console to know the mandatory and optional fields.

Field name | Details  
---|---  
Location | us-central1  
Connector | SAP HANA  
Connector version | 1  
Connection Name | sap-hana-db-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
Database | S19  
BrowsableSchemas | GOOGLEUSER  
Include Table Type | Yes  
Enable Verbose Logging | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host address  
host 1 | 192.0.2.0/24  
port 1 | 31015  
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

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

### EMPLOYEE_PROCEDURE_HANA action

This action returns data of an Id.

#### Input parameters of the EMPLOYEE_PROCEDURE_HANA action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ID | Integer | True | Type ID which need to passed in procedure  
  
For example on how to configure the `EMPLOYEE_PROCEDURE_HANA` action, see Examples.

### ExecuteCustomQuery action

This action allows you to perform specific tasks. For example, HANADB enables you to execute a custom SQL query.

#### Input parameters of the ExecuteCustomQuery action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
query | String | True | Query string that needs to be executed.  
queryParameters | Array, Null | True | Query parameters to be passed in order.  
maxRows | Number, Null | False | Maximum number of rows to be returned.  
timeout | Number, Null | False | Number of seconds to wait for the query execution.  
  
For example on how to configure the `ExecuteCustomQuery` action, see Examples.

## Action examples

### Example - EMPLOYEE_PROCEDURE_HANA

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `EMPLOYEE_PROCEDURE_HANA` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ID":1
         }
         

If the action is successful, the `EMPLOYEE_PROCEDURE_HANA` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "EMP_ID": 1.0,
    "NAME": "Komal",
    "CITY": "UP",
    "SALARY": 7500.0,
    "DEPARTMENT": "IT" 
    }]
    




### Example - ExecuteCustomQuery Join_GroupBy

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT CUSTOMER.COMPANY, SUM(ORDERS.AMOUNT) AS Total
         FROM ORDERS
         INNER JOIN CUSTOMER
         ON ORDERS.CUSTOMER_ID = CUSTOMER.ID
         GROUP BY CUSTOMER.COMPANY"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "COMPANY": "google India",
    "TOTAL": 1560.0
    },{
    "COMPANY": "IBM India",
    "TOTAL": 4500.0
    }]
    




### Example - ExecuteCustomQuery Join

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT ID, NAME, AGE, AMOUNT FROM CUSTOMERS JOIN ORDERS ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID"
           }]
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "ID": 3.0,
      "NAME": "Kaushik",
      "AGE": 23.0,
      "AMOUNT": 3000.0
    }, {
      "ID": 3.0,
      "NAME": "Kaushik",
      "AGE": 23.0,
      "AMOUNT": 1500.0
    }, {
      "ID": 2.0,
      "NAME": "Khilan",
      "AGE": 25.0,
      "AMOUNT": 1560.0
    }, {
      "ID": 4.0,
      "NAME": "Chaitali",
      "AGE": 25.0,
      "AMOUNT": 2060.0
    }]
    




### Example - ExecuteCustomQuery Groupby_Having_Count

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT COUNT(ID), CITY FROM GCP_HANA_CUSTOM GROUP BY CITY HAVING COUNT(ID) > 1"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "COUNT(ID)": 2.0,
      "CITY": "Delhi"
    }] 
    




### Example - ExecuteCustomQuery GroupBy

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT COUNT(ID), CITY FROM GCP_HANA_CUSTOM GROUP BY CITY"
         }
         

This example will update the ExecuteCustomQuery records. If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "COUNT(ID)": 1.0,
      "CITY": "Kolkata"
    }, {
      "COUNT(ID)": 1.0,
      "CITY": "Katihar"
    }, {
      "COUNT(ID)": 1.0,
      "CITY": "Bangalore"
    }, {
      "COUNT(ID)": 2.0,
      "CITY": "Delhi"
    }]
    




### Example - ExecuteCustomQuery GroupBy_OrderBy

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT COUNT(ID), CITY FROM GCP_HANA_CUSTOM GROUP BY CITY ORDER BY COUNT(ID) DESC"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "COUNT(ID)": 2.0,
      "CITY": "Delhi"
    }, {
      "COUNT(ID)": 1.0,
      "CITY": "Kolkata"
    }, {
      "COUNT(ID)": 1.0,
      "CITY": "Bangalore"
    }, {
      "COUNT(ID)": 1.0,
      "CITY": "Katihar"
    }]
    




### Example - ExecuteCustomQuery Insert_Table

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "INSERT INTO CUSTOMER VALUES (3, 'IBM India')"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]
    




### Example - ExecuteCustomQuery SUM_AggFunc

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT SUM(SALARY) FROM CUSTOMERS"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "SUM(SALARY)": 12000.0
    }] 
    




### Example - ExecuteCustomQuery AVG_AggFunc

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT AVG(SALARY) FROM CUSTOMERS"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "AVG(SALARY)": 3000.0
    }] 
    




### Example - ExecuteCustomQuery MAX_AggFunc

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT MAX(SALARY) FROM CUSTOMERS"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "MAX(SALARY)": 6500.0
    }] 
    




### Example - ExecuteCustomQuery MIN_AggFunc

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT MIN(SALARY) FROM CUSTOMERS"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "MIN_SALARY": 1500.0
    }]
    




### Example - ExecuteCustomQuery COUNT_AggFunc

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT COUNT(*) FROM CUSTOMERS"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "COUNT(*)": 4.0
    }]
    




### Example - ExecuteCustomQuery CreateTable

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "CREATE TABLE CUSTOMER (ID INT NOT NULL,COMPANY VARCHAR (20))"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]
    




### Example - ExecuteCustomQuery AlterTable

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "ALTER TABLE GCP_HANA_CUSTOM ADD CONSTRAINT test PRIMARY KEY (ID)"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]
    




### Example - ExecuteCustomQuery TruncateTable

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "TRUNCATE TABLE GCP_HANA_RENAME"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]
    




### Example - ExecuteCustomQuery DropTable

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "DROP TABLE GCP_HANA_DROP"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]
    




### Example - ExecuteCustomQuery RenameTable

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "RENAME TABLE GCP_HANA_CUSTOM1 TO GCP_HANA_RENAME"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]
    




### Example - ExecuteCustomQuery UpdateTable

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "UPDATE CUSTOMERS SET ADDRESS = 'Pune' WHERE ID = 3"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]
    




### Example - ExecuteCustomQuery SELECT_DATA_Table

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "SELECT * FROM CUSTOMERS"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "ID": 1.0,
      "NAME": "Ramesh",
      "AGE": 32.0,
      "ADDRESS": "Ahmedabad",
      "SALARY": 2000.0
    }, {
      "ID": 2.0,
      "NAME": "Khilan",
      "AGE": 25.0,
      "ADDRESS": "Delhi",
      "SALARY": 1500.0
    }, {
      "ID": 4.0,
      "NAME": "Chaitali",
      "AGE": 25.0,
      "ADDRESS": "Mumbai",
      "SALARY": 6500.0
    }]
    




### Example - ExecuteCustomQuery DeleteTable

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteCustomQuery` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "query": "DELETE FROM CUSTOMERS WHERE ID = 3"
         }
         

If the action is successful, the `ExecuteCustomQuery` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    }]
    




### Example - Insert a JSON array into a DB

To bulk insert data from a JSON array into a SAP HANA database table you can use one of the following methods:

#### Use a custom query with JSON table

Use the **Execute Custom Query** feature combined with a SAP HANA `JSON_TABLE` function. This method uses a single query to parse a JSON array and insert all records simultaneously.

To perform a bulk insert with a custom query, do the following:

  1. Transform your source data into a single JSON string. For example: 
         
         '[ {"id": 701, "name": "Laptop", "email": "EMAIL_ADDRESS"},{"id": 702, "name": "Keyboard", "email": "EMAIL_ADDRESS"}]'

  2. Select the action **Execute Custom Query**.
  3. Use an `INSERT` statement that uses the `JSON_TABLE` function to parse the input string. For example: 
         
         INSERT INTO YOUR_TABLE_NAME (ID, NAME, EMAIL)
         SELECT
             ID,
             NAME,
             EMAIL
         FROM
         JSON_TABLE(?, '$[*]'
             COLUMNS (
                 ID INT PATH '$.id',
                 NAME NVARCHAR(100) PATH '$.name',
                 EMAIL NVARCHAR(100) PATH '$.email'
             )
         ) AS jt;
         

  4. Map the Integration variable containing your JSON string to the single bind parameter `?`.
  5. Execute the query and verify the success of the operation.



#### Use a For Each Loop task

This method uses Application Integration to loop through the JSON array. For each JSON object in the array, it calls a sub-integration that performs a single `INSERT` operation. The iteration happens within the integration itself.

  1. Go to the **Integration** and create a **For Each Loop** task.
  2. Locate the **List to iterate** field and assign your input JSON array variable to this field. The loop will now iterate over each object within this array.
  3. Under **Sub-integration details** , provide the **Sub-integration name** and the **API trigger ID** of the sub-integration you want to call for each iteration.
  4. In the **Execution Task** section, provide a **Sub-integration variable name**.
  5. In the **Sub-integration** , use an **Execute Custom Query** or a pre-configured entity configuration to perform the `INSERT` operation using the data from the incoming JSON object.



#### Use a stored procedure

This method uses your database to handle looping and insertion. You must create a stored procedure in SAP HANA that can parse a JSON array and insert the data, and then you can use a connectors task in Application Integration to call the procedure and pass the entire JSON array to it.

To use a stored procedure for bulk insertion, do the following:

  1. Create a stored procedure in your SAP HANA database that can parse a JSON array and insert the data. 
         
         {
                 CREATE PROCEDURE "YOUR_SCHEMA"."SP_INSERT_FROM_JSON" (
                     IN JSON_STRING CLOB
                 )
                 LANGUAGE SQLSCRIPT
                 SQL SECURITY INVOKER
                 DEFAULT SCHEMA "YOUR_SCHEMA"
                 AS
                 BEGIN
         
                     -- Parse JSON string using JSON_TABLE and insert directly into target table
                     INSERT INTO "YOUR_SCHEMA"."YOUR_TABLE" (ID, NAME, GRADE)
                     SELECT ID, NAME, GRADE
                     FROM JSON_TABLE(:JSON_STRING, '$[*]'
                         COLUMNS (
                             ID   INT PATH '$.ID',
                             NAME NVARCHAR(100) PATH '$.NAME',
                             GRADE FLOAT PATH '$.GRADE'
                         )
                     );
         
                 END;
                 }
             

  2. Use the **Connectors** task in Application Integration to call the procedure and pass the entire JSON array to it. In the `Configure connector task` dialog, click `Actions`.
  3. Select the created procedure, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **connectorInputPayload** and then enter a JSON data value similar to the following in the `Default Value` field: 
         
         [
                 { "ID": 1, "NAME": "Alice", "GRADE": 11.11 },
                 { "ID": 2, "NAME": "Bob", "GRADE": 22.22 }
               ]
             

If the action is successful, the data will be inserted into the database with the response code of `200`.




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the employees

This example lists all the employees in the `Employee` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). For example, `City='Bangalore'`. You can also specify multiple filter conditions by using the logic operators. For example, `City='Bangalore' and region='asia-south2'`. 



### Example - Get a record

This example gets a record with the specified ID from the `Employee` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `12294` in the **Default Value** field. 

Here, `12294` is a primary key value in the `Employee` entity.




### Example - Create a record in `Hana_unicode`

This example creates a record in the `Hana_unicode` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Hana_unicode` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ID": 2.0,
         "UNICODEDATA": "Unicode データ型はグローバル化されたデータの保存に使用されます",
         "TEST": "Test7"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "ID": 2.0,
         "UNICODEDATA": "Unicode データ型はグローバル化されたデータの保存に使用されます",
         "TEST": "Test7"
         }




### Example - Create a record in `Languages`

This example creates a record in the `Languages` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Languages` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ID": 5,
         "ARABICTEXT": "مرحبا",
         "GERMANTEXT": "Günther",
         "HINDITEXT": "नमस्ते",
         "ENGLISHTEST": "Test1"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "ID": 5.0,
         "ARABICTEXT": "مرحبا",
         "GERMANTEXT": "Günther",
         "HINDITEXT": "नमस्ते",
         "ENGLISHTEST": "Test1"
         }




### Example - Update a record

This example updates a record in the `Employee` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "SALARY": 9000.0
         }

  5. Click **entityId** , and then enter `12294` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "SALARY": 9000.0
         }




### Example - Delete a record

This example deletes the record with the specified ID in the `Employee` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `10001` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
database | STRING | False | The name of the SAP HANA database.   
browsable_schemas | STRING | False | This property restricts the schemas reported to a subset of the available schemas. For example, BrowsableSchemas=SchemaA,SchemaB,SchemaC.   
include_system_objects | BOOLEAN | False | Set IncludeSystemObjects to True to fetch Hana System schema and tables.   
include_table_types | BOOLEAN | False | If set to true, the provider will report the types of individual tables and views.   
session_variables | STRING | False | A comma-separated list of session variables to set on the current connection.   
enable_logging | ENUM | False | Enables verbosity for logging during a connection by selecting a level between 1 (least verbose) and 5 (most verbose). This feature can aid in troubleshooting error messages or other unexpected behavior. However, please be aware that this option will log all communication details, including requests, responses, and SSL certificates, between the connector and backend. Therefore, it is not advisable to utilize this function in a live production environment. Supported values are: 1, 2, 3, 4, 5  
  
## Use the SAP Hana connection in an integration

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
