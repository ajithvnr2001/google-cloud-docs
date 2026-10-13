---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.configfile-class
title: Class protos.google.api.servicemanagement.v1.ConfigFile (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:00.129439+00:00
---

# Class protos.google.api.servicemanagement.v1.ConfigFile (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.configfile-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.servicemanagement.v1.ConfigFile (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  2.2.0  1.2.2  1.1.3  0.4.0  0.3.1  0.2.6 

Represents a ConfigFile.

## Implements

[protos.google.api.servicemanagement.v1.IConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.iconfigfile)

## Package

[@google-cloud/service-management](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.servicemanagement.v1.IConfigFile);

Constructs a new ConfigFile.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.iconfigfile)`   
Properties to set  
  
## Properties 

### fileContents
    
    
    public fileContents: (Uint8Array|Buffer|string);

ConfigFile fileContents.

### filePath
    
    
    public filePath: string;

ConfigFile filePath.

### fileType
    
    
    public fileType: (google.api.servicemanagement.v1.ConfigFile.FileType|keyof typeof google.api.servicemanagement.v1.ConfigFile.FileType);

ConfigFile fileType.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.servicemanagement.v1.IConfigFile): google.api.servicemanagement.v1.ConfigFile;

Creates a new ConfigFile instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.iconfigfile)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.configfile-class)` | ConfigFile instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.servicemanagement.v1.ConfigFile;

Decodes a ConfigFile message from the specified reader or buffer.

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
`[ConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.configfile-class)` | ConfigFile  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.servicemanagement.v1.ConfigFile;

Decodes a ConfigFile message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.configfile-class)` | ConfigFile  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.servicemanagement.v1.IConfigFile, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConfigFile message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.iconfigfile)`   
ConfigFile message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.servicemanagement.v1.IConfigFile, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConfigFile message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.iconfigfile)`   
ConfigFile message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.servicemanagement.v1.ConfigFile;

Creates a ConfigFile message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.configfile-class)` | ConfigFile  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ConfigFile

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

Converts this ConfigFile to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.servicemanagement.v1.ConfigFile, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ConfigFile message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ConfigFile](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.servicemanagement.v1.configfile-class)`   
ConfigFile  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ConfigFile message.

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
