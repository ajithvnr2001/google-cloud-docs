---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/sybase/configure/
title: SAP ASE (Sybase) \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:56.296974+00:00
---

# SAP ASE (Sybase)  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/sybase/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SAP ASE (Sybase)

The Sybase connector lets you perform insert, delete, update, and read operations on Sybase.

## Before you begin

Before using the Sybase connector, do the following tasks:

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

Supported regions for connectors include: 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Sybase** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. **Service Account** : Select a service account that has the required roles.
     6. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     7. **Database** : The name of the Sybase database. 
     8. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     9. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : You can specify the destination details either as a host address or a service attachment. Select any of the following destination types: 
        * **Host address** : If you want to specify the hostname or IP address of the destination.
        * **Service attachment** : If you want to specify the private endpoint for your internal IP addresses. The service attachment, lets you hide your internal IP addresses from the external network. You can create a service attachment in Google Cloud, by using the Private Service Connect feature. For information on configuring a Private Service Connect, see [Publish managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

Based on your selection of destination type, enter the host address or the service attachment name.

To enter additional destinations, click **+Add destination**.

     2. Click **Next**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Sybase connection:

        * Username and password 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  7. **Review** : Review your connection and authentication details.
  8. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : The Sybase user account used to authenticate.
    * **Password** : Secret Manager Secret containing the password used to authenticate the user.
    * **Secret version** : The version of the secret that contains the password.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating a SAP ASE connection.

### Username and password connection type

The following table lists the connection properties that you need to specify to create a username and password connection: Field name | Details  
---|---  
Location | europe-west1  
Connector | SAP ASE  
Connector version | 1  
Connection Name | google-cloud-SAP ASE-soap-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Database | Alex  
Verbosity level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Host Address | 198.51.100.0  
Authentication | User Password  
Username | USERNAME  
Password | PASSWORD  
Secret Version | 1  
  
For information about LDAP user authentication, see [LDAP user authentication](https://help.sap.com/docs/SAP_ASE/2705a3b1e3df4514ab089cfedf87750d/a92c9fd3bc2b101487039c6bace8170a.html).

### SSL connectiontype

The following table lists the connection properties that you need to specify to create a SSL connection: Field name | Details  
---|---  
Location | us-central1  
Connector | Sybase  
Connector version | 1  
Connection Name | google-cloud-sybase-ssl-conn  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Database | Alex  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Trust Store | Private  
Custom Trust Store | CUSTOM TRUST STORE  
Secret Version | 2  
Client Certificate | CLIENT_CERTIFICATE  
Secret Version | 7  
Client Private Key | CLIENT PRIVATE KEY  
Secret Version | 4  
Client Private Key Passphrase | CLIENT PRIVATE KEY PASSPHRASE  
Secret Version | 1  
Host Address | 198.51.100.0  
Port | PORT  
Authentication | USER PASSWORD  
Username | USERNAME  
Password | PASSWORD  
Secret Version | 1  
  
For information about enabling SSL, see [Enabling SSL](https://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc01672.1572/html/sec_admin/sec_admin383.htm).

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

The Sybase connector can process 2 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

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

### Example - Create a table

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         CREATE TABLE customqueries98(
              ID   INT ,
              NAME VARCHAR (20),
              AGE  INT,
              City  CHAR (25) ,
              SALARY   DECIMAL (18, 2)  );

This example shows the Execute Custom Query to create a new table. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter returns a blank payload.




### Example - Alter a table

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         ALTER TABLE customqueries98 ADD CONSTRAINT ID PRIMARY KEY (ID)

This example shows the Execute Custom Query to alter a table. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter returns a blank payload.




### Example - Truncate a table

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         TRUNCATE TABLE customqueries99

This example shows the Execute Custom Query to truncate a table If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter returns a blank payload.




### Example - Drop a table

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         DROP TABLE customqueries99

This example shows the Execute Custom Query to drop a table. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter returns a blank payload.




### Example - Validate SUM

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         SELECT SUM(SALARY) as Total FROM EMPLOYEES

This example shows the Execute Custom Query to validate the SUM of the Aggregate function. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Total": 7500.0
      }] 




### Example - Validate AVG

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         SELECT AVG(SALARY) as Average FROM EMPLOYEES

This example shows the Execute Custom Query to validate AVG of Aggregate function. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Average": 7500.0
      }] 




### Example - Validate MAX

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         SELECT MAX(SALARY) as Max_Salary FROM EMPLOYEES

This example shows the Execute Custom Query to validate MAX of Aggregate Function. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Max_Salary": 7500.0
      }] 




### Example - Validate MIN

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         SELECT MIN(SALARY) as Min_Salary FROM EMPLOYEES

This example shows the Execute Custom Query to validate MIN of Aggregate function. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Min_Salary": 7500.0    
      }]




### Example - Validate COUNT

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         select count(*) from EMPLOYEES

This example shows the Execute Custom Query to validate Count of Aggregate function. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "": 1.0
      }]




### Example - Use Join and GroupBy

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         SELECT SmallMoney.amount, Sum(Testsybase.clone) AS Total
           FROM Testsybase
           INNER JOIN SmallMoney
           ON Testsybase.id = SmallMoney.id
           GROUP BY SmallMoney.amount;

This example shows the Execute Custom Query by using Join and GroupBy. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "amount": 1122.56,
        "Total": 14.0
      }, {
        "amount": 123.4567,
        "Total": 11.0
      }, {
        "amount": 1123.45,
        "Total": 13.0
      }]




### Example - Use Join and Query parameters

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         SELECT e.payload,e.rest,ed.id FROM Testsybase e, Smallmoney ed where e.id=ed.id and ed.id=?

This example shows the Execute Custom Query by using Join and Query parameters. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "payload": 5678.9,
        "rest": 13.6666,
        "id": 2.0
      }] 




### Example - Use GroupBy, Having and Count

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         select payload, count(payload) from Testsybase group by payload having count(payload)>=1

This example shows the Execute Custom Query by using GroupBy, Having and Count. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "payload": 1234.56,
        "": 1.0
      }, {
        "payload": 2345.67,
        "": 1.0
      }, {
        "payload": 4352.78,
        "": 1.0
      }, {
        "payload": 6789.12,
        "": 1.0
      }]




### Example - Use Column Cast, LIKE, and other operators

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         select e.id,e.clone from Testsybase e where e.payload>10 and e.rest LIKE '%1%' AND e.id<>3 order by e.id;

This example shows the Execute Custom Query by using Column Cast, LIKE, and other operators, such as i.e. <>. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "id": 1.0,
        "clone": 10.0
      }, {
        "id": 2.0,
        "clone": 99.0
      }, {
        "id": 4.0,
        "clone": 14.0
      }]




### Example - Execute a function by providing inputs in integration

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         SELECT dbo.MultiplyNumbers(5, 10) AS Result

This example shows the Execute Custom Query for executing a function by providing inputs in integration. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "Result": 50.0
      }] 




### Example - Create a function by providing inputs in integration

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         CREATE FUNCTION MultiplyNumbersTest1
           (@num1 INT, @num2 INT) 
           RETURNS INT AS RETURN @num1 * @num2

This example shows the Execute Custom Query for creating a function by providing inputs in integration. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter returns a blank payload.




### Example - Execute a procedure by providing inputs in integration

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "@EmpID": 1.0
           } 
           

This example shows the Execute Custom Query for executing a procedure by providing some input in integration. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "EmpID": 1.0,
        "LastName": "Test",
        "FirstName": "Bcone",
        "Address": "Noida",
        "City": "UP"
      }] 
      




### Example - Create a procedure by providing inputs in integration

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         CREATE PROCEDURE SelectAllEmployees2 @EmpID int
           AS
           SELECT * FROM Employees WHERE EmpID = @EmpID

This example shows the Execute Custom Query for creating a procedure by providing inputs in integration. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter returns a blank payload.




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the records

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select numbers_table from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - Get a record from an entity

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select numbers_table from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to Get single numbers_table. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `1.0` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Create a record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select numbers_table from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "bigint_column": 1.2345678901234516E16,
         "usmallint_column": 124.0,
         "numeric_column": 987.664,
         "real_column": 67.88999938964847,
         "uint_column": 125.0,
         "ubigint_column": 1.2345678901234516E16,
         "decimal_column": 124.459,
         "smallint_column": 16.0,
         "int_column": 125.0,
         "floatn_column": 154.45,
         "tinyint_column": 127.0,
         "id": 20.0
         }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
         "Success": true 
         }
         




### Example - Update a record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select numbers_table from the `Entity` list.
  3. Select the `Update` operation, and then click **Do ne**.
  4. Set the entity ID to Update a numbers_table. To set the entity ID, in the **Da ta mapper** section of the **Tasks** , click **e ntityId** and then enter `20.0` in the given field.
  5. In the **Da ta mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         
         {
         "uint_column": 128.0,
         "floatn_column": 154.95
         }

Running this example, returns an empty payload on success.




### Example - Delete data from a table

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select numbers_table from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to Delete numbers_table. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `2.0` in the **Input Value** field and choose the EntityId as Local variable. 



## Use the Sybase connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).



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
