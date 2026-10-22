---
url: https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage-mcp-toolbox/
title: Use data lineage with MCP, Gemini, and other agents \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:30.169236+00:00
---

# Use data lineage with MCP, Gemini, and other agents  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage-mcp-toolbox/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use data lineage with MCP, Gemini, and other agents Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect data lineage to developer tools such as the Gemini CLI and other Model Context Protocol (MCP) clients. Connecting data lineage to these tools enables AI-driven lineage tracking and data provenance analysis directly within your development environment.

You can connect IDEs and developer tools that support MCP by using a local [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox). You can then use AI agents in your existing IDE to query data lineage graphs, discover upstream data provenance, and analyze downstream impact across your assets.

For more information about MCP, see [Introduction to Model Context Protocol](https://modelcontextprotocol.io/introduction).

This guide demonstrates the connection process for the following tools:

  * Gemini CLI
  * Gemini Code Assist
  * Claude Code
  * Claude desktop
  * Codex
  * Cline (VS Code extension)
  * Cursor
  * Visual Studio Code (Copilot)
  * Windsurf (formerly Codeium)



## What MCP tools does data lineage provide?

The data lineage integration allows AI agents to query and analyze data lineage, representing the flow of data between source (upstream) and target (downstream) assets. It supports both entity-level lineage (tracking data flow between entire assets such as tables and files) and column-level lineage (tracking data flow between specific fields or columns within assets).

Data lineage provides the `datalineage-search-lineage` tool, which retrieves a streaming response of lineage links connected to requested assets.

For more information about the data lineage source and its available tools, see the [Data Lineage Source documentation](https://mcp-toolbox.dev/integrations/datalineage/source/).

## Required roles

To get the permissions that you need to connect to data lineage using MCP Toolbox, ask your administrator to grant you the following IAM roles on your project: 

  * To enable APIs: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) 
  * To use data lineage skills: [Data Lineage Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to connect to data lineage using MCP Toolbox. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to connect to data lineage using MCP Toolbox:

  * To enable APIs: `serviceusage.services.enable`
  * To use data lineage skills: 
    * `datalineage.lineage.searchLinks`
    * `datalineage.processes.get`
    * `datalineage.runs.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable the required APIs

  1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Data lineage API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datalineage.googleapis.com)

  5. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




## Install MCP Toolbox

You don't need to install MCP Toolbox if you only plan to use Gemini Code Assist, as it bundles the required server capabilities. For other IDEs and tools, follow the steps in this section to install MCP Toolbox.

  1. Download the latest version of MCP Toolbox as a binary. Select the [MCP Toolbox binary release](https://github.com/googleapis/mcp-toolbox/releases) that corresponds to your (OS) and CPU architecture. You must use MCP Toolbox `v0.31.0` or later.

### Linux/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/linux/amd64/toolbox

Replace `VERSION` with MCP Toolbox version—for example, `v0.31.0`.

### macOS (Darwin)/arm64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/darwin/arm64/toolbox

Replace `VERSION` with MCP Toolbox version—for example, `v0.31.0`.

### macOS (Darwin)/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/darwin/amd64/toolbox

Replace `VERSION` with MCP Toolbox version—for example, `v0.31.0`.

### Windows/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/windows/amd64/toolbox

Replace `VERSION` with MCP Toolbox version—for example, `v0.31.0`.

  2. Make the binary executable:
         
         chmod +x toolbox
         

  3. Verify the installation:
         
         ./toolbox --version
         

A successful installation returns the version number, for example, `0.15.0`.




## Set up clients and connections for data lineage

This section explains how to connect data lineage to your tools.

To connect your MCP-compatible IDEs and tools to data lineage, you must first install MCP Toolbox and create a custom configuration file for your lineage source and tools.

**Note:** You don't need to install MCP Toolbox if you only plan to use Gemini Code Assist.

  1. In your project root or configuration directory, create a YAML file named `lineage-config.yaml` with the following configuration:
         
         kind: source
         name: lineage-source
         type: datalineage
         project: ${DATALINEAGE_PROJECT}
         ---
         kind: tool
         name: search_lineage
         type: datalineage-search-lineage
         source: lineage-source
         description: Retrieves a streaming response of lineage links connected to requested assets.
         

  2. Set the environment variable for your Google Cloud project:
         
         export DATALINEAGE_PROJECT=PROJECT_ID
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  3. Configure your specific client using the `--config` flag instead of a prebuilt configuration, as shown in the following sections.




### Gemini CLI

You can use data lineage in the Gemini CLI by configuring it as a local MCP server using MCP Toolbox and your custom `lineage-config.yaml` file.

  1. In your project's working directory, create a folder named `.gemini` (or open your global `~/.gemini` directory).
  2. Within that directory, create or open the `settings.json` file.
  3. Add the following configuration:
         
         {
           "mcpServers": {
             "dataLineage": {
               "command": "./PATH/TO/toolbox",
               "args": ["--config","/PATH/TO/lineage-config.yaml","--stdio"],
               "env": {
                 "DATALINEAGE_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Save the configuration.

  5. Start the Gemini CLI in interactive mode:
         
         gemini
         

In the Gemini CLI, use the [`/mcp`](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/commands.md) command to verify that the `dataLineage` server is connected.




### Gemini Code Assist

Gemini Code Assist bundles the required MCP server capabilities, so you don't need to install MCP Toolbox separately.

  1. In VS Code, install the [Gemini Code Assist](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist) extension.
  2. Enable Agent Mode in Gemini Code Assist chat.
  3. In your working directory, create a folder named `.gemini`. Within that, create a `settings.json` file.
  4. Add the following configuration:
         
         {
           "mcpServers": {
             "dataLineage": {
               "command": "./PATH/TO/toolbox",
               "args": ["--config","/PATH/TO/lineage-config.yaml","--stdio"],
               "env": {
                 "DATALINEAGE_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  5. Save the configuration.




### Claude Code

While the official plugin provides tools for Knowledge Catalog, you can use data lineage in Claude Code by configuring a local MCP Toolbox server with your custom configuration file.

  1. Set the environment variable to connect to your data lineage project:
         
         export DATALINEAGE_PROJECT=PROJECT_ID
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  2. Configure Claude Code to use the MCP Toolbox server:
         
         claude mcp add datalineage -- /PATH/TO/toolbox --config=/PATH/TO/lineage-config.yaml --stdio
         

  3. Start the agent:
         
         claude
         




### Codex

To use data lineage in Codex, configure an MCP server connection in your Codex configuration to run MCP Toolbox with your custom `lineage-config.yaml` file:

  1. Set the environment variable to connect to your data lineage project:
         
         export DATALINEAGE_PROJECT="PROJECT_ID"
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  2. In your Codex MCP configuration, add the server using MCP Toolbox:
         
         {
           "mcpServers": {
             "dataLineage": {
               "command": "./PATH/TO/toolbox",
               "args": ["--config","/PATH/TO/lineage-config.yaml","--stdio"],
               "env": {
                 "DATALINEAGE_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.




### Claude desktop

  1. Open [Claude Desktop](https://claude.ai/download) and navigate to **Settings**.
  2. To open the configuration file, in the **Developer** tab, click **Edit config**.
  3. Add the configuration:
         
         {
           "mcpServers": {
             "dataLineage": {
               "command": "./PATH/TO/toolbox",
               "args": ["--config","/PATH/TO/lineage-config.yaml","--stdio"],
               "env": {
                 "DATALINEAGE_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Save the configuration.

  5. Restart Claude desktop. The new chat screen displays an MCP icon representing the new MCP server.




### Cline

  1. In VS Code, open the [Cline](https://github.com/cline/cline) extension and then click the **MCP Servers** icon.
  2. To open the configuration file, tap **Configure MCP Servers**.
  3. Add the following configuration:
         
         {
           "mcpServers": {
             "dataLineage": {
               "command": "./PATH/TO/toolbox",
               "args": ["--config","/PATH/TO/lineage-config.yaml","--stdio"],
               "env": {
                 "DATALINEAGE_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Save the configuration. A green active status appears after the server connects successfully.




### Cursor

  1. Create the `.cursor` directory in your project root if it doesn't exist.
  2. Create the `.cursor/mcp.json` file if it doesn't exist and open it.
  3. Add the following configuration:
         
         {
           "mcpServers": {
             "dataLineage": {
               "command": "./PATH/TO/toolbox",
               "args": ["--config","/PATH/TO/lineage-config.yaml","--stdio"],
               "env": {
                 "DATALINEAGE_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Save the configuration.

  5. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects.




### VS Code (Copilot)

  1. Open [VS Code](https://code.visualstudio.com/docs/copilot/overview) and create `.vscode` directory in your project root if it doesn't exist.
  2. Create the `.vscode/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration:
         
         {
           "servers": {
             "dataLineage": {
               "command": "./PATH/TO/toolbox",
               "args": ["--config","/PATH/TO/lineage-config.yaml","--stdio"],
               "env": {
                 "DATALINEAGE_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Save the configuration.




### Windsurf

  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to Cascade assistant.
  2. To open the configuration file, click the MCP icon, then click **Configure**.
  3. Add the following configuration:
         
         {
           "mcpServers": {
             "dataLineage": {
               "command": "./PATH/TO/toolbox",
               "args": ["--config","/PATH/TO/lineage-config.yaml","--stdio"],
               "env": {
                 "DATALINEAGE_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Save the configuration.




## Use the skills

Your AI assistant is now connected to data lineage. Try asking your AI assistant to trace upstream and downstream data lineage between your assets.

For example, you can ask your AI assistant to:

  * Trace where a BigQuery table's data originates (upstream lineage).
  * Discover which downstream tables or reports depend on a specific data asset (downstream lineage).
  * Inspect column-level lineage between specific fields across assets.



## Optional: Add system instructions

System instructions are a way to provide specific guidelines to the LLM, helping it to understand the context and respond more accurately. Set up system instructions based on the [Data Lineage recommended system prompt](https://github.com/googleapis/mcp-toolbox/blob/main/docs/en/integrations/datalineage/source.md#sample-system-prompt).

For example, you can add instructions to guide the LLM on how to use the data lineage skills:

  * When asked to trace upstream or downstream data flow between assets or columns, use the `search_lineage` skill or `datalineage-search-lineage` tool.

**Note:** We recommend this optional step to get a better experience and avoid additional work, for example, designing your own agent.

For more information about how to configure instructions, see [Use instructions to get AI edits that follow your coding style](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode#_use-instructions-to-get-ai-edits-that-follow-your-coding-style).

## What's next

  * Review the [difference between local and remote MCP servers](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview).
  * Learn how to [use the local MCP Toolbox server for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/pre-built-tools-with-mcp-toolbox).
  * Read the [Data Lineage MCP tools reference](https://mcp-toolbox.dev/integrations/datalineage/source/).
  * Learn more [about data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage).
  * [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
