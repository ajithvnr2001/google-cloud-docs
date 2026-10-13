---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationdatasets-class
title: Class protos.google.cloud.dialogflow.v2.ConversationDatasets (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:34.999089+00:00
---

# Class protos.google.cloud.dialogflow.v2.ConversationDatasets (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationdatasets-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.ConversationDatasets (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a ConversationDatasets

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.ConversationDatasets

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ConversationDatasets service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ConversationDatasets;

Creates new ConversationDatasets service using the specified rpc implementation.

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
`[ConversationDatasets](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationdatasets-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConversationDataset(request, callback)
    
    
    public createConversationDataset(request: google.cloud.dialogflow.v2.ICreateConversationDatasetRequest, callback: google.cloud.dialogflow.v2.ConversationDatasets.CreateConversationDatasetCallback): void;

Calls CreateConversationDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationdatasetrequest)`   
CreateConversationDatasetRequest message or plain object  
`callback` |  `[CreateConversationDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversationDataset(request)
    
    
    public createConversationDataset(request: google.cloud.dialogflow.v2.ICreateConversationDatasetRequest): Promise<google.longrunning.Operation>;

Calls CreateConversationDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationdatasetrequest)`   
CreateConversationDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### deleteConversationDataset(request, callback)
    
    
    public deleteConversationDataset(request: google.cloud.dialogflow.v2.IDeleteConversationDatasetRequest, callback: google.cloud.dialogflow.v2.ConversationDatasets.DeleteConversationDatasetCallback): void;

Calls DeleteConversationDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteconversationdatasetrequest)`   
DeleteConversationDatasetRequest message or plain object  
`callback` |  `[DeleteConversationDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversationDataset(request)
    
    
    public deleteConversationDataset(request: google.cloud.dialogflow.v2.IDeleteConversationDatasetRequest): Promise<google.longrunning.Operation>;

Calls DeleteConversationDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteconversationdatasetrequest)`   
DeleteConversationDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### getConversationDataset(request, callback)
    
    
    public getConversationDataset(request: google.cloud.dialogflow.v2.IGetConversationDatasetRequest, callback: google.cloud.dialogflow.v2.ConversationDatasets.GetConversationDatasetCallback): void;

Calls GetConversationDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationdatasetrequest)`   
GetConversationDatasetRequest message or plain object  
`callback` |  `[GetConversationDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversationDataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversationDataset(request)
    
    
    public getConversationDataset(request: google.cloud.dialogflow.v2.IGetConversationDatasetRequest): Promise<google.cloud.dialogflow.v2.ConversationDataset>;

Calls GetConversationDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationdatasetrequest)`   
GetConversationDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ConversationDataset](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationdataset)>` | Promise  
  
### importConversationData(request, callback)
    
    
    public importConversationData(request: google.cloud.dialogflow.v2.IImportConversationDataRequest, callback: google.cloud.dialogflow.v2.ConversationDatasets.ImportConversationDataCallback): void;

Calls ImportConversationData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportConversationDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iimportconversationdatarequest)`   
ImportConversationDataRequest message or plain object  
`callback` |  `[ImportConversationDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importConversationData(request)
    
    
    public importConversationData(request: google.cloud.dialogflow.v2.IImportConversationDataRequest): Promise<google.longrunning.Operation>;

Calls ImportConversationData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportConversationDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iimportconversationdatarequest)`   
ImportConversationDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### listConversationDatasets(request, callback)
    
    
    public listConversationDatasets(request: google.cloud.dialogflow.v2.IListConversationDatasetsRequest, callback: google.cloud.dialogflow.v2.ConversationDatasets.ListConversationDatasetsCallback): void;

Calls ListConversationDatasets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationdatasetsrequest)`   
ListConversationDatasetsRequest message or plain object  
`callback` |  `[ListConversationDatasetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversationDatasetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversationDatasets(request)
    
    
    public listConversationDatasets(request: google.cloud.dialogflow.v2.IListConversationDatasetsRequest): Promise<google.cloud.dialogflow.v2.ListConversationDatasetsResponse>;

Calls ListConversationDatasets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationdatasetsrequest)`   
ListConversationDatasetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListConversationDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listconversationdatasetsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
