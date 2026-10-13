---
url: https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension/
title: Getting started with the Looker extension for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:48.097960+00:00
---

# Getting started with the Looker extension for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Getting started with the Looker extension for VS Code Stay organized with collections  Save and categorize content based on your preferences. 

The [**Looker by Google Cloud**](https://marketplace.visualstudio.com/items?itemName=Google.vscode-looker-official) extension for Visual Studio Code (VS Code) lets you develop LookML directly within your local desktop environment. It provides rich syntax highlighting, bidirectional file synchronization with your Looker instance, and integration with AI coding agents for "vibe coding."

The extension is built by using the Visual Studio Code (VS Code) framework, and it supports integrated development environments (IDEs) that are based on the VS Code IDE, such as the following IDEs and coding tools:

  * Claude Code
  * Codex
  * Cursor
  * Kiro
  * VS Code
  * Windsurf
  * Zed



IDEs that are not forks of VS Code, such as IntelliJ and Eclipse, aren't supported by the Looker extension for VS Code.

This guide covers how to set up and authenticate the extension.

## AI-enabled workflow

The Looker extension for VS Code is part of an AI-enabled agentic development workflow for editing and creating LookML files. To enable this workflow, configure the following tools:

  * A **local IDE** that is based on VS Code. The IDE must either contain a **built-in AI agent** (for example, Cursor), or, if the IDE doesn't contain a built-in AI agent, the IDE must be integrated with a **stand-alone agentic tool** (such as [Gemini CLI](https://geminicli.com/) or Claude Code). See your local IDE's documentation for how to connect your IDE to an agent.
  * The **Looker extension for VS Code**.
  * An **MCP server** , such as the [Looker-managed MCP server](https://docs.cloud.google.com/looker/docs/mcp).



To learn more about the AI-enabled workflow, see the [AI-assisted development (vibe coding) with Looker](https://docs.cloud.google.com/looker/docs/ai-assisted-development-vscode) documentation page.

## Before you begin

Before you install the extension, you must meet the following requirements:

  * **Looker-managed MCP server (optional but recommended)** : If you plan to use AI-assisted development, connect your IDE and your AI agent to the Looker-managed MCP server. Instructions for setting up the MCP server appear on the [Looker-managed MCP server](https://docs.cloud.google.com/looker/docs/mcp) documentation page. See your tools' documentation for additional details.
  * **Looker permissions** : You must have the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) Looker permission for any models that you want to edit.
  * **Looker instance** : Your instance must be running Looker 26.6 or later.
  * **Project configuration** : You must have a project in Looker (either configured as a bare repository or [configured for Git](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#integrating_looker_with_git)).
  * **Git installation (optional)** : If you plan to clone your LookML repository, you must have [Git](https://git-scm.com/) installed on your local machine.
  * **OAuth Client ID** : If you're using OAuth authentication (recommended), you must obtain an OAuth Client ID from your Looker admin.



## Admin setup

If your organization uses OAuth for authentication, a Looker admin must register the Looker extension for VS Code as an OAuth client in the Looker Admin UI.

Use the Looker [API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) to set up OAuth integration. You can access the API Explorer using one of the following methods:

### API Explorer installed

If your Looker instance already has the API Explorer installed, you can access it with this URL format:
    
    
    LOOKER_INSTANCE_URL/extensions/marketplace_extension_api_explorer::api-explorer/
    

### API Explorer not installed

If your Looker instance doesn't have the API Explorer, you can install it from the Looker Marketplace. See the [Using the API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer#installing_the_api_explorer) page for information about how to install the API Explorer.

### PSA private instance

If you are using a Looker (Google Cloud core) private connections instance that uses [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa), the Looker Marketplace and API Explorer aren't supported. To register an AI agent, you must call the [`oauth_client_apps`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/register_oauth_client_app) API endpoint directly. If you use this method, you can skip the remaining steps of this API Explorer procedure.

The following is an example of a `curl` command that you can use with the `oauth_client_apps` endpoint to register the agent.
    
    
    curl -X POST "https://LOOKER_INSTANCE_URL/api/4.0/oauth_client_apps/CLIENT_GUID" \
    -H "Authorization: token ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "redirect_uri": "REDIRECT_URI",
      "display_name": "CLIENT_NAME",
      "description": "OAuth client to access MCP server using CLIENT_NAME",
      "enabled": true
    }'
    

To register the extension, complete the following steps:

  1. Follow the instructions in the [Registering an OAuth client application](https://docs.cloud.google.com/looker/docs/api-cors#registering_an_oauth_client_application) documentation to register the extension.
  2. For the `client_guid` field, complete the following steps:

     * Use any globally unique ID.
     * Be prepared to distribute the ID to any LookML developers who want to use the extension.
  3. For the `redirect_uri`, enter the callback URL for your IDE. Depending on your IDE or coding tool, use one of the following callback URLs:

IDE or tool | Callback URL  
---|---  
Antigravity IDE (available in Looker 26.12 or later) | 
         
         antigravity-ide://google.vscode-looker-official/oauth_callback  
  
Code-OSS | 
         
         code-oss://google.vscode-looker-official/oauth_callback  
  
Cursor | 
         
         cursor://google.vscode-looker-official/oauth_callback  
  
HTTPS | 
         
         https://google.vscode-looker-official/oauth_callback  
  
Kiro (OAuth support for Kiro is available in Looker 26.16 or later) | 
         
         kiro://google.vscode-looker-official/oauth_callback  
  
Looker | 
         
         looker://google.vscode-looker-official/oauth_callback  
  
VS Code | 
         
         vscode://google.vscode-looker-official/oauth_callback  
  
Windsurf | 
         
         windsurf://google.vscode-looker-official/oauth_callback  
  
**Note:** Looker validates custom URI schemes against an allowlist of supported IDEs and tools. If you attempt to register a redirect URI for an IDE whose scheme is not on Looker's allowlist, Looker will return an error during registration.
  4. Ensure that the **Enabled** field is set to `true`.

  5. Complete the `display_name` and `description` fields as described in the [Registering an OAuth client application](https://docs.cloud.google.com/looker/docs/api-cors#registering_an_oauth_client_application) documentation.




Once the app is registered, the API Explorer will return a response with a summary of the registration. Make sure that the redirect URI matches what you entered in the request parameter. You can use the **Get OAuth Client App** endpoint with the `client_guid` value to review your registration details.

Provide the generated `client_guid` value to your developers; they will use it when configuring the extension.

## Install the extension

The extension is available on both major extension marketplaces:

  * [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Google.vscode-looker-official) (for standard VS Code)
  * [Open VSX Registry](https://open-vsx.org/extension/Google/vscode-looker-official) (for Cursor, Antigravity IDE, and VSCodium)



Complete the following steps to install the extension:

  1. Open your IDE, such as VS Code or Cursor.
  2. Click the **Extensions** icon in the Activity Bar.
  3. Find **Looker by Google Cloud** and click **Install**.
  4. Once the extension is installed, the ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/looker-color.svg)**Looker** icon appears in the Activity Bar.



## Configure the extension

**Note:** We recommend configuring and managing your settings by using the onboarding walkthrough.

To configure the extension with your Looker instance details, run the interactive onboarding walkthrough:

  1. With a workspace open, open the Command Palette (**Command-Shift-P** on macOS or **Ctrl+Shift+P** on Windows/Linux).
  2. Run the **Looker: Show Onboarding Walkthrough** command to open the onboarding walkthrough.
  3. Follow the prompts in the walkthrough to enter your Looker instance URL, project ID, and authentication details. If you are using a bare repository, you will also be prompted to populate your workspace with the project's LookML files during this process.



### Authenticate with OAuth (Recommended)

OAuth 2.1 is the recommended authentication flow. When prompted during the onboarding walkthrough, choose OAuth and provide the following configuration values:

  * **Looker Instance URL** : The URL of your Looker instance.
  * **OAuth Client ID** : The OAuth client ID (`client_guid`) that you receive from your Looker administrator.
  * **Project ID** : The name of the LookML project that you want to edit. To find it, within your Looker instance, open the [**LookML Projects** page](https://docs.cloud.google.com/looker/docs/manage-projects). The project ID is in the **Project** column.



### Authenticate with API credentials

If you prefer to use Looker API keys, follow the documentation to [create API credentials](https://docs.cloud.google.com/looker/docs/api-auth#authentication_without_an_sdk). When prompted during the onboarding walkthrough, choose API credentials and provide the following configuration values:

  * **Looker Instance URL** : The URL of your Looker instance.
  * **Client ID** and **Client Secret** : The client ID and client secret for the API credentials that you're using to authenticate. To find these credentials, within your Looker instance, open your [**Account** page](https://docs.cloud.google.com/looker/docs/user-account); then, in the **API Keys** section, click the **Manage** button to view your client IDs and secrets.
  * **Project ID** : The name of the project that you want to edit. To find the project name, within your Looker instance, open the [**LookML Projects** page](https://docs.cloud.google.com/looker/docs/manage-projects). The project ID is in the **Project** column.

**Note:** You can't enter the `looker.clientSecret` manually in your workspace's `settings.json` file. Use the onboarding walkthrough to configure API credentials.

### Settings

**Note:** Managing these settings by using the onboarding walkthrough is recommended.

Although using the onboarding walkthrough is recommended, you can also configure extension settings in your VS Code `settings.json` file. This file is located either in your workspace `.vscode` folder (`.vscode/settings.json`) or in your global user settings file (`settings.json`). You can also configure them by using the visual VS Code Settings editor (**Preferences: Open Settings (UI)**).

**Tip:** Modify the workspace-level settings instead of global values, to isolate Looker instance and project details to the related LookML project directories.

All `looker.<setting>` properties must be defined in VS Code `settings.json` files, including the extension MCP setting `looker.mcpServerUrl`. Defining these settings in an AI agent's MCP configuration file (such as `.agents/mcp_config.json`) or other settings files will not work with the extension.

You can configure the following extension settings in `settings.json`:

Setting | Description | Default  
---|---|---  
`looker.instanceURL` | Base URL of the Looker instance (for example, `https://mycompany.looker.com`). | -  
`looker.authURL` | URL to use for OAuth authentication. Only set if different from your instance URL. | `looker.instanceURL`  
`looker.sdkURL` | URL to use for API requests. Only set if different from your instance URL. | `looker.instanceURL`  
`looker.oauthClientId` | Looker OAuth Client ID. Required for OAuth. | -  
`looker.clientId` | Looker API Client ID. Required for API Key auth. | -  
`looker.clientSecret` | Looker API Client Secret. _Deprecated._ Use the onboarding walkthrough to configure API credentials. | -  
`looker.projectId` | LookML project ID. | -  
`looker.mcpServerUrl` | URL of the target MCP server that the extension's local MCP proxy forwards requests to. Only set if different from `looker.instanceURL/mcp` (for example, `http://localhost:5000/mcp`). | `looker.instanceURL/mcp`  
`looker.acceptSelfSignedCertificates` | Ignore SSL certificate errors (for example, for self-signed certificates). **Warning: Enabling this option is not recommended.** | `false`  
`looker.askBeforeOverwritingRemote` | Always ask before overwriting remote files when a conflict is detected. | `false`  
  
## Configure your MCP client

To enable your AI agent to interact with Looker through the extension, you must configure your agent to connect to the extension's local MCP proxy at `http://127.0.0.1:5050/mcp`.

Your AI agent references its own MCP configuration file (such as `.agents/mcp_config.json` in VS Code, `.mcp.json` in Claude Code, or `.cursor/mcp.json` in Cursor). Pointing this configuration to the local proxy lets the extension capture your agent's MCP requests and forward them with the appropriate authentication headers.

### Looker-managed MCP server (default and recommended)

The extension runs a local reverse proxy (default: `http://127.0.0.1:5050/mcp`) that connects to Looker's built-in managed MCP server (`LOOKER_INSTANCE_URL/mcp`). The proxy automatically injects OAuth bearer tokens and buffers AI agent tool requests until pending local file synchronizations are completed, ensuring that validation tools never evaluate stale code on the server.

### Custom or self-hosted MCP server (optional)

If your organization hosts a custom MCP server (such as the [stand-alone MCP Toolbox for Databases](https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox)):

  1. In VS Code settings, set `looker.mcpServerUrl` to your custom server URL (for example, `http://localhost:5000/mcp`).
  2. Configure your IDE's MCP client to point to the extension proxy at `http://127.0.0.1:5050/mcp`.



### Visual Studio Code (Copilot)

  1. Open [VS Code](https://code.visualstudio.com/docs/copilot/overview) and create the `.agents` directory in your project root, if it doesn't already exist. 
  2. Create the `.agents/mcp_config.json` file, if it doesn't already exist, and open it.
  3. Add the following configuration and save the file: 


    
    
          {
            "mcpServers": {
              "Looker": {
                "serverUrl": "http://127.0.0.1:5050/mcp",
                "disabledTools": [
                  "query_url",
                  "get_looks",
                  "run_look",
                  "make_look",
                  "get_dashboards",
                  "run_dashboard",
                  "make_dashboard",
                  "add_dashboard_element",
                  "add_dashboard_filter",
                  "generate_embed_url",
                  "health_pulse",
                  "health_analyze",
                  "health_vacuum",
                  "get_project_files",
                  "get_project_file",
                  "create_project_file",
                  "update_project_file",
                  "delete_project_file",
                  "get_project_directories",
                  "create_project_directory",
                  "delete_project_directory",
                  "project_git_branch"
                ]
              }
            }
          }
      

### Claude Code

  1. Create the `.mcp.json` file in your project root, if it doesn't already exist. 
  2. Add the following configuration and save the file: 


    
    
          {
            "mcpServers": {
              "Looker": {
                "type": "http",
                "url": "http://127.0.0.1:5050/mcp"
              }
            }
          }
      

### Cursor

  1. Create the `.cursor` directory in your project root, if it doesn't already exist.
  2. Create the `.cursor/mcp.json` file, if it doesn't already exist, and open it.
  3. Add the following configuration and save the file: 


    
    
          {
            "mcpServers": {
              "Looker": {
                "type": "http",
                "url": "http://127.0.0.1:5050/mcp"
              }
            }
          }
      

  4. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects.



### Cline

  1. Open the [Cline](https://github.com/cline/cline) extension in VS Code and click the **MCP Servers** icon.
  2. Click **Configure MCP Servers** to open the configuration file.
  3. Add the following configuration and save the file: 


    
    
          {
            "mcpServers": {
              "Looker": {
                "type": "http",
                "url": "http://127.0.0.1:5050/mcp"
              }
            }
          }
      

### Windsurf

  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to Cascade assistant.
  2. Click the MCP icon, and then click **Configure** to open the configuration file.
  3. Add the following configuration and save the file: 


    
    
          {
            "mcpServers": {
              "Looker": {
                "type": "http",
                "url": "http://127.0.0.1:5050/mcp"
              }
            }
          }
      

## Authenticate through Looker

If you're using OAuth authentication, you must sign in to link your local IDE to your Looker account.

  1. Open the Command Palette.
  2. Run the command: **Looker: Sign In (OAuth)**.
  3. Acknowledge the prompt to open your browser.
  4. In the browser, authorize the extension to access your Looker account.
  5. After authorizing, the browser redirects back to your IDE. You should see a notification stating **Successfully signed in to Looker!**



## Populate your local LookML project

To begin development, open your LookML project in your local IDE by using the appropriate method for your repository configuration:

### Git repository

If your LookML project is configured for Git, follow these steps:

  1. In VS Code, open a new window.
  2. Open the Command Palette and select **Git: Clone**.
  3. Enter the URL of your remote Git repository (for example, from GitHub or GitLab) and choose a local folder.
  4. Open the cloned folder in your IDE.



### Bare repository mode

If your LookML project is configured as a [bare repository](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#configuring_a_bare_git_repository), follow these steps:

  1. With a workspace open, create and open an empty local folder for your project.
  2. Open the Command Palette (**Command-Shift-P** on macOS or **Ctrl+Shift+P** on Windows/Linux).
  3. Run the **Looker: Show Onboarding Walkthrough** command to open the onboarding walkthrough.
  4. In the **Select Project** step, select the LookML project that you want to work on and click **Next**.
  5. The extension recognizes that your local folder is empty and prompts you to populate the workspace with the project's files. Click **Populate Workspace** to populate the workspace.
  6. Complete the onboarding walkthrough.



Once the workspace is populated, the extension automatically begins synchronizing your local folder with your checked-out branch in your Looker instance's Development Mode.

## Troubleshooting

You can view extension logs in your IDE's **Output** panel. Select the **Looker** channel to view logs. For more detailed logs, open the Command Palette, run the **Developer: Set Log Level** command, and select **Debug** or **Trace**.

  * **Authentication errors** : Verify that your `looker.instanceURL` and `looker.oauthClientId` are correct. Ensure that the redirect URI in Looker matches exactly.
  * **Sync issues** : Check extension logs to address sync issues. To view logs, open the **Output** panel and select **Looker** from the drop-down menu.
  * **Bad Request response during OAuth** : Ensure your Looker instance is accessible from your local network and that you have a valid internet connection.



If you encounter issues with the extension, running the **Developer: Reload Window** command from the Command Palette can help resolve them.

## What's next

  * [Managing LookML files and Git with the Looker extension for VS Code](https://docs.cloud.google.com/looker/docs/manage-lookml-files-git-vscode)
  * [Looker-managed MCP server](https://docs.cloud.google.com/looker/docs/mcp)
  * [Use the MCP Toolbox for Databases](https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox)
  * [AI-assisted development (vibe coding) with Looker](https://docs.cloud.google.com/looker/docs/ai-assisted-development-vscode)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
