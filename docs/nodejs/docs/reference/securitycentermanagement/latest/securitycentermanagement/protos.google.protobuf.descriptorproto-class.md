---
url: https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.descriptorproto-class
title: Class protos.google.protobuf.DescriptorProto (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:11.429640+00:00
---

# Class protos.google.protobuf.DescriptorProto (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.descriptorproto-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.DescriptorProto (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.4.0  0.3.0  0.1.0 

Represents a DescriptorProto.

## Implements

[protos.google.protobuf.IDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.idescriptorproto)

## Package

[@google-cloud/securitycentermanagement](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IDescriptorProto);

Constructs a new DescriptorProto.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.idescriptorproto)`   
Properties to set  
  
## Properties 

### enumType
    
    
    public enumType: google.protobuf.IEnumDescriptorProto[];

DescriptorProto enumType.

### extension
    
    
    public extension: google.protobuf.IFieldDescriptorProto[];

DescriptorProto extension.

### extensionRange
    
    
    public extensionRange: google.protobuf.DescriptorProto.IExtensionRange[];

DescriptorProto extensionRange.

### field
    
    
    public field: google.protobuf.IFieldDescriptorProto[];

DescriptorProto field.

### name
    
    
    public name: string;

DescriptorProto name.

### nestedType
    
    
    public nestedType: google.protobuf.IDescriptorProto[];

DescriptorProto nestedType.

### oneofDecl
    
    
    public oneofDecl: google.protobuf.IOneofDescriptorProto[];

DescriptorProto oneofDecl.

### options
    
    
    public options?: (google.protobuf.IMessageOptions|null);

DescriptorProto options.

### reservedName
    
    
    public reservedName: string[];

DescriptorProto reservedName.

### reservedRange
    
    
    public reservedRange: google.protobuf.DescriptorProto.IReservedRange[];

DescriptorProto reservedRange.

### visibility
    
    
    public visibility: (google.protobuf.SymbolVisibility|keyof typeof google.protobuf.SymbolVisibility);

DescriptorProto visibility.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IDescriptorProto): google.protobuf.DescriptorProto;

Creates a new DescriptorProto instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.idescriptorproto)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.descriptorproto-class)` | DescriptorProto instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.DescriptorProto;

Decodes a DescriptorProto message from the specified reader or buffer.

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
`[DescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.descriptorproto-class)` | DescriptorProto  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.DescriptorProto;

Decodes a DescriptorProto message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.descriptorproto-class)` | DescriptorProto  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IDescriptorProto, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DescriptorProto message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.idescriptorproto)`   
DescriptorProto message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IDescriptorProto, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DescriptorProto message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.idescriptorproto)`   
DescriptorProto message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.DescriptorProto;

Creates a DescriptorProto message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.descriptorproto-class)` | DescriptorProto  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DescriptorProto

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

Converts this DescriptorProto to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.DescriptorProto, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DescriptorProto message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.protobuf.descriptorproto-class)`   
DescriptorProto  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DescriptorProto message.

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
