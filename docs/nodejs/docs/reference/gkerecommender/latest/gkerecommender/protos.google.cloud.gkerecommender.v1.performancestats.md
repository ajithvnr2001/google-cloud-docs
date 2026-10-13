---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancestats
title: Class protos.google.cloud.gkerecommender.v1.PerformanceStats (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:05.643205+00:00
---

# Class protos.google.cloud.gkerecommender.v1.PerformanceStats (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancestats

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkerecommender.v1.PerformanceStats (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a PerformanceStats.

## Implements

[protos.google.cloud.gkerecommender.v1.IPerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancestats)

## Package

[@google-cloud/gkerecommender](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkerecommender.v1.IPerformanceStats);

Constructs a new PerformanceStats.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancestats)`   
Properties to set  
  
## Properties 

### cost
    
    
    public cost: google.cloud.gkerecommender.v1.ICost[];

PerformanceStats cost.

### ntpotMilliseconds
    
    
    public ntpotMilliseconds: number;

PerformanceStats ntpotMilliseconds.

### outputTokensPerSecond
    
    
    public outputTokensPerSecond: number;

PerformanceStats outputTokensPerSecond.

### queriesPerSecond
    
    
    public queriesPerSecond: number;

PerformanceStats queriesPerSecond.

### ttftMilliseconds
    
    
    public ttftMilliseconds: number;

PerformanceStats ttftMilliseconds.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkerecommender.v1.IPerformanceStats): google.cloud.gkerecommender.v1.PerformanceStats;

Creates a new PerformanceStats instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancestats)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancestats)` | PerformanceStats instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkerecommender.v1.PerformanceStats;

Decodes a PerformanceStats message from the specified reader or buffer.

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
`[PerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancestats)` | PerformanceStats  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkerecommender.v1.PerformanceStats;

Decodes a PerformanceStats message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancestats)` | PerformanceStats  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkerecommender.v1.IPerformanceStats, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PerformanceStats message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancestats)`   
PerformanceStats message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkerecommender.v1.IPerformanceStats, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PerformanceStats message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancestats)`   
PerformanceStats message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkerecommender.v1.PerformanceStats;

Creates a PerformanceStats message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancestats)` | PerformanceStats  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PerformanceStats

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

Converts this PerformanceStats to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkerecommender.v1.PerformanceStats, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PerformanceStats message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PerformanceStats](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancestats)`   
PerformanceStats  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PerformanceStats message.

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
