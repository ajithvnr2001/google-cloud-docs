---
url: https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_get_key_string/
title: MCP Tools Reference: apikeys.googleapis.com \u00a0|\u00a0 API Keys API Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:57.359266+00:00
---

# MCP Tools Reference: apikeys.googleapis.com  |  API Keys API Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_get_key_string/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ API Keys API Documentation ](https://docs.cloud.google.com/api-keys/docs)
  * [ Reference ](https://docs.cloud.google.com/api-keys/docs/apis)



Send feedback 

#  MCP Tools Reference: apikeys.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `apikeys_get_key_string`

Retrieves the actual secret API key string. Treat as highly sensitive.

The following code sample shows how to use `curl` to call the `apikeys_get_key_string` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://apikeys.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "apikeys_get_key_string",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `GetKeyString` method.

### GetKeyStringRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the API key to be retrieved.  
  
## Output Schema

Response message for `GetKeyString` method.

### GetKeyStringResponse

JSON representation  
---  
      
    
    {
      "keyString": string
    }  
  
Fields  
---  
`keyString` |  `string` An encrypted and signed value of the key.  
  
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

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
