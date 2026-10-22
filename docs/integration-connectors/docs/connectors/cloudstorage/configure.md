---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudstorage/configure/
title: Cloud Storage \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:41.393744+00:00
---

# Cloud Storage  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudstorage/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Storage

The Google Cloud Storage connector lets you connect to a Google Cloud Storage and perform file transfer operations.

## Before you begin

Before using the Cloud Storage connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`
      * `roles/storage.admin`

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
     1. **Connector** : Select **Cloud Storage** from the drop down list of available Connectors.
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
     8. **Project ID** : The ID of the Google Cloud project where the data resides. 
     9. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     10. Click **NEXT**.
  5. **Review** : Review your connection.
  6. Click **Create**.



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

The Google Cloud Storage connector can process a maximum of 10 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

The Google Cloud Storage connection supports the following actions:

  * DownloadObject
  * UploadObject
  * CopyObject
  * MoveObject
  * DeleteObject
  * SignURL

**Note:** The results of all the entity operations and actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### DownloadObject action

The following table describes the input parameters of the `DownloadObject` action.

Parameter name | Required | Data type | Description  
---|---|---|---  
Bucket | Yes | String | Bucket name where the object to be downloaded is present.  
ObjectFilePath | No | String | Name of the object that should be downloaded. If not specified, all the objects from the specified bucket will be downloaded.  If the object to download is present in a child folder of a bucket, you must provide the full path of such object. For example, to download `logfile.txt` that is present in `bucket_01`'s `folderA`, the object path should be `folderA/logfile.txt`.   
HasBytes | No | Boolean | Whether to download content as bytes. The valid values are `true` or `false`. If set to `true`, the content is downloaded as a `Base64` encoded string. By default, the `HasBytes` field is set to `false`.  
UpdatedEndDate | No | Date | The end date range to download objects. If not specified, objects will be downloaded from the specified `UpdatedStartDate` until the present day.  
UpdatedStartDate | No | Date | The start of the date range to download objects. If not specified, objects will be downloaded from the beginning of the time until the `UpdatedEndDate`.  
**Note:** The objects will not be downloaded to any local system, but will be available to you as a JSON response in the Connector task's `connectorOutputPayload` response parameter after you run your integration.

For examples on how to configure the `DownloadObject` action, see Examples.

### UploadObject action

The following table describes the input parameters of the `UploadObject` action.

Parameter name | Required | Data type | Description  
---|---|---|---  
Bucket | Yes | String | Bucket name where the object will be uploaded.  
FolderPath | No | String | The path to the folder where the object should be uploaded.  
ContentBytes | No | String | Content to upload in the form of bytes (Base64 encoded string).  
HasBytes | No | Boolean | Whether to upload content as bytes. Valid values; `true` or `false`. If set to `true`, the content you want to upload should be a Base64 encoded string. By default, the `HasBytes` field is set to `false`.  
Content | Yes | String | The content to be uploaded.  
ObjectName | No | String | Name of the object that will be uploaded.  
**Note:** If the specified upload folder doesn't exist, the folder is automatically created in the bucket.

For examples on how to configure the `UploadObject` action, see Examples.

### CopyObject action

The following table describes the input parameters of the `CopyObject` action.

Parameter name | Required | Data type | Description  
---|---|---|---  
BucketSource | Yes | String | Bucket name from which you want to copy the object.  
ObjectSource | Yes | String | Full path of the folder where you want to copy the object.  
BucketDestination | Yes | String | Bucket name to which you want to copy the object.  
ObjectDestination | No | String | Full path of the destination including the object name. If you don't specify any object name, the name of the source object is retained.  
  
For examples on how to configure the `CopyObject` action, see Examples.

### MoveObject action

The following table describes the input parameters of the MoveObject action.

Parameter name | Required | Data type | Description  
---|---|---|---  
BucketSource | Yes | String | Bucket name from which you want to move the object.  
ObjectSource | Yes | String | Full path of the folder where you want to move the object.  
BucketDestination | Yes | String | Bucket name to which you want to move the object.  
ObjectDestination | No | String | Full path of the destination including the object name. If you don't specify any object name, the name of the source object is retained.  
**Tip:** If you want to rename a file in a bucket, use the MoveObject action and specify the same bucket name in both source and destination.

### DeleteObject action

The following table describes the input parameters of the `DeleteObject` action.

Parameter name | Required | Data type | Description  
---|---|---|---  
BucketSource | Yes | String | Bucket name where the object to be deleted is present.  
ObjectSource | Yes | String | Name of the object that you want to delete.  
Generation | No | Double | Version of the object to delete. If present, deletes the specified revision of the object as opposed to the latest version, which is the default behaviour.  
IfGenerationMatch | No | Double | Makes the delete operation conditional on whether the object's current generation matches the given value. Setting this value to 0 makes the operation succeed only if there are no live versions of the object.  
IfGenerationNotMatch | No | Double | Makes the delete operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting this value to `0` makes the operation succeed only if there is a live version of the object.  
IfMetagenerationMatch | No | Double | Makes the delete operation conditional on whether the object's current metageneration matches the specified value.  
IfMetagenerationNotMatch | No | Double | Makes the delete operation conditional on whether the object's current metageneration does not match the specified value.  
  
### SignURL action

The following table describes the input parameters of the `SignURL` action which creates a signed URL for the specified object.

Parameter name | Required | Data type | Description  
---|---|---|---  
Bucket | Yes | String | The bucket name where the object resides.  
Object | Yes | String | The name of the object to generate the SignedURL for.  
RequestMethod | No | String | The method that the signed request will use. The default value is `GET`.  
Location | No | String | Location of the specified bucket. The default value is `auto`.  
ActiveDateTime | No | String | The dateTime when the SignedURL will become active. If not specified the current dateTime will be used.  
Query | No | String | The query string that must be included when using the SignedURL, if not specified no query string will be used.  
CustomHeaders | No | String | A comma separated list of name=value of the headers to use with the SignedURL, if not specified not custom headers will be used.  
ExpiresIn | Yes | String | The expiration time for the SignedURL it should be in the format: `1d2h3m4s`, the maximum value is `7d0h0m0s`.  
HMAC Access ID | Yes | String | The HMAC access ID. For information, see [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).   
HMAC Secret | Yes | String | The HMAC secret.  
  
## Examples

This examples in this section describe the following operations: 

  * List all objects
  * List all objects in a bucket
  * List objects using the LIKE filter for name
  * List all buckets
  * Download an object
  * Download a binary object
  * Upload a binary object to a bucket
  * Upload an object to a bucket
  * Upload an object to a folder
  * Copy an object
  * Move an object
  * Delete an object
  * Create a signed URL for an object



The following table lists the sample scenarios and the corresponding configuration in the Connectors task:

Task | Configuration  
---|---  
List all objects | 

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select the `Objects` entity and then select the `List` operation.
  3. Click **Done**.

This lists all the objects in all the buckets. The objects are listed in the `Connectors` task's `connectorOutputPayload` response parameter.  
List all objects in a bucket | 

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select the `Objects` entity and then select the `List` operation.
  3. Click **Done**.
  4. Set the [filterClause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter) to the bucket name from which you want to list the objects. To set the clause, in the `Task Input` section of the `Connectors` task, click **filterClause** and then enter `Bucket = 'BUCKET_NAME'` in the **Default Value** field. For example, `Bucket = 'bucket_01'`.

  
List objects using the LIKE filter for name | 

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select the `Objects` entity and then select the `List` operation.
  3. Click **Done**.
  4. Set the [filterClause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter) to the bucket name from which you want to list the objects. To set the clause, in the `Task Input` section of the `Connectors` task, click **filterClause** and then enter `Name LIKE 'NAME%' AND Bucket = 'BUCKET_NAME'` in the **Default Value** field. For example, `Name LIKE 'Operations%' AND Bucket = 'OperationsBucket'`.

  
List all buckets | 

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select the `Buckets` entity and then select the `List` operation.
  3. Click **Done**.

  
Download an object | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Bucket": "bucket-test-01",
           "ObjectFilePath": "logfile.txt"
         }

This example downloads the `logfile.txt` file. The downloaded file's content is available to you in JSON format in the `Connectors` task's `connectorOutputPayload` response parameter. 
  
Download a binary object |  The steps to download a binary object are the same as downloading a regular object as previously described. Additionally, you must specify the `HasBytes` as `true` in the `connectorInputPayload` field. This downloads the object as a Base64 encoded string. Sample value for the `connectorInputPayload` field:
    
    
    {
    "Bucket": "bucket-test-01",
    "ObjectFilePath": "image01.png",
    "HasBytes" : true
    }

If the download is successful, the output in the `connectorOutputPayload` field will be similar to the following:
    
    
    {
    "Success": "true",
    "ContentBytes": "SGVsbG8gdGVzdCE\u003d"
    }

By default, the `HasBytes` field is set to `false`. If the file, contains special characters, such as ä, Ø, Thành, do the following:

  1. **Encode in UTF-8:** Encode the file in UTF-8 to handle the special charecters.
  2. **Convert to Base64:** Convert the file to Base64 to ensure that the original text remains intact.
  3. **Decode the Base64 string:** Decode the file to Base64 string to retrieve the original value with the special characters.

  
Upload a binary object to a bucket | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "ContentBytes": "SGVsbG8gVGVzdCE=",
         "Bucket": "bucket-test-01",
         "ObjectName" : "test-file-01",
         "HasBytes": true
         }

This example creates the `test-file-01` file in the `bucket-test-01` bucket. If there is an existing file with the `test-file-01` name, it's overwritten. 
  
Upload an object to a bucket | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "Content": "Hello test!",
         "Bucket": "bucket-test-01",
         "ObjectName" : "test-file-01.txt"
         }

This example creates the `test-file-01.txt` file with the content `Hello test!` in the `bucket-test-01` bucket. If there is an existing file with the `test-file-01.txt` name, it's overwritten. 
  
Upload an object to a folder | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "Content": "Hello test!",
         "Bucket": "bucket-test-01",
         "FolderPath": "folderA",
         "ObjectName": "test-file-01.txt"
         }

This example creates the `test-file-01.txt` file with the content `Hello test!` in the `bucket-test-01`'s `folderA` folder. If the folder has an existing file with the `test-file-01.txt` name, it's overwritten. 
  
Copy an object | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CopyObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "BucketSource": "bucket_01",
         "ObjectSource": "folderA/logfile.txt",
         "BucketDestination": "bucket_02",
         "ObjectDestination": "folderB/logfile.txt"
         }

This example copies the `folderA/logfile.txt` file from `bucket_01` to `folderB/logfile.txt` in `bucket_02`. 
If the copy is successful, the output in the `connectorOutputPayload` field will be similar to the following:
    
    
    {
    "Success": "true"
    }  
  
Move an object | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MoveObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "BucketSource": "bucket_01",
         "ObjectSource": "folderA/logfile.txt",
         "BucketDestination": "bucket_02",
         "ObjectDestination": "folderB/logfile.txt"
         }

This example moves the `folderA/logfile.txt` file from `bucket_01` to `folderB/logfile.txt` in `bucket_02`. 
If the copy is successful, the output in the `connectorOutputPayload` field will be similar to the following:
    
    
    {
    "Success": "true"
    }  
  
Delete an object | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteObject` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "BucketSource": "bucket_01",
         "ObjectSource": "logfile.txt"
         }

This example deletes the `logfile.txt` file from `bucket_01`. 
If the copy is successful, the output in the `connectorOutputPayload` field will be similar to the following:
    
    
    {
    "Success": "true"
    }  
  
Create a signed URL for an object | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SignURL` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
         "Bucket": "bucket-test-01",
         "ObjectName" : "test-file-01.txt"
         }

This example creates a signed URL for the `test-file-01.txt` file which is in the `bucket-test-01` bucket. If the action is successful, you will get the signed URL in the response similar to the following:
    
    {
    "Success": "true",
    "SignURL": "https://storage.googleapis.com/example-bucket/cat.jpeg?X-Goog-Algorithm=
    GOOG4-RSA-SHA256&X-Goog-Credential=example%40example-project.iam.gserviceaccount.com
    %2F20181026%2Fus-central1%2Fstorage%2Fgoog4_request&X-Goog-Date=20181026T18
    1309Z&X-Goog-Expires=900&X-Goog-SignedHeaders=host&X-Goog-Signature=247a2aa45f16
    9edf4d187d54e7cc46e4731b1e6273242c4f4c39a1d2507a0e58706e25e3a85a7dbb891d62afa849
    6def8e260c1db863d9ace85ff0a184b894b117fe46d1225c82f2aa19efd52cf21d3e2022b3b868dc
    c1aca2741951ed5bf3bb25a34f5e9316a2841e8ff4c530b22ceaa1c5ce09c7cbb5732631510c2058
    0e61723f5594de3aea497f195456a2ff2bdd0d13bad47289d8611b6f9cfeef0c46c91a455b94e90a
    66924f722292d21e24d31dcfb38ce0c0f353ffa5a9756fc2a9f2b40bc2113206a81e324fc4fd6823
    a29163fa845c8ae7eca1fcf6e5bb48b3200983c56c5ca81fffb151cca7402beddfc4a76b13344703
    2ea7abedc098d2eb14a7"
    }


  
  
## Considerations

  * A downloadable object can have a maximum size of 10 MB.
  * You can't upload multiple files using the `UploadObject` action. You can upload only a single file.



## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
project_id | STRING | True | The ID of the Google Cloud project where the data resides.   
  
## Use the Cloud Storage connection in an integration

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
