---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforsqlserver/configure/
title: Cloud SQL for SQL Server \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:03.645110+00:00
---

# Cloud SQL for SQL Server  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforsqlserver/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud SQL for SQL Server

The Cloud SQL for SQL Server connector lets you insert, read, update and delete rows in a SQL Server database.

## Supported versions

SQL Server versions: 2008, 2012, 2014, 2016, 2017, 2019, and 2022

## Before you begin

Before using the Cloud SQL for SQL Server connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`
      * `roles/cloudsql.editor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 

  * Enable the `sqladmin.googleapis.com` (Cloud SQL Admin API) service.


  * For information about creating Cloud SQL for SQL Server instance on Google Cloud, see [Create an instance on Google Cloud](https://cloud.google.com/sql/docs/sqlserver/create-instance).
  * For information about PSC connectivity using SOCKS5 proxy, see [PSC Connectivity using SOCKS5 proxy](https://cloud.google.com/integration-connectors/docs/configure-cloudsql-psc).



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
     1. **Connector** : Select **Cloud SQL for SQL Server** from the drop down list of available Connectors.
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
     8. **Project ID** : The ID of the Google Cloud project where the CloudSQL instance resides. 
     9. **Database Region** : The name of the region where the CloudSQL instance resides. 
     10. **Instance ID** : The ID of the CloudSQL instance to connect to. 
     11. **Database Name** : The name of the Sql Server database to connect to. 
     12. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     13. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

**Note:** If you are connecting to a private Cloud SQL instance, configure a SOCKS5 proxy server, and enter the hostname or IP address of the proxy in the **Host address** field.

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **NEXT**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Cloud SQL for SQL Server connection:

     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : The Sql Server username to use for the connection.
    * **Password** : Secret Manager Secret containing the password associated with the Sql Server username.



### Connection configuration samples

#### Basic authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | CloudSQL SQL Server  
Connector version | 1  
Connection Name | cloudsql-server-private  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Project ID | connectors-prod-test  
Database Region | us-central1  
Instance ID | google-cloud-bcone-sql-instance1  
Database Name | sqlcloudprivate_DB  
Minimum number of nodes | 2  
Maximum number of nodes | 2  
Destination Type | Host address  
host | HOST  
port | PORT  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
**Note:** The host address specified in the connection is the network endpoint attachment created using PSC connectivity via Socks5 proxy method.

## System limitations

The Cloud SQL for SQL Server connector can process a maximum of 30 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Cloud SQL for SQL Server connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



Also, see the [Perform CRUD operations on a MySQL database](https://docs.cloud.google.com/integration-connectors/docs/perform-crud-operation-mysql-database) tutorial that shows how to create a MySQL connection, and use the connection in an integration to perform read and write operations.

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

This section provides [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) available in this connector.

### Employee_Procedure action

This action fetches data of an employee.

#### Input parameters of the Employee_Procedure Action

Parameter name | Data type | Required | Description  
---|---|---|---  
ID | Int | True | The ID of the employee.  
  
For an example of how to configure the `Employee_Procedure` action, see Action examples.

## Action examples

This section provides examples of actions available in this connector.

### Example - Fetch data of an employee

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `Employee_Procedure` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ID": 3
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "ID": 3,
      "Name": "Charlie",
      "City": "Paris",
      "SALARY": 6500.0,
      "Department": "IT"
    }]
    




## Entity operation examples

This section provides examples of entity operations available in this connector.

### Example - List all the persons

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Persons` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** to meet your filtering needs.

You must use single quotes (') to enclose the value for a **filterClause**. You can use the **filterClause** to filter records based on the columns.




### Example - Get person details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Persons` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `1` in the **Default Value** field. This ID specifies the record to retrieve.



### Example - Delete a person

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Persons` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `9` in the **Default Value** field. This ID specifies the record to delete.



### Example - Create a person

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Persons` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "LastName": "Charlie",
           "FirstName": "Cruz",
           "Address": "123 Main Street",
           "City": "Paris"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following::
         
         {
           "PersonID": 100.0,
           "LastName": "Charlie",
           "FirstName": "Cruz",
           "Address": "123 Main Street",
           "City": "Paris"
         }
         




### Example - Create employee details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SQL_Performance_EmployeeDetails` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ID": 9.0,
           "FirstName": "Alex",
           "LastName": "Ariel",
           "MyDate": "2021-10-22",
           "MyTime": "13:54:19",
           "MySmallDateTime": "2021-10-22 13:54:00.0",
           "MyDateTime": "2021-10-22 13:54:19.057",
           "MyDateTime2": "2021-10-22 13:54:19.055",
           "MyDateTimeOffset": "2021-10-22 13:54:19.055",
           "MyDecimalColumn": 123.0,
           "MyNumericColumn": 12345.12,
           "salary": 4000.0,
           "Location": "Paris",
           "City": "Paris",
           "Designation": "Consultant",
           "Position": "Junior",
           "Experience": 5.0,
           "Emp_Father_Name": "Taylor",
           "Emp_Spouse": "Yuri",
           "Age": 29.0,
           "Celsius": 35.0,
           "Isregistered": "AA==",
           "Data": "{\"name\": \"Raj\",\"skills\": [\"SSIS\", \"SSRS\", \"JS\"],\"Age\": 30}",
           "Emp_Status": "Active",
           "Emp_Department": "IT",
           "Emp_Zip": 121212.0,
           "Sex": "Male",
           "Manager": "Dana",
           "ManagerId": 10.0,
           "Manager_Location": "Paris",
           "HR_Name": "Sasha",
           "Emp_Technology": "SQL",
           "Company_Name": "Altostrat",
           "Company_Location": "Paris",
           "Emp_Degree": "BE",
           "Emp_10TH": "Y",
           "Emp_12TH": "Y",
           "Emp_10Th_Marks": 70.0,
           "Emp_12TH_Marks": 80.0,
           "Emp_Degree_Marks": 90.0,
           "work": "WFH",
           "Emp_Language": "English",
           "Emp_System": "Laptop",
           "Daily_Hrs": 9.0,
           "Week_Days": 5.0,
           "Weekly_Off": 2.0,
           "Client_Name": "Google",
           "Client_Location": "Lisbon",
           "Team_Size": 15.0,
           "Reports_TO": "Manager"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "ID": 9.0,
           "FirstName": "Alex",
           "LastName": "Ariel",
           "City": "Paris",
           "Salary": 4000.0
         }
         




### Example - Create an employee

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "NAME": "Dana",
           "AGE": 30,
           "City": "Lisbon",
           "SALARY": 10000.0
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "ID": 88.0,
           "NAME": "Dana",
           "AGE": 30,
           "City": "Lisbon",
           "SALARY": 10000.0
         }
         




### Example - Update person details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Persons` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "LastName": "Charlie",
           "FirstName": "Cruz",
           "Address": "8 Rue du Nom Fictif",
           "City": "Paris"
         }
         

In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `10` in the **Default Value** field. This ID specifies the record to update. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `'10'`.

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
      "LastName": "Charlie",
      "FirstName": "Cruz",
      "Address": "8 Rue du Nom Fictif",
      "City": "Paris"
    }
    




### Example - Update employee details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SQL_Performance_EmployeeDetails` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Age": 30
         }
         

In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `5` in the **Default Value** field. This ID specifies the record to update. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `'5'`.

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
      "Age": 30
    }
    




### Example - Update an employee

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "AGE": 41,
           "City": "Paris",
           "SALARY": 10000.0
         }
         

  5. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `2` in the **Default Value** field. This ID specifies the record to update. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `'2'`.

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "AGE": 41,
           "City": "Paris",
           "SALARY": 10000.0
         }
         




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
project_id | STRING | True | Project ID of the project that contains the Cloud SQL instance. e.g. myproject.   
database_region | STRING | True | The cloud region for the instance. e.g. us-central1.   
instance_id | STRING | True | Database instance ID. This does not include the project ID. e.g. myinstance.   
database_name | STRING | True | Name of the database in the instance. e.g. mydatabase.   
  
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
