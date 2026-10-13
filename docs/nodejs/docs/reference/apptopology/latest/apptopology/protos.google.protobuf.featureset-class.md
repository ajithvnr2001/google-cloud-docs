---
url: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.featureset-class
title: Class protos.google.protobuf.FeatureSet (0.3.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:01:12.648111+00:00
---

# Class protos.google.protobuf.FeatureSet (0.3.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.featureset-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FeatureSet (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.0 

Represents a FeatureSet.

## Implements

[protos.google.protobuf.IFeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.ifeatureset)

## Package

[@google-cloud/apptopology](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IFeatureSet);

Constructs a new FeatureSet.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.ifeatureset)`   
Properties to set  
  
## Properties 

### defaultSymbolVisibility
    
    
    public defaultSymbolVisibility: (google.protobuf.FeatureSet.VisibilityFeature.DefaultSymbolVisibility|keyof typeof google.protobuf.FeatureSet.VisibilityFeature.DefaultSymbolVisibility);

FeatureSet defaultSymbolVisibility.

### enforceNamingStyle
    
    
    public enforceNamingStyle: (google.protobuf.FeatureSet.EnforceNamingStyle|keyof typeof google.protobuf.FeatureSet.EnforceNamingStyle);

FeatureSet enforceNamingStyle.

### enforceProtoLimits
    
    
    public enforceProtoLimits: (google.protobuf.FeatureSet.ProtoLimitsFeature.EnforceProtoLimits|keyof typeof google.protobuf.FeatureSet.ProtoLimitsFeature.EnforceProtoLimits);

FeatureSet enforceProtoLimits.

### enumType
    
    
    public enumType: (google.protobuf.FeatureSet.EnumType|keyof typeof google.protobuf.FeatureSet.EnumType);

FeatureSet enumType.

### fieldPresence
    
    
    public fieldPresence: (google.protobuf.FeatureSet.FieldPresence|keyof typeof google.protobuf.FeatureSet.FieldPresence);

FeatureSet fieldPresence.

### jsonFormat
    
    
    public jsonFormat: (google.protobuf.FeatureSet.JsonFormat|keyof typeof google.protobuf.FeatureSet.JsonFormat);

FeatureSet jsonFormat.

### messageEncoding
    
    
    public messageEncoding: (google.protobuf.FeatureSet.MessageEncoding|keyof typeof google.protobuf.FeatureSet.MessageEncoding);

FeatureSet messageEncoding.

### repeatedFieldEncoding
    
    
    public repeatedFieldEncoding: (google.protobuf.FeatureSet.RepeatedFieldEncoding|keyof typeof google.protobuf.FeatureSet.RepeatedFieldEncoding);

FeatureSet repeatedFieldEncoding.

### utf8Validation
    
    
    public utf8Validation: (google.protobuf.FeatureSet.Utf8Validation|keyof typeof google.protobuf.FeatureSet.Utf8Validation);

FeatureSet utf8Validation.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IFeatureSet): google.protobuf.FeatureSet;

Creates a new FeatureSet instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.ifeatureset)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.featureset-class)` | FeatureSet instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FeatureSet;

Decodes a FeatureSet message from the specified reader or buffer.

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
`[FeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.featureset-class)` | FeatureSet  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FeatureSet;

Decodes a FeatureSet message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.featureset-class)` | FeatureSet  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IFeatureSet, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureSet message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.ifeatureset)`   
FeatureSet message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IFeatureSet, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureSet message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.ifeatureset)`   
FeatureSet message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FeatureSet;

Creates a FeatureSet message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.featureset-class)` | FeatureSet  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FeatureSet

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

Converts this FeatureSet to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FeatureSet, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FeatureSet message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FeatureSet](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.protobuf.featureset-class)`   
FeatureSet  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FeatureSet message.

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
