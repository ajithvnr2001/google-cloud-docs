---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.deployments-class
title: Class protos.google.cloud.dialogflow.cx.v3.Deployments (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:03.409050+00:00
---

# Class protos.google.cloud.dialogflow.cx.v3.Deployments (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.deployments-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.cx.v3.Deployments (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents a Deployments

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.cx.v3.Deployments

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Deployments service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Deployments;

Creates new Deployments service using the specified rpc implementation.

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
`[Deployments](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.deployments-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getDeployment(request, callback)
    
    
    public getDeployment(request: google.cloud.dialogflow.cx.v3.IGetDeploymentRequest, callback: google.cloud.dialogflow.cx.v3.Deployments.GetDeploymentCallback): void;

Calls GetDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetdeploymentrequest)`   
GetDeploymentRequest message or plain object  
`callback` |  `[GetDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and Deployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDeployment(request)
    
    
    public getDeployment(request: google.cloud.dialogflow.cx.v3.IGetDeploymentRequest): Promise<google.cloud.dialogflow.cx.v3.Deployment>;

Calls GetDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetdeploymentrequest)`   
GetDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.Deployment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.deployment-class)>` | Promise  
  
### listDeployments(request, callback)
    
    
    public listDeployments(request: google.cloud.dialogflow.cx.v3.IListDeploymentsRequest, callback: google.cloud.dialogflow.cx.v3.Deployments.ListDeploymentsCallback): void;

Calls ListDeployments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ilistdeploymentsrequest)`   
ListDeploymentsRequest message or plain object  
`callback` |  `[ListDeploymentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDeploymentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDeployments(request)
    
    
    public listDeployments(request: google.cloud.dialogflow.cx.v3.IListDeploymentsRequest): Promise<google.cloud.dialogflow.cx.v3.ListDeploymentsResponse>;

Calls ListDeployments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ilistdeploymentsrequest)`   
ListDeploymentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.ListDeploymentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.listdeploymentsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
