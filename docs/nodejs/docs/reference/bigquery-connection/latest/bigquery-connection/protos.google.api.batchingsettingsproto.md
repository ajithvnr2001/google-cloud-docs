---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.batchingsettingsproto
title: Class protos.google.api.BatchingSettingsProto (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:02.448656+00:00
---

# Class protos.google.api.BatchingSettingsProto (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.batchingsettingsproto

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.BatchingSettingsProto (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  2.2.1  2.1.1  2.0.2  1.5.1  1.4.2  1.3.5 

Represents a BatchingSettingsProto.

## Implements

[protos.google.api.IBatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.ibatchingsettingsproto)

## Package

[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IBatchingSettingsProto);

Constructs a new BatchingSettingsProto.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.ibatchingsettingsproto)`   
Properties to set  
  
## Properties 

### delayThreshold
    
    
    public delayThreshold?: (google.protobuf.IDuration|null);

BatchingSettingsProto delayThreshold.

### elementCountLimit
    
    
    public elementCountLimit: number;

BatchingSettingsProto elementCountLimit.

### elementCountThreshold
    
    
    public elementCountThreshold: number;

BatchingSettingsProto elementCountThreshold.

### flowControlByteLimit
    
    
    public flowControlByteLimit: number;

BatchingSettingsProto flowControlByteLimit.

### flowControlElementLimit
    
    
    public flowControlElementLimit: number;

BatchingSettingsProto flowControlElementLimit.

### flowControlLimitExceededBehavior
    
    
    public flowControlLimitExceededBehavior: (google.api.FlowControlLimitExceededBehaviorProto|keyof typeof google.api.FlowControlLimitExceededBehaviorProto);

BatchingSettingsProto flowControlLimitExceededBehavior.

### requestByteLimit
    
    
    public requestByteLimit: number;

BatchingSettingsProto requestByteLimit.

### requestByteThreshold
    
    
    public requestByteThreshold: (number|Long|string);

BatchingSettingsProto requestByteThreshold.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IBatchingSettingsProto): google.api.BatchingSettingsProto;

Creates a new BatchingSettingsProto instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.ibatchingsettingsproto)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.batchingsettingsproto)` | BatchingSettingsProto instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.BatchingSettingsProto;

Decodes a BatchingSettingsProto message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[BatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.batchingsettingsproto)` | BatchingSettingsProto  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.BatchingSettingsProto;

Decodes a BatchingSettingsProto message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.batchingsettingsproto)` | BatchingSettingsProto  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IBatchingSettingsProto, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchingSettingsProto message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.ibatchingsettingsproto)`   
BatchingSettingsProto message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IBatchingSettingsProto, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchingSettingsProto message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.ibatchingsettingsproto)`   
BatchingSettingsProto message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.BatchingSettingsProto;

Creates a BatchingSettingsProto message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.batchingsettingsproto)` | BatchingSettingsProto  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BatchingSettingsProto

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this BatchingSettingsProto to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.BatchingSettingsProto, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BatchingSettingsProto message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BatchingSettingsProto](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.api.batchingsettingsproto)`   
BatchingSettingsProto  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BatchingSettingsProto message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
