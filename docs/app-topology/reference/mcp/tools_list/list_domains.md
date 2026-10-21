---
url: https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/list_domains/
title: MCP Tools Reference: apptopology.googleapis.com \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:15.108343+00:00
---

# MCP Tools Reference: apptopology.googleapis.com  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/list_domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  MCP Tools Reference: apptopology.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_domains`

ListDomains method returns all available topology domains in a specific location.

The following code sample shows how to use `curl` to call the `list_domains` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://apptopology.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_domains",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request for ListDomains.

### ListDomainsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent location to list domains for. Format: `projects/{project}/locations/{location}` Only `global` location is supported.  
`pageSize` |  `integer` Optional. The maximum number of domains to return. The service may return fewer than this value. If unspecified, at most 50 domains will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `ListDomains` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListDomains` must match the call that provided the page token.  
  
## Output Schema

Response for ListDomains.

### ListDomainsResponse

JSON representation  
---  
      
    
    {
      "domains": [
        {
          object ([Domain](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/get_domain#Output.Schema.Domain))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`domains[]` |  `object (`[Domain](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/get_domain#Output.Schema.Domain)`)` The domains in the specified location.  
`nextPageToken` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Domain

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The pre-defined topology domain. Currently only SRE, DEVOPS, and SECURITY are available. Format: `projects/{project}/locations/{location}/domains/{domain}`  
  
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

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
