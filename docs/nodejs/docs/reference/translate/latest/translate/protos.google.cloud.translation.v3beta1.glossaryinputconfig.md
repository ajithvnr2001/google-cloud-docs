---
url: https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.glossaryinputconfig
title: Class protos.google.cloud.translation.v3beta1.GlossaryInputConfig (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:10.206443+00:00
---

# Class protos.google.cloud.translation.v3beta1.GlossaryInputConfig (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.glossaryinputconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.translation.v3beta1.GlossaryInputConfig (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.0.1  9.3.0  8.5.0  8.0.3  7.2.1  7.1.1  7.0.4  6.3.1  6.2.7  6.1.0 

Represents a GlossaryInputConfig.

## Implements

[protos.google.cloud.translation.v3beta1.IGlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.iglossaryinputconfig)

## Package

[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.translation.v3beta1.IGlossaryInputConfig);

Constructs a new GlossaryInputConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.iglossaryinputconfig)`   
Properties to set  
  
## Properties 

### gcsSource
    
    
    public gcsSource?: (google.cloud.translation.v3beta1.IGcsSource|null);

GlossaryInputConfig gcsSource.

### source
    
    
    public source?: "gcsSource";

GlossaryInputConfig source.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.translation.v3beta1.IGlossaryInputConfig): google.cloud.translation.v3beta1.GlossaryInputConfig;

Creates a new GlossaryInputConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.iglossaryinputconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.glossaryinputconfig)` | GlossaryInputConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.translation.v3beta1.GlossaryInputConfig;

Decodes a GlossaryInputConfig message from the specified reader or buffer.

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
`[GlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.glossaryinputconfig)` | GlossaryInputConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.translation.v3beta1.GlossaryInputConfig;

Decodes a GlossaryInputConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.glossaryinputconfig)` | GlossaryInputConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.translation.v3beta1.IGlossaryInputConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GlossaryInputConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.iglossaryinputconfig)`   
GlossaryInputConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.translation.v3beta1.IGlossaryInputConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GlossaryInputConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.iglossaryinputconfig)`   
GlossaryInputConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.translation.v3beta1.GlossaryInputConfig;

Creates a GlossaryInputConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.glossaryinputconfig)` | GlossaryInputConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GlossaryInputConfig

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

Converts this GlossaryInputConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.translation.v3beta1.GlossaryInputConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GlossaryInputConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GlossaryInputConfig](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3beta1.glossaryinputconfig)`   
GlossaryInputConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GlossaryInputConfig message.

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
