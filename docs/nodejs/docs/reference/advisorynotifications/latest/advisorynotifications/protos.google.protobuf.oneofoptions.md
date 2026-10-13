---
url: https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.oneofoptions
title: Class protos.google.protobuf.OneofOptions (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:53.849830+00:00
---

# Class protos.google.protobuf.OneofOptions (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.oneofoptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.OneofOptions (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.1.0  0.2.1  0.1.0 

Represents an OneofOptions.

## Implements

[protos.google.protobuf.IOneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ioneofoptions)

## Package

[@google-cloud/advisorynotifications](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IOneofOptions);

Constructs a new OneofOptions.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ioneofoptions)`   
Properties to set  
  
## Properties 

### features
    
    
    public features?: (google.protobuf.IFeatureSet|null);

OneofOptions features.

### uninterpretedOption
    
    
    public uninterpretedOption: google.protobuf.IUninterpretedOption[];

OneofOptions uninterpretedOption.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IOneofOptions): google.protobuf.OneofOptions;

Creates a new OneofOptions instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ioneofoptions)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.oneofoptions)` | OneofOptions instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.OneofOptions;

Decodes an OneofOptions message from the specified reader or buffer.

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
`[OneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.oneofoptions)` | OneofOptions  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.OneofOptions;

Decodes an OneofOptions message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.oneofoptions)` | OneofOptions  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IOneofOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OneofOptions message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ioneofoptions)`   
OneofOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IOneofOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OneofOptions message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ioneofoptions)`   
OneofOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.OneofOptions;

Creates an OneofOptions message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.oneofoptions)` | OneofOptions  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OneofOptions

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

Converts this OneofOptions to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.OneofOptions, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OneofOptions message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OneofOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.oneofoptions)`   
OneofOptions  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OneofOptions message.

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
