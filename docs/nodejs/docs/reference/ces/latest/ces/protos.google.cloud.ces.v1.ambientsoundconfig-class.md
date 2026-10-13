---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ambientsoundconfig-class
title: Class protos.google.cloud.ces.v1.AmbientSoundConfig (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:05:53.721149+00:00
---

# Class protos.google.cloud.ces.v1.AmbientSoundConfig (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ambientsoundconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.AmbientSoundConfig (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an AmbientSoundConfig.

## Implements

[protos.google.cloud.ces.v1.IAmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iambientsoundconfig)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IAmbientSoundConfig);

Constructs a new AmbientSoundConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iambientsoundconfig)`   
Properties to set  
  
## Properties 

### gcsUri
    
    
    public gcsUri?: (string|null);

AmbientSoundConfig gcsUri.

### prebuiltAmbientNoise
    
    
    public prebuiltAmbientNoise?: (google.cloud.ces.v1.AmbientSoundConfig.PrebuiltAmbientNoise|keyof typeof google.cloud.ces.v1.AmbientSoundConfig.PrebuiltAmbientNoise|null);

AmbientSoundConfig prebuiltAmbientNoise.

### prebuiltAmbientSound
    
    
    public prebuiltAmbientSound?: (string|null);

AmbientSoundConfig prebuiltAmbientSound.

### source
    
    
    public source?: ("prebuiltAmbientNoise"|"gcsUri"|"prebuiltAmbientSound");

AmbientSoundConfig source.

### volumeGainDb
    
    
    public volumeGainDb: number;

AmbientSoundConfig volumeGainDb.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IAmbientSoundConfig): google.cloud.ces.v1.AmbientSoundConfig;

Creates a new AmbientSoundConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iambientsoundconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ambientsoundconfig-class)` | AmbientSoundConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.AmbientSoundConfig;

Decodes an AmbientSoundConfig message from the specified reader or buffer.

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
`[AmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ambientsoundconfig-class)` | AmbientSoundConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.AmbientSoundConfig;

Decodes an AmbientSoundConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ambientsoundconfig-class)` | AmbientSoundConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IAmbientSoundConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AmbientSoundConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iambientsoundconfig)`   
AmbientSoundConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IAmbientSoundConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AmbientSoundConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iambientsoundconfig)`   
AmbientSoundConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.AmbientSoundConfig;

Creates an AmbientSoundConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ambientsoundconfig-class)` | AmbientSoundConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AmbientSoundConfig

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

Converts this AmbientSoundConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.AmbientSoundConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AmbientSoundConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AmbientSoundConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ambientsoundconfig-class)`   
AmbientSoundConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AmbientSoundConfig message.

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
