---
url: https://docs.cloud.google.com/sql/docs/sqlserver/use-cloudsql-mcp/
title: Use the Cloud SQL remote MCP server \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:43.701561+00:00
---

# Use the Cloud SQL remote MCP server  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/use-cloudsql-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Use the Cloud SQL remote MCP server Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/use-cloudsql-mcp "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp "View this page for the PostgreSQL database engine") | SQL Server

This document shows you how to use the Cloud SQL for SQL Server remote Model Context Protocol (MCP) server to connect with AI applications including Antigravity, ChatGPT, Claude, and custom applications you are developing. The Cloud SQL remote MCP server lets you access and run Cloud SQL tools to create, manage, and query Cloud SQL resources from your AI-enabled development environments and AI agent platforms. The Cloud SQL for SQL Server remote MCP server is enabled when you enable the Cloud SQL for SQL Server API. 

[Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) standardizes how large language models (LLMs) and AI applications or agents connect to external data sources. MCP servers let you use their tools, resources, and prompts to take actions and get updated data from their backend service.

## What's the difference between local and remote MCP servers?

Local MCP servers
    Typically run on your local machine and use the standard input and output streams (stdio) for communication between services on the same device.
Remote MCP servers
    Run on the service's infrastructure and offer an HTTP endpoint to AI applications for communication between the AI MCP client and the MCP server. For more information about MCP architecture, see [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

## Stateless core

With [MCP version 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28), MCP changes from a bidirectional, stateful protocol to a stateless protocol. Each MCP request is self-describing and can be routed using headers. There isn't a need for the `initialize`/`initialized` handshake or `Mcp-Session-Id` because each request includes all the information needed in HTTP headers or the `_meta` parameter. MCP servers can request additional information required by a tool through [multi-round-trip requests (MRTR)](https://modelcontextprotocol.io/specification/latest/basic/patterns/mrtr).

To help route and process requests without parsing the request body, some MCP headers are required, including the following:

  * Headers that are required by the MCP specification such as the [protocol version header](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#protocol-version-header) and [standard request headers](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#standard-request-headers).
  * [Custom headers](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#custom-headers-from-tool-parameters) that are defined by the MCP server. These headers are mirrored into HTTP headers from the tool's input schema using the `x-mcp-header` property. For example, an MCP server might define a custom header to specify the Google Cloud region or project ID.



For more information about MCP architecture, see the MCP version 2026-07-28 [specification](https://modelcontextprotocol.io/specification/2026-07-28) and [key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

## Google and Google Cloud remote MCP servers

Google and Google Cloud remote MCP servers have the following features and benefits: 

  * Simplified, centralized discovery
  * Managed global or regional HTTP endpoints
  * Fine-grained authorization
  * Optional prompt and response security with Model Armor protection
  * Centralized audit logging



For information about other MCP servers and information about security and governance controls available for Google Cloud MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

Remote MCP Servers are managed by Google and offer additional security and governance controls compared to local MCP Servers provided by [Cloud SQL for SQL Server MCP Toolbox for Databases](https://mcp-toolbox.dev/integrations/cloud-sql-mssql/source/). For more information about other remote MCP servers and about the security and governance controls available for MCP, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

The following sections only apply to the Cloud SQL for SQL Server remote MCP server.

## Before you begin

### Required roles

To get the permissions that you need to use the Cloud SQL remote MCP server, ask your administrator to grant you the following IAM roles on the project where you want to use the remote Cloud SQL MCP server: 

  * Make MCP tool calls in a project: [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) 
  * Create a backup of a Cloud SQL instance: [Cloud SQL Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
  * Create an OAuth client ID: [OAuth Config Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.editor) (`roles/oauthconfig.editor`) 
  * Create, clone, restore from backup, or update a Cloud SQL instance: [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) 
  * Update a Cloud SQL user: [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) 
  * Create secrets and access secret versions in Secret Manager: [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) 
  * Execute SQL statements (including read-only) in Cloud SQL: 
    * [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)
    * [Cloud SQL Studio User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.StudioUser) (`roles/cloudsql.StudioUser`)
  * Get a Cloud SQL instance or list all Cloud SQL instances in a project: [Cloud SQL Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.viewer) (`roles/cloudsql.viewer`) 
  * Import data into a Cloud SQL instance: 
    * [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * List Cloud SQL users: [Cloud SQL Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.viewer) (`roles/cloudsql.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the Cloud SQL remote MCP server. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the Cloud SQL remote MCP server:

  * Make MCP tool calls: `mcp.tools.call`
  * Access a secret version in Secret Manager: `secretmanager.secretVersions.access`
  * Clone a Cloud SQL instance: `cloudsql.instances.clone`
  * Create a Cloud SQL instance: `cloudsql.instances.create`
  * Create a Cloud SQL backup: `cloudsql.backupRuns.create`
  * Execute SQL statements (including read-only) on a Cloud SQL instance: `cloudsql.instances.executeSql`
  * Get a Cloud SQL instance: `cloudsql.instances.get`
  * Get a Cloud SQL instance operation: `cloudsql.instances.get`
  * Import data to a Cloud SQL instance: `cloudsql.instances.import`
  * List Cloud SQL instances in a project: `cloudsql.instances.list`
  * List Cloud SQL users: `cloudsql.users.list`
  * Restore from Cloud SQL backup: 
    * `cloudsql.backupRuns.get`
    * `cloudsql.instances.restoreBackup`
  * Update a Cloud SQL instance: `cloudsql.instances.update`
  * Update a Cloud SQL user: `cloudsql.users.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure an MCP client to use the Cloud SQL MCP server

Host programs, such as Claude or the Gemini CLI, can instantiate MCP clients that connect to a single MCP server. A host program can have multiple clients that connect to different MCP servers. To connect to a remote MCP server, the MCP client must know at a minimum the URL of the remote MCP server.

Use the following instructions to configure MCP clients to connect to your remote Cloud SQL MCP server.

### Gemini CLI

To add a Cloud SQL remote MCP server to your Gemini CLI, configure it as an extension.

  1. Create an extension file in the following location: `~/.gemini/extensions/EXT_NAME/gemini-extension.json` where `~/` is your home directory and EXT_NAME is the name you want to give the extension.

  2. Save the following content in your extension file:
         
         {
                   "name": "EXT_NAME",
                   "version": "1.0.0",
                   "mcpServers": {
                     "Cloud SQL MCP Server": {
                       "httpUrl": "https://sqladmin.googleapis.com/mcp",
                       "authProviderType": "google_credentials",
                       "oauth": {
                         "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
                       },
                       "timeout": 30000,
                       "headers": {
                         "x-goog-user-project": "PROJECT_ID"
                       }
                     }
                   }
                 }
                 

  3. Save the extensions file.

  4. Start Gemini CLI:
         
         gemini
                 

  5. Run `/mcp` to view your configured MCP server and its tools.

The response is similar to the following:
         
         Configured MCP servers:
                 🟢 Cloud SQL MCP Server (from sqladmin )
                   - list_instances
                   - get_instance
                   - clone_instance
                   - create_instance
                   - update_instance
                   - execute_sql
                   - execute_sql_readonly
                   - get_operation
                   - create_user
                   - update_user
                   - list_users
                   - create_backup
                   - restore_backup
                   - import_data
                   - postgres_upgrade_precheck
                 




The remote MCP server is ready to use in Gemini CLI.

### Antigravity

To configure the Cloud SQL remote MCP server for use with [Antigravity](https://antigravity.google/docs/get-started), use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

#### Authenticate to the Google Cloud project

  1. Sign in to Google Cloud using ADC by running the following command. 
         
         gcloud auth application-default login
             

  2. Copy the generated URL and token into a browser window.
  3. A sign-in screen appears. Choose the account that has permissions to call MCP tools and use the remote MCP server. After you sign in, your credentials are stored in the local credential file used by ADC. 



#### Add the remote MCP server to Antigravity

  1. Open Antigravity.
  2. In the **Agent** pane, click more_horiz to open the **Additional options** menu, and select **MCP servers**.
  3. In the **MCP Store** window, select **Manage MCP Servers**. In the main editor window, the **Manage MCP servers** pane appears.
  4. In the **Manage MCP servers** pane, click **View raw config** to open a tab with the `mcp_json.config` file.
  5. Add the following configuration to the `mcp_config.json` file: 
         
         {
              "mcpServers": {
                 "cloud-sql": {
                    "serverUrl": "https://sqladmin.googleapis.com/mcp",
                     "authProviderType": "google_credentials",
                     "disabled": false
               }
             }
           }

  6. Return to the **Manage MCP servers** pane, and click **Refresh**. A list of available tools for the Cloud SQL remote MCP server appears. 
  7. In the **Agent** pane, enter a prompt for the agent that uses the remote Cloud SQL MCP server. For example: 
         
         List the Cloud SQL instances in the project.

  8. Verify that the agent is using `list_instances` tool from the Cloud SQL remote MCP server. In the **Agent** pane, you can see the agent's work include the following: 

`MCP tool: cloud-sql/list_instance`




### Claude.ai

You must have the Claude Enterprise, Pro, Max, or Team plan to configure Google and Google Cloud MCP servers in Claude.ai. For pricing information, see [Claude Pricing](https://claude.com/pricing).

To add a Google or Google Cloud remote MCP server to Claude.ai, configure a custom connector with a OAuth client ID and OAuth client secret:

#### Create an Oauth 2.0 client ID and secret

  1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/use-cloudsql-mcp)

You are prompted to create a project if you don't have one selected.

  2. In the **Application type** list, select **Web application**.

  3. In the **Name** field, enter a name for your application.

  4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then add `https://claude.ai/api/mcp/auth_callback` in the **URIs** field.

  5. Click **Create**. The client is created. To access the client ID, in the Google Cloud console, go to **Google Auth Platform > Clients**.

  6. In the **OAuth 2.0 client IDs** list, select the client name.

  7. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.



#### Create a custom connector in Claude.ai

Follow the instructions for the Claude plan that you're using:

### Enterprise and Team

  1. In Claude.ai, navigate to **Admin settings > Connectors**.

  2. Click **Add custom connector**.

  3. In the **Add custom connector** dialog, enter the following:

     * **Server name** : a human readable name for the server.
     * **Remote MCP server URL** : `https://sqladmin.googleapis.com/mcp`
  4. Expand the **Advanced settings** menu and then enter the following:

     * **OAuth client ID** : the OAuth 2.0 client ID you created.
     * **OAuth client secret** : the secret for your OAuth 2.0 client. To retrieve the secret, go to **Google Auth Platform > Clients** and then select the OAuth client ID you created. In the **Client secrets** section, click to copy the **Client secret**.
  5. Click **Add**.

The custom connector is created.

  6. Open the **Tools** menu and enable the connector.

Claude.ai can use the MCP server.




### Pro and Max

  1. In Claude.ai, navigate to **Settings > Connectors**.

  2. Click **Add custom connector**.

  3. In the **Add custom connector** dialog, enter the following:

     * **Server name** : a human readable name for the server.
     * **Remote MCP server URL** : `https://sqladmin.googleapis.com/mcp`
  4. Expand the **Advanced settings** menu and then enter the following:

     * **OAuth client ID** : the OAuth 2.0 client ID you created.
     * **OAuth client secret** : the secret for your OAuth 2.0 client. To retrieve the secret, go to **Google Auth Platform > Clients** and then select the OAuth client ID you created. In the **Client secrets** section, click to copy the **Client secret**.
  5. Click **Add**.

The custom connector is created.

  6. Open the **Tools** menu and enable the connector.

Claude.ai can use the MCP server.




### ChatGPT

You must have a [ChatGPT Business subscription](https://chatgpt.com/business/) to use Google and Cloud SQL MCP servers with ChatGPT.

To add a Google or Cloud SQL remote MCP server to ChatGPT, create a Google OAuth 2.0 client ID and secret, and then add the MCP server as an App in ChatGPT.

#### Create an Oauth 2.0 client ID and secret

  1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/use-cloudsql-mcp)

You are prompted to create a project if you don't have one selected.

  2. In the **Application type** list, select **Web application**.

  3. In the **Name** field, enter a name for your application.

  4. In the **Authorized JavaScript origins** section, click **\+ Add URI** , and then add `https://chatgpt.com` in the **URIs** field.

  5. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then add `https://chatgpt.com/connector_platform_oauth_redirect` in the **URIs** field.

  6. Click **Create**. The client is created. To access the client ID, in the Google Cloud console, go to **Google Auth Platform > Clients**.

  7. In the **OAuth 2.0 client IDs** list, select the client name.

  8. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.



#### Add the MCP server as an app in ChatGPT

  1. Sign in to ChatGPT.
  2. Turn on Developer mode: 
     1. In ChatGPT, click your username to open the **Profile menu** , and then select **Settings**.
     2. In the Settings menu, select **Apps** , and then click **Advanced settings**.
     3. In the **Advanced settings** , click the **Developer mode** toggle to the on position.
  3. In **Settings** > **Apps** , click the **Create app** button.
  4. In the **New app** dialog, enter the following information: 
     * **Name** : the name of the MCP server.
     * **Description** : an optional description of the MCP server.
     * **MCP server URL** : `https://sqladmin.googleapis.com/mcp`
     * **Authentication** : 
       * In the **Authentication** menu, select **OAuth**.
       * In the **OAuth client ID** field, enter your Google OAuth client ID.
       * In the **OAuth secret** field, enter your Google OAuth client secret.
     * Confirm that you understand the risk associated with MCP server use, and then click **Create**.



The MCP server is displayed in the **Apps** menu, and is ready for use through chat prompts.

## General guidance for MCP clients

If your MCP client isn't listed in Configure an MCP client to use the Cloud SQL MCP server, then you use the following information to connect to a remote MCP server in your host program or AI application. You are prompted to enter details about the server, such as its name and URL.

For the Cloud SQL remote MCP server, enter the following as required:

  * **Server name** : Cloud SQL MCP server
  * **Server URL** or **Endpoint** : https://sqladmin.googleapis.com/mcp (or a specialized toolset URL)
  * **Transport** : [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http)
  * **Authentication details** : Depending on how you want to authenticate, you can enter your Google Cloud credentials, your OAuth Client ID and secret, or an agent identity and credentials. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).
  * **OAuth scope** : the [OAuth 2.0 scope](https://developers.google.com/identity/protocols/oauth2/scopes) that you want to use when connecting to the Cloud SQL MCP server.



### Authentication and authorization

Cloud SQL MCP servers use the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) for authentication and authorization. All [Google Cloud identities](https://docs.cloud.google.com/docs/authentication/identity-products) are supported for authentication to MCP servers.

The Cloud SQL remote MCP server doesn't accept API keys.

We recommend creating a separate identity for agents using MCP tools so that access to resources can be controlled and monitored. For more information on authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

### Cloud SQL MCP OAuth scopes

OAuth 2.0 uses scopes and credentials to determine if an authenticated principal is authorized to take a specific action on a resource. For more information about OAuth 2.0 scopes at Google, read [Using OAuth 2.0 to access Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes).

Cloud SQL has the following MCP tool OAuth scopes:

Scope URI for gcloud CLI | Description  
---|---  
`https://www.googleapis.com/auth/cloud-platform` | Create, update, and list Cloud SQL resources including instances and database users. Import data and execute SQL statements on Cloud SQL instances.  
`https://www.googleapis.com/auth/cloudsql` | Create, update, and list Cloud SQL resources including instances and database users. Import data and execute SQL statements on Cloud SQL instances. You can use this scope in addition to or instead of the broader platform-wide scope.  
`https://www.googleapis.com/auth/cloudsql.readonly` | View Cloud SQL resources and the data in Cloud SQL instances. You can use this scope for executing read-only SQL statements.  
  
Additional scopes might be required on the resources accessed during a tool call. To view a list of scopes required for Cloud SQL, see [Cloud SQL Admin API](https://developers.google.com/identity/protocols/oauth2/scopes#sqladmin).

## Available toolsets

The Cloud SQL remote MCP server provides specialized endpoint URLs (toolsets) that expose specific subsets of tools depending on your security and workflow requirements. You can configure your MCP client to connect to any of the following toolset URLs:

  * **All tools** : `https://sqladmin.googleapis.com/mcp` Exposes all available tools for the remote MCP server.

  * **Read-only** : `https://sqladmin.googleapis.com/mcp/readonly` Exposes read-only tools:

    * `get_instance`
    * `get_operation`
    * `list_instances`
    * `list_users`
    * `execute_sql_readonly`
  * **Instance management** : `https://sqladmin.googleapis.com/mcp/instance_manage` Exposes tools for creating, modifying, and managing Cloud SQL instances:

    * `clone_instance`
    * `create_instance`
    * `get_instance`
    * `get_operation`
    * `list_instances`
    * `update_instance`
  * **Query execution** : `https://sqladmin.googleapis.com/mcp/query_execution` Exposes tools for executing SQL statements:

    * `execute_sql`
    * `get_operation`



## Available tools

  * `clone_instance`: creates a Cloud SQL instance as a clone of source instance.
  * `create_backup`: creates a backup of a Cloud SQL instance.
  * `create_instance`: initiates the creation of a Cloud SQL instance. 
  * `execute_sql`: executes any valid SQL statements (DDL, DCL, DQL, DML) on a Cloud SQL instance.
  * `execute_sql_readonly`: executes any valid read-only SQL statement on a Cloud SQL instance.
  * `get_instance`: gets the details of a Cloud SQL instance.
  * `get_operation`: gets the status of a long-running operation in Cloud SQL.
  * `import_data`: imports data into a Cloud SQL instance from Cloud Storage.
  * `list_instances`: lists all Cloud SQL instances in a project.
  * `list_users`: lists all database users for a Cloud SQL instance.
  * `restore_backup`: restores a backup of a Cloud SQL instance.
  * `update_instance`: updates supported settings of a Cloud SQL instance.
  * `update_user`: updates a database user for a Cloud SQL instance.



To view additional details of available MCP tools and their descriptions for the Cloud SQL remote MCP server, see the [Cloud SQL MCP reference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp).

### List tools

Use the [MCP inspector](https://modelcontextprotocol.io/docs/tools/inspector) to list tools, or send a `tools/list` HTTP request directly to the Cloud SQL remote MCP server. The `tools/list` method doesn't require authentication.
    
    
    curl -X POST https://sqladmin.googleapis.com/TOOLSET_ENDPOINT \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
        -H 'MCP-Protocol-Version: MCP_PROTOCOL_VERSION' \
        -H 'Mcp-Method: tools/list' \
        -d '{
          "jsonrpc": "2.0",
          "id": 1,
          "method": "tools/list",
          "params": {
            "_meta": {
              "io.modelcontextprotocol/protocolVersion": "MCP_PROTOCOL_VERSION",
              "io.modelcontextprotocol/clientCapabilities": {
                "extensions": {
                  "io.modelcontextprotocol/ui": {
                    "mimeTypes": ["text/html;profile=mcp-app"]
                  }
                }
              }
            }
          }
        }'
    

Replace the following:

  * `TOOLSET_ENDPOINT`: The remainder of the MCP endpoint after the service name. For example, for Cloud SQL, this might be `mcp/toolset-name`.
  * `MCP_PROTOCOL_VERSION`: The MCP protocol version. For example, `2026-07-28`.



### Create an instance

By default, when you create a Cloud SQL instance using the [`create_instance` tool](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/create_instance), the instance is configured with a public IP address.

To create an instance with a private IP address, you can create an instance enabled with either [private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access) or [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect). When you create an instance with a private IP address, its public IP address is disabled automatically.

To enable private services access, a private services access connection must already be available to the project where you're creating the Cloud SQL instance. To enable Private Service Connect, a Private Service Connect endpoint must already exist in a project that's accessible to the Cloud SQL instance that you're creating.

### Update an instance

The `update_instance` tool lets you make the following updates to your Cloud SQL instance:

  * Change the [edition](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro) and [tier](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview) of your instance
  * Enable or disable [data cache](https://docs.cloud.google.com/sql/docs/sqlserver/data-cache)
  * Enable or disable the [public IP address](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip) configuration for your instance
  * Enable or disable [private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access)
  * Enable or disable [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect)



### Execute SQL statements

The remote Cloud SQL MCP server provides two separate tools for executing SQL statements. You can use the `execute_sql` tool to administer and make changes to your database. For executing read-only SQL statements, such as querying data, you can use the `execute_sql_readonly` tool.

In both cases, to execute the SQL statements, your Cloud SQL instance must meet the following requirements:

  * The `data_api_access` configuration setting on the instance must be set to the value `ALLOW_DATA_API`. When you create an instance using the `create_instance` tool, the `data_api_access` configuration setting is configured automatically.
  * To authenticate, use a [built-in database user](https://docs.cloud.google.com/sql/docs/sqlserver/built-in-authentication) account. Store the user's password in a [regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret) in Secret Manager in the same region as your Cloud SQL instance, and specify both `user` and `password_secret_version` when calling the tool.



If the `data_api_access` configuration setting for the instance isn't set to `ALLOW_DATA_API`, then use the [`update_instance` tool](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/update_instance) to update the configuration for the instance.

#### sqlcommenter tags

When executing queries using the `execute_sql` or `execute_sql_readonly` tool, set the optional `sql_commenter_enabled` parameter to `true` to append [sqlcommenter](https://google.github.io/sqlcommenter/) tags to the SQL statements for database observability and telemetry. The appended comment includes the following tags:

  * `mcp.tool`: the name of the MCP tool called.
  * `mcp.server`: the identity of the remote MCP server (`Remote MCP Server`).
  * `user.identity`: the authenticated database or IAM user identity executing the query.
  * `mcp.client`: the identified AI client or application agent (for example, Claude, Gemini, or Antigravity).



These default tags are the only supported tags, and no other tags can be added.

You can view the executed queries and their appended sqlcommenter tags in [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/sqlserver/manage-data-using-studio) or in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) by viewing your database query and audit logs.

## Sample use cases

The following are sample use cases for the Cloud SQL MCP server:

### Web application development

A sample use case might be the rapid development of web applications and the provisioning of Cloud SQL instances as their source database. In this use case, using the Cloud SQL MCP server lets you build a new database and populate it with initial data for a new project using natural language.

**Sample prompt:**
    
    
    "Create a new SQL Server development instance and set up a table called products."
    

**Workflow:**

The workflow for setting up a web application might look like the following:

  * **Provisioning** : The agent calls the `create_instance` tool to create a new Cloud SQL instance with development environment-sized specifications.

  * **Verification** : The agent uses the `get_operation` tool to poll the status of the instance creation operation.

  * **Connection** : When the operation is complete, the agent uses the `get_instance` tool to retrieve the instance connection metadata.

  * **Schema setup** : When ready, the agent uses the `execute_sql` to run the `CREATE TABLE products` SQL statement.

  * **Data seeding** : The agent uses `execute_sql` again to insert initial seed data (DML) into the newly created table.

  * **Data seeding** : When ready, the agent uses the `import_data` to import a data file from Cloud Storage of products.




### Query a database using natural language

You can query a Cloud SQL database, update records, and make schema updates using natural language.

**Sample prompt** :
    
    
    "Add a `stock_count` column to the inventory table."
    

**Workflow** : The workflow for querying a database with natural language might look like the following.

  * **Schema migration** : The agent calls `execute_sql` to run an `ALTER TABLE` statement, adding the new `stock_count` column to the database schema.

  * **Validation** : The agent uses `get_instance` to confirm that the instance update has successfully completed.




**Sample prompt** :
    
    
    "Show me a list of shoes that are priced above $100 from the inventory table."
    

**Workflow:**

  * **Query execution** : The agent calls `execute_sql` to run the SQL statement that retrieves the data.



## Limitations

The Cloud SQL remote MCP server has the following limitations:

  * If the `execute_sql` or `execute_sql_readonly` tool returns a response that's larger than 10 MB, then the response will be truncated.
  * When using the `execute_sql` or `execute_sql_readonly` tool, queries that run for longer than 30 seconds can time out.
  * Cloud SQL for SQL Server doesn't support the `create_user` tool.



## Optional security and safety configurations

MCP introduces new security risks and considerations due to the wide variety of actions that you can do with the MCP tools. To minimize and manage these risks, Google Cloud offers default settings and customizable policies to control the use of MCP tools in your Google Cloud organization or project.

For more information about MCP security and governance, see [AI security and safety](https://docs.cloud.google.com/mcp/ai-security-safety).

### Model Armor

[Model Armor](https://docs.cloud.google.com/model-armor/overview) is a Google Cloud service designed to enhance the security and safety of your AI applications. It works by proactively screening LLM prompts and responses, protecting against various risks and supporting responsible AI practices. Whether you are deploying AI in your cloud environment, or on external cloud providers, Model Armor can help you prevent malicious input, verify content safety, protect sensitive data, maintain compliance, and enforce your AI safety and security policies consistently across your diverse AI landscape.

When Model Armor is enabled with [logging enabled](https://docs.cloud.google.com/model-armor/configure-logging), Model Armor logs the entire payload. This might expose sensitive information in your logs.

#### MCP request routing to Model Armor

Model Armor is available in [certain regions](https://docs.cloud.google.com/model-armor/locations). When Model Armor is enabled and you use an MCP server in a jurisdiction that Model Armor doesn't support, the routing behavior of the call might be different for different MCP servers and might break data residency compliance for in-use and in-transit data. For more information about the behavior of individual MCP servers, see [Model Armor supported products](https://docs.cloud.google.com/mcp/model-armor-supported-products). 

#### Enable Model Armor

You must enable Model Armor APIs before you can use Model Armor.

###  Console 

  1. Enable the Model Armor API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=modelarmor.googleapis.com)

  2. Select the project where you want to activate Model Armor.




###  gcloud 

Before you begin, follow these steps using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) with the Model Armor API:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following command to set the API endpoint for the Model Armor service.
         
         gcloud config set api_endpoint_overrides/modelarmor "https://modelarmor.LOCATION.rep.googleapis.com/"

Replace `LOCATION` with the region where you want to use Model Armor.




#### Configure protection for Google and Google Cloud remote MCP servers

To help protect your MCP tool calls and responses you can use Model Armor floor settings. A floor setting defines the minimum security filters that apply across the project. This configuration applies a consistent set of filters to all MCP tool calls and responses within the project.

**Tip:** Don't enable the prompt injection and jailbreak filter unless your MCP traffic carries natural language data.

Set up a Model Armor floor setting with MCP sanitization enabled. For more information, see [Configure Model Armor floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings).

**Note:** If the agent and the MCP server are in different projects, you can create floor settings in both projects (the client project and the resource project). In this case, Model Armor is invoked twice, once for each project.

See the following example command:
    
    
    gcloud model-armor floorsettings update \
    --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
    --enable-floor-setting-enforcement=TRUE \
    --add-integrated-services=GOOGLE_MCP_SERVER \
    --google-mcp-server-enforcement-type=INSPECT_AND_BLOCK \
    --enable-google-mcp-server-cloud-logging \
    --malicious-uri-filter-settings-enforcement=ENABLED \
    --add-rai-settings-filters='[{"confidenceLevel": "MEDIUM_AND_ABOVE", "filterType": "DANGEROUS"}]'

Replace `PROJECT_ID` with your Google Cloud project ID.

Note the following settings:

  * `INSPECT_AND_BLOCK`: The enforcement type that inspects content for the Google MCP server and blocks prompts and responses that match the filters.
  * `ENABLED`: The setting that enables a filter or enforcement.
  * `MEDIUM_AND_ABOVE`: The confidence level for the Responsible AI - Dangerous filter settings. You can modify this setting, though lower values might result in more false positives. For more information, see [Model Armor confidence levels](https://docs.cloud.google.com/model-armor/overview#ma-confidence-levels).



#### Disable scanning MCP traffic with Model Armor

To stop Model Armor from automatically scanning traffic to and from Google MCP servers based on the project's floor settings, run the following command:
    
    
    gcloud model-armor floorsettings update \
      --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
      --remove-integrated-services=GOOGLE_MCP_SERVER
    

Replace `PROJECT_ID` with the Google Cloud project ID. Model Armor doesn't automatically apply the rules defined in this project's floor settings to any Google MCP server traffic.

Model Armor floor settings and general configuration can impact more than just MCP. Because Model Armor integrates with services like Vertex AI, any changes you make to floor settings can affect traffic scanning and safety behaviors across all integrated services, not just MCP.

### Control MCP use with IAM policies

Identity and Access Management (IAM) [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) and [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies) help you secure Google Cloud and Google MCP servers.

You can combine multiple criteria to build customized security and governance policies by allowing or denying access based on the following:

  * The principal.
  * Tool properties like the read-only attribute.
  * The service name or tool name.
  * The application's OAuth client ID.



For more information, see [Control MCP use with Identity and Access Management](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

## What's next

  * Read the [Cloud SQL MCP tools documentation](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp).
  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).
  * Learn about other [remote MCP servers](https://docs.cloud.google.com/mcp/supported-products).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
