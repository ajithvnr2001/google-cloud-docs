---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/delete_feed/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:32.021540+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/delete_feed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `delete_feed`

Delete a feed from Chronicle.

Permanently removes a feed from Chronicle. This action cannot be undone and will stop any data ingestion from this feed.

**Workflow Integration:**

  * Use to permanently remove a feed configuration.
  * Essential for cleaning up unused or obsolete feeds.



**Use Cases:**

  * Remove a feed for a decommissioned data source.
  * Clean up test feeds.



**Example Usage:**

  * `delete_feed(feedId="feed_12345", projectId="my-project", customerId="my-customer", region="us")`



The following sample demonstrate how to use `curl` to invoke the `delete_feed` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "delete_feed",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for DeleteFeed.

### DeleteFeedRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "feedId": string
    }  
  
Fields  
---  
`projectId` |  `string` Google Cloud project ID (required).  
`customerId` |  `string` Chronicle customer ID (required).  
`region` |  `string` Chronicle region (e.g., "us", "europe") (required).  
`feedId` |  `string` The unique ID of the feed to delete.  
  
## Output Schema

A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance:
    
    
    service Foo {
      rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
    }
    

### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
