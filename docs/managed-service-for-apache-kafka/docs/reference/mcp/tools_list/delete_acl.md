---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/delete_acl/
title: MCP Tools Reference: managedkafka \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:24.878716+00:00
---

# MCP Tools Reference: managedkafka  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/delete_acl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)



Send feedback 

#  MCP Tools Reference: managedkafka Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `delete_acl`

Deletes a Google Cloud Managed Service for Apache Kafka ACL. Please provide the Project ID, Location, Cluster ID, and ACL ID.

A DeleteAclRequest is used to delete an ACL.

  * `name` (required): The name of the ACL to delete. Structured like `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. `acl_id` is structured like one of the following: 
    * For ACLs on the cluster: `cluster`
    * For ACLs on a single resource within the cluster: `topic/{resource_name}`, `consumerGroup/{resource_name}`, or `transactionalId/{resource_name}`
    * For ACLs on all resources that match a prefix: `topicPrefixed/{resource_name}`, `consumerGroupPrefixed/{resource_name}`, or `transactionalIdPrefixed/{resource_name}`
    * For ACLs on all resources of a given type (i.e. the wildcard literal "*"): `allTopics` (represents `topic/*`), `allConsumerGroups` (represents `consumerGroup/*`), or `allTransactionalIds` (represents `transactionalId/*`)



The following sample demonstrate how to use `curl` to invoke the `delete_acl` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://managedkafka.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "delete_acl",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for DeleteAcl.

### DeleteAclRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the acl to delete. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`.The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
  
## Output Schema

A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance:
    
    
    service Foo {
      rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
    }
    

### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-03 UTC."],[],[]] 
