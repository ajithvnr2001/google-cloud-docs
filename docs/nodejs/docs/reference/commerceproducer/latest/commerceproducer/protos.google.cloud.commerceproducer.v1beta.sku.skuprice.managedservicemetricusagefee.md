---
url: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.managedservicemetricusagefee
title: Class protos.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ManagedServiceMetricUsageFee (0.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:32:04.871916+00:00
---

# Class protos.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ManagedServiceMetricUsageFee (0.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.managedservicemetricusagefee

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ManagedServiceMetricUsageFee (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a ManagedServiceMetricUsageFee.

## Implements

[protos.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.IManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.imanagedservicemetricusagefee)

## Package

[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.commerceproducer.v1beta.Sku.SkuPrice.IManagedServiceMetricUsageFee);

Constructs a new ManagedServiceMetricUsageFee.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.imanagedservicemetricusagefee)`   
Properties to set  
  
## Properties 

### canonicalMetric
    
    
    public canonicalMetric: string;

ManagedServiceMetricUsageFee canonicalMetric.

### priceStructure
    
    
    public priceStructure?: "tieredPrice";

ManagedServiceMetricUsageFee priceStructure.

### tieredPrice
    
    
    public tieredPrice?: (google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ITieredPrice|null);

ManagedServiceMetricUsageFee tieredPrice.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.commerceproducer.v1beta.Sku.SkuPrice.IManagedServiceMetricUsageFee): google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ManagedServiceMetricUsageFee;

Creates a new ManagedServiceMetricUsageFee instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.imanagedservicemetricusagefee)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.managedservicemetricusagefee)` | ManagedServiceMetricUsageFee instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ManagedServiceMetricUsageFee;

Decodes a ManagedServiceMetricUsageFee message from the specified reader or buffer.

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
`[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.managedservicemetricusagefee)` | ManagedServiceMetricUsageFee  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ManagedServiceMetricUsageFee;

Decodes a ManagedServiceMetricUsageFee message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.managedservicemetricusagefee)` | ManagedServiceMetricUsageFee  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.commerceproducer.v1beta.Sku.SkuPrice.IManagedServiceMetricUsageFee, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ManagedServiceMetricUsageFee message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.imanagedservicemetricusagefee)`   
ManagedServiceMetricUsageFee message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.commerceproducer.v1beta.Sku.SkuPrice.IManagedServiceMetricUsageFee, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ManagedServiceMetricUsageFee message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.imanagedservicemetricusagefee)`   
ManagedServiceMetricUsageFee message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ManagedServiceMetricUsageFee;

Creates a ManagedServiceMetricUsageFee message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.managedservicemetricusagefee)` | ManagedServiceMetricUsageFee  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ManagedServiceMetricUsageFee

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

Converts this ManagedServiceMetricUsageFee to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ManagedServiceMetricUsageFee, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ManagedServiceMetricUsageFee message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku.skuprice.managedservicemetricusagefee)`   
ManagedServiceMetricUsageFee  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ManagedServiceMetricUsageFee message.

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

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
