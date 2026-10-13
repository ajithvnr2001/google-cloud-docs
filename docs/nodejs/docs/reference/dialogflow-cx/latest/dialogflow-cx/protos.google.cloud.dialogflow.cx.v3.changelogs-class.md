---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.changelogs-class
title: Class protos.google.cloud.dialogflow.cx.v3.Changelogs (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:53:03.008861+00:00
---

# Class protos.google.cloud.dialogflow.cx.v3.Changelogs (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.changelogs-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.cx.v3.Changelogs (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents a Changelogs

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.cx.v3.Changelogs

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Changelogs service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Changelogs;

Creates new Changelogs service using the specified rpc implementation.

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
`[Changelogs](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.changelogs-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getChangelog(request, callback)
    
    
    public getChangelog(request: google.cloud.dialogflow.cx.v3.IGetChangelogRequest, callback: google.cloud.dialogflow.cx.v3.Changelogs.GetChangelogCallback): void;

Calls GetChangelog.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChangelogRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetchangelogrequest)`   
GetChangelogRequest message or plain object  
`callback` |  `[GetChangelogCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and Changelog  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChangelog(request)
    
    
    public getChangelog(request: google.cloud.dialogflow.cx.v3.IGetChangelogRequest): Promise<google.cloud.dialogflow.cx.v3.Changelog>;

Calls GetChangelog.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetChangelogRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetchangelogrequest)`   
GetChangelogRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.Changelog](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.changelog)>` | Promise  
  
### listChangelogs(request, callback)
    
    
    public listChangelogs(request: google.cloud.dialogflow.cx.v3.IListChangelogsRequest, callback: google.cloud.dialogflow.cx.v3.Changelogs.ListChangelogsCallback): void;

Calls ListChangelogs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChangelogsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ilistchangelogsrequest)`   
ListChangelogsRequest message or plain object  
`callback` |  `[ListChangelogsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and ListChangelogsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChangelogs(request)
    
    
    public listChangelogs(request: google.cloud.dialogflow.cx.v3.IListChangelogsRequest): Promise<google.cloud.dialogflow.cx.v3.ListChangelogsResponse>;

Calls ListChangelogs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListChangelogsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ilistchangelogsrequest)`   
ListChangelogsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.ListChangelogsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.listchangelogsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
