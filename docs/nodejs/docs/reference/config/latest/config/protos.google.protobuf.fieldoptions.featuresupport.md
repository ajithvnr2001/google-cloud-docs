---
url: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.featuresupport
title: Class protos.google.protobuf.FieldOptions.FeatureSupport (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:14.589440+00:00
---

# Class protos.google.protobuf.FieldOptions.FeatureSupport (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.featuresupport

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FieldOptions.FeatureSupport (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.14.0  0.12.0  0.7.0  0.5.0  0.2.0  0.1.1 

Represents a FeatureSupport.

## Implements

[protos.google.protobuf.FieldOptions.IFeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.ifeaturesupport)

## Package

[@google-cloud/config](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.FieldOptions.IFeatureSupport);

Constructs a new FeatureSupport.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.ifeaturesupport)`   
Properties to set  
  
## Properties 

### deprecationWarning
    
    
    public deprecationWarning: string;

FeatureSupport deprecationWarning.

### editionDeprecated
    
    
    public editionDeprecated: (google.protobuf.Edition|keyof typeof google.protobuf.Edition);

FeatureSupport editionDeprecated.

### editionIntroduced
    
    
    public editionIntroduced: (google.protobuf.Edition|keyof typeof google.protobuf.Edition);

FeatureSupport editionIntroduced.

### editionRemoved
    
    
    public editionRemoved: (google.protobuf.Edition|keyof typeof google.protobuf.Edition);

FeatureSupport editionRemoved.

### removalError
    
    
    public removalError: string;

FeatureSupport removalError.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.FieldOptions.IFeatureSupport): google.protobuf.FieldOptions.FeatureSupport;

Creates a new FeatureSupport instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.ifeaturesupport)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.featuresupport)` | FeatureSupport instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FieldOptions.FeatureSupport;

Decodes a FeatureSupport message from the specified reader or buffer.

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
`[FeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.featuresupport)` | FeatureSupport  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FieldOptions.FeatureSupport;

Decodes a FeatureSupport message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.featuresupport)` | FeatureSupport  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.FieldOptions.IFeatureSupport, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureSupport message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.ifeaturesupport)`   
FeatureSupport message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.FieldOptions.IFeatureSupport, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureSupport message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.ifeaturesupport)`   
FeatureSupport message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FieldOptions.FeatureSupport;

Creates a FeatureSupport message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.featuresupport)` | FeatureSupport  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FeatureSupport

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

Converts this FeatureSupport to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FieldOptions.FeatureSupport, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FeatureSupport message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FeatureSupport](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.protobuf.fieldoptions.featuresupport)`   
FeatureSupport  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FeatureSupport message.

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
