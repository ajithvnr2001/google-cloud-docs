---
url: https://docs.cloud.google.com/api-gateway/docs/mcp-configure/
title: Configure Model Context Protocol \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:04.912104+00:00
---

# Configure Model Context Protocol  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/mcp-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Model Context Protocol

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

This document describes how to configure API Gateway to act as a remote Model Context Protocol (MCP) server.

## Before you begin

  * Ensure you have a valid OpenAPI 3.x specification for your API. MCP is not supported for OpenAPI 2.0.
  * Ensure you understand the [basics of API Gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway).



## Configuration validation

When you upload your OpenAPI specification, API Gateway performs the following validations for MCP configuration:

  * **Location** : The `x-google-mcp-tool` extension must only be specified at the individual operation level.
  * **HTTP Method** : Only `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` operations can be exposed as MCP tools.
  * **Tool Name** : Tool names must match `[A-Za-z0-9_.-]{1,128}` and be unique across the specification.
  * **Description** : Every tool must resolve to a non-empty description (taken from the operation's description, summary, or override). Operations without a resolvable description are rejected.
  * **Security** : If you configure authentication for `tools/list`, you must name exactly one security scheme defined under `components.securitySchemes`. The scheme can be a JWT scheme or an API key scheme. If you use a JWT scheme, you must also name it in the specification's top-level `security` requirement.



## Authentication model

API Gateway applies different authentication rules depending on the MCP method called:

  * **Protocol Lifecycle** : The `initialize` and `notifications/initialized` methods are **unauthenticated**.
  * **Tool Invocation (`tools/call`)**: Reuses the authentication policies defined for the **underlying operation** in your OpenAPI specification. It enforces the same API key or JWT requirements as calling the REST endpoint directly.
  * **Tool Discovery (`tools/list`)**: By default, this method is unauthenticated. However, as a security best practice, we strongly recommend that you protect tool discovery by enabling authentication for this method using `tools-list.security`. You can authenticate `tools/list` with either a JWT or an API key.



## Steps to configure MCP

Follow these steps to expose your API as MCP tools:

### 1\. Identify operations to expose

Review your OpenAPI specification and decide which operations should be available to AI agents.

### 2\. Update your OpenAPI specification

You can enable MCP globally for all eligible operations, or configure it on a per-operation basis.

#### Global enablement

Enable MCP globally by adding the `mcp` field to `x-google-api-management` at the document level:
    
    
    openapi: 3.0.3
    info:
      title: Bookstore API
      version: 1.0.0
    x-google-api-management:
      mcp: true
      backends:
        bookstore-backend:
          address: https://bookstore-backend-12345678.us-central1.run.app
    

**Note:** Ensure your operations have a backend configured (either using `x-google-backend` at the operation level or using global defaults) for them to be eligible as MCP tools.

When globally enabled, all eligible operations (based on HTTP method and path) are exposed as MCP tools. By default, the tool name is the operation's `operationId`, and the description is the operation's description or summary.

#### Per-operation configuration

You can override global settings or selectively expose operations using `x-google-mcp-tool`:
    
    
    paths:
      /v1/shelves/{shelf}:
        delete:
          operationId: deleteShelf
          summary: Delete a shelf.
          x-google-backend: bookstore-backend
          x-google-mcp-tool:
            name: delete_shelf
            description: "Permanently delete a shelf and every book on it."
    

You can also opt-out an operation when globally enabled by setting `x-google-mcp-tool: false`.

### 3\. Authenticate `tools/list` (Recommended)

By default, the `tools/list` method (which enumerates available tools) is unauthenticated. As a security best practice, we strongly recommend that you enforce authentication by configuring `tools-list.security` under `x-google-api-management/mcp`. You can name either a JWT scheme or an API key scheme.

The following example requires a JWT:
    
    
    x-google-api-management:
      mcp:
        tools-list:
          security:
            myJWT: []
    

The following example requires an API key. Clients must send the key in the `x-api-key` HTTP header; `tools/list` doesn't read API keys from query parameters. A request without a valid key receives a JSON-RPC error and no tool list. To learn how to create an API key, see [Use API keys](https://docs.cloud.google.com/api-gateway/docs/authenticate-api-keys).
    
    
    x-google-api-management:
      mcp:
        tools-list:
          security:
            api_key: []
    components:
      securitySchemes:
        api_key:
          type: apiKey
          name: x-api-key
          in: header
    

**Note:** Configuring the `mcp` extension as an object (for example, to enable authentication for `tools/list`) also enables MCP globally for all eligible operations. If you want to configure `tools/list` security but don't want to expose all eligible operations, you must explicitly opt-out those operations by setting `x-google-mcp-tool: false`.

### 4\. Create and deploy the API config

Create an API config from your annotated specification and deploy it to a gateway using the standard flow. See [Deploying an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api) for details.

### 5\. Verify MCP support

Once deployed, you can verify that the gateway is serving MCP requests.

#### Handshake

Send an initialization request to establish protocol version and capabilities:
    
    
    curl -X POST https://my-gateway-12345.uc.a.run.app/mcp \
      -H "Content-Type: application/json" \
      -d '{
      "jsonrpc": "2.0",
      "id": 1,
      "method": "initialize",
      "params": {
        "protocolVersion": "2025-11-25",
        "capabilities": {},
        "clientInfo": {"name": "demo-client", "version": "1.0.0"}
      }
    }'
    

**Note:** Clients should send the `MCP-Protocol-Version` header on every request after initialization. If the header is absent, the gateway falls back to version `2025-03-26`.

#### Acknowledge handshake

Acknowledge the initialization. The gateway responds with `HTTP 202 Accepted`:
    
    
    curl -X POST https://my-gateway-12345.uc.a.run.app/mcp \
      -H "Content-Type: application/json" \
      -H "MCP-Protocol-Version: 2025-11-25" \
      -d '{"jsonrpc": "2.0", "method": "notifications/initialized"}'
    

#### Discover tools

List the available tools. If you configured `tools-list.security`, add the matching credential, such as an `Authorization: Bearer` header for a JWT or an `x-api-key` header for an API key:
    
    
    curl -X POST https://my-gateway-12345.uc.a.run.app/mcp \
      -H "Content-Type: application/json" \
      -H "MCP-Protocol-Version: 2025-11-25" \
      -d '{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}'
    

#### How arguments map to the REST request

The arguments passed to a tool are mapped to the underlying REST request based on the OpenAPI specification:

  * **Path and query parameters** : Become top-level properties in the `arguments` object, keyed by their OpenAPI parameter names.
  * **Request body** : Nested under a single property named `body`. For example, to create a resource, you pass `{"body": {"fieldName": "value"}}`.
  * **Headers** : Also become top-level properties. The gateway injects them as standard HTTP headers in the backend call.

**Note:** You cannot bind parameters to reserved system headers or headers starting with `x-google-`.

The transcoded backend request is indistinguishable from a direct REST request to your backend service. Backend services cannot programmatically distinguish between a direct REST call and one transcoded from MCP.

#### Invoke a tool

Invoke a specific tool. Ensure you include any required authentication tokens if the underlying REST operation requires them:
    
    
    curl -X POST https://my-gateway-12345.uc.a.run.app/mcp \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $TOKEN" \
      -H "MCP-Protocol-Version: 2025-11-25" \
      -d '{
      "jsonrpc": "2.0",
      "id": 3,
      "method": "tools/call",
      "params": {
        "name": "delete_shelf",
        "arguments": {"shelf": "sci-fi"}
      }
    }'
    

## Observability

MCP requests yield standard API Gateway metrics and logs. You can distinguish MCP traffic from standard REST traffic by inspecting the request path (typically ending in `/mcp`) or by configuring custom metrics.

### Troubleshooting MCP failures

MCP distinguishes between transport failures and protocol failures. The gateway returns HTTP 200 with a JSON-RPC error object for protocol and application errors, as non-200 responses can cause many MCP clients to fail at the transport layer.

The following table describes common symptoms and fixes:

Symptom | JSON-RPC Code | HTTP Status | Meaning and Typical Fix  
---|---|---|---  
Method Not Allowed | n/a | `405` | A non-POST request reached `/mcp`. Only HTTP `POST` is supported.  
JSON parse error | `-32700` | `400` | The request body is not valid JSON.  
Missing/Invalid Method or ID | `-32600` | `200` | The body is valid JSON but not a valid JSON-RPC request. Check required fields (`jsonrpc`, `method`, `id`).  
Method is not supported | `-32601` | `200` | The method is outside the supported scope (e.g., `ping`).  
Unsupported protocol version | `-32602` | `200` | The `protocolVersion` names a version the gateway does not support.  
Missing Protocol Version | `-32602` | `200` | The `initialize` params omit `protocolVersion` or it is not a string.  
Unknown tool | `-32602` | `200` | Tool name not found. Clean client cache or verify deployment.  
Invalid tool arguments | `-32602` | `200` | Arguments are missing or invalid. Verify the `body` key nesting.  
Body too large | `-32000` | `200` | The response payload exceeded size limits.  
Transport body too large | n/a | `413` | The raw HTTP request body exceeded gateway transport limits.  
Server error | `-32000` | `200` | Unparseable backend response. Check logs.  
Unauthorized / Forbidden | n/a | `401` / `403` | Authentication failure. The response carries a `WWW-Authenticate` header pointing at protected resource metadata.  
  
Backend application errors typically surface as a successful JSON-RPC response (`HTTP 200`) with `result.isError: true` containing the backend error body.

## What's next

  * [Model Context Protocol overview](https://docs.cloud.google.com/api-gateway/docs/mcp-overview)
  * [OpenAPI 3.x extensions](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions)
  * [OpenAPI 3.x feature limitations](https://docs.cloud.google.com/api-gateway/docs/openapi-v3-limitations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
