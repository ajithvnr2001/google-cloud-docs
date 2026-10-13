---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.messagesv1beta3-class
title: Class protos.google.dataflow.v1beta3.MessagesV1Beta3 (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:13.594713+00:00
---

# Class protos.google.dataflow.v1beta3.MessagesV1Beta3 (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.messagesv1beta3-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.dataflow.v1beta3.MessagesV1Beta3 (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.0.2  2.1.2  2.0.1  1.2.0  1.1.0  1.0.2 

Represents a MessagesV1Beta3

## Inheritance

$protobuf.rpc.Service > protos.google.dataflow.v1beta3.MessagesV1Beta3

## Package

[@google-cloud/dataflow](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new MessagesV1Beta3 service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): MessagesV1Beta3;

Creates new MessagesV1Beta3 service using the specified rpc implementation.

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
`[MessagesV1Beta3](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.messagesv1beta3-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### listJobMessages(request, callback)
    
    
    public listJobMessages(request: google.dataflow.v1beta3.IListJobMessagesRequest, callback: google.dataflow.v1beta3.MessagesV1Beta3.ListJobMessagesCallback): void;

Calls ListJobMessages.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListJobMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.ilistjobmessagesrequest)`   
ListJobMessagesRequest message or plain object  
`callback` |  `[ListJobMessagesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListJobMessagesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listJobMessages(request)
    
    
    public listJobMessages(request: google.dataflow.v1beta3.IListJobMessagesRequest): Promise<google.dataflow.v1beta3.ListJobMessagesResponse>;

Calls ListJobMessages.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListJobMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.ilistjobmessagesrequest)`   
ListJobMessagesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.dataflow.v1beta3.ListJobMessagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.listjobmessagesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
