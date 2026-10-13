---
url: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.encryptioninfo-class
title: Class protos.google.spanner.admin.database.v1.EncryptionInfo (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:51.719799+00:00
---

# Class protos.google.spanner.admin.database.v1.EncryptionInfo (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.encryptioninfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.spanner.admin.database.v1.EncryptionInfo (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an EncryptionInfo.

## Implements

[protos.google.spanner.admin.database.v1.IEncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.iencryptioninfo)

## Package

[@google-cloud/spanner-api](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.spanner.admin.database.v1.IEncryptionInfo);

Constructs a new EncryptionInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.iencryptioninfo)`   
Properties to set  
  
## Properties 

### encryptionStatus
    
    
    public encryptionStatus?: (google.rpc.IStatus|null);

EncryptionInfo encryptionStatus.

### encryptionType
    
    
    public encryptionType: (google.spanner.admin.database.v1.EncryptionInfo.Type|keyof typeof google.spanner.admin.database.v1.EncryptionInfo.Type);

EncryptionInfo encryptionType.

### kmsKeyVersion
    
    
    public kmsKeyVersion: string;

EncryptionInfo kmsKeyVersion.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.spanner.admin.database.v1.IEncryptionInfo): google.spanner.admin.database.v1.EncryptionInfo;

Creates a new EncryptionInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.iencryptioninfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.encryptioninfo-class)` | EncryptionInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.spanner.admin.database.v1.EncryptionInfo;

Decodes an EncryptionInfo message from the specified reader or buffer.

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
`[EncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.encryptioninfo-class)` | EncryptionInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.spanner.admin.database.v1.EncryptionInfo;

Decodes an EncryptionInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.encryptioninfo-class)` | EncryptionInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.spanner.admin.database.v1.IEncryptionInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EncryptionInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.iencryptioninfo)`   
EncryptionInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.spanner.admin.database.v1.IEncryptionInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EncryptionInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.iencryptioninfo)`   
EncryptionInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.spanner.admin.database.v1.EncryptionInfo;

Creates an EncryptionInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.encryptioninfo-class)` | EncryptionInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EncryptionInfo

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

Converts this EncryptionInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.spanner.admin.database.v1.EncryptionInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EncryptionInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EncryptionInfo](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.encryptioninfo-class)`   
EncryptionInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EncryptionInfo message.

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
