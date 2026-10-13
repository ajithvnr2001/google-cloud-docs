---
url: https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/create_session/
title: MCP Tools Reference: spanner.googleapis.com \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:28.895530+00:00
---

# MCP Tools Reference: spanner.googleapis.com  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/create_session/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  MCP Tools Reference: spanner.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_session`

Create a session in a given database for query executions using execute_sql tool.

  * Session can be reused to execute multiple concurrent operations.



The following sample demonstrate how to use `curl` to invoke the `create_session` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://spanner.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_session",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `CreateSession`.

### CreateSessionRequest

JSON representation  
---  
      
    
    {
      "database": string,
      "fineGrainedAccessRole": string
    }  
  
Fields  
---  
`database` |  `string` Required. The database in which the new session is created. Format: `projects/{project}/instances/{instance}/databases/{database}`  
`fineGrainedAccessRole` |  `string` Optional. The fine grained access role of the session. All operations performed using the session will be performed with the fine grained access role.  
  
## Output Schema

A session for Spanner API.

### Session

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the session. Format: `projects/{project}/instances/{instance}/databases/{database}/sessions/{session}`  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
