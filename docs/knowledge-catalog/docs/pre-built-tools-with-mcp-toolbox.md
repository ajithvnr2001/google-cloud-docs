---
url: https://docs.cloud.google.com/knowledge-catalog/docs/pre-built-tools-with-mcp-toolbox/
title: Use Knowledge Catalog with MCP, Gemini, and other agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:50.646179+00:00
---

# Use Knowledge Catalog with MCP, Gemini, and other agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/pre-built-tools-with-mcp-toolbox/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use Knowledge Catalog with MCP, Gemini, and other agents Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect your Knowledge Catalog (formerly Dataplex Universal Catalog) instance to developer tools such as the Gemini CLI. Connecting Knowledge Catalog to these tools enables AI-driven data discovery and asset management directly within your tool.

To connect data lineage to developer tools using a local MCP Toolbox server, see [Use data lineage with local MCP Toolbox server](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage-mcp-toolbox).

For an integrated command-line experience, we recommend using the dedicated Knowledge Catalog extension for Gemini CLI. The extension bundles the underlying skills directly into the extension, which simplifies setup and configuration.

Alternatively, you can connect other IDEs and developer tools that support MCP by using a local [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox). You can then use AI agents in your existing IDE to discover data assets in Knowledge Catalog. For more information about MCP, see [Introduction to Model Context Protocol](https://modelcontextprotocol.io/introduction).

This guide demonstrates the connection process for the following tools:

  * Gemini CLI (through extension)
  * Gemini Code Assist
  * Claude Code
  * Claude desktop
  * Codex
  * Cline (VS Code extension)
  * Cursor
  * Visual Studio Code (Copilot)
  * Windsurf (formerly Codeium)



## About Gemini CLI and extensions

Gemini CLI is an open-source conversational AI agent from Google that accelerates development workflows and assists with coding, debugging, data exploration, and content creation. It offers an agent-driven experience to interact with Data Cloud services, such as Knowledge Catalog, and other popular open-source databases.

For more information about Gemini CLI, see the [Gemini CLI documentation](https://github.com/google-gemini/gemini-cli/blob/main/README.md).

### How do Gemini CLI extensions work?

Extensions expand the capabilities of Gemini CLI, letting it connect to and control specific Google Cloud services and other tools. They provide Gemini with context and API understanding, enabling conversational interaction. You can load Gemini CLI extensions from GitHub URLs, local directories, or registries. These extensions offer new skills, slash commands, and prompts. These are separate from IDE extensions, such as Gemini Code Assist, which integrate using the MCP Toolbox.

### What MCP tools does Knowledge Catalog provide?

The Knowledge Catalog extension for Gemini CLI integrates AI into your data governance and discovery tasks. You can interact with Knowledge Catalog using natural language prompts in your terminal.

For all available skills, see the [Knowledge Catalog skills on GitHub](https://github.com/gemini-cli-extensions/knowledge-catalog/tree/main/skills).

For more information about the Knowledge Catalog extension, see the [Gemini CLI Extension - Knowledge Catalog](https://github.com/gemini-cli-extensions/knowledge-catalog).

## Required roles

To get the permissions that you need to connect to Knowledge Catalog using MCP Toolbox or the Gemini CLI extension, ask your administrator to grant you the following IAM roles on your project: 

  * To enable APIs: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) 
  * To use Knowledge Catalog skills: [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to connect to Knowledge Catalog using MCP Toolbox or the Gemini CLI extension. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to connect to Knowledge Catalog using MCP Toolbox or the Gemini CLI extension:

  * To enable APIs: `serviceusage.services.enable`
  * To use Knowledge Catalog skills: 
    * `dataplex.projects.search`
    * `dataplex.entries.get`
    * `dataplex.aspectTypes.get`
    * `dataplex.aspectTypes.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable the Dataplex API

  1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

  5. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




## Install MCP Toolbox

You don't need to install MCP Toolbox if you only plan to use Gemini Code Assist or the Gemini CLI extension, as they bundle the required server capabilities. For other IDEs and tools, follow the steps in this section to install MCP Toolbox.

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




## Set up clients and connections

This section explains how to connect Knowledge Catalog to your tools.

To connect MCP-compatible tools and IDEs, you must first install MCP Toolbox. The toolbox acts as an open-source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that sits between your IDE and Knowledge Catalog, providing a secure and efficient control plane for your AI tools. After installation, see the section for your specific tool for configuration instructions.

**Note:** You don't need to install MCP Toolbox if you only plan to use Gemini Code Assist or the Gemini CLI extension.

### Gemini CLI extension

This method uses the `knowledge-catalog` extension for the standalone Gemini CLI tool, and doesn't use MCP Toolbox.

  1. Install the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#quickstart).
  2. Install the Knowledge Catalog extension for Gemini CLI from the GitHub repository:
         
         gemini extensions install https://github.com/gemini-cli-extensions/knowledge-catalog
         

  3. Set the environment variable to connect to your Knowledge Catalog project:
         
         export DATAPLEX_PROJECT=PROJECT_ID
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Start the Gemini CLI in interactive mode:
         
         gemini
         

The CLI automatically loads the Knowledge Catalog extension and its skills, which you can use to interact with your database.

In the Gemini CLI, use the [`/extensions`](https://github.com/google-gemini/gemini-cli/blob/bbcc90613390e4d3d3aed911fbc1535af80d643b/docs/cli/commands.md) command to verify that the extension is installed.




### Gemini Code Assist

Gemini Code Assist bundles the required MCP server capabilities, so you don't need to install MCP Toolbox separately.

  1. In VS Code, install the [Gemini Code Assist](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist) extension.
  2. Enable **Agent Mode** in Gemini Code Assist chat.
  3. In your working directory, create a folder named `.gemini`. Within that folder, create a `settings.json` file.
  4. Add the following configuration:
         
         {
           "mcpServers": {
             "knowledgeCatalog": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","dataplex","--stdio"],
               "env": {
                 "DATAPLEX_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  5. Save the configuration.




### Claude Code

  1. Install [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).
  2. Set the environment variable to connect to your Knowledge Catalog project:
         
         export DATAPLEX_PROJECT=PROJECT_ID
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  3. Start the agent:
         
         claude
         

  4. Install the plugin:
         
         /plugin install knowledge-catalog@claude-plugins-official
         


**Tip:** Run `/plugin list` inside Claude Code to verify the plugin is active, or `/reload-plugins` if you just installed it. 

### Codex

  1. Install the Data Cloud Plugins marketplace:
         
         codex plugin marketplace add GoogleCloudPlatform/data-cloud-plugins
         

  2. Install the Knowledge Catalog plugin:
         
         codex plugin install dataplex@data-cloud-plugins
         

  3. Configure the environment variables to connect to your Knowledge Catalog project:
         
         export DATAPLEX_PROJECT=PROJECT_ID
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Optional. Update the marketplace:
         
         codex plugin marketplace upgrade data-cloud-plugins
         




### Claude desktop

  1. Open [Claude Desktop](https://claude.ai/download) and navigate to **Settings**.
  2. To open the configuration file, go to the **Developer** tab and click **Edit config**.
  3. Add the following configuration:
         
         {
           "mcpServers": {
             "knowledgeCatalog": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","dataplex","--stdio"],
               "env": {
                 "DATAPLEX_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Save the configuration.

  5. Restart Claude desktop. The new chat screen displays an MCP icon representing the new MCP server.




### Cline

  1. In VS Code, open the [Cline](https://github.com/cline/cline) extension and then click the **MCP Servers** icon.
  2. To open the configuration file, click **Configure MCP Servers**.
  3. Add the following configuration:
         
         {
           "mcpServers": {
             "knowledgeCatalog": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","dataplex","--stdio"],
               "env": {
                 "DATAPLEX_PROJECT": "PROJECT_ID"
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
             "knowledgeCatalog": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","dataplex","--stdio"],
               "env": {
                 "DATAPLEX_PROJECT": "PROJECT_ID"
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
             "knowledgeCatalog": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","dataplex","--stdio"],
               "env": {
                 "DATAPLEX_PROJECT": "PROJECT_ID"
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
             "knowledgeCatalog": {
               "command": "./PATH/TO/toolbox",
               "args": ["--prebuilt","dataplex","--stdio"],
               "env": {
                 "DATAPLEX_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         

Replace `PROJECT_ID` with the Google Cloud project ID.

  4. Save the configuration.




## Use the skills

Your AI assistant is now connected to Knowledge Catalog. Try asking your AI assistant to find some data assets such as BigQuery datasets, Cloud SQL instances, and others.

For all available skills, see the [Knowledge Catalog skills on GitHub](https://github.com/gemini-cli-extensions/knowledge-catalog/tree/main/skills).

## Optional: Add system instructions

System instructions are a way to provide specific guidelines to the LLM, helping it to understand the context and respond more accurately. Set up system instructions based on the [recommended system prompt](https://github.com/googleapis/mcp-toolbox/blob/main/docs/en/integrations/knowledge-catalog/source.md#sample-system-prompt).

For example, you can add instructions to guide the LLM on how to use the Knowledge Catalog skills:

  * When asked to find datasets or tables, use the `search_entries` skill.
  * If asked for table schema or metadata details such as data quality rules or ownership, use the `lookup_entry` skill.
  * When asked about governance rules or classifications, start by using `search_aspect_types` to find relevant aspect types.
  * If answering questions requires broad set of metadata, use the `lookup_context` skill to retrieve it.

**Note:** We recommend this optional step to get a better experience and avoid additional work, for example, designing your own agent.

For more information about how to configure instructions, see [Use instructions to get AI edits that follow your coding style](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode#_use-instructions-to-get-ai-edits-that-follow-your-coding-style).

## What's next

  * Learn how to [use the local MCP Toolbox server for data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage-mcp-toolbox).
  * Review the [difference between local and remote MCP servers](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview).
  * See the [Use the Antigravity CLI to test data context](https://docs.cloud.google.com/knowledge-catalog/docs/use-antigravity-cli-agent-to-test-data-context) use case.
  * Read the [Knowledge Catalog MCP tools reference](https://mcp-toolbox.dev/integrations/knowledge-catalog/source/) and [Data Lineage MCP tools reference](https://mcp-toolbox.dev/integrations/datalineage/source/).
  * [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).
  * Learn how to [ingest custom sources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources) into Knowledge Catalog.
  * Learn how to [manage aspects and enrich metadata](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
