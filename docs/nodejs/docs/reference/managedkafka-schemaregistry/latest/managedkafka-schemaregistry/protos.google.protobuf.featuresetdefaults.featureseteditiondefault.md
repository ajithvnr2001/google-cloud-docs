---
url: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.featureseteditiondefault
title: Class protos.google.protobuf.FeatureSetDefaults.FeatureSetEditionDefault (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:10.489925+00:00
---

# Class protos.google.protobuf.FeatureSetDefaults.FeatureSetEditionDefault (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.featureseteditiondefault

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FeatureSetDefaults.FeatureSetEditionDefault (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a FeatureSetEditionDefault.

## Implements

[protos.google.protobuf.FeatureSetDefaults.IFeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.ifeatureseteditiondefault)

## Package

[@google-cloud/managedkafka-schemaregistry](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.FeatureSetDefaults.IFeatureSetEditionDefault);

Constructs a new FeatureSetEditionDefault.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.ifeatureseteditiondefault)`   
Properties to set  
  
## Properties 

### edition
    
    
    public edition: (google.protobuf.Edition|keyof typeof google.protobuf.Edition);

FeatureSetEditionDefault edition.

### fixedFeatures
    
    
    public fixedFeatures?: (google.protobuf.IFeatureSet|null);

FeatureSetEditionDefault fixedFeatures.

### overridableFeatures
    
    
    public overridableFeatures?: (google.protobuf.IFeatureSet|null);

FeatureSetEditionDefault overridableFeatures.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.FeatureSetDefaults.IFeatureSetEditionDefault): google.protobuf.FeatureSetDefaults.FeatureSetEditionDefault;

Creates a new FeatureSetEditionDefault instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.ifeatureseteditiondefault)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.featureseteditiondefault)` | FeatureSetEditionDefault instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FeatureSetDefaults.FeatureSetEditionDefault;

Decodes a FeatureSetEditionDefault message from the specified reader or buffer.

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
`[FeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.featureseteditiondefault)` | FeatureSetEditionDefault  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FeatureSetDefaults.FeatureSetEditionDefault;

Decodes a FeatureSetEditionDefault message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.featureseteditiondefault)` | FeatureSetEditionDefault  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.FeatureSetDefaults.IFeatureSetEditionDefault, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureSetEditionDefault message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.ifeatureseteditiondefault)`   
FeatureSetEditionDefault message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.FeatureSetDefaults.IFeatureSetEditionDefault, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureSetEditionDefault message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.ifeatureseteditiondefault)`   
FeatureSetEditionDefault message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FeatureSetDefaults.FeatureSetEditionDefault;

Creates a FeatureSetEditionDefault message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.featureseteditiondefault)` | FeatureSetEditionDefault  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FeatureSetEditionDefault

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

Converts this FeatureSetEditionDefault to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FeatureSetDefaults.FeatureSetEditionDefault, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FeatureSetEditionDefault message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FeatureSetEditionDefault](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.protobuf.featuresetdefaults.featureseteditiondefault)`   
FeatureSetEditionDefault  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FeatureSetEditionDefault message.

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
