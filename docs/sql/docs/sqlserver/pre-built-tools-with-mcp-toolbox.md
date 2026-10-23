---
url: https://docs.cloud.google.com/sql/docs/sqlserver/pre-built-tools-with-mcp-toolbox/
title: Use Cloud SQL for SQL Server with MCP, Gemini CLI, and other agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:32.390789+00:00
---

# Use Cloud SQL for SQL Server with MCP, Gemini CLI, and other agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/pre-built-tools-with-mcp-toolbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Use Cloud SQL for SQL Server with MCP, Gemini CLI, and other agents Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/pre-built-tools-with-mcp-toolbox "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/pre-built-tools-with-mcp-toolbox "View this page for the PostgreSQL database engine") | SQL Server

This page shows you how to connect your Cloud SQL instance to various AI developer assistance tools, including the following:

  * Gemini CLI extension for Cloud SQL for SQL Server
  * Gemini CLI extension for SQL Server


  * Gemini Code Assist
  * Claude code
  * Claude desktop
  * Codex
  * Cline (VS Code extension)
  * Cursor
  * Visual Studio Code (Copilot)
  * Windsurf (Codeium)
  * Antigravity



For an integrated experience, we recommend using the dedicated [Gemini CLI extension for Cloud SQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/pre-built-tools-with-mcp-toolbox#use-gemini-cli-extensions-in-cloud-sql).

As Google Cloud's next-generation command-line interface, Gemini CLI bundles the underlying skills directly into the extension, which simplifies setup and configuration. You can configure Gemini Code Assist to use the Gemini CLI, offering similar setup benefits in your IDE.

For other developer tools that support the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), you can connect by manually configuring the [MCP Toolbox for Databases (Toolbox)](https://github.com/googleapis/mcp-toolbox). Toolbox is an open-source MCP server that connects AI agents to your data by managing tasks such as authentication and connection pooling. This lets you interact with your data using natural language directly from your IDE. For these tools, this method provides core database interaction capabilities.

For more information, see [Prebuilt tools](https://mcp-toolbox.dev/documentation/configuration/prebuilt-configs/) and [MCP Toolbox for Databases on GitHub](https://github.com/googleapis/mcp-toolbox/pull/1495/files).

## About Gemini CLI and extensions

Gemini CLI is an open-source AI agent designed to assist with development workflows by assisting with coding, debugging, data exploration, and content creation. It provides an agentic interface for interacting with database and analytics services and popular open-source databases.

## How extensions work

Gemini CLI is highly extensible, allowing for the addition of new tools and capabilities through extensions. You can load the extensions from a GitHub URL, a local directory, or a configurable registry. They provide new tools, slash commands, skills, and prompts to assist with your workflow.

## Use the Gemini CLI extensions in Cloud SQL for SQL Server

The Cloud SQL Gemini CLI extension is based on MCP Toolbox for Databases.

The integration with Gemini CLI is through a dedicated extension that offers additional capabilities compared to the standard Toolbox connection. The extension offers a streamlined installation process and a set of skills based on MCP Tools.

For more information, see GitHub documentation for the [Gemini CLI extension for Cloud SQL for SQL Server](https://github.com/gemini-cli-extensions/cloud-sql-sqlserver). 

### Gemini CLI extension for Cloud SQL for SQL Server databases

The `cloud-sql-sqlserver` extension includes skills for querying the database and monitoring database health. 

For all available skills, see the [Cloud SQL skills on GitHub](https://github.com/gemini-cli-extensions/cloud-sql-sqlserver/tree/main/skills) The `cloud-sql-sqlserver-observability` extension provides a unified interface for managing and monitoring database performance and health directly from the Gemini CLI.

Category | Tools  
---|---  
Observability | 

  * `get_system_metrics`: Retrieves system metrics for a Cloud SQL instance.

  
  
### Gemini CLI extension for SQL Server databases

For a list of those operations, see [MCP Toolbox for Databases](https://mcp-toolbox.dev/integrations/mssql/prebuilt-configs/) and [Gemini CLI extension for SQL Server](https://github.com/gemini-cli-extensions/sql-server).

## Before you begin

  * In the Google Cloud console, on the [project selector page](https://console.cloud.google.com/projectselector2/home/dashboard), select or create a Google Cloud project.

  * [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

  * [Enable the Cloud SQL Admin API in the Google Cloud project](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=%7Bconsole_url%7D).

  * By default, Cloud SQL assigns a public IP address to a new instance. Depending on your use case, make sure either a [Public IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip) or [Private IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip) is set up for your Cloud SQL instances. Toolbox connects securely using the [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/language-connectors).

  * Grant the necessary [Identity and Access Management (IAM)](https://docs.cloud.google.com/sql/docs/sqlserver/roles-and-permissions) roles to the user that will be running the MCP server. The tools available depends on the roles granted:

Task | Role name | Required IAM role  
---|---|---  
Provides read-only access to resources, including the following operations: 
    * `get_instance`
    * `list_instances`
    * `list_databases`
    * `wait_for_operation`
| Cloud SQL Viewer | `roles/cloudsql.viewer`  
Provides read-only access to monitoring data such as time series metrics. | Cloud Monitoring Viewer | `roles/monitoring.viewer`  
Provides permissions to manage existing resources, including the following: 
    * All `viewer` tools
    * `create_database`
| Cloud SQL Editor | `roles/cloudsql.editor`  
Provides full control over all resources, including the following: 
    * All `viewer` and `editor` tools
    * `create_instance`
    * `create_user`
| Cloud SQL Admin | `roles/cloudsql.admin`  
  * Configure [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) for your environment.

  * Create or reuse [a database user](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users), and have the username and password ready.




## Connect with Antigravity

You can connect Cloud SQL for SQL Server to Antigravity in the following ways:

  * Use the MCP Store
  * Use a custom configuration

**Note:** You don't need to download the MCP Toolbox binary to use these methods.

### MCP Store

The most recommended method to connect to Cloud SQL for SQL Server in Antigravity is to use the built-in MCP Store.

  1. Open [Antigravity](https://antigravity.google/docs/mcp) and open the editor's **agent panel**.
  2. Click the **"..."** icon at the top of the panel and select **MCP Servers**.
  3. Locate **Cloud SQL for SQL Server** in the list of available servers and click **Install**.
  4. Follow the on-screen prompts to securely link your accounts where applicable.



After you install Cloud SQL for SQL Server in the MCP Store, resources and tools from the server are automatically available to the editor.

### Custom configuration

To connect to a custom MCP server, follow these steps:

  1. Open [Antigravity](https://antigravity.google/docs/mcp) and open the editor's **agent panel**.
  2. Click the **"..."** icon at the top of the panel and select **MCP Servers**.
  3. Click **Manage MCP Servers > View raw config** to open the `mcp_config.json` file.
  4. Add the following configuration, replace the environment variables with your values, and save.


    
    
    {
      "mcpServers": {
        "cloud-sql-mssql": {
          "command": "npx",
          "args": ["-y","@toolbox-sdk/server","--prebuilt","cloud-sql-mssql","--stdio"],
          "env": {
              "CLOUD_SQL_MSSQL_PROJECT": "PROJECT_ID",
              "CLOUD_SQL_MSSQL_REGION": "REGION",
              "CLOUD_SQL_MSSQL_INSTANCE": "INSTANCE_ID",
              "CLOUD_SQL_MSSQL_DATABASE": "DATABASE_NAME",
              "CLOUD_SQL_MSSQL_USER": "USER_ID",
              "CLOUD_SQL_MSSQL_PASSWORD": "PASSWORD"
          }
        }
      }
    }
    

Once you configure the custom MCP server, the resources and tools from the Cloud SQL for SQL Server server are available to the editor.

## Install the MCP Toolbox

**Note:** This step isn't required for Gemini CLI extensions.

  1. Download the binary that corresponds to your operating system and CPU architecture. 

### linux/amd64
         
         curl -O https://storage.googleapis.com/genai-toolbox/v0.7.0/linux/amd64/toolbox

### darwin/arm64
         
         curl -O https://storage.googleapis.com/genai-toolbox/v0.7.0/darwin/arm64/toolbox

### darwin/amd64
         
         curl -O https://storage.googleapis.com/genai-toolbox/v0.7.0/darwin/amd64/toolbox

### windows/amd64
         
         curl -O https://storage.googleapis.com/genai-toolbox/v0.7.0/windows/amd64/toolbox

  2. Make the binary executable: 
         
         chmod +x toolbox

  3. Verify the installation using the following command: 
         
         ./toolbox --version




## Configure the MCP Client

This section describes how to configure various developer tools to connect to your Cloud SQL instance using [Toolbox](https://github.com/googleapis/mcp-toolbox). Toolbox acts as an open-source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that sits between your IDE and your database, providing a secure and efficient control plane for your AI tools. Select the tab for your specific tool to see the configuration instructions.

### Gemini CLI for Cloud SQL for SQL Server

  


  1. Install the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#quickstart).
  2. Install the Cloud SQL for SQL Server extension for Gemini CLI from the GitHub repository using the following command: 
         
         gemini extensions install https://github.com/gemini-cli-extensions/cloud-sql-sqlserver

While installing the extension, replace the following: 
         
         export CLOUD_SQL_MSSQL_PROJECT="PROJECT_NAME"
         export CLOUD_SQL_MSSQL_REGION="REGION"
         export CLOUD_SQL_MSSQL_INSTANCE="INSTANCE_NAME"
         export CLOUD_SQL_MSSQL_DATABASE="DATABASE_NAME"
         export CLOUD_SQL_MSSQL_USER="DATABASE_USER_NAME"
         export CLOUD_SQL_MSSQL_PASSWORD="PASSWORD"
         export CLOUD_SQL_MSSQL_IP_TYPE="IP_TYPE"
         

Replace the following: 
     * PROJECT_NAME: The Google Cloud project ID.
     * REGION: The region of your Cloud SQL instance.
     * INSTANCE_NAME: The ID of your Cloud SQL instance.
     * DATABASE_NAME: The name of the database to connect to.
     * DATABASE_USER_NAME: Optional: The database username. Defaults to IAM authentication if unspecified.
     * PASSWORD: Optional: The password for the database user. Defaults to IAM authentication if unspecified.
     * IP_TYPE: Optional: The IP type, such as "Public" (default) or "Private".
  3. Start the Gemini CLI in interactive mode: 
         
         gemini

The CLI automatically loads the Gemini CLI extension for Cloud SQL and its tools, which you can use to interact with your database.

In the Gemini CLI, use the [`/extensions`](https://github.com/google-gemini/gemini-cli/blob/bbcc90613390e4d3d3aed911fbc1535af80d643b/docs/cli/commands.md) command to verify the extension is installed and [`/mcp list`](https://github.com/google-gemini/gemini-cli/blob/bbcc90613390e4d3d3aed911fbc1535af80d643b/docs/cli/commands.md) command to see the tools.




### Gemini CLI for SQL Server

  


  1. Install the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#quickstart).
  2. Install the SQL Server software extension for Gemini CLI from the GitHub repository using the following command: 
         
         gemini extensions install https://github.com/gemini-cli-extensions/sql-server

While installing the extension, replace the following: 
         
         export MSSQL_HOST="HOST"
         export MSSQL_PORT="PORT"
         export MSSQL_DATABASE="DATABASE"
         export MSSQL_USER="USER"
         export MSSQL_PASSWORD="PASSWORD"
         

Replace the following: 
     * HOST: The hostname or IP address of the SQL Server server.
     * PORT: The port number for the SQL Server server.
     * DATABASE: The name of the database to connect to.
     * USER: The database username.
     * PASSWORD: The password for the database user.
  3. Start the Gemini CLI in interactive mode: 
         
         gemini

The CLI automatically loads the Gemini CLI extension for SQL Server and its tools, which you can use to interact with your database.




### Gemini Code Assist

  


  1. Install the [Gemini Code Assist](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist) extension in Visual Studio Code.
  2. Enable Agent Mode in Gemini Code Assist chat.
  3. In your working directory, create a folder named `.gemini`. Within it, create a `settings.json` file.
  4. Add the following configuration, replace the environment variables with your values, and then save: 
         
         {
           "mcpServers": {
             "cloud-sql-sqlserver": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","cloud-sql-mssql","--stdio"],
               "env": {
                 "CLOUD_SQL_MSSQL_PROJECT": "PROJECT_ID",
                 "CLOUD_SQL_MSSQL_REGION": "REGION",
                 "CLOUD_SQL_MSSQL_INSTANCE": "INSTANCE_ID",
                 "CLOUD_SQL_MSSQL_DATABASE": "DATABASE_NAME",
                 "CLOUD_SQL_MSSQL_IP_ADDRESS": "IP_ADDRESS",
                 "CLOUD_SQL_MSSQL_USER": "USER_ID",
                 "CLOUD_SQL_MSSQL_PASSWORD": "PASSWORD"
               }
             }
           }
         }
         
         




### Claude code

  


  1. Install [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).
  2. Set environment variables to connect to your Cloud SQL instance: 
         
         export CLOUD_SQL_MSSQL_PROJECT="PROJECT_NAME"
         export CLOUD_SQL_MSSQL_REGION="REGION"
         export CLOUD_SQL_MSSQL_INSTANCE="INSTANCE_NAME"
         export CLOUD_SQL_MSSQL_DATABASE="DATABASE_NAME"
         export CLOUD_SQL_MSSQL_USER="DATABASE_USER_NAME"
         export CLOUD_SQL_MSSQL_PASSWORD="PASSWORD"
         export CLOUD_SQL_MSSQL_IP_TYPE="IP_TYPE"
         

Replace the following: 
     * PROJECT_NAME: The Google Cloud project ID.
     * REGION: The region of your Cloud SQL instance.
     * INSTANCE_NAME: The ID of your Cloud SQL instance.
     * DATABASE_NAME: The name of the database to connect to.
     * DATABASE_USER_NAME: Optional: The database username. Defaults to IAM authentication if unspecified.
     * PASSWORD: Optional: The password for the database user. Defaults to IAM authentication if unspecified.
     * IP_TYPE: Optional: The IP type, such as "Public" (default) or "Private".
  3. Start the agent: 
         
         claude

  4. Install the plugin: 
         
         /plugin install cloud-sql-sqlserver@claude-plugins-official


**Tip:** Run `/plugin list` inside Claude Code to verify the plugin is active, or `/reload-plugins` if you just installed it. 

### Claude desktop

  


  1. Open [Claude Desktop](https://claude.ai/download) and navigate to **Settings**.
  2. Under the **Developer** tab, tap **Edit Config** to open the configuration file.
  3. Add the following to connect to the MCP server and set the environment variables: 
         
         {
           "mcpServers": {
             "cloud-sql-sqlserver": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","cloud-sql-mssql","--stdio"],
               "env": {
                 "CLOUD_SQL_MSSQL_PROJECT": "PROJECT_ID",
                 "CLOUD_SQL_MSSQL_REGION": "REGION",
                 "CLOUD_SQL_MSSQL_INSTANCE": "INSTANCE_ID",
                 "CLOUD_SQL_MSSQL_DATABASE": "DATABASE_NAME",
                 "CLOUD_SQL_MSSQL_IP_ADDRESS": "IP_ADDRESS",
                 "CLOUD_SQL_MSSQL_USER": "USER_ID",
                 "CLOUD_SQL_MSSQL_PASSWORD": "PASSWORD"
               }
             }
           }
         }
         
         

  4. Restart Claude Desktop. The new chat screen displays the MCP icon with the new MCP server available.



### Codex

  


  1. Install the Data Cloud Plugins marketplace: 
         
         codex plugin marketplace add GoogleCloudPlatform/data-cloud-plugins

  2. Install the plugin: 
         
         codex plugin install cloud-sql-sqlserver@data-cloud-plugins

  3. Configure the environment variables to connect to your Cloud SQL instance: 
         
         export CLOUD_SQL_MSSQL_PROJECT="PROJECT_NAME"
         export CLOUD_SQL_MSSQL_REGION="REGION"
         export CLOUD_SQL_MSSQL_INSTANCE="INSTANCE_NAME"
         export CLOUD_SQL_MSSQL_DATABASE="DATABASE_NAME"
         export CLOUD_SQL_MSSQL_USER="DATABASE_USER_NAME"
         export CLOUD_SQL_MSSQL_PASSWORD="PASSWORD"
         export CLOUD_SQL_MSSQL_IP_TYPE="IP_TYPE"
         

Replace the following: 
     * PROJECT_NAME: The Google Cloud project ID.
     * REGION: The region of your Cloud SQL instance.
     * INSTANCE_NAME: The ID of your Cloud SQL instance.
     * DATABASE_NAME: The name of the database to connect to.
     * DATABASE_USER_NAME: Optional: The database username. Defaults to IAM authentication if unspecified.
     * PASSWORD: Optional: The password for the database user. Defaults to IAM authentication if unspecified.
     * IP_TYPE: Optional: The IP type, such as "Public" (default) or "Private".
  4. Optional. Update the marketplace: 
         
         codex plugin marketplace upgrade data-cloud-plugins

  5. Run `codex plugin list` or use the `plugins` interactive menu to verify your installed plugins.



### Cline

  


  1. Open [Cline](https://github.com/cline/cline) extension in VS Code and tap **MCP Servers** icon.
  2. Tap **Configure MCP Servers** to open the configuration file.
  3. Add the following configuration, replace the environment variables with your values, and save: 
         
         {
           "mcpServers": {
             "cloud-sql-sqlserver": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","cloud-sql-mssql","--stdio"],
               "env": {
                 "CLOUD_SQL_MSSQL_PROJECT": "PROJECT_ID",
                 "CLOUD_SQL_MSSQL_REGION": "REGION",
                 "CLOUD_SQL_MSSQL_INSTANCE": "INSTANCE_ID",
                 "CLOUD_SQL_MSSQL_DATABASE": "DATABASE_NAME",
                 "CLOUD_SQL_MSSQL_IP_ADDRESS": "IP_ADDRESS",
                 "CLOUD_SQL_MSSQL_USER": "USER_ID",
                 "CLOUD_SQL_MSSQL_PASSWORD": "PASSWORD"
               }
             }
           }
         }
         
         

A green active status appears after the server connects successfully.



### Cursor

  


  1. Create `.cursor` directory in your project root if it does not exist.
  2. Create `.cursor/mcp.json` file if it does not exist and open it.
  3. Add the following configuration, replace the environment variables with your values, and save: 
         
         {
           "mcpServers": {
             "cloud-sql-sqlserver": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","cloud-sql-mssql","--stdio"],
               "env": {
                 "CLOUD_SQL_MSSQL_PROJECT": "PROJECT_ID",
                 "CLOUD_SQL_MSSQL_REGION": "REGION",
                 "CLOUD_SQL_MSSQL_INSTANCE": "INSTANCE_ID",
                 "CLOUD_SQL_MSSQL_DATABASE": "DATABASE_NAME",
                 "CLOUD_SQL_MSSQL_IP_ADDRESS": "IP_ADDRESS",
                 "CLOUD_SQL_MSSQL_USER": "USER_ID",
                 "CLOUD_SQL_MSSQL_PASSWORD": "PASSWORD"
               }
             }
           }
         }
         
         

  4. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects.



### Visual Studio Code (Copilot)

  


  1. Open [VS Code](https://code.visualstudio.com/docs/agents/overview) and create `.vscode` directory in your project root if it does not exist.
  2. Create `.vscode/mcp.json` file if it does not exist, and open it.
  3. Add the following configuration, replace the environment variables with your values, and save: 
         
         {
           "servers": {
             "cloud-sql-sqlserver": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","cloud-sql-mssql","--stdio"],
               "env": {
                 "CLOUD_SQL_MSSQL_PROJECT": "PROJECT_ID",
                 "CLOUD_SQL_MSSQL_REGION": "REGION",
                 "CLOUD_SQL_MSSQL_INSTANCE": "INSTANCE_ID",
                 "CLOUD_SQL_MSSQL_DATABASE": "DATABASE_NAME",
                 "CLOUD_SQL_MSSQL_IP_ADDRESS": "IP_ADDRESS",
                 "CLOUD_SQL_MSSQL_USER": "USER_ID",
                 "CLOUD_SQL_MSSQL_PASSWORD": "PASSWORD"
               }
             }
           }
         }
         
         




### Windsurf

  


  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to **Cascade assistant**.
  2. Tap MCP icon, then tap **Configure** to open the configuration file.
  3. Add the following configuration, replace the environment variables with your values, and save: 
         
         {
           "mcpServers": {
             "cloud-sql-sqlserver": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","cloud-sql-mssql","--stdio"],
               "env": {
                 "CLOUD_SQL_MSSQL_PROJECT": "PROJECT_ID",
                 "CLOUD_SQL_MSSQL_REGION": "REGION",
                 "CLOUD_SQL_MSSQL_INSTANCE": "INSTANCE_ID",
                 "CLOUD_SQL_MSSQL_DATABASE": "DATABASE_NAME",
                 "CLOUD_SQL_MSSQL_IP_ADDRESS": "IP_ADDRESS",
                 "CLOUD_SQL_MSSQL_USER": "USER_ID",
                 "CLOUD_SQL_MSSQL_PASSWORD": "PASSWORD"
               }
             }
           }
         }
         
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
