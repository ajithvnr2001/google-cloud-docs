---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.interpolationboostspec-class
title: Class protos.google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:21.875687+00:00
---

# Class protos.google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.interpolationboostspec-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents an InterpolationBoostSpec.

## Implements

[protos.google.cloud.discoveryengine.v1.Control.BoostAction.IInterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.iinterpolationboostspec)

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.discoveryengine.v1.Control.BoostAction.IInterpolationBoostSpec);

Constructs a new InterpolationBoostSpec.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.iinterpolationboostspec)`   
Properties to set  
  
## Properties 

### attributeType
    
    
    public attributeType: (google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec.AttributeType|keyof typeof google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec.AttributeType);

InterpolationBoostSpec attributeType.

### controlPoints
    
    
    public controlPoints: google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec.IControlPoint[];

InterpolationBoostSpec controlPoints.

### fieldName
    
    
    public fieldName: string;

InterpolationBoostSpec fieldName.

### interpolationType
    
    
    public interpolationType: (google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec.InterpolationType|keyof typeof google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec.InterpolationType);

InterpolationBoostSpec interpolationType.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.discoveryengine.v1.Control.BoostAction.IInterpolationBoostSpec): google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec;

Creates a new InterpolationBoostSpec instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.iinterpolationboostspec)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[InterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.interpolationboostspec-class)` | InterpolationBoostSpec instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec;

Decodes an InterpolationBoostSpec message from the specified reader or buffer.

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
`[InterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.interpolationboostspec-class)` | InterpolationBoostSpec  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec;

Decodes an InterpolationBoostSpec message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[InterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.interpolationboostspec-class)` | InterpolationBoostSpec  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.discoveryengine.v1.Control.BoostAction.IInterpolationBoostSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InterpolationBoostSpec message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.iinterpolationboostspec)`   
InterpolationBoostSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.discoveryengine.v1.Control.BoostAction.IInterpolationBoostSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InterpolationBoostSpec message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.iinterpolationboostspec)`   
InterpolationBoostSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec;

Creates an InterpolationBoostSpec message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[InterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.interpolationboostspec-class)` | InterpolationBoostSpec  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for InterpolationBoostSpec

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

Converts this InterpolationBoostSpec to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an InterpolationBoostSpec message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[InterpolationBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.control.boostaction.interpolationboostspec-class)`   
InterpolationBoostSpec  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an InterpolationBoostSpec message.

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
