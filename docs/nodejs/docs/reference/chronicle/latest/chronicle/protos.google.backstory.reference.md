---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.reference
title: Class protos.google.backstory.Reference (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:56.316456+00:00
---

# Class protos.google.backstory.Reference (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.reference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.backstory.Reference (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a Reference.

## Implements

[protos.google.backstory.IReference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.ireference)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.backstory.IReference);

Constructs a new Reference.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IReference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.ireference)`   
Properties to set  
  
## Properties 

### entity
    
    
    public entity?: (google.backstory.IEntity|null);

Reference entity.

### event
    
    
    public event?: (google.backstory.IUDM|null);

Reference event.

### graphEnrichment
    
    
    public graphEnrichment?: (google.backstory.IEntityGraphEnrichment|null);

Reference graphEnrichment.

### id
    
    
    public id?: (google.backstory.IId|null);

Reference id.

### joinedDataTableRows
    
    
    public joinedDataTableRows: google.backstory.IDataTableRowInfo[];

Reference joinedDataTableRows.

### logBatchToken
    
    
    public logBatchToken: string;

Reference logBatchToken.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.backstory.IReference): google.backstory.Reference;

Creates a new Reference instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IReference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.ireference)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Reference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.reference)` | Reference instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.backstory.Reference;

Decodes a Reference message from the specified reader or buffer.

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
`[Reference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.reference)` | Reference  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.backstory.Reference;

Decodes a Reference message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Reference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.reference)` | Reference  
  
### encode(message, writer)
    
    
    public static encode(message: google.backstory.IReference, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Reference message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IReference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.ireference)`   
Reference message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.backstory.IReference, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Reference message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IReference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.ireference)`   
Reference message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.backstory.Reference;

Creates a Reference message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Reference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.reference)` | Reference  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Reference

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

Converts this Reference to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.backstory.Reference, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Reference message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Reference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.reference)`   
Reference  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Reference message.

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
