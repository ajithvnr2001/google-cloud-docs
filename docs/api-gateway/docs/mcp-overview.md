---
url: https://docs.cloud.google.com/api-gateway/docs/mcp-overview/
title: Model Context Protocol overview \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:21.515723+00:00
---

# Model Context Protocol overview  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/mcp-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Model Context Protocol overview

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

This document provides an overview of Model Context Protocol (MCP) support in API Gateway.

API Gateway can act as a remote MCP server, enabling you to expose your existing REST APIs to AI agents and LLMs without rewriting your backend services.

## Background

The Model Context Protocol (MCP) is an open standard that lets you build AI agents directly against your existing infrastructure. Instead of writing custom integration code for every tool or API, MCP provides a standard way for AI models to discover and invoke functionality in your environment.

When configured as an MCP server, API Gateway acts as a proxy. It translates standard MCP JSON-RPC protocol messages sent from agentic systems into standard HTTP REST requests toward your existing backends.

## Supported features

During Public Preview, API Gateway supports the following MCP features:

  * **Remote MCP server** : API Gateway acts as a remote server, receiving MCP requests over HTTP (POST).
  * **OpenAPI 3.x integration** : MCP configuration is derived directly from your OpenAPI 3.x specification using custom extensions.
  * **Supported MCP lifecycle methods** : 
    * `initialize`: Establishes protocol version and capabilities.
    * `notifications/initialized`: Acknowledges the handshake.
    * `tools/list`: Allows clients to discover available tools and their schemas.
    * `tools/call`: Allows clients to invoke a tool with arguments.

**Note:** All other MCP methods (such as `resources/*` or `prompts/*`) are not supported and return a JSON-RPC error code `-32601`.

## Limitations

The following limitations apply to MCP support in API Gateway:

  * Resources (`resources/*`) and Prompts (`prompts/*`) are not supported.
  * Stdio transport is not supported.
  * OpenAPI 2.0 is not supported.
  * Streaming or long-running tool calls are not supported.
  * **Model Routing Mutual Exclusion** : You cannot enable both MCP and Model Routing within the same API configuration. If `x-google-api-management.mcp` is enabled, `x-google-model-router` cannot be used.



For a complete list of technical limits, see [OpenAPI 3.x feature limitations](https://docs.cloud.google.com/api-gateway/docs/openapi-v3-limitations#mcp-limitations).

## Use cases

  * **Expose existing REST APIs as MCP tools** : Turn your existing APIs into AI-ready tools without changing backend code.
  * **Select tools per operation** : Explicitly choose which API paths and methods are exposed to agents.
  * **Protect the tool surface** : Apply existing API Gateway security policies (like API keys or OAuth) to your MCP endpoint.



## Request flow

The canonical path for MCP requests is `<basepath>/mcp`, where `<basepath>` is derived from your gateway's URL or `x-google-endpoint` configuration.

The following diagram shows the request flow for an MCP `tools/call` request:

  1. An MCP client (e.g., an AI agent) sends a JSON-RPC request to the gateway's MCP endpoint (e.g., `POST /mcp` or `POST /v1/mcp` if a version prefix is used).
  2. The gateway validates the request and checks authentication.
  3. The gateway inspects the payload to determine which tool is being called.
  4. The gateway translates the MCP payload into a standard HTTP request (path, parameters, body) based on the mapping defined in the API config.
  5. The gateway forwards the request to the backend service.
  6. The backend returns a standard HTTP response.
  7. The gateway translates the HTTP response back into an MCP JSON-RPC response and returns it to the client.



## Discovery through API Hub and Agent Registry

If you integrate your gateway with API hub, your MCP-enabled gateway is published to API hub as an MCP server with additional MCP-specific metadata, and it also appears in Agent Registry automatically. 

For gateways without MCP enabled, standard API metadata is published. Only gateways that have MCP enabled will display these additional MCP configurations in API hub.

No separate registration step is needed. Agents can then discover the server and its tools through either catalog.

To query Agent Registry, enable its API in your project:
    
    
    gcloud services enable agentregistry.googleapis.com
    

## What's next

  * [Configure Model Context Protocol](https://docs.cloud.google.com/api-gateway/docs/mcp-configure)
  * [OpenAPI 3.x extensions](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions)
  * [OpenAPI 3.x feature limitations](https://docs.cloud.google.com/api-gateway/docs/openapi-v3-limitations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
