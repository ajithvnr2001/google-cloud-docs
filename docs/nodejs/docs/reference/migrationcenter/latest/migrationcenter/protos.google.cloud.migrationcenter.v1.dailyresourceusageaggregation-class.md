---
url: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.dailyresourceusageaggregation-class
title: Class protos.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:27:48.788210+00:00
---

# Class protos.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.dailyresourceusageaggregation-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0 

Represents a DailyResourceUsageAggregation.

## Implements

[protos.google.cloud.migrationcenter.v1.IDailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.idailyresourceusageaggregation)

## Package

[@google-cloud/migrationcenter](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.migrationcenter.v1.IDailyResourceUsageAggregation);

Constructs a new DailyResourceUsageAggregation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.idailyresourceusageaggregation)`   
Properties to set  
  
## Properties 

### cpu
    
    
    public cpu?: (google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.ICPU|null);

DailyResourceUsageAggregation cpu.

### date
    
    
    public date?: (google.type.IDate|null);

DailyResourceUsageAggregation date.

### disk
    
    
    public disk?: (google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.IDisk|null);

DailyResourceUsageAggregation disk.

### memory
    
    
    public memory?: (google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.IMemory|null);

DailyResourceUsageAggregation memory.

### network
    
    
    public network?: (google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.INetwork|null);

DailyResourceUsageAggregation network.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.migrationcenter.v1.IDailyResourceUsageAggregation): google.cloud.migrationcenter.v1.DailyResourceUsageAggregation;

Creates a new DailyResourceUsageAggregation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.idailyresourceusageaggregation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.dailyresourceusageaggregation-class)` | DailyResourceUsageAggregation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.migrationcenter.v1.DailyResourceUsageAggregation;

Decodes a DailyResourceUsageAggregation message from the specified reader or buffer.

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
`[DailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.dailyresourceusageaggregation-class)` | DailyResourceUsageAggregation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.migrationcenter.v1.DailyResourceUsageAggregation;

Decodes a DailyResourceUsageAggregation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.dailyresourceusageaggregation-class)` | DailyResourceUsageAggregation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.migrationcenter.v1.IDailyResourceUsageAggregation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DailyResourceUsageAggregation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.idailyresourceusageaggregation)`   
DailyResourceUsageAggregation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.migrationcenter.v1.IDailyResourceUsageAggregation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DailyResourceUsageAggregation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.idailyresourceusageaggregation)`   
DailyResourceUsageAggregation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.migrationcenter.v1.DailyResourceUsageAggregation;

Creates a DailyResourceUsageAggregation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.dailyresourceusageaggregation-class)` | DailyResourceUsageAggregation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DailyResourceUsageAggregation

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

Converts this DailyResourceUsageAggregation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.migrationcenter.v1.DailyResourceUsageAggregation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DailyResourceUsageAggregation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DailyResourceUsageAggregation](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.dailyresourceusageaggregation-class)`   
DailyResourceUsageAggregation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DailyResourceUsageAggregation message.

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
