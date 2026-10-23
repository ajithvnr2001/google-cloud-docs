---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/sageintacct/configure/
title: Sage Intacct \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:53.211992+00:00
---

# Sage Intacct  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/sageintacct/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sage Intacct

The Sage Intacct connector lets you perform insert, delete, update, and read operations on Sage Intacct data.

## Supported versions

The Sage Intacct connector supports the Sage Intacct REST API.

## Before you begin

Before using the Sage Intacct connector, do the following tasks:

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



  * To connect to Sage Intacct, you must have a web services developer license, which includes a web services sender ID. If you need a developer license, contact the Sage Intacct team. The company that receives the API calls must [ authorize the sender ID](https://developer.intacct.com/support/faq/#why-am-i-getting-an-error-about-an-invalid-web-services-authorization). You must login to the company as a [Web Services user](https://www.intacct.com/ia/docs/en_US/help_action/Administration/Users/web-services-only-users.htm?cshid=Web_services_users).



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
     1. **Connector** : Select **Sage Intacct** from the drop down list of available Connectors.
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
     7. **Company ID** : The company ID to authenticate to Intacct.
     8. **Client ID** : The client ID of the distributed child company to access.
     9. **Sender ID** : The web services sender ID assigned to you by Intacct.
     10. **Sender Password** : The password corresponding to the web services sender ID.
     11. **Include Detail Aggregate** : Includes the item aggregate, which contains child entity information corresponding to the parent entity. 
     12. **Use Legacy** : Uses Legacy API implementation.
     13. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
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

The following authentication types are supported by the Sage Intacct connection:

     * Username and Password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and Password**
    * **Username** : Username for connector.
    * **Password** : Secret Manager Secret containing the password associated with the connector.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when you create the connection.

### Basic authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Sage Intacct  
Connector version | 1  
Connection Name | sage-intacct-integrationuser  
Enable Cloud Logging | Yes  
Service Account | Your_Project_Number.iam.gserviceaccount.com  
Company ID | Company@123  
Sender ID | ID@1234  
Sender Password | Password@1234  
Include Detail Aggregate | True  
Use Legacy | False  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host Address  
Host 1 | https://api.intacct.com/xx/xml/xmlgw.phtml  
Authentication | Yes  
Username | User_Name  
Password | Password  
Secret version | 1  
  
### Basic read only connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Sage Intacct  
Connector version | 1  
Connection Name | sage-intacct-basicereadonly  
Enable Cloud Logging | Yes  
Service Account | Your_Project_Number.iam.gserviceaccount.com  
Company ID | Company@123  
Include Detail Aggregate | True  
Use Legacy | False  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host Address  
Host 1 | https://api.intacct.com/xx/xml/xmlgw.phtml  
Authentication | Yes  
Username | User_Name  
Password | Password  
Secret version | 1  
  
## Use the Sage Intacct connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



### Support for stored procedures

This connector supports user-defined stored procedures and functions. If you have any stored procedures and functions in your backend, those are listed in the `Actions` column of the `Configure connector task` dialog. 

## System limitations

The Sage Intacct connector can process a maximum of 1 query per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) supported by the Sage Intacct connector. To understand how to configure the actions, see Action examples.

### CreateAttachment action

This action creates an attachment.

#### Input parameters of the CreateAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
SupDocId | String | Yes | The id of the attachment supdoc.  
SupDocFolderName | String | Yes | The name of the attachment folder.  
SupDocDescription | String | Yes | Description of the attachment.  
Attachment Name | String | Yes | The name of the attachment.  
Attachment Type | String | Yes | The attachment type.  
Attachment data | String | Yes | Attachment data encoded in base64.  
SupDocName | String | Yes | The name of the supdoc.  
  
For example on how to configure the `CreateAttachment` action, see  Examples.

### UpdateAttachment action

This action updates the attachment.

#### Input parameters of the UpdateAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
SupDocFolderName | String | Yes | The name of the attachment folder.  
AttachmentName | String | Yes | The attachment name.  
SupDocDescription | String | Yes | Description of the attachment.  
SupDocId | String | Yes | The id of the attachment supdoc.  
  
For example on how to configure the `UpdateAttachment` action, see  Examples.

### ReverseInvoice Action

This action reverses the invoice.

#### Input parameters of the ReverseInvoice action

Parameter name | Data type | Required | Description  
---|---|---|---  
Key | String | Yes | The id of the invoice that is to be reversed.  
DateReversed | String | Yes | The reversal date of the invoice.  
  
For example on how to configure the `ReverseInvoice` action, see Examples.

### VoidAPPayment action

This action performs the VoidAPPayment action on the invoices.

#### Input parameters of the VoidAPPayment action

Parameter name | Data type | Required | Description  
---|---|---|---  
Key | String | Yes | The id of the invoice that is to be updated.  
  
For example on how to configure the `VoidAPPayment` action, see Examples.

### ApproveVendor action

This action approves the vendors.

#### Input parameters of the ApproveVendor action

Parameter name | Data type | Required | Description  
---|---|---|---  
VendorRecordNumber | String | Yes | The record number of the vendor.  
  
For example on how to configure the `ApproveVendor` action, see Examples.

### DeclineVendor action

This action declines a vendor.

#### Input parameters of the DeclineVendor action

Parameter name | Data type | Required | Description  
---|---|---|---  
VendorRecordNumber | String | Yes | The record number of the vendor.  
  
For example on how to configure the `DeclineVendor` action, see Examples.

### GetVendorApprovalHistory action

This action allows you to view vendor approval history.

#### Input parameters of the GetVendorApprovalHistory action

Parameter name | Data type | Required | Description  
---|---|---|---  
VendorRecordNumber | String | Yes | The record number of the vendor.  
  
For example on how to configure the `GetVendorApprovalHistory` action, see Examples.

## Action examples

This section lists the actions supported by the SageIntaact connector. To understand how to configure the actions.

### Example - CreateAttachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "SupDocId": "newSupDocID12",
             "SupDocFolderName": "MyTestFolder",
             "SupDocDescription": "Google Attachment",
             "AttachmentName": "Google attachment",
             "AttachmentType": "txt",
             "AttachmentData": "hi there, this is a testing protocol",
             "SupDocName": "New Document"
           }
           

This action returns confirmation message of the CreateAttachment If the action is successful, the `CreateAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [{
        "Result": "Success"
      }] 
      




### Example - UpdateAttachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "SupDocFolderName": "MyTestFolder",
               "AttachmentName": "Google attachment",
               "SupDocDescription": "Google updated description",
               "SupDocId": "newSupDocID12"
             }
             

This action returns confirmation message of the UpdateAttachment If the action is successful, the `UpdateAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [{
          "Result": "Success"
        }] 
        




### Example - ReverseInvoice

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ReverseInvoice` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "Key": "1708",
               "DateReversed": "2025-07-30"
               }
             

This action returns confirmation message of the ReverseInvoice If the action is successful, the `ReverseInvoice` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [{
          "Success": "success"
         }] 
        




### Example - VoidAPPayment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `VoidAPPayment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "Key": "1723"
               } 
             

This action returns confirmation message of the VoidAPPayment If the action is successful, the `VoidAPPayment` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [{
          "Success": "success"
        }] 
        




### Example - ApproveVendor

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ApproveVendor` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "VendorRecordNo": "30891"
               } 
             

This action returns confirmation message of the ApproveVendor If the action is successful, the `ApproveVendor` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [{
          "Success": "success"
        }] 
        




### Example - DeclineVendor

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeclineVendor` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "VendorRecordNo": "30892"
               } 
             

This action returns confirmation message of the DeclineVendor If the action is successful, the `DeclineVendor` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         [{
               "Success": "success"
              }] 
             




### Example - GetVendorApprovalHistory

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetVendorApprovalHistory` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "VendorRecordNo": "30892"
               }
             

This action returns confirmation message of the GetVendorApprovalHistory If the action is successful, the `GetVendorApprovalHistory` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         [{
               [{
               "approvaltype": "Create",
               "creationdate": "09/20/2024",
               "submittedby": "emma",
               "eventdate": "09/20/2024",
               "approverid": "",
               "approvedby": "IntegrationUser",
               "state": "Declined",
               "comments": "Declined byIntegrationUser, via API on 09/20/2024",
               "recordno": "10724"
             }]
             }]
             




## Supported entity operations

This section shows how to perform some of the [entity operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### Example - List all Vendors

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Vendor` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per your requirement.

The value for filter clause should be always passed within the single quotes (') in this format. You can make use of filter clause for filtering records based on any columns.




For the entity Sodocument, make sure to use a filter clause in your request, such as Docparid='Sales Order'.

### Example - Get a Vendor record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Vendor` from the `Entity` list.
  3. Select the `Get` operation, and then click**Done**.
  4. Here, the entity ID is "20001". To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"20001"` in the **Input Value** field and choose the EntityId as local variable. 

Value of entity id should be passed directly. Here, "20001" is the entity id and the unique primary key value, which should be passed

In cases, where passing single entity id can throw an error as there will be two composite keys. In such cases, you can make use of filter clause and pass the value, such as id = '20001'



### Example - Delete a Vendor record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Vendor` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Here, the entity id is set to "20001". To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"20001"` in the **Input Value** field and choose the EntityId as local variable. 

In cases, where the Entity has two composite business or primary keys instead of specifying the **entityId** , you can set the **filterClause** to ` id='20001'`.




### Example - Create a Vendor record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Vendor` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Displaycontact_companyname": "Altostrat",
               "Displaycontact_lastname": "Cymbalgroup",
               "Name": "Altostrat_Ltd"
             }
             

If the integration is successful, the `Vendor` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 83.0,
               "Vendorid": "20047"
             }
             




### Example - Create an APBill record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `APBill` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Whencreated": "2024-05-05",
               "Whenposted": "2024-06-06",
               "Recordid": "25",
               "Vendorid": "20029",
               "Currency": "USD",
               "Itemaggregate":"<APBILLITEM>
                 <ACCOUNTNO>60400</ACCOUNTNO>
                 <TRX_AMOUNT>700</TRX_AMOUNT>
                 <ENTRYDESCRIPTION>Line 1 of my bill</ENTRYDESCRIPTION>
                 <LOCATIONID>100</LOCATIONID>
                 <DEPARTMENTID>300</DEPARTMENTID>
                 <VENDORID>20029</VENDORID>
                 </APBILLITEM>",
               "Whendue": "2024-12-12"
               }
             

If the integration is successful, the `APBill` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 1511.0
              }
             




### Example - Create a Vendtype record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Vendtype` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Name": "Google Created vendtype",
               "Status": "active"
               }
             

If the integration is successful, the `Vendtype` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Name": "Google Created vendtype",
               "Recordno": 16.0
               }
             




### Example - Create a Customer record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Name": "Altostrat_Ltd",
               "Displaycontact_firstname":"Altostrat"
               }
             

If the integration is successful, the `Customer` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 3663.0,
               "Customerid":"13825"
               }
             




### Example - Create an ARInvoice record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `ARInvoice` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Customerid": "10303",
               "Whencreated": "2024-07-30",
               "Itemaggregate": <lineitem>
                <glaccountno>40100</glaccountno>
                <amount>100</amount>
                <locationid>100</locationid>
                <departmentid>200</departmentid>
                </lineitem>",
               "Recordid": "789",
               "Whendue": "2024-08-30"
               }
             

If the integration is successful, the `Domains` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Success": true
              }
             




### Example - Create a CustType record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `CustType` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Name": "MGR PVT",
               "Status": "active"
               }
             

If the integration is successful, the `CustType` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Name": "MGR PVT"
               }
             




### Example - Create a ReportingPeriod record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select ReportingPeriod from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Header1": "Altostrat Reporting Period1",
               "Start_date": "2024-06-13",
               "End_date": "2024-06-15",
               "Name": "Google_Report_Test"
               }
             

If the integration is successful, the `ReportingPeriod` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 259.0
               }
             




### Example - Create a GLAccount record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `GLAccount` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Accountno": "12120",
               "Title": "Google_GLAccount_1"
               } 
             

If the integration is successful, the `GLAccount` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Accountno": "12120"
               }
             




### Example - Create a GLAcctGrp record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `GLAcctGrp` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Normal_balance": "credit",
               "Name": "AccountGrp13",
               "Iskpi": false,
               "Membertype": "Accounts"
               }
             

If the integration is successful, the `GLAcctGrp` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 484.0
               }
             




### Example - Create a Purchasing_Item record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Purchasing_Item` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Itemtype": "Non-Inventory",
               "Itemid": "89899",
               "Name": "Created Item"
               }
             

If the integration is successful, the `Purchasing_Item` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Itemid": "89899"
               }
             




### Example - Create an OrderEntity_Item record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `OrderEntity_Item` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Itemtype": "Inventory",
               "Itemid": "89899",
               "Name": "Created Item"
               }
             

If the integration is successful, the `OrderEntity_Item` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 76.0,
               "Itemid": "89899"
               }
             




### Example - Create a Checkingaccount record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Checkingaccount` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Bankaccountid": "100_VVV",
               "Bankaccountno": "442516879127",
               "Glaccountno": "20200",
               "Bankname": "Sapphire Venture Bank",
               "Routingno": "121010303",
               "Bankaccounttype": "checking",
               "Phone": "4085551212",
               "Locationid": "100",
               "Mailaddress_zip": "95110",
               "Mailaddress_city": "San Jose",
               "Mailaddress_state": "CA",
               "Mailaddress_country": "United States"
               }
             

If the integration is successful, the `Checkingaccount` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Bankaccountid": "100_VVV"
               }
             




### Example - Create a Savingsaccount record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Savingsaccount` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Bankaccountid": "CCI",
               "Bankname": "CCIB",
               "Locationid": "100"
               }
             

If the integration is successful, the `savingsaccount` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Bankaccountid": "CCI"
               }
             




### Example - Create a SOPriceList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SOPriceList` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Datefrom": "2024-01-01",
               "Dateto": "2025-01-01",
               "Name": "SOListGoogle"
               }
             

If the integration is successful, the `SOPriceList` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 28.0,
               "Name": "SOListGoogle"
               }
             




### Example - Create a Contacts record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Contacts` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Contactname": "Alex taylor's",
               "Printas": "sage intacct"
               }
             

If the integration is successful, the `Company_Contacts` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 3929.0,
               "Contactname": "Alex taylor's"
               }
             




### Example - Create a UserInfo record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `UserInfo` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Loginid": "Dana cruz",
               "Contactinfo_lastname": "Cruz",
               "Contactinfo_firstname": "Dana",
               "Contactinfo_email2": "danacruz@gmail.com",
               "Usertype": "business user"
               }
             

If the integration is successful, the `Company_UserInfo` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Loginid": "Dana cruz"
               }
             




### Example - Create a Department record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Department` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Departmentid": "GFK2",
               "Title": "Google Created department 2"
               }
             

If the integration is successful, the `Company_Department` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 10.0
               }
             




### Example - Create an EarningType record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `EarningType` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Name": "PRMethod",
               "Method": "Salary",
               "Billableacctno": "51701",
               "Nonbillableacctno": "51702"
               }
             

If the integration is successful, the `Company_EarningType` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": "9"
               }
             




### Example - Create an Employee record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Locationid": "100",
               "Personalinfo_contactname": "New Google"
               }
             

If the integration is successful, the `Company_Employee` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 42.0,
               "Employeeid": "1028"
               }
             




### Example - Create a Location record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Company_Location from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Locationid": "350",
               "Name": "Lisbon",
               "Parentid": "100",
               "Startdate": "2000-02-02",
               "Status": "inactive"
               }
             

If the integration is successful, the `Company_Location` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Locationid": "350"
               }
             




### Example - Creat a Project record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Project` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Name": "newproject",
               "Projectcategory": "Contract"
               }
             

If the integration is successful, the `Company_Project` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 19.0,
               "Projectid": "1013"
               }
             




### Example - Create an EmployeeEntityContacts record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `EmployeeEntityContacts` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Categoryname": "Primary Contact2",
               "Employee_employeeid": "1002",
               "Contact_name": "Charlie, Mahan"
              }
             

If the integration is successful, the `Company_EmployeeEntityContacts` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 284.0
               }
             




### Example - Create an EmployeeType record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `EmployeeType` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Name": "New employee type 1 Google",
               "Status": "active"
               }
             

If the integration is successful, the `Company_EmployeeType` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 9.0,
               "Name": "New employee type 1 Google"
               }
             




### Example - Create a GlBatch record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `GlBatch` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Journal": "PYRJ",
               "Batch_date": "2019-03-31",
               "Batch_title": "Google description non legacy",
               "Itemaggregate": "<GLENTRY>
                 <ACCOUNTNO>60400</ACCOUNTNO>
                 <DEPARTMENT>100</DEPARTMENT>
                 <LOCATION>100</LOCATION>
                 <CURRENCY>USD</CURRENCY>
                 <TR_TYPE>-1</TR_TYPE>
                 <AMOUNT>1450.80</AMOUNT>
                 <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
                 <DESCRIPTION>Accrued salaries</DESCRIPTION>
                 </GLENTRY>\n<GLENTRY>
                 <ACCOUNTNO>40200</ACCOUNTNO>
                 <DEPARTMENT>100</DEPARTMENT>
                 <LOCATION>100</LOCATION>
                 <TR_TYPE>1</TR_TYPE>
                 <AMOUNT>1450.80</AMOUNT>
                 <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
                 <DESCRIPTION>Salary expense</DESCRIPTION>\n</GLENTRY>",
                "State": "Draft"
                }
             

If the integration is successful, the `GlBatch` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 3138.0
              }
             




### Example - Create an AttachmentFolders record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AttachmentFolders` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "name": "Google"
              } 
             

If the integration is successful, the `AttachmentFolders` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Success": true
              }
             




### Example - Create a Bankacctrecon record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Bankacctrecon` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Financialentity": "100_SVB",
               "Stmtendingdate": "2023-01-01",
               "Mode": "Automatch",
               "Stmtendingbalance": 1659605.22
               }
             

If the integration is successful, the `Bankacctrecon` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 3.0
               }
             




### Example - Create a Podocument record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Podocument` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Docparid": "Purchase Requisition",
               "Whencreated": "2024-11-06",
               "Custvendid": "20034",
               "Contact_contactname": "New BGC(V20034)",
               "Billto_contactname": "New BGC(V20034)",
               "Itemaggregate": "<potransitem>
                 <itemid>60400</itemid>
                 <DEPARTMENT>I1</DEPARTMENT>
                 <quantity>100</quantity>
                 <unit>Each</unit>
                 <price>1</price>
                 <location>100</location>
                 <departmentid>100</departmentid>
                 </potransitem>"
             }
             

If the integration is successful, the `Podocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 3138.0
             }
             




### Example - Create a VendorGroup record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `VendorGroup` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Id": "AltostratTesting",
               "Name": "Googlecloud-vendor1",
               "Sortfield": "VENDORID",
               "Memberfilters": "<filter>
                 <MEMBERFILTERS>
                 <FIELD>VENDTYPE</FIELD>
                 <OPERATOR>=</OPERATOR>
                 <VALUE>Supplier</VALUE>
                 </MEMBERFILTERS>
                 <MEMBERFILTERS>
                 <FIELD>VENDTYPE</FIELD>
                 <OPERATOR>=</OPERATOR>
                 <VALUE>Burnham</VALUE>
                 </MEMBERFILTERS>
               </filter>"
              }
             

If the integration is successful, the `VendorGroup` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Success": true
              }
             




### Example - Create a Sodocument record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sodocument` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Custvendid": "10001",
               "Itemaggregate": """<sotransitem>
             <bundlenumber></bundlenumber>
                 <item_id>CSS1000</item_id>
                 <quantity>1</quantity>
                 <unit>Each</unit>
                 <price>2</price>
                 <locationid>100</locationid>
                 <departmemtid>100</departmentid>
                 </sotransitem>"",
               "Whencreated": "2024-09-14",
               "Docparid": "Sales Invoice"
             }
             

If the integration is successful, the `Sodocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
                "Docid": "Sales Invoice-IN0112"
               }
             




### Example - Create an Arpymt record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Arpymt` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Financialentity": "100_SVB",
               "Paymentmethod": "Cash",
               "Customerid": "10303",
               "Receiptdate": "2025-05-05",
               "Itemaggregate": "<ARPYMTDETAIL>
             <RECORDKEY>1677</RECORDKEY>
                 <TRX_PAYMENTAMOUNT>35</TRX_PAYMENTAMOUNT>
                 </ARPYMTDETAIL>"
             }
             

If the integration is successful, the `Arpymt` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 3138.0
              }
             




### Example - Create an Appymt record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Appymt` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
               "Financialentity": "100_SVB",
               "Paymentmethod": "EFT",
               "Vendorid": "20003",
               "Whencreated": "2024-08-28",
               "Itemaggregate": ""<APPYMTDETAIL>
             <RECORDKEY>1677</RECORDKEY>
                 <TRX_PAYMENTAMOUNT>35</TRX_PAYMENTAMOUNT>
                 </APPYMTDETAIL>""
             }
             

If the integration is successful, the `Appymt` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
               "Recordno": 1753.0
               }
             




### Example - Update a Vendor record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Vendor` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Name": "Altostrat,Lisbon"
              }
             

  5. Set the entity ID in Data Mapper to the entity of the Vendor. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `20044`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Vendorid": "20044"
              }
             




### Example - Update an APBill record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `APBill` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Whendue": "2024-12-12"
              }
             

  5. Set the entity ID in Data Mapper to the entity of the APBill. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `1371`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": 12.0
               }
             




### Example - Update a Customer record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Name": "Altostrat",
               "Status": "inactive"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the Customer. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Customerid='10100'\n`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": 21.0,
               "Customerid": "10100"
               }
             




### Example - Update a CustType record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `CustType` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Status": "inactive"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the CustType. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `MGR PVT`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Name": "MGR PVT"
               }
             




### Example - Update a ReportingPeriod record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `ReportingPeriod` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Start_date": "2024-06-14",
               "End_date": "2024-06-14",
               "Header1": "Reporting Time Changed"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the ReportingPeriod. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `257`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": 257.0
               } 
             




### Example - Update a GLAcctGrp record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `GLAcctGrp` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Title": "Google updated title"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the GLAcctGrp. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Name='AccountGrp13'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": 484.0
               }
             




### Example - Update a Purchasing_Item record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Purchasing_Item` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Sodescription": "Google updated description",
               "Name": "Google updated name"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the Purchasing_Item. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `89899`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Itemid": "89899"
               }
             




### Example - Update an OrderEntity_Item record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select OrderEntity_Item from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Name": "Item Update"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the OrderEntity_Item. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Recordno= '73' and Itemid= 'C32'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Itemid": "C32"
               }
             




### Example - Update a POPriceList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `POPriceList` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Status": "active"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the POPriceList. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Recordno='18'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": 18.0,
               "Name": "Special Purchasing price list"
               } 
             




### Example - Update a sodocument record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `sodocument` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Description": "Google_Update SO Document"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the sodocument . To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `189`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": "189"
               }
             




### Example - Update a Checkingaccount record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Checkingaccount` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Bankname": "Google updated bank name"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the Checkingaccount. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `100_SVBDF`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Bankaccountid": "100_SVBDF"
              }
             




### Example - Update a SOPriceList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SOPriceList` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Datefrom": "2022-01-01",
               "Dateto": "2026-01-01"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the SOPriceList. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `RecordNo='27'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": 1.0,
               "Name": "Base Price List"
               }
             




### Example - Update a Project record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Project` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Description": "Google updated description"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the Project. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `1010`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Projectid": "1010"
               }
             




### Example - Update an EmployeeType record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `EmployeeType` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Status": "inactive"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the EmployeeType. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Name='New employee type 1 Google'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": 9.0,
               "Name": "New employee type 1 Google"
               }
             




### Example - Update an EmployeeEntityContacts record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `EmployeeEntityContacts` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Categoryname": "updated contact"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the EmployeeEntityContacts. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `5.0`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": 5.0
               }
             




### Example - Update an Employee record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Employee` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Title": "Google Updated title"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the Employee. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `1024`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Employeeid": "1024"
               }
             




### Example - Update a UserInfo record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `UserInfo` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Usertype": "business user"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the UserInfo. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `RecordNo='41'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Loginid": "jsmithf"
               }
             




### Example - Update a Contact record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Contact` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Printas": "AT"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the Contact. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Recordno= '33533'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Recordno": 33533.0,
               "Contactname": "Alex taylor's g"
               }
             




### Example - Update a vendType record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `vendType` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Name": "Google updated name pv"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the vendType. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Name= 'Google Created vendtype'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Name": "Google Created vendtype"
               }
             




### Example - Update a customer record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `customer` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Status": "inactive"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the customer. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Recordno= '10001'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Customerid": "10001"
               }
             




### Example - Update a StatAccount record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `StatAccount` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Title": "Google_Update_Stat1111111"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the StatAccount. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Accountno= 'EPFOA'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Accountno": "EPFOA"
               }
             




### Example - Update a GlAccount record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `GlAccount` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Title": "Google_GLaccount_Update2"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the GlAccount. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Accountno= '10010'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Accountno": "10010"
              }
             




### Example - Update a PoPriceList record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PoPriceList` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Status": "inactive"
              }
             

  5. Set the entity ID in Data Mapper to the entity of the PoPriceList. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Name= 'Google price lists'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Name": "Google price lists"
               }
             




### Example - Update an Allocation record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Allocation` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Description": "Google updated"
              }
             

  5. Set the entity ID in Data Mapper to the entity of the Allocation. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Allocationid= 'ExpenseSwap'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Allocationid": "ExpenseSwap"
              }
             




### Example - Update a SavingsAccount record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SavingsAccount` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Phone": "(800) 555‑0100"
              }
             

  5. Set the entity ID in Data Mapper to the entity of the SavingsAccount. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Allocationid= 'ExpenseSwap'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
               "Bankaccountid": "SBB"
               }
             




### Example - Update a Podocument record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Podocument` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
               "Message": "updated"
               }
             

  5. Set the entity ID in Data Mapper to the entity of the Podocument. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `docid= 'Blanket PO-PO0041'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
         
               }
             




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

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
