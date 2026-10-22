---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/ftp/configure/
title: FTP \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:14.024225+00:00
---

# FTP  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/ftp/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FTP

The FTP connector lets you connect to a FTP server and perform file transfer operations.

## Before you begin

Before using the FTP connector, do the following tasks:

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

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **FTP** from the drop down list of available Connectors.
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
     8. **File Retrieval Depth** : Specify the depth level of folders you want to query from the Root table. 
     9. **Passive** : Controls whether to direct the server into passive mode. Recommended if behind a firewall. 
     10. **Remote Path** : The current path in the FTP server. 
     11. **SSL Mode** : The authentication mechanism to be used when connecting to the FTP server. 
     12. **Table Depth** : The depth level to display subfolders as views. 
     13. **Use MLSD** : Uses listings for machine processing. Used only for FTP servers. 
     14. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     15. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+Add Destination**.

  6. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the FTP connection:

     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **Next**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : The FTP username to use for the connection.
    * **Password** : Secret Manager Secret containing the password associated with the FTP username.



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

The FTP connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists some of the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### Upload action

The following table describes the input parameters of the `Upload` action.

Parameter name | Data type | Required | Description  
---|---|---|---  
Content | String | No | Content to upload as a file.  
ContentBytes | String | No | Bytes content (as a Base64 string) to upload as a file. Use this to upload binary data.  
HasBytes | Boolean | No | Specifies if the content should be uploaded as bytes. The default value is `false`.  
RemoteFile | String | Yes | The file name on the remote host.  
Overwrite | Boolean | No | Specifies if the remote file should be overwritten. The default value is `false`.  
  
For examples on how to configure the `Upload` action, see Examples.

### Download action

The following table describes the input parameters of the `Download` action.

Parameter name | Data type | Required | Description  
---|---|---|---  
RemoteFile | String | Yes | The file name on the remote host.  
HasBytes | Boolean | No | Specifies if the content should be downloaded as bytes. The default value is `false`.  
  
For examples on how to configure the `Download` action, see Examples.

### MoveFile action

The following table describes the input parameters of the `MoveFile` action.

Parameter name | Data type | Required | Description  
---|---|---|---  
RemoteFile | String | Yes | The path of the remote file to be moved.  
DestinationPath | String | Yes | The new path you want to move the file to.  
  
For examples on how to configure the `MoveFile` action, see Examples.

### RenameFile action

The following table describes the input parameters of the `RenameFile` action.

Parameter name | Data type | Required | Description  
---|---|---|---  
RemoteFile | String | Yes | Remote file path and name to be renamed.  
NewFileName | String | Yes | New name of the remote file.  
  
For examples on how to configure the `RenameFile` action, see Examples.

## Examples

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
  * The `FilePath` field is defined in the input payload's JSON schema. For the list of all the available fields, see Input payload JSON schema.
  * You can dynamically set the filter clause by using the Data Mapping task in your integration. For more information, see Dynamic configuration of filterClasue.

  
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

This sample creates the `file_1.txt` file that has the content `This is a sample text!` in the FTP server's `/tmp` directory. And any existing file with the same name is overwritten because the `Overwrite` attribute value is `true`.  Setting the `Overwrite` attribute is optional; by default, the value is `false`.  
**Note:** You can't upload a local file directly to the FTP server. You must specify the file's entire content in the `Content` attribute.   
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

This sample creates the `image_1.png` file with the content as specified in the `ContentBytes` field. The file is created in the FTP server's `/tmp` directory. And any existing file with the same name is overwritten because the `Overwrite` attribute value is `true`.  Setting the `Overwrite` attribute is optional; by default the value is `false`.  
  
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
  
## JSON schema for payload

All the entity objects in a FTP connection have a pre-defined JSON schema. Having a good understanding of the schema, lets you easily configure the input or output payload values. The entity objects in a FTP connection use the following JSON schema:
    
    
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

## Dynamic configuration of filterClause

For the List, Update, and Delete operations, you can set the value of the filterClasue input variable dynamically at runtime by using the [Data Mapping](https://docs.cloud.google.com/application-integration/docs/data-mapping-task) task in your integration. For example, you might want to send the filter clause's value when invoking the [API trigger](https://docs.cloud.google.com/application-integration/docs/configuring-api-trigger) in your integration. The following image shows a sample mapping for the `filterClause` variable in the Data Mapping editor of the Data Mapping task: ![set filter clause in the data mapping editor](https://docs.cloud.google.com/static/integration-connectors/images/data_mapping_filter_clause.png)

## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
file_retrieval_depth | STRING | False | Specify the depth level of folders you want to query from the Root table.   
passive | BOOLEAN | False | Controls whether to direct the server into passive mode. Recommended if behind a firewall.   
remote_path | STRING | False | The current path in the FTP server.   
table_depth | INTEGER | False | The depth level to display subfolders as views.   
use_mlsd | BOOLEAN | False | Uses listings for machine processing. Used only for FTP servers.   
  
## Use the FTP connection in an integration

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
