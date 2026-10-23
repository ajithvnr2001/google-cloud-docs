---
url: https://docs.cloud.google.com/mcp/configure-mcp-ai-application/
title: Configure MCP in an AI application \u00a0|\u00a0 Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:38.945494+00:00
---

# Configure MCP in an AI application  |  Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/configure-mcp-ai-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Configure MCP in an AI application Stay organized with collections  Save and categorize content based on your preferences. 

You can configure most AI applications to use remote MCP servers. This guide provides general information on MCP configuration as well as detailed configuration instructions for several common MCP AI applications.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Required roles

[Non-Google Cloud MCP servers](https://docs.cloud.google.com/mcp/supported-products#google-mcp-servers) don't require the MCP Tool User (`roles/mcp.toolUser`) role. You also can't use Identity and Access Management (IAM) policies or permissions to control access to non-Google Cloud MCP servers.

To get the permission that you need to make tool calls to Google Cloud MCP tools, ask your administrator to grant you the [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) IAM role on the Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `mcp.tools.call` permission, which is required to make tool calls to Google Cloud MCP tools. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To access Google Cloud products through MCP, your administrator must also grant you or your agent the required IAM roles for the resources that you access. See the documentation for the MCP server for the required roles or access for specific actions.

## Enable the product or service

You can use MCP to connect to [supported products](https://docs.cloud.google.com/mcp/supported-products) when the product API is enabled in your Google Cloud project.

To connect to a supported product through MCP, enable the product API:

#### Roles required to enable APIs

To enable APIs, you need the Service Usage Admin IAM role (`roles/serviceusage.serviceUsageAdmin`), which contains the `serviceusage.services.enable` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
    
    
    gcloud services enable SERVICE_NAME
    

Replace SERVICE_NAME with the service name of the product you want to use through MCP. For example, the BigQuery service name is `bigquery.googleapis.com`. See the MCP server's documentation to determine the service name. To view all available services and their documentation, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).

## Configure an MCP client to use the remote MCP server

AI applications and agents, such as Claude or Gemini CLI, can instantiate an MCP client that connects to a single MCP server. An AI application can have multiple clients that connect to different MCP servers. To connect to a remote MCP server, the MCP client must know at a minimum the URL of the remote MCP server.

### Use toolsets

Agents can be overloaded by too many tools. To decrease the number of tools available to your agent, you can use _toolsets_. Toolsets contain a subset of tools from an MCP server, and have their own unique endpoint. Your agent treats a toolset as an MCP server.

For example, a single MCP server might have 60 or more tools. If you use a toolset for the same MCP server with 15 tools, then you can use the MCP server without overloading your agent.

To configure a toolset, use the toolset endpoint in your MCP configuration instead of the MCP server endpoint.

### General guidance for all MCP clients

In your AI application, look for a way to connect to a remote MCP server. You are prompted to enter details about the server, such as its name and URL.

Enter the following as required:

  * **Server name** : the name of the remote MCP server or toolset—for example, "BigQuery MCP server".
  * **Server or toolset URL** or **Endpoint** : the MCP endpoint of the server or toolset you want to use—for example, `https://bigquery.googleapis.com/mcp` or `https://aiplatform.googleapis.com/mcp/models`. Some MCP servers also offer [regional endpoints](https://docs.cloud.google.com/docs/security/compliance/about-regional-endpoints).

**Note:** If you have data residency requirements for in-use data and you want to use Model Armor, then ensure that you only use MCP servers with regional endpoints that offer data residency compliance for in-use data. For more information, see [Model Armor supported products](https://docs.cloud.google.com/mcp/model-armor-supported-products) and [Integration with Google and Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/data-residency#mcp-servers).
  * **Transport** : [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http)

  * **Authentication details** : depending on how you want to authenticate, you can enter your Google Cloud credentials, your OAuth client ID and secret, or an agent identity and credentials. For more information on authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

  * **OAuth scope** : the [OAuth 2.0 scope](https://developers.google.com/identity/protocols/oauth2/scopes) that you want to use when connecting to the MCP server—for example, `https://www.googleapis.com/auth/bigquery`. Different scopes are required for different levels of access. To determine the required scope for the MCP server, refer to the server's documentation.




#### Redirect URIs

For web-based applications, and some desktop applications, you must allowlist a redirect URI when you create a client ID and secret for authentication. Redirect URIs are used by the authorization server to send tokens to your application. Your application's documentation should specify the redirect URI that you must use. [Custom redirect URIs](https://developers.google.com/identity/protocols/oauth2/native-app#redirect-uri_custom-scheme) aren't supported.

#### Authentication methods

Most applications that can connect to MCP servers offer a way to add authentication, but not all Google authentication methods are supported by all applications.

Use the following authentication methods to connect to MCP servers:

**Authentication type** | **Use cases**  
---|---  
[Application Default Credentials (ADC)](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers#adc) | Connecting from a Google-owned application like [Antigravity](https://antigravity.google/) or from an application running on Google infrastructure. ADC is a good strategy if you want to run your code in a development and a production environment without changing how your application authenticates.  
[OAuth 2.0 Client ID and secret](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers#client-id-secret) | Connecting from a Google-owned or third-party application. Given the security implications of getting the implementation correct, we strongly encourage you to use OAuth 2.0 libraries when interacting with Google's OAuth 2.0 endpoints. It is a best practice to use well-debugged code provided by others, and it will help you protect yourself and your users. For more information, see [Client libraries](https://developers.google.com/identity/protocols/oauth2#libraries).  
[Authorization header](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers#auth-header-token) | Connecting from a Google-owned or third-party application using an [OAuth 2.0 bearer token](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers#bearer-token) or an [API key](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers#api-key). This method has better security than using a client ID and secret, but OAuth tokens must be refreshed regularly.  
  
#### Authentication identities

You can use your own user identity to authenticate to MCP servers. When you do so, the MCP client has the same access as you do on Google and Google Cloud resources, and actions taken by the MCP client are attributed to you.

For production workloads that use Google Cloud MCP servers, we recommend that you create a separate agent or workload identity, instead of using your identity. Using a separate identity to access Google Cloud MCP servers lets you use IAM roles and policies to limit the actions of the MCP client. You can also view actions taken through MCP requests in your logs. You can't use IAM policies or permissions to control access to [non-Google Cloud MCP servers](https://docs.cloud.google.com/mcp/supported-products#google-mcp-servers). For more information, see [Set up authentication for MCP servers](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers) and [Authenticate to Google and Google Cloud MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

You can authenticate to MCP servers using the following credential types:

  * **Authenticate with your user credentials** : [Create an OAuth Client ID](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers#create-client-id) to authenticate with your user credentials. For web-based applications, select the **Web** client ID type; for desktop applications, select the **Desktop** client ID type.
  * **Impersonate a service account** : In most cases, you can use your user credentials to authenticate from a local development environment. If that isn't feasible, or if you need to test the permissions assigned to a service account, then you can use [service account impersonation](https://docs.cloud.google.com/mcp/authenticate-mcp#on-gcp).
  * **Authenticate with an agent identity** : For production workloads, create a separate identity for your agent. You can use [workload identity pools](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools), or create an [agent identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) to use instead of your own identity.
  * **Authenticate with an API key** : For services that don't require a principal, use [API keys for authentication](https://docs.cloud.google.com/mcp/authenticate-mcp#api-keys).



### Client-specific guidance

For application-specific instructions consult the following sections.

### Antigravity

To add a Google or Google Cloud remote MCP server to Antigravity, follow the instructions in [Antigravity Editor: MCP Integration](https://antigravity.google/docs/mcp). You can authenticate with [Application Default Credentials (ADC)](https://antigravity.google/docs/mcp#google-credentials) or a [client ID and secret](https://antigravity.google/docs/mcp#oauth).

### Gemini CLI

**Important:** Unpaid tier and Google One users: Gemini CLI will be replaced by Antigravity CLI on June 18, 2026. To learn more, see [An important update: Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/).

To add a Google or Google Cloud remote MCP server to your Gemini CLI, configure it as an extension and [authenticate](https://geminicli.com/docs/tools/mcp-server/#authentication-provider-type) using Google Application Default Credentials (ADC).

  1. Use your gcloud CLI credentials to configure your [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials): 
         
         gcloud auth application-default login

If the MCP server you're using requires OAuth scopes beyond the default `https://www.googleapis.com/auth/cloud-platform` scope, then use the [`--scopes` flag](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login#--scopes) to include those scopes.

  2. Create an extension file in the following location: `~/.gemini/extensions/EXT_NAME/gemini-extension.json` where `~/` is your home directory and EXT_NAME is the name you want to give the extension.

  3. Save the following content in your extension file:
         
         {
           "name": "EXT_NAME",
           "version": "1.0.0",
           "mcpServers": {
             "MCP_SERVER_NAME": {
               "httpUrl": "MCP_ENDPOINT",
               "authProviderType": "google_credentials",
               "oauth": {
                 "scopes": ["SCOPE"]
               },
               "timeout": 30000,
               "headers": {
                 "x-goog-user-project": "PROJECT_ID"
               }
             }
           }
         }

Replace the following:

     * EXT_NAME: the name of the extension.
     * MCP_SERVER_NAME: the name of the MCP server. MCP server names must start with a letter or an underscore, and must only contain alphanumeric characters (a-z, A-Z, 0-9), underscores (_), dots (.), colons (:), or dashes (-), with a maximum length of 64.
     * MCP_ENDPOINT: the endpoint of the MCP server—for example, `https://bigquery.googleapis.com/mcp`.
     * SCOPE: the [OAuth scope](https://developers.google.com/identity/protocols/oauth2/scopes) for the MCP server.
     * PROJECT_ID: your Google Cloud project ID.

For services that don't require OAuth scopes, you can omit the `"oauth"` section.

For services like [Antigravity](https://antigravity.google/docs/get-started) that support bearer tokens, add the `"Authorization"` parameter to the `"headers"` section of the JSON file:
    
    {
      ...
          "headers": {
            "Authorization": "Bearer YOUR_TOKEN",
            "x-goog-user-project": "PROJECT_ID"
    }

Replace YOUR_TOKEN with your bearer token. You can generate a token by running the [`gcloud auth application-default print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token). 

  4. Start Gemini CLI:
         
         gemini

  5. Run `/mcp` to view your configured MCP server and its tools.

The response is similar to the following:
         
         Configured MCP servers:
         🟢 BigQuery (from bigquery-mcp) - Ready (5 tools)
           Tools:
           - execute_sql
           - get_dataset_info
           - get_table_info
           - list_dataset_ids
           - list_table_ids




The remote MCP server is ready to use in Gemini CLI.

### Claude.ai

To add a Google or Google Cloud remote MCP server to Claude.ai, configure a custom connector with a OAuth client ID and OAuth client secret:

  1. Create an Oauth 2.0 client ID and secret:

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized JavaScript origins** section, click **\+ Add URI** , and then enter `https://claude.ai` in the **URIs** field.

     5. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://claude.ai/api/mcp/auth_callback` in the **URIs** field.

     6. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     7. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.
  2. Follow the instructions to [create a custom connector](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp). Enter your Client ID and secret in the **Advanced settings** menu.



### Claude Code

To add a Google or Google Cloud remote MCP server to Claude Code, configure a custom connector with a OAuth client ID and OAuth client secret:

  1. [Install Claude Code](https://code.claude.com/docs/en/quickstart).
  2. Create an Oauth 2.0 client ID and secret:

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://claude.ai/api/mcp/auth_callback` in the **URIs** field.

     5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.
  3. Follow the instructions to [create a custom connector](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp). Enter your Client ID and secret in the **Advanced settings** menu.



### Claude Desktop

To add a Google or Google Cloud remote MCP server to Claude Desktop, configure a custom connector with a OAuth client ID and OAuth client secret:

  1. [Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop).
  2. Create an Oauth 2.0 client ID and secret:

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://claude.ai/api/mcp/auth_callback` in the **URIs** field.

     5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.
  3. Follow the instructions to [create a custom connector](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp). Enter your Client ID and secret in the **Advanced settings** menu.



### ChatGPT

You must have a [ChatGPT Business subscription](https://chatgpt.com/business/) to use Google and Google Cloud MCP servers with ChatGPT.

To add a Google or Google Cloud remote MCP server to ChatGPT, create a Google OAuth 2.0 client ID and secret, and then add the MCP server as a plugin in ChatGPT.

#### Create an Oauth 2.0 client ID and secret

  1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

  2. In the **Application type** list, select **Web application**.

  3. In the **Name** field, enter a name for your application.

  4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://chatgpt.com/connector_platform_oauth_redirect` in the **URIs** field.

  5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

  6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.



#### Add the MCP server as a plugin in ChatGPT

  1. Sign in to ChatGPT.
  2. To add an MCP server to ChatGPT, follow the instructions in [Build a plugin](https://developers.openai.com/plugins/build/plugins).
  3. Enter your client ID and secret as needed for authentication.



The MCP server is displayed in the **Plugins** menu, and is ready for use through chat prompts.

### Cursor

To add a Google or Google Cloud remote MCP server to Cursor, create a client ID and secret, and then configure the MCP server with static OAuth. Cursor uses different redirect URIs depending on how you're accessing Cursor—through the web or a desktop application.

  1. Create an Oauth 2.0 client ID and secret:

### Web or Cursor agents

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://www.cursor.com/agents/mcp/oauth/callback` in the **URIs** field.

     5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.

### Desktop

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `http://localhost:8787/callback` in the **URIs** field.

     5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.

  2. Follow the instructions to [Configure the MCP server with static OAuth](https://cursor.com/docs/mcp#static-oauth-for-remote-servers).
  3. [Use the MCP server in Chat](https://cursor.com/docs/mcp#using-mcp-in-chat).



### OpenCode CLI

To add a Google or Google Cloud remote MCP server to [OpenCode CLI](https://opencode.ai/docs/), follow the instructions in [OpenCode: MCP](https://opencode.ai/docs/cli/#mcp).

### Replit

To add a Google or Google Cloud remote MCP server to [Replit](https://replit.com), follow the instructions in [Replit: MCP Servers Overview](https://docs.replit.com/references/mcp/overview#mcp-servers-overview).

### Visual Studio Code

To configure an MCP server in Visual Studio Code (VS Code), do the following:

  1. Install [VS Code](https://code.visualstudio.com/).
  2. Open VS Code and then open the **Command palette** by pressing `Ctrl`+`Shift`+`P` (Windows or Linux) or `Cmd`+`Shift`+`P` (macOS).
  3. In the Command palette, select **MCP: Add Server...**.
  4. Select **HTTP (HTTP or server-sent events)**.
  5. Enter the MCP endpoint of the server that you want to connect to and then press `Enter`. For example, `https://run.googleapis.com/mcp`
  6. Enter a name for the server and then press `Enter`.
  7. If you want to make the MCP server available to all workspaces, select **Global**. If you want to make the MCP server available to only the current workspace, select **Workspace**.

Your `mcp.json` file is updated with the server information.




#### Authenticate to the MCP server

You can use an Oauth client ID and secret or [Application Default Credentials](https://docs.cloud.google.com/docs/authentication#adc) (ADC) to authenticate to the MCP server.

**Note** : If you use ADC for authentication, then you need to regenerate your access token every hour.

#### OAuth Client ID

  1. In VS Code, open the Chat pane by pressing `Ctrl`+`Alt`+`I` (on Windows or linux) or `Shift`+`Command`+`I` (macOS).
  2. In the Chat pane, select **Set agent** , and then select **Agent**.

  3. The first time you use the MCP server, you'll be prompted to set up authentication. To use the MCP server, enter a prompt in chat that uses one of the available tools. If you're not sure which tool to use, then you can ask the agent to list the tools for the server. 

For example, you can enter the following prompt to list the available tools: "List the tools available for SERVER_NAME", where SERVER_NAME is the name you gave the MCP server.

The **Dynamic client registration not supported** dialog opens.

  4. Click **copy URIs and proceed**.
  5. You won't need the copied URLs, so there's no need to record them.


  1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

  2. In the **Application type** list, select **Desktop app**.

  3. In the **Name** field, enter a name for your application.

  4. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

  5. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.



##### Configure VS Code to use your OAuth client ID and secret

  1. In VS Code, enter your OAuth client ID and then press `Enter`.
  2. When prompted, enter your OAuth client secret and then press `Enter`.
  3. In the **VS Code** dialog that opens, click **Allow**.

The agent completes the MCP tool call and responds in chat.




#### Clear cached credentials

VS Code caches dynamic authentication providers to streamline your login experience. If you previously entered credentials, and want to enter new credentials, you must clear the cached credentials.

To clear cached credentials, do the following:

  1. In VS Code, open the **Command palette** by pressing `Ctrl`+`Shift`+`P` (on Windows or linux) or `Command`+`Shift`+`P` (macOS).
  2. In the **Command palette** , select **Authentication: Remove dynamic authentication providers** , and then select the client ID that you want to remove your cached credentials for.

  3. Reload VS Code and connect to a remote MCP server again.

You are prompted to enter your OAuth Client ID and secret.




#### ADC

  1. Set up [Application default credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) for your environment.
  2. If you're using a local shell, then create local authentication credentials for your user account:
         
         gcloud auth application-default login

  3. Generate an application default token by running the following command: 
         
         gcloud auth application-default print-access-token

  4. In your `mcp.json` file, add the following to your MCP server entry:
         
         "headers": {
               "Authorization": "Bearer TOKEN"
               "x-goog-user-project": "PROJECT_ID"
             }

Replace the following:

     * TOKEN: the application default token.

     * PROJECT_ID: your project ID.

The following example shows an MCP server entry that uses ADC for authentication:
    
    {
      "servers": [
        {
          "name": "My Cloud Run MCP Server",
          "uri": "https://run.googleapis.com/mcp",
          "headers": {
            "Authorization": "Bearer nYkwroEYjN4Fw1TTNhe69F4rR6o9bvrR1P4U1l0DVq9p81sN0",
            "x-goog-user-project": "my-project"
          }
        }
      ]
    }
    

  5. In VS Code, open the Chat pane by pressing `Ctrl`+`Alt`+`I` (on Windows or linux) or `Shift`+`Command`+`I` (macOS).
  6. In the Chat pane, select **Set agent** , and then select **Agent**.

  7. Send a prompt to the agent that uses one of the available MCP tools. If you're not sure which tool to use, then you can ask the agent to list the tools for the MCP server.



## What's next

  * [Learn about AI security and safety](https://docs.cloud.google.com/mcp/ai-security-safety).
  * Explore different methods to [authenticate to Google and Google Cloud remote MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
