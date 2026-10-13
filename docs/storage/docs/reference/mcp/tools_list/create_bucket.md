---
url: https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/create_bucket/
title: MCP Tools Reference: storage.googleapis.com \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:34.340468+00:00
---

# MCP Tools Reference: storage.googleapis.com  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/create_bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  MCP Tools Reference: storage.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_bucket`

Creates a bucket in a project.

The following sample demonstrates how to use `curl` to invoke the `create_bucket` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://storage.googleapis.com/storage/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_bucket",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

### CreateBucketRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "bucketName": string,
      "location": string,
      "uniformBucketLevelAccess": boolean
    }  
  
Fields  
---  
`projectId` |  `string` Required.   
`bucketName` |  `string` Required. The name of the bucket to create.  
`location` |  `string` Optional. The location of the bucket. Object data for objects in the bucket resides in physical storage within this region. Region names are case-insensitive (e.g., 'us-central1', 'us'). Defaults to 'us' if not specified.  
`uniformBucketLevelAccess` |  `boolean` Optional. If true, enables uniform bucket-level access on the bucket. When enabled, access checks only use bucket-level IAM policies, and Access Control Lists (ACLs) on individual objects are ignored.  
  
## Output Schema

Response message for CreateBucket.

### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
