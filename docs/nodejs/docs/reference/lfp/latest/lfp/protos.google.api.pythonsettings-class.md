---
url: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.pythonsettings-class
title: Class protos.google.api.PythonSettings (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:27.615874+00:00
---

# Class protos.google.api.PythonSettings (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.pythonsettings-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.PythonSettings (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.10.0  0.4.1  0.2.0  0.1.0 

Represents a PythonSettings.

## Implements

[protos.google.api.IPythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.ipythonsettings)

## Package

[@google-shopping/lfp](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IPythonSettings);

Constructs a new PythonSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.ipythonsettings)`   
Properties to set  
  
## Properties 

### common
    
    
    public common?: (google.api.ICommonLanguageSettings|null);

PythonSettings common.

### experimentalFeatures
    
    
    public experimentalFeatures?: (google.api.PythonSettings.IExperimentalFeatures|null);

PythonSettings experimentalFeatures.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IPythonSettings): google.api.PythonSettings;

Creates a new PythonSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.ipythonsettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.pythonsettings-class)` | PythonSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.PythonSettings;

Decodes a PythonSettings message from the specified reader or buffer.

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
`[PythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.pythonsettings-class)` | PythonSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.PythonSettings;

Decodes a PythonSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.pythonsettings-class)` | PythonSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IPythonSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PythonSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.ipythonsettings)`   
PythonSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IPythonSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PythonSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.ipythonsettings)`   
PythonSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.PythonSettings;

Creates a PythonSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.pythonsettings-class)` | PythonSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PythonSettings

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

Converts this PythonSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.PythonSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PythonSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PythonSettings](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.api.pythonsettings-class)`   
PythonSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PythonSettings message.

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
