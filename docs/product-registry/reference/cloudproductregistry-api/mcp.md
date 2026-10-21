---
url: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/
title: MCP Reference: cloudproductregistry.googleapis.com \u00a0|\u00a0 Cloud Product Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:00.925116+00:00
---

# MCP Reference: cloudproductregistry.googleapis.com  |  Cloud Product Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Product Registry API ](https://docs.cloud.google.com/product-registry)
  * [ APIs & Reference ](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest)



Send feedback 

#  MCP Reference: cloudproductregistry.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

This MCP service provides tools to interact with Cloud Product Registry.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Cloud Product Registry API MCP server has the following global MCP endpoint:

  * https://cloudproductregistry.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The cloudproductregistry.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[get_product_suite](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/get_product_suite)` |  Retrieves details of a specific ProductSuite, which is a high-level grouping of logical products under a common brand (e.g., Google Cloud Platform). This tool should be invoked when you need to fetch information about a specific product suite, using its unique name in the format of `productSuites/{product_suite_id}`.   
`[list_product_suites](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/list_product_suites)` |  Lists all available ProductSuites, which are high-level groupings of logical products under a common brand (e.g., Google Cloud Platform). This tool should be invoked when you need to discover or browse through the product suites available in the registry.   
`[get_logical_product](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/get_logical_product)` |  Retrieves details of a specific LogicalProduct, which is a standalone, customer-facing product within a Product Suite. This tool should be invoked when you need to fetch information about a specific logical product, using its unique name in the format of `logicalProducts/{logical_product_id}`.   
`[list_logical_products](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/list_logical_products)` |  Lists LogicalProducts matching the given criteria. LogicalProducts are standalone, customer-facing products within a Product Suite. This tool should be invoked when you need to search for logical products based on specific filters, such as product suite. When filters are not provided, all logical products are returned.   
`[get_logical_product_variant](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/get_logical_product_variant)` |  Retrieves details of a specific LogicalProductVariant, which is a specific variant of a LogicalProduct (e.g., Cloud SQL for MySQL is a variant of Cloud SQL Product). This tool should be invoked when you need to fetch information about a specific logical product variant, using its unique name in the format of `logicalProducts/{logical_product_id}/variants/{logical_product_variant_id}`.   
`[list_logical_product_variants](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/list_logical_product_variants)` |  Lists LogicalProductVariants matching the given criteria. LogicalProductVariants are specific variants of a LogicalProduct (e.g., Cloud SQL for MySQL is a variant of Cloud SQL Product). This tool should be invoked when you need to search for logical product variants based on specific filters, such as parent logical product.   
`[lookup_entity_by_name](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/lookup_entity_by_name)` |  Looks up a specific entity by its name, providing details about it. This tool supports ProductSuite, LogicalProduct, and LogicalProductVariant lookups and should be invoked when you have the name of an entity and need to retrieve its details without knowing its specific type beforehand. Supported names are in the format of `productSuites/{product_suite_id}`, `logicalProducts/{logical_product_id}`, and `logicalProducts/{logical_product_id}/variants/{logical_product_variant_id}`.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://cloudproductregistry.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
