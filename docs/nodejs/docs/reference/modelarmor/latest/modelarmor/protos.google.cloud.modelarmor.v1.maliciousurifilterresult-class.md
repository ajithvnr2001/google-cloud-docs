---
url: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.maliciousurifilterresult-class
title: Class protos.google.cloud.modelarmor.v1.MaliciousUriFilterResult (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:11:50.092818+00:00
---

# Class protos.google.cloud.modelarmor.v1.MaliciousUriFilterResult (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.maliciousurifilterresult-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.modelarmor.v1.MaliciousUriFilterResult (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0 

Represents a MaliciousUriFilterResult.

## Implements

[protos.google.cloud.modelarmor.v1.IMaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.imaliciousurifilterresult)

## Package

[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.modelarmor.v1.IMaliciousUriFilterResult);

Constructs a new MaliciousUriFilterResult.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.imaliciousurifilterresult)`   
Properties to set  
  
## Properties 

### executionState
    
    
    public executionState: (google.cloud.modelarmor.v1.FilterExecutionState|keyof typeof google.cloud.modelarmor.v1.FilterExecutionState);

MaliciousUriFilterResult executionState.

### maliciousUriMatchedItems
    
    
    public maliciousUriMatchedItems: google.cloud.modelarmor.v1.MaliciousUriFilterResult.IMaliciousUriMatchedItem[];

MaliciousUriFilterResult maliciousUriMatchedItems.

### matchState
    
    
    public matchState: (google.cloud.modelarmor.v1.FilterMatchState|keyof typeof google.cloud.modelarmor.v1.FilterMatchState);

MaliciousUriFilterResult matchState.

### messageItems
    
    
    public messageItems: google.cloud.modelarmor.v1.IMessageItem[];

MaliciousUriFilterResult messageItems.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.modelarmor.v1.IMaliciousUriFilterResult): google.cloud.modelarmor.v1.MaliciousUriFilterResult;

Creates a new MaliciousUriFilterResult instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.imaliciousurifilterresult)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.maliciousurifilterresult-class)` | MaliciousUriFilterResult instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.modelarmor.v1.MaliciousUriFilterResult;

Decodes a MaliciousUriFilterResult message from the specified reader or buffer.

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
`[MaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.maliciousurifilterresult-class)` | MaliciousUriFilterResult  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.modelarmor.v1.MaliciousUriFilterResult;

Decodes a MaliciousUriFilterResult message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.maliciousurifilterresult-class)` | MaliciousUriFilterResult  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.modelarmor.v1.IMaliciousUriFilterResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MaliciousUriFilterResult message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.imaliciousurifilterresult)`   
MaliciousUriFilterResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.modelarmor.v1.IMaliciousUriFilterResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MaliciousUriFilterResult message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.imaliciousurifilterresult)`   
MaliciousUriFilterResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.modelarmor.v1.MaliciousUriFilterResult;

Creates a MaliciousUriFilterResult message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.maliciousurifilterresult-class)` | MaliciousUriFilterResult  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MaliciousUriFilterResult

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

Converts this MaliciousUriFilterResult to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.modelarmor.v1.MaliciousUriFilterResult, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MaliciousUriFilterResult message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MaliciousUriFilterResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.maliciousurifilterresult-class)`   
MaliciousUriFilterResult  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MaliciousUriFilterResult message.

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
