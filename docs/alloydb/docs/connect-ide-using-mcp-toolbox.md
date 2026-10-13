---
url: https://docs.cloud.google.com/alloydb/docs/connect-ide-using-mcp-toolbox/
title: Use AlloyDB for PostgreSQL with MCP, Gemini CLI, and other agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:55.366572+00:00
---

# Use AlloyDB for PostgreSQL with MCP, Gemini CLI, and other agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/connect-ide-using-mcp-toolbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Use AlloyDB for PostgreSQL with MCP, Gemini CLI, and other agents Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to connect your AlloyDB instance to various agents that support the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction).

We recommend using the dedicated AlloyDB extension for [Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli). The Gemini CLI integrates the underlying MCP server directly into the extension, so you don't need to perform a separate server setup. You can configure Gemini Code Assist to use the Gemini CLI, offering similar setup benefits in your IDE.

Alternatively, other IDEs and agents supporting the MCP can connect through [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox). Toolbox is an open-source MCP server designed to connect AI agents to your data. It handles tasks like authentication and connection pooling, letting you interact with your data with natural language directly from your IDE.

## Before you begin

To connect to your AlloyDB instance and use the available tools, you must have one of the following Identity and Access Management (IAM) roles, or a custom role with equivalent permissions:

Task | Role name | Required Identity and Access Management (IAM) role  
---|---|---  
Use read-only tools to list and get AlloyDB resources | AlloyDB Viewer | `roles/alloydb.viewer`  
Connect to an instance and run queries | [Cloud AlloyDB Client](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect#required-iam-permissions) | `roles/alloydb.client`  
Service Usage Consumer | `roles/serviceusage.serviceUsageConsumer`  
Perform administrative tasks (such as creating or managing clusters, instances, and users) | AlloyDB Admin | `roles/alloydb.admin`  
Use the observability extension | Monitoring Viewer | `roles/monitoring.viewer`  
  
Before you can connect to your AlloyDB instance, complete the following steps to set up your project and database.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud APIs necessary to create and connect to AlloyDB.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com,servicenetworking.googleapis.com)

     1. In the **Confirm project** step, click **Next** to confirm the name of the project you are going to make changes to.

     2. In the **Enable APIs** step, click **Enable** to enable the following:

        * AlloyDB API
        * Compute Engine API
        * Cloud Resource Manager API
        * Service Networking API

The Service Networking API is required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in the same Google Cloud project as AlloyDB. 

The Compute Engine API and Cloud Resource Manager API are required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in a different Google Cloud project.

  7. [Create or select a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect).
  8. Configure [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) for your environment.
  9. Create or reuse a [database user](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles). Be ready to enter the username and password.



## Use the Gemini CLI extensions for AlloyDB

Gemini CLI is an open-source AI agent designed to assist with development workflows by assisting with coding, debugging, data exploration, and content creation. Its mission is to provide an agentic interface for interacting with Data Cloud services and popular open-source databases.

The integration with Gemini CLI is through dedicated extensions that offer additional capabilities compared to a standard MCP Toolbox connection. The following sections describe the `alloydb` and `alloydb-observability` extensions, which offer an installation process and a set of tools. The open-source extensions contains detailed information on installation, configuration, and usage examples. For more information, see the [Gemini CLI Extension - AlloyDB for PostgreSQL](https://github.com/gemini-cli-extensions/alloydb).

### AlloyDB extension

The `alloydb` extension includes tools for querying the database, managing AlloyDB resources, and monitoring database health.

The following examples use a sample `ecommerce` database with the following tables:

  * `products`: contains product information, including `product_id`, `product_name`, `category`, and `price`.
  * `customers`: stores customer data, such as `customer_id`, `first_name`, `last_name`, and `email`.
  * `orders`: holds order information, including `order_id`, `customer_id`, and `order_date`.

Category | Tools | Example natural language prompt  
---|---|---  
Database operations |  `database_overview` | Give me an overview of the current database.  
`list_tables` | Show me all the tables in the current database.  
`execute_sql` | Show me the 10 most expensive products in the "Laptops" category.  
`list_active_queries` | What queries are running on the database?  
`get_query_plan` | Explain the query plan for a query that finds all customers who have not placed an order in the last 6 months.  
`list_available_extensions` | What are the available extensions I can install?  
`list_installed_extensions` | List all the extensions that are installed.  
`list_indexes` | List all indexes in the `products` table.  
`list_locks` | Show all active locks on the database.  
`list_schemas` | List all schemas in the database.  
`list_sequences` | Show all sequences in the current schema.  
`list_triggers` | List all triggers for the `orders` table.  
`list_views` | Show me all the views in the `sales` schema.  
Resource management  
clusters, instances, users | `create_cluster` | Create an AlloyDB cluster named `sales-quarterly-db` in the `us-east1` region.  
`get_cluster` | Get the details for the cluster `sales-quarterly-db`.  
`list_clusters` | List all of my AlloyDB clusters.  
`create_instance` | Create a new read instance in the `sales-quarterly-db` cluster.  
`get_instance` | Show me the information for the instance `sales-quarterly-db-rp`.  
`list_instances` | List all instances in the `sales-quarterly-db` cluster.  
`create_user` | **Note:** The `create_user` tool can create two types of database users: 

  * **Database users with built-in authentication** : these users are managed within the database and authenticate with a password.
  * **IAM users** : these users are managed in IAM and authenticate using their IAM credentials.

When creating a database user with built-in authentication, you must provide a password. When creating an IAM user, you must provide the IAM principal.  Create a new database user named `reporting_user` with password `report_password`.  
Create a new IAM database user for `reporting_user@example.com`.  
`get_user` | Get the information for the user `reporting_user`.  
`list_users` | List all database users.  
`wait_for_operation` | What is the status of the operation `operation-163562789`?  
Database health and maintenance | `list_autovacuum_configurations` | Show me the current autovacuum configuration.  
`list_memory_configurations` | What are the current memory configurations for the primary instance?  
`list_top_bloated_tables` | List the top five most bloated tables.  
`list_replication_slots` | Display all active replication slots.  
`replication_stats` | Show the current replication statistics.  
`list_invalid_indexes` | Check for any invalid indexes in the `ecommerce` database.  
`long_running_transactions` | Are there any long-running transactions?  
  
### AlloyDB Observability extension

The `alloydb-observability` extension provides a unified interface for managing and monitoring database performance and health directly from the Gemini CLI.

Category | Tools | Example natural language prompt  
---|---|---  
Observability | `get_system_metrics` | What are the system metrics, like CPU usage, for the last hour?  
`get_query_metrics` | Show me the query performance metrics from the last 15 minutes.  
  
You can use the Gemini CLI extension for AlloyDB in two ways:

  * A standalone command-line tool
  * Integrated into your IDE with Gemini Code Assist



### Gemini CLI

  1. Install the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation).
  2. Install the AlloyDB extension for Gemini CLI from the GitHub repository using the following command: 
         
         gemini extensions install https://github.com/gemini-cli-extensions/alloydb
         

  3. Set environment variables to connect to your AlloyDB instance: 
         
         export ALLOYDB_POSTGRES_PROJECT="PROJECT_ID"
         export ALLOYDB_POSTGRES_REGION="REGION"
         export ALLOYDB_POSTGRES_CLUSTER="CLUSTER_NAME"
         export ALLOYDB_POSTGRES_INSTANCE="INSTANCE_NAME"
         export ALLOYDB_POSTGRES_DATABASE="DATABASE_NAME"
         

The Gemini CLI extension for AlloyDB uses your [application default credentials (ADC)](/authentication/application-default-credentials) for authentication by default. If you want to connect as a database user instead, set the following optional environment variables:
         
         #Optional: Set for database user authentication
         export ALLOYDB_POSTGRES_USER="USERNAME"
         export ALLOYDB_POSTGRES_PASSWORD="PASSWORD"
         

To connect using a private IP address, you must also set the following environment variable:
         
         export ALLOYDB_POSTGRES_IP_TYPE="private"
         

  4. Start the Gemini CLI in interactive mode: 
         
         gemini
         

The CLI automatically loads the AlloyDB extension for Gemini CLI extension and its tools, which you can use to interact with your database. 



### Gemini Code Assist

We recommend to configure Gemini Code Assist to use the Gemini CLI, this approach removes the need to manually configure an MCP server.

  1. Make sure you have installed and configured the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation) and the [`alloydb` extension](https://github.com/gemini-cli-extensions/alloydb).
  2. [Configure Gemini Code Assist to use the Gemini CLI](https://developers.google.com/gemini-code-assist/docs/set-up-gemini-standard-enterprise).
  3. Start interacting with your AlloyDB instance using natural language directly within the Gemini Code Assist chat.



## Connect with Antigravity

You can connect AlloyDB to Antigravity in the following ways:

  * Using the MCP Store
  * Using a custom configuration



**Note:** You don't need to download the MCP Toolbox binary to use these methods.

### MCP Store

The most recommended method to connect to AlloyDB in [Antigravity](https://antigravity.google/docs/mcp) is by using the built-in MCP Store.

  1. Open [Antigravity](https://antigravity.google/docs/mcp) and open the **editor's agent panel**.
  2. Click the **"..."** icon at the top of the panel and select **MCP Servers**.
  3. Locate **AlloyDB for PostgreSQL** in the list of available servers and click **Install**.
  4. Follow the on-screen prompts to securely link your accounts (where applicable).



After you install AlloyDB in the MCP Store, resources and tools from the server are automatically available to the editor.

### Custom config

To connect to a custom MCP server, follow these steps:

  1. Open [Antigravity](https://antigravity.google/docs/mcp) and open the **editor's agent panel**.
  2. Click the **"..."** icon at the top of the panel and select **MCP Servers**.
  3. Click **Manage MCP Servers > View raw config** to open the `mcp_config.json` file.
  4. Add and save the following configuration to the `mcp_config.json` file.


    
    
    {
      "mcpServers": {
        "alloydb-postgres": {
          "command": "npx",
          "args": ["-y","@toolbox-sdk/server","--prebuilt","alloydb-postgres","--stdio"],
          "env": {
              "ALLOYDB_POSTGRES_PROJECT": "PROJECT_ID",
              "ALLOYDB_POSTGRES_REGION": "REGION",
              "ALLOYDB_POSTGRES_CLUSTER": "CLUSTER_NAME",
              "ALLOYDB_POSTGRES_INSTANCE": "INSTANCE_NAME",
              "ALLOYDB_POSTGRES_DATABASE": "DATABASE_NAME",
              "ALLOYDB_POSTGRES_USER": "USERNAME",
              "ALLOYDB_POSTGRES_PASSWORD": "PASSWORD"
          }
        }
      }
    }
    

**Note:** To connect using a private IP address, add the `"ALLOYDB_POSTGRES_IP_TYPE": "private"` property to the `env` object. Make sure to add a comma to the preceding line to keep the JSON valid.  Replace the following: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: your AlloyDB region name.
  * `CLUSTER_NAME`: your AlloyDB cluster name.
  * `INSTANCE_NAME`: your AlloyDB instance name.
  * `DATABASE_NAME`: your AlloyDB database name.
  * `USERNAME`: your AlloyDB username for the `ALLOYDB_POSTGRES_USER` variable.
  * `PASSWORD`: your AlloyDB password for the `ALLOYDB_POSTGRES_PASSWORD` variable.



## Connect with other IDEs using MCP Toolbox for Databases

This section describes how to connect to your AlloyDB instance from various agents using [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox). Toolbox acts as an open-source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that sits between your IDE and your database, providing a control plane for your AI tools. This section provides instructions for connecting to an AlloyDB instance using either a public or private IP address. By default, Toolbox uses a public IP address, but you can configure a private IP connection by setting the `ALLOYDB_POSTGRES_IP_TYPE` environment variable as shown in the configuration examples.

### Install MCP Toolbox for Databases

To connect your IDE to AlloyDB, you must install MCP Toolbox for Databases, an open-source server that connects AI agents to your data.

  1. Download the latest version of Toolbox as a binary. Select the [binary](https://github.com/googleapis/genai-toolbox/releases) corresponding to your operating system (OS) and CPU architecture. You must use Toolbox version v0.15.0 or later.

### linux/amd64
         
         curl -O https://storage.googleapis.com/genai-toolbox/v0.15.0/linux/amd64/toolbox
         

### darwin/arm64
         
         curl -O https://storage.googleapis.com/genai-toolbox/v0.15.0/darwin/arm64/toolbox
         

### darwin/amd64
         
         curl -O https://storage.googleapis.com/genai-toolbox/v0.15.0/darwin/amd64/toolbox
         

### windows/amd64
         
         curl -O https://storage.googleapis.com/genai-toolbox/v0.15.0/windows/amd64/toolbox
         

  2. Make the binary an executable.
         
         chmod +x toolbox
         

  3. Verify the installation.
         
         ./toolbox --version
         




### Configure your client

Select your agent tool from the following options:

### Claude code

  1. Install [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).
  2. Create the `.mcp.json` file in your project root, if it doesn't exist. 
  3. Add the configuration, replace the environment variables with your values, and save.

  

    
    
    {
      "mcpServers": {
        "alloydb": {
          "command": "./PATH/TO/toolbox",
          "args": ["--prebuilt","alloydb-postgres","--stdio"],
          "env": {
              "ALLOYDB_POSTGRES_PROJECT": "PROJECT_ID",
              "ALLOYDB_POSTGRES_REGION": "REGION",
              "ALLOYDB_POSTGRES_CLUSTER": "CLUSTER_NAME",
              "ALLOYDB_POSTGRES_INSTANCE": "INSTANCE_NAME",
              "ALLOYDB_POSTGRES_DATABASE": "DATABASE_NAME",
              "ALLOYDB_POSTGRES_USER": "USERNAME",
              "ALLOYDB_POSTGRES_PASSWORD": "PASSWORD"
          }
        }
      }
    }
    

**Note:** To connect using a private IP address, add the following line to the `env` object: `"ALLOYDB_POSTGRES_IP_TYPE": "private"`

### Claude desktop

  1. Open [Claude Desktop](https://claude.ai/download) and navigate to **Settings**.
  2. In the **Developer** tab, click **Edit Config** to open the configuration file.
  3. Add the configuration, replace the environment variables with your values, and save.

  

    
    
    {
      "mcpServers": {
        "alloydb": {
          "command": "./PATH/TO/toolbox",
          "args": ["--prebuilt","alloydb-postgres","--stdio"],
          "env": {
              "ALLOYDB_POSTGRES_PROJECT": "PROJECT_ID",
              "ALLOYDB_POSTGRES_REGION": "REGION",
              "ALLOYDB_POSTGRES_CLUSTER": "CLUSTER_NAME",
              "ALLOYDB_POSTGRES_INSTANCE": "INSTANCE_NAME",
              "ALLOYDB_POSTGRES_DATABASE": "DATABASE_NAME",
              "ALLOYDB_POSTGRES_USER": "USERNAME",
              "ALLOYDB_POSTGRES_PASSWORD": "PASSWORD"
          }
        }
      }
    }
    

**Note:** To connect using a private IP address, add the following line to the `env` object: `"ALLOYDB_POSTGRES_IP_TYPE": "private"`

  4. Restart Claude Desktop.
  5. The new chat screen displays a hammer (MCP) icon with the new MCP server.



### Cline

  1. Open the [Cline](https://github.com/cline/cline) extension in VS Code and tap **MCP Servers** icon.
  2. Click **Configure MCP Servers** to open the configuration file.
  3. Add the following configuration, replace the environment variables with your values, and save.

  

    
    
    {
      "mcpServers": {
        "alloydb": {
         "command": "./PATH/TO/toolbox",
          "args": ["--prebuilt","alloydb-postgres","--stdio"],
          "env": {
              "ALLOYDB_POSTGRES_PROJECT": "PROJECT_ID",
              "ALLOYDB_POSTGRES_REGION": "REGION",
              "ALLOYDB_POSTGRES_CLUSTER": "CLUSTER_NAME",
              "ALLOYDB_POSTGRES_INSTANCE": "INSTANCE_NAME",
              "ALLOYDB_POSTGRES_DATABASE": "DATABASE_NAME",
              "ALLOYDB_POSTGRES_USER": "USERNAME",
              "ALLOYDB_POSTGRES_PASSWORD": "PASSWORD"
          }
        }
      }
    }
    

  
A green active status appears after the server connects successfully.   
  
**Note:** To connect using a private IP address, add the following line to the `env` object: `"ALLOYDB_POSTGRES_IP_TYPE": "private"`

### Cursor

  1. Create the `.cursor` directory in your project root if it doesn't exist.
  2. Create the `.cursor/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replace the environment variables with your values, and save.


    
    
    {
      "mcpServers": {
        "alloydb": {
          "command": "./PATH/TO/toolbox",
          "args": ["--prebuilt","alloydb-postgres","--stdio"],
          "env": {
              "ALLOYDB_POSTGRES_PROJECT": "PROJECT_ID",
              "ALLOYDB_POSTGRES_REGION": "REGION",
              "ALLOYDB_POSTGRES_CLUSTER": "CLUSTER_NAME",
              "ALLOYDB_POSTGRES_INSTANCE": "INSTANCE_NAME",
              "ALLOYDB_POSTGRES_DATABASE": "DATABASE_NAME",
              "ALLOYDB_POSTGRES_USER": "USERNAME",
              "ALLOYDB_POSTGRES_PASSWORD": "PASSWORD"
          }
        }
      }
    }
    

**Note:** To connect using a private IP address, add the following line to the `env` object: `"ALLOYDB_POSTGRES_IP_TYPE": "private"`

  4. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects.



### Visual Studio Code (Copilot)

  1. Open [VS Code](https://code.visualstudio.com/docs/copilot/overview) and create `.vscode` directory in your project root if it does not exist. 
  2. Create the `.vscode/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replace the environment variables with your values, and save.


    
    
    {
      "servers": {
        "alloydb": {
          "command": "./PATH/TO/toolbox",
          "args": ["--prebuilt","alloydb-postgres","--stdio"],
          "env": {
            "ALLOYDB_POSTGRES_PROJECT": "PROJECT_ID",
            "ALLOYDB_POSTGRES_REGION": "REGION",
            "ALLOYDB_POSTGRES_CLUSTER": "CLUSTER_NAME",
            "ALLOYDB_POSTGRES_INSTANCE": "INSTANCE_NAME",
            "ALLOYDB_POSTGRES_DATABASE": "DATABASE_NAME",
            "ALLOYDB_POSTGRES_USER": "USERNAME",
            "ALLOYDB_POSTGRES_PASSWORD": "PASSWORD"
          }
        }
      }
    }
    

**Note:** To connect using a private IP address, add the following line to the `env` object: `"ALLOYDB_POSTGRES_IP_TYPE": "private"`

### Windsurf

  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to Cascade assistant.
  2. Click the MCP icon, then click **Configure** to open the configuration file.
  3. Add the following configuration, replace the environment variables with your values, and save.


    
    
    {
      "mcpServers": {
        "alloydb": {
          "command": "./PATH/TO/toolbox",
          "args": ["--prebuilt","alloydb-postgres","--stdio"],
          "env": {
              "ALLOYDB_POSTGRES_PROJECT": "PROJECT_ID",
              "ALLOYDB_POSTGRES_REGION": "REGION",
              "ALLOYDB_POSTGRES_CLUSTER": "CLUSTER_NAME",
              "ALLOYDB_POSTGRES_INSTANCE": "INSTANCE_NAME",
              "ALLOYDB_POSTGRES_DATABASE": "DATABASE_NAME",
              "ALLOYDB_POSTGRES_USER": "USERNAME",
              "ALLOYDB_POSTGRES_PASSWORD": "PASSWORD"
          }
        }
      }
    }
    

**Note:** To connect using a private IP address, add the following line to the `env` object: `"ALLOYDB_POSTGRES_IP_TYPE": "private"`

### Access advanced query insights using MCP Toolbox for Databases

You can use MCP Toolbox for Databases to access AlloyDB observability features and advanced query insights directly in your IDE. This lets AI agents analyze query execution statistics, monitor wait events, and retrieve index recommendations to troubleshoot database performance.

#### Required roles

To get the permissions that you need to use the AlloyDB observability prebuilt configurations in MCP Toolbox for Databases, ask your administrator to grant you the following IAM roles on the project where you want to use the tools: 

  * View Cloud Monitoring data: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
  * View Database Insights data: [Database Insights Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the AlloyDB observability prebuilt configurations in MCP Toolbox for Databases. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the AlloyDB observability prebuilt configurations in MCP Toolbox for Databases:

  * Get query metrics: `queryMetrics.fetch`
  * Get system metrics: `systemMetrics.fetch`
  * Get advanced aggregated query statistics: `queryStats.fetch`
  * Get advanced time series query statistics: `queryTimeSeries.fetch`
  * Get advanced aggregated wait event statistics: `waitEventStats.fetch`
  * Get advanced time series wait event statistics: `waitEventTimeSeries.fetch`
  * Get index recommendations: `recommendations.query, resourceRecommendations.query`
  * View Monitoring metrics: `monitoring.timeseries.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To configure your IDE to use the `alloydb-postgres-observability` prebuilt configuration, add the following configuration to your client's MCP configuration file.

For more information, see the [MCP Toolbox for Databases: AlloyDB for PostgreSQL observability prebuilt configuration documentation](https://mcp-toolbox.dev/integrations/cloudmonitoring/prebuilt-configs/alloydb-postgres-observability/).
    
    
    {
      "mcpServers": {
        "alloydb-observability": {
          "command": "./PATH/TO/toolbox",
          "args": ["--prebuilt", "alloydb-postgres-observability", "--stdio"],
        }
      }
    }
    

By connecting with this prebuilt configuration, your agent can invoke the following AlloyDB advanced query insights tools to troubleshoot performance:

  * [`get_advanced_aggregated_query_stats`](https://mcp-toolbox.dev/integrations/databaseinsights/tools/databaseinsights-get-advanced-aggregated-query-stats/): Fetches aggregated query execution statistics.
  * [`get_advanced_aggregated_wait_event_stats`](https://mcp-toolbox.dev/integrations/databaseinsights/tools/databaseinsights-get-advanced-aggregated-wait-event-stats/): Fetches aggregated wait event bottleneck metrics.
  * [`get_advanced_time_series_query_stats`](https://mcp-toolbox.dev/integrations/databaseinsights/tools/databaseinsights-get-advanced-time-series-query-stats/): Fetches time series performance metrics for queries over time.
  * [`get_advanced_time_series_wait_event_stats`](https://mcp-toolbox.dev/integrations/databaseinsights/tools/databaseinsights-get-advanced-time-series-wait-event-stats/): Fetches time series metrics for wait events over time.
  * [`get_index_recommendations`](https://mcp-toolbox.dev/integrations/databaseinsights/tools/databaseinsights-get-index-recommendations/): Fetches index recommendations to optimize query performance.



## Connect using Data Agent Kit

Google Cloud Data Agent Kit lets you connect to and query your AlloyDB database directly in VS Code, VS Code-based IDEs, and supported CLIs.

The benefits of using Data Agent Kit include the following:

  * Data discovery and exploration capabilities that let you ask questions about your AlloyDB data in natural language
  * The elimination of context switching between AlloyDB tools and your development environment
  * Plugins that let you use agentic CLIs with your Google Cloud resources



For more information, see [Data Agent Kit overview](https://docs.cloud.google.com/data-agent-kit/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
