---
url: https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.entityannotation
title: Class protos.google.cloud.vision.v1p2beta1.EntityAnnotation (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:39.645771+00:00
---

# Class protos.google.cloud.vision.v1p2beta1.EntityAnnotation (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.entityannotation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.vision.v1p2beta1.EntityAnnotation (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.3.5  5.2.0  4.3.2  4.2.1  4.0.3  3.1.3  3.0.1  2.4.2  2.3.8 

Represents an EntityAnnotation.

## Implements

[protos.google.cloud.vision.v1p2beta1.IEntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.ientityannotation)

## Package

[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.vision.v1p2beta1.IEntityAnnotation);

Constructs a new EntityAnnotation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.ientityannotation)`   
Properties to set  
  
## Properties 

### boundingPoly
    
    
    public boundingPoly?: (google.cloud.vision.v1p2beta1.IBoundingPoly|null);

EntityAnnotation boundingPoly.

### confidence
    
    
    public confidence: number;

EntityAnnotation confidence.

### description
    
    
    public description: string;

EntityAnnotation description.

### locale
    
    
    public locale: string;

EntityAnnotation locale.

### locations
    
    
    public locations: google.cloud.vision.v1p2beta1.ILocationInfo[];

EntityAnnotation locations.

### mid
    
    
    public mid: string;

EntityAnnotation mid.

### properties
    
    
    public properties: google.cloud.vision.v1p2beta1.IProperty[];

EntityAnnotation properties.

### score
    
    
    public score: number;

EntityAnnotation score.

### topicality
    
    
    public topicality: number;

EntityAnnotation topicality.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.vision.v1p2beta1.IEntityAnnotation): google.cloud.vision.v1p2beta1.EntityAnnotation;

Creates a new EntityAnnotation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.ientityannotation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.entityannotation)` | EntityAnnotation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.vision.v1p2beta1.EntityAnnotation;

Decodes an EntityAnnotation message from the specified reader or buffer.

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
`[EntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.entityannotation)` | EntityAnnotation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.vision.v1p2beta1.EntityAnnotation;

Decodes an EntityAnnotation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.entityannotation)` | EntityAnnotation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.vision.v1p2beta1.IEntityAnnotation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EntityAnnotation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.ientityannotation)`   
EntityAnnotation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.vision.v1p2beta1.IEntityAnnotation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EntityAnnotation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.ientityannotation)`   
EntityAnnotation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.vision.v1p2beta1.EntityAnnotation;

Creates an EntityAnnotation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.entityannotation)` | EntityAnnotation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EntityAnnotation

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

Converts this EntityAnnotation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.vision.v1p2beta1.EntityAnnotation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EntityAnnotation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EntityAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p2beta1.entityannotation)`   
EntityAnnotation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EntityAnnotation message.

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
