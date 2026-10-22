---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/acumatica/configure/
title: Acumatica \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:02.783616+00:00
---

# Acumatica  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/acumatica/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Acumatica

The Acumatica connector lets you perform insert, delete, update, and read operations on a Acumatica database.

## Before you begin

Before using the Acumatica connector, do the following tasks:

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




### Configure Acumatica

For information about installing Acumatica ERP, see [Install Acumatica ERP](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=a7107850-2ba2-48c3-913f-efbed9f306d8). 

Acumatica ERP instance comes with the default user account that you can use to sign in to the system. You can start working with Acumatica ERP after changing the password for the default user.

  1. To launch the application instance, click **Perform Application Maintenance** on the welcome page of the Acumatica ERP configuration wizard .
  2. Click on the link that is automatically generated in the Acumatica ERP program group.
  3. Navigate to http://localhost/INSTANCE_NAME in the web browser, enter the INSTANCE_NAME; the name which is specified in the virtual directory field during configuration.

If you used the default name for the virtual directory during the deployment of the instance, use http://localhost/AcumaticaERP/.

The http://localhost/INSTANCE_NAME URL works only on the local computer where you have installed Acumatica ERP Tools. To access the Acumatica ERP instance remotely, use the fully qualified domain name (FQDN) of the server instead of localhost in the URL.

  4. Enter the following on the Sign-In page:
  5. **Username** : enter "admin" as the username.
  6. **Password** : enter the password.
  7. Click **Sign In**.
  8. Enter the new password in the **New Password** column and click **Confirm Password**. 
  9. Click **Acumatica User Agreement** , and read the user agreement.
  10. Select **Check here** to indicate that you have read and agreed to the terms of the Acumatica user agreement, and agree to these terms of the user agreement.
  11. Click **Sign In**.



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
     1. **Connector** : Select **Acumatica** from the drop down list of available Connectors.
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
     8. **Company** : Your Acumatica Company. 
     9. **Endpoint Name** : The name of the endpoint in Acumatica WebService which you wish to access. You can find available endpoints in Web Service Endpoints form in Acumatica ERP. 
     10. **Endpoint Version** : The version of the endpoint. You can find available endpoints in Web Service Endpoints form in Acumatica ERP and their version under Endpoint Version. 
     11. **Inquiry Tables** : Comma seperated Inquiry Tables. Inquiry tables in Contract 3 Acumatica API version 17.200.001 are: AccountByPeriodInquiry, AccountBySubaccountInquiry, AccountDetailsInquiry, AccountSummaryInquiry, InventoryAllocationInquiry, InventorySummaryInquiry, InvoicedItemsInquiry, SalesPricesInquiry,VendorPricesInquiry. 
     12. **Schema** : Used to specify what Acumatica API to use. The default one is the REST Contact API. When OData is specified the OData API will be used and all the Generic Inquires exposed via OData will be dynamically retrieved. 
     13. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     14. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     15. Click **NEXT**.
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

The following authentication types are supported by the Acumatica connection:

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

This section lists the sample values for the various fields that you configure when creating the Acumatica connection.

### REST connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Acumatica  
Connector version | 1  
Connection Name | acumatica  
Enable Cloud Logging | False  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Host | https://examplepetstore.com  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
  
## OData connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Acumatica  
Connector version | 1  
Connection Name | acumatica  
Enable Cloud Logging | False  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Company | Example Organization  
Endpoint Version |  22.200.001  | Inquiry Table |  PX_Objects_AP_APInvoice   
Schema |  OData   
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Host | https://examplepetstore.com  
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

The Acumatica connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### ExecuteAction action

This action lets you execute an action.

#### Input parameters of the ExecuteAction action

Parameter name | Data type | Required | Description  
---|---|---|---  
ActionName | String | No | The name of the action that you are going to execute.  
EntityRecord | String | No | The entity record in the JSON format or the temporary table of entity records to which the action should be applied.  
Parameters | String | No | The parameters of the action in the JSON format.  
TopLevelEntity | String | No | The name of the entity type for which you are going to perform an action.  
  
#### Output parameters of the ExecuteAction action

This action returns confirmation message of the ExecuteAction.

For example on how to configure the `ExecuteAction` action, see Examples.

## Action examples

### Example - Execute an action

This action executes the specified action.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ExecuteAction` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ActionName": "PrintSalesOrder",   
         "TopLevelEntity": "SalesOrder"
         "EntityRecord": "{
         "Type": {
           "value": "IN"
         },
         "OrderNbr": {
           "value": "000007"
         },
         "CustomerID": {
           "value": "CANDYY"
         },
         "LocationID": {
           "value": "MAIN"
         }}}"

If the action is successful, the `ExecuteAction` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success",   
    "AffectedRecords": "1"
    }] 




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the customers

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



### Example - List all the journal transactions

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `JournalTransaction` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all the sales orders

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesOrder` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - Get a purchase order details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PurchaseOrder` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to get a purchase order details. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `000001` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Get a sales person details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Salesperson` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to get a sales person details. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `SP0001` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Get a vendor details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Vendor` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to get a vendor details. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `ACMEDO` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Delete an account

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Account` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to delete an account. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `10250` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Delete a customer

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to delete a customer. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `SANDWICH` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Delete a sales person

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Salesperson` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to delete sales person. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `SP0004` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Create a journal transaction

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `JournalTransaction` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Description": "go again",
           "BatchNbr": "000008",
           "CurrencyID": "INR",
           "Module": "GL" 
             }
           

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
             "BatchNbr": "000016",   "Module": "GL" 
             }]
             




### Example - Create a customer

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
              "LocationName": "Primary Location",
              "StatementCycleID": "WEEKLY",
              "CustomerClass": "CSTMRCLAS1",
              "CurrencyID": "INR",
              "CustomerID": "BISCCITY",
              "CustomerName": "Biscuit City Cafe" 
              }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
              "CustomerID": "BISCCITY"
              }




### Example - Create a sales order

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesOrder` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
              "Approved": true,
              "BaseCurrencyID": "INR",
              "CashAccount": "10200",
              "ControlTotal": 30.0,
              "CustomerID": "BISCCITY",
              "Description": "SO--0016"
              }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
              "OrderNbr": "000025",
              "OrderType": "CS" 
              }




### Example - Create a purchase order

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PurchaseOrder` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
              "ControlTotal": 200.0,
              "CurrencyID": "INR",
              "Description": "PO--14",
              "VendorID": "ACMEDO"
              }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
              "OrderNbr": "000021",
              "Type": "Normal"
              }




### Example - Create a sales person

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Salesperson` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
              "Name": "Sales person 0009",
              "SalespersonID": "SP0009",
              "DefaultCommission": 10.0
              }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
              "SalespersonID": "SP0009" 
              }




### Example - Create a vendor

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Vendor` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
              "APAccount": "20000",
              "CashAccount": "10200",
              "LocationName": "Secondary Location",
              "MaxReceipt": 100.0,
              "MinReceipt": 0.0,
              "VendorClass": "DEFAULTV",
              "VendorID": "ALLFRUITS"
              }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
              "VendorID": "ALLFRUITS"
              }




### Example - Create a bill

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Bill` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
              "Amount": 10.0,
              "Description": "new test",
              "DueDate": "2024-01-26 00:00:00.0",
              "LocationID": "MAIN",
              "Terms": "30D",
              "Vendor": "TESTVENDOR"
              }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
              "ReferenceNbr": "000020",
              "Type": "Bill"
              }




### Example - Create a check

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Check` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
              "Description": "check check check",
              "CurrencyID": "INR",
              "CashAccount": "10200",
              "PaymentMethod": "CHECK",
              "Vendor": "ACMEDO"
              }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
              "ReferenceNbr": "000013",
              "Type": "Payment"
              }




### Example - Create a sales invoice

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesInvoice` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
              "Description": "testing custom",
              "Amount": 10.0,
              "Balance": 0.0,
              "CustomerID": "BISCCITY",
              "DueDate": "2023-04-21 00:00:00.0"
              }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
              "ReferenceNbr": "000024",
              "Type": "Invoice"
              }




### Example - Create an invoice

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Invoice` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { 
              "Terms": "30D",
              "Description": "forever",
              "LocationID": "MAIN",
              "Customer": "BISCCITY", 
              "LinkARAccount": "11000"
              }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
              "ReferenceNbr": "000026",
              "Type": "Invoice"
              }




### Example - Update a sales order details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesOrder` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "Approved": true,
               "Description": "SO--0014"
                 }
           

  5. Click **entityId** , and then enter `000025` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
               "OrderNbr": "000025",
               "OrderType": "CS"
                 }]
           




### Example - Update a payment details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Payment` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to update a payment details. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **FilterClause** and then enter `ReferenceNbr='000007' AND Type='Payment'` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "CurrencyID": "INR"
         }
         

Instead of specifying the **entityId** , you can also set the **filterClause** to `ReferenceNbr='000007' AND Type='Payment'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "ReferenceNbr": "000007",
    "Type": "Payment" 
    }
    




### Example - Update a project transaction details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `ProjectTransaction` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to update a project transaction details. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **FilterClause** and then enter `Module='PM' AND ReferenceNbr='PM00000003'` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "Description": "updated"
         }
         

Instead of specifying the **entityId** , you can also set the **filterClause** to `Module='PM' AND ReferenceNbr='PM00000003'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "Module": "PM",
    "ReferenceNbr": "PM00000003"
    }




### Example - Update a journal transaction details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `JournalTransaction` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to update a journal transaction details. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **FilterClause** and then enter `BatchNbr='000016' AND Module='GL'` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "BatchNbr": "000012",
         "CurrencyID": "INR",
         "Description": "updated",
         "Module": "GL"
         }
         

Instead of specifying the **entityId** , you can also set the **filterClause** to `BatchNbr='000016' AND Module='GL'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "BatchNbr": "000012",
    "Module": "GL"
    }
    




### Example - Update a customer details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to update a customer details. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `BISCCITY` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "LocationName": "Primary Location",
         "StatementCycleID": "DAILY",
         "CustomerID": "BISCCITY",
         "CustomerClass": "CSTMRCLAS1",
         "Terms": "30D"
         }
         

Instead of specifying the **entityId** , you can also set the **filterClause** to `BISCCITY`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "CustomerID": "BISCCITY"
    } 




### Example - Update a purchase order details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PurchaseOrder` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to update a purchase order details. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **FilterClause** and then enter `OrderNbr='000025' AND OrderType='CS'` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "Approved": true,
         "Description": "SO--0014"
         }
         

Instead of specifying the **entityId** , you can also set the **filterClause** to `OrderNbr='000025' AND OrderType='CS'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "OrderNbr": "000025",
    "OrderType": "CS"
    }




### Example - Update a sales person details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Salesperson` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to update a sales person details. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `SP0009` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "DefaultCommission": 20.0
         }
         

Instead of specifying the **entityId** , you can also set the **filterClause** to `SP0009`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "SalespersonID": "SP0009"
    }




### Example - Update a bill details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Bill` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to update a bill details. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **FilterClause** and then enter `ReferenceNbr='000019' AND Type='Bill'` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "Amount": 10.0,
         "Description": "updated"
         }
         

Instead of specifying the **entityId** , you can also set the **filterClause** to `ReferenceNbr='000019' AND Type='Bill'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "ReferenceNbr": "000019",
    "Type": "Bill"
    }




### Example - Update a check details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Check` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to update a check details. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **FilterClause** and then enter `ReferenceNbr='000013' AND Type='Payment'` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "Description": "updated check"
         }
         

Instead of specifying the **entityId** , you can also set the **filterClause** to `ReferenceNbr='000013' AND Type='Payment'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "ReferenceNbr": "000013",
    "Type": "Payment"
    }




### Example - Update a sales invoice details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SalesInvoice` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to update a sales invoice details. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **FilterClause** and then enter `ReferenceNbr='000024'` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "Description": "shipping pastries"
         }
         

Instead of specifying the **entityId** , you can also set the **filterClause** to `ReferenceNbr='000024'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "ReferenceNbr": "000024",
    "Type": "Invoice"
    }




## Use the Acumatica connection in an integration

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
