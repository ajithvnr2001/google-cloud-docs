---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.disableplannertransfer
title: Class protos.google.cloud.ces.v1.TransferRule.DisablePlannerTransfer (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:13.024574+00:00
---

# Class protos.google.cloud.ces.v1.TransferRule.DisablePlannerTransfer (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.disableplannertransfer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.TransferRule.DisablePlannerTransfer (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents a DisablePlannerTransfer.

## Implements

[protos.google.cloud.ces.v1.TransferRule.IDisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.idisableplannertransfer)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.TransferRule.IDisablePlannerTransfer);

Constructs a new DisablePlannerTransfer.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.idisableplannertransfer)`   
Properties to set  
  
## Properties 

### expressionCondition
    
    
    public expressionCondition?: (google.cloud.ces.v1.IExpressionCondition|null);

DisablePlannerTransfer expressionCondition.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.TransferRule.IDisablePlannerTransfer): google.cloud.ces.v1.TransferRule.DisablePlannerTransfer;

Creates a new DisablePlannerTransfer instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.idisableplannertransfer)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.disableplannertransfer)` | DisablePlannerTransfer instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.TransferRule.DisablePlannerTransfer;

Decodes a DisablePlannerTransfer message from the specified reader or buffer.

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
`[DisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.disableplannertransfer)` | DisablePlannerTransfer  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.TransferRule.DisablePlannerTransfer;

Decodes a DisablePlannerTransfer message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.disableplannertransfer)` | DisablePlannerTransfer  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.TransferRule.IDisablePlannerTransfer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DisablePlannerTransfer message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.idisableplannertransfer)`   
DisablePlannerTransfer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.TransferRule.IDisablePlannerTransfer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DisablePlannerTransfer message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.idisableplannertransfer)`   
DisablePlannerTransfer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.TransferRule.DisablePlannerTransfer;

Creates a DisablePlannerTransfer message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.disableplannertransfer)` | DisablePlannerTransfer  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DisablePlannerTransfer

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

Converts this DisablePlannerTransfer to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.TransferRule.DisablePlannerTransfer, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DisablePlannerTransfer message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DisablePlannerTransfer](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.transferrule.disableplannertransfer)`   
DisablePlannerTransfer  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DisablePlannerTransfer message.

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
