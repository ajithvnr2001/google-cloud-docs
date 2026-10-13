---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.fieldinfo-class
title: Class protos.google.api.FieldInfo (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:45.093703+00:00
---

# Class protos.google.api.FieldInfo (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.fieldinfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.FieldInfo (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a FieldInfo.

## Implements

[protos.google.api.IFieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.ifieldinfo)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IFieldInfo);

Constructs a new FieldInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.ifieldinfo)`   
Properties to set  
  
## Properties 

### format
    
    
    public format: (google.api.FieldInfo.Format|keyof typeof google.api.FieldInfo.Format);

FieldInfo format.

### referencedTypes
    
    
    public referencedTypes: google.api.ITypeReference[];

FieldInfo referencedTypes.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IFieldInfo): google.api.FieldInfo;

Creates a new FieldInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.ifieldinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.fieldinfo-class)` | FieldInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.FieldInfo;

Decodes a FieldInfo message from the specified reader or buffer.

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
`[FieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.fieldinfo-class)` | FieldInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.FieldInfo;

Decodes a FieldInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.fieldinfo-class)` | FieldInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IFieldInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.ifieldinfo)`   
FieldInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IFieldInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.ifieldinfo)`   
FieldInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.FieldInfo;

Creates a FieldInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.fieldinfo-class)` | FieldInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FieldInfo

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

Converts this FieldInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.FieldInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FieldInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FieldInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.api.fieldinfo-class)`   
FieldInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FieldInfo message.

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
