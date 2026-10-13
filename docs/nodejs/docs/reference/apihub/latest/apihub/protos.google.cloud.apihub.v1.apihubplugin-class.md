---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubplugin-class
title: Class protos.google.cloud.apihub.v1.ApiHubPlugin (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:43.130108+00:00
---

# Class protos.google.cloud.apihub.v1.ApiHubPlugin (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubplugin-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.ApiHubPlugin (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an ApiHubPlugin

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apihub.v1.ApiHubPlugin

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ApiHubPlugin service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ApiHubPlugin;

Creates new ApiHubPlugin service using the specified rpc implementation.

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
`[ApiHubPlugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubplugin-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createPlugin(request, callback)
    
    
    public createPlugin(request: google.cloud.apihub.v1.ICreatePluginRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.CreatePluginCallback): void;

Calls CreatePlugin.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatepluginrequest)`   
CreatePluginRequest message or plain object  
`callback` |  `[CreatePluginCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Plugin  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPlugin(request)
    
    
    public createPlugin(request: google.cloud.apihub.v1.ICreatePluginRequest): Promise<google.cloud.apihub.v1.Plugin>;

Calls CreatePlugin.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatepluginrequest)`   
CreatePluginRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Plugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class)>` | Promise  
  
### createPluginInstance(request, callback)
    
    
    public createPluginInstance(request: google.cloud.apihub.v1.ICreatePluginInstanceRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.CreatePluginInstanceCallback): void;

Calls CreatePluginInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePluginInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateplugininstancerequest)`   
CreatePluginInstanceRequest message or plain object  
`callback` |  `[CreatePluginInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPluginInstance(request)
    
    
    public createPluginInstance(request: google.cloud.apihub.v1.ICreatePluginInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreatePluginInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePluginInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreateplugininstancerequest)`   
CreatePluginInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.longrunning.operation)>` | Promise  
  
### deletePlugin(request, callback)
    
    
    public deletePlugin(request: google.cloud.apihub.v1.IDeletePluginRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.DeletePluginCallback): void;

Calls DeletePlugin.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletepluginrequest)`   
DeletePluginRequest message or plain object  
`callback` |  `[DeletePluginCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePlugin(request)
    
    
    public deletePlugin(request: google.cloud.apihub.v1.IDeletePluginRequest): Promise<google.longrunning.Operation>;

Calls DeletePlugin.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideletepluginrequest)`   
DeletePluginRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.longrunning.operation)>` | Promise  
  
### deletePluginInstance(request, callback)
    
    
    public deletePluginInstance(request: google.cloud.apihub.v1.IDeletePluginInstanceRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.DeletePluginInstanceCallback): void;

Calls DeletePluginInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePluginInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteplugininstancerequest)`   
DeletePluginInstanceRequest message or plain object  
`callback` |  `[DeletePluginInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePluginInstance(request)
    
    
    public deletePluginInstance(request: google.cloud.apihub.v1.IDeletePluginInstanceRequest): Promise<google.longrunning.Operation>;

Calls DeletePluginInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePluginInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideleteplugininstancerequest)`   
DeletePluginInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.longrunning.operation)>` | Promise  
  
### disablePlugin(request, callback)
    
    
    public disablePlugin(request: google.cloud.apihub.v1.IDisablePluginRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.DisablePluginCallback): void;

Calls DisablePlugin.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisablePluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.idisablepluginrequest)`   
DisablePluginRequest message or plain object  
`callback` |  `[DisablePluginCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Plugin  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disablePlugin(request)
    
    
    public disablePlugin(request: google.cloud.apihub.v1.IDisablePluginRequest): Promise<google.cloud.apihub.v1.Plugin>;

Calls DisablePlugin.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDisablePluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.idisablepluginrequest)`   
DisablePluginRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Plugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class)>` | Promise  
  
### disablePluginInstanceAction(request, callback)
    
    
    public disablePluginInstanceAction(request: google.cloud.apihub.v1.IDisablePluginInstanceActionRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.DisablePluginInstanceActionCallback): void;

Calls DisablePluginInstanceAction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisablePluginInstanceActionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.idisableplugininstanceactionrequest)`   
DisablePluginInstanceActionRequest message or plain object  
`callback` |  `[DisablePluginInstanceActionCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disablePluginInstanceAction(request)
    
    
    public disablePluginInstanceAction(request: google.cloud.apihub.v1.IDisablePluginInstanceActionRequest): Promise<google.longrunning.Operation>;

Calls DisablePluginInstanceAction.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDisablePluginInstanceActionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.idisableplugininstanceactionrequest)`   
DisablePluginInstanceActionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.longrunning.operation)>` | Promise  
  
### enablePlugin(request, callback)
    
    
    public enablePlugin(request: google.cloud.apihub.v1.IEnablePluginRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.EnablePluginCallback): void;

Calls EnablePlugin.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnablePluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ienablepluginrequest)`   
EnablePluginRequest message or plain object  
`callback` |  `[EnablePluginCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Plugin  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enablePlugin(request)
    
    
    public enablePlugin(request: google.cloud.apihub.v1.IEnablePluginRequest): Promise<google.cloud.apihub.v1.Plugin>;

Calls EnablePlugin.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEnablePluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ienablepluginrequest)`   
EnablePluginRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Plugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class)>` | Promise  
  
### enablePluginInstanceAction(request, callback)
    
    
    public enablePluginInstanceAction(request: google.cloud.apihub.v1.IEnablePluginInstanceActionRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.EnablePluginInstanceActionCallback): void;

Calls EnablePluginInstanceAction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnablePluginInstanceActionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ienableplugininstanceactionrequest)`   
EnablePluginInstanceActionRequest message or plain object  
`callback` |  `[EnablePluginInstanceActionCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enablePluginInstanceAction(request)
    
    
    public enablePluginInstanceAction(request: google.cloud.apihub.v1.IEnablePluginInstanceActionRequest): Promise<google.longrunning.Operation>;

Calls EnablePluginInstanceAction.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEnablePluginInstanceActionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ienableplugininstanceactionrequest)`   
EnablePluginInstanceActionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.longrunning.operation)>` | Promise  
  
### executePluginInstanceAction(request, callback)
    
    
    public executePluginInstanceAction(request: google.cloud.apihub.v1.IExecutePluginInstanceActionRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.ExecutePluginInstanceActionCallback): void;

Calls ExecutePluginInstanceAction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExecutePluginInstanceActionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iexecuteplugininstanceactionrequest)`   
ExecutePluginInstanceActionRequest message or plain object  
`callback` |  `[ExecutePluginInstanceActionCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### executePluginInstanceAction(request)
    
    
    public executePluginInstanceAction(request: google.cloud.apihub.v1.IExecutePluginInstanceActionRequest): Promise<google.longrunning.Operation>;

Calls ExecutePluginInstanceAction.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExecutePluginInstanceActionRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iexecuteplugininstanceactionrequest)`   
ExecutePluginInstanceActionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.longrunning.operation)>` | Promise  
  
### getPlugin(request, callback)
    
    
    public getPlugin(request: google.cloud.apihub.v1.IGetPluginRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.GetPluginCallback): void;

Calls GetPlugin.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetpluginrequest)`   
GetPluginRequest message or plain object  
`callback` |  `[GetPluginCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Plugin  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPlugin(request)
    
    
    public getPlugin(request: google.cloud.apihub.v1.IGetPluginRequest): Promise<google.cloud.apihub.v1.Plugin>;

Calls GetPlugin.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPluginRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetpluginrequest)`   
GetPluginRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.Plugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class)>` | Promise  
  
### getPluginInstance(request, callback)
    
    
    public getPluginInstance(request: google.cloud.apihub.v1.IGetPluginInstanceRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.GetPluginInstanceCallback): void;

Calls GetPluginInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPluginInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetplugininstancerequest)`   
GetPluginInstanceRequest message or plain object  
`callback` |  `[GetPluginInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and PluginInstance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPluginInstance(request)
    
    
    public getPluginInstance(request: google.cloud.apihub.v1.IGetPluginInstanceRequest): Promise<google.cloud.apihub.v1.PluginInstance>;

Calls GetPluginInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPluginInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetplugininstancerequest)`   
GetPluginInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.PluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugininstance-class)>` | Promise  
  
### listPluginInstances(request, callback)
    
    
    public listPluginInstances(request: google.cloud.apihub.v1.IListPluginInstancesRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.ListPluginInstancesCallback): void;

Calls ListPluginInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPluginInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistplugininstancesrequest)`   
ListPluginInstancesRequest message or plain object  
`callback` |  `[ListPluginInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPluginInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPluginInstances(request)
    
    
    public listPluginInstances(request: google.cloud.apihub.v1.IListPluginInstancesRequest): Promise<google.cloud.apihub.v1.ListPluginInstancesResponse>;

Calls ListPluginInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPluginInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistplugininstancesrequest)`   
ListPluginInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListPluginInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listplugininstancesresponse)>` | Promise  
  
### listPlugins(request, callback)
    
    
    public listPlugins(request: google.cloud.apihub.v1.IListPluginsRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.ListPluginsCallback): void;

Calls ListPlugins.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPluginsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistpluginsrequest)`   
ListPluginsRequest message or plain object  
`callback` |  `[ListPluginsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPluginsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPlugins(request)
    
    
    public listPlugins(request: google.cloud.apihub.v1.IListPluginsRequest): Promise<google.cloud.apihub.v1.ListPluginsResponse>;

Calls ListPlugins.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPluginsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilistpluginsrequest)`   
ListPluginsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListPluginsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listpluginsresponse)>` | Promise  
  
### updatePluginInstance(request, callback)
    
    
    public updatePluginInstance(request: google.cloud.apihub.v1.IUpdatePluginInstanceRequest, callback: google.cloud.apihub.v1.ApiHubPlugin.UpdatePluginInstanceCallback): void;

Calls UpdatePluginInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePluginInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateplugininstancerequest)`   
UpdatePluginInstanceRequest message or plain object  
`callback` |  `[UpdatePluginInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and PluginInstance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePluginInstance(request)
    
    
    public updatePluginInstance(request: google.cloud.apihub.v1.IUpdatePluginInstanceRequest): Promise<google.cloud.apihub.v1.PluginInstance>;

Calls UpdatePluginInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePluginInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdateplugininstancerequest)`   
UpdatePluginInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.PluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugininstance-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
