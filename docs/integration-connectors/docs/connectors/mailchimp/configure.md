---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/mailchimp/configure/
title: MailChimp \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:32.738937+00:00
---

# MailChimp  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/mailchimp/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MailChimp

The MailChimp connector lets you perform insert, delete, update, and read operations on MailChimp dataset.

## Before you begin

Before using the MailChimp connector, do the following tasks:

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




## MailChimp configuration

### Set up a MailChimp account

For more information about setting up the MailChimp account, see [Account Login](https://mailchimp.com/help/create-an-account/#Sign_up_for_an_account).

### Set up authentication

#### API Keys - authentication type

For more information about generating a MailChimp API Key, see [Generate API Key](https://mailchimp.com/developer/marketing/guides/quick-start/#generate-your-api-key).

  1. Navigate to the API Keys section of your MailChimp account.
  2. Click **Create New Key** and enter a descriptive name. 
  3. Copy the generated key and store it in a secure location.You cannot view or copy the key later.



#### OAuth 2.0 - authentication type

For more information about generating OAuth Credentials for MailChimp account, see [GenerateOAuth Credentials](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/#register-your-application).

  1. Navigate to the Registered Apps page in your MailChimp account.
  2. Click **Register An App**.
  3. Complete the Register an App form.
  4. Click **Create**.
  5. Copy the client ID and client secret that appears.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

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
     1. **Connector** : Select **MailChimp** from the drop down list of available Connectors.
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
     8. **Datacenter** : The datacenter used for your MailChimp account. 
     9. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     10. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     11. Click **NEXT**.
  5. In the **Authentication** section, enter the authentication details. 
     1. The MailChimp connection doesn't require any authentication.
     2. Click **NEXT**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the MailChimp connection.

### API Keys - connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | MailChimp  
Connector version | 1  
Connection Name | google-cloud-mailchimp-api-conn  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication:Not Available | True  
API Key | API_KEY  
Secret version | 1  
  
### OAuth 2 - connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | MailChimp  
Connector version | 1  
Connection Name | google-cloud-mailchimp-oauth-conn  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication:OAuth 2.0 - Authorization code | True  
Client ID | CLIENT_ID  
Client Secret | CLIENT_SECRET  
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

The MailChimp connector can process 6 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

###  CampaignTest action

Send a test email for a MailChimp campaign.

#### Input parameters of the CampaignTest action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
CampaignID | string | True | The ID of the campaign to test.  
TestEmails | string | True | A comma-separated list of emails to send.  
SendType | string | True | The type of test email to send. Either html or plaintext The allowed values are html, plaintext. The default value is html.  
  
For example on how to configure the `CampaignTest` action, see Action examples.

### CampaignSend action

Send a MailChimp campaign.

#### Input parameters of the CampaignSend action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
CampaignID | string | True | The ID of the campaign to send.  
  
For example on how to configure the `CampaignSend ` action, see Action examples.

###  CampaignPause action

Pauses a MailChimp RSS campaign.

#### Input parameters of the CampaignPause action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
CampaignID | string | True | The ID of the campaign to pause.  
  
For example on how to configure the `CampaignPause ` action, see Action examples.

###  CampaignResume action

Resumes a MailChimp RSS campaign.

#### Input parameters of the CampaignResume action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
CampaignID | string | True | The ID of the campaign to resume.  
  
For example on how to configure the `CampaignResume ` action, see Action examples.

## Action examples

### Example - CampaignTest

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CampaignTest ` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "CampaignID": "4bd7a9abac",
         "TestEmails": "sample@gmail.com",
         "SendType": "plaintext"
         }

If the action is successful, the `CampaignTest` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Success": "true"
    }




### Example - CampaignSend

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CampaignSend` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "CampaignID": "1699382f6d"
         } 

If the action is successful, the `CampaignSend ` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Success": "true"
    }




### Example - CampaignPause

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CampaignPause ` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "CampaignID": "4bd7a9abac"
         }

If the action is successful, the `CampaignPause` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Success": "true"
    }




### Example - CampaignResume

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CampaignResume ` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "CampaignID": "4bd7a9abac"
         }

This example will show the specific Object records. If the action is successful, the `CampaignResume ` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Success": "true"
    }




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all campaigns

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Campaigns from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



### Example - Get a single automation

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Automations` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `1ac204985e` in the **Default Value** field. 

Here, `1ac204985e` is a unique record ID in the `Automations` entity.




### Example - Delete a campaign

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Campaigns` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `06f20ace93` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

### Example - Create a campaign folder

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `CampaignFolders` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "CampaignFolderCreated1707812599459"
         }
         
         
         Running this example, returns a response similar to the following in the connector
         task's connectorOutputPayload output variable:
         
         
         
         
         {
         "Id": "650469bb07"
         }
         




### Example - Update a file manager folder

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `FileManagerFolders` from the `Entity` list.
  3. Select the `Update` operation, and then click **Do ne**.
  4. In the **Task Input** section of the **Co nnectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field:
         
         {   
         "Name": "MyNewFolder9"
         }

  5. Click **entityId** , and then enter `18159` in the **Default Value** field. 

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {   
         "Id": "18159"
         }




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
datacenter | ENUM | False | The datacenter used for your MailChimp account. Supported values are: None, US1, US2, US3, US4, US5, US6, US7, US8, US9, US10, US11, US12, US13  
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the MailChimp connection in an integration

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
