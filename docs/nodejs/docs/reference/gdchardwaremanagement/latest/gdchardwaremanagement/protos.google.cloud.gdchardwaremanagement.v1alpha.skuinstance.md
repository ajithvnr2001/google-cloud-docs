---
url: https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.skuinstance
title: Class protos.google.cloud.gdchardwaremanagement.v1alpha.SkuInstance (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:00.041477+00:00
---

# Class protos.google.cloud.gdchardwaremanagement.v1alpha.SkuInstance (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.skuinstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gdchardwaremanagement.v1alpha.SkuInstance (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.10.0  0.7.0  0.5.1  0.4.0  0.2.0 

Represents a SkuInstance.

## Implements

[protos.google.cloud.gdchardwaremanagement.v1alpha.ISkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iskuinstance)

## Package

[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gdchardwaremanagement.v1alpha.ISkuInstance);

Constructs a new SkuInstance.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iskuinstance)`   
Properties to set  
  
## Properties 

### billingSku
    
    
    public billingSku: string;

SkuInstance billingSku.

### billingSkuPerVcpu
    
    
    public billingSkuPerVcpu: string;

SkuInstance billingSkuPerVcpu.

### powerSupply
    
    
    public powerSupply: (google.cloud.gdchardwaremanagement.v1alpha.PowerSupply|keyof typeof google.cloud.gdchardwaremanagement.v1alpha.PowerSupply);

SkuInstance powerSupply.

### regionCode
    
    
    public regionCode: string;

SkuInstance regionCode.

### subscriptionDurationMonths
    
    
    public subscriptionDurationMonths: number;

SkuInstance subscriptionDurationMonths.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gdchardwaremanagement.v1alpha.ISkuInstance): google.cloud.gdchardwaremanagement.v1alpha.SkuInstance;

Creates a new SkuInstance instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iskuinstance)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.skuinstance)` | SkuInstance instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gdchardwaremanagement.v1alpha.SkuInstance;

Decodes a SkuInstance message from the specified reader or buffer.

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
`[SkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.skuinstance)` | SkuInstance  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gdchardwaremanagement.v1alpha.SkuInstance;

Decodes a SkuInstance message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.skuinstance)` | SkuInstance  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gdchardwaremanagement.v1alpha.ISkuInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SkuInstance message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iskuinstance)`   
SkuInstance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gdchardwaremanagement.v1alpha.ISkuInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SkuInstance message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iskuinstance)`   
SkuInstance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gdchardwaremanagement.v1alpha.SkuInstance;

Creates a SkuInstance message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.skuinstance)` | SkuInstance  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SkuInstance

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

Converts this SkuInstance to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gdchardwaremanagement.v1alpha.SkuInstance, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SkuInstance message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SkuInstance](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.skuinstance)`   
SkuInstance  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SkuInstance message.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
