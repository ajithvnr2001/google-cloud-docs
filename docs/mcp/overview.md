---
url: https://docs.cloud.google.com/mcp/overview/
title: Google Cloud MCP servers overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:02.012990+00:00
---

# Google Cloud MCP servers overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Google Cloud MCP servers overview Stay organized with collections  Save and categorize content based on your preferences. 

Remote [Model Context Protocol (MCP)](https://cloud.google.com/discover/what-is-model-context-protocol) servers let you use Google and Google Cloud services in your AI applications with governance, security, and access control. Developed by [Anthropic](https://www.anthropic.com/), MCP is an open source protocol that standardizes how AI applications connect to external tools and data sources. Google Cloud remote MCP servers support [MCP version 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28).

You can also publish your own remote MCP servers using [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) or [Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers). For more information, see MCP server publishing.

## How MCP works

MCP lets an AI application communicate with external services through a standardized set of components:

MCP server
    A program that exposes capabilities of a service, like an API or database, to AI applications through standardized MCP interfaces.
MCP host
    The main AI application that you're using or building—for example, Claude, VS Code, Gemini CLI, or Cursor IDE.
MCP client
    A software component within the MCP host that handles communication between your AI application and the MCP server.

### Local versus remote MCP servers

_Local_ MCP servers typically run on your local machine and use the standard input and output streams (stdio) for communication between services on the same device.

_Remote_ MCP servers run on the service's infrastructure and offer an HTTP endpoint to AI applications for communication between the AI MCP client and the MCP server.

For more information, see [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

## Stateless core

With [MCP version 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28), MCP changes from a bidirectional, stateful protocol to a stateless protocol. Each MCP request is self-describing and can be routed using headers. You don't need the `initialize`/`initialized` handshake or `Mcp-Session-Id` because each request includes all the information needed in HTTP headers or the `_meta` parameter. MCP servers can request additional information required by a tool through [multi-round-trip requests (MRTR)](https://modelcontextprotocol.io/specification/latest/basic/patterns/mrtr).

To help route and process requests without parsing the request body, some MCP headers are required, including the following:

  * Headers that are required by the MCP specification such as the [protocol version header](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#protocol-version-header) and [standard request headers](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#standard-request-headers).
  * [Custom headers](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#custom-headers-from-tool-parameters) that are defined by the MCP server. These headers are mirrored into HTTP headers from the tool's input schema using the `x-mcp-header` property. For example, an MCP server might define a custom header to specify the Google Cloud region or project ID.



For more information about MCP architecture, see the MCP version 2026-07-28 [specification](https://modelcontextprotocol.io/specification/2026-07-28) and [key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

## Google Cloud remote MCP servers

Google Cloud remote MCP servers have the following features and benefits:

  * **MCP discovery** : Once a server is configured for use in your project, AI applications can discover the server's capabilities, like tools, prompts, and resources, by using MCP discovery methods like [`tools/list`](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#listing-tools), [`prompts/list`](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts#listing-prompts), and [`resources/list`](https://modelcontextprotocol.io/specification/2026-07-28/server/resources#listing-resources). You can manage MCP servers in [Agent Registry](https://docs.cloud.google.com/agent-registry/overview).
  * **Toolsets** : Select a specific toolset from an MCP server to prevent overloading your agent's context with too many tools.
  * **Administrative controls** : Control MCP use with Identity and Access Management (IAM) policies.
  * **Authentication and Authorization** : Google and Google Cloud remote MCP servers are compliant with the [MCP authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization). Only agents, MCP clients, and end-users with established identities can authenticate and use MCP tools, prompts, and resources.
  * **Fine-grained authorization policies** : Use IAM to control who can do what on which Google Cloud resources with MCP tools, prompts, and resources.
  * **Model Armor** : Scan MCP calls and responses to help protect against security risks and enforce your AI security policies.



For a list of Google and Google Cloud remote MCP servers, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).

## Google remote MCP servers

Google remote MCP servers have the following features and benefits:

  * **MCP discovery** : Once a server is configured for use in your project, AI applications can discover the server's capabilities, like tools, prompts, and resources, by using MCP discovery methods like [`tools/list`](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#listing-tools), [`prompts/list`](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts#listing-prompts), and [`resources/list`](https://modelcontextprotocol.io/specification/2026-07-28/server/resources#listing-resources). You can manage MCP servers in [Agent Registry](https://docs.cloud.google.com/agent-registry/overview).
  * **Toolsets** : Select a specific toolset from an MCP server to prevent overloading your agent's context with too many tools.
  * **Administrative controls** : Control MCP use with your existing administrative controls.
  * **Authentication and Authorization** : Google remote MCP servers are compliant with the [MCP authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization).
  * **Model Armor** : Scan MCP calls and responses to help protect against security risks and enforce your AI security policies.



Google remote MCP servers don't require the MCP Tool User (`roles/mcp.toolUser`) role. You also can't use IAM policies or permissions to control access to Google remote MCP servers.

For a list of Google and Google Cloud remote MCP servers, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).

## MCP server features

MCP servers support the following features:

  * **Tools** : Let AI take actions like calling APIs.
  * **Prompts** : Predefined inputs provided by MCP servers that can help users interact with tools more effectively—you can use prompts provided by a server, but you can't define your own.
  * **Resources** : Allow servers to share data that provides context to language models, such as files, database schemas, or application-specific information.
  * **Elicitation** : When supported by the MCP client, MCP servers can request additional information from the user to help fulfill a request.



For more information, see [Manage MCP servers](https://docs.cloud.google.com/mcp/manage-mcp-servers).

## Extensions

Beyond the core MCP specifications, individual Google and Google Cloud MCP servers might support the following extensions:

  * **MCP Apps** : Sandboxed interactive UI elements that render inside a conversation. For more information, see MCP Apps.



## Authentication

To authenticate to Google and Google Cloud MCP servers that require authentication, use your Google credentials or create an identity for your AI application. For more information, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp) and [Set up authentication for MCP servers](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers).

## Control access with Identity and Access Management

IAM allow and deny policies help you secure Google Cloud MCP servers. [Non-Google Cloud MCP servers](https://docs.cloud.google.com/mcp/supported-products#google-mcp-servers) don't require the MCP Tool User (`roles/mcp.toolUser`) role. You also can't use IAM policies or permissions to control access to non-Google Cloud MCP servers. For more information, see [Access control with IAM](https://docs.cloud.google.com/mcp/access-control) and [Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

## Toolsets

Agents can become slow, confused, and expensive to run when you load too many tools into context. To help you limit the tools available to your agent, some Google and Google Cloud MCP servers offer logical groups of MCP tools called _toolsets_. Each toolset has its own HTTP endpoint and functions as a virtual MCP server. You can configure a toolset the same way that you configure an MCP server. For more information about configuring MCP servers, see [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).

To determine if an MCP server offers toolsets, review the server's MCP reference documentation linked from our [Supported products](https://docs.cloud.google.com/mcp/supported-products) page.

## MCP apps

MCP apps let you visually interact with data using charts, forms, dashboards, or other interactive elements. MCP app content is published by MCP servers as an [MCP resource](https://modelcontextprotocol.io/specification/2026-07-28/server/resources) and is rendered in a sandboxed iframe within your existing agent conversation.

Different MCP servers might offer different MCP app behaviors, but the following benefits apply to all MCP apps:

  * MCP apps can call any MCP tool within the MCP server, and can dynamically update with fresh information sent from the MCP server.
  * MCP apps can ask to use capabilities and tools that you've configured in addition to MCP tools offered by the MCP server.
  * MCP apps run in a sandboxed iframe controlled by your host application, which is designed to restrict access to the parent window, local storage, and cookies. Your host application also controls which tools an MCP app can use.



### Model Armor considerations for MCP apps

Because Model Armor doesn't scan MCP `resource/read` calls that are made to render an MCP app, the content of the MCP app resource isn't scanned. However, any tool calls made through the MCP app are still scanned by Model Armor if it's enabled. You can consider the content of an MCP app to be trusted because it's published by a Google or Google Cloud MCP server that you've configured.

For more information about MCP apps, see the MCP specification for [MCP apps](https://modelcontextprotocol.io/extensions/apps/overview).

## Model Armor protection

Model Armor helps secure your agentic AI applications by sanitizing MCP requests and responses. This process helps mitigate risks such as prompt injection, sensitive data disclosure, and tool poisoning.

To view a list of MCP servers that support Model Armor, see [Model Armor supported products](https://docs.cloud.google.com/mcp/model-armor-supported-products). To enable Model Armor for MCP endpoints, see [Configure Model Armor protection for Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration).

## MCP server publishing

To create and publish your own MCP server, you can choose from the following MCP publishing options:

  * [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) users with an existing API can [publish their API as an MCP server](https://docs.cloud.google.com/docs/api-platform/apigee-mcp/apigee-mcp-overview).
  * Developers who want to create their own MCP server can [host it on Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers).



## What's next

  * [Explore supported products](https://docs.cloud.google.com/mcp/supported-products).
  * [Enable or disable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
