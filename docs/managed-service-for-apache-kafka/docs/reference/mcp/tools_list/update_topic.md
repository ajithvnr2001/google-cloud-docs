---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/update_topic/
title: MCP Tools Reference: managedkafka \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:18.745944+00:00
---

# MCP Tools Reference: managedkafka  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/update_topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/apis)



Send feedback 

#  MCP Tools Reference: managedkafka Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_topic`

Update an existing Google Cloud Managed service for Apache Kafka topic.

**Important Notes:**

  * The UpdateTopic request requires the name of the topic to be updated in the format `projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}`.



The following sample demonstrate how to use `curl` to invoke the `update_topic` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://managedkafka.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_topic",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for UpdateTopic.

### UpdateTopicRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "configs": {
        string: string,
        ...
      },
      "fieldsToClear": [
        string
      ],
    
      // Union field _partition_count can be only one of the following:
      "partitionCount": integer
      // End of list of possible types for union field _partition_count.
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the topic to update. Format: projects/{project}/locations/{location}/clusters/{cluster_id}/topics/{topic_id}  
`configs` |  `map (key: string, value: string)` Optional. Configurations for the topic that are overridden from the cluster defaults. Note that this will replace the entire set of configs for the topic.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`fieldsToClear[]` |  `string` Optional. Fields to clear in the topic update.  
Union field `_partition_count`.`_partition_count` can be only one of the following:  
`partitionCount` |  `integer` Optional. The number of partitions this topic has.  
  
### ConfigsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
## Output Schema

A Kafka topic in a given cluster.

### Topic

JSON representation  
---  
      
    
    {
      "name": string,
      "partitionCount": integer,
      "replicationFactor": integer,
      "configs": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the topic. The `topic` segment is used when connecting directly to the cluster. Structured like: projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}  
`partitionCount` |  `integer` Required. The number of partitions this topic has. The partition count can only be increased, not decreased. Please note that if partitions are increased for a topic that has a key, the partitioning logic or the ordering of the messages will be affected.  
`replicationFactor` |  `integer` Required. Immutable. The number of replicas of each partition. A replication factor of 3 is recommended for high availability.  
`configs` |  `map (key: string, value: string)` Optional. Configurations for the topic that are overridden from the cluster defaults. The key of the map is a Kafka topic property name, for example: `cleanup.policy`, `compression.type`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### ConfigsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
