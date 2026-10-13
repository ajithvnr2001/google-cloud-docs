---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/trello/configure/
title: Trello \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:26.169982+00:00
---

# Trello  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/trello/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trello

The Trello connector lets you perform insert, delete, update, and read operations on Trello dataset.

## Before you begin

Before using the Trello connector, do the following tasks:

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




### Trello configuration

#### Create custom Power up

For information about creating Power up, see [Create custom power up](https://developer.atlassian.com/cloud/trello/guides/power-ups/managing-power-ups/#adding-a-new-custom-power-up).

#### Generete API key and token

  1. Create a Trello Power up for generating an API key.
  2. Go to [ Admin page](https://trello.com/power-ups/admin), after you have created Power up to access your Power up information.
  3. Navigate to the API Key tab and select the option to generate a new API key.
  4. Click **Token**.
  5. Click **Allow**.
  6. Copy the token.



For more information about Trello API, see [API Introduction](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

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
     1. **Connector** : Select **Trello** from the drop down list of available Connectors.
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
     8. **Board Id** : The Trello BoardId. 
     9. **Include Organization Boards** : IncludeOrganizationBoards determines if the logged in user has organizations or an enterprise of its own. And want to retrieve data from both organization and personal boards. 
     10. **Member Id** : The Trello MemberId. 
     11. **Organization Id** : The Trello OrganizationId. 
     12. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
        * **Proxy Auth Scheme** : Select the authentication type to authenticate with the proxy server. The following authentication types are supported: 
          * **Basic** : Basic HTTP authentication.
          * **Digest** : Digest HTTP authentication.
        * **Proxy User** : A user name to be used to authenticate with the proxy server. 
        * **Proxy Password** : The Secret manager secret of the user's password. 
        * **Proxy SSL Type** : The SSL type to use when connecting to the proxy server. The following authentication types are supported: 
          * **Auto** : Default setting. If the URL is an HTTPS URL, then the Tunnel option is used. If the URL is an HTTP URL, then the NEVER option is used.
          * **Always** : The connection is always SSL enabled.
          * **Never** : The connection is not SSL enabled.
          * **Tunnel** : The connection is through a tunneling proxy. The proxy server opens a connection to the remote host and traffic flows back and forth through the proxy.
        * In the **Proxy Server** section, enter details of the proxy server. 
          1. Click **\+ Add destination**.
          2. Select a **Destination Type**. 
             * **Host address** : Specify the hostname or IP address of the destination. 

If you want to establish a private connection to your backend system, do the following:

               * Create a [PSC service attachment](https://docs.cloud.google.com/integration-connectors/docs/configure-psc).
               * Create an [endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/create-ep-attachment) and then enter the details of the endpoint attachment in the **Host address** field.
     13. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     14. Click **NEXT**.
  5. In the **Authentication** section, enter the following details: 
     1. **Api Key** : The Trello API key that is used to authenticate by using Trello's own authorization route.
     2. **Token** : The Trello token key that is used to authenticate using Trello's own authorization route.
  6. Click **NEXT**.
  7. **Review** : Review your connection and authentication details.
  8. Click **Create**.



### Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Trello connection.

####  Trello server connection type

< Field name | Details  
---|---  
Location | Us-central1  
Connector | Trello  
Connector version | 1  
Connection Name | trello-google-cloud-new  
Enable Cloud Logging | No  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Proxy | No  
App Key | APP_KEY  
Token | TOKEN  
Secret version | 1  
  
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

The Stripe connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### UploadAttachment action

This action lets you upload an attachment.

#### Input parameters of the UploadAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
CardId | String | Yes | Id of the card for which attachment has to be added.  
Name | String | No | Name of the file to be uploaded. A maximum of 256 characters is allowed.  
MimeType | String | No | The mimeType of the attachment. A maximum of 256 characters is allowed.  
SetCover | String | No | Determines whether to use the new attachment as a cover for the Card. The default value is `false`.  
AttachmentPath | String | No | The local attachment path.  
FileName | String | Yes | The file name including extension to be used for the AttachmentPath or Content input. FileName is optional for AttachmentPath input, and is required for Content input.  
Url | String | No | A URL to attach. Must start with either `http://` or `https://`.  
Content | String | No | Alternative to AttachmentPath. The InputStream to read the attachment bytes from.  
HasBytes | Boolean | No | Specifies if the content to upload is in a binary (Base64 encoded string) format. The default value is `false`.  
  
For example on how to configure the `UploadAttachment` action, see Action examples.

### DownloadAttachment action

This action lets you download an attachment.

#### Input parameters of the DownloadAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
CardId | String | Yes | ID of the card for which where the attachment should be downloaded.  
AttachmentId | String | Yes | Id of the attachment that has to be downloaded.  
HasBytes | Boolean | No | Specifies if the content to download is in a binary (Base64 encoded string) format. The default value is `false`.  
  
For example on how to configure the `DownloadAttachment` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Upload an attachment

This example uploads an attachment.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "CardId": "6597cb14a9f10710fa2c4532",
         "FileName": "Test111",
         "Content": "This is test content"
         }

If the action is successful, the `UploadAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "Bytes": "27",
    "Date": "2024-02-16T12:45:47.714Z",
    "AttachmentId": "65cf58fbc68bd1c37057968b",
    "IdMember": "6597ca4e233f48b42ffd3db7",
    "Position": "81920",
    "Url": "https://trello.com/1/cards/5681cb14a9f10247fa2c4532/attachments/65cf58fbc68bd1c36587968b/download/Test111"
    }]




### Example - Download an attachment

This example downloads an attachment.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "CardId": "6597cb14a9f10710fa2c4532",
         "AttachmentId": "65cf58fbc68bd1c37057968b"
         }

If the action is successful, the `DownloadAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "FileName": "testFile.txt",
    "Content": "This is test content"
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all records

This example lists all the records in the `Checklists` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Checklists` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 
. 


### Example - Get a record

This example gets a record with the specified ID from the `BoardPlugins` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `BoardPlugins` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `55a5d917446f517774210011` in the **Default Value** field. 

Here, `55a5d917446f517774210011` is a unique record ID in the `BoardPlugins` entity.




### Example - Delete a card

This example deletes a file with the specified ID from the `Cards` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Cards` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `65b14f4e19abc0a1face4937` in the **Default Value** field.



### Example - Create a card

This example creates a card in the `Cards` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Cards` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "Testcard123",
           "Description": "test description",
           "ListID": "6597ca5df2b58ad47e6b1031"
           }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
           "CardId": "65b14f4e19abc0a1face4937"
           }




### Example - Update a card

This example updates a card in the `Cards` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Cards` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Description": "test description_Updated"
           }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
    
    {
      "CardId": "65b14f4e19abc0a1face4937"
      }




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
board_id | STRING | False | The Trello BoardId.   
include_organization_boards | BOOLEAN | False | IncludeOrganizationBoards determines if the logged in user has organizations or an enterprise of its own. And want to retrieve data from both organization and personal boards.   
member_id | STRING | False | The Trello MemberId.   
organization_id | STRING | False | The Trello OrganizationId.   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the Trello connection in an integration

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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
