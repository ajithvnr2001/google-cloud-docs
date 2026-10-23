---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/marketo/configure/
title: Marketo \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:49.346681+00:00
---

# Marketo  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/marketo/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Marketo

The Marketo connector lets you perform insert, delete, update, and read operations on Marketo data.

## Before you begin

Before using the Marketo connector, do the following tasks:

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
     1. **Connector** : Select **Marketo** from the drop down list of available Connectors.
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
     7. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     8. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : You can specify the destination details either as a host address or a service attachment. Select any of the following destination types: 
        * **Host address** : If you want to specify the hostname or IP address of the destination.
        * **Service attachment** : If you want to specify the private endpoint for your internal IP addresses. The service attachment, lets you hide your internal IP addresses from the external network. You can create a service attachment in Google Cloud, by using the Private Service Connect feature. For information on configuring a Private Service Connect, see [Publish managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

Based on your selection of destination type, enter the host address or the service attachment name.

To enter additional destinations, click **+Add destination**.

     2. Click **Next**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Marketo connection:

        * OAuth 2.0 Client Credentials 
        * Username and password 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  7. **Review** : Review your connection and authentication details.
  8. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 Client Credentials**
    * **Client ID** : The client id provided by connector for the app you created.
    * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.


  * **Username and password**
    * **UserId** : The Marketo SOAP API User Id.
    * **EncryptionKey** : Secret Manager Secret containing the Marketo SOAP API Encryption Key.



## System limitations

The Marketo connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Marketo connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).



## Actions

This section lists the [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### AddLandingPageContentSection action

Adds a content section to the target landing page.

#### Input parameters of the AddLandingPageContentSection action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
LandingPageId | String | True | Id of the landing page  
ContentId | String | True | Id of the content section. Also the HTML id of the section.  
Type | String | True | Type of content section. The allowed values are Image, Form, Rectangle, Snippet, RichText, HTML.  
  
For example on how to configure the `AddLandingPageContentSection` action, see Action examples.

### DeleteLandingPageContentSection action

Deletes the section of the landing page content in Marketo.

#### Input parameters of the DeleteLandingPageContentSection action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
LandingPageId | String | True | Id of the landing page.  
ContentId | String | True | Id of the content section. Also the HTML id of the section.  
  
For example on how to configure the `DeleteLandingPageContentSection` action, see Action examples.

### UpdateEmailContent action

Updates the content of an email.

#### Input parameters of the UpdateEmailContent action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
EmailId | String | True | The Id of the email.  
FromEmail | String | True | From-address of the Email  
FromName | String | True | From-name of the Email  
ReplyTo | String | True | Reply-To address of the Email  
Subject | String | True | Subject Line of the Email  
  
For example on how to configure the `UpdateEmailContent` action, see Action examples.

### UpdateLandingPageContentSection action

Add or update the section of the landing page content in Marketo.

#### Input parameters of the UpdateLandingPageContentSection action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Type | String | True | Type of content section.The allowed values are Image, Form, Rectangle, Snippet, RichText, HTML.  
Value | String | True | Type of content section.  
LandingPageId | String | True | Id of the landing page.  
ContentId | String | True | Id of the content section. Also the HTML id of the section.  
  
For example on how to configure the `UpdateLandingPageContentSection` action, see Action examples.

### GetImportProgramMembersStatus action

Gets the status of an import program members from file operation for Marketo.

#### Input parameters of the GetImportProgramMembersStatus action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
BatchId | String | True | The Id of the import leads batch.  
  
For example on how to configure the `GetImportProgramMembersStatus` action, see Action examples.

### ScheduleCampaign action

Remotely schedules a batch campaign to run at a given time.

#### Input parameters of the ScheduleCampaign action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
CampaignId | String | True | Id of the batch campaign to schedule.  
RunAt | String | True | Datetime to run the campaign at. If unset, the campaign will be run five minutes after the call is made.  
  
For example on how to configure the `ScheduleCampaign` action, see Action examples.

### ListMembersOfList action

Determines whether leads are contained within a list in Marketo.

#### Input parameters of the ListMembersOfList action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ListId | String | True | The Id of the list to check for leads.  
LeadId | String | True | A comma-separated list of lead Ids to be checked if they are in the list specified by ListId.  
  
For example on how to configure the `ListMembersOfList` action, see Action examples.

### AssociateLead action

Associates a known Marketo lead record to a munchkin cookie and its associated web activity history

#### Input parameters of the AssociateLead action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
LeadId | String | True | Id of the Lead to associate.  
Cookie | String | True | The cookie value to associate  
  
For example on how to configure the `AssociateLead` action, see Action examples.

### MergeLeads action

Merges two or more known lead records into a single lead record.

#### Input parameters of the MergeLeads action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
WinningLeadId | String | True | The id of the winning lead record   
LoosingLeadId | String | True | A comma separated list of loosing lead ids  
  
For example on how to configure the `MergeLeads` action, see Action examples.

### GetImportLeadsStatus action

Gets the status of an import leads from file operation for Marketo.

#### Input parameters of the GetImportLeadsStatus action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
BatchId | String | True | The Id of the import leads batch.  
  
For example on how to configure the `GetImportLeadsStatus` action, see Action examples.

### CancelExportJob action

Cancels an export job. 

#### Input parameters of the CancelExportJob action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
JobId | String | True | The id of the export job.   
Type | String | True | The object type of the BulkExtract. Available values are : Activities, Leads, ProgramMembers The allowed values are Activities, Leads, ProgramMembers.  
  
For example on how to configure the `CancelExportJob` action, see Action examples.

### EnqueueExportJob action

Places an export job in queue and starts the job when computing resources become available. 

#### Input parameters of the EnqueueExportJob action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
JobId | String | True | The id of the export job.   
Type | String | True | The object type of the BulkExtract. Available values are : Activities, Leads, ProgramMembers. The allowed values are Activities, Leads, ProgramMembers.  
  
For example on how to configure the `EnqueueExportJob` action, see Action examples.

### GetExportJobStatus action

Returns the status of an export job. Job status is available for 30 days after Completed or Failed status was reached. 

#### Input parameters of the GetExportJobStatus action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
JobId | String | True | The id of the export job.   
Type | String | True | The object type of the BulkExtract. Available values are : Activities, Leads, ProgramMembers. The allowed values are Activities, Leads, ProgramMembers.  
  
For example on how to configure the `GetExportJobStatus` action, see Action examples.

### CreateEmailTemplate action

Creates a new email template.

#### Input parameters of the CreateEmailTemplate action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
FolderId | String | True | The Id of the folder  
FolderType | String | True | The type of the folder.  
Name | String | True | The name of the Email Template. Must be unique under the parent folder.  
File | String | True | Multipart File. HTML content for template.  
  
For example on how to configure the `CreateEmailTemplate` action, see Action examples.

### UpdateLeadProgramStatus action

Changes the program status of a list of leads in a target program. Only existing members of the program may have their status changed with this API.

#### Input parameters of the UpdateLeadProgramStatus action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ProgramId | String | True | Id of the batch campaign to schedule.  
LeadIds | String | True | A comma separated list of lead ids for input.  
Status | String | True | Program status of the record.  
  
For example on how to configure the `UpdateLeadProgramStatus` action, see Action examples.

### RemoveLeadsFromList action

Removes leads from a list in Marketo.

#### Input parameters of the RemoveLeadsFromList action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ListId | String | True | The Id of the list to remove leads from.   
LeadId | String | True | A comma-separated list of lead Ids to be removed from the list specified by ListId.  
  
For example on how to configure the `RemoveLeadsFromList` action, see Action examples.

### ImportCustomObjectsFromFile action

Imports custom objects from a file into Marketo.

#### Input parameters of the ImportCustomObjectsFromFile action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
File | String | True | The path to the file containing custom objects to be imported into Marketo, i.e. 'C:\temp\custom_object_import.csv'.   
TableName | String | True | The name of the custom object table. Ex: CustomObject_test   
Format | String | True | The format of the file that will be used to import custom objects into Marketo. The allowed values are csv, tsv, ssv.  
Content | String | True | The content as InputStream to be uploading when File is not specified.   
  
For example on how to configure the `ImportCustomObjectsFromFile` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - AddLandingPageContentSection

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddLandingPageContentSection ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "LandingPageId": "1005",
           "ContentId": "1120",
           "Type": "HTML"
         }

This example shows the specific Object records. If the action is successful, the `CampaignTest` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "Id": "1130",
      "json:repeatelementorder": "id",
      "requestsuccess": "true",
      "@affectedrows": "1"
    }]




### Example - DeleteLandingPageContentSection

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteLandingPageContentSection` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "LandingPageId": "1005",
           "ContentId": "1009"
         } 

This example shows the specific Object records. If the action is successful, the `DeleteLandingPageContentSection ` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "Id": "1005",
      "json:repeatelementorder": "id",
      "requestsuccess": "true",
      "@affectedrows": "1"
    }]




### Example - UpdateEmailContent

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateEmailContent ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "EmailId": "1001",
           "FromName": "test",
           "FromEmail": "222larabrown@gmail.com",
           "Subject": "TestSubject Line",
           "ReplyTo": "222larabrown@gmail.com"
         }

This example shows the specific Object records. If the action is successful, the `UpdateEmailContent` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "Id": "1001",
      "json:repeatelementorder": "id",
      "requestsuccess": "true"
    }]




### Example - UpdateLandingPageContentSection

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateLandingPageContentSection ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Type": "HTML",
           "Value": "
         Test Update
         ",
           "LandingPageId": "1005",
           "ContentId": "1120"
         }

This example shows the specific Object records. If the action is successful, the `UpdateLandingPageContentSection ` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "Id": "1005",
      "json:repeatelementorder": "id",
      "requestsuccess": "true",
      "@affectedrows": "1"
    }]




### Example - GetImportProgramMembersStatus

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetImportProgramMembersStatus ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "BatchId": "1029"
         } 

This example shows the specific Object records. If the action is successful, the `GetImportProgramMembersStatus` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "BatchId": "1029",
      "Status": "Complete",
      "NumOfLeadsProcessed": "3",
      "NumOfRowsFailed": "0",
      "NumOfRowsWithWarning": "3",
      "Message": "Import succeeded, 3 records imported (3 members), 3 warning.",
      "importid": "1029",
      "requestsuccess": "true"
    }]




### Example - ScheduleCampaign

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ScheduleCampaign ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "CampaignId": "1065",
           "RunAt": "2024-05-23T18:05:00+0000"
         } 

This example shows the specific Object records. If the action is successful, the `ScheduleCampaign` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "Success": "true",
      "id": "1065",
      "json:repeatelementorder": "id",
      "requestsuccess": "true"
    }]




### Example - ListMembersOfList

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ListMembersOfList ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "ListId": "1003",
           "LeadId": "13,25,21"
         } 

This example shows the specific Object records. If the action is successful, the `ListMembersOfList` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "LeadId": "13",
      "Status": "notmemberof",
      "ReasonCode": null,
      "ReasonMessage": null,
      "id": "13",
      "requestsuccess": "true"
    }, {
      "LeadId": "25",
      "Status": "notmemberof",
      "ReasonCode": null,
      "ReasonMessage": null,
      "id": "25",
      "requestsuccess": "true"
    }, {
      "LeadId": "21",
      "Status": "notmemberof",
      "ReasonCode": null,
      "ReasonMessage": null,
      "id": "21",
      "requestsuccess": "true"
    }]




### Example - AssociateLead

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AssociateLead ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "LeadId": 582.0,
           "Cookie": "id:703-VQQ-088%26token:_mch-marketo.com-_mch-mktoweb.com-1717156982039-98850"
         }

This example shows the specific Object records. If the action is successful, the `AssociateLead` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "Status": "Success"
    }] 




### Example - MergeLeads

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MergeLeads ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "LoosingLeadId": "10",
           "WinningLeadId": "45"
         } 

This example shows the specific Object records. If the action is successful, the `MergeLeads` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
      [{
      "Status": "Success"
    }] 




### Example - GetImportLeadsStatus

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetImportLeadsStatus ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "BatchId": "1022"
         }

This example shows the specific Object records. If the action is successful, the `GetImportLeadsStatus` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "BatchId": "1022",
      "Status": "Complete",
      "NumOfLeadsProcessed": "3",
      "NumOfRowsFailed": "0",
      "NumOfRowsWithWarning": "0",
      "Message": "Import succeeded, 3 records imported (3 members)",
      "importid": "1022",
      "requestsuccess": "true"
    }]




### Example - Cancel an export job

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CancelExportJob ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "JobId": "ddf64e6f-0e9c-4254-91a9-32277349a22b",
           "Type": "Leads"
         }

This example shows the specific Object records. If the action is successful, the `CancelExportJob` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "JobId": "ddf64e6f-0e9c-4254-91a9-32277349a22b",
      "JobStatus": "Cancelled",
      "Format": "CSV",
      "CreatedAt": "2024-05-28T05:45:13Z",
      "StartedAt": null,
      "QueuedAt": null,
      "exportid": null,
      "json:repeatelementorder": null,
      "status": null,
      "requestsuccess": null
    }]




### Example - EnqueueExportJob

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `EnqueueExportJob ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "JobId": "d04f60fb-5e68-40b5-9928-76fdb9034303",
           "Type": "Leads"
         }

This example shows the specific Object records. If the action is successful, the `EnqueueExportJob` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "JobId": "d04f60fb-5e68-40b5-9928-76fdb9034303",
      "JobStatus": "Queued",
      "Format": "CSV",
      "CreatedAt": "2024-05-27T12:12:53Z",
      "QueuedAt": "2024-05-27T12:13:20Z",
      "exportid": null,
      "json:repeatelementorder": null,
      "status": null,
      "requestsuccess": null
    }]




### Example - GetExportJobStatus

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetExportJobStatus ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "JobId": "358a974e-7bbb-475e-a71e-72ce4c01ffa4",
           "Type": "Leads"
         }

This example shows the specific Object records. If the action is successful, the `GetExportJobStatus` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "JobId": "358a974e-7bbb-475e-a71e-72ce4c01ffa4",
      "Format": "CSV",
      "CreatedAt": "2024-05-23T10:12:09Z",
      "JobStatus": "Created",
      "QueuedAt": null,
      "StartedAt": null,
      "FinishedAt": null,
      "NumberOfRecords": null,
      "FileSize": null,
      "exportid": null,
      "status": null,
      "requestsuccess": null
    }]




### Example - CreateEmailTemplate

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateEmailTemplate ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "FolderId": 27.0,
           "FolderType": "Folder",
           "Content": "\n\n\n \n
         My First Heading
         \n
         My first paragraph.
         
         \n \n\n",
           "Name": "Test1718166502676",
           "Filename": "FileName1718166502678"
         }

This example shows the specific Object records. If the action is successful, the `CreateEmailTemplate` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "Id": "1048",
      "createdat": "2024-06-12T04:28:23Z+0000",
      "folder_type": "Folder",
      "workspace": "Default",
      "folder_foldername": "Templates",
      "name": "Test1718166502676",
      "version": "2",
      "requestsuccess": "true",
      "url": "https://app-abc.marketo.com/#ET1048B2ZN27",
      "folder_value": "27",
      "updatedat": "2024-06-12T04:28:23Z+0000",
      "status": "draft"
    }]




### Example - UpdateLeadProgramStatus 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateLeadProgramStatus ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "ProgramId": "1002",
           "Status": "Member",
           "LeadIds": "3"
         }

This example shows the specific Object records. If the action is successful, the `UpdateLeadProgramStatus` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "Success": "true",
      "id": "3",
      "status": "updated",
      "requestsuccess": "true"
    }]




### Example - RemoveLeadsFromList

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveLeadsFromList ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "ListId": "1026",
           "LeadId": "57"
         }

This example shows the specific Object records. If the action is successful, the `RemoveLeadsFromList` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "LeadId": "57",
      "Status": "skipped",
      "ReasonCode": "1015",
      "ReasonMessage": "Lead not in list",
      "id": "57",
      "requestsuccess": "true"
    }]




### Example - ImportCustomObjectsFromFile

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ImportCustomObjectsFromFile ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "JobId": "358a974e-7bbb-475e-a71e-72ce4c01ffa4",
           "Type": "Leads"
         }

This example shows the specific Object records. If the action is successful, the `ImportCustomObjectsFromFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "JobId": "358a974e-7bbb-475e-a71e-72ce4c01ffa4",
      "Format": "CSV",
      "CreatedAt": "2024-05-23T10:12:09Z",
      "JobStatus": "Created",
      "QueuedAt": null,
      "StartedAt": null,
      "FinishedAt": null,
      "NumberOfRecords": null,
      "FileSize": null,
      "exportid": null,
      "status": null,
      "requestsuccess": null
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

When you use a list operation and expect the data volume to be high, we recommend that you specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter) for the following entities: `LeadsLists`, `LeadPrograms`, `Activities`, `LandingPageContentSec`, `LeadChanges`, `LeadChangesFields`, `Emails`, `LandingPages`, `Forms`, `Programs`, `Leads`, `LandingPageTemplateCon`, `OpportunityRoles`, `SalesPersons`, `Tokens`, `ListStaticMemberShip`, `Opportunities`, `LeadChangesAttributes`, and `Segments`. Also, to sort the result set, you must first apply the filter clause.

### Example - List all Emails

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Emails from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - Get single SmartCampaigns

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select SmartCampaigns from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to Get single SmartCampaigns. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `1002` in the **Input Value** field and choose the EntityId as Local variable.



### Example - Delete Emails

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Emails from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to Delete Emails. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `1048.0` in the **Input Value** field and choose the EntityId as Local variable. 



### Example - Create Emails

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Emails from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
         "Template": 1.0,
         "FolderId": 1002.0,
         "Name": "Test Email",
         "FolderType": "Program"
         }
         
         
         Running this example, returns a response similar to the following in the Connector
         task's connectorOutputPayload output variable:
         
         
         
         
         {
         "Id": "1048.0"
         }




### Example - Update EmailTemplates

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select EmailTemplates from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the EntityID to Update a EmailTemplates. To set the EntityID, in the **Data mapper** section of the **Tasks** , click **EntityID** and then enter `1034.0` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         
         {
         "Name": "temp email updated",
         "Description": "updation"
         }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
    "Id": 1034.0
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
