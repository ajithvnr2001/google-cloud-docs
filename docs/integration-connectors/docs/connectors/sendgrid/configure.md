---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/sendgrid/configure/
title: SendGrid \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:26.025168+00:00
---

# SendGrid  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/sendgrid/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SendGrid

The SendGrid connector lets you perform insert, delete, update, and read operations on SendGrid dataset.

## Before you begin

Before using the SendGrid connector, do the following tasks:

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




### Set up authentication using API key

  1. Go to to **Settings** and select **API Keys**.
  2. Click **Create API Key**
  3. Enter a name for your API key
  4. Select from **Full Access** , **Restricted Access** , or **Billing Access** options
  5. Select **Restricted Access** , or **Billing Access** , and select the specific permissions for each category.
  6. Click **Create and View**.
  7. Copy the APi key and save it for later use.



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
     1. **Connector** : Select **SendGrid** from the drop down list of available Connectors.
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
     8. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     9. Click **NEXT**.
  5. In the **Authentication** section, enter the authentication details. For more information, see [Configure authentication](https://docs.cloud.google.com/integration-connectors/docs/connectors/sendgrid/configure-auth). | 
  6. Click **NEXT**.
  7. **Review** : Review your connection and authentication details.
  8. Click **Create**.



### Configure authentication

* **API key authentication**

  * **API key** : Select the Secret Manager secret of the API key.
  * **Secret version** : Select the secret version.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the SendGrid connection.

### Web connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Sendgrid  
Connector version | 1  
Connection Name | sendgrid-google-cloud-conn  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
API Key | API_KEY  
Secret Version | 1  
  
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

The SendGrid connector can process 8 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists some of the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### SendMail2 action

This action sends an email along with attachment.

#### Request body fields for the SendMail2 action

Field name | Data type | Required | Description  
---|---|---|---  
Subject | String | Yes | The subject of the email to be sent.  
ContentValue | String | No | The content of the email to be sent.  
ContentType | String | No | The type of content to be sent. supported values are text/plain and text/html.  
Content | String | Yes | The aggregate for Content object.  
SendAt | String | No | The date and time when you want your email to be delivered. Scheduling more than 72 hours in advance is forbidden.  
FromEmail | String | Yes | The email address of the sender.  
FromName | String | No | The name of the sender.  
ToEmail | String | No | Email address to send the email to.  
ToName | String | No | Email's respective names to send the email to.  
To | String | No | The aggregate for To recipients.  
ToCCEmail | String | No | Email address of the recipients who will receive a copy of your email.  
ToCCName | String | No | Name of the recipients who will receive a copy of your email.  
ToBCCName | String | No | Name of the recipients who will receive a blind carbon copy of your email.  
ToBCC | String | No | The aggregate for ToBCC recipients.  
ReplyToEmail | String | No | The email address of the person to whom you are replying to.  
ReplyToName | String | No | The name of the person to whom you are replying to.  
AttachmentPaths | String | No | Path of the file to attach to the email to be sent.  
TemplateId | String | Yes | The ID of the template that you may want to send.  
DynamicTemplateData | String | No | The data of the dynamic template.  
Personalizations | String | Yes | An array of messages and their metadata. Each object within personalizations can be thought of as an envelope - it defines who should receive an individual message and how that message should be handled.   
  
#### Output parameters of the send an email action

This action returns confirmation message whether or not the mail was sent successfully.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Send an email

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendMail2` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "FromName": "Name",
             "FromEmail": "cloudysanfrancisco@gmail.com",
             "Subject": "[{\"value\": \"cymbalgroup.com\",\"type\": \"text/plain\"}]",
             "TemplateId": "d-c4bc730a0b094a3a9d9cabb7347b5edc",
             "Personalizations": "[{\"subject\": \"Test Subject3\",\"send_at\": 1698659820,\"from\": {\"name\": \"hi\",\"email\": \"email@gmail\"},\"to\":      
             [{\"email\": \"email@gmail.com\",\"name\": \"test\"}\n ]}]",
             "Content": "[{\"value\": \"abc@cdata.com\",\"type\": \"text/plain\"}]"
         }

This action returns confirmation message. If the action is successful, the task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True"
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all contacts

This example lists all the contacts in the `NMCContacts` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `NMCContacts` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). For example, `City='Bangalore'`. You can also specify multiple filter conditions by using the logic operators. For example, `City='Bangalore' and region='asia-south2'`. 



### Example - Get a record

This example gets a record with the specified ID from the `NMCSegments` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `NMCSegments` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `0d44bb3f-d28e-4bcf-aba2-c77be831ad46` in the **Default Value** field. 

Here, `0d44bb3f-d28e-4bcf-aba2-c77be831ad46` is a primary key value in the `NMCSegments` entity.




### Example - Create a record

This example creates a record in the `NMCSenders` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `NMCSenders` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Nickname": "Test",
         "FromEmail": "test1@examplepetstore.com",
         "FromName": "testuser",   
         "ReplytoEmail": "test1@examplepetstore.com",  
         "Address": "NA", 
         "City": "NA", 
         "Country": "India"}

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Id": 5360940.0
         }




### Example - Create a record

This example creates a record in the `NMCLists` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `NMCLists` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "TEST_CON_LIST1699262238224",
         "ContactCount": 3.0}

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Id": "d927f128-b718-447a-affe-417f1a8b3abd"}




### Example - Update a record

This example updates a record in the `NMCSenders` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `NMCSenders` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Nickname": "Test",
         "FromEmail": "test2@examplepetstore.com",
         "FromName": "testuser",   
         "ReplytoEmail": "test2@examplepetstore.com",  
         "Address": "NA", 
         "City": "NA", 
         "Country": "India"}

  5. Click **entityId** , and then enter `5360940.0` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Id":"5360940.0"
         }




### Example - Delete a record

This example deletes the record with the specified ID in the `NMCSegments` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `NMCSegments` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `c58b9151-7279-428a-bac2-12b4bf2b48b0` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
  
## Use the SendGrid connection in an integration

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
