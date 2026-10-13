---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.answerrecords-class
title: Class protos.google.cloud.dialogflow.v2.AnswerRecords (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:11.865296+00:00
---

# Class protos.google.cloud.dialogflow.v2.AnswerRecords (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.answerrecords-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.AnswerRecords (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents an AnswerRecords

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.AnswerRecords

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AnswerRecords service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AnswerRecords;

Creates new AnswerRecords service using the specified rpc implementation.

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
`[AnswerRecords](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.answerrecords-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### listAnswerRecords(request, callback)
    
    
    public listAnswerRecords(request: google.cloud.dialogflow.v2.IListAnswerRecordsRequest, callback: google.cloud.dialogflow.v2.AnswerRecords.ListAnswerRecordsCallback): void;

Calls ListAnswerRecords.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnswerRecordsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistanswerrecordsrequest)`   
ListAnswerRecordsRequest message or plain object  
`callback` |  `[ListAnswerRecordsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAnswerRecordsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnswerRecords(request)
    
    
    public listAnswerRecords(request: google.cloud.dialogflow.v2.IListAnswerRecordsRequest): Promise<google.cloud.dialogflow.v2.ListAnswerRecordsResponse>;

Calls ListAnswerRecords.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAnswerRecordsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistanswerrecordsrequest)`   
ListAnswerRecordsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListAnswerRecordsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listanswerrecordsresponse)>` | Promise  
  
### updateAnswerRecord(request, callback)
    
    
    public updateAnswerRecord(request: google.cloud.dialogflow.v2.IUpdateAnswerRecordRequest, callback: google.cloud.dialogflow.v2.AnswerRecords.UpdateAnswerRecordCallback): void;

Calls UpdateAnswerRecord.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAnswerRecordRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdateanswerrecordrequest)`   
UpdateAnswerRecordRequest message or plain object  
`callback` |  `[UpdateAnswerRecordCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and AnswerRecord  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAnswerRecord(request)
    
    
    public updateAnswerRecord(request: google.cloud.dialogflow.v2.IUpdateAnswerRecordRequest): Promise<google.cloud.dialogflow.v2.AnswerRecord>;

Calls UpdateAnswerRecord.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAnswerRecordRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdateanswerrecordrequest)`   
UpdateAnswerRecordRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.AnswerRecord](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.answerrecord)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
