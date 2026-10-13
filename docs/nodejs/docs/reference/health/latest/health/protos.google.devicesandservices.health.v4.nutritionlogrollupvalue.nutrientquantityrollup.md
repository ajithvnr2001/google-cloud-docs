---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.nutrientquantityrollup
title: Class protos.google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:24.027846+00:00
---

# Class protos.google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.nutrientquantityrollup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a NutrientQuantityRollup.

## Implements

[protos.google.devicesandservices.health.v4.NutritionLogRollupValue.INutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.inutrientquantityrollup)

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devicesandservices.health.v4.NutritionLogRollupValue.INutrientQuantityRollup);

Constructs a new NutrientQuantityRollup.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.inutrientquantityrollup)`   
Properties to set  
  
## Properties 

### nutrient
    
    
    public nutrient: (google.devicesandservices.health.v4.Nutrient|keyof typeof google.devicesandservices.health.v4.Nutrient);

NutrientQuantityRollup nutrient.

### quantity
    
    
    public quantity?: (google.devicesandservices.health.v4.NutritionLogRollupValue.IWeightQuantityRollup|null);

NutrientQuantityRollup quantity.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devicesandservices.health.v4.NutritionLogRollupValue.INutrientQuantityRollup): google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup;

Creates a new NutrientQuantityRollup instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.inutrientquantityrollup)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[NutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.nutrientquantityrollup)` | NutrientQuantityRollup instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup;

Decodes a NutrientQuantityRollup message from the specified reader or buffer.

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
`[NutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.nutrientquantityrollup)` | NutrientQuantityRollup  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup;

Decodes a NutrientQuantityRollup message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[NutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.nutrientquantityrollup)` | NutrientQuantityRollup  
  
### encode(message, writer)
    
    
    public static encode(message: google.devicesandservices.health.v4.NutritionLogRollupValue.INutrientQuantityRollup, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NutrientQuantityRollup message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.inutrientquantityrollup)`   
NutrientQuantityRollup message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devicesandservices.health.v4.NutritionLogRollupValue.INutrientQuantityRollup, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NutrientQuantityRollup message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.inutrientquantityrollup)`   
NutrientQuantityRollup message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup;

Creates a NutrientQuantityRollup message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[NutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.nutrientquantityrollup)` | NutrientQuantityRollup  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for NutrientQuantityRollup

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

Converts this NutrientQuantityRollup to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a NutrientQuantityRollup message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[NutrientQuantityRollup](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.nutritionlogrollupvalue.nutrientquantityrollup)`   
NutrientQuantityRollup  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a NutrientQuantityRollup message.

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
