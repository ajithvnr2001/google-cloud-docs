---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/sftp/configure/
title: SFTP \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:05.078876+00:00
---

# SFTP  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/sftp/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SFTP

The SFTP connector lets you connect to a SFTP server and perform file transfer operations.

## Before you begin

In your Google Cloud project, do the following tasks:

  * Ensure that network connectivity is set up. For information, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant `roles/secretmanager.viewer` and `roles/secretmanager.secretAccessor` IAM roles to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. 
  * Enable `secretmanager.googleapis.com` (Secret Manager API) and `connectors.googleapis.com` (Connectors API). For more information, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). 



## Create a SFTP connection

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, select a location from the **Region** list and then click **Next**. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

  4. In the **Connection Details** section, complete the following: 
     1. In the **Connector** field, select **SFTP**.
     2. In the **Connector version** field, select the desired version.
     3. In the **Connection Name** field, enter a name for the connection instance. The connection name can contain lower-case letters, numbers, or hyphens. The name must begin with a letter and end with a letter or number and the name must not exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. In the **Service Account** field, select an account that has the required roles.
     7. (Optional) Configure the **Connection node settings**.
        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. (Optional) In the **Remote Path** field, enter the folder path in the SFTP server to perform the entity operations, such as `List`, `Create`, `Update`, or `Delete`.

If you are accessing entities (files or folders) in the root folder, or the immediate child folders of the root folder, you need not set any value to this field. However, if you want to access nested entities that are present at a depth of 2 levels or more from the root folder, you must set the value of this field to the base path of the folder that has the entities you want to access. For example, if you want to access the `/folder_A/folder_B/folder_C/test.png` file, you must set the Remote Path to `/folder_A/folder_B/folder_C`. 

     9. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     10. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to and click **Next**.

In the **Destination Type** field, select the desired type:

     * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
     * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

  6. In the **Authentication** section, select an **Authentication type** and enter the relevant details and click **Next**. 

The following authentication types are supported by the SFTP connection:

     * Username and password
     * SSH_PUBLIC_KEY

To understand how to configure these authentication types, see Configure authentication.

  7. Review your connection and authentication details, and then click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : The SFTP username to use for the connection.
    * **Password** : Secret Manager Secret containing the password associated with the SFTP username.


  * **SSH_PUBLIC_KEY**
    * **Username** : The SFTP user account used to authenticate.
    * **SSH Private Key** : Private Key for SSH authentication.
    * **SSH Private Key password** : Passphrase/password protecting the private key, if any.
    * **SSH Private Key type** : Format of the Private Key.



## Use the SFTP connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



### Actions

This section lists some of the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

#### Upload action

The following table describes the input parameters of the `Upload` action.

Parameter name | Data type | Required | Description  
---|---|---|---  
Content | String | No | Content to upload as a file.  
ContentBytes | String | No | Bytes content (as a Base64 string) to upload as a file. Use this to upload binary data.  
HasBytes | Boolean | No | Specifies if the content is uploaded as bytes. The default value is `false`.  
RemoteFile | String | Yes | The filename on the remote host.  
Overwrite | Boolean | No | Specifies if the remote file is overwritten. The default value is `false`.  
  
For examples on how to configure the `Upload` action, see Examples.

#### Download action

The following table describes the input parameters of the `Download` action.

Parameter name | Data type | Required | Description  
---|---|---|---  
RemoteFile | String | Yes |  The filename on the remote host. You can use the `*` wildcard character, but other wildcard characters aren't supported. For more information, see Download multiple files.   
HasBytes | Boolean | No | Specifies if the content should be downloaded as bytes. The default value is `false`.  
  
For examples on how to configure the `Download` action, see Examples.

#### MoveFile action

The following table describes the input parameters of the `MoveFile` action.

Parameter name | Data type | Required | Description  
---|---|---|---  
RemoteFile | String | Yes | The path of the remote file to be moved.  
DestinationPath | String | Yes | The new path you want to move the file to.  
  
For examples on how to configure the `MoveFile` action, see Examples.

#### RenameFile action

The following table describes the input parameters of the `RenameFile` action.

Parameter name | Data type | Required | Description  
---|---|---|---  
RemoteFile | String | Yes | Remote file path and name to be renamed.  
NewFileName | String | Yes | New name of the remote file.  
  
For examples on how to configure the `RenameFile` action, see Examples.

### Examples

This section describes how to perform some of the entity operations and actions in this connector. The examples describe the following operations: 

  * List all files in the root directory
  * List files that match a pattern in a directory
  * Move a file
  * Rename a file
  * Delete a file
  * Upload an ASCII text file
  * Upload a binary file
  * Download an ASCII text file
  * Download a binary file
  * Download multiple files



The following table lists the sample scenarios and the corresponding configuration in the Connectors task:

Task | Sample command | Configuration  
---|---|---  
List all files in the root directory | `ls /` | 

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select the `Root` entity and then select the `List` operation.
  3. Click **Done**.

  
List `.csv` files in a directory | `ls /tmp/*.csv` | 

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select the base directory (/tmp) from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Set the filter clause. To set the clause, in the **Task Input** section of the **Connectors** task, click **filterClause** and then enter `FilePath LIKE '/tmp/%.csv'` in the **Default Value** field.

**Note:**

  * The value for the file pattern in the filter clause must be enclosed within single quotes (').
  * The `Entity` list displays only the base level directories. Hence, you can list the files present only in the base level directories. Listing of files in the child directories is not supported. 
  * The `FilePath` field is defined in the input payload's JSON schema. For the list of all the available fields, see JSON schema for payload.
  * You can dynamically set the filter clause by using the Data Mapping task in your integration.

  
Move a file  | `mv /tmp/dir_A/hello_world.txt /dir_B/dir_C/` | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MoveFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RemoteFile": "/tmp/dir_A/hello_world.txt",
         "DestinationPath": "/dir_B/dir_C/"
         }


This example moves the `/tmp/dir_A/hello_world.txt` file to the `/dir_B/dir_C/` directory. Running this example, returns a response smiliar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    
    [{
    "Success":"true"
    }]  
  
Rename a file  | `mv /tmp/hello_world.txt /tmp/hello_world_new.txt` | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RenameFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RemoteFile": "/tmp/hello_world.txt",
         "NewFilename": "hello_world_new.txt"
         }


This example renames the `hello_world.txt` file to `hello_world_new.txt`. Running this example, returns a response smiliar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    
    [{
    "Success":"true"
    }]  
  
Delete a file | `rm /tmp/myfile.csv` | 

  1. In the `Configure connector task` dialog, click `Entities`.
  2. From the `Entity` list, select the base directory that has the file to be moved.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to the file's full path. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **entityId** and then enter `/tmp/myfile.csv` in the **Default Value** field. Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to `FilePath LIKE '/tmp/myfile.csv'`.

  
Upload an ASCII text file | `put file_1.txt /tmp/file_1.txt` | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `Upload` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
           "Content": "This is a sample text!\r\n",
           "RemoteFile": "/tmp/file_1.txt",
           "Overwrite": true
         }

This sample creates the `file_1.txt` file that has the content `This is a sample text!` in the SFTP server's `/tmp` directory. And any existing file with the same name is overwritten because the `Overwrite` attribute value is `true`.  Setting the `Overwrite` attribute is optional; by default, the value is `false`.  
**Note:** You can't upload a local file directly to the SFTP server. You must specify the file's entire content in the `Content` attribute.   
Upload a binary file | `put image_1.png /tmp/image_1.png` | To upload a binary content, you must first encode the content in the Base64 format. You can choose a tool of your choice to encode the content. Steps for encoding the content are out of the scope of this document. After you have the content as a Base64 string, perform the following steps: 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `Upload` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
           "ContentBytes": "SGVsbG8gd29ybGQ=",
           "RemoteFile": "/tmp/image_1.png",
           "Overwrite": true,
           "HasBytes": true
         }

This sample creates the `image_1.png` file with the content as specified in the `ContentBytes` field. The file is created in the SFTP server's `/tmp` directory. And any existing file with the same name is overwritten because the `Overwrite` attribute value is `true`.  Setting the `Overwrite` attribute is optional; by default the value is `false`.  
  
Download an ASCII text file | `get /tmp/myfile.txt` | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `Download` action, and then click **Done**.
  3. In the **Task Output** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "RemoteFile": "/tmp/myfile.txt"
         }


The content of the downloaded file is available as a string in the `Content` field of the Connector task's `connectorOutputPayload` response parameter.   
Download a binary file | `get /tmp/myfile.png` | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `Download` action, and then click **Done**.
  3. In the **Task Output** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "RemoteFile": "/tmp/myfile.png",
         "HasBytes" : true
         }


The content of the downloaded file is available as a Base64 encoded string in the `ContentBytes` field of the Connector task's `connectorOutputPayload` response parameter.   
Download multiple files | `` | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `Download` action, and then click **Done**.
  3. In the **Task Output** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "RemoteFile": "/tmp/myfile*.txt"
         }


**Note:**

  * The `*` character is the only supported wildcard for the `RemoteFile` parameter.
  * When using a wildcard that matches multiple files, the `Download` action returns the content of only one matching file. It doesn't return the content of all matching files. To download multiple files, you must first list the files using the `List` operation and then perform a separate `Download` action for each file.

  
  
## System limitations

The SFTP connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
remote_path | STRING | False | The current path in the SFTP server.   
  
## JSON schema for payload

All the entity objects in a SFTP connection have a pre-defined JSON schema. The entity objects in a SFTP connection use the following JSON schema:
    
    
        {
          "type": "object",
          "properties": {
            "FilePath": {
              "type": "string",
              "readOnly": false
            },
            "Filename": {
              "type": [
                "string",
                "null"
              ],
              "readOnly": false,
              "description": "The name of the file or directory."
            },
            "FileSize": {
              "type": [
                "number",
                "null"
              ],
              "readOnly": false,
              "description": "The size of the file."
            },
            "LastModified": {
              "type": [
                "string",
                "null"
              ],
              "readOnly": false
            },
            "IsDirectory": {
              "type": [
                "boolean",
                "null"
              ],
              "readOnly": false
            },
            "Permissions": {
              "type": [
                "string",
                "null"
              ],
              "readOnly": false
            },
            "Owner": {
              "type": [
                "string",
                "null"
              ],
              "readOnly": false
            },
            "OwnerId": {
              "type": [
                "string",
                "null"
              ],
              "readOnly": false
            },
            "Group": {
              "type": [
                "string",
                "null"
              ],
              "readOnly": false
            },
            "GroupId": {
              "type": [
                "string",
                "null"
              ],
              "readOnly": false
            }
          }
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
