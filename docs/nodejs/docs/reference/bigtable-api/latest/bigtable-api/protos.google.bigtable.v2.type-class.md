---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.type-class
title: Class protos.google.bigtable.v2.Type (0.9.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:22.200700+00:00
---

# Class protos.google.bigtable.v2.Type (0.9.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.type-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.bigtable.v2.Type (0.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.0 (latest)  0.8.0  0.2.0 

Represents a Type.

## Implements

[protos.google.bigtable.v2.IType](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.itype)

## Package

[@google-cloud/bigtable-api](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.bigtable.v2.IType);

Constructs a new Type.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IType](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.itype)`   
Properties to set  
  
## Properties 

### aggregateType
    
    
    public aggregateType?: (google.bigtable.v2.Type.IAggregate|null);

Type aggregateType.

### arrayType
    
    
    public arrayType?: (google.bigtable.v2.Type.IArray|null);

Type arrayType.

### boolType
    
    
    public boolType?: (google.bigtable.v2.Type.IBool|null);

Type boolType.

### bytesType
    
    
    public bytesType?: (google.bigtable.v2.Type.IBytes|null);

Type bytesType.

### dateType
    
    
    public dateType?: (google.bigtable.v2.Type.IDate|null);

Type dateType.

### enumType
    
    
    public enumType?: (google.bigtable.v2.Type.IEnum|null);

Type enumType.

### float32Type
    
    
    public float32Type?: (google.bigtable.v2.Type.IFloat32|null);

Type float32Type.

### float64Type
    
    
    public float64Type?: (google.bigtable.v2.Type.IFloat64|null);

Type float64Type.

### int64Type
    
    
    public int64Type?: (google.bigtable.v2.Type.IInt64|null);

Type int64Type.

### kind
    
    
    public kind?: ("bytesType"|"stringType"|"int64Type"|"float32Type"|"float64Type"|"boolType"|"timestampType"|"dateType"|"aggregateType"|"structType"|"arrayType"|"mapType"|"protoType"|"enumType");

Type kind.

### mapType
    
    
    public mapType?: (google.bigtable.v2.Type.IMap|null);

Type mapType.

### protoType
    
    
    public protoType?: (google.bigtable.v2.Type.IProto|null);

Type protoType.

### stringType
    
    
    public stringType?: (google.bigtable.v2.Type.IString|null);

Type stringType.

### structType
    
    
    public structType?: (google.bigtable.v2.Type.IStruct|null);

Type structType.

### timestampType
    
    
    public timestampType?: (google.bigtable.v2.Type.ITimestamp|null);

Type timestampType.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.bigtable.v2.IType): google.bigtable.v2.Type;

Creates a new Type instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IType](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.itype)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Type](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.type-class)` | Type instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.bigtable.v2.Type;

Decodes a Type message from the specified reader or buffer.

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
`[Type](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.type-class)` | Type  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.bigtable.v2.Type;

Decodes a Type message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Type](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.type-class)` | Type  
  
### encode(message, writer)
    
    
    public static encode(message: google.bigtable.v2.IType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Type message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IType](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.itype)`   
Type message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.bigtable.v2.IType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Type message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IType](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.itype)`   
Type message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.bigtable.v2.Type;

Creates a Type message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Type](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.type-class)` | Type  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Type

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

Converts this Type to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.bigtable.v2.Type, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Type message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Type](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.v2.type-class)`   
Type  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Type message.

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
