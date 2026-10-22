---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/overview/
title: Google Drive connector \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:11.126396+00:00
---

# Google Drive connector  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Google Drive connector

The Google Drive connector lets you create and configure a [Google Drive](https://developers.google.com/drive) connection in Integration Connectors. You can use this connection in your business applications to securely exchange data and perform operations with Google Drive. 

For the list of supported entities and operations, see Supported entities and operations. For information about the supported connector-specific actions, see Supported actions. 

All connections in Integration Connectors provide a layer of abstraction for the underlying service objects. These objects are exposed as manageable [entities](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action), allowing you to perform standard [operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) or use connector-specific [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action). 

## Google Drive connector versions

The Google Drive connector supports two versions:

  * **Google Drive v1** : use this connector version to access the Google Drive v3 API.
  * **Google Drive v2** : use this connector version to access the Google Drive v2 API.



For information about creating a Google Drive connection, see [Create and configure a Google Drive connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/configure). 

## Supported entities and operations

The Google Drive connector supports the following entities and operations: 

Entity | Description | Operations  
---|---|---  
`File` | Represents a file in Google Drive. | `Get`, `List`, `Create`, `Update`, `Delete`  
`Folder` | Represents a folder in Google Drive. | `Get`, `List`, `Create`, `Update`, `Delete`  
`Permission` | Represents a permission for a file or folder in Google Drive. | `Get`, `List`, `Create`, `Update`, `Delete`  
`Drive` | Represents a drive in Google Drive. | `Get`, `List`, `Create`, `Update`, `Delete`  
  
For Application Integration usecase examples, see [Use case examples in Application Integration](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/configure#entityexamples-exp). 

## Supported actions

The Google Drive connector supports the following actions: 

CopyResource
    **Description** : creates a copy of a specified resource in Google Drive. You can define a new name for the copied file and specify its destination folder by providing a list of parent folder IDs . 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Id` | String | Yes | The ID of the resource to be copied.  
`NewName` | String | Yes | The new name of the copied file.  
`ParentIDs` | String | No | A comma-separated list of parent folder IDs in which the copied file will be placed. If not specified, the file will be copied to the same folder where the file was located.   
`IgnoreDefaultVisibility` | Boolean | No | Determines whether to bypass the default visibility settings for the newly created file. If the domain is configured to make all uploaded files visible by default, setting this parameter to true overrides that behavior for this specific request. The default value is false.  
`IncludeLabels` | String | No | A comma-separated list of IDs of labels to include in the labelInfo part of the response.  
`IncludePermissionsForView` | String | Yes | This field specifies which additional view permissions to include in the response. The supported value is published.  
`KeepRevisionForever` | Boolean | No | Indicates whether to keep the revisions of the file forever. This feature applies only to files with binary content in Google Drive. A maximum of 200 revisions can be kept forever per file. If the limit is reached, you must delete existing revisions to add new ones. The default value is false.  
`OCRLanguage` | String | No | This field provides a language hint for OCR (Optical Character Recognition) when importing image files. Specify the language using an ISO 639-1 two-letter language code, such as, `en` for English, `de` for German.  
`SupportsAllDrives` | Boolean | Yes | This parameter indicates whether to track the changes in My Drives and shared drives.  
Set this parameter to true to enable access to shared drives. The default value is false.  
  
#### Output parameters

Parameter name | Data type | Description  
---|---|---  
`CopiedFileID` | String | The ID of the copied file.  
`Success` | String | This parameter indicates whether the operation was successful or not.  
  
#### Usecase example

The following example shows how to configure the `CopyResource` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `CopyResource` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "Id": "10QIXnPK3DjiLnVL1QvpIsuHPo16zVkYQuJsTVvt_B-c", "NewName": "Copied of Untitles Document.txt1750848165952", "ParentIDs": "1uaAUsRZLLF07KypCDNUBvHn3Xx2lxmo5"}
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         [{"CopiedFileID": "15NUzJGarp-b8TdT0tXBGD9hJMnYjZbiydaE4lbZV0EU", "Success": "TRUE"}]
               




* * *

CreateFolder
    **Description** : creates a new folder within your Google Drive. You must provide a name for the new folder and specify its location by providing the IDs of its parent folders. You can also add an optional description and mark the folder as starred. 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Name` | String | Yes | The title for the folder.  
`Description` | String | No | The description for the folder.  
`Starred` | Boolean | No | This parameter indicates whether the folder is starred. The default value is false.  
`ParentIds` | String | Yes | A comma-separated list of IDs of the parent folders in which the new folder will be created.  
  
#### Output parameters

Parameter name | Data type | Description  
---|---|---  
`Success` | String | This parameter indicates whether the operation was successful or not.  
`Id` | String | The ID of the new folder.  
  
#### Usecase example

The following example shows how to configure the `CreateFolder` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `CreateFolder` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "Name": "Test Folder", "ParentIds": "1uaAUsRZLLF07KypCDNUBvHn3Xx2lxmo5"}
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         [{"Success": "TRUE", "Id": "10QIXnPK3DjiLnVL1QvpIsuHPo16zVkYQuJsTVvt_B-c"}]
               




* * *

DeleteResource
    **Description** : permanently removes a file or folder from Google Drive. To use this action, you need to provide the unique ID of the resource you wish to delete. 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Id` | String | Yes | The ID of the resource to be deleted.  
  
#### Output parameters

Parameter name | Data type | Description  
---|---|---  
`Success` | String | This parameter indicates whether the operation was successful or not.  
  
#### Usecase example

The following example shows how to configure the `DeleteResource` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `DeleteResource` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "Id": "10QIXnPK3DjiLnVL1QvpIsuHPo16zVkYQuJsTVvt_B-c"}
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         [{"Success": "TRUE"}]
               




* * *

DownloadFile
    **Description** : downloads a file from Google Drive 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Id` | String | Yes | The ID of the file to be downloaded.  
`LocalFile` | String | No | The file path and file name where the file will be saved, leave empty to store the file in memory instead.   
`Encoding` | String | No | The encoding type for the file data. If LocalFile is empty, the file data will be returned in the specified encoding. The allowed values are NONE, and BASE64. The default value is BASE64.  
`Overwrite` | Boolean | No | This parameter determines whether to overwrite the file if it already exists when downloading.  
The default value is false, set the parameter to TRUE to overwrite the file.  
`FileFormat` | String | No | The format in which the file can be downloaded, maximum size of the file can be 10MB. Leave this parameter blank to download in its original format. The supported formats are DOCX, ODT, RTF, HTML, TXT, and PDF.   
  
#### Output parameters

Parameter name | Data type | Description  
---|---|---  
`FileData` | String | If LocalFile is not provided, the file data will be returned using the specified Encoding.  
`Success` | String | This parameter indicates whether the operation was successful or not.  
  
#### Usecase example

The following example shows how to configure the `DownloadFile` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `DownloadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "Id": "10QIXnPK3DjiLnVL1QvpIsuHPo16zVkYQuJsTVvt_B-c", "LocalFile": "gs://test-bucket/test-file.txt", "Encoding": "NONE", "Overwrite": true, "FileFormat": "HTML"}
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         [{"FileData": "This is a test file.", "Success": "TRUE"}]
               




* * *

MoveResource
    **Description** : moves a file or folder to a different location within Google Drive. You need to provide the ID of the resource to be moved and the IDs of the new parent folders. 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Id` | String | Yes | The ID of the resource to be moved.  
`ParentIDs` | String | Yes | A comma-separated list of IDs to be used as parent folders.   
A resource within a shared drive must have exactly one parent folder, and only users with the 'file organizer' or 'organizer' role can move files and folders within a shared drive.  
  
#### Output parameters

Parameter name | Data type | Description  
---|---|---  
`Success` | String | This parameter indicates whether the operation was successful or not.  
  
#### Usecase example

The following example shows how to configure the `MoveResource` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `MoveResource` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "Id": "10QIXnPK3DjiLnVL1QvpIsuHPo16zVkYQuJsTVvt_B-c", "ParentIDs": "1uaAUsRZLLF07KypCDNUBvHn3Xx2lxmo5"}
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         [{"Success": "TRUE"}]
               




* * *

UpdateResource
    **Description** : updates the metadata of a file or folder in Google Drive. You can modify its name, description, MIME type, and whether it's starred. 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Id` | String | Yes | The ID of the resource to be updated.  
`Name` | String | Yes | The new name of the updated file.  
`Description` | String | No | A description of the file or folder.  
`MIMEType` | String | No | The MIME type of the file.  
`Starred` | String | No | This parameter indiactes whether the resource is starred. The default value is false.  
  
#### Output parameters

Parameter name | Data type | Description  
---|---|---  
`Success` | String | This parameter indicates whether the operation was successful or not.  
  
#### Usecase example

The following example shows how to configure the `UpdateResource` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `UpdateResource` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "Id": "10QIXnPK3DjiLnVL1QvpIsuHPo16zVkYQuJsTVvt_B-c", "Name": "New Name", "Description": "New Description", "MIMEType": "application/vnd.google-apps.document", "Starred": true}
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         [{"Success": "TRUE"}]
               




* * *

UploadFile
    **Description** : uploads a file to Google Drive. You must provide the file data and its MIME type. You can also specify the parent folder where the file will be placed and a filename for the uploaded file. 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Id` | String | Yes | The ID of the file to be uploaded.  
`FileData` | String | Yes | The file data to be uploaded.  
`MIMEType` | String | Yes | The MIME type of the file.  
`ParentIDs` | String | No | A comma-separated list of parent folder IDs in which the uploaded file will be placed. If not specified, the file will be uploaded to the root folder of the user's My Drive.  
`Filename` | String | No | The name of the file to be uploaded.  
  
#### Output parameters

Parameter name | Data type | Description  
---|---|---  
`Success` | String | This parameter indicates whether the operation was successful or not.  
  
#### Usecase example

The following example shows how to configure the `UploadFile` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `UploadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "Id": "10QIXnPK3DjiLnVL1QvpIsuHPo16zVkYQuJsTVvt_B-c", "FileData": "This is a test file.", "MIMEType": "text/plain", "ParentIDs": "1uaAUsRZLLF07KypCDNUBvHn3Xx2lxmo5", "Filename": "test-file.txt"}
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         [{"Success": "TRUE"}]
               




* * *

SubscribeToFileChanges
    **Description** : subscribes to notifications for changes to a specific file in Google Drive. 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Id` | String | Yes | The ID of the file to be subscribed to.  
`Token` | String | Yes | The token to be used for subscribing to file changes.  
  
#### Output parameters

Parameter name | Data type | Description  
---|---|---  
`Success` | String | This parameter indicates whether the operation was successful or not.  
  
#### Usecase example

The following example shows how to configure the `SubscribeToFileChanges` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `SubscribeToFileChanges` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
                   "FileId": "1o-SMcimUT91sfLNf6NoESirH9BsVqvym0YORLo2GAoY",
                   "Id": "Id11752060129918",
                   "Address": "https://cloudsearch.googleapis.net/notifications",
                   "ChannelToken": "token"
                 }
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following: 
         
         [
                   {
                     "Kind": "api#channel",
                     "Id": "Id11752060129918",
                     "ResourceId": "BfrGPBKDiD1SH1dg6Ng73nLTfl0",
                     "ResourceUri": "https://www.googleapis.com/drive/v3/files/1o-SMcimUT91sfLNf6NoESirH9BsVqvym0YORLo2GAoY?alt=json&supportsAllDrives=true",
                     "Token": "token",
                     "Expiration": "1752063731000"
                   }
                 ]
               




* * *

SubscribeToUserChanges
    **Description** : subscribes to notifications for changes made by a specific user in Google Drive. 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Id` | String | Yes | The ID of the user to be subscribed to.  
`Token` | String | Yes | The token to be used for subscribing to user changes.  
  
#### Usecase example

The following example shows how to configure the `SubscribeToUserChanges` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `SubscribeToUserChanges` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
                   "Id": "11752060129918",
                   "Address": "https://cloudsearch.googleapis.net/notifications",
                   "ChannelToken": "token"
                 }
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following: 
         
         [
                   {
                     "Kind": "api#channel",
                     "Id": "Id11752060129918",
                     "ResourceId": "BfrGPBKDiD1SH1dg6Ng73nLTfl0",
                     "ResourceUri": "https://www.googleapis.com/drive/v3/users/me?alt=json&supportsAllDrives=true",
                     "Token": "token",
                     "Expiration": "1752063731000"
                   }
                 ]
               




* * *

StopWatchingResources
    **Description** : unsubscribes you from receiving notifications for a previously watched resource. 

#### Input parameters

Parameter name | Data type | Required | Description  
---|---|---|---  
`Id` | String | Yes | The ID of the resource to be stopped watching.  
`Token` | String | Yes | The token to be used for stopping watching resources.  
  
#### Usecase example

The following example shows how to configure the `StopWatchingResources` action in Application Integration:

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the `StopWatchingResources` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
                   "Id": "Id11752060129918",
                   "Token": "token"
                 }
               

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following: 
         
         [
                   {
                     "Kind": "api#channel",
                     "Id": "stopid1751971586168",
                     "ResourceId": "CXPNGzAnYjqSazkd9-nNTFHTkwo",
                     "ResourceUri": "https://www.googleapis.com/drive/v3/files/11OsOCgkV5hsRai6UwpkLngvqnCcrA4sy1tqfPi_VJio?alt=json&supportsAllDrives=true",
                     "Token": null,
                     "Expiration": "1751975186000"
                   }
                 ]
         




## System limitations

The Google Drive connector can process a maximum of 2QPS transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## What's next

  * Learn how to [create and configure a Google Drive connection](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/configure).
  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
