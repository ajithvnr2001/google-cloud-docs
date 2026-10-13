---
url: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.extensionrangeoptions-class
title: Class protos.google.protobuf.ExtensionRangeOptions (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:37.675389+00:00
---

# Class protos.google.protobuf.ExtensionRangeOptions (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.extensionrangeoptions-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.ExtensionRangeOptions (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an ExtensionRangeOptions.

## Implements

[protos.google.protobuf.IExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.iextensionrangeoptions)

## Package

[@google-cloud/connectors](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IExtensionRangeOptions);

Constructs a new ExtensionRangeOptions.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.iextensionrangeoptions)`   
Properties to set  
  
## Properties 

### declaration
    
    
    public declaration: google.protobuf.ExtensionRangeOptions.IDeclaration[];

ExtensionRangeOptions declaration.

### features
    
    
    public features?: (google.protobuf.IFeatureSet|null);

ExtensionRangeOptions features.

### uninterpretedOption
    
    
    public uninterpretedOption: google.protobuf.IUninterpretedOption[];

ExtensionRangeOptions uninterpretedOption.

### verification
    
    
    public verification: (google.protobuf.ExtensionRangeOptions.VerificationState|keyof typeof google.protobuf.ExtensionRangeOptions.VerificationState);

ExtensionRangeOptions verification.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IExtensionRangeOptions): google.protobuf.ExtensionRangeOptions;

Creates a new ExtensionRangeOptions instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.iextensionrangeoptions)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.extensionrangeoptions-class)` | ExtensionRangeOptions instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.ExtensionRangeOptions;

Decodes an ExtensionRangeOptions message from the specified reader or buffer.

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
`[ExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.extensionrangeoptions-class)` | ExtensionRangeOptions  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.ExtensionRangeOptions;

Decodes an ExtensionRangeOptions message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.extensionrangeoptions-class)` | ExtensionRangeOptions  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IExtensionRangeOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ExtensionRangeOptions message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.iextensionrangeoptions)`   
ExtensionRangeOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IExtensionRangeOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ExtensionRangeOptions message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.iextensionrangeoptions)`   
ExtensionRangeOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.ExtensionRangeOptions;

Creates an ExtensionRangeOptions message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.extensionrangeoptions-class)` | ExtensionRangeOptions  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ExtensionRangeOptions

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

Converts this ExtensionRangeOptions to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.ExtensionRangeOptions, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ExtensionRangeOptions message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ExtensionRangeOptions](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.protobuf.extensionrangeoptions-class)`   
ExtensionRangeOptions  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ExtensionRangeOptions message.

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
