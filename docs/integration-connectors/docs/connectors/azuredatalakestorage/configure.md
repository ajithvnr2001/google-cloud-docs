---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/azuredatalakestorage/configure/
title: Azure Data Lake Storage \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:57.034848+00:00
---

# Azure Data Lake Storage  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/azuredatalakestorage/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Azure Data Lake Storage

The Azure Data Lake Storage connector lets you connect to Azure Data Lake Storage and use SQL to retrieve and update the Azure Data Lake Storage data.

## Before you begin

Before using the Azure Data Lake Storage connector, do the following tasks:

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

  * For information about how to create an Azure storage account, see [Create a storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal). For information about creating a container in Azure, see [Create a container](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-explorer#create-a-container). For information about creating a directory in Azure, see [Create a directory](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-explorer#create-a-directory).



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
     1. **Connector** : Select **Azure Data Lake Storage** from the drop down list of available Connectors.
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
     8. **Account** : This property specifies the name of the Azure Data Lake Storage account. 
     9. **Directory** : This property specifies the root path to list files and folders. 
     10. **File System** : This property specifies the name of the FileSystem which will be used in a Gen 2 storage account. For Example, the name of your Azure blob container. 
     11. **Chunk Size** : The size of chunks (in Mb) to use when uploading large files. 
     12. **Include Sub Directories** : Choose if the sub directories paths should be listed in the Resources view in the ADLSGen2 Schema. 
     13. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     14. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Azure Data Lake Storage connection:

        * Shared Access Signature
        * Account Access Key
        * JWT Authentication

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **Shared Access Signature**
    * **Shared Access Signature** : Secret Manager Secret containing the Shared Access Signature.


  * **Account Access Key**
    * **Account Access Key** : Secret Manager Secret containing the Account Access Key.
  * **JWT Authentication**
    * **Client ID** : The client ID used for requesting access tokens.
    * **Private Key** : Secret Manager Secret containing the contents of the private key file in PEM format. The private key must match the public key/certificate.
    * **Private Key Password** : Secret Manager Secret containing the password (paraphrase) of the private key file.



### Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Azure Data Lake Storage connection.

#### Shared Access Signature connection type

Fieldname  | Details  
---|---  
Location | us-central1  
Connector | azuredatalakestorage  
Connector version | 1  
Connection Name | adls-gen2-conn-public  
Enable Cloud Logging | Yes  
Service Account | account@my-project.iam.gserviceaccount.com  
Account | google-cloud-dslgen3  
Directory | directory  
File System | container  
Include Sub Directories | No  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Shared Access Signature | SHARED_ACCESS_SIGNATURE  
Secret Version | 1  
  
#### Account access key connection type

Fieldname  | Details  
---|---  
Location | us-central1  
Connector | azuredatalakestorage   
Connector version | 1  
Connection Name | azure-data-lake-conn  
Enable Cloud Logging | Yes  
Service Account | account@my-project.iam.gserviceaccount.com  
Account | google-cloud-dslgen3  
Directory | north-america  
File System | container  
Include Sub Directories | No  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Account Access key | ACCOUNT_ACCESS_KEY  
Secret Version | 1  
  
#### JWT authentication connection type

Fieldname | Details  
---|---  
Location | us-central1  
Connector | azuredatalakestorage  
Connector version | 1  
Connection Name | adls-gen2-jwt-conn  
Enable Cloud Logging | Yes  
Service Account | account@my-project.iam.gserviceaccount.com  
Account | your-adls-account-name  
Directory | north-america  
File System | data-lake-container  
Include Sub Directories | Yes  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication type | JWT Authentication  
Client ID | CLIENT_ID  
Private Key | PRIVATE_KEY_SECRET  
Private Key Password | PRIVATE_KEY_PASSWORD_SECRET  
Secret Version (for Private Key) | 1  
Secret Version (for Private Key Password) | 1  
  
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

The Azure Data Lake Storage connector can process 5 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### DownloadFile action

This action lets you download the contents of a particular blob from a directory or a container.

#### Input parameters of the DownloadFile action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Path | String | Yes | The path of the file (including the file name) to download. For example: 

  * FILE_NAME
  * `dir1/FILE_NAME`
  * `dir1/dir2/FILE_NAME`

  
HasBytes | Boolean | No | Whether to download content as bytes (Base64 format). 

  * To download non-text files such as `.pdf`, `.xls`, and `.docx`, you must set HasBytes to `true`.
  * To download a text file, you can set HasBytes to `true` or `false`. If you set the value to `true`, the text content is downloaed as bytes (Base64 format).

The default value of this parameter is `false`.   
  
#### Output parameters of the DownloadFile action

If the action is successful, it returns the contents of the file or the blob.

For example on how to configure the `DownloadFile` action, see Action examples.

### CreateFile action

This action lets your create a blob or a file in a container or a directory.

#### Input parameters of the CreateFile action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Path | String | Yes | The path of the file which will be created.  
  
For example on how to configure the `CreateFile` action, see Action examples.

### CopyFile action

This action lets you copy the contents of a file or a blob to another file or blob in the same container or directory.

#### Input parameters of the CopyFile action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
SourcePath | String | Yes | The path of the file which will be copied.  
DestinationPath | String | Yes | The path of the file where it will be copied.  
  
For example on how to configure the `CopyFile` action, see Action examples.

### DeleteObject action

This action lets you delete a file or a blob.

#### Input parameters of the DeleteObject action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Recursive | String | No | Set this to `true` to delete all the folder's content including any sub-folders.  
Path | String | Yes | The path of the file or folder to be deleted.  
DeleteType | String | Yes | 

  * Set this to FILESANDFOLDERS to delete the file or folder specified in the Path parameter.
  * Set this to FILES to delete only the files inside the folder specified in the Path parameter.

  
  
For example on how to configure the `DeleteObject` action, see Action examples.

### LeaseBlob action

This action lets you create and manage a lock on a blob.

#### Input parameters of the LeaseBlob action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Path | String | Yes | The path of the file.  
LeaseAction | String | Yes | Specifies the lease action to execute.  
LeaseDuration | Integer | Yes | Specifies the duration of the lease.  
  
For example on how to configure the `LeaseBlob` action, see Action examples.

### UploadFile Action

This action let users upload the contents to a particular blob or container.

#### Input parameters of the UploadFile action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Path | String | Yes | The path of the file to be uploaded.  
HasBytes | Boolean | No | Whether to upload content as bytes.  
Content | String | Yes | Content to upload.  
  
For example on how to configure the `UploadFile` action, see Action examples.

### RenameObject Action

This action lets you rename a file or a folder.

#### Input parameters of the RenameObject action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Path | String | Yes | The path which will be renamed.  
RenameTo | String | Yes | The new name of the file or the folder.  
  
For example on how to configure the `RenameObject` action, see Action examples.

## Action examples

### Example - Download a file

This example downloads a binary file.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Path": "testdirectory1/test1.pdf",
         "HasBytes": true
         }

If the action is successful, the `DownloadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "ContentBytes": "UEsDBBQABgAIAAAAIQCj77sdZQEAAFIFAAATAAgCW0NvbnRlbnRfVHlwZXNdLnhtbCCiBAIooA"
    }]




### Example - Upload a file

This example uploads content as a blob.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Path": "testblob4",
         "HasBytes": true,
         "Content": "abcdef\nabcdef"
         }

If the action is successful, the `UploadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Create a file

This example creates a file in the specified directory.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "path": "testdirectory1/testblob"
         }

If the action is successful, the `CreateFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Copy a file

This example copies a file from one location to another location.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CopyFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "SourcePath": "testdirectory1/testblob",
         "DestinationPath": "testblob"
         }

If the action is successful, the `CopyFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Delete a blob

This example deletes the specified blob.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "path": "testdirectory1/testblob"
         }

If the action is successful, the `DeleteObject` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Lease a blob

This example leases the specified blob.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `LeaseBlob` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Path": "testblob2",
         "LeaseAction": "Acquire",
         "LeaseDuration": 60.0
         }

If the action is successful, the `LeaseBlob` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "LeaseId": "7aae9ca2-f015-41b6-9bdf-5fd3401fc493",
    "Success": "true"
    }]




### Example - Rename a blob

This example renames a blob.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RenameObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Path": "testblob",
         "RenameTo": "testblob6"
         }

If the action is successful, the `RenameObject` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the records

This example lists all the records in the `Resource` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Resource` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



### Example - Get a record

This example gets a record with the specified ID from the `Resource` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Resource` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `testdirectory1/testblob1` in the **Default Value** field. 

Here, `testdirectory1/testblob1` is a unique record ID in the `Resource` entity.




## Use the Azure Data Lake Storage connection in an integration

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
