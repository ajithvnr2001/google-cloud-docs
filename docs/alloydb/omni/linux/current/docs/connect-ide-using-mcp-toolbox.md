---
url: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/connect-ide-using-mcp-toolbox/
title: Use AlloyDB Omni with MCP, Gemini CLI, and other agents \u00a0|\u00a0 AlloyDB Omni using RPM: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:37:41.612830+00:00
---

# Use AlloyDB Omni with MCP, Gemini CLI, and other agents  |  AlloyDB Omni using RPM: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/connect-ide-using-mcp-toolbox/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)



Send feedback 

#  Use AlloyDB Omni with MCP, Gemini CLI, and other agents Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/connect-ide-using-mcp-toolbox)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/connect-ide-using-mcp-toolbox)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/connect-ide-using-mcp-toolbox)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/connect-ide-using-mcp-toolbox)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/connect-ide-using-mcp-toolbox)

This document describes how to connect your AlloyDB Omni instance to various agents that support the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). 

Since AlloyDB Omni is PostgreSQL compatible, you can use tools and extensions designed for PostgreSQL.

For the simplest setup, use the dedicated PostgreSQL extension for [Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli); it integrates the underlying MCP server directly into the extension, so you don't need to perform a separate server setup. You can configure Gemini Code Assist to use the Gemini CLI, offering similar setup benefits in your IDE.

Alternatively, other IDEs and agents supporting the MCP can connect through [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox). Toolbox is an open-source MCP server designed to connect AI agents to your data. It handles tasks like authentication and connection pooling, letting you interact with your data with natural language directly from your IDE.

## Before you begin

Before you connect to your AlloyDB Omni instance, make sure to do the following:

  1. [Install AlloyDB Omni for Linux](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/deploy-vm) and have a running database instance.
  2. Create or reuse a database user. Be ready to enter the username and password.



## Use the Gemini CLI extension for PostgreSQL

**Note:** The PostgreSQL Gemini CLI extension is based on MCP Toolbox for Databases. MCP Toolbox for Databases is in beta (pre-v1.0), and may see breaking changes until the first stable release (v1.0).

Gemini CLI is an open-source AI agent designed to assist with development workflows by assisting with coding, debugging, data exploration, and content creation. Its mission is to provide an agentic interface for interacting with Data Cloud services and popular open-source databases.

The integration with Gemini CLI for AlloyDB Omni is through the [PostgreSQL extension](https://github.com/gemini-cli-extensions/postgres). This extension provides a set of tools to interact with PostgreSQL and AlloyDB Omni allowing you to manage your databases, execute queries, and explore schemas directly from the Gemini CLI using natural language prompts.

The following examples use a sample `ecommerce` database with the following tables:

  * `products`: contains product information, including `product_id`, `product_name`, `category`, and `price`.
  * `customers`: stores customer data, such as `customer_id`, `first_name`, `last_name`, and `email`.
  * `orders`: holds order information, including `order_id`, `customer_id`, and `order_date`.



The following tools are available within the PostgreSQL extension:

Category | Tool | Example natural language prompt  
---|---|---  
Database operations | `execute_sql` | Show me the 10 most expensive products in the 'Laptops' category.  
`get_query_plan` | Explain the query plan for a query that finds all customers who have not placed an order in the last 6 months.  
`list_active_queries` | What queries are running on the database?  
`database_overview` | Give me an overview of the current database.  
`list_tables` | Show me all the tables in the current database.  
`list_views` | What views are available?  
`list_schemas` | List all schemas.  
`list_triggers` | Show me the triggers on the orders table.  
`list_available_extensions` | What are the available extensions I can install?  
`list_installed_extensions` | List all the extensions that are installed.  
`list_indexes` | List all indexes.  
`list_sequences` | List all sequences.  
Database health and maintenance | `list_autovacuum_configurations` | Show me the current autovacuum configuration.  
`list_memory_configurations` | What are the current memory configurations?  
`list_top_bloated_tables` | List the top five most bloated tables.  
`list_replication_slots` | Display all active replication slots.  
`list_invalid_indexes` | Check for any invalid indexes in the `ecommerce` database.  
`long_running_transactions` | Show me the long running transactions.  
`list_locks` | List all locks.  
`replication_stats` | Show me the replication stats.  
  
You can use the Gemini CLI extension for PostgreSQL in two ways:

  * A standalone command-line tool
  * Integrated into your IDE with Gemini Code Assist



### Gemini CLI

  1. Install the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation) (version 0.6.0 or later).
  2. Install the PostgreSQL extension for Gemini CLI from the GitHub repository using the following command: 
         
         gemini extensions install https://github.com/gemini-cli-extensions/postgres

  3. Set environment variables to connect to your AlloyDB Omni instance: 
         
         export POSTGRES_HOST="DATABASE_HOST"
         export POSTGRES_PORT="DATABASE_PORT"
         export POSTGRES_DATABASE="DATABASE_NAME"
         export POSTGRES_USER="DATABASE_USER"
         export POSTGRES_PASSWORD="DATABASE_PASSWORD"
         

You can also load these variables from a `.env` file in your working directory.

  4. Start the Gemini CLI in interactive mode: 
         
         gemini

The CLI automatically loads the PostgreSQL extension and its tools, which you can use to interact with your database. 



### Gemini Code Assist

To avoid manually configuring an MCP server, configure Gemini Code Assist to use the Gemini CLI.

  1. Install and configure the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation) and the [`postgres` extension](https://github.com/gemini-cli-extensions/postgres) as described in the Gemini CLI tab.
  2. [Configure Gemini Code Assist to use the Gemini CLI](https://developers.google.com/gemini-code-assist/docs/set-up-gemini-standard-enterprise).
  3. Start interacting with your AlloyDB Omni instance using natural language directly within the Gemini Code Assist chat.



## Connect with other IDEs using MCP Toolbox for Databases

This section describes how to connect to your AlloyDB Omni instance from various agents using [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox).

### Install MCP Toolbox for Databases

To connect your IDE to AlloyDB Omni, you must install MCP Toolbox for Databases, an open-source server that connects AI agents to your data.

  1. Download the latest version of Toolbox as a binary. Select the [binary](https://github.com/googleapis/genai-toolbox/releases) corresponding to your operating system (OS) and CPU architecture.

### linux/amd64
         
         curl -L -O https://storage.googleapis.com/genai-toolbox/v0.21.0/linux/amd64/toolbox

### darwin/arm64
         
         curl -L -O https://storage.googleapis.com/genai-toolbox/v0.21.0/darwin/arm64/toolbox

### darwin/amd64
         
         curl -L -O https://storage.googleapis.com/genai-toolbox/v0.21.0/darwin/amd64/toolbox

### windows/amd64
         
         curl -L -O https://storage.googleapis.com/genai-toolbox/v0.21.0/windows/amd64/toolbox.exe

  2. Make the binary an executable.
         
         chmod +x toolbox
         

  3. Verify the installation.
         
         ./toolbox --version
         




### Configure your client

Select your agent tool from the following options:

### Cursor

  1. Create the `.cursor` directory in your project root if it doesn't exist.
  2. Create the `.cursor/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replace the environment variables with your values, and save.


    
    
    {
      "mcpServers": {
        "alloydbomni": {
          "command": "PATH_TO_TOOLBOX",
          "args": ["--prebuilt","postgres","--stdio"],
          "env": {
            "POSTGRES_HOST": "DATABASE_HOST",
            "POSTGRES_PORT": "DATABASE_PORT",
            "POSTGRES_DATABASE": "DATABASE_NAME",
            "POSTGRES_USER": "DATABASE_USER",
            "POSTGRES_PASSWORD": "DATABASE_PASSWORD"
          }
        }
      }
    }
    

  4. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects.



### Windsurf

  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to Cascade assistant.
  2. Click the MCP icon, then click **Configure** to open the configuration file.
  3. Add the following configuration, replace the environment variables with your values, and save.


    
    
    {
      "mcpServers": {
        "alloydbomni": {
          "command": "PATH_TO_TOOLBOX",
          "args": ["--prebuilt","postgres","--stdio"],
          "env": {
            "POSTGRES_HOST": "DATABASE_HOST",
            "POSTGRES_PORT": "DATABASE_PORT",
            "POSTGRES_DATABASE": "DATABASE_NAME",
            "POSTGRES_USER": "DATABASE_USER",
            "POSTGRES_PASSWORD": "DATABASE_PASSWORD"
          }
        }
      }
    }
    

### Visual Studio Code (Copilot)

  1. Open [VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers) and create `.vscode` directory in your project root if it does not exist. 
  2. Create the `.vscode/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replace the environment variables with your values, and save.


    
    
    {
      "servers": {
        "alloydbomni": {
          "command": "PATH_TO_TOOLBOX",
          "args": ["--prebuilt","postgres","--stdio"],
          "env": {
            "POSTGRES_HOST": "DATABASE_HOST",
            "POSTGRES_PORT": "DATABASE_PORT",
            "POSTGRES_DATABASE": "DATABASE_NAME",
            "POSTGRES_USER": "DATABASE_USER",
            "POSTGRES_PASSWORD": "DATABASE_PASSWORD"
          }
        }
      }
    }
    

### Cline

  1. Open the [Cline](https://github.com/cline/cline) extension in VS Code and click **MCP Servers** icon.
  2. Click **Configure MCP Servers** to open the configuration file.
  3. Add the following configuration, replace the environment variables with your values, and save.


    
    
    {
      "mcpServers": {
        "alloydbomni": {
          "command": "PATH_TO_TOOLBOX",
          "args": ["--prebuilt","postgres","--stdio"],
          "env": {
            "POSTGRES_HOST": "DATABASE_HOST",
            "POSTGRES_PORT": "DATABASE_PORT",
            "POSTGRES_DATABASE": "DATABASE_NAME",
            "POSTGRES_USER": "DATABASE_USER",
            "POSTGRES_PASSWORD": "DATABASE_PASSWORD"
          }
        }
      }
    }
          

  4. A green active status appears after the server connects successfully. 



### Claude desktop

  1. Open [Claude Desktop](https://claude.ai/download) and navigate to **Settings**.
  2. In the **Developer** tab, click **Edit Config** to open the configuration file.
  3. Add the configuration, replace the environment variables with your values, and save.


    
    
    {
      "mcpServers": {
        "alloydbomni": {
          "command": "PATH_TO_TOOLBOX",
          "args": ["--prebuilt","postgres","--stdio"],
          "env": {
            "POSTGRES_HOST": "DATABASE_HOST",
            "POSTGRES_PORT": "DATABASE_PORT",
            "POSTGRES_DATABASE": "DATABASE_NAME",
            "POSTGRES_USER": "DATABASE_USER",
            "POSTGRES_PASSWORD": "DATABASE_PASSWORD"
          }
        }
      }
    }
    

  4. Restart Claude Desktop.
  5. The new chat screen displays a hammer (MCP) icon with the new MCP server.



### Claude code

  1. Install [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).
  2. Create the `.mcp.json` file in your project root, if it doesn't exist. 
  3. Add the configuration, replace the environment variables with your values, and save.


    
    
    {
      "mcpServers": {
        "alloydbomni": {
          "command": "PATH_TO_TOOLBOX",
          "args": ["--prebuilt","postgres","--stdio"],
          "env": {
            "POSTGRES_HOST": "DATABASE_HOST",
            "POSTGRES_PORT": "DATABASE_PORT",
            "POSTGRES_DATABASE": "DATABASE_NAME",
            "POSTGRES_USER": "DATABASE_USER",
            "POSTGRES_PASSWORD": "DATABASE_PASSWORD"
          }
        }
      }
    }
    

  4. Restart Claude code to apply the new configuration.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
