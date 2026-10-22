---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/confluence/configure/
title: Confluence \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:46.302473+00:00
---

# Confluence  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/confluence/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Confluence

You can use the Confluence connector to perform insert, delete, update, and read operations on Confluence.

## Before you begin

Before using the Confluence connector, do the following tasks:

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

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Confluence** from the drop down list of available connectors. 
     2. **Connector version** : Select the connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the connection instance. 

Connection names must meet the following criteria:

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles. 
     7. Optionally, select **Include Archived Spaces** to include content from archived spaces in the result. The default is false. 
     8. Optionally, enter a **Space Key** for search to display contents only from this specific space. 
     9. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     10. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     11. Optionally, click **\+ ADD LABEL** to add a label to the connection in the form of a key/value pair. 
     12. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **NEXT**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an authentication type and enter the relevant details. 

The following authentication types are supported by the Confluence connector:

     * **Basic**
     * **APIToken**
     * **OAuth2.0**

To understand how to configure these authentication types, see Configure authentication. 

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Basic**
    * **Username** : The Confluence user account used to authenticate.
    * **Password** : The password associated with the account.
  * **APIToken**
    * **Username** : The Confluence username used to create the API token.
    * **API Token** : The password for the username is an API token. Select the secret manager secret containing the API token associated with the Confluence username. 
  * **OAuth 2.0 - Authorization code**
    * **Client ID:** Client ID as provided by your external application.
    * **Scopes:** The minimum required permission scopes depend on whether you are using Confluence's classic or granular scopes: 
      * Classic scopes: `search:confluence` and `offline_access`
      * Granular scopes: `read:content-details:confluence` and `offline_access`
Additionally, include any scopes necessary for your application. For more information about Confluence scopes, see [Confluence scopes](https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/). 
    * **Client secret:** Select the [Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart). You should have created the Secret Manager secret prior configuring this authorization. 
    * **Secret version:** Secret Manager secret version for client secret.

For the `Authorization code` authentication type, after creating the connection, you must perform a few additional steps for configuring authentication. For more information, see Additional steps after connection creation. 

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

**Note:** If you are using `Authorization code` authentication type and have made any configuration changes in your Confluence application, you must re-authorize your Confluence connection. To understand how to re-authorize, see Re-authorization for Authorization code. 



### Additional steps after connection creation

If you selected `OAuth 2.0 - Authorization code` for authentication, you must do the following additional steps after creating the connection:

  1. In the [Connections page](https://console.cloud.google.com/connectors/connections), locate the newly created connection. 

Notice that the **Status** for the new connector will be **Authorization required**.

  2. Click **Authorization required**. 

This shows the **Edit authorization** pane.

  3. Copy the **Redirect URI** value to your external application.
  4. Verify the authorization details.
  5. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com/connectors/connections).




## Re-authorization for authorization code

If you are using `Authorization code` authentication type and have made any configuration changes in your Confluence application, you must re-authorize your Confluence connection. To re-authorize a connection, perform the following steps: 

  1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

  2. Click **Edit** to edit the connection details. 
  3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

  4. Click **Save**. This takes you to the connection details page.
  5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
  6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




## System limitations

The Confluence connector can process 28 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Confluence connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



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

The Confluence connector provides actions such as DownloadAttachment and UploadAttachment. To understand how to configure the actions, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Download Attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "AttachmentId": "xyz"
           }




## Entity operation examples

### Example - List all the Requests

This example lists all the Requests in the `Requests` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Requests from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.



### Example - Get User from a specific Account Id

This example gets the User with having AccoundId as 6035864ce2020c0070b5285b from the `Users` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **filterClause** and then enter `AccountId=6035864ce2020c0070b5285b` in the **Default Value** field. 

Here, `AccountId` is the primary key value of the `Users` entity.




### Example - List Pages

This example lists the pages from the `Pages` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Pages` from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.



### Example - Get Pages

This example gets a page record from the `Pages` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Pages` from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `123` in the **Default Value** field. 

Here, `123` is an unique identifier for the resource `Pages` entity.




### Example - Create Pages

This example creates a page record in the `Pages` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Pages` from the `Entity` list.
  3. Select the `CREATE` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
               "SpaceId": "12345",
               "Status": "Current",
               "Title": "FROM XYZ",
               "Storage": "XYZ1234"
             }
         




### Example - Update Pages

This example updates a page record in the `Pages` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Pages` from the `Entity` list.
  3. Select the `UPDATE` operation, and then click **Do ne**.
  4. In the **Task Input** section of the **Co nnectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field:
         
         {
             "Title": "Update abc"
             }

  5. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `12345` in the **Default Value** field. 

If the integration is successful, the connector task's `connectorOutputPayload` field will have the response of the update operation.
    
    {
        "Id": 1234
        }




### Example - Delete a Page

This example deletes a page from the `Pages` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Pages` from the `Entity` list.
  3. Select the `DELETE` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `123` in the **Default Value** field. 

Alternately, if the entity has composite primary keys instead of specifying the **entityId** , you can set the **filterClause**. For example, `Id='123'`.




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
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
