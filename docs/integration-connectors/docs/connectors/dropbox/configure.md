---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/dropbox/configure/
title: Dropbox \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:35.494421+00:00
---

# Dropbox  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/dropbox/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Dropbox

The Dropbox connector lets you connect to a Dropbox instance and perform the supported operations.

## Before you begin

Before using the Dropbox connector, do the following tasks:

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

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Dropbox** from the drop down list of available Connectors.
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
     7. **Impersonate User Id** :Optionally to Specify the User Id to impersonate. 
     8. **Impersonate User Mode** :Optionally to Specify the type of the user impersonation. It should be whether the User mode or the Admin mode. 
     9. **Include Sub Directories** :Optionally If you want to include sub directories while listing files and folders. 
     10. **Include Team Resources** :Optionally If you want to include team files and folders. 
     11. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     12. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the dropbox connection:

        * OAuth 2.0 Auth Code Grant 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 Auth Code Grant**
    * **Client ID** : The client ID used for requesting access tokens.
    * **Scopes** : A comma-separated list of desired scopes from dropbox permissions Portal.
    * **Client secret** : The client secret used for requesting access tokens.



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

The Dropbox connector can process 18 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### CopyResource action

This action lets you copy a file or folder to a different location in the user's Dropbox.

#### Input parameters of the CopyResource action

Parameter name | Data type | Required | Description  
---|---|---|---  
From_Path | String | Yes | Path in the user's Dropbox to be copied or moved.  
To_Path | String | Yes | Destination path in the user's Dropbox for the copied resource.  
Autorename | String | No | If there's a conflict, have the Dropbox server try to auto rename the file to avoid the conflict. The default for this field is False.  
Allow_Ownership_Transfer | String | No | Allow moves by owner even if it would result in an ownership transfer for the content being moved. This does not apply to copies. The default for this field is False.  
ObjectPathsAggregate | String | No | An aggregate representing the object path. Can also be the name of a #TEMP table.  
  
For example on how to configure the `CopyResource` action, see Action examples.

### CreateFolder action

This action lets you create a folder at a given path.

#### Input parameters of the CreateFolder action

Parameter name | Data type | Required | Description  
---|---|---|---  
Path | String | Yes | Path in the user's Dropbox to create.   
AutoRename | Boolean | No | If there's a conflict, have the Dropbox server try to autorename the folder to avoid the conflict. The default value is false.  
ForceAsync | Boolean | No | Whether to force the create to happen asynchronously. Only available when using ObjectPathsAggregate. The default value is false.  
ObjectPathsAggregate | String | No | A JSON aggregate representing the paths. Can also be the name of a #TEMP table.  
  
For example on how to configure the `CreateFolder` action, see Action examples.

### DeleteResource action

This action lets you delete the file or folder at a given path. If the path is a folder, all its contents will be deleted too.

#### Input parameters of the DeleteResource action

Parameter name | Data type | Required | Description  
---|---|---|---  
Path | String | Yes | A unique identifier for the file or folder.  
ObjectPathsAggregate | String | No | An aggregate representing the object path. Can also be the name of a #TEMP table.  
  
For example on how to configure the `DeleteResource` action, see Action examples.

### MoveResource action

Move a file or folder to a different location in the user's Dropbox. If the source path is a folder all its contents will be moved. Note that we do not currently support case-only renaming.

#### Input parameters of the MoveResource action

Parameter name | Data type | Required | Description  
---|---|---|---  
From_Path | String | Yes | Path in the user's Dropbox to be copied or moved.  
To_Path | String | Yes | Path in the user's Dropbox that is the destination.  
Autorename | String | No | If there's a conflict, have the Dropbox server try to auto rename the file to avoid the conflict. The default for this field is False.  
Allow_Ownership_Transfer | String | No | Allow moves by owner even if it would result in an ownership transfer for the content being moved. This does not apply to copies. The default for this field is False.  
ObjectPathsAggregate | String | No | An aggregate representing the object path. Can also be the name of a #TEMP table.  
  
For example on how to configure the `MoveResource` action, see Action examples.

### RenameResource action

This action lets you rename a resource by providing a path and new name.

#### Input parameters of the RenameResource action

Parameter name | Data type | Required | Description  
---|---|---|---  
Path | String | Yes | The path to resource to be renamed. EX: /myFolder/sample.txt  
NewName | String | Yes | The new name for the resource. EX: sampleDocument.txt  
  
For example on how to configure the `RenameResource` action, see Action examples.

### UnshareFolder action

This action lets you Unshares a folder. Requires the sharing.write scope.

#### Input parameters of the UnshareFolder action

Parameter name | Data type | Required | Description  
---|---|---|---  
FolderId | String | Yes | The id of the shared folder to unshare.  
LeaveCopy | String | No | If true, members of this shared folder will get a copy of this folder after it's unshared. The default value is false.  
  
For example on how to configure the `UnshareFolder` action, see Action examples.

### DownloadFile action

This action lets you Downloads a File. Requires the files.content.read scope.

#### Input parameters of the DownloadFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
Id | String | Yes | The ID of the document to download.  
Revision | String | No | The revision of the document to download, for example 'rev:a1c10ce0dd78'.  
Path | String | No | The path of the file or folder to download.  
AsZip | Boolean | No | Download a folder in a zip format. Must be set to true to download a folder.  
FileStream | String | No | An instance of an output stream where file data is written to. Only used if DownloadTo is not set.  
DownloadTo | String | No | The folder path to download the file to.  
FileType | String | Yes | The type of file(file or paper)  
  
For example on how to configure the `DownloadFile` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Copy a resource

The following example shows how to copy a resource with specified path to a different path:

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CopyResource` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "From_Path": "/DropboxFolder/pptxFile.pptx",
           "To_Path": "/DropBoxFolder2/Folder/pptFile.pptx"
         }

If the action is successful, the `CopyResource` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Success": "true", "metadata_.tag": "file", 
      "metadata_name": "pptxFile.pptx", 
      "metadata_path_lower": "/testingdropboxupdated/abcde/pptxfile.pptx", 
      "metadata_path_display": "/TestingDropBoxUpdated/abcde/pptxFile.pptx", 
      "metadata_parent_shared_folder_id": "3204685267", "metadata_id": "id:8-07A6kHAoIAAAAAAAAC1w",
      "metadata_client_modified": "2024-06-13T11:06:37Z", "metadata_server_modified": "2024-07-12T10:19:02Z",
      "metadata_rev": "61d0a3560ecb5bf039dd3", "metadata_size": "17052", 
      "metadata_sharing_info_read_only": "false", "metadata_sharing_info_parent_shared_folder_id": "3204685267",
      "metadata_sharing_info_modified_by": "dbid:AACVLctlrEo-ouTSxUVSTi0loZCSZKc933A", 
      "metadata_is_downloadable": "true", 
      "metadata_content_hash": "0234f7d4eaf914cb276716c8b2a24e24655d1f6f39ee549207e33a4255e2fba2" } ]




### Example - Create a folder

The following example shows how to create a folder at a given path:

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateFolder` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Path": "/TestDrobBoxFolder/newFolder"
         }

If the action is successful, the `CreateFolder` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Id": "id:8-07A6kHAoIAAAAAAAAC2Q" } ]




### Example - Delete a resource

The following example shows how to delete a resource:

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteResource` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Path": "/TestingDropBox/FolderToBeDeletedName"
         }

If the action is successful, the `DeleteResource` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Move a resource

The following example shows how to move a resource:

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MoveResource` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "From_Path": "/TestDropBoxFolder/Folder1/dummypdf2.pdf",
           "To_Path": "/EmptyFolder/Folder1/dummypdf2.pdf"
         }

If the action is successful, the `MoveResource` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Status": "Success"
      }]




### Example - Rename a resource

The following example shows how to rename a resource:

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RenameResource` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Path": "/TestDropBox/abcd",
           "NewName": "abcded"
         }

If the action is successful, the `RenameResource` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Unshare a folder 

The following example shows how to unshare a folder:

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UnshareFolder` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "FolderId": "3336772979"
         }

If the action is successful, the `UnshareFolder` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Download a file

The following example shows how to download a file:

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Id": "id:8-07A6kHAoIAAAAAAAABcg",
           "FileType": "file"
         }

If the action is successful, the `DownloadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Success": "true", "Name": "license.txt", 
      "Id": "id:8-07A6kHAoIAAAAAAAABcg", "ClientModified": "2024-07-09T09:52:41Z", 
      "ServerModified": "2024-07-09T09:52:41Z", "Revision": "61ccd7da2b987c0f52053", "Size": "11", 
      "LowerCasePath": "/sahil kapoor/testingdropboxupdated/uploadfolderwithnestedfolder/nestedfolder2/license.txt",
       "DisplayPath": "/Sahil Kapoor/TestingDropBoxUpdated/uploadFolderWithNestedFolder/NestedFolder2/license.txt",
        "PreviewURL": null, "IsDownloadable": "true", "HasExplicitSharedMembers": null, 
      "ContentHash": "f6dc724d119649460e47ce719139e521e082be8a9755c5bece181de046ee65fe", "Owner": null,
      "Title": null, "MimeType": null, "FileData": "SGVsbG8gd29ybGQ=", "parent_shared_folder_id": "3237290067",
      "sharing_info_read_only": "false", "sharing_info_parent_shared_folder_id": "3237290067", 
      "sharing_info_modified_by": "dbid:AACVLctlrEo-ouTSxUVSTi0loZCSZKc933A" } ]




## Use the Dropbox connection in an integration

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
