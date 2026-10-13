---
url: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.clientlibrarysettings
title: Class protos.google.api.ClientLibrarySettings (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:06.527585+00:00
---

# Class protos.google.api.ClientLibrarySettings (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.clientlibrarysettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.ClientLibrarySettings (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.1.0  6.5.0  5.2.2  5.1.2  5.0.2  4.3.2  4.2.9 

Represents a ClientLibrarySettings.

## Implements

[protos.google.api.IClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.iclientlibrarysettings)

## Package

[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IClientLibrarySettings);

Constructs a new ClientLibrarySettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.iclientlibrarysettings)`   
Properties to set  
  
## Properties 

### cppSettings
    
    
    public cppSettings?: (google.api.ICppSettings|null);

ClientLibrarySettings cppSettings.

### dotnetSettings
    
    
    public dotnetSettings?: (google.api.IDotnetSettings|null);

ClientLibrarySettings dotnetSettings.

### goSettings
    
    
    public goSettings?: (google.api.IGoSettings|null);

ClientLibrarySettings goSettings.

### javaSettings
    
    
    public javaSettings?: (google.api.IJavaSettings|null);

ClientLibrarySettings javaSettings.

### launchStage
    
    
    public launchStage: (google.api.LaunchStage|keyof typeof google.api.LaunchStage);

ClientLibrarySettings launchStage.

### nodeSettings
    
    
    public nodeSettings?: (google.api.INodeSettings|null);

ClientLibrarySettings nodeSettings.

### phpSettings
    
    
    public phpSettings?: (google.api.IPhpSettings|null);

ClientLibrarySettings phpSettings.

### pythonSettings
    
    
    public pythonSettings?: (google.api.IPythonSettings|null);

ClientLibrarySettings pythonSettings.

### restNumericEnums
    
    
    public restNumericEnums: boolean;

ClientLibrarySettings restNumericEnums.

### rubySettings
    
    
    public rubySettings?: (google.api.IRubySettings|null);

ClientLibrarySettings rubySettings.

### version
    
    
    public version: string;

ClientLibrarySettings version.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IClientLibrarySettings): google.api.ClientLibrarySettings;

Creates a new ClientLibrarySettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.iclientlibrarysettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.clientlibrarysettings)` | ClientLibrarySettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.ClientLibrarySettings;

Decodes a ClientLibrarySettings message from the specified reader or buffer.

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
`[ClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.clientlibrarysettings)` | ClientLibrarySettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.ClientLibrarySettings;

Decodes a ClientLibrarySettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.clientlibrarysettings)` | ClientLibrarySettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IClientLibrarySettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClientLibrarySettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.iclientlibrarysettings)`   
ClientLibrarySettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IClientLibrarySettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClientLibrarySettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.iclientlibrarysettings)`   
ClientLibrarySettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.ClientLibrarySettings;

Creates a ClientLibrarySettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.clientlibrarysettings)` | ClientLibrarySettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ClientLibrarySettings

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

Converts this ClientLibrarySettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.ClientLibrarySettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ClientLibrarySettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ClientLibrarySettings](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.api.clientlibrarysettings)`   
ClientLibrarySettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ClientLibrarySettings message.

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
