---
url: https://docs.cloud.google.com/chronicle/docs/secops/use-google-secops-mcp/
title: Configure MCP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:30.991046+00:00
---

# Configure MCP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/use-google-secops-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure MCP

This document shows you how to use the Google Security Operations remote Model Context Protocol (MCP) server to connect with AI applications including Antigravity, ChatGPT, Claude, and custom applications you are developing. The Google Security Operations remote MCP server is enabled when you enable the Google Security Operations API. 

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

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Chronicle API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=chronicle.googleapis.com)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Chronicle API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=chronicle.googleapis.com)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init


**Note:** Make sure you are on the Google Cloud platform. Customers using SOAR APIs need to migrate to Google Cloud before using Google Cloud MCP servers.**Note:** The Workforce Identity Federation Provider created for authentication to Google SecOps cannot be used for authentication to Google Cloud Hosted MCP. In order to authenticate to a Google Cloud Hosted MCP Server you need to create a dedicated Workforce Identity Federation provider that authenticates against your Google Cloud environment, separate to the Google SecOps Workforce Identity Federation provider. 

### Required roles

To get the permissions that you need to use the Google SecOps remote MCP server, ask your administrator to grant you the following IAM roles on the project where you want to use the Google SecOps MCP server: 

  * Make MCP tool calls: [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) 
  * Access to the Chronicle API service: [Chronicle API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`) 
  * Grant administrator access to Google SecOps: [Chronicle SOAR Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`) 
  * Optional: Configure custom IAM roles with the permissions needed for the Chronicle API methods invoked by the MCP tools. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the Google SecOps remote MCP server. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the Google SecOps remote MCP server:

  * Make MCP tool calls: `mcp.tools.call`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Authentication and authorization

The Google Security Operations remote MCP server uses the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) for authentication and authorization. All [Google Cloud identities](https://docs.cloud.google.com/docs/authentication/identity-products) are supported for authentication to MCP servers. 

## Google SecOps MCP OAuth scopes

OAuth 2.0 uses scopes and credentials to determine if an authenticated principal is authorized to take a specific action on a resource. For more information about OAuth 2.0 scopes at Google, read [Using OAuth 2.0 to access Google APIs](https://developers.google.com/identity/protocols/oauth2).

Google SecOps has the following MCP tool OAuth scope:

Scope URI for gcloud CLI | Description  
---|---  
`https://www.googleapis.com/auth/chronicle` | Allows access to read and modify data.  
  
## Configure an MCP client to use the Google SecOps MCP server

AI applications and agents, such as Claude or Antigravity, can instantiate an MCP client that connects to a single MCP server. An AI application can have multiple clients that connect to different MCP servers. If your application isn't listed in the [client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance), then you can use the following information to connect from most applications.

In your AI application, look for a way to add or connect to a remote MCP server. For the Google SecOps MCP server, enter the following information as required:

  * **Server name** : Google SecOps MCP server
  * **Server URL** or **Endpoint** : Select the [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=africa-south1#service-endpoint) and add /mcp at the end. For example, `https://us-chronicle.googleapis.com/mcp`
  * **Transport** : [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http)
  * **Authentication details** : depending on how you want to authenticate, you can enter your Google Cloud credentials, your OAuth Client ID and secret, or an agent identity and credentials. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).
  * **OAuth scope** : the [OAuth 2.0 scope](https://developers.google.com/identity/protocols/oauth2/scopes) that you want to use when connecting to the Google SecOps MCP server. For Google SecOps, use `https://www.googleapis.com/auth/chronicle`.



### Redirect URIs

For web-based applications, and some desktop applications, you must allowlist a redirect URI when you create a client ID and secret for authentication. Redirect URIs are used by the authorization server to send tokens to your application. Your application's documentation should specify the redirect URI that you must use. [Custom redirect URIs](https://developers.google.com/identity/protocols/oauth2/native-app#redirect-uri_custom-scheme) aren't supported.

For application-specific guidance about setting up and connecting to MCP server, see [Client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance).

For more general guidance, see the following resources:

  * [Connect to remote MCP servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers).
  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).



## Configure Antigravity to use the Google SecOps MCP server

You can configure Google Antigravity (both the desktop IDE and the CLI) to connect to the Google SecOps MCP server.

### Configure the shared MCP configuration file

Antigravity uses a shared configuration file for all MCP servers.

  1. Open the shared MCP configuration file `~/.gemini/config/mcp_config.json` in a text editor.
  2. Add the Google SecOps MCP server configuration to the `mcpServers` object:
         
         {
           "mcpServers": {
             "google-cloud-secops": {
               "serverUrl": "https://us-chronicle.googleapis.com/mcp",
               "authProviderType": "google_credentials",
               "oauth": {
                 "scopes": [
                   "https://www.googleapis.com/auth/cloud-platform"
                 ]
               },
               "timeout": 300000
             }
           }
         }
         

Replace `https://us-chronicle.googleapis.com/mcp` with the appropriate [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=africa-south1#service-endpoint) for your Google SecOps instance.




### Configure tenant-specific context

The Google SecOps MCP server requires additional context: `customer_id`, `project_id`, and `region`. In Antigravity, you manage this using workspace-specific configuration.

  1. Create a dedicated workspace directory for your tenant (for example, `~/workspace/secops/tenant-a/`).
  2. In that directory, create a configuration file named `secops_tenant.json` with the following content:
         
         {
           "customer_id": "YOUR_CUSTOMER_ID",
           "project_id": "YOUR_PROJECT_ID",
           "region": "YOUR_REGION"
         }
         

Replace `YOUR_CUSTOMER_ID`, `YOUR_PROJECT_ID`, and `YOUR_REGION` with your actual tenant details. The region must be lowercase (for example, `us` or `eu`).




### Use the configuration

You can use the configuration in either the Antigravity CLI or the desktop IDE.

#### In the Antigravity CLI

  1. In your terminal, navigate to the workspace directory you created:
         
         cd ~/workspace/secops/tenant-a/
         

  2. Start the Antigravity CLI:
         
         agy
         

The CLI automatically loads the context from `secops_tenant.json` on startup.

  3. Verify the configuration by running the `/mcp` command in the CLI to see the active tools. If the context loading was unsuccessful, you can debug with the Antigravity CLI logs in `~/.gemini/antigravity-cli/log/`.




#### In the Antigravity desktop IDE

  1. Open the Antigravity desktop application.
  2. Create a new project and select the workspace folder you created (containing `secops_tenant.json`).
  3. Start a new conversation. The agent will have access to the Google SecOps MCP tools with the correct tenant context.



## Configure Gemini Enterprise to use the Google SecOps MCP server

You can integrate Google SecOps with Gemini Enterprise using a Custom MCP datastore. This allows users to query Google SecOps directly from the main Gemini Enterprise chat.

### Prerequisites

  1. Ensure the remote MCP server is enabled for your Google SecOps instance.
  2. Ensure that organization policies don't prevent the creation of custom MCP servers.



### Step 1: Set up an OAuth 2.0 Web Application

You must create an OAuth 2.0 Web Application in the Google Cloud project associated with your Google SecOps instance.

  1. In the Google Cloud Console, go to **APIs & Services** > **Credentials**.
  2. Click **Create Credentials** and select **OAuth client ID**.
  3. Select **Web application** as the application type.
  4. Enter a name for the client (for example, `Gemini Enterprise SecOps MCP`).
  5. Under **Authorized redirect URIs** , add the following URLs: 
     * `https://vertexaisearch.cloud.google.com/oauth-redirect`
     * `https://vertexaisearch.cloud.google.com/static/oauth/oauth.html`
  6. Click **Create** and save the generated **Client ID** and **Client Secret**.

**Note:** Ensure that users who will connect to the server have the following IAM roles in the project: Chronicle API Viewer (`roles/chronicle.viewer`), MCP Tool User (`roles/mcp.toolUser`), and Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`).

### Step 2: Add the Google SecOps datastore in Gemini Enterprise

An administrator must configure the Custom MCP connector globally.

  1. Open Gemini Enterprise and navigate to your application, or create a new one.
  2. Go to **Connected Data Stores** and click **New Data Store**.
  3. Select **Custom MCP** and enter the following details: 
     * **MCP Server URL** : Select your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=africa-south1#service-endpoint) and add `/mcp` at the end (for example, `https://us-chronicle.googleapis.com/mcp`).
     * **Authorization URL** : `https://accounts.google.com/o/oauth2/v2/auth`
     * **Authorization URL Parameters** : `&access_type=offline&prompt=consent`
     * **Token URL** : `https://oauth2.googleapis.com/token`
     * **Client ID** : Enter the Client ID from Step 1.
     * **Client Secret** : Enter the Client Secret from Step 1.
     * **OAuth Scopes** : Enter `https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/chronicle` (separated by a space).
  4. Save the datastore (for example, name it `Agentic SOC`).
  5. In your Gemini Enterprise App, select **Connected Data Stores** and ensure your new datastore is enabled.
  6. Select **Actions** in the menu and click **Reload Custom Actions**.
  7. Select the actions you want to enable for your users and click **Enable Actions**.



### Step 3: Authenticate the connector in chat

Each user must authorize Gemini to access Google SecOps on their behalf.

  1. Open the main Gemini Enterprise chat.
  2. Locate your connected datastore (for example, `Agentic SOC`) at the bottom of the chat window and toggle it **ON**.
  3. Complete the sign-in prompt to grant the necessary OAuth permissions.



### Step 4: Set up Gemini Memory for context

To ensure Gemini routes API calls correctly with the necessary tenant context, you must save your environment details to Gemini's Memory.

Send a prompt like the following to Gemini (replace placeholder values with your actual data):
    
    
    Remember that for all Google SecOps and Agentic SOC queries, my Customer ID is CUSTOMER_ID, my Region is REGION, and my Google Cloud project ID is PROJECTID.
    

Gemini will confirm that it has saved these details.

### Step 5: Start querying

You can now query Google SecOps using natural language in the main chat. For example:

  * "Using the Agentic SOC connector, find logon attempts from the last 3 days."
  * "Summarize the latest open cases in SecOps."



## Available tools

To view details of available MCP tools and their descriptions for the Google SecOps MCP server, see the [Google SecOps MCP reference](https://docs.cloud.google.com/chronicle/docs/reference/mcp).

### List tools

Use the [MCP inspector](https://modelcontextprotocol.io/docs/tools/inspector) to list tools, or send a `tools/list` HTTP request directly to the Google Security Operations remote MCP server. The `tools/list` method doesn't require authentication.
    
    
    curl -X POST https://chronicle.REGION.rep.googleapis.com/TOOLSET_ENDPOINT \
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

  * `TOOLSET_ENDPOINT`: The remainder of the MCP endpoint after the service name. For example, for Google Security Operations, this might be `mcp/toolset-name`.
  * `MCP_PROTOCOL_VERSION`: The MCP protocol version. For example, `2026-07-28`.



## Sample use cases

The following are sample use cases for the Google SecOps MCP server:

**Tool** : `list_rule_errors`

**Sample prompt** :
    
    
    List rule errors for the rule: ru_ddd45753-d749-4fee-b068-29072e750cfb
    

**Response** :
    
    
    Here are the rule errors for ru_ddd45753-d749-4fee-b068-29072e750cfb:
    
    Error Message: query took too long to execute, see https://docs.cloud.google.com/chronicle/docs/detection/yara-l-best-practices for tips for optimizing rules; these optimization tips are applicable to various types of queries
    
    Time Range: 2025-02-16T10:00:00Z to 2025-02-16T11:00:00Z
    Rule: projects/935934211738/locations/US/instances/eb3b937b-3ab6-47e5-8185-24837b826691/rules/ru_ddd45753-d749-4fee-b068-29072e750cfb@v_1740004374_748943000
    Error Message: query took too long to execute, see https://docs.cloud.google.com/chronicle/docs/detection/yara-l-best-practices for tips for optimizing rules; these optimization tips are applicable to various types of queries
    
    Time Range: 2025-02-16T11:00:00Z to 2025-02-16T12:00:00Z
    Rule: projects/935934211738/locations/US/instances/eb3b937b-3ab6-47e5-8185-24837b826691/rules/ru_ddd45753-d749-4fee-b068-29072e750cfb@v_1740004374_748943000
    The errors indicate that the queries for this rule took too long to execute during the specified time ranges. You may want to review the YARA-L best practices for optimizing rules.
    

**Tool** : `create_rules`

**Sample prompt** :
    
    
    Create the following rule:
    successful_user_logins_from_outside_us_test {
    meta:
    author = "Google SecOps Gemini"
    description = "Detect successful user logins originating from outside the United States."
    severity = "Medium"
    events:
    $e.metadata.event_type = "USER_LOGIN"
    $e.security_result.action = "ALLOW"
    $e.principal.ip_geo_artifact.location.country_or_region != "United States"
    outcome:
    $user = array($e.principal.user.userid)
    $source_ip = array($e.principal.ip)
    $country = array($e.principal.ip_geo_artifact.location.country_or_region)
    $city = array($e.principal.ip_geo_artifact.location.city)
    condition:
    $e
    }
    

**Response** :
    
    
    The rule successful_user_logins_from_outside_us_test has been successfully created with the following details:
    
    Name: projects/935934211738/locations/US/instances/eb3b937b-3ab6-47e5-8185-24837b826691/rules/ru_cff9cae1-bb88-4456-b725-4c08f21803ed
    Revision ID: v_1768208899_054095000
    Display Name: successful_user_logins_from_outside_us_test
    Author: Google SecOps Gemini
    Description: Detect successful user logins originating from outside the United States.
    Severity: Medium
    Compilation State: SUCCEEDED
    Create Time: 2026-01-12T09:08:19.054095Z
    

## Optional security and safety configurations

MCP introduces new security risks and considerations due to the wide variety of actions that can be taken with MCP tools. To minimize and manage these risks, Google Cloud offers defaults and customizable policies to control the use of MCP tools in your Google Cloud organization or project.

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

Before you begin, follow these steps using the Google Cloud CLI with the Model Armor API:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

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

  * Read the [Google Security Operations MCP reference documentation](https://docs.cloud.google.com/chronicle/docs/reference/mcp).
  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
