---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/smartsheet/configure/
title: Smartsheet \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:21.598048+00:00
---

# Smartsheet  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/smartsheet/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Smartsheet

The Smartsheet connector lets you perform insert, delete, update, and read operations on Smartsheet data.

## Supported versions

This connector supports the Smartsheet version 25.2.0.246.

## Before you begin

Before using the Smartsheet connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




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
     1. **Connector** : Select **Smartsheet** from the drop down list of available Connectors.
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
     7. **Header** : Optionally, specify this field to detect column names from the first row.
     8. **Hide Formatting Characters** : Optionally, specify this field to hide currency symbols and percentage signs in numeric values. This will also convert these columns from varchar to double.
     9. **Ignore Rows Not Found** : Optionally, if this field is not selected and any of the specified Row IDs are not found, no rows will be deleted, and a 'not found' error will be returned.
     10. **Report Compatibility Level** : Optionally, specify the compatibility level for the returned data.
     11. **Use Full File Paths As Table Names** : Optionally, specify this field to include the full file path in the name of an exposed table or view, corresponding to a sheet or report.
     12. **Value Source** : Optionally, indicates whether the cell will use the Value fields as its value or the DisplayValue field.
     13. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     14. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     15. Click **NEXT**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Smartsheet connection:

        * OAuth2.0 - Authorization Code
        * Personal Access Token
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

     2. Click **NEXT**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### OAuth 2.0 authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | smartsheet  
Connector version | 1  
Connection Name | smartsheet-oauth-connection  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Client ID | CLIENT_ID  
Scopes | ADMIN_SHEETS, ADMIN_SIGHTS, ADMIN_USERS, ADMIN_WEBHOOKS, ADMIN_WORKSPACES, CREATE_SHEETS, CREATE_SIGHTS, DELETE_SHEETS, DELETE_SIGHTS, READ_CONTACTS, READ_EVENTS, READ_SHEETS, READ_SIGHTS, READ_USERS, SHARE_SHEETS, SHARE_SIGHTS, WRITE_SHEETS  
Client secret | CLIENT_SECRET  
Secret version | 1  
Authorization URL | https://app.smartsheet.com/b/authorize  
  
### Personal access token authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | smartsheet  
Connector version | 1  
Connection Name | smartsheet-accesstoken-connection  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Personal Access Token | PERSONAL_ACCESS_TOKEN  
Secret version | 3  
  
You can create a Smartsheet account using the link [Smartsheet Login](https://www.smartsheet.com/).

To know more about Smartsheet API, refer to [Smartsheet API Reference](https://developers.smartsheet.com/api/smartsheet/introduction).

## System limitations

The Smartsheet connector can process a maximum of 10 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Smartsheet connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Actions

This section shows how to perform some of the [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### DownloadAttachment action

This action downloads an attachment from a sheet.

#### Input parameters of the DownloadAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
SheetId | String | True | The unique identifier of the sheet.  
AttachmentID | String | True | The unique identifier of the attachment.  
  
For an example on how to configure the `DownloadAttachment` action, see Examples.

### DeleteAttachment action

This action deletes a specified attachment from a sheet.

#### Input parameters of the DeleteAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
SheetId | String | True | The unique identifier of the sheet.  
AttachmentID | String | True | The unique identifier of the attachment.  
  
For example on how to configure the `DeleteAttachment` action, see Examples.

### CopyRowsToAnotherSheet action

This action copies rows from one sheet to another sheet.

#### Input parameters of the CopyRowsToAnotherSheet action

Parameter name | Data type | Required | Description  
---|---|---|---  
SheetId | String | True | The unique identifier of the sheet from which the rows will be copied.  
RowIds | String | True | A comma-separated list of row IDs to copy from the sheet.  
DestinationSheetId | String | True | The unique identifier of the destination sheet to which the rows will be copied.  
  
For example on how to configure the `CopyRowsToAnotherSheet` action, see Examples.

### CopySheet action

This action copies a sheet to a folder, home directory, or workspace.

#### Input parameters of the CopySheet action

Parameter name | Data type | Required | Description  
---|---|---|---  
SheetId | String | True | The unique identifier of the sheet to be copied.  
DestinationType | String | True | The destination type to which the sheet will be copied. The accepted values are folder, home, or workspace.  
DestinationId | String | True | The unique identifier of the destination to which the sheet will be copied. This field is required when the DestinationType is folder or workspace, and must be null when it is home.  
NewName | String | True | The desired name of the copied sheet.  
Include | String | False | A comma-separated list of additional sheet elements to include in the copy operation. The accepted values are attachments, cellLinks, data, discussions, filters, forms, ruleRecipients, rules, and shares.  
  
For example on how to configure the `CopySheet` action, see Examples.

### MoveRowsToAnotherSheet action

This action moves rows from one sheet to another sheet.

#### Input parameters of the MoveRowsToAnotherSheet action

Parameter name | Data type | Required | Description  
---|---|---|---  
SheetId | String | True | The unique identifier of the sheet from which the rows will be moved.  
RowIds | String | True | A comma-separated list of the row IDs to move from the sheet.  
DestinationSheetId | String | True | The unique identifier of the destination sheet to which the rows will be moved.  
  
For example on how to configure the `MoveRowsToAnotherSheet` action, see Examples.

### MoveSheet action

This action moves a sheet to a folder, home directory, or workspace.

#### Input parameters of the MoveSheet action

Parameter name | Data type | Required | Description  
---|---|---|---  
SheetId | String | True | The unique identifier of the sheet to be moved.  
DestinationType | String | True | The destination type where the sheet will be moved. The accepted values are folder, home, or workspace.  
DestinationId | String | True | The unique identifier of the destination to which the sheet will be moved. This field is required when the DestinationType is folder or workspace, and must be null when it is home.  
  
For example on how to configure the `MoveSheet` action, see Examples.

## Action examples

This section shows how to perform some of the action examples in this connector.

### Example - Download an attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "SheetId": "5141926996037508",
           "AttachmentID": "1667587811610500"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "Success": "true",
        "URL": "https://s3.amazonaws.com/SmartsheetB1/37540b4438a6466a973d678484c1fac8?response-content-disposition=attachment%3Bfilename%3D%22TestGOOGLE3.txt%22%3Bfilename*%3DUTF-8%27%27TestGOOGLE3.txt&Signature=rVHv4loce%2BrL4lYPlteTgAmkB%2Bk%3D&Expires=1744826533&AWSAccessKeyId=11950YFEZZJFSSKKB3G2",
        "Content": "VGhpcyBpcyBhIHRlc3QgYXR0YWNobWVudC4="
      }
    ]
    




### Example - Delete an attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select `DeleteAttachment` action, and then click **Done**.
  3. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "SheetId": "5141926996037508",
           "AttachmentID": "1667587811610500"
         }
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    [
      {
        "Success": "true",
      }
    ]
    




### Example - Copy rows to another sheet

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select `CopyRowsToAnotherSheet` action, and then click **Done**.
  3. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "SheetId": "7483321975000964",
           "RowIds": "7935781927128964",
           "DestinationSheetId": "7197099985686404"
         }
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    [
      {
      "Success": "true",
    	"AffectedRows":"1"
      }
    ]
    




### Example - Copy a sheet

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select `CopySheet` action, and then click **Done**.
  3. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "SheetId": "5141926996037508",
           "DestinationType": "workspace",
           "DestinationId": "4219254305253252",
           "NewName": "Copied sheet appears",
           "Include": "comments"
         }
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    [
      {
        "Success": "true",
      }
    ]
    




### Example - Move rows to another sheet

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select `MoveRowsToAnotherSheet` action, and then click **Done**.
  3. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "SheetId": "7483321975000964",
           "RowIds": "7935781927128964",
           "DestinationSheetId": "7197099985686404"
         }
         

Running this example returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    [
      {
      "Success": "true",
    	"AffectedRows":"1"
      }
    ]
    




### Example - Move a sheet

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select `MoveSheet` action, and then click **Done**.
  3. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "SheetId": "5141926996037508",
           "DestinationType": "workspace",
           "DestinationId": "4219254305253252"
         }
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    [
      {
        "Success": "true",
      }
    ]
    




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the columns of a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Info_Columns` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement.

You must use single quotes (') to enclose the value for a filter clause. You can use the filterClause to filter records based on the columns.




### Example - Get column details of a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Info_Columns` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entityId to "849633317179268" which is the key to be passed. To set the entityId, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"849633317179268"` in the **Input Value** field and choose the entityId as local variable. 

The value for entityId should be passed directly, such as "849633317179268". Here, "849633317179268" is the unique primary key value, which must be passed

In some cases, passing entityId may throw an error because of two composite keys. In such cases, you can use the filterClause and pass the value, such as id='849633317179268'.




### Example - Delete a row from a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Team_Task_List_by_Priority` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entityId to "849633317179268" which is the key to be passed. To set the entityId, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"849633317179268"` in the **Input Value** field and choose the entityId as local variable. 

If the entity has two composite business or primary keys instead of specifying the **entityId** , you can also set the **filterClause** to `id='849633317179268'`.




### Example - Create an attachment to a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Info_Attachments` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {
           "SheetId": "5141926996037508",
           "RowId": "8196592918597508",
           "Name": "Random.txt",
           "ContentEncoded": "VGhpcyBpcyBhIHRlc3QgYXR0YWNobWVudC4="
         }
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {"Id": "7144235189178244" }
         




### Example - Create a project in a row with fixed deadlines using a Gantt-style layout

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Gantt_Project_with_Hard_Deadline` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "Created from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {"RowId": "7860088629366660"}
         




### Example - Create a team task in a row of a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Team_Task_List_by_Priority` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "Created from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {"RowId": "7860088629366660"}
         




### Example - Create a sales activity in a row of a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Sales_Activity_Tracking_by_Rep_Month` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "Created from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {"RowId": "7860088629366660"}
         




### Example - Create a sales opportunity in a row of a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Simple_Sales_Pipeline` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "Created from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {"RowId": "7860088629366660" }
         




### Example - Create a sales report in a row of a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Report_Sales_Activity_And_Team_Objectives` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "Created from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {"RowId": "7860088629366660" }
         




### Example - Create an order in a row of a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Customer_Order_Tracking_History` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "Created from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {"RowId": "7860088629366660" }
         




### Example - Create a new column in a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Info_Columns` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {
           "SheetId": "3315287605596036",
           "Title": "newexposedcolumn",
           "Index": 2,
           "Type": "DATE"
         }
         

Running this example returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "550917885349764"
         }
         




### Example - Create a new folder in a workspace

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Info_Folders` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {
           "ParentFolderId": "8716915511191428",
           "Name": "sub-folder-p2"
         }
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "550917885349764"
         }
         




### Example - Create a new workspace in an account

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Info_Workspaces` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {
           "Name": "new workspace (newly exposed)"
         }
         

Running this example returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "550917885349764"
         }
         




### Example - Create a new user in an account

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Info_Users` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {
           "FirstName": "charlie",
           "Email": "charlie@altostrat.com",
           "LastName": "c",
           "Admin": true,
           "LicensedSheetCreator": true
         }
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "550917885349764"
         }
         




### Example - Update project details in a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Gantt_Project_with_Hard_Deadline` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the **entityId** in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `849633317179268` in the given field.
  5. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "updated from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    {
      "RowId": null
    }
    




### Example - Update a team task in a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Team_Task_List_by_Priority` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the **entityId** in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `849633317179268` in the given field.
  5. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "updated from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    {
      "RowId": null
    }
    




### Example - Update a sales activity in a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Sales_Activity_Tracking_by_Rep_Month` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the **entityId** in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `849633317179268` in the given field.
  5. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "updated from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    {
      "RowId": null
    }
    




### Example - Update a sales opportunity in a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Simple_Sales_Pipeline` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the **entityId** in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `849633317179268` in the given field.
  5. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "updated from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    {
      "RowId": null
    }
    




### Example - Update a sales report in a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Report_Sales_Activity_And_Team_Objectives` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the **entityId** in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `849633317179268` in the given field.
  5. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "updated from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    {
      "RowId": null
    }
    




### Example - Update an order in a sheet

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sheet_Customer_Order_Tracking_History` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the **entityId** in the **Data mapper** section of the **Tasks** , click **entityId** and then enter `849633317179268` in the given field. 
  5. In the **Data mapper** section of the **Task** click `Open Data Mapping` editor and then enter a value similar to the following in the `Input Value` field: 
         
         {"Task Name": "updated from googlecloud"}
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    {
      "RowId": null
    }
    




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
