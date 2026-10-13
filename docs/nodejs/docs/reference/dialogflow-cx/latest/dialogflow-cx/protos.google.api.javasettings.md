---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.javasettings
title: Class protos.google.api.JavaSettings (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:13.443229+00:00
---

# Class protos.google.api.JavaSettings (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.javasettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.JavaSettings (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents a JavaSettings.

## Implements

[protos.google.api.IJavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.ijavasettings)

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IJavaSettings);

Constructs a new JavaSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.ijavasettings)`   
Properties to set  
  
## Properties 

### common
    
    
    public common?: (google.api.ICommonLanguageSettings|null);

JavaSettings common.

### libraryPackage
    
    
    public libraryPackage: string;

JavaSettings libraryPackage.

### serviceClassNames
    
    
    public serviceClassNames: { [k: string]: string };

JavaSettings serviceClassNames.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IJavaSettings): google.api.JavaSettings;

Creates a new JavaSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.ijavasettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[JavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.javasettings)` | JavaSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.JavaSettings;

Decodes a JavaSettings message from the specified reader or buffer.

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
`[JavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.javasettings)` | JavaSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.JavaSettings;

Decodes a JavaSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[JavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.javasettings)` | JavaSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IJavaSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified JavaSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.ijavasettings)`   
JavaSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IJavaSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified JavaSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.ijavasettings)`   
JavaSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.JavaSettings;

Creates a JavaSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[JavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.javasettings)` | JavaSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for JavaSettings

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

Converts this JavaSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.JavaSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a JavaSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[JavaSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.api.javasettings)`   
JavaSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a JavaSettings message.

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
