---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/mcp/configure-mcp/
title: Create and configure an MCP connector \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:34.260585+00:00
---

# Create and configure an MCP connector  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/mcp/configure-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Create and configure an MCP connector

The page describes how to create and configure an MCP connector in Integration Connectors. For more information about the MCP connector, see [MCP connector overview](https://docs.cloud.google.com/integration-connectors/docs/connectors/mcp/overview-mcp).

## Before you begin

Before using the MCP connector, complete the following tasks:

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

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the Google Cloud console, go to the **Integration Connectors** > **Connections** page. 

[Go to Connections](https://console.cloud.google.com/connectors/connections)

  2. Select or [create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to use for the connector.
  3. Click add_box **Create Connection**. 

The **Create Connection** page appears.

  4. In the **Location** section: 
     1. Click **Region** and then select a location for the connection. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  5. In the **Connection Details** section, provide the following details: 
     1. **Connector** : Select **MCP (Preview)**.
     2. **Connector version** : Select the version of the connector to use. 
     3. **Connection Name** : Enter a name for the connection. **Important:** The connection name must be unique within the selected region. The connection name must adhere to the following rules: 
        * The name must contain lower-case letters, numbers, or hyphens.
        * The name must begin with a letter and end with a letter or number.
        * The name must not exceed 49 characters.
     4. **Description** : (Optional) Enter a description for the connection.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select the service account to use for the connection. Ensure that the service account has the relevant IAM roles and permissions.
     7. **MCP Endpoint** : (Optional) Leave empty to use the default endpoint - `/mcp`. If the endpoint is same as the host address, then set this to `/`. Only applicable for the Streamable HTTP Server.
     8. **Connection node settings** : (Optional) Configure the connection node settings. 
        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes process more transactions for a connection, and fewer nodes process fewer transactions. To understand how nodes affect connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default, the minimum number of nodes is 2 (for better availability), and the maximum number of nodes is 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     9. Click **Next**.
  6. In the **Destinations** section, enter details of the remote host (backend system) to connect to. 
     1. **Destination Type** : Select the destination type. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

Examples of host addresses to use:

        * `https://your-service.example.com/sse` (No Authentication)
        * `https://your-oauth-provider.example.com/sse` (OAuth 2.0 - Authorization code)
        * `https://your-api-key-service.example.com/sse` (API Key Authentication)
  7. To enter additional destinations, click **+Add Destination**.
  8. Click **Next**.


* In the **Authentication** section, select and configure the authentication for the connection: 

### No Authentication

This type is used for hosts without specific authentication requirements.

### OAuth 2.0 - Authorization code

This type is used for hosts that support the OAuth 2.0 Authorization Code grant type.

  1. **Client ID:** Enter the Client ID provided by your external application.
  2. **Scopes:** Enter the required permission scopes.
  3. **Client secret:** Choose the [Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart) containing the client secret.
  4. **Secret version:** Select the Secret Manager secret version for the client secret.
  5. **Enable PKCE:** Optional: Enable PKCE for the auth code flow. Enable only if server supports PKCE.
  6. **Authorization URL:** Enter the URL for authorization.
  7. **Access Token URL:** Enter the URL to obtain the access token.



For the `Authorization code` authentication, after creating the connection, you must complete a few additional steps to complete the authentication configuration. For more information, see Additional steps after connection creation. 

**Note:** If you are using `Authorization code` authentication and have made any configuration changes in your application, you must re-authorize your connection. To re-authorize, see Re-authorization for Authorization code. 

### Additional steps after connection creation

If you selected OAuth 2.0 - Authorization code for authentication, you must complete the following additional steps after creating the connection:

  1. In the **Connections** page, locate the newly created connection.
  2. The status for the new connection is **Authorization required**.
  3. Click **Authorization required**. 

The **Edit authorization** pane appears.

  4. Copy the **Redirect URI** value to your external application.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

  5. Verify the authorization details.
  6. Click **Authorize**. 

If the authorization is successful, the connection status is set to **Active** in the Connections page.




### API Key Authentication

This type is used for hosts that require an API key for authentication.

  * **API key:** Select the Secret Manager secret containing the API key. For example, `projects/PROJECT_ID/secrets/your-api-key-secret/versions/1`. 
  * **API key parameter name:** The name of the parameter for the API key. For example, `Authorization`.
  * **API key location:** The location where the API key is sent. For example, `Header`. 


* Click **Next**.
* In the **Review** section, review the connection and authentication details. To make changes, click any of the previous sections.
* Click **Create**. 

Integration Connectors starts creating the connection with the provided configuration. The connection creation takes a few minutes to complete. After the connection is created, the system redirects you to the **Connections** page. 

## Use the MCP connection in an integration

After you create the connection, it becomes available in Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



### Create an integration using the MCP connector

To create an integration using the MCP connector, perform the following steps:

  1. Add an **API Trigger** to your integration: 
     1. In the Google Cloud console, go to the Application Integration page. 

[Go to Application Integration](https://console.cloud.google.com/application-integration)

     2. In the navigation menu, click **Integrations**. The **Integrations List** page appears.
     3. Select an existing integration or click **Create integration** to create a new one.
     4. If you are creating a new integration: 
        1. Enter an integration name and description in the **Create Integration** pane.
        2. Select a region for the integration. The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information.
        3. Optional. Select a service account for the integration. The option to select a service account is displayed only if you have enabled integration governance for the selected region.
        4. Click **Create**. The newly created integration opens in the integration editor.
     5. In the integration editor navigation bar, click **Triggers** to view the list of available triggers.
     6. Click and place the **API trigger** element to the designer.
  2. Add **Data Mapping** if required. 
  3. Go to **Tasks** and choose one of the connectors listed above or the one you created, if applicable.
  4. Click **Configure connector** and choose actions. The default settings are pre-selected. 

A dropdown will show various actions, which are tools in this context.

![Screenshot showing available actions in the MCP connector configuration.](https://docs.cloud.google.com/static/integration-connectors/images/mcpactions.png)

     1. Configure the required input parameters for the action. You can set these as integration inputs, use variables from previous tasks, or specify default values directly.
     2. Pass the required arguments and test the connection. 

![Screenshot showing task input in the MCP connector configuration.](https://docs.cloud.google.com/static/integration-connectors/images/mcp-taskinput.png)




For the list of supported entities and operations, see [Supported entities and operations](https://docs.cloud.google.com/integration-connectors/docs/connectors/mcp/overview-mcp#supported_entities_and_operations). For information about the supported connector-specific actions, see [Supported actions](https://docs.cloud.google.com/integration-connectors/docs/connectors/mcp/overview-mcp#supported_actions). 

## Use case example in Application Integration

The following examples demonstrate how to use the Connectors task in Application Integration to perform operations using your configured MCP connection.

### Example - Jira: Create Issue

To create an issue in Jira using a MCP connection:

  1. In the **Configure connector** task dialog, select your Jira MCP connection (e.g., `jira-connection`).
  2. Click **Actions**.
  3. Select the `create_issue` action.
  4. Click **Done**.
  5. In the **Task Input** section, pass the following arguments: 
         
         {
           "fields": {
             "project": {
               "key": "YOUR_PROJECT_KEY"
             },
             "summary": "New issue created from Integration Connectors",
             "issuetype": {
               "name": "Task"
             },
             "description": "This is a test issue created via the MCP Jira connector."
           }
         }
                 




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
proxy_enabled | BOOLEAN | False | Set to true to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
