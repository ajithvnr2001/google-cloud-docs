---
url: https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.cloudapiregistry-class
title: Class protos.google.cloud.apiregistry.v1beta.CloudApiRegistry (0.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:10.471671+00:00
---

# Class protos.google.cloud.apiregistry.v1beta.CloudApiRegistry (0.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.cloudapiregistry-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apiregistry.v1beta.CloudApiRegistry (0.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.0 

Represents a CloudApiRegistry

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apiregistry.v1beta.CloudApiRegistry

## Package

[@google-cloud/apiregistry](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CloudApiRegistry service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CloudApiRegistry;

Creates new CloudApiRegistry service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistry](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.cloudapiregistry-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getMcpServer(request, callback)
    
    
    public getMcpServer(request: google.cloud.apiregistry.v1beta.IGetMcpServerRequest, callback: google.cloud.apiregistry.v1beta.CloudApiRegistry.GetMcpServerCallback): void;

Calls GetMcpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcpserverrequest)`   
GetMcpServerRequest message or plain object  
`callback` |  `[GetMcpServerCallback](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and McpServer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMcpServer(request)
    
    
    public getMcpServer(request: google.cloud.apiregistry.v1beta.IGetMcpServerRequest): Promise<google.cloud.apiregistry.v1beta.McpServer>;

Calls GetMcpServer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcpserverrequest)`   
GetMcpServerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apiregistry.v1beta.McpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcpserver)>` | Promise  
  
### getMcpTool(request, callback)
    
    
    public getMcpTool(request: google.cloud.apiregistry.v1beta.IGetMcpToolRequest, callback: google.cloud.apiregistry.v1beta.CloudApiRegistry.GetMcpToolCallback): void;

Calls GetMcpTool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcptoolrequest)`   
GetMcpToolRequest message or plain object  
`callback` |  `[GetMcpToolCallback](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and McpTool  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMcpTool(request)
    
    
    public getMcpTool(request: google.cloud.apiregistry.v1beta.IGetMcpToolRequest): Promise<google.cloud.apiregistry.v1beta.McpTool>;

Calls GetMcpTool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcptoolrequest)`   
GetMcpToolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apiregistry.v1beta.McpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcptool)>` | Promise  
  
### listMcpServers(request, callback)
    
    
    public listMcpServers(request: google.cloud.apiregistry.v1beta.IListMcpServersRequest, callback: google.cloud.apiregistry.v1beta.CloudApiRegistry.ListMcpServersCallback): void;

Calls ListMcpServers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest)`   
ListMcpServersRequest message or plain object  
`callback` |  `[ListMcpServersCallback](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMcpServersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMcpServers(request)
    
    
    public listMcpServers(request: google.cloud.apiregistry.v1beta.IListMcpServersRequest): Promise<google.cloud.apiregistry.v1beta.ListMcpServersResponse>;

Calls ListMcpServers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest)`   
ListMcpServersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apiregistry.v1beta.ListMcpServersResponse](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.listmcpserversresponse)>` | Promise  
  
### listMcpTools(request, callback)
    
    
    public listMcpTools(request: google.cloud.apiregistry.v1beta.IListMcpToolsRequest, callback: google.cloud.apiregistry.v1beta.CloudApiRegistry.ListMcpToolsCallback): void;

Calls ListMcpTools.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest)`   
ListMcpToolsRequest message or plain object  
`callback` |  `[ListMcpToolsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMcpToolsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMcpTools(request)
    
    
    public listMcpTools(request: google.cloud.apiregistry.v1beta.IListMcpToolsRequest): Promise<google.cloud.apiregistry.v1beta.ListMcpToolsResponse>;

Calls ListMcpTools.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest)`   
ListMcpToolsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apiregistry.v1beta.ListMcpToolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.listmcptoolsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
