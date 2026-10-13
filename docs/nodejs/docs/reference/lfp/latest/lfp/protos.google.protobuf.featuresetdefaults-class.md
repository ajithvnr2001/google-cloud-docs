---
url: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.featuresetdefaults-class
title: Class protos.google.protobuf.FeatureSetDefaults (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:30.692634+00:00
---

# Class protos.google.protobuf.FeatureSetDefaults (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.featuresetdefaults-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FeatureSetDefaults (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.10.0  0.4.1  0.2.0  0.1.0 

Represents a FeatureSetDefaults.

## Implements

[protos.google.protobuf.IFeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.ifeaturesetdefaults)

## Package

[@google-shopping/lfp](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IFeatureSetDefaults);

Constructs a new FeatureSetDefaults.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.ifeaturesetdefaults)`   
Properties to set  
  
## Properties 

### defaults
    
    
    public defaults: google.protobuf.FeatureSetDefaults.IFeatureSetEditionDefault[];

FeatureSetDefaults defaults.

### maximumEdition
    
    
    public maximumEdition: (google.protobuf.Edition|keyof typeof google.protobuf.Edition);

FeatureSetDefaults maximumEdition.

### minimumEdition
    
    
    public minimumEdition: (google.protobuf.Edition|keyof typeof google.protobuf.Edition);

FeatureSetDefaults minimumEdition.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IFeatureSetDefaults): google.protobuf.FeatureSetDefaults;

Creates a new FeatureSetDefaults instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.ifeaturesetdefaults)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.featuresetdefaults-class)` | FeatureSetDefaults instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FeatureSetDefaults;

Decodes a FeatureSetDefaults message from the specified reader or buffer.

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
`[FeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.featuresetdefaults-class)` | FeatureSetDefaults  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FeatureSetDefaults;

Decodes a FeatureSetDefaults message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.featuresetdefaults-class)` | FeatureSetDefaults  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IFeatureSetDefaults, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureSetDefaults message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.ifeaturesetdefaults)`   
FeatureSetDefaults message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IFeatureSetDefaults, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureSetDefaults message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.ifeaturesetdefaults)`   
FeatureSetDefaults message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FeatureSetDefaults;

Creates a FeatureSetDefaults message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.featuresetdefaults-class)` | FeatureSetDefaults  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FeatureSetDefaults

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

Converts this FeatureSetDefaults to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FeatureSetDefaults, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FeatureSetDefaults message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FeatureSetDefaults](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.featuresetdefaults-class)`   
FeatureSetDefaults  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FeatureSetDefaults message.

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
