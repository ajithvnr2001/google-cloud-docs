---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iocstats
title: Class protos.google.backstory.SecurityResult.IoCStats (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:23.871519+00:00
---

# Class protos.google.backstory.SecurityResult.IoCStats (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iocstats

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.backstory.SecurityResult.IoCStats (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents an IoCStats.

## Implements

[protos.google.backstory.SecurityResult.IIoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iiocstats)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.backstory.SecurityResult.IIoCStats);

Constructs a new IoCStats.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iiocstats)`   
Properties to set  
  
## Properties 

### benignCount
    
    
    public benignCount: number;

IoCStats benignCount.

### firstLevelSource
    
    
    public firstLevelSource: string;

IoCStats firstLevelSource.

### iocStatsType
    
    
    public iocStatsType: (google.backstory.SecurityResult.IoCStatsType|keyof typeof google.backstory.SecurityResult.IoCStatsType);

IoCStats iocStatsType.

### maliciousCount
    
    
    public maliciousCount: number;

IoCStats maliciousCount.

### quality
    
    
    public quality: (google.backstory.SecurityResult.ProductConfidence|keyof typeof google.backstory.SecurityResult.ProductConfidence);

IoCStats quality.

### responseCount
    
    
    public responseCount: number;

IoCStats responseCount.

### secondLevelSource
    
    
    public secondLevelSource: string;

IoCStats secondLevelSource.

### sourceCount
    
    
    public sourceCount: number;

IoCStats sourceCount.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.backstory.SecurityResult.IIoCStats): google.backstory.SecurityResult.IoCStats;

Creates a new IoCStats instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iiocstats)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[IoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iocstats)` | IoCStats instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.backstory.SecurityResult.IoCStats;

Decodes an IoCStats message from the specified reader or buffer.

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
`[IoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iocstats)` | IoCStats  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.backstory.SecurityResult.IoCStats;

Decodes an IoCStats message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[IoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iocstats)` | IoCStats  
  
### encode(message, writer)
    
    
    public static encode(message: google.backstory.SecurityResult.IIoCStats, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IoCStats message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iiocstats)`   
IoCStats message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.backstory.SecurityResult.IIoCStats, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IoCStats message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iiocstats)`   
IoCStats message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.backstory.SecurityResult.IoCStats;

Creates an IoCStats message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[IoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iocstats)` | IoCStats  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for IoCStats

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

Converts this IoCStats to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.backstory.SecurityResult.IoCStats, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an IoCStats message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IoCStats](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.securityresult.iocstats)`   
IoCStats  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an IoCStats message.

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
