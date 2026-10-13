---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/delete_topic/
title: MCP Tools Reference: managedkafka \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:53.244071+00:00
---

# MCP Tools Reference: managedkafka  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/delete_topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/apis)



Send feedback 

#  MCP Tools Reference: managedkafka Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `delete_topic`

Deletes a Google Cloud Managed Service for Apache Kafka topic.

The following sample demonstrate how to use `curl` to invoke the `delete_topic` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://managedkafka.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "delete_topic",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for DeleteTopic.

### DeleteTopicRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the topic to delete. Format: projects/{project}/locations/{location}/clusters/{cluster_id}/topics/{topic_id}  
  
## Output Schema

A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance:
    
    
    service Foo {
      rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
    }
    

### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
