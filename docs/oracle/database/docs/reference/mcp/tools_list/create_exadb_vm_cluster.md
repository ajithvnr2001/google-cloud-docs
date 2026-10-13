---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_exadb_vm_cluster/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:56.849597+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_exadb_vm_cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_exadb_vm_cluster`

Create an Exadb Vm Cluster. An Exadb Vm Cluster is a set of Virtual Machines (VMs) on an Exadata Infrastructure.

The following sample demonstrate how to use `curl` to invoke the `create_exadb_vm_cluster` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_exadb_vm_cluster",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for CreateExadbVmCluster.

### CreateExadbVmClusterRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "exadbVmCluster": {
        object ([ExadbVmCluster](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_exadb_vm_cluster#Input.Schema.ExadbVmCluster))
      },
      "exadbVmClusterId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name of the project to create the Exadb Vm Cluster in. Format: `projects/{project}/locations/{location}`  
`exadbVmCluster` |  `object (`[ExadbVmCluster](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_exadb_vm_cluster#Input.Schema.ExadbVmCluster)`)` Required. The Exadb Vm Cluster to create.  
`exadbVmClusterId` |  `string` Required. The ID to use for the Exadb Vm Cluster that is being created.  
  
### ExadbVmCluster

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "gridImageId": string,
      "nodeCount": integer,
      "enabledEcpuCountPerNode": integer,
      "additionalEcpuCountPerNode": integer,
      "sizeInGbsPerNode": integer,
      "licenseModel": enum (LicenseModel),
      "exascaleDbStorageVault": string,
      "hostnamePrefix": string,
      "sshPublicKeys": [
        string
      ],
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone))
      },
      "shapeAttribute": enum (ShapeAttribute),
      "scanListenerPortTcp": integer,
      "odbSubnet": string,
      "backupOdbSubnet": string,
      "clusterName": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the ExadbVmCluster resource in the following format: projects/{project}/locations/{region}/exadbVmClusters/{exadb_vm_cluster}  
`displayName` |  `string` Required. The display name for the ExadbVmCluster.  
`gridImageId` |  `string` Required. Grid Infrastructure Version.  
`nodeCount` |  `integer` Required. The number of nodes/VMs in the ExadbVmCluster.  
`enabledEcpuCountPerNode` |  `integer` Required. The number of ECPUs enabled per node for an exadata vm cluster on exascale infrastructure.  
`additionalEcpuCountPerNode` |  `integer` Optional. The number of additional ECPUs per node for an Exadata VM cluster on exascale infrastructure.  
`sizeInGbsPerNode` |  `integer` Required. The storage allocation for the exadbvmcluster per node, in gigabytes (GB).  
`licenseModel` |  `enum (`LicenseModel`)` Optional. The license type of the ExadbVmCluster.  
`exascaleDbStorageVault` |  `string` Required. The name of ExascaleDbStorageVault associated with the ExadbVmCluster.  
`hostnamePrefix` |  `string` Required. Prefix for VM cluster host names.  
`sshPublicKeys[]` |  `string` Required. The SSH public keys for the ExadbVmCluster.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone)`)` Optional. The time zone of the ExadbVmCluster.  
`shapeAttribute` |  `enum (`ShapeAttribute`)` Required. The shape attribute of the VM cluster.  
`scanListenerPortTcp` |  `integer` Optional. SCAN listener port - TCP  
`odbSubnet` |  `string` Required. The name of the OdbSubnet associated with the ExadbVmCluster for IP allocation.  
`backupOdbSubnet` |  `string` Required. The name of the backup OdbSubnet associated with the ExadbVmCluster.  
`clusterName` |  `string` Optional. The cluster name for Exascale vm cluster.  
  
### TimeZone

JSON representation  
---  
      
    
    {
      "id": string,
      "version": string
    }  
  
Fields  
---  
`id` |  `string` IANA Time Zone Database time zone. For example "America/New_York".  
`version` |  `string` Optional. IANA Time Zone Database version number. For example "2019a".  
  
## Output Schema

This resource represents a long-running operation that is the result of a network API call.

### Operation

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      },
      "done": boolean,
    
      // Union field result can be only one of the following:
      "error": {
        object ([Status](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database#Output.Schema.Status))
      },
      "response": {
        "@type": string,
        field1: ...,
        ...
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `object` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `object (`[Status](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
`response` |  `object` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
