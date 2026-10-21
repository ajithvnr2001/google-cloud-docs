---
url: https://docs.cloud.google.com/looker/docs/2608/mcp/
title: Looker-managed MCP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:57:46.314311+00:00
---

# Looker-managed MCP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2608/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Looker-managed MCP server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Provide feedback or report issues with this preview feature by sending a detailed email to [looker-mcp-support-external@google.com](mailto:looker-mcp-support-external@google.com).

The **Looker-managed MCP server** is a built-in integration that embeds a Model Context Protocol (MCP) server directly into the Looker platform. It allows AI agents — such as Gemini CLI, Claude Desktop, Cursor, and Copilot — to securely connect to a Looker instance and interact with business data and LookML models.

By hosting the server, Looker removes the need for you to deploy and maintain your own middleware infrastructure, providing a plug-and-play, secure, and governed gateway to trusted business insights.

The Looker-managed MCP server is in preview for Looker (Google Cloud core) and Looker (original) instances. Customer-hosted (on-premise) instances are not supported for this preview.

If you're using a customer-hosted instance, or if you prefer to manage your own infrastructure, you can connect using the standalone [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox). The MCP Toolbox is an open-source MCP server that you can run on your local computer or on your own server to act as a bridge between AI agents and your Looker instance. See the [Use Looker with MCP, Gemini CLI and other agents](https://docs.cloud.google.com/looker/docs/2608/connect-ide-to-looker-using-mcp-toolbox) documentation page for more information.

## Before you begin

To use the Looker-managed MCP server, you must meet the following requirements:

### Instance requirements

  * You must be using a Looker (Google Cloud core) or a Looker (original) instance.
  * The instance must be hosted by Looker.



### Required permissions

  * **To[manage tool access](https://docs.cloud.google.com/looker/docs/2608/admin-panel-platform-mcp#model_context_protocol_mcp_settings)**: you must have the [**Admin**](https://docs.cloud.google.com/looker/docs/2608/admin-panel-users-roles#default_roles) Looker role.
  * **Toregister your AI agent as an OAuth client using the API Explorer**: you must have the [**Admin**](https://docs.cloud.google.com/looker/docs/2608/admin-panel-users-roles#default_roles) Looker role.
  * **To connect an AI agent to the Looker-managed MCP server** : you need your standard Looker login credentials to authenticate during the OAuth connection process. The AI agent must first be registered as an OAuth client by a Looker admin. Once connected, the AI agent will inherit the Looker roles and access of the user who authenticated.



## Set up the managed MCP server

Configure tool access to set up the managed MCP server.

### Configure tool settings

By default, all tools are disabled for the managed MCP server. Looker admins must explicitly enable the tools that AI agents are allowed to use. See the [**Admin settings - Model Context Protocol (MCP)**](https://docs.cloud.google.com/looker/docs/2608/admin-panel-platform-mcp) documentation page for steps to enable tools.

## Register an AI agent through OAuth

During the preview launch, Looker admins must manually register an AI agent in order to connect the agent to the managed MCP server.

  1. Open the [Looker API Explorer](https://docs.cloud.google.com/looker/docs/2608/api-explorer#starting_the_api_explorer).

     * If your Looker instance already has the API Explorer installed, you can access it with this URL format:
           
           https://LOOKER_INSTANCE_URL/extensions/marketplace_extension_api_explorer::api-explorer/
           

     * If your Looker instance doesn't have the API Explorer, you can install it from the Looker Marketplace. See the [Using the API Explorer](https://docs.cloud.google.com/looker/docs/2608/api-explorer#installing_the_api_explorer) page for information.

     * If you are using a Looker (Google Cloud core) private connections instance that uses [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa), the Looker Marketplace and API Explorer aren't supported. To register an AI agent, you must call the [`oauth_client_apps`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/register_oauth_client_app) API endpoint directly. If you use this method, you can skip the following API Explorer procedure and proceed directly to the Configure an MCP client section.

#### Expand this section to see an example of a `curl` command that you can use with the `oauth_client_apps` endpoint to register the agent.
           
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

  3. On the **Register OAuth App** page, click the **Run It** button.

  4. In the **Request** tab of the **Run It** dialog, enter the following information into the corresponding fields:

     * For the `client_guid` field, complete the following steps:

       * If the agent prescribes a specific client ID, use that client ID.
       * If the agent doesn't prescribe a specific client ID, use any globally unique ID.
       * Be prepared to distribute the ID to any LookML developers who want to use the agent.
**Tip:** Enter your the `client_guid` value here for use later in the procedure: client_guid.
     * For the `redirect_uri`, the URI varies depending on the AI agent application. You can refer to your agent's OAuth authentication documentation for its specific redirect URL. The format may look like one of the following examples:

###  Gemini CLI 
           
           http://localhost:7777/oauth/callback
           

**Note:** Some tools, such as the Gemini CLI, may require you to set an environment variable (for example, `export OAUTH_CALLBACK_PORT=7777`) to ensure that the tools use a static port that matches your registered redirect URI.

###  Gemini Code Assist
           
           http://localhost:7777/oauth/callback
           

We recommend using Gemini CLI with Gemini Code Assist, in which case they share the same local callback server and port configuration.

###  Claude code 

Claude Code uses a random available port for OAuth callback, but you should fix it using the `--callback-port 8080` flag (or with the `callbackPort` setting in `mcp.json`) to match your registered URI. 
           
           http://localhost:8080/callback
           

###  VS Code & other IDEs 

For IDEs, the redirect URI may look something like this, customized for your IDE.
           
           vscode://google.vscode-looker-official/oauth_callback
           

###  Cloud-hosted apps 

For Cloud-hosted applications, it may look like a secure HTTPS URL:
           
           https://AI_AGENT_URL/oauth2callback
           

###  Local apps 

For applications running locally, it should be a localhost URL with a static port:
           
           http://localhost:7777/oauth/callback
           

**Note:** Some tools, such as the Gemini CLI, may require you to set an environment variable (for example, `export OAUTH_CALLBACK_PORT=7777`) to ensure that the tools use a static port that matches your registered redirect URI.

     * Complete the `display_name` and `description` as described in the [Registering an OAuth client application](https://docs.cloud.google.com/looker/docs/2608/api-cors#registering_an_oauth_client_application) documentation.

  5. Select the checkbox for **I understand that this API endpoint will change data.**

  6. Click **Run**.

  7. You can verify that you successfully set up authentication by using the `Get OAuth Client App` method in the API Explorer by following these steps:

     * In the API Explorer's **Search** field, enter **Get OAuth Client App**.
     * Click **Run It**.
     * In the **client_guid** field, enter the value that you used when you registered the OAuth:
           
           client_guid
           

If you set up OAuth successfully, the **Response** tab will return the values that you entered when you registered the app.




## Configure the MCP client

Once the AI agent is registered, you can connect it to the managed MCP endpoint as an MCP client. Refer to your agent's documentation to complete client setup.

  * **Server URL:** `LOOKER_INSTANCE_URL/mcp`
  * **Authentication:** OAuth 2.1



### Example configurations (mcp.json)

This section describes how to configure various developer tools to connect to your Looker instance using the Looker-managed MCP server. The MCP server sits between your IDE and Looker, providing a secure and efficient control plane for your AI tools. Select the tab for your specific tool to see the configuration instructions.

### Gemini CLI

Configure the Gemini CLI to connect directly to the Looker-managed MCP server.

  1. Install the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation).
  2. Add the remote MCP server using the following command, replacing `LOOKER_INSTANCE_URL` with the your Looker instance URL: 
         
         gemini mcp add --transport http looker LOOKER_INSTANCE_URL/mcp
         

Alternatively, you can configure this manually by adding the following configuration to your `settings.json` file (located in `~/.gemini/settings.json` or your project directory):
         
         {
           "mcpServers": {
             "looker": {
               "httpUrl": "LOOKER_INSTANCE_URL/mcp",
               "oauth": {
                 "clientId": "CLIENT_GUID"
               }
             }
           }
         }
         

  3. Start the Gemini CLI in interactive mode: 
         
         gemini
         

When prompted to connect, the CLI initiates the OAuth authorization flow to securely authenticate with your Looker instance. 



### Gemini Code Assist

We recommend that you configure Gemini Code Assist to use the Gemini CLI. This approach removes the need to manually configure an MCP server.

  1. Make sure that you have installed and configured the [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation) and the Looker-managed MCP server.
  2. [Configure Gemini Code Assist to use the Gemini CLI](https://developers.google.com/gemini-code-assist/docs/set-up-gemini-standard-enterprise).
  3. Start interacting with your Looker instance using natural language directly within the Gemini Code Assist chat.



### Claude code

  1. Install [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).
  2. Create the `.mcp.json` file in your project root, if it doesn't exist. 
  3. Add the following configuration, replacing `LOOKER_INSTANCE_URL` with the URL of your Looker instance and `CLIENT_GUID` with your OAuth client GUID, and then save. 


    
    
          {
            "mcpServers": {
              "looker-managed-mcp": {
                "type": "http",
                "url": "LOOKER_INSTANCE_URL/mcp",
                "oauth": {
                  "clientId": "CLIENT_GUID",
                  "callbackPort": 8080
                }
              }
            }
          }
      

### Claude desktop

  1. In Claude desktop, navigate to **Settings** and select **Connectors**.
  2. Choose **Add custom connector** and enter a name (for example, **Looker**).
  3. For the URL, enter the URL for your Looker instance with the `/mcp` path appended (for example, `https://looker.example.com/mcp`).
  4. Under **Advanced settings** , enter the exact string that you used for the `client_guid` during your OAuth app registration. Leave the OAuth client secret blank.
  5. Select **Add** to save the connector. When prompted to connect, Claude desktop securely initiates the PKCE authorization flow through your browser.


  4. Restart Claude desktop.



### Cline

  1. Open the [Cline](https://github.com/cline/cline) extension in your IDE and click the **MCP Servers** icon.
  2. Click **Configure MCP Servers** to open the configuration file.
  3. Add the following configuration, replacing `LOOKER_INSTANCE_URL` with your Looker URL, and then save. 


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "type": "http",
                "url": "LOOKER_INSTANCE_URL/mcp"
              }
            }
          }
      

A green active status appears after the server connects successfully. 

### Cursor

  1. Create the `.cursor` directory in your project root if it doesn't exist.
  2. Create the `.cursor/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replacing `LOOKER_INSTANCE_URL` with your Looker URL, and then save. 


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "type": "http",
                "url": "LOOKER_INSTANCE_URL/mcp"
              }
            }
          }
      

  4. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects.



### Visual Studio Code (Copilot)

  1. Open [VS Code](https://code.visualstudio.com/docs/copilot/overview) and create the `.vscode` directory in your project root if it doesn't exist. 
  2. Create the `.vscode/mcp.json` file if it doesn't exist, and open it.
  3. Add the following configuration, replacing `LOOKER_INSTANCE_URL` with the URL of your Looker instance, and then save. 


    
    
          {
            "servers": {
              "looker-toolbox": {
                "type": "http",
                "url": "LOOKER_INSTANCE_URL/mcp"
              }
            }
          }
      

### Windsurf

  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to Cascade assistant.
  2. Click the MCP icon, then click **Configure** to open the configuration file.
  3. Add the following configuration, replacing `LOOKER_INSTANCE_URL` with the URL of your Looker instance, and then save. 


    
    
          {
            "mcpServers": {
              "looker-toolbox": {
                "type": "http",
                "url": "LOOKER_INSTANCE_URL/mcp"
              }
            }
          }
      

### Authenticate with the client

After you have configured your MCP client with the `mcp.json` settings, the first time you attempt to interact with Looker through that client, it will initiate the OAuth 2.1 authentication flow. This typically involves the client opening a browser window where you must log in to your Looker instance using your standard credentials and grant the application permission to access Looker on your behalf.

This login process is the interactive authentication step that allows the MCP client to obtain an access token for making future requests.

See your client's documentation for further details.

Once connected, the client will inherit your Looker roles and content access. The client will also have access to the AI tools that your Looker admin has enabled for the MCP server. For a list of all possible tools, see the [Use AI tools](https://docs.cloud.google.com/looker/docs/2608/connect-ide-to-looker-using-mcp#ai-tools) documentation.

**Tip:** You must reconnect your client to the MCP server to register any new tools that have been enabled. See your client's documentation for instructions on how to reconnect.

## Security and governance

The managed MCP server is designed to inherit Looker's existing security and governance framework.

  * **Permissions boundary:** The server enforces strict user-level permissions. An AI agent cannot access data or models that the authenticated user is not authorized to see.
  * **VPC Service Controls:** For Looker (Google Cloud core) instances that use VPC Service Controls, the managed MCP endpoint respects existing VPC Service Controls boundaries with no additional policies or configurations required.
  * **Customer-managed encryption keys (CMEK):** For Looker (Google Cloud core) instances that use [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek), the managed MCP server is CMEK-compliant with no additional policies or configurations required.



### Audit logging

Every action taken by an AI agent is logged in Looker **System Activity** and [**Cloud Audit Logs**](https://docs.cloud.google.com/looker/docs/looker-core-audit-logging).

#### System Activity

Looker-managed MCP server activity is tracked in the **History** and **Event Attribute** Explores. The [Monitoring Looker usage with System Activity Explores](https://docs.cloud.google.com/looker/docs/2608/usage-reports-with-system-activity-explores) documentation page provides the following sample queries:

  * [What API calls have been initiated by the Looker-managed MCP server?](https://docs.cloud.google.com/looker/docs/2608/usage-reports-with-system-activity-explores#api-calls-mcp)
  * [What events are related to a request from the Looker-managed MCP server?](https://docs.cloud.google.com/looker/docs/2608/usage-reports-with-system-activity-explores#mcp-events)
  * [What updates have been made to the Looker-managed MCP server tool settings by Looker admins?](https://docs.cloud.google.com/looker/docs/2608/usage-reports-with-system-activity-explores#mcp-admin-updates)
  * [What queries have been run by users of the Looker-managed MCP server?](https://docs.cloud.google.com/looker/docs/2608/usage-reports-with-system-activity-explores#history_explore_managed_mcp)



#### Cloud Audit Logs

Looker (Google Cloud core) instances also track Looker-managed MCP server activity through Cloud Audit Logs. The **Looker (Google Cloud core) audit logging** documentation page provides [sample queries](https://docs.cloud.google.com/looker/docs/looker-core-audit-logging#sample_queries).

## Limitations

  * **Fine-grained scopes:** OAuth scopes are not yet supported for the managed MCP server. Access control relies on the global tool allowlist and the user's base permissions.
  * **Dynamic registration:** Dynamic Client Registration is not supported in the preview.
  * **Client refresh:** Changes to the tool allowlist are not automatically pushed to connected clients. Users must wait 30 seconds after making a change to the tool list and then reconnect their client to refresh the tool manifest. See your client's documentation for information about how to reconnect to the MCP server.
  * **Server capacity** : During the preview phase, the managed MCP server is configured with a fixed capacity to help us gather performance data. During periods of peak usage, you may experience occasional timeouts. This is expected behavior.
  * **IP allowlists:** The Looker-managed MCP server isn't compatible with IP allowlists in Looker (original). It is compatible with IP allowlists in Looker (Google Cloud core).



## Pricing and quotas

The Looker-managed MCP server is available at no additional cost. However, tool calls made by AI agents consume the instance's standard administrative and query-based API quotas. High agent activity may impact your available API quota.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
