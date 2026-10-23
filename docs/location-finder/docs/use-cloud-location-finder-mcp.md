---
url: https://docs.cloud.google.com/location-finder/docs/use-cloud-location-finder-mcp/
title: Use the Cloud Location Finder remote MCP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:13.040545+00:00
---

# Use the Cloud Location Finder remote MCP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/location-finder/docs/use-cloud-location-finder-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Cloud Location Finder ](https://docs.cloud.google.com/location-finder/docs)
  * [ Guides ](https://docs.cloud.google.com/location-finder/docs/overview)



Send feedback 

#  Use the Cloud Location Finder remote MCP server Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to use the Cloud Location Finder remote Model Context Protocol (MCP) server to connect with AI applications including Antigravity, ChatGPT, Claude, and custom applications you are developing. The Cloud Location Finder remote MCP server allows large language model (LLM)-powered agents to securely retrieve cloud location data and perform actions using standard MCP tools. This built-in integration enables agents to reason about latency, sustainability, and compliance boundaries when managing multi-cloud or hybrid deployments. The Cloud Location Finder remote MCP server is enabled when you enable the Cloud Location Finder API. 

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

  * You must have a Google Cloud project with the Cloud Location Finder API enabled. For instructions, see the [Cloud Location Finder Quickstart](https://docs.cloud.google.com/location-finder/docs/quickstart).



### Required roles

To get the permissions that you need to use the Cloud Location Finder MCP server, ask your administrator to grant you the following IAM roles on the project where you want to use the Cloud Location Finder MCP server: 

  * Make MCP tool calls: [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the Cloud Location Finder MCP server. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the Cloud Location Finder MCP server:

  * Make MCP tool calls: `mcp.tools.call`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Authentication and authorization

The Cloud Location Finder remote MCP server uses the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) for authentication and authorization. All [Google Cloud identities](https://docs.cloud.google.com/docs/authentication/identity-products) are supported for authentication to MCP servers. 

The Cloud Location Finder remote MCP server requires authentication using OAuth 2.0. It does not accept API keys.

We recommend that you create a separate identity for agents that are using MCP tools so that access to resources can be controlled and monitored. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

## Cloud Location Finder MCP OAuth scopes

OAuth 2.0 uses scopes and credentials to determine if an authenticated principal is authorized to take a specific action on a resource. For more information about OAuth 2.0 scopes at Google, read [Using OAuth 2.0 to access Google APIs](https://developers.google.com/identity/protocols/oauth2).

Cloud Location Finder requires the following MCP tool OAuth scope:

Scope URI for gcloud CLI | Description  
---|---  
`https://www.googleapis.com/auth/cloud-platform` | Allows full access to all Google Cloud services.  
  
Additional scopes might be required on the resources accessed during a tool call.

## Configure an MCP client to use the Cloud Location Finder MCP server

AI applications and agents, such as Claude or Antigravity, can instantiate an MCP client that connects to a single MCP server. An AI application can have multiple clients that connect to different MCP servers. If your application isn't listed in the [client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance), then you can use the following information to connect from most applications.

In your AI application, look for a way to add or connect to a remote MCP server. For the Cloud Location Finder MCP server, enter the following information as required:

  * **Server name** : Cloud Location Finder MCP server
  * **Server URL** or **Endpoint** : `https://cloudlocationfinder.googleapis.com/mcp`
  * **Transport** : [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http)
  * **Authentication details** : depending on how you want to authenticate, you can enter your Google Cloud credentials, your OAuth Client ID and secret, or an agent identity and credentials. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).
  * **OAuth scope** : the Cloud Location Finder MCP server requires the `https://www.googleapis.com/auth/cloud-platform` scope.



### Redirect URIs

For web-based applications, and some desktop applications, you must allowlist a redirect URI when you create a client ID and secret for authentication. Redirect URIs are used by the authorization server to send tokens to your application. Your application's documentation should specify the redirect URI that you must use. [Custom redirect URIs](https://developers.google.com/identity/protocols/oauth2/native-app#redirect-uri_custom-scheme) aren't supported.

For application-specific guidance about setting up and connecting to MCP server, see [Client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance).

For more general guidance, see the following resources:

  * [Connect to remote MCP servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers).
  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).



## Available tools

To view details of available MCP tools and their descriptions for the Cloud Location Finder MCP server, see the [Cloud Location Finder MCP reference](https://docs.cloud.google.com/location-finder/docs/reference/mcp).

### List tools

Use the [MCP inspector](https://modelcontextprotocol.io/docs/tools/inspector) to list tools, or send a `tools/list` HTTP request directly to the Cloud Location Finder remote MCP server. The `tools/list` method doesn't require authentication.
    
    
    curl -X POST https://cloudlocationfinder.googleapis.com/TOOLSET_ENDPOINT \
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

  * `TOOLSET_ENDPOINT`: the remainder of the MCP endpoint after the service name. For example, for Cloud Location Finder, this might be `mcp/toolset-name`.
  * `MCP_PROTOCOL_VERSION`: the MCP protocol version. For example, `2026-07-28`.



## Example use cases

The following are example use cases for the Cloud Location Finder MCP server. These examples show the types of prompts you can provide to your agent.

### Proximity and latency

**Prompt:** "Find the nearest Google Cloud zone to the AWS us-east-1 region."

This prompts the agent to use the `search_cloud_locations` tool to filter for zones that are closest to the `aws-us-east-1` location based on network latency:

### Sustainability

**Prompt:** "List Google Cloud regions that have a carbon free energy percentage of 80% or higher."

This prompts the agent to use the `list_cloud_locations` tool to filter regions with a `carbon_free_energy_percentage >= 80`:

### Compliance setup

**Prompt:** "Find all cloud locations in Europe to ensure data residency compliance."

## Optional security and safety configurations

MCP introduces new security risks and considerations due to the wide variety of actions that you can do with the MCP tools. To minimize and manage these risks, Google Cloud offers default settings and customizable policies to control the use of MCP tools in your Google Cloud organization or project.

For more information about MCP security and governance, see [AI security and safety](https://docs.cloud.google.com/mcp/ai-security-safety).

### Control MCP use with IAM policies

Identity and Access Management (IAM) [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) and [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies) help you secure Google Cloud and Google MCP servers.

You can combine multiple criteria to build customized security and governance policies by allowing or denying access based on the following:

  * The principal.
  * Tool properties like the read-only attribute.
  * The service name or tool name.
  * The application's OAuth client ID.



For more information, see [Control MCP use with Identity and Access Management](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

## What's next

  * Read the [Cloud Location Finder MCP reference documentation](https://docs.cloud.google.com/location-finder/docs/reference/mcp).
  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
