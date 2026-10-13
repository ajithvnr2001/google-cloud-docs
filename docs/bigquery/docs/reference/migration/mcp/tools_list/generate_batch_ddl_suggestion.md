---
url: https://docs.cloud.google.com/bigquery/docs/reference/migration/mcp/tools_list/generate_batch_ddl_suggestion/
title: MCP Tools Reference: bigquerymigration.googleapis.com \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:44.685287+00:00
---

# MCP Tools Reference: bigquerymigration.googleapis.com  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/reference/migration/mcp/tools_list/generate_batch_ddl_suggestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback 

#  MCP Tools Reference: bigquerymigration.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `generate_batch_ddl_suggestion`

Generates Data Definition Language (DDL) suggestions for a batch of queries stored in Cloud Storage. This is a fallback for when no metadata .ZIP file is available from the source system. The suggested columns and types are inferred from how the queries use them, so they are approximate. The suggestion runs asynchronously. Use the `fetch_batch_ddl_suggestion` tool with the returned suggestion ID to poll its state until it is `SUCCEEDED` or `FAILED`. Wait at least 10 seconds before rechecking the state.

The following code sample shows how to use `curl` to call the `generate_batch_ddl_suggestion` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://bigquerymigration.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "generate_batch_ddl_suggestion",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `GenerateBatchDdlSuggestion`.

### GenerateBatchDdlSuggestionRequest

JSON representation  
---  
      
    
    {
      "projectNumber": string,
      "location": string,
      "sourceDialect": string,
      "targetDialect": string,
      "sourceBaseUri": [
        string
      ],
      "targetBaseUri": string
    }  
  
Fields  
---  
`projectNumber` |  `string` Required. The Google Cloud project number.  
`location` |  `string` Required. The location.  
`sourceDialect` |  `string` Required. The dialect of the source queries.  
`targetDialect` |  `string` Required. The dialect of the target queries.  
`sourceBaseUri[]` |  `string` Required. The Cloud Storage path containing the inputs.  
`targetBaseUri` |  `string` Required. The base URI for all writes to persistent storage in Cloud Storage.  
  
## Output Schema

Response message for `GenerateBatchDdlSuggestion`.

### GenerateBatchDdlSuggestionResponse

JSON representation  
---  
      
    
    {
      "suggestion": string,
      "suggestionState": string
    }  
  
Fields  
---  
`suggestion` |  `string` The ID of the suggestion workflow created for this batch translation.  
`suggestionState` |  `string` The current state of the suggestion workflow, typically `RUNNING`.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
