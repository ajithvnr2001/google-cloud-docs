---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.food-class
title: Class protos.google.devicesandservices.health.v4.Food (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:16.278332+00:00
---

# Class protos.google.devicesandservices.health.v4.Food (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.food-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.Food (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Food.

## Implements

[protos.google.devicesandservices.health.v4.IFood](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ifood)

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devicesandservices.health.v4.IFood);

Constructs a new Food.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFood](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ifood)`   
Properties to set  
  
## Properties 

### accessLevel
    
    
    public accessLevel: (google.devicesandservices.health.v4.FoodAccessLevel|keyof typeof google.devicesandservices.health.v4.FoodAccessLevel);

Food accessLevel.

### brand
    
    
    public brand: string;

Food brand.

### defaultServing
    
    
    public defaultServing?: (google.devicesandservices.health.v4.Food.IFoodServing|null);

Food defaultServing.

### description
    
    
    public description: string;

Food description.

### displayName
    
    
    public displayName: string;

Food displayName.

### energyAvg
    
    
    public energyAvg?: (google.devicesandservices.health.v4.IEnergyQuantity|null);

Food energyAvg.

### energyFromFat
    
    
    public energyFromFat?: (google.devicesandservices.health.v4.IEnergyQuantity|null);

Food energyFromFat.

### energyMax
    
    
    public energyMax?: (google.devicesandservices.health.v4.IEnergyQuantity|null);

Food energyMax.

### energyMin
    
    
    public energyMin?: (google.devicesandservices.health.v4.IEnergyQuantity|null);

Food energyMin.

### languageCode
    
    
    public languageCode: string;

Food languageCode.

### mealType
    
    
    public mealType: (google.devicesandservices.health.v4.MealType|keyof typeof google.devicesandservices.health.v4.MealType);

Food mealType.

### nutrients
    
    
    public nutrients: google.devicesandservices.health.v4.INutrientQuantity[];

Food nutrients.

### servings
    
    
    public servings: google.devicesandservices.health.v4.Food.IFoodServing[];

Food servings.

### totalCarbohydrate
    
    
    public totalCarbohydrate?: (google.devicesandservices.health.v4.IWeightQuantity|null);

Food totalCarbohydrate.

### totalFat
    
    
    public totalFat?: (google.devicesandservices.health.v4.IWeightQuantity|null);

Food totalFat.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devicesandservices.health.v4.IFood): google.devicesandservices.health.v4.Food;

Creates a new Food instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFood](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ifood)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Food](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.food-class)` | Food instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devicesandservices.health.v4.Food;

Decodes a Food message from the specified reader or buffer.

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
`[Food](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.food-class)` | Food  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devicesandservices.health.v4.Food;

Decodes a Food message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Food](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.food-class)` | Food  
  
### encode(message, writer)
    
    
    public static encode(message: google.devicesandservices.health.v4.IFood, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Food message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFood](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ifood)`   
Food message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devicesandservices.health.v4.IFood, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Food message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFood](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ifood)`   
Food message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devicesandservices.health.v4.Food;

Creates a Food message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Food](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.food-class)` | Food  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Food

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

Converts this Food to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devicesandservices.health.v4.Food, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Food message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Food](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.food-class)`   
Food  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Food message.

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
