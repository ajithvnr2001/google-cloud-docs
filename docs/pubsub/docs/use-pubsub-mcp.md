---
url: https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp/
title: Use the Pub/Sub remote MCP server to manage Pub/Sub resources and publish messages \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:54.816775+00:00
---

# Use the Pub/Sub remote MCP server to manage Pub/Sub resources and publish messages  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Use the Pub/Sub remote MCP server to manage Pub/Sub resources and publish messages Stay organized with collections  Save and categorize content based on your preferences. 

The Pub/Sub remote MCP server offers a global endpoint, locational endpoints, and regional endpoints. The global MCP endpoint and the locational MCP endpoints are Generally Available. Regional MCP endpoints are in Preview and subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

This document describes how to use the Pub/Sub remote MCP server to connect to Pub/Sub from AI applications such as Gemini CLI, agent mode in Gemini Code Assist, Claude Code, or in AI applications that you're developing.

The Pub/Sub MCP server lets you manage Pub/Sub resources and publish messages. You can create, list, get, update, and delete Pub/Sub topics, subscriptions, and snapshots, as well as publish messages to topics.

The Pub/Sub remote MCP server is enabled when you enable the Pub/Sub API. 

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

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  6. Enable the Pub/Sub API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=pubsub)




### Required roles

To get the permissions that you need to use the Pub/Sub MCP server, ask your administrator to grant you the following IAM roles on the project where you want to use the MCP server: 

  * Make MCP tool calls: [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) 
  * Create, update, and delete Pub/Sub resources: [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the Pub/Sub MCP server. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the Pub/Sub MCP server:

  * Make MCP tool calls: `mcp.tools.call`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The required Pub/Sub permissions depend on the specific operation that you want to perform. For more information, see [Pub/Sub roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub).

## Authentication and authorization

The Pub/Sub remote MCP server uses the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) for authentication and authorization. All [Google Cloud identities](https://docs.cloud.google.com/docs/authentication/identity-products) are supported for authentication to MCP servers. 

Pub/Sub does not support API keys as an authentication method.

We recommend creating a separate identity for agents using MCP tools so that access to resources can be controlled and monitored. For more information on authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

## Pub/Sub MCP OAuth scopes

OAuth 2.0 uses scopes and credentials to determine if an authenticated principal is authorized to take a specific action on a resource. For more information about OAuth 2.0 scopes at Google, read [Using OAuth 2.0 to access Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes). Pub/Sub has the following MCP tool OAuth scopes:

Scope URI | Description  
---|---  
`https://www.googleapis.com/auth/pubsub` | View and manage Pub/Sub resources.  
  
Additional scopes might be required on the resources accessed during a tool call. To view a list of scopes required for Pub/Sub, see [Pub/Sub API](https://developers.google.com/identity/protocols/oauth2/scopes#pubsub).

## Configure an MCP client to use the Pub/Sub MCP server

AI applications and agents, such as Claude or Antigravity, can instantiate an MCP client that connects to a single MCP server. An AI application can have multiple clients that connect to different MCP servers. If your application isn't listed in the [client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance), then you can use the following information to connect from most applications.

In your AI application, look for a way to add or connect to a remote MCP server. For the Pub/Sub MCP server, enter the following information as required:

  * **Server name** : Pub/Sub MCP server
  * **Server URL** or **Endpoint** : https://pubsub.googleapis.com/mcp
  * **Transport** : [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http)
  * **Authentication details** : depending on how you want to authenticate, you can enter your Google Cloud credentials, your OAuth Client ID and secret, or an agent identity and credentials. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).
  * **OAuth scope** : the [OAuth 2.0 scope](https://developers.google.com/identity/protocols/oauth2/scopes) that you want to use when connecting to the Pub/Sub MCP server. For more information, see Pub/Sub MCP OAuth scopes.



### Redirect URIs

For web-based applications, and some desktop applications, you must allowlist a redirect URI when you create a client ID and secret for authentication. Redirect URIs are used by the authorization server to send tokens to your application. Your application's documentation should specify the redirect URI that you must use. [Custom redirect URIs](https://developers.google.com/identity/protocols/oauth2/native-app#redirect-uri_custom-scheme) aren't supported.

For application-specific guidance about setting up and connecting to MCP server, see [Client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance).

For more general guidance, see the following resources:

  * [Connect to remote MCP servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers).
  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).



## Available tools

To view details of available MCP tools and their descriptions for the Pub/Sub MCP server, see the [Pub/Sub MCP reference](https://docs.cloud.google.com/pubsub/docs/reference/mcp).

### List tools

Use the [MCP inspector](https://modelcontextprotocol.io/docs/tools/inspector) to list tools, or send a `tools/list` HTTP request directly to the Pub/Sub remote MCP server. The `tools/list` method doesn't require authentication.
    
    
    curl -X POST https://pubsub.googleapis.com/TOOLSET_ENDPOINT \
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

  * `TOOLSET_ENDPOINT`: the remainder of the MCP endpoint after the service name. For example, for Pub/Sub, this might be `mcp/toolset-name`.
  * `MCP_PROTOCOL_VERSION`: the MCP protocol version. For example, `2026-07-28`.



## Sample use cases

The following are sample use cases for the Pub/Sub MCP server:

  * Create a Pub/Sub pipeline that includes a topic with subscriptions.

  * Create a subscription that uses Pub/Sub features such as [message filtering](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter).

  * Add [Single Message Transforms](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview) (SMTs) to your existing Pub/Sub pipeline.




### Sample prompts

  * "Build a pipeline that consumes messages from Pub/Sub topic `my-topic`, filters out messages that have attribute `priority=low`, and writes the messages to Cloud Storage bucket `my-bucket`."

  * "Create a subscription from topic `my-topic` to BigQuery table `my-table`, with failed deliveries sent to `my-dead-letter-topic`."




## Optional security and safety configurations

MCP introduces new security risks and considerations due to the wide variety of actions that you can do with the MCP tools. To minimize and manage these risks, Google Cloud offers default settings and customizable policies to control the use of MCP tools in your Google Cloud organization or project.

For more information about MCP security and governance, see [AI security and safety](https://docs.cloud.google.com/mcp/ai-security-safety).

### Use Model Armor

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

  * Read the [Pub/Sub MCP reference documentation](https://docs.cloud.google.com/pubsub/docs/reference/mcp).
  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
