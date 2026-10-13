---
url: https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.fielddescriptorproto-class
title: Class protos.google.protobuf.FieldDescriptorProto (0.3.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:28.806166+00:00
---

# Class protos.google.protobuf.FieldDescriptorProto (0.3.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.fielddescriptorproto-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FieldDescriptorProto (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a FieldDescriptorProto.

## Implements

[protos.google.protobuf.IFieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.ifielddescriptorproto)

## Package

[@google-cloud/ftp](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IFieldDescriptorProto);

Constructs a new FieldDescriptorProto.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.ifielddescriptorproto)`   
Properties to set  
  
## Properties 

### defaultValue
    
    
    public defaultValue: string;

FieldDescriptorProto defaultValue.

### extendee
    
    
    public extendee: string;

FieldDescriptorProto extendee.

### jsonName
    
    
    public jsonName: string;

FieldDescriptorProto jsonName.

### label
    
    
    public label: (google.protobuf.FieldDescriptorProto.Label|keyof typeof google.protobuf.FieldDescriptorProto.Label);

FieldDescriptorProto label.

### name
    
    
    public name: string;

FieldDescriptorProto name.

### number
    
    
    public number: number;

FieldDescriptorProto number.

### oneofIndex
    
    
    public oneofIndex: number;

FieldDescriptorProto oneofIndex.

### options
    
    
    public options?: (google.protobuf.IFieldOptions|null);

FieldDescriptorProto options.

### proto3Optional
    
    
    public proto3Optional: boolean;

FieldDescriptorProto proto3Optional.

### type
    
    
    public type: (google.protobuf.FieldDescriptorProto.Type|keyof typeof google.protobuf.FieldDescriptorProto.Type);

FieldDescriptorProto type.

### typeName
    
    
    public typeName: string;

FieldDescriptorProto typeName.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IFieldDescriptorProto): google.protobuf.FieldDescriptorProto;

Creates a new FieldDescriptorProto instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.ifielddescriptorproto)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.fielddescriptorproto-class)` | FieldDescriptorProto instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FieldDescriptorProto;

Decodes a FieldDescriptorProto message from the specified reader or buffer.

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
`[FieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.fielddescriptorproto-class)` | FieldDescriptorProto  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FieldDescriptorProto;

Decodes a FieldDescriptorProto message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.fielddescriptorproto-class)` | FieldDescriptorProto  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IFieldDescriptorProto, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldDescriptorProto message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.ifielddescriptorproto)`   
FieldDescriptorProto message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IFieldDescriptorProto, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldDescriptorProto message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.ifielddescriptorproto)`   
FieldDescriptorProto message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FieldDescriptorProto;

Creates a FieldDescriptorProto message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.fielddescriptorproto-class)` | FieldDescriptorProto  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FieldDescriptorProto

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

Converts this FieldDescriptorProto to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FieldDescriptorProto, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FieldDescriptorProto message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FieldDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.protobuf.fielddescriptorproto-class)`   
FieldDescriptorProto  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FieldDescriptorProto message.

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
