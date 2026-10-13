---
url: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.raifiltertyperesult
title: Class protos.google.cloud.modelarmor.v1.RaiFilterResult.RaiFilterTypeResult (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:11:52.313777+00:00
---

# Class protos.google.cloud.modelarmor.v1.RaiFilterResult.RaiFilterTypeResult (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.raifiltertyperesult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.modelarmor.v1.RaiFilterResult.RaiFilterTypeResult (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0 

Represents a RaiFilterTypeResult.

## Implements

[protos.google.cloud.modelarmor.v1.RaiFilterResult.IRaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.iraifiltertyperesult)

## Package

[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.modelarmor.v1.RaiFilterResult.IRaiFilterTypeResult);

Constructs a new RaiFilterTypeResult.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.iraifiltertyperesult)`   
Properties to set  
  
## Properties 

### confidenceLevel
    
    
    public confidenceLevel: (google.cloud.modelarmor.v1.DetectionConfidenceLevel|keyof typeof google.cloud.modelarmor.v1.DetectionConfidenceLevel);

RaiFilterTypeResult confidenceLevel.

### filterType
    
    
    public filterType: (google.cloud.modelarmor.v1.RaiFilterType|keyof typeof google.cloud.modelarmor.v1.RaiFilterType);

RaiFilterTypeResult filterType.

### matchState
    
    
    public matchState: (google.cloud.modelarmor.v1.FilterMatchState|keyof typeof google.cloud.modelarmor.v1.FilterMatchState);

RaiFilterTypeResult matchState.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.modelarmor.v1.RaiFilterResult.IRaiFilterTypeResult): google.cloud.modelarmor.v1.RaiFilterResult.RaiFilterTypeResult;

Creates a new RaiFilterTypeResult instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.iraifiltertyperesult)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.raifiltertyperesult)` | RaiFilterTypeResult instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.modelarmor.v1.RaiFilterResult.RaiFilterTypeResult;

Decodes a RaiFilterTypeResult message from the specified reader or buffer.

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
`[RaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.raifiltertyperesult)` | RaiFilterTypeResult  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.modelarmor.v1.RaiFilterResult.RaiFilterTypeResult;

Decodes a RaiFilterTypeResult message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.raifiltertyperesult)` | RaiFilterTypeResult  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.modelarmor.v1.RaiFilterResult.IRaiFilterTypeResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RaiFilterTypeResult message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.iraifiltertyperesult)`   
RaiFilterTypeResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.modelarmor.v1.RaiFilterResult.IRaiFilterTypeResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RaiFilterTypeResult message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.iraifiltertyperesult)`   
RaiFilterTypeResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.modelarmor.v1.RaiFilterResult.RaiFilterTypeResult;

Creates a RaiFilterTypeResult message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.raifiltertyperesult)` | RaiFilterTypeResult  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RaiFilterTypeResult

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

Converts this RaiFilterTypeResult to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.modelarmor.v1.RaiFilterResult.RaiFilterTypeResult, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RaiFilterTypeResult message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RaiFilterTypeResult](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifilterresult.raifiltertyperesult)`   
RaiFilterTypeResult  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RaiFilterTypeResult message.

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
