---
url: https://docs.cloud.google.com/endpoints/docs/openapi/openapi-v3-limitations/
title: OpenAPI 3.x feature limitations \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:06.811576+00:00
---

# OpenAPI 3.x feature limitations  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/openapi-v3-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options)



Send feedback 

#  OpenAPI 3.x feature limitations Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

This document describes the feature limitations for using OpenAPI 3.x with Endpoints.

For more information on supported OpenAPI specification versions, see [OpenAPI overview](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview).

## New OpenAPI 3.x limitations

This section describes limitations for OpenAPI that are new with OpenAPI 3.x support.

### Servers

OpenAPI 3.x supports multiple `server` objects to define hosts and base paths. However, Cloud Endpoints only uses a single server object to configure the hostname and base path, identified by the `x-google-endpoint` extension.

While you can define multiple servers in your OpenAPI specification, Cloud Endpoints uses only the server with the `x-google-endpoint` extension. You can define the `x-google-endpoint` extension on only one server.

For **Cloud Endpoints** , a hostname is required, so only one server must have the `x-google-endpoint` extension.

For example, the following server definitions are **valid** for Cloud Endpoints:
    
    
    servers:
      - url: https://my-api.endpoints.my-project-id.cloud.goog
        x-google-endpoint: {}
    
    
    
    servers:
      - url: https://my-api.endpoints.my-project-id.cloud.goog
        x-google-endpoint: {}
      - url: https://example.com
    

The following server definition is **invalid** for Endpoints:
    
    
    servers:
      - url: https://my-api-1.endpoints.my-project-id.cloud.goog
        x-google-endpoint: {}
      - url: https://my-api-2.endpoints.my-project-id.cloud.goog
        x-google-endpoint: {}
    

The following definition is also **invalid for Cloud Endpoints** :
    
    
    servers:
      - url: https://my-api.endpoints.my-project-id.cloud.goog
    

### Servers across multiple files

If you upload multiple OpenAPI files, all files must follow the `servers` section limitations. If one file contains a server with the `x-google-endpoint` extension, then all files must define a server with an `x-google-endpoint` extension.

Furthermore, all servers with the `x-google-endpoint` extension must use an identical host in the server URL, and the `x-google-endpoint` configuration must be identical across all files. The basepath in the server URL can differ.

### Relative URL

Cloud Endpoints requires a hostname, so it does not support relative URLs.

### Unsupported extensions

OpenAPI 3.x does not support the `x-google-allow` extension.

## Pre-existing limitations

This section describes limitations that existed in OpenAPI 2.0 and continue to apply to OpenAPI 3.x.

### Scopes ignored

Although you can define scopes in a security scheme object, ESP or Cloud Endpoints Frameworks don't check them.

### Multiple security requirements

You can specify more than one security requirement in your OpenAPI document.

  * **Security requirements with an API key** : Cloud Endpoints does not support alternative (logical OR) security requirements when one of the schemes is an API key. Cloud Endpoints supports conjunctions (logical AND), so you can require both an API key and OAuth2 authentication.

  * **Security requirements for OAuth2** : Cloud Endpoints supports alternative (logical OR) security requirements for different OAuth2 authentication schemes. Cloud Endpoints does not support conjunctions (logical AND) unless the additional security requirement is an API key.

  * **Optional Security Requirements** : OpenAPI 3 supports optional security by including an empty requirement (`{}`). API Key supports this, but OAuth does not.




### Security definition validation

For OpenAPI 3.x, using an undefined security schema results in an error, and Cloud Endpoints rejects the specification. This is a change from OpenAPI 2.0, where this only produced a warning.

### URL path templating

Cloud Endpoints supports only URL path template parameters that correspond to entire path segments (delimited by `/`). Cloud Endpoints does not support parameters for partial path segments.

For example, Cloud Endpoints supports `/items/{itemId}`, but it does not support `/items/overview.{format}`.

### Operations on URL root path `/`

While the OpenAPI document accepts operations on the root path `/`, Extensible Service Proxy rejects requests to the root path. This limitation does not apply to ESPv2, which supports the root path.

### Parameters, schemas, request bodies, and types

Extensible Service Proxy and ESP ignore most parameter, schema, request body, and type definitions. Extensible Service Proxy and ESP don't enforce required parameters and type definitions, and they forward requests to your API.

Extensible Service Proxy and ESP support only primitive types in request parameters.

### External type references

Cloud Endpoints does not support references to types outside of the OpenAPI document. For example, you cannot use a `$ref` to an external URL.

### Custom port in service host address

You cannot use custom ports in the `url` of a `servers` object.

### YAML alias limitations

An OpenAPI document can contain a maximum of 200 YAML alias nodes.

### Non-repeating request body

You can define only one `requestBody` per operation, and it must be of a non-repeating type.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
