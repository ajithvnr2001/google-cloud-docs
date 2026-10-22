---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/hdfs/configure/
title: HDFS \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:25.059092+00:00
---

# HDFS  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/hdfs/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HDFS

The HDFS connector lets you perform insert, delete, update, and read actions on the HDFS data.

## Supported versions

This connector supports HDFS Hadoop version 3.4.0.

## Before you begin

Before using the HDFS connector, do the following tasks:

  * In your Google Cloud project: 
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

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **HDFS** from the drop down list of available Connectors.
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
     7. **Path** : Specify the HDFS path to use as the working directory.
     8. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     9. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     10. Click **NEXT**.
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

The following authentication types are supported by the HDFS connection:

     * Username and Password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and Password**
    * **Username** : Enter the username to use for the HDFS connection.
    * **Password** : Enter the secret manager secret containing the password associated with the username.
    * **Secret Version** : Select the secret version for the secret selected above.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### Username and password connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | HDFS  
Connector version | 1  
Connection Name | hdfs-v24-new  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 2  
Destination Type | Host Address  
Host | 10.128.0.  
port1 | 10000  
Username | user1  
Password | PASSWORD  
Secret Version | 1  
  
## System limitations

The HDFS connector can process a maximum of 20 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the HDFS connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Actions

This section shows how to perform some of the [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### MakeDirectory action

This action creates a directory in the specified path.

#### Input parameters of the MakeDirectory action

Parameter name | Data type | Required | Description  
---|---|---|---  
Permission | String | False | The permissions to create a new directory.  
Path | String | True | The path of the new directory.  
  
For an example about how to configure the `MakeDirectory` action, see Examples.

### ListStatus action

This action lists the contents of the supplied path.

#### Input parameters of the ListStatus action

Parameter name | Data type | Required | Description  
---|---|---|---  
Path | String | True | The path of the file.  
  
For an example about how to configure the `ListStatus` action, see Examples.

### GetHomeDirectory action

This action gets the home directory of the current user.

#### Input parameters of the GetHomeDirectory action

Parameter name | Data type | Required | Description  
---|---|---|---  
connectorInputPayload | Json | True | The connector's input payload.  
  
For an example about how to configure the `GetHomeDirectory` action, see Examples.

### DeleteFile action

This action deletes a file or a directory.

#### Input parameters of the DeleteFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
Path | String | True | The path of the file.  
Recursive | Boolean | False | Specifies whether to delete the subfolders of a folder.  
  
For an example about how to configure the `DeleteFile` action, see Examples.

### GetContentSummary action

This action gets the content summary of a file or a folder.

#### Input parameters of the GetContentSummary action

Parameter name | Data type | Required | Description  
---|---|---|---  
Path | String | True | The path of the file or folder.  
  
For an example about how to configure the `GetContentSummary` action, see Examples.

### RenameFile action

This action renames a file or a directory.

#### Input parameters of the RenameFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
path | String | True | The path of the file.  
destination | String | True | Specifies the new name and path of the file.  
  
For an example about how to configure the `RenameFile` action, see Examples.

### SetPermission action

This action sets the permission of a path.

#### Input parameters of the SetPermission action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Path | String | True | The path of the file.  
Permission | String | True | Specifies the unix permissions in an octal (base-8) notation.  
  
For an example about how to configure the `SetPermission` action, see Examples.

### SetPermission action

This action sets permission of a path.

#### Input parameters of the SetPermission action

Parameter name | Data type | Required | Description  
---|---|---|---  
Path | String | True | The path of the file.  
Permission | String | True | Specifies the Unix permissions in an octal (base-8) notation.  
  
For an example about how to configure the `SetPermission` action, see Examples.

### SetOwner action

This action sets an owner and group of a path.

#### Input parameters of the SetOwner action

Parameter name | Data type | Required | Description  
---|---|---|---  
Path | String | True | The path of the file.  
Owner | String  | True | The new owner of the path.  
group | String | False | The name of the new group.  
  
For an example about how to configure the `SetOwner` action, see Examples.

### UploadFile action

This action uploads a file.

#### Input parameters of the UploadFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
path | String | True | The path of the file.  
Content | String  | True | The content of the uploaded file.  
  
For an example about how to configure the `UploadFile` action, see Examples.

### DownloadFile action

This action downloads a file.

#### Input parameters of the DownloadFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
path | String | True | The path of the file.  
WriteToFile | String  | False | The local location of file to which the output is written.  
  
For an example about how to configure the `DownloadFile` action, see Examples.

### AppendToFile action

This action appends a file.

#### Input parameters of the AppendToFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
path | String | True | The path of the file.  
Content | String  | True | The content to append to the file.  
  
For an example about how to configure the `AppendToFile` action, see Examples.

### GetFileChecksum action

This actions gets the checksum of a file.

#### Input parameters of the GetFileChecksum action

Parameter name | Data type | Required | Description  
---|---|---|---  
path | String | True | The path of the file.  
  
For an example about how to configure the `GetFileChecksum` action, see Examples.

## Action examples

This section shows how to perform some of the action examples in this connector.

### Example - Make a directory

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MakeDirectory` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path": "/user/hduser"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": true
    }]
    




### Example - Get the home directory

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetHomeDirectory` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {}
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Path": "/user/hduser"
    }]
    




### Example - Delete a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteFile` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path": "/user/hduser/testFile"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": true
    }]
    




### Example - List status of a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ListStatus` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "path": "/user/hduser/deletefile"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "fileId": 16471.0,
      "PathSuffix": "data.txt",
      "owner": "hduser",
      "group": "supergroup",
      "length": 38.0,
      "permission": "644",
      "replication": 1.0,
      "storagePolicy": 0.0,
      "childrenNum": 0.0,
      "blockSize": 1.34217728E8,
      "modificationTime": "2024-08-16 16:12:01.921",
      "accessTime": "2024-08-16 16:12:01.888",
      "type": "FILE"
    }, {
      "fileId": 16469.0,
      "PathSuffix": "file2.txt",
      "owner": "hduser",
      "group": "supergroup",
      "length": 53.0,
      "permission": "644",
      "replication": 1.0,
      "storagePolicy": 0.0,
      "childrenNum": 0.0,
      "blockSize": 1.34217728E8,
      "modificationTime": "2024-08-16 16:12:01.762",
      "accessTime": "2024-08-16 16:12:01.447",
      "type": "FILE"
    }]
    




### Example - Get content summary of a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetContentSummary` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path": "/user/hduser/appendtofile"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "DirectoryCount": "1",
      "FileCount": "1",
      "Length": 52.0,
      "Quota": -1.0,
      "SpaceConsumed": 52.0,
      "SpaceQuota": -1.0,
      "ecpolicy": "",
      "snapshotdirectorycount": "0",
      "snapshotfilecount": "0",
      "snapshotlength": "0",
      "snapshotspaceconsumed": "0"
    }]
    




### Example - Rename a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `hdfs_RenameFile_action` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path": "/user/hduser/renamefile_second/file1.txt",
           "Destination": "/user/hduser/renamefile_second/file1rename"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": true
    }]
    




### Example - Set permission of a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SetPermission` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path": "/user/hduser/gcpdirectory",
           "Permission": "777"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": true
    }]
    




### Example - Set the owner of a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SetOwner` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path": "/user/hduser/gcpdirectory",
           "Owner": "newowner"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": true
    }]
    




### Example - Upload a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadFile` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         { "Path": "/user/newfile9087.txt", "Content": "string" }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": true
    }]
    




### Example - Download a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadFile` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         { "Path": "/user/sampleFile/file1.txt" }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Output": "This is sample File\nfor this testing\ncontent" } ]
    




### Example - Append a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AppendToFile ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         { "Path": "/user/sampleFile/file1.txt", "Content": "content" }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Success": true } ]
    




### Example - Get checksum of a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetFileChecksum ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         { "Path": "/user/sampleFile/file1.txt" }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Algorithm": "MD5-of-0MD5-of-512CRC32C", "Bytes": "00000200000000000000000080f5b53ae8c165ae56e86109b8bb2a1700000000", "Length": 28 } ]
    




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List data of all the files

This example fetches the data of all the files in the `Files` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Object` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - Get data of a permission

This example gets the data of the permission with the specified ID from the `Permission` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Permission` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `/user/hduser/appendfile` in the **Default Value** field. 

Here, `/user/hduser/appendfile` is a unique ID in the `Permission` entity.




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
