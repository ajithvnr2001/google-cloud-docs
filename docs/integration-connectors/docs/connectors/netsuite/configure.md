---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/netsuite/configure/
title: NetSuite \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:29.063577+00:00
---

# NetSuite  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/netsuite/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# NetSuite

The NetSuite connector lets you perform insert, delete, update, and read operations on NetSuite data.

## Before you begin

Before using the NetSuite connector, do the following tasks:

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
     1. **Connector** : Select **Netsuite** from the drop down list of available Connectors.
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
     8. **Account Id** : The company account your username is associated with on NetSuite. 
     9. **Aggregate Column Mode** : Indicating how aggregate columns should be treated. 
     10. **Application Id** : As of version 2020.1, requests to NetSuite require an application ID. 
     11. **Custom Field Permissions** : A comma separated list of custom field permissions. Gives more control than IncludeCustomFieldColumns . 
     12. **Include Child Tables** : A boolean indicating if child tables should be displayed. 
     13. **Include Custom Field Columns** : A boolean indicating if you would like to include custom field columns. 
     14. **Include Custom List Tables** : A boolean indicating if you would like to use tables based on custom lists. 
     15. **Include Custom Record Tables** : A boolean indicating if you would like to use tables based on custom record types. 
     16. **Include Reference Columns** : A comma separated list representing the columns to include when retrieving data from a field representing a record reference. 
     17. **Maximum Concurrent Sessions** : The maximum number of concurrent sessions available for use in the connection. 
     18. **Net Suite Date Format** : The preferred date format set in NetSuite UI. 
     19. **Net Suite Long Date Format** : The preferred long date format set in NetSuite UI. 
     20. **Netsuite Metadata Folder** : A path to a directory to download metadata files from NetSuite. Set this for best performance. 
     21. **Report Doubles As Decimal** : Indicates if doubles should be reported as decimal. 
     22. **Request Memorized Transactions** : A boolean indicating if you would like to request memorized transactions when retrieving transactions from NetSuite. 
     23. **Role Id** : The RoleId is the InternalId of the role that will be used to log in to NetSuite. Leave empty to use the user's default role. 
     24. **Schema** : The type of schema to use. You can select any of the following values: 
        * **SuiteTalk** \- For SOAP based connectivity.
        * **SuiteSQL** \- For REST based connectivity. 
     25. **Use Async Services** : A boolean indicating if you would like to use asynchronous services when inserting, updating, and deleting. 
     26. **Use Internal Names For Customizations** : A boolean indicating if you would like to use internal names for customizations. 
     27. **Use Upserts** : A boolean indicating if you would like to perform an upsert when an insert operation is used. 
     28. **User Timezone Offset** : Your user timezone offset as defined in your NetSuite preferences under Home --> Preferences --> Time Zone. Ex: EST. 
     29. **Row Scan Depth** : The number of rows to scan when dynamically determining columns for the table. 
     30. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     31. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     32. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : You can specify the destination details either as a host address or a service attachment. Select any of the following destination types: 
        * **Host address** : If you want to specify the hostname or IP address of the destination.
        * **Service attachment** : If you want to specify the private endpoint for your internal IP addresses. The service attachment, lets you hide your internal IP addresses from the external network. You can create a service attachment in Google Cloud, by using the Private Service Connect feature. For information on configuring a Private Service Connect, see [Publish managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

Based on your selection of destination type, enter the host address or the service attachment name.

To enter additional destinations, click **+Add destination**.

     2. Click **Next**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Netsuite connection:

        * Username and password 
        * Token Based Authentication 
        * OAuth 2.0 Auth Code Grant 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  7. **Review** : Review your connection and authentication details.
  8. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**

Username and password authentication. This is valid only for Netsuite version 2020.2 or older.

    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.


  * **Token Based Authentication**

Token Based Authentication for Netsuite. This can be used for both `SuiteTalk` and `SuiteQL` schemes.

    * **OAuth Client Id** : the Consumer Key displayed when the application was created.
    * **OAuth Client Secret** : Secret Manager Secret containing the consumer secret displayed when the application was created.
    * **OAuth Access Token** : the Token Id when the access token was created.
    * **OAuth Access Token Secret** : Secret Manager Secret containing the token secret when the access token was created.


  * **OAuth 2.0 - Authorization code**

Authorization of connection is done with a web-based user login flow. This is valid only for the `SuiteQL` scheme.

    * **Client ID** : The client ID used for requesting access tokens.
    * **Scopes** : A comma-separated list of the required scopes.
    * **Client secret** : The client secret used for requesting access tokens.

For the `Authorization code` authentication type, after creating the connection, you should perform a few additional steps for configuring authentication. For more information, see Additional steps after connection creation.

**Note:** If you are using `Authorization code` authentication type and have made any configuration changes in your external application, you must re-authorize your HTTP connection. To understand how to re-authorize, see Re-authorization for Authorization code. 


### Additional steps after connection creation

If you selected `OAuth 2.0 - Authorization code` for authentication, you must do the following additional steps after creating the connection:

  1. In the [Connections page](https://console.cloud.google.com/connectors/connections), locate the newly created connection. 

Notice that the **Status** for the new connector will be **Authorization required**.

  2. Click **Authorization required**. 

This shows the **Edit authorization** pane.

  3. Copy the **Redirect URI** value to your external application.
  4. Verify the authorization details.
  5. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com/connectors/connections).




## Re-authorization for Authorization code

If you are using `Authorization code` authentication type and have made any configuration changes in your backend NetSuite application, you must re-authorize your NetSuite connection. To re-authorize a connection, perform the following steps:

  1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

  2. Click **Edit** to edit the connection details. 
  3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

  4. Click **Save**. This takes you to the connection details page.
  5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
  6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




### Configure NetSuite

To generate client ID, client secret, token ID and token secret, do the following:

  1. Create a new integration in Netsuite.
  2. Provide integration details such as name, and enable token-based authentication.
  3. Specify a callback URL, such as `https:cloud.google.com/connectors/oauth?e=ApplicationIntegrationConnectorPaginatedFieldsLaunch%3A%3AApplicationIntegrationConnectorPaginatedFieldsEnabled&project=PROJECT_NAME`.
  4. After you submit the integration, you will receive a client ID and client secret. Save these details.
  5. [Set up an integration user record](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_160810961778.html#Setting-Up-the-Integration-User-Record).
  6. To create a token and secret, navigate to the **Home page** , select **Manage Access Tokens** , and then click on **New My Access Token**. You will use these details to create a token based authentication in Google Cloud.



For information about how to set up postman, see [Importing the Postman Collection](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1545059880.html#Importing-the-Postman-Collection).

## System limitations

The Netsuite connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the NetSuite connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Entity operation examples

This section lists the entity operations supported by the Netsuite connector and shows how to perform some of the [entity operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

Entity | Supported Operations  
---|---  
CreditMemo | LIST, GET, CREATE, UPDATE  
Customer | LIST, GET, CREATE, UPDATE  
CustomerPayment | LIST, GET, CREATE, UPDATE  
ItemFulfillment | LIST, GET, CREATE  
JournalEntry | LIST, GET, CREATE  
PurchaseOrder | LIST, GET, CREATE, UPDATE  
ReturnAuthorization | LIST, GET, CREATE  
SalesOrder | LIST, GET, CREATE, UPDATE  
Vendor | LIST, GET, CREATE, UPDATE  
VendorBill | LIST, GET, CREATE, UPDATE  
VendorCredit | LIST, GET, CREATE, UPDATE  
VendorPayment | LIST, GET, CREATE, UPDATE  
CashRefund | LIST, GET, CREATE  
CashSale | LIST, GET, CREATE  
CustomerDeposit | LIST, GET  
CustomerRefund | LIST, GET  
Employee | LIST, GET  
Estimate | LIST, GET  
File | LIST, GET  
InventoryAdjustment | LIST, GET, CREATE  
InventoryItem | LIST, GET  
ItemReceipt | LIST, GET  
Opportunity | LIST, GET  
PaycheckJournal | LIST, GET, CREATE  
SupportCase | LIST, GET  
SupportCaseIssue | LIST, GET  
TransferOrder | LIST, GET, CREATE  
VendorReturnAuthorization | LIST, GET  
WorkOrder | LIST, GET  
AssemblyItem | LIST, GET  
Bin | LIST, GET  
CustomerCategory | LIST, GET  
ItemGroup | LIST, GET  
KitItem | LIST, GET  
LotNumberedAssemblyItem | LIST, GET  
LotNumberedInventoryItem | LIST, GET  
NonInventoryPurchaseItem | LIST, GET  
NonInventoryResaleItem | LIST, GET  
NonInventorySaleItem | LIST, GET  
OtherChargePurchaseItem | LIST, GET  
OtherChargeResaleItem | LIST, GET  
OtherChargeSaleItem | LIST, GET  
SerializedAssemblyItem | LIST, GET  
SerializedInventoryItem | LIST, GET  
ServicePurchaseItem | LIST, GET  
ServiceResaleItem | LIST, GET  
ServiceSaleItem | LIST, GET  
CreditMemo_itemList | CREATE  
Invoice_itemList | CREATE  
PurchaseOrder_itemList | CREATE  
SalesOrder_itemList | CREATE  
VendorBill_itemList | CREATE  
VendorCredit_itemList | CREATE  
VendorPayment_applyList | CREATE  
  
When you perform an insert operation in NetSuite, if all the necessary fields and data are not specified, the API to which the entity is aligned rejects the request. This results in an exception. The exception might vary based on the entity used in the insert operation. You must provide the NetSuite line items in the query to successfully insert data. You can specify the line item through the ItemListAggregate field that is available in all parent tables. The following is the format for the ItemListAggregate field: 
    
    
        "`<ItemList>`\n" +
                  "  <Row>\n" +
                          "    <ItemList_Item_InternalId>656</ItemList_Item_InternalId>\n" +
                          "    <ItemList_Item_Name>Iphone 15Pro</ItemList_Item_Name>\n" +
                          "    <ItemList_Line>1</ItemList_Line>\n" +
                          "    <ItemList_Description>Canon PowerShot Camera Test</ItemList_Description>\n" +
                          "    <ItemList_Amount>8500.0</ItemList_Amount>\n" +
                          "    <ItemList_Quantity>17.0</ItemList_Quantity>\n" +
                          "    <ItemList_Price_InternalId>1</ItemList_Price_InternalId>\n" +
                          "    <ItemList_Price_Name>List Price</ItemList_Price_Name>\n" +
                          "    <ItemList_Rate>500.00</ItemList_Rate>\n" +
                          "    <ItemList_Location_InternalId>1</ItemList_Location_InternalId>\n" +
                          "    <ItemList_Location_Name>02: NewYork</ItemList_Location_Name>\n" +
                          "    <ItemList_TaxCode_InternalId>-7</ItemList_TaxCode_InternalId>\n" +
                          "    <ItemList_TaxCode_Name>-Not Taxable-</ItemList_TaxCode_Name>\n" +
                          "    <ItemList_ShipGroup>1</ItemList_ShipGroup>\n" +
                          "    <ItemList_ItemIsFulfilled>false</ItemList_ItemIsFulfilled>\n" +
                          "    <CustomFieldListAggregate>\n" +
                          "      <CustomField InternalId=\"4779\" Type=\"platformCore:StringCustomFieldRef\" ScriptId=\"custcol121\">\n" +
                          "        <Value>1</Value>\n" +
                          "      </CustomField>\n" +
                          "    </CustomFieldListAggregate>\n" +
                          "  </Row>\n" +
                          "  <Row>\n" +
                          "    <ItemList_Item_InternalId>656</ItemList_Item_InternalId>\n" +
                          "    <ItemList_Item_Name>Iphone 15Pro</ItemList_Item_Name>\n" +
                          "    <ItemList_Line>4</ItemList_Line>\n" +
                          "    <ItemList_Description>Canon PowerShot Camera Test</ItemList_Description>\n" +
                          "    <ItemList_Amount>8500.0</ItemList_Amount>\n" +
                          "    <ItemList_Quantity>17.0</ItemList_Quantity>\n" +
                          "    <ItemList_Price_InternalId>1</ItemList_Price_InternalId>\n" +
                          "    <ItemList_Price_Name>List Price</ItemList_Price_Name>\n" +
                          "    <ItemList_Rate>500.00</ItemList_Rate>\n" +
                          "    <ItemList_Location_InternalId>2</ItemList_Location_InternalId>\n" +
                          "    <ItemList_Location_Name>01: California</ItemList_Location_Name>\n" +
                          "    <ItemList_TaxCode_InternalId>-7</ItemList_TaxCode_InternalId>\n" +
                          "    <ItemList_TaxCode_Name>-Not Taxable-</ItemList_TaxCode_Name>\n" +
                          "    <ItemList_ShipGroup>1</ItemList_ShipGroup>\n" +
                          "    <ItemList_ItemIsFulfilled>false</ItemList_ItemIsFulfilled>\n" +
                          "    <CustomFieldListAggregate>\n" +
                          "      <CustomField InternalId=\"4776\" Type=\"platformCore:StringCustomFieldRef\" ScriptId=\"custcol121\">\n" +
                          "        <Value>4</Value>\n" +
                          "      </CustomField>\n" +
                          "    </CustomFieldListAggregate>\n" +
                          "  </Row>\n" +
         "`</ItemList>`;"
      

### Example - List all the credit memos

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `CreditMemo` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



### Example - Get a CreditMemo record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CreditMemo from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. Set the entity ID to 1083723 which is the Key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `1083723` in the **Input Value** field and choose the EntityId as Local variable. 

Pass the entity ID directly. Passing an entity ID might throw an error if composite keys exist. In such cases, use the filter clause to specify the ID.




### Example - Create a PurchaseOrder record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select PurchaseOrder from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
                   "Entity_InternalId": "2041",
                   "Location_InternalId": "6",
                   " + "<ItemList>\n" +
                       "  <Row>\n" +
                           "    <ItemList_Item_InternalId>979</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Line>2</ItemList_Line>\n" +
                           "    <ItemList_Amount>66500.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "  <Row>\n" +
                           "    <ItemList_Item_InternalId>979</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Line>3</ItemList_Line>\n" +
                           "    <ItemList_Amount>16500.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "</ItemList>" + ",
                   "Email": "222larabrown@gmail.com"
               }

If the integration is successful, the `PurchaseOrder` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1093053"
           } 
           




### Example - Create a ReturnAuthorization record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select ReturnAuthorization from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
                   "Entity_InternalId": "1709",
                   "Status": "Approved",
                   " + "<ItemList>\n" +
                       "  <Row>\n" +
                           "    <ItemList_Item_InternalId>945</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Line>2</ItemList_Line>\n" +
                           "    <ItemList_Amount>2500.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "  <Row>\n" +
                           "    <ItemList_Item_InternalId>945</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Line>3</ItemList_Line>\n" +
                           "    <ItemList_Amount>16500.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "</ItemList>" + "
               }

If the integration is successful, the `ReturnAuthorization` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1093053"
           } 
           




### Example - Create a SalesOrder record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select SalesOrder from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
                   " + "<ItemList>\n" +
                       "  <Row>\n" +
                           "    <ItemList_Item_InternalId>945</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Line>1</ItemList_Line>\n" +
                           "    <ItemList_Amount>9990900.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "  <Row>\n" +
                           "    <ItemList_Item_InternalId>945</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Amount>99900.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "</ItemList>" + ",
                   "Entity_InternalId": "1709"
               }

If the integration is successful, the `SalesOrder` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1093053"
           } 
           




### Example - Create a CreditMemo_itemList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CreditMemo_itemList from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "ItemList_Item_InternalId": "945",
             "Entity_InternalId": "1709",
             "Location_InternalId": "5",
             "ItemList_Amount": 7777777.0,
             "ItemList_Description": "Created"
           }
           

If the integration is successful, the `CreditMemo_itemList` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1093053",
             "ListId": "1"
           }
           




### Example - Create a Customer record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Customer from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "CompanyName": "Bcone8",
             "Email": "222larabrown@gmail.com"
           }
           

If the integration is successful, the `Customer` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "4767"
           } 
           




### Example - Create an Invoice_itemList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Invoice_itemList from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "ItemList_Item_InternalId": "945",
             "Entity_InternalId": "1709",
             "ItemList_Amount": 945.0,
             "Item": "InvoiceItem"
           }
           

If the integration is successful, the `Invoice_itemList` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1093052",
             "ListId": "1"
           } 
           




### Example - Create a CustomerPayment record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CustomerPayment from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "Customer_InternalId": "1714",
             "Payment": 9999.0
           } 
           

If the integration is successful, the `CustomerPayment` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1090749"
           } 
           




### Example - Create a PurchaseOrder_itemList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select PurchaseOrder_itemList from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "Entity_InternalId": "2041",
             "Location_InternalId": "6",
             "ItemList_Description": "Created on Jan 11",
             "ItemList_Item_InternalId": "979"
           } 
           

If the integration is successful, the `PurchaseOrder_itemList` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1093151",
             "ListId": "1"
           }  
           




### Example - Create a SalesOrder_itemList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select SalesOrder_itemList from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "Email": "222larabrown@gmail.com",
             "Entity_InternalId": "1709",
             "ItemList_Item_InternalId": "945",
             "ItemList_Amount": 1000.0
           }
           

If the integration is successful, the `SalesOrder_itemList` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1093351",
             "ListId": "1"
           }  
           




### Example - Create a Vendor record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Vendor from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "CompanyName": "Deloitte",
             "LegalName": "AU Vendor"
           } 
           

If the integration is successful, the `Vendor` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "5067"
           }  
           




### Example - Create a VendorBill_itemList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select VendorBill_itemList from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "Entity_InternalId": "2041",
             "ItemList_Item_InternalId": "1374",
             "ItemList_Amount": 700.0
           } 
           

If the integration is successful, the `VendorBill_itemList` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "5067"
           }  
           




### Example - Create a VendorCredit_itemList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select VendorCredit_itemList from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "Entity_InternalId": "2041",
             "Location_InternalId": "6",
             "ItemList_Item_InternalId": "992",
             "ItemList_Description": "Created on Jan 12"
           }
           

If the integration is successful, the `VendorCredit_itemList` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1093353",
             "ListId": "1"
           }  
           




### Example - Create a VendorPayment_applyList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select VendorPayment_applyList from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "ApplyList_Doc": 3339.0,
             "ApplyList_Apply": true,
             "Entity_InternalId": "1471"
           }
           

If the integration is successful, the `VendorPayment_applyList` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1093756",
             "ListId": "1"
           }   
           




### Example - Create a CreditMemo record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CreditMemo from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
                   "ItemListAggregate": " + "<ItemList>\n" +
                          "  <Row>\n" +
                          "    <ItemList_Item_InternalId>6</ItemList_Item_InternalId>\n" +
                          "    <ItemList_Line>2</ItemList_Line>\n" +
                          "    <ItemList_Amount>8800.0</ItemList_Amount>\n" +
                          "  </Row>\n" +
                          "  <Row>\n" +
                          "    <ItemList_Item_InternalId>6</ItemList_Item_InternalId>\n" +
                          "    <ItemList_Line>3</ItemList_Line>\n" +
                          "    <ItemList_Amount>9900.0</ItemList_Amount>\n" +
                          "  </Row>\n" +
                          "</ItemList>" + ",
                   "Entity_InternalId": "11",
                   "Email": "222larabrown@gmail.com"
               }

If the integration is successful, the `CreditMemo` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "106"
           }
           




### Example - Create an Invoice record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Invoice from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
                   "ItemListAggregate": " + "<ItemList>\n" +
                       "  <Row>\n" +
                           "    <ItemList_Item_InternalId>6</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Line>1</ItemList_Line>\n" +
                           "    <ItemList_Amount>7998500.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "  <Row>\n" +
                           "    <ItemList_Item_InternalId>6</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Line>2</ItemList_Line>\n" +
                           "    <ItemList_Amount>6500.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "</ItemList>" + ",
                   "Memo": "May9"
               }

If the integration is successful, the `Invoice` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "206"
           }
           




### Example - Create an ItemFulfillment record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select ItemFulfillment from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "CreatedFrom_InternalId": "411",
             "ShipStatus": "_picked"
           } 
           

If the integration is successful, the `ItemFulfillment` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "412"
           }
           




### Example - Create a JournalEntry record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select JournalEntry from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
                   "Subsidiary_InternalId": "1",
                   "Memo": "Journal Entry created on April 2",
                   "LineListAggregate":" + "<LineList>\n" +
                       "  <Row>\n" +
                           "    <LineList_Account_InternalId>1</LineList_Account_InternalId>\n" +
                           "    <LineList_Line>1</LineList_Line>\n" +
                           "    <LineList_credit>500.0</LineList_credit>\n" +
                           "  </Row>\n" +
                           "  <Row>\n" +
                           "    <LineList_Account_InternalId>1</LineList_Account_InternalId>\n" +
                           "    <LineList_Line>1</LineList_Line>\n" +
                           "    <LineList_debit>500.00</LineList_debit>\n" +
                           "  </Row>\n" +
                           "</LineList>" + "
               }

If the integration is successful, the `JournalEntry` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "612"
           }
           




### Example - Create a PurchaseOrder record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select PurchaseOrder from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
                   "Entity_InternalId": "2041",
                   "Location_InternalId": "6",
                   " + "<ItemList>\n" +
                       "  <Row>\n" +
                           "    <ItemList_Item_InternalId>979</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Line>2</ItemList_Line>\n" +
                           "    <ItemList_Amount>66500.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "  <Row>\n" +
                           "    <ItemList_Item_InternalId>979</ItemList_Item_InternalId>\n" +
                           "    <ItemList_Line>3</ItemList_Line>\n" +
                           "    <ItemList_Amount>16500.0</ItemList_Amount>\n" +
                           "  </Row>\n" +
                           "</ItemList>" + ",
                   "Email": "222larabrown@gmail.com"
               }

If the integration is successful, the `PurchaseOrder` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1116228"
           }
           




### Example - Create a VendorBill record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select VendorBill from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {"Entity_InternalId": "12",
           " + "<ItemList>\n" +
                       "  <Row>\n" +
                               "    <ItemList_Item_InternalId>7</ItemList_Item_InternalId>\n" +
                               "    <ItemList_Line>1</ItemList_Line>\n" +
                               "    <ItemList_Amount>77700.0</ItemList_Amount>\n" + +
                               "  </Row>\n" +
                               "  <Row>\n" +
                               "    <ItemList_Item_InternalId>7</ItemList_Item_InternalId>\n" +
                               "    <ItemList_Line>2</ItemList_Line>\n" +
                               "    <ItemList_Amount>888888</ItemList_Amount>\n" + +
                               "  </Row>\n" +
                               "</ItemList>;" + "}

If the integration is successful, the `VendorBill` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "816"
           }
           




### Example - Create a VendorCredit record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select VendorCredit from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {"Entity_InternalId": "12",
           " + "<ItemList>\n" +
                       "  <Row>\n" +
                               "    <ItemList_Item_InternalId>7</ItemList_Item_InternalId>\n" +
                               "    <ItemList_Line>1</ItemList_Line>\n" +
                               "    <ItemList_Amount>77700.0</ItemList_Amount>\n" +
                               "  </Row>\n" +
                               "  <Row>\n" +
                               "    <ItemList_Item_InternalId>7</ItemList_Item_InternalId>\n" +
                               "    <ItemList_Line>2</ItemList_Line>\n" +
                               "    <ItemList_Amount>888888</ItemList_Amount>\n" +
                               "  </Row>\n" +
                               "</ItemList>;" + "}

If the integration is successful, the `VendorCredit` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "818"
           }
           




### Example - Create a VendorPayment record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select VendorPayment from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "Entity_InternalId": "12",
             "ApplyList_Apply": true,
             "ApplyList_Doc": 714.0
           }       
           

If the integration is successful, the `VendorPayment` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
             "InternalId": "1025",
             "ListId": "1"
           } 
           




### Example - Create a TRANSFERORDER record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select TRANSFERORDER from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "Location_InternalId": "1",
           "TransferLocation_InternalId": "3",
           "ItemListAggregate": 
            " + "<ItemList>\n" +
                       "  <Row>\n" +
                       "    <ItemList_Item_InternalId>8</ItemList_Item_InternalId>\n" +
                       "    <ItemList_Line>1</ItemList_Line>\n" +
                       "    <ItemList_Amount>77700.0</ItemList_Amount>\n" +
                       "  </Row>\n" +
                       "  <Row>\n" +
                       "    <ItemList_Item_InternalId>8</ItemList_Item_InternalId>\n" +
                       "    <ItemList_Line>2</ItemList_Line>\n" +
                       "    <ItemList_Amount>888888</ItemList_Amount>\n" +
                       "  </Row>\n" +
                       "</ItemList>;"
           }
           

If the integration is successful, the `TRANSFERORDER` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
           "InternalId": "1337"
           } 
           




### Example - Create a CashSale record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CashSale from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "Entity_InternalId": "10",
           "Location_InternalId": "3",
           "ItemListAggregate": 
            "<ItemList>\n" +
                       "  <Row>\n" +
                       "    <ItemList_Item_InternalId>8</ItemList_Item_InternalId>\n" +
                       "    <ItemList_Line>1</ItemList_Line>\n" +
                       "    <ItemList_Amount>77700.0</ItemList_Amount>\n" +
                       "  </Row>\n" +
                       "  <Row>\n" +
                       "    <ItemList_Item_InternalId>8</ItemList_Item_InternalId>\n" +
                       "    <ItemList_Line>2</ItemList_Line>\n" +
                       "    <ItemList_Amount>888888</ItemList_Amount>\n" +
                       "  </Row>\n" +
                       "</ItemList>;"
           }
           

If the integration is successful, the `CashSale` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
           "InternalId": "1234"
           } 
           




### Example - Create a PaycheckJournal record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select PaycheckJournal from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "Employee_InternalId": "8",
           "Account_InternalId": "314",
           "EarningListAggregate":  
            "<EarningList>\n" +
                       "  <Row>\n" +
                       "    <EarningList_PayrollItem_InternalId>2</EarningList_PayrollItem_InternalId>\n" +
                       "    <EarningList_Amount>1998</EarningList_Amount>\n" +
                       "  </Row>\n" +
                       "</EarningList>;"
           }
           

If the integration is successful, the `PaycheckJournal` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
           "InternalId": "1746"
           } 
           




### Example - Create an InventoryAdjustment record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select InventoryAdjustment from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "Account_InternalId": "1",
           "AdjLocation_InternalId": "1",
           "Location_InternalId": "3",
           "InventoryListAggregate": 
            "<InventoryList>\n" +
                       "  <Row>\n" +
                       "    <InventoryList_Item_InternalId>8</InventoryList_Item_InternalId>\n" +
                       "    <InventoryList_Line>1</InventoryList_Line>\n" +
                       "    <InventoryList_Location_InternalId>1</InventoryList_Location_InternalId>\n" +
                       "    <InventoryList_AdjustQtyBy>100</InventoryList_AdjustQtyBy>\n" +
                       "  </Row>\n" +
                       "</InventoryList>;"
           }
           

If the integration is successful, the `InventoryAdjustment` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
           "InternalId": "1640"
           } 
           




### Example - Create a CashRefund record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CashRefund from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "Entity_InternalId": "10",
           "Location_InternalId": "3",
           "ItemListAggregate": 
            "<ItemList>\n" +
                       "  <Row>\n" +
                       "    <ItemList_Item_InternalId>8</ItemList_Item_InternalId>\n" +
                       "    <ItemList_Line>1</ItemList_Line>\n" +
                       "    <ItemList_Amount>799.0</ItemList_Amount>\n" +
                       "  </Row>\n" +
                       "  <Row>\n" +
                       "    <ItemList_Item_InternalId>8</ItemList_Item_InternalId>\n" +
                       "    <ItemList_Line>2</ItemList_Line>\n" +
                       "    <ItemList_Amount>666</ItemList_Amount>\n" +
                       "  </Row>\n" +
                       "</ItemList>;"
           }
           

If the integration is successful, the `CashRefund` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
           "InternalId": "1232"
           } 
           




### Example - Update a CreditMemo record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CreditMemo from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Email2": "222larabrown@gmail.com"
           } 
           

  5. Set the entity ID in Data Mapper to the entity of the CreditMemo. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 1090651`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "1090651"
           } 
           




### Example - Update a Customer record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Customer from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Email": "222larabrown@gmail.com"
           } 
           

  5. Set the entity ID in Data Mapper to the entity of the Customer. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 4767`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "4767"
           } 
           




### Example - Update an Invoice record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Invoice from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Email2": "222larabrown@gmail.com"
           } 
           

  5. Set the entity ID in Data Mapper to the entity of the Invoice. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 1083927`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "1083927"
           } 
           




### Example - Update a CustomerPayment record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CustomerPayment from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Customer_InternalId": "1714",
             "Payment": 7.77777777E8
           } 
           

  5. Set the entity ID in Data Mapper to the entity of the CustomerPayment. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 1090749`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "1090749"
           } 
           




### Example - Update a PurchaseOrder record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select PurchaseOrder from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Message": "Aspirin Updated"
           } 
           

  5. Set the entity ID in Data Mapper to the entity of the PurchaseOrder. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 1000`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "1000"
           } 
           




### Example - Update a SalesOrder record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select PurchaseOrder from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Email": "222larabrown@gmail.com",
             "Entity_InternalId": "1709",
             "Item_InternalId": "945"
           }
           

  5. Set the entity ID in Data Mapper to the entity of the SalesOrder. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 1086949`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "1086949"
           } 
           




### Example - Update a Vendor record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Vendor from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "CompanyName": "Deloitte_Updated"
           } 
           

  5. Set the entity ID in Data Mapper to the entity of the Vendor. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 4567`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "4567"
           } 
           




### Example - Update a VendorBill record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select VendorBill from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Memo": "Memo_Jan 11"
           } 
           

  5. Set the entity ID in Data Mapper to the entity of the VendorBill. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 3339`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "3339"
           } 
           




### Example - Update a VendorCredit record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select VendorCredit from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Memo": "16253"
           } 
           

  5. Set the entity ID in Data Mapper to the entity of the VendorCredit. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 1091549`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "1091549"
           } 
           




### Example - Update a VendorPayment record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select VendorPayment from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Memo": "Jan8"
           } 
           

  5. Set the entity ID in Data Mapper to the entity of the VendorPayment. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to ` 1082627`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "InternalId": "1082627"
           } 
           




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
account_id | STRING | True | The company account your username is associated with on NetSuite.   
aggregate_column_mode | STRING | False | Indicating how aggregate columns should be treated.   
application_id | STRING | False | As of version 2020.1, requests to NetSuite require an application ID.   
custom_field_permissions | STRING | False | A comma separated list of custom field permissions. Gives more control than IncludeCustomFieldColumns .   
include_child_tables | BOOLEAN | False | A boolean indicating if child tables should be displayed.   
include_custom_field_columns | BOOLEAN | False | A boolean indicating if you would like to include custom field columns.   
include_custom_list_tables | BOOLEAN | False | A boolean indicating if you would like to use tables based on custom lists.   
include_custom_record_tables | BOOLEAN | False | A boolean indicating if you would like to use tables based on custom record types.   
include_reference_columns | STRING | False | A comma separated list representing the columns to include when retrieving data from a field representing a record reference.   
maximum_concurrent_sessions | INTEGER | False | The maximum number of concurrent sessions available for use in the connection.   
net_suite_date_format | STRING | False | The preferred date format set in NetSuite UI.   
net_suite_long_date_format | STRING | False | The preferred long date format set in NetSuite UI.   
netsuite_metadata_folder | STRING | False | A path to a directory to download metadata files from NetSuite. Set this for best performance.   
report_doubles_as_decimal | BOOLEAN | False | Indicates if doubles should be reported as decimal.   
request_memorized_transactions | BOOLEAN | False | A boolean indicating if you would like to request memorized transactions when retrieving transactions from NetSuite.   
role_id | STRING | False | The RoleId is the InternalId of the role that will be used to log in to NetSuite. Leave empty to use the user's default role.   
schema | STRING | True | The type of schema to use.   
use_async_services | BOOLEAN | False | A boolean indicating if you would like to use asynchronous services when inserting, updating, and deleting.   
use_internal_names_for_customizations | BOOLEAN | False | A boolean indicating if you would like to use internal names for customizations.   
use_upserts | BOOLEAN | False | A boolean indicating if you would like to perform an upsert when an insert operation is used.   
user_timezone_offset | STRING | False | Your user timezone offset as defined in your NetSuite preferences under Home --> Preferences --> Time Zone. Ex: EST.   
row_scan_depth | STRING | False | The number of rows to scan when dynamically determining columns for the table.   
verbosity | STRING | False | Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates).   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
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
