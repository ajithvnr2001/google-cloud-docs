---
url: https://docs.cloud.google.com/application-integration/docs/perform-crud-operation-mysql-database/
title: Perform CRUD operations on a MySQL database \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:09.910190+00:00
---

# Perform CRUD operations on a MySQL database  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/perform-crud-operation-mysql-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Perform CRUD operations on a MySQL database

This tutorial shows you how to connect to a MySQL database instance from a sample integration and perform the list, get, create, update, and delete operations on a MySQL database table.

##  Before you begin 

  * Ensure that you have access to Application Integration.
  * Select the Google Cloud project and perform the following tasks:

    * Grant the following roles to the service account that you want to use to create the connection: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`
    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

If these services have not been enabled for your project previously, you are prompted to enable them when [creating the connection](https://docs.cloud.google.com/application-integration/docs/perform-crud-operation-mysql-database#create-connection).

  * Ensure that you have access to a MySQL server that you can use to create a database. For a list of all the supported connectors and the supported versions, see [ Connector reference](https://docs.cloud.google.com/integration-connectors/docs/connector-reference-overview). 



## Create a database and table in MySQL

Run the following commands from a system that has a MySQL client installed: 

  1. Connect to your MySQL server: 
         
         mysql --host=MYSQL_HOSTNAME_OR_IP_ADDRESS --port=PORT_NUMBER -uUSERNAME -pPASSWORD

Replace the following: 
     * `MYSQL_HOSTNAME_OR_IP_ADDRESS`: the name or IP address of your MySQL server. 
     * `PORT_NUMBER`: the port number for your MySQL server. 
     * `USERNAME`: the username for your MySQL server. 
     * `PASSWORD`: the user's password for your MySQL server. 
  2. Create a MySQL database: 
         
         CREATE DATABASE tutorialDB;

  3. Create a table: 
         
         CREATE TABLE EMPLOYEE
           (
           employee_id int auto_increment primary key,
           employee_first_name varchar(500) NOT null,
           employee_last_name varchar(500) NOT null,
           employee_emailID varchar(500)
           ); 

  4. Add rows to the `EMPLOYEE` table that you created: 
         
         INSERT INTO EMPLOYEE (employee_first_name,employee_last_name,employee_emailID) values ("Peter","Dilliard","test-01@test.com");
         INSERT INTO EMPLOYEE (employee_first_name,employee_last_name,employee_emailID) values ("Meaghan","Webb","test-02@test.com");
         

  5. Verify that the table is created and rows are added: 
         
         SELECT * FROM EMPLOYEE;

The following table rows are displayed: 
         
         +-------------+---------------------+--------------------+------------------+
         | employee_id | employee_first_name | employee_last_name | employee_emailID |
         +-------------+---------------------+--------------------+------------------+
         |           1 | Peter               | Dilliard           | test-01@test.com |
         |           2 | Meaghan             | Webb               | test-02@test.com |
         +-------------+---------------------+--------------------+------------------+
         




## Create a MySQL connection

To enable an integration to connect to your MySQL database, create a new connection to your MySQL database: 

  1. Click **+Create new** to open the **Create Connection** page.
  2. In the **Location** section, choose the location for the connection. 
     1. From the **Region** list, select the region where you want to create the connection. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  3. In the **Connection Details** section, enter the following details: 
     1. From the **Connector** list, select **MySQL**.
     2. From the **Connector version** list, select the connector version. 
     3. In the **Connection Name** field, enter a name for the connection instance. 

Connection names must meet the following criteria: 

        * Use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Names must begin with a letter and end with a letter or number.
        * Names cannot exceed 49 characters.
     4. Optional: In the **Description** field, add a description of the connection instance.
     5. Optional: Enable **Cloud Logging**.
     6. From the **Service Account** list, select a service account that has the required roles.
     7. In the **Database name** field, enter the name of the MySQL database.
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
     10. Optional: To add a label to the connection, click **+Add Label**.
     11. Click **Next**.
  4. In the **Destinations** section, enter details of the remote host (backend system) to which you want to connect. 
     * From the **Destination Type** list, select a host address. 
       * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
       * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+Add Destination**.

  5. Click **Next**.
  6. In the **Authentication** section, you can provide credentials: 
     * In the **Username** field, enter the MySQL username for the connection.
     * In the **Password** field, enter the [Secret Manager](https://console.cloud.google.com/security/secret-manager) secret containing the password associated with the MySQL username. 
       * If you have previously created a secret, and it is not available in the list, select **Enter Secret Manually**. In the **Add a secret by resource ID** dialog, copy and paste the resource ID from the [Secret Manager](https://console.cloud.google.com/security/secret-manager). 
         * To use the latest version, copy and paste the resource ID from the parent secret, in the format: `"projects/project-number/secrets/secret-name"`
         * To select a specific version, copy and paste the resource ID for that specific version, in the format `"projects/project-number/secrets/secret-name/versions/1"`

To add the secret, click **Add Secret**.

       * If you have not created a secret for use with MySQL, click **Create New Secret**. In the **Create Secret** dialog enter the following details: 
         * In the **Name** field, enter the secret name.
         * In the **Secret value** field, enter the contents of the secret or upload a file that contains the secret.
         * Click **Create Secret**.
     * From the **Secret version** list, select the version of the **Password** secret from the list of available versions in the drop-down. 
     * Click **Next**. 


* In the **Review** section, review your connection and authentication details.
* Click **Create**.

## Configure an Integration to use the MySQL connection

To use the MySQL connection that you created in an integration, you must perform the following tasks: 

  1. Create a new integration.
  2. Add and configure an API trigger.
  3. Add and configure a Connectors task.
  4. Connect the API Trigger element to the Connectors task element.



### Create a new integration

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click **Create integration**.
  4. In the **Integration name** field, enter a name for your integration.
**Note** : Integration names must meet the following requirements: 
     * Names must start and end with letters or numbers.
     * Names cannot contain spaces or more than one dash or underscore in a row.
  5. Optional: In the **Description** field, enter a description. 
  6. From the **Region** list, select a region for the integration. The **Regions** list only lists the regions provisioned in your Google Cloud project. To provision a new region, click **Enable Region**. For information about how to provision new regions, see [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region).
  7. To open the integration editor, click **Create**.



### Add and configure an API trigger

After you **create a new integration** , you can add and configure an **API** trigger to your integration. To do so, follow these steps: 

  1. In the integration editor toolbar, click **Triggers** to display a list of available triggers.
  2. Drag the **API** element to the integration editor.



### Add and configure a Connectors task

To configure a **Connectors** task to list all the entities in the `employee` table, follow these steps: 

  1. In the integration editor toolbar, click **Tasks** to display the list of available tasks.
  2. Drag the **Connectors** element to the integration editor.
  3. Click the **Connectors** task element on the designer to open the **Connectors** panel.
  4. In the **Connectors** panel, click **Configure Connector**. 

In the **Connector Task Editor** dialog that appears, follow these steps: 

     1. From the **Region** list, select the connection region where you created your MySQL connection. 
     2. From the **Connection** list, select the MySQL connection that you created and then click **Next**.
     3. In the **Type** section, select **Entities** and then click **Next**.
     4. From the **Entity** list, select **employee**.
     5. From the **Operation** list, select **List** and then click **Next**.
     6. To complete the connection configuration and close the dialog, click **Done**.



### Connect the API Trigger element to the Connectors task element

Next, add an edge connection to connect the API trigger to the Connectors task. An edge connection is a connection between any two elements in an integration. For information about edges and edge conditions, see [Edges](https://docs.cloud.google.com/application-integration/docs/edge-overview). 

To add the edge connection, follow these steps:

  1. At the bottom of the API Trigger element, click the **Fork** control point.
  2. Drag and drop the edge connection at the **Join** control point at the top of the connectors task element.



## Test the Integration

To test the integration, follow these steps:

  1. In the integration editor toolbar, click **Test**.
  2. Optional: Change the **Execution Deadline (in minutes)** value, and then click **Test Integration**. 
  3. After the integration completes successfully, the **Test Integration** pane displays the message **Integration execution succeeded**. To view the logs, click **View logs**. 
  4. Expand the **Response Parameters** section. In **Connector output payload** , the following output is displayed: 
         
         [ {
             "employee_id": 1.0,
             "employee_first_name": "Peter",
             "employee_last_name": "Dilliard",
             "employee_emailID": "test-01@test.com"
           },
           {
             "employee_id": 2.0,
             "employee_first_name": "Meaghan",
             "employee_last_name": "Webb",
             "employee_emailID": "test-02@test.com"
           } ]




## Perform other operations on your MySQL database table

When you configure a Connectors task in your integration, you can select any one of the following operations:

  * List
  * Get
  * Create
  * Update
  * Delete



You've already used the List operation to view all the rows in the `employee` table. In the following sections of this tutorial, you'll use the Get, Create, Update, and Delete operations to add, modify or remove rows from the `employee` table. 

### Get a row from a table

If you know the entity ID (or primary key) of the row that you want to fetch, provide that value as input to a Get operation in your integration. The details returned by the Get operation are similar to the details returned by the List operation. However, while the List operation fetches details of all the table rows that match the specified query, the Get operation fetches details of only the table row that matches the specified entity ID. 

Remember that, while the List operation by default returns all the rows in the table, the Get operation requires an entity ID as a search parameter. So, to use the Get operation, you must know the entity ID of the row that you want to fetch, or provide a default value for the entity ID. 

To get details of a specified row, perform the following steps to configure the **Connectors** task that you created earlier: 

  1. In integration editor, click the connectors task element to view the **Connectors** configuration pane.
  2. In the **Connectors** configuration pane, click **Configure Connector**. In the **Connector Task Editor** dialog that appears, follow these steps: 
  3. In the **Set entities/action** section, from the **Operations** list, select **Get**.
  4. Click **Done**.


* In the **Connectors** configuration pane, expand the **Task Input** section. Then, do the following: 

  1. Click the entity ID.
  2. In the **Edit variable** dialog that appears, select **Input to Integration**.
  3. Click **Save**


* In the integration editor toolbar, click **Test**.
* Optional: Change the **Execution Deadline (in minutes)** value.
* Enter the entity ID of the entity for which you want to fetch details. For example, `2`.
* Click **Test Integration**.
* After the integration completes successfully, the **Test Integration** pane displays the message **Integration execution succeeded**. To view the logs, click **View logs**.
* Expand the **Response Parameters** section. In **Connector output payload** , the following output is displayed: 
    
    
    [ {
        "employee_id": 2.0,
        "employee_first_name": "Meaghan",
        "employee_last_name": "Webb",
        "employee_emailID": "test-02@test.com"
      } ]

* You can verify that the information displayed here matches the information in the corresponding row in your MySQL table. To view this information in your MySQL table, execute the following command from your MySQL client: 
    
    
    SELECT * FROM employee WHERE employee_id=2;

The following table row is displayed: 
    
    
    +-------------+---------------------+--------------------+------------------+
    | employee_id | employee_first_name | employee_last_name | employee_emailID |
    +-------------+---------------------+--------------------+------------------+
    |           2 | Meaghan             | Webb               | test-02@test.com |
    +-------------+---------------------+--------------------+------------------+
        

### Add a row to a table

The Create operation allows you to add a row in a table. When you use the Create operation, you must provide all the values for the entity in the connector input payload. 

To add a row using the Create operation, perform the following steps to configure the **Connectors** task that you created earlier: 

  1. In integration editor, click the connectors task element to view the **Connectors** configuration pane.
  2. In the **Connectors** configuration pane, click **Configure Connector**. In the **Connector Task Editor** dialog that appears, follow these steps: 
  3. In the **Set entities/action** section, from the **Operations** list, select **Create**.
  4. Click **Done**.


* In the **Connectors** configuration pane, expand the **Task Input** section. Then, do the following: 

  1. Click the entity ID.
  2. In the **Edit variable** dialog that appears, select **Input to Integration**
  3. Click **Save**.


* In the integration editor toolbar, click **Test**.
* Optional: Change the **Execution Deadline (in minutes)** value.
* Enter the details for the entity that you want to create. For example, to add a new employee in the `employee` table, enter the following JSON: 
    
    
    {
      "employee_first_name": "Mary",
      "employee_last_name": "Smith",
      "employee_emailID": "test-03@test.com"
    }

**Note** : Don't specify the primary key, `employee_id`, as it is a read-only value that is generated when the row is added to the table. 
* Click **Test Integration**.
* After the integration completes successfully, the **Test Integration** pane displays the message **Integration execution succeeded**. To view the logs, click **View logs**.
* Expand the **Response Parameters** section. In **Connector output payload** , the following output is displayed: 
    
    
    {
      "employee_first_name": "Mary",
      "employee_last_name": "Smith",
      "employee_emailID": "test-03@test.com"
    }

Under **Connector output payload** , the entity ID is displayed as output: 
    
    
    {
      "employee_id": 3.0
    }

* You can verify that the row is added in your MySQL table. To view this information in your MySQL table, execute the following command from your MySQL client: 
    
    
    SELECT * FROM employee;

The following table rows are displayed: 
    
    
    +-------------+---------------------+--------------------+------------------+
    | employee_id | employee_first_name | employee_last_name | employee_emailID |
    +-------------+---------------------+--------------------+------------------+
    |           1 | Peter               | Dilliard           | test-01@test.com |
    |           2 | Meaghan             | Webb               | test-02@test.com |
    |           3 | Mary                | Smith              | test-03@test.com |
    +-------------+---------------------+--------------------+------------------+
        

### Update a row in a table

Use the Update operation to make changes to the values in a table row. For example, you can use this operation to update the email ID of an employee in the `employee` table. To specify the entity that you want to update, you can provide the entity ID as you did for the Get operation. Alternatively, you can use the **Filter clause** parameter to pass values on which to filter the table rows. This is useful if you want to make the same change in multiple rows based on specific search criteria. 

To update a table row, perform the following steps to configure the **Connectors** task that you created earlier: 

  1. In integration editor, click the connectors task element to view the **Connectors** configuration pane.
  2. In the **Connectors** configuration pane, click **Configure Connector**. In the **Connector Task Editor** dialog that appears, follow these steps: 
  3. In the **Set entities/action** section, from the **Operations** list, select **Update**.
  4. Click **Done**.


* In the **Connectors** configuration pane, expand the **Task Input** section. Then, do the following: 

  1. Click **Filter clause**.
  2. In the **Edit variable** dialog that appears, select **Input to Integration**
  3. Click **Save**.


* In the integration editor toolbar, click **Test**.
* Optional: Change the **Execution Deadline (in minutes)** value.
* Enter the criteria that you want to filter by. For example, to find an employee with the email ID `test-03@test.com`, enter: 
    
    
    employee_emailID="test-03@test.com"

**Note** : If you have multiple table rows that match the filter criteria, the update that you specify in the next step is made on all the matching rows.
* Enter the values that you want to update. For example, to update the email ID of all the employees in the `employee` table whose current email ID matches the filter clause `test-03@test.com`, enter the following JSON: 
    
    
    {
      "employee_emailID": "msmith@test.com"
    }

**Note** : You don't need to specify values for all the columns in the table. Enter the values that you want to update. The other values aren't modified. 
* Click **Test Integration**.
* After the integration completes successfully, the **Test Integration** pane displays the message **Integration execution succeeded**. 

To validate that the entity was updated, use the Get operation to get the details of the specified entity. 

* You can verify that the row is updated in your MySQL table. To view this information in your MySQL table, execute the following command from your MySQL client: 
    
    
    SELECT * FROM employee;

The following table rows are displayed: 
    
    
    +-------------+---------------------+--------------------+------------------+
    | employee_id | employee_first_name | employee_last_name | employee_emailID |
    +-------------+---------------------+--------------------+------------------+
    |           1 | Peter               | Dilliard           | test-01@test.com |
    |           2 | Meaghan             | Webb               | test-02@test.com |
    |           3 | Mary                | Smith              | msmith@test.com  |
    +-------------+---------------------+--------------------+------------------+
          

### Delete a row in a table

You can use the Delete operation to delete one or more table rows. Provide the entity ID or use the filter clause to specify the rows that you want to delete. Remember that, if you use the filter clause to specify criteria for rows that you want to delete, it's possible to delete multiple rows that match the given filter. If you want to delete only one specific row, use the entity ID. 

To delete a table row using the entity ID, perform the following steps to configure the **Connectors** task that you created earlier: 

  1. In integration editor, click the connectors task element to view the **Connectors** configuration pane.
  2. In the **Connectors** configuration pane, click **Configure Connector**. In the **Connector Task Editor** dialog that appears, follow these steps: 
  3. In the **Set entities/action** section, from the **Operations** list, select **Get**.
  4. Click **Done**.


* In the **Connectors** configuration pane, expand the **Task Input** section. Then, do the following: 

  1. Click the entity ID.
  2. In the **Edit variable** dialog that appears, select **Input to Integration**
  3. Click **Save**.


* In the integration editor toolbar, click **Test**.
* Optional: Change the **Execution Deadline (in minutes)** value.
* Enter the entity ID of the entity for which you want to fetch details. For example, `2`.
* Click **Test Integration**.
* After the integration completes successfully, the **Test Integration** pane displays the message **Integration execution succeeded**. 

To validate that the table row was deleted, use the Get operation to get the details of the row that you deleted. This should return an error for the specified entity ID.

You can also use the List operation and optionally provide a filter clause for the table row (or rows) that you deleted. This returns the list of rows remaining, which could be an empty list. 

For example, if you deleted the table row with entity ID 3, then if you specify the filter clause `employee_emailID="msmith@test.com"` or the entity ID **3** for the List operation, the response parameters in the logs display `[]`.

* You can verify that the row is deleted in your MySQL table. To verify this in your MySQL table, execute the following command from your MySQL client: 
    
    
    SELECT * FROM employee;

The following table rows are displayed: 
    
    
    +-------------+---------------------+--------------------+------------------+
    | employee_id | employee_first_name | employee_last_name | employee_emailID |
    +-------------+---------------------+--------------------+------------------+
    |           1 | Peter               | Dilliard           | test-01@test.com |
    |           2 | Meaghan             | Webb               | test-02@test.com |
    +-------------+---------------------+--------------------+------------------+
            

## What's next

Try building integrations with other connectors. For the list of all the supported connectors, see [All Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/connector-reference-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
