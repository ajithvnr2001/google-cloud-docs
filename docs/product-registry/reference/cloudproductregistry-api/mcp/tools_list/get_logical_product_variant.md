---
url: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/get_logical_product_variant/
title: MCP Tools Reference: cloudproductregistry.googleapis.com \u00a0|\u00a0 Cloud Product Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:01.380284+00:00
---

# MCP Tools Reference: cloudproductregistry.googleapis.com  |  Cloud Product Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/get_logical_product_variant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Product Registry API ](https://docs.cloud.google.com/product-registry)
  * [ APIs & Reference ](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest)



Send feedback 

#  MCP Tools Reference: cloudproductregistry.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_logical_product_variant`

Retrieves details of a specific LogicalProductVariant, which is a specific variant of a LogicalProduct (e.g., Cloud SQL for MySQL is a variant of Cloud SQL Product). This tool should be invoked when you need to fetch information about a specific logical product variant, using its unique name in the format of `logicalProducts/{logical_product_id}/variants/{logical_product_variant_id}`.

The following code sample shows how to use `curl` to call the `get_logical_product_variant` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudproductregistry.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_logical_product_variant",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for GetLogicalProductVariant.

### GetLogicalProductVariantRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the LogicalProductVariant to retrieve. Format: logicalProducts/{logical_product}/variants/{variant}  
  
## Output Schema

Represents a distinct offering derived from a primary product that retains core functionalities but offers specialized features for a specific market segment.

### LogicalProductVariant

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "lifecycleState": enum ([LifecycleState](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/get_logical_product#Output.Schema.LifecycleState)),
      "replaced": boolean,
      "replacement": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the LogicalProductVariant. Format: logicalProducts/{logical_product}/variants/{variant}  
`title` |  `string` Display name of the LogicalProductVariant.  
`lifecycleState` |  `enum (`[LifecycleState](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/mcp/tools_list/get_logical_product#Output.Schema.LifecycleState)`)` Output only. Current Lifecycle state of the logical product variant.  
`replaced` |  `boolean` Output only. Indicates whether the logical product variant has been replaced. If `false`, the variant is active. If `true`, the variant has been replaced by another type, and the `replacement` field contains the resource name of that replacement.  
`replacement` |  `string` Output only. The resource name of the Logical Entity that the logical product variant is replaced by. This field is only populated when this logical product variant is replaced by some other type. Eg: logicalProducts/{logical_product}, productSuites/{product_suite}, etc.  
  
### LifecycleState

Enum representing the lifecycle state of the underlying entity.

Enums  
---  
`LIFECYCLE_STATE_UNSPECIFIED` | The default value. This value is used if the lifecycle state is not set.  
`LIFECYCLE_STATE_PUBLIC_PREVIEW` | The entity is in Public Preview. It is available to all customers, but may not be feature-complete or have full support guarantees.  
`LIFECYCLE_STATE_PRIVATE_GA` | Deprecated: Private General Availability entities are not exposed. The entity is in Private General Availability. It is fully supported and stable, but only available to a select group of customers.  
`LIFECYCLE_STATE_GA` | The entity is Generally Available. It is fully supported, stable, and available to all customers.  
`LIFECYCLE_STATE_DEPRECATED` | The entity is deprecated. It is no longer recommended for use and may be removed in a future version.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
