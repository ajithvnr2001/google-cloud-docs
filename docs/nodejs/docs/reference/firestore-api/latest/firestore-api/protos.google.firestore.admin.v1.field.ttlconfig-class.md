---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ttlconfig-class
title: Class protos.google.firestore.admin.v1.Field.TtlConfig (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:34.750557+00:00
---

# Class protos.google.firestore.admin.v1.Field.TtlConfig (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ttlconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.firestore.admin.v1.Field.TtlConfig (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a TtlConfig.

## Implements

[protos.google.firestore.admin.v1.Field.ITtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ittlconfig)

## Package

[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.firestore.admin.v1.Field.ITtlConfig);

Constructs a new TtlConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ittlconfig)`   
Properties to set  
  
## Properties 

### expirationOffset
    
    
    public expirationOffset?: (google.protobuf.IDuration|null);

TtlConfig expirationOffset.

### state
    
    
    public state: (google.firestore.admin.v1.Field.TtlConfig.State|keyof typeof google.firestore.admin.v1.Field.TtlConfig.State);

TtlConfig state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.firestore.admin.v1.Field.ITtlConfig): google.firestore.admin.v1.Field.TtlConfig;

Creates a new TtlConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ittlconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[TtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ttlconfig-class)` | TtlConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.firestore.admin.v1.Field.TtlConfig;

Decodes a TtlConfig message from the specified reader or buffer.

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
`[TtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ttlconfig-class)` | TtlConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.firestore.admin.v1.Field.TtlConfig;

Decodes a TtlConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[TtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ttlconfig-class)` | TtlConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.firestore.admin.v1.Field.ITtlConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TtlConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ittlconfig)`   
TtlConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.firestore.admin.v1.Field.ITtlConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TtlConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ittlconfig)`   
TtlConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.firestore.admin.v1.Field.TtlConfig;

Creates a TtlConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[TtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ttlconfig-class)` | TtlConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for TtlConfig

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

Converts this TtlConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.firestore.admin.v1.Field.TtlConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a TtlConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[TtlConfig](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field.ttlconfig-class)`   
TtlConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a TtlConfig message.

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

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
