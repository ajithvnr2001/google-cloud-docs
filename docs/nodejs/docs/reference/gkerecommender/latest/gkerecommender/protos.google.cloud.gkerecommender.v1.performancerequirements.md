---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancerequirements
title: Class protos.google.cloud.gkerecommender.v1.PerformanceRequirements (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:49:07.824334+00:00
---

# Class protos.google.cloud.gkerecommender.v1.PerformanceRequirements (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancerequirements

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkerecommender.v1.PerformanceRequirements (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a PerformanceRequirements.

## Implements

[protos.google.cloud.gkerecommender.v1.IPerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancerequirements)

## Package

[@google-cloud/gkerecommender](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkerecommender.v1.IPerformanceRequirements);

Constructs a new PerformanceRequirements.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancerequirements)`   
Properties to set  
  
## Properties 

### targetCost
    
    
    public targetCost?: (google.cloud.gkerecommender.v1.ICost|null);

PerformanceRequirements targetCost.

### targetNtpotMilliseconds
    
    
    public targetNtpotMilliseconds?: (number|null);

PerformanceRequirements targetNtpotMilliseconds.

### targetTtftMilliseconds
    
    
    public targetTtftMilliseconds?: (number|null);

PerformanceRequirements targetTtftMilliseconds.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkerecommender.v1.IPerformanceRequirements): google.cloud.gkerecommender.v1.PerformanceRequirements;

Creates a new PerformanceRequirements instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancerequirements)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancerequirements)` | PerformanceRequirements instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkerecommender.v1.PerformanceRequirements;

Decodes a PerformanceRequirements message from the specified reader or buffer.

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
`[PerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancerequirements)` | PerformanceRequirements  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkerecommender.v1.PerformanceRequirements;

Decodes a PerformanceRequirements message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancerequirements)` | PerformanceRequirements  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkerecommender.v1.IPerformanceRequirements, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PerformanceRequirements message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancerequirements)`   
PerformanceRequirements message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkerecommender.v1.IPerformanceRequirements, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PerformanceRequirements message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.iperformancerequirements)`   
PerformanceRequirements message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkerecommender.v1.PerformanceRequirements;

Creates a PerformanceRequirements message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancerequirements)` | PerformanceRequirements  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PerformanceRequirements

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

Converts this PerformanceRequirements to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkerecommender.v1.PerformanceRequirements, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PerformanceRequirements message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PerformanceRequirements](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.performancerequirements)`   
PerformanceRequirements  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PerformanceRequirements message.

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
