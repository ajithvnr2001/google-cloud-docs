---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importjob-class
title: Class protos.google.cloud.kms.v1.ImportJob (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:08:53.868124+00:00
---

# Class protos.google.cloud.kms.v1.ImportJob (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importjob-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.kms.v1.ImportJob (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Represents an ImportJob.

## Implements

[protos.google.cloud.kms.v1.IImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportjob)

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.kms.v1.IImportJob);

Constructs a new ImportJob.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportjob)`   
Properties to set  
  
## Properties 

### attestation
    
    
    public attestation?: (google.cloud.kms.v1.IKeyOperationAttestation|null);

ImportJob attestation.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

ImportJob createTime.

### cryptoKeyBackend
    
    
    public cryptoKeyBackend: string;

ImportJob cryptoKeyBackend.

### expireEventTime
    
    
    public expireEventTime?: (google.protobuf.ITimestamp|null);

ImportJob expireEventTime.

### expireTime
    
    
    public expireTime?: (google.protobuf.ITimestamp|null);

ImportJob expireTime.

### generateTime
    
    
    public generateTime?: (google.protobuf.ITimestamp|null);

ImportJob generateTime.

### importMethod
    
    
    public importMethod: (google.cloud.kms.v1.ImportJob.ImportMethod|keyof typeof google.cloud.kms.v1.ImportJob.ImportMethod);

ImportJob importMethod.

### name
    
    
    public name: string;

ImportJob name.

### protectionLevel
    
    
    public protectionLevel: (google.cloud.kms.v1.ProtectionLevel|keyof typeof google.cloud.kms.v1.ProtectionLevel);

ImportJob protectionLevel.

### publicKey
    
    
    public publicKey?: (google.cloud.kms.v1.ImportJob.IWrappingPublicKey|null);

ImportJob publicKey.

### publicKeyFormat
    
    
    public publicKeyFormat: (google.cloud.kms.v1.PublicKey.PublicKeyFormat|keyof typeof google.cloud.kms.v1.PublicKey.PublicKeyFormat);

ImportJob publicKeyFormat.

### state
    
    
    public state: (google.cloud.kms.v1.ImportJob.ImportJobState|keyof typeof google.cloud.kms.v1.ImportJob.ImportJobState);

ImportJob state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.kms.v1.IImportJob): google.cloud.kms.v1.ImportJob;

Creates a new ImportJob instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportjob)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importjob-class)` | ImportJob instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.kms.v1.ImportJob;

Decodes an ImportJob message from the specified reader or buffer.

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
`[ImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importjob-class)` | ImportJob  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.kms.v1.ImportJob;

Decodes an ImportJob message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importjob-class)` | ImportJob  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.kms.v1.IImportJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImportJob message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportjob)`   
ImportJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.kms.v1.IImportJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImportJob message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportjob)`   
ImportJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.kms.v1.ImportJob;

Creates an ImportJob message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importjob-class)` | ImportJob  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ImportJob

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

Converts this ImportJob to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.kms.v1.ImportJob, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ImportJob message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importjob-class)`   
ImportJob  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ImportJob message.

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
