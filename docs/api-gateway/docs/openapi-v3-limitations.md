---
url: https://docs.cloud.google.com/api-gateway/docs/openapi-v3-limitations/
title: OpenAPI 3.x feature limitations \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:24:38.688771+00:00
---

# OpenAPI 3.x feature limitations  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/openapi-v3-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# OpenAPI 3.x feature limitations

This document describes the feature limitations for using OpenAPI 3.x with API Gateway.

For more information on supported OpenAPI specification versions, see [OpenAPI overview](https://docs.cloud.google.com/api-gateway/docs/openapi-overview).

## New OpenAPI 3.x limitations

This section describes limitations for features new in OpenAPI 3.x.

### Servers

OpenAPI 3.x supports multiple `server` objects to define hosts and base paths. However, API Gateway relies on a single server object, identified by the `x-google-endpoint` extension, to configure the service.

While you can define multiple servers, API Gateway considers only the server that contains the `x-google-endpoint` extension, and permits only one such server. For API Gateway, a server URL is not required, so you can have either no servers defined or one server with the `x-google-endpoint` extension.

For example, the following definitions are **valid** for API Gateway:
    
    
    servers:
      - url: https://example.com
        x-google-endpoint: {}
    
    
    
    servers:
      - url: https://example.com
        x-google-endpoint: {}
      - url: https://example2.com
    

The following definition is **invalid** because it contains multiple `x-google-endpoint` extensions:
    
    
    servers:
      - url: https://example.com
        x-google-endpoint: {}
      - url: https://example2.com
        x-google-endpoint: {}
    

The following definition is **valid for API Gateway** , but API Gateway ignores the server object:
    
    
    servers:
      - url: https://example.com
    

### Servers across multiple files

If you upload multiple OpenAPI files and one file contains a server with the `x-google-endpoint` extension, then all files must also have a server defined with an identical `x-google-endpoint` extension and an identical host in the server URL. The basepath may differ between files.

### Relative URL

For API Gateway, relative URLs in the `servers` object are treated as a basepath on their own because a hostname is not required in the specification. This is different from the standard OpenAPI behavior, which resolves relative URLs against the server hosting the OpenAPI definition. For example, API Gateway treats `url: /v1` as a basepath.

Basepaths must begin with '/'. API Gateway rejects URLs that don't have a scheme or begin with '/' to indicate a basepath.

### Unsupported extensions

API Gateway does not support the `x-google-allow` extension for OpenAPI 3.x.

### File size limits

API Gateway enforces a total size limit of 10MB and a file count limit of 50 for uploaded OpenAPI 3.x files.

### MCP limitations

During Public Preview, the following limitations apply to Model Context Protocol (MCP) support:

  * **Tool count limit** : Customers are limited to a maximum of 1,000 MCP tools per Gateway.
  * **HTTP methods** : Only `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` operations can be exposed as MCP tools. `HEAD`, `OPTIONS`, and `TRACE` are not supported.
  * **Streaming** : Server-Sent Events (SSE) streaming of long-running tool calls is not supported.
  * **Batch requests** : JSON-RPC batch arrays are rejected.
  * **Multi-modal payloads** : Tool responses are limited to UTF-8 text. Binary responses are not supported.
  * **Statelessness** : The implementation is stateless; session identifiers (like `MCP-Session-Id`) are not used or maintained.
  * **Unsupported MCP methods** : Specialized methods such as `resources/*`, `prompts/*`, `sampling/*`, `completion/*`, `ping`, and `logging/*` are not supported and return a JSON-RPC error code `-32601`.
  * **No tool annotations** : Hints such as `destructiveHint` or `readOnlyHint` are not emitted in tool declarations.
  * **CORS Preflight** : Automated CORS preflight handling (`OPTIONS` requests) on the `/mcp` path is not managed by the gateway.
  * **Model Routing Mutual Exclusion** : You cannot use both MCP and Model Routing within the same API configuration.
  * **Unsupported MCP responses** : Operations that return empty bodies in the response, such as HTTP 204 responses, are not supported.
  * **Schema Discovery** : Complex nested object schemas derived from your OpenAPI specification may not render fully or correctly in the `tools/list` discovery response due to a known configuration processing limitation.



## Pre-existing limitations

This section describes limitations carried over from OpenAPI 2.0 that also apply to OpenAPI 3.x.

### Scopes ignored

Although API Gateway accepts OpenAPI documents with scopes defined in a security scheme object, API Gateway does not check or enforce these scopes.

### Multiple security requirements

  * **API Key Requirements** : API Gateway does not support alternative (logical OR) security requirements if one of the schemes is an API key. However, API Gateway supports conjunctions (logical AND), which lets you require both an API key and an OAuth2 token.
  * **OAuth2 Requirements** : API Gateway supports alternative (logical OR) security requirements for different OAuth2 security schemes. API Gateway does not support conjunctions (logical AND) unless the additional security requirement is an API key.
  * **Optional Security** : You can use an empty security requirement (`- {}`) to make security optional for an API key, but API Gateway does not support this for OAuth.



### Security definition validation

API Gateway will reject an OpenAPI 3.x specification that uses a security requirement without a corresponding definition in the `securityDefinitions` section.

### URL path templating

API Gateway only supports URL path template parameters that represent entire path segments, for example, `/items/{itemId}`. API Gateway does not support and rejects parameters corresponding to partial segments, for example, `/items/prefix_{id}_suffix`.

### Parameters, schemas, request bodies, and types

API Gateway accepts OpenAPI documents with various parameter and type definitions (for example, `required` parameters and array formats), but it does not enforce them. API Gateway forwards incoming requests to your API regardless of these definitions.

API Gateway supports only primitive types in request parameters.

### External type references

API Gateway does not support references to types outside of the provided OpenAPI document. For example, API Gateway does not allow and rejects a `$ref` that points to an external URL.

### Custom port in host address

API Gateway does not allow custom ports in the `servers.url` field of an OpenAPI document.

### YAML alias limitations

An OpenAPI document submitted to API Gateway can have a maximum of 200 YAML alias nodes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
