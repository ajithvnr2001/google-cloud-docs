---
url: https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.periodconsumption
title: Class protos.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption (3.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:03.710449+00:00
---

# Class protos.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption (3.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.periodconsumption

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption (3.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.1 (latest)  2.4.0  2.3.0  1.16.0  1.15.0  1.12.0  1.11.0  1.8.0  1.7.0  1.5.0  1.4.0  1.3.0  1.1.0  0.7.1  0.6.1  0.5.0  0.3.2 

Represents a PeriodConsumption.

## Implements

[protos.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.IPeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.iperiodconsumption)

## Package

[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.IPeriodConsumption);

Constructs a new PeriodConsumption.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.iperiodconsumption)`   
Properties to set  
  
## Properties 

### consumed
    
    
    public consumed?: (number|null);

PeriodConsumption consumed.

### consumptionInterval
    
    
    public consumptionInterval?: (google.type.IInterval|null);

PeriodConsumption consumptionInterval.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.IPeriodConsumption): google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption;

Creates a new PeriodConsumption instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.iperiodconsumption)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.periodconsumption)` | PeriodConsumption instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption;

Decodes a PeriodConsumption message from the specified reader or buffer.

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
`[PeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.periodconsumption)` | PeriodConsumption  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption;

Decodes a PeriodConsumption message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.periodconsumption)` | PeriodConsumption  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.IPeriodConsumption, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PeriodConsumption message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.iperiodconsumption)`   
PeriodConsumption message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.IPeriodConsumption, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PeriodConsumption message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.iperiodconsumption)`   
PeriodConsumption message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption;

Creates a PeriodConsumption message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.periodconsumption)` | PeriodConsumption  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PeriodConsumption

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

Converts this PeriodConsumption to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PeriodConsumption message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PeriodConsumption](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1alpha.usageresourceallowancestatus.periodconsumption)`   
PeriodConsumption  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PeriodConsumption message.

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
