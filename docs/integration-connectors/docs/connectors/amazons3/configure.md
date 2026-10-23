---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/amazons3/configure/
title: Amazon S3 \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:56.910278+00:00
---

# Amazon S3  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/amazons3/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Amazon S3

The Amazon S3 connector provides SQL access to Amazon S3 Buckets and objects.

## Before you begin

Before using the Amazon S3 connector, do the following tasks:

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
     1. **Connector** : Select **Amazon S3** from the drop down list of available Connectors.
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
     8. **AWS Region** : Region where your Amazon S3 instance is hosted 
     9. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     10. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+Add destination**.

  6. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Amazon S3 connection:

     * Root credentials 
     * AWS IAM Roles 
     * AWS Temporary Credentials 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **Next**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Root credentials**

To authenticate using account root credentials. 

    * **AWS Access Key** : The access key of the root user
    * **AWS Access Secret** : The secret key of the root user


  * **AWS IAM Roles**

To authenticate using an AWS IAM role. 

    * **AWS Access Key** : The access key of the IAM user to assume the role for
    * **AWS Access Secret** : The secret key of the IAM user to assume the role for
    * **AWS Role ARN** : Specify the Role ARN for the role you'd like to authenticate with. Only credentials for the specified role would be retrieved.
    * **AWS External Id** : Required only when you assume a role in another account.


  * **AWS Temporary Credentials**

To authenticate using temporary credentials 

    * **AWS Access Key** : The access key of the IAM user to assume the role for
    * **AWS Access Secret** : The secret key of the IAM user to assume the role for
    * **AWS Session Token** : This is generated alonside the temporary credentials.
    * **AWS Role ARN** : Specify the Role ARN for the role you'd like to authenticate with. Only credentials for the specified role would be retrieved.
    * **AWS External Id** : Required only when you assume a role in another account.



For information about how to set up an AWS account, see [Setting up Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-up-s3.html). For information about how to create an S3 bucket, see [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html). Contact your AWS administrator to create AWS IAM role credentials or AWS temporary credentials in the AWS account. 

### Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Amazon S3 connection.

#### Root credentials connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Amazon S3  
Connector version | 1  
Connection Name | aws-s3  
Description | aws-s3  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
AWS Region | Northern Virginia  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Root credentials | Yes  
AWS Access Key | AWS_ACCESS_KEY  
AWS Access Secret | AWS_ACCESS_SECRET  
Secret version | 1  
  
#### AWS IAM roles connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Amazon S3  
Connector version | 1  
Connection Name | aws-s3  
Description | aws-s3  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
AWS Region | Northern Virginia  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
AWS IAM Roles | Yes  
AWS Access Key | AWS_ACCESS_KEY  
AWS Access Secret | AWS_ACCESS_SECRET  
Secret version | 1  
  
#### AWS temporary credentials connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Amazon S3  
Connector version | 1  
Connection Name | aws-s3  
Description | aws-s3  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
AWS Region | Northern Virginia  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
AWS Temporary Credentials | Yes  
AWS Access Key | AWS_ACCESS_KEY  
AWS Access Secret | AWS_ACCESS_SECRET  
Secret version | 1  
AWS Session Token | AWS_SESSION_TOKEN  
  
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

## Actions

This section lists some of the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### CopyObject action

This action lets you copy an object from one bucket to another bucket or within the same bucket.

#### Input parameters of the CopyObject action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
BucketSource | String | Yes | Bucket name where the object should be copied from.  
ObjectSource | Object | Yes | Name of the object that should be copied.  
BucketDestination | String | Yes | Bucket name where the object should be copied to.  
ObjectDestination | String | No | Name of the object in the destination bucket. If not specified, the name will be the same as the original name.  
  
#### Output parameters of the CopyObject action

This action returns the status 200 (OK) if the copy is successful.

To understand how to configure the `CopyObject` action, see Action examples.

### DownloadObjects action

This action gets one more objects from a bucket.

#### Input parameters of the DownloadObjects action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Bucket | String | Yes | Bucket name where the object to be downloaded is present.  
Object | String | No | Name of the object that should be downloaded. If not specified, all the objects from the specified bucket are downloaded.  
HasBytes | Boolean | Yes | Specifies if the content should be downloaded as a Base64 encoded string.  
UpdatedStartDate | Datetime | No | The start date of the time range to download objects. If not specified, objects are downloaded from the oldest until the UpdatedEndDate.  
UpdatedEndDate | Datetime | No | The end date of the time range to download objects. If not specified, objects are downloaded from the specified UpdatedStartDate until the current day.  
  
#### Output parameters of the DownloadObjects action

This action returns the status 200 (OK) if the download is successful.

To understand how to configure the `DownloadObjects` action, see Action examples.

### UploadObject action

This action lets you upload an object to a bucket.

#### Input parameters of the UploadObject action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Bucket | String | Yes | Bucket name where the object should be uploaded.  
ContentBytes | String | No | The byte content to upload as a file.  
HasBytes | Boolean | Yes | Specifies if the content should be uploaded as a Base64 encoded string.  
AccessPolicy | String | No | The access policy for this object. The allowed values are PRIVATE, ANONREAD, ANONREADWRITE, and AUTHREAD. The default value is PRIVATE.  
Content | String | No | The content to be uploaded. | FileName | String | No | Name of the file to be uploaded. This value is required when you specify the FileContent parameter.  
  
#### Output parameters of the UploadObject action

This action returns the status 200 (OK) if the object upload is successful.

To understand how to configure the `UploadObject` action, see Action examples.

### DeleteObject Action

This action lets you delete an object from a bucket.

#### Input parameters of the DeleteObject action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Bucket | String | Yes | Bucket name where the object to be deleted is present.  
Object | String | Yes | Name of the object that should be deleted.  
  
#### Output parameters of the DeleteObject action

This action returns the status 200 (OK) if the deletion is successful.

To understand how to configure the `DeleteObject` action, see Action examples.

### MoveObject action

This action let users move an existing object of a specific bucket to another bucket or in the same bucket.

#### Input parameters of the MoveObject action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
BucketSource | String | Yes | The source bucket name where the object to be moved is present.  
ObjectSource | String | Yes | Name of the object that should be moved.  
BucketDestination | String | Yes | The destination bucket name where the object should be moved to.  
ObjectDestination | String | No | Name of the object in the destination bucket. If not specified, the original name is retained.  
  
#### Output parameters of the MoveObject action

This action returns the status 200 (OK) if the move operation is successful.

To understand how to configure the `MoveObject` action, see Action examples.

### PutBucketAcl action

This action lets you update the Access Control List (ACL) of a bucket.

#### Input parameters of the PutBucketAcl action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Bucket | String | Yes | Bucket name for which the ACL should be applied.  
ACL | String | Yes | Access level to be applied for the bucket.  
  
#### Output parameters of the PutBucketAcl action

This action returns the status 200 (OK) if the bucket ACL update is successful.

To understand how to configure the `PutBucketAcl` action, see Action examples.

### PutObjectAcl action

This action lets you update the Access Control List (ACL) of an object in a bucket.

#### Input parameters of the PutObjectAcl action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Bucket | String | Yes | Bucket name in which the object is present.  
ACL | String | Yes | Access level to be applied for the object.  
KEY | String | Yes | Object name for which the ACL should be applied.  
  
#### Output parameters of the PutObjectAcl action

This action returns the status 200 (OK) if the object ACL update is successful.

To understand how to configure the `PutObjectAcl` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Copy an object

This example copies an object from one bucket to another bucket.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CopyObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "BucketSource": "aws-s3-bucket-source",
         "ObjectSource": "pic.jpg",
         "BucketDestination": "aws-s3-bucket-destination",
         "ObjectDestination": "new_pic.jpg"
         }

If the action is successful, the `CopyObject` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Download an object

This example downloads an object from the specified bucket.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadObjects` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Bucket": "aws-s3-bucket-source",
         "HasBytes": true
         }

If the action is successful, the `DownloadObjects` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "RemoteFile": "prefix1%2Faws-s3-bucket-source%2Finventory-test-1%2F2023-09-10T01-00Z%2Fmanifest.json",
    "ContentBytes": "ewogICJzb3VyY2VCdWNrZXQiIDogImF3cy1zMy1idWNrZXQtYmNvbmUiLAogICJnOK"
    },
    {
    "Success": "True",
    "RemoteFile": "upload1.txt",
    "ContentBytes": "VGhpcyBpcyBhIHRlc3RpbmcgZmlsZQ=="
    }]




### Example - Upload an object

This example uploads an object to the specified bucket.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Bucket": "aws-s3-bucket-source",
         "FileName": "upload_1.txt",
         "Content": "This is a testing file",
         "AccessPolicy": "PUBLIC"
         }

If the action is successful, the `UploadObject` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "success",
    "bucket": "aws-s3-bucket-source",
    "rss:title": "Object 'upload_1.txt' was created in the bucket: aws-s3-bucket-source",
    "object": "upload_1.txt"
    }]




### Example - Delete an object

This example deletes an object from the specified bucket.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Bucket": "aws-s3-bucket-source",
         "Object": "abc.png"
         }

If the action is successful, the `DeleteObject` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Move an object

This example moves an object from one bucket to another bucket.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MoveObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "BucketSource": "aws-s3-bucket-source",
         "ObjectSource": "abc.png",
         "BucketDestination": "aws-s3-bucket-destination",
         "ObjectDestination": "moved.png"
         }

If the action is successful, the `MoveObject` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Update the ACL of a bucket

This example updates the access control permissions for a bucket.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `PutBucketAcl` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "BucketSource": "aws-s3-bucket-source",
         "ACL": "public-read"
         }

If the action is successful, the `PutBucketAcl` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Update the ACL of an object

This example updates the access control permissions for an object in a bucket.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `PutObjectAcl` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Bucket": "aws-s3-bucket-source",
         "ACL": "aws-exec-read",
         "Key": "AWS_S3_BusinessCase_V2.xlsx"
         }

If the action is successful, the `PutObjectAcl` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List metadata of all the objects

This example fetches the metadata of all the objects in the `Object` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Object` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). For example, `Bucket='test-bucket'`. You can also specify multiple filter conditions by using the logic operators. For example, `Bucket='test-bucket' and OwnerId='b1ecc809ad8467088afb'`. 



### Example - Get metadata of a bucket

This example gets the metadata of the bucket with the specified ID from the `Bucket` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Bucket` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `demo_replication` in the **Default Value** field. 

Here, `demo_replication` is a unique bucket ID in the `Bucket` entity.




### Example - Create a bucket

This example creates a bucket in the `Bucket` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Bucket` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Bucket": "Demo1697528098686"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
         "Bucket": "Demo1697528098686"
         }]




### Example - Delete a bucket

This example deletes the bucket with the specified ID in the `Bucket` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Bucket` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `demo1697528098686` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

## Use the Amazon S3 connection in an integration

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
