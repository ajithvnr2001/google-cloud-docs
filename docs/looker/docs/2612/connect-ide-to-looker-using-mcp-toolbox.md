---
url: https://docs.cloud.google.com/looker/docs/2612/connect-ide-to-looker-using-mcp-toolbox/
title: Use the MCP Toolbox for Databases \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:25:19.387455+00:00
---

# Use the MCP Toolbox for Databases  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2612/connect-ide-to-looker-using-mcp-toolbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the MCP Toolbox for Databases

**Note:** The **Looker-managed MCP server** is the recommended method for connecting AI applications to Looker instances that are hosted by Looker. It provides a built-in, secure, and zero-infrastructure integration directly within the Looker platform. For setup instructions, see the [**Looker-managed MCP server** documentation page](https://docs.cloud.google.com/looker/docs/2612/mcp).

This page shows you how to use the [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) to connect your Looker instance to integrated development environments (IDEs) and developer tools that support the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). The MCP Toolbox is a good option if you're using a **customer-hosted instance** , or if you prefer to manage your own infrastructure. Otherwise, we recommend using the [Looker-managed MCP server](https://docs.cloud.google.com/looker/docs/2612/mcp) instead.

We recommend using the dedicated Looker extension for [Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) with the MCP Toolbox. Use Looker's semantic layer to provide the Gemini CLI with secure, governed, and on-demand access to trusted data, and accelerate workflows by automating the creation of reports, visualizations, and dashboards from natural language prompts. As Google Cloud's next-generation command-line interface, the Gemini CLI is the recommended tool for interacting with your Looker instances from the command line.

You can also connect other integrated development environments (IDEs) and developer tools that support the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) by using the general-purpose [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox). The MCP Toolbox is an open-source MCP server that simplifies connecting AI agents to your data by handling complexities like authentication and connection pooling, which lets you interact with your data using natural language directly from your IDE. For these tools, this method provides core database interaction capabilities.

**Note:** The MCP Toolbox is an open-source project provided "as-is". It is not a supported Google Cloud product and is not covered by the Google Cloud Technical Support Services Guidelines or SLAs. For support, see the project's [GitHub Issues page](https://github.com/googleapis/mcp-toolbox/issues).

## About Gemini CLI and extensions

Gemini CLI is an open-source AI agent that's designed to accelerate development workflows by assisting with coding, debugging, data exploration, and content creation. Its mission is to provide an elegant agentic experience for interacting with data cloud services and popular open-source databases.

### How extensions work

Gemini CLI is highly extensible, allowing for the addition of new tools and capabilities through extensions. These extensions are straightforward to install. You can load them from a GitHub URL, a local directory, or a configurable registry. These extensions provide a rich set of capabilities, including new tools, slash commands, and prompts to streamline your workflow.

## Prepare Looker authentication

You have two options to authenticate your MCP client with Looker: you can either use standard API credentials or you can authenticate the client through through an OAuth application registration.

### Option 1: API credentials

  1. Get a Looker Client ID and Client Secret. Follow the directions on the [Looker API authentication](https://docs.cloud.google.com/looker/docs/2612/api-auth#authentication_with_an_sdk) documentation page.
  2. Have the base URL of your Looker instance available. It is likely something like `https://looker.example.com`. In some cases the API is listening at a different port, and you will need to use `https://looker.example.com:19999` instead.



### Option 2: OAuth application registration

  1. Open the [Looker API Explorer](https://docs.cloud.google.com/looker/docs/2612/api-explorer#starting_the_api_explorer).

### API Explorer installed

If your Looker instance already has the API Explorer installed, you can access it with this URL format:
         
         LOOKER_INSTANCE_URL/extensions/marketplace_extension_api_explorer::api-explorer/
         

### API Explorer not installed

If your Looker instance doesn't have the API Explorer, you can install it from the Looker Marketplace. See the [Using the API Explorer](https://docs.cloud.google.com/looker/docs/2612/api-explorer#installing_the_api_explorer) page for information about how to install the API Explorer.

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
         

  2. Under the **Auth** method, find the **Register OAuth App** API endpoint. You can also search for "oauth app" in the **Search** field.

  3. Select **Run It**.

  4. For the **`client_guid`** , enter a custom string (for example, `gemini_cli` or `claude-desktop`).

  5. In the request body, enter the following JSON configuration:
         
         {
           "redirect_uri": "AI_AGENT_REDIRECT_URI",
           "display_name": "APPLICATION_NAME",
           "description": "APPLICATION_DESCRIPTION",
           "enabled": true
         }
         

Replace the following:

     * `AI_AGENT_REDIRECT_URI`: The redirect URI for your AI agent extension or shared service application.

       * For Cloud-hosted applications, it may look like a secure HTTPS URL: `https://AI_AGENT_URL/oauth2callback`
       * For applications running locally, it should be a localhost URL with a static port: `http://localhost:7777/oauth/callback`

**Note:** Some tools, such as the Gemini CLI, may require you to set an environment variable (for example, `export OAUTH_CALLBACK_PORT=7777`) to ensure that the tools use a static port that matches your registered redirect URI.
       * For IDEs, it may look like the following: `vscode://google.vscode-looker-official/oauth_callback`

     * `APPLICATION_NAME`: The display name for your OAuth application—for example, `Claude Desktop`.

     * `APPLICATION_DESCRIPTION`: A short description of your OAuth application.

  6. Check the confirmation box next to **I understand that this API endpoint will change data** , and then select **Run**.




## Install MCP Toolbox

**Note:** If you are using the Gemini CLI or Gemini Code Assist to connect to your Looker instance by using the [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox), you don't need to install MCP Toolbox. MCP Toolbox will be installed when the Gemini extension is installed during the configuration step.

  1. Download the latest version of MCP Toolbox as a binary. Select the [binary](https://github.com/googleapis/mcp-toolbox/releases) that corresponds to your OS and CPU architecture. You must use MCP Toolbox version V1.0.0 or later.

### linux/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/v1.0.0/linux/amd64/toolbox
         

### darwin/arm64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/v1.0.0/darwin/arm64/toolbox
         

### darwin/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/v1.0.0/darwin/amd64/toolbox
         

### windows/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/v1.0.0/windows/amd64/toolbox.exe
         

  2. Make the binary an executable.
         
         chmod +x toolbox
         

  3. Verify the installation.
         
         ./toolbox --version
         




## Run MCP Toolbox as a shared service

For MCP clients that require OAuth authentication over HTTPS, you must deploy the MCP Toolbox behind an HTTPS reverse proxy (such as Cloud Run). The reverse proxy terminates SSL and forwards requests to the MCP Toolbox container.

### Configure the server environment

  1. Set the following environment variables in your deployment: 

     * `LOOKER_BASE_URL=YOUR_LOOKER_BASE_URL`
     * `LOOKER_USE_CLIENT_OAUTH=true`
  2. Run the MCP Toolbox with the following arguments: 

     * `--prebuilt=looker,looker-dev`
     * `--mcp-prm-file=prm.json`
     * `[--address=0.0.0.0]`
     * `[--port=8080]`

MCP Toolbox normally listens on `127.0.0.1` port `5000`. If the reverse proxy is on another host, use `--address=0.0.0.0` to bind to all IP addresses. Use the `--port=` setting if you need to use a listening port other than `5000`. For example, Cloud Run automatically forwards external traffic from port `443`, the HTTPS port, to `8080`.

  3. Create a Protected Resource Metadata (PRM) configuration file (`prm.json`) with the following structure: 
         
         {
         "resource": "https://PROXY_URL/mcp",
         "authorization_servers": ["LOOKER_URL"],
         "scopes_supported": ["cors_api"]
         }
         

Replace the following:

     * `PROXY_URL`: The domain and base path of your reverse proxy server.
     * `LOOKER_URL`: The base URL of your Looker instance.



For an example of how to configure the client when you're running MCP Toolbox as a shared service, see the example [Claude desktop configuration](https://docs.cloud.google.com/looker/docs/2612/connect-ide-to-looker-using-mcp-toolbox#mcp-configure-your-mcp-client-claudedesktop).

## Configure the MCP client

This section describes how to configure various developer tools to connect to your Looker instance using the [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox). The toolbox acts as an open-source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that sits between your IDE and your database, providing a secure and efficient control plane for your AI tools. Select the tab for your specific tool to see the configuration instructions.

  * Gemini CLI
  * Gemini Code Assist
  * Claude code
  * Claude desktop
  * Cline (VS Code extension)
  * Cursor
  * Visual Studio Code  (Copilot)
  * Windsurf (Codium)



### Gemini CLI

Choose the connection method that's based on your authentication choice:

#### Option 1: API credentials with extension

  1. Install the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation).
  2. Install the Looker extension for Gemini CLI from the GitHub repository using the following command: 
         
         gemini extensions install https://github.com/gemini-cli-extensions/looker
         

  3. Set environment variables to connect to your Looker instance, replacing the following environment variables with your values: 
     * `LOOKER_URL`: The URL of your Looker instance.
     * `CLIENT_ID` and `CLIENT_SECRET`: The [API key](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-users#api_keys) that is used to access the [Looker API](https://docs.cloud.google.com/looker/docs/2612/api-auth).
     * `VERIFY_SSL`: Either `true` or `false`, depending on whether you use [SSL encryption](https://docs.cloud.google.com/looker/docs/2612/enabling-secure-db-access#option_2_ssl_encryption) to connect your database to your Looker instance.
    
    export LOOKER_BASE_URL="LOOKER_URL"
    export LOOKER_CLIENT_ID="CLIENT_ID"
    export LOOKER_CLIENT_SECRET="CLIENT_SECRET"
    export LOOKER_VERIFY_SSL="VERIFY_SSL"
    

  4. Start the Gemini CLI in interactive mode: 
         
         gemini
         

The CLI automatically loads the Looker extension for Gemini CLI extension and its tools, which you can use to interact with your Looker instance. 



#### Option 2: Remote shared service with OAuth

To connect to a remote shared service using OAuth, do not install the Looker extension. Instead, configure the Gemini CLI to connect directly to your remote MCP server.

  1. Install the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation).
  2. Add the remote MCP server using the following command, replacing `PROXY_URL` with the domain of your reverse proxy server: 
         
         gemini mcp add --transport http looker https://PROXY_URL/mcp
         

Alternatively, you can configure this manually by adding the following configuration to your `settings.json` file (located in `~/.gemini/settings.json` or your project directory):
         
         {
           "mcpServers": {
             "looker": {
               "httpUrl": "https://PROXY_URL/mcp"
             }
           }
         }
         

  3. Start the Gemini CLI in interactive mode: 
         
         gemini
         

When prompted to connect, the CLI initiates the OAuth authorization flow to securely authenticate with your Looker instance. 



### Gemini Code Assist

We recommend to configure Gemini Code Assist to use the Gemini CLI. This approach removes the need to manually configure an MCP server.

  1. Make sure that you have installed and configured the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation) and either the [`looker` extension](https://github.com/gemini-cli-extensions/looker) (for API credentials) or a remote MCP server configuration (for shared service with OAuth).
  2. [Configure Gemini Code Assist to use the Gemini CLI](https://developers.google.com/gemini-code-assist/docs/set-up-gemini-standard-enterprise).
  3. Start interacting with your Looker instance using natural language directly within the Gemini Code Assist chat.



### Claude code

Choose the connection method that's based on your authentication choice:

#### Option 1: API credentials

  1. Install [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).
  2. Create the `.mcp.json` file in your project root, if it doesn't exist. 
  3. Add the following configuration, replacing the following environment variables with your values, and then save. 
     * `LOOKER_URL`: The URL of your Looker instance.
     * `CLIENT_ID` and `CLIENT_SECRET`: The [API key](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-users#api_keys) that is used to access the [Looker API](https://docs.cloud.google.com/looker/docs/2612/api-auth).
     * `VERIFY_SSL`: Either `true` or `false`, depending on whether you use [SSL encryption](https://docs.cloud.google.com/looker/docs/2612/enabling-secure-db-access#option_2_ssl_encryption) to connect your database to your Looker instance.


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "command": "./PATH/TO/toolbox",
                "args": ["--stdio", "--prebuilt", "looker"],
                "env": {
                    "LOOKER_BASE_URL": "LOOKER_URL",
                    "LOOKER_CLIENT_ID": "CLIENT_ID",
                    "LOOKER_CLIENT_SECRET": "CLIENT_SECRET",
                    "LOOKER_VERIFY_SSL": "VERIFY_SSL",
              }
              }
            }
          }
      

#### Option 2: Remote shared service with OAuth

  1. Install [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).
  2. Create the `.mcp.json` file in your project root, if it doesn't exist. 
  3. Add the following configuration, replacing `PROXY_URL` with the domain of your reverse proxy server, and then save. 


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "type": "http",
                "url": "https://PROXY_URL/mcp"
              }
            }
          }
      

### Claude desktop

Choose the connection method that's based on your authentication choice:

#### Option 1: API credentials

  1. Open [Claude desktop](https://claude.ai/download) and navigate to **Settings**.
  2. In the **Developer** tab, click **Edit Config** to open the configuration file.
  3. Add the following configuration, replacing the following environment variables with your values, and then save. 
     * `LOOKER_URL`: The URL of your Looker instance.
     * `CLIENT_ID` and `CLIENT_SECRET`: The [API key](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-users#api_keys) that is used to access the [Looker API](https://docs.cloud.google.com/looker/docs/2612/api-auth).
     * `VERIFY_SSL`: Either `true` or `false`, depending on whether you use [SSL encryption](https://docs.cloud.google.com/looker/docs/2612/enabling-secure-db-access#option_2_ssl_encryption) to connect your database to your Looker instance.


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "command": "./PATH/TO/toolbox",
                "args": ["--stdio", "--prebuilt", "looker"],
                "env": {
                    "LOOKER_BASE_URL": "LOOKER_URL",
                    "LOOKER_CLIENT_ID": "CLIENT_ID",
                    "LOOKER_CLIENT_SECRET": "CLIENT_SECRET",
                    "LOOKER_VERIFY_SSL": "VERIFY_SSL",
              }
              }
            }
          }
      

#### Option 2: Remote shared service with OAuth

  1. In Claude desktop, navigate to **Settings** and select **Connectors**.
  2. Choose **Add custom connector** and enter a name (for example, **Looker**).
  3. For the URL, enter the endpoint of your reverse proxy server with the `/mcp` path appended (for example, `https://looker-mcp-toolbox.example.com/mcp`).
  4. Under **Advanced settings** , enter the exact string that you used for the `client_guid` during your OAuth app registration. Leave the OAuth client secret blank.
  5. Select **Add** to save the connector. When prompted to connect, Claude desktop securely initiates the PKCE authorization flow through your browser.


  4. Restart Claude desktop.



### Cline

Choose the connection method that's based on your authentication choice:

#### Option 1: API credentials

  1. Open the [Cline](https://github.com/cline/cline) extension in VS Code and click the **MCP Servers** icon.
  2. Click **Configure MCP Servers** to open the configuration file.
  3. Add the following configuration, replacing the following environment variables with your values, and then save. 
     * `LOOKER_URL`: The URL of your Looker instance.
     * `CLIENT_ID` and `CLIENT_SECRET`: The [API key](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-users#api_keys) that is used to access the [Looker API](https://docs.cloud.google.com/looker/docs/2612/api-auth).
     * `VERIFY_SSL`: Either `true` or `false`, depending on whether you use [SSL encryption](https://docs.cloud.google.com/looker/docs/2612/enabling-secure-db-access#option_2_ssl_encryption) to connect your database to your Looker instance.


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "command": "./PATH/TO/toolbox",
                "args": ["--stdio", "--prebuilt", "looker"],
                "env": {
                    "LOOKER_BASE_URL": "LOOKER_URL",
                    "LOOKER_CLIENT_ID": "CLIENT_ID",
                    "LOOKER_CLIENT_SECRET": "CLIENT_SECRET",
                    "LOOKER_VERIFY_SSL": "VERIFY_SSL",
              }
              }
            }
          }
      

A green active status appears after the server connects successfully. 

#### Option 2: Remote shared service with OAuth

  1. Open the [Cline](https://github.com/cline/cline) extension in VS Code and click the **MCP Servers** icon.
  2. Click **Configure MCP Servers** to open the configuration file.
  3. Add the following configuration, replacing `PROXY_URL` with the domain of your reverse proxy server, and then save. 


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "type": "http",
                "url": "https://PROXY_URL/mcp"
              }
            }
          }
      

A green active status appears after the server connects successfully. 

### Cursor

Choose the connection method that's based on your authentication choice:

#### Option 1: API credentials

  1. Create the `.cursor` directory in your project root if it doesn't exist.
  2. Create the `.cursor/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replacing the following environment variables with your values, and then save. 
     * `LOOKER_URL`: The URL of your Looker instance.
     * `CLIENT_ID` and `CLIENT_SECRET`: The [API key](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-users#api_keys) that is used to access the [Looker API](https://docs.cloud.google.com/looker/docs/2612/api-auth).
     * `VERIFY_SSL`: Either `true` or `false`, depending on whether you use [SSL encryption](https://docs.cloud.google.com/looker/docs/2612/enabling-secure-db-access#option_2_ssl_encryption) to connect your database to your Looker instance.


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "command": "./PATH/TO/toolbox",
                "args": ["--stdio", "--prebuilt", "looker"],
                "env": {
                    "LOOKER_BASE_URL": "LOOKER_URL",
                    "LOOKER_CLIENT_ID": "CLIENT_ID",
                    "LOOKER_CLIENT_SECRET": "CLIENT_SECRET",
                    "LOOKER_VERIFY_SSL": "VERIFY_SSL",
              }
              }
            }
          }
      

  4. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects.



#### Option 2: Remote shared service with OAuth

  1. Create the `.cursor` directory in your project root if it doesn't exist.
  2. Create the `.cursor/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replacing `PROXY_URL` with the domain of your reverse proxy server, and then save. 


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "type": "http",
                "url": "https://PROXY_URL/mcp"
              }
            }
          }
      

  4. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects.



### Visual Studio Code (Copilot)

Choose the connection method that's based on your authentication choice:

#### Option 1: API credentials

  1. Open [VS Code](https://code.visualstudio.com/docs/copilot/overview) and create the `.vscode` directory in your project root if it doesn't exist. 
  2. Create the `.vscode/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replacing the following environment variables with your values, and then save. 
     * `LOOKER_URL`: The URL of your Looker instance.
     * `CLIENT_ID` and `CLIENT_SECRET`: The [API key](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-users#api_keys) that is used to access the [Looker API](https://docs.cloud.google.com/looker/docs/2612/api-auth).
     * `VERIFY_SSL`: Either `true` or `false`, depending on whether you use [SSL encryption](https://docs.cloud.google.com/looker/docs/2612/enabling-secure-db-access#option_2_ssl_encryption) to connect your database to your Looker instance.


    
    
          {
            "servers": {
              "looker-toolbox": {
                "command": "./PATH/TO/toolbox",
                "args": ["--stdio", "--prebuilt", "looker"],
                "env": {
                    "LOOKER_BASE_URL": "LOOKER_URL",
                    "LOOKER_CLIENT_ID": "CLIENT_ID",
                    "LOOKER_CLIENT_SECRET": "CLIENT_SECRET",
                    "LOOKER_VERIFY_SSL": "VERIFY_SSL",
              }
              }
            }
          }
      

#### Option 2: Remote shared service with OAuth

  1. Open [VS Code](https://code.visualstudio.com/docs/copilot/overview) and create the `.vscode` directory in your project root if it doesn't exist. 
  2. Create the `.vscode/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replacing `PROXY_URL` with the domain of your reverse proxy server, and then save. 


    
    
          {
            "servers": {
              "looker-toolbox": {
                "type": "http",
                "url": "https://PROXY_URL/mcp"
              }
            }
          }
      

### Windsurf

Choose the connection method that's based on your authentication choice:

#### Option 1: API credentials

  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to Cascade assistant.
  2. Click the MCP icon, then click **Configure** to open the configuration file.
  3. Add the following configuration, replacing the following environment variables with your values, and then save. 
     * `LOOKER_URL`: The URL of your Looker instance.
     * `CLIENT_ID` and `CLIENT_SECRET`: The [API key](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-users#api_keys) that is used to access the [Looker API](https://docs.cloud.google.com/looker/docs/2612/api-auth).
     * `VERIFY_SSL`: Either `true` or `false`, depending on whether you use [SSL encryption](https://docs.cloud.google.com/looker/docs/2612/enabling-secure-db-access#option_2_ssl_encryption) to connect your database to your Looker instance.


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "command": "./PATH/TO/toolbox",
                "args": ["--stdio", "--prebuilt", "looker"],
                "env": {
                    "LOOKER_BASE_URL": "LOOKER_URL",
                    "LOOKER_CLIENT_ID": "CLIENT_ID",
                    "LOOKER_CLIENT_SECRET": "CLIENT_SECRET",
                    "LOOKER_VERIFY_SSL": "VERIFY_SSL",
              }
              }
            }
          }
      

#### Option 2: Remote shared service with OAuth

  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to Cascade assistant.
  2. Click the MCP icon, then click **Configure** to open the configuration file.
  3. Add the following configuration, replacing `PROXY_URL` with the domain of your reverse proxy server, and then save. 


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "type": "http",
                "url": "https://PROXY_URL/mcp"
              }
            }
          }
      

## Use AI tools

Your AI tool is now connected to Looker using MCP. Try asking your AI assistant to list models, Explores, dimensions, and measures. You can also run a query by retrieving the SQL for a query or running a saved Look.

The following tools are available to the LLM:

### Looker Model and Query Tools

These tools are used to get information about a Looker model and execute queries against that model.

  * `get_models`: List all LookML models on your Looker instance.
  * `get_explores`: List the explores in a given model.
  * `get_dimensions`: List the dimensions in a given Explore.
  * `get_measures`: List the measures in a given Explore.
  * `get_filters`: List the filters in a given Explore.
  * `get_parameters`: List the parameters in a given Explore.
  * `query`: Run a query and return the data.
  * `query_sql`: Return the SQL that is generated by Looker for a query.
  * `query_url`: Return a link to the query in Looker for further exploration.



### Looker Content Tools

These tools get saved content (Looks and Dashboards) from a Looker instance and create new saved content.

  * `get_looks`: Return the saved Looks that match a title or description.
  * `run_look`: Run a saved Look and return the data.
  * `make_look`: Create a saved Look in Looker and return the URL.
  * `get_dashboards`: Return the saved dashboards that match a title or description.
  * `make_dashboard`: Create a saved dashboard in Looker and return the URL.
  * `add_dashboard_element`: Add a tile to a dashboard.



### Looker Instance Health Tools

These tools offer the same health check algorithms that the popular CLI [Henry](https://github.com/looker-open-source/henry) offers.

  * `health_pulse`: Check the health of a Looker instance.
  * `health_analyze`: Analyze the usage of a Looker object.
  * `health_vacuum`: Find LookML elements that might be unused.



### LookML Authoring Tools

These tools allow enable the caller to write and modify LookML files as well as get the database schema needed to write LookML effectively.

  * `dev_mode`: Turn [Development Mode](https://docs.cloud.google.com/looker/docs/2612/dev-mode-prod-mode#development_mode) on and off for the session. LookML authoring must be done in Development Mode. Queries that are run in Development Mode use the modified LookML so you can test the impact of your changes.
  * `get_projects`: Get the list of available LookML projects.
  * `get_project_files`: Get the list of LookML files in a project.
  * `get_project_file`: Get the content of a LookML file.
  * `create_project_file`: Create a new LookML file.
  * `update_project_file`: Modify an existing LookML file.
  * `delete_project_file`: Delete a LookML file.
  * `get_connections`: Get the list of connections.
  * `get_connection_schemas`: Get the list of schemas for a connection.
  * `get_connection_databases`: Get the list of databases for a connection.
  * `get_connection_tables`: Get the list of tables for a connection.
  * `get_connection_table_columns`: Get the list of columns for a table in a connection.

**Note:** Prebuilt tools are pre-1.0, so expect some tool changes between versions. Because LLMs adapt to the tools that are available, most users won't be affected.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
