---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importcryptokeyversionrequest
title: Class protos.google.cloud.kms.v1.ImportCryptoKeyVersionRequest (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:08:53.543989+00:00
---

# Class protos.google.cloud.kms.v1.ImportCryptoKeyVersionRequest (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importcryptokeyversionrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.kms.v1.ImportCryptoKeyVersionRequest (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Represents an ImportCryptoKeyVersionRequest.

## Implements

[protos.google.cloud.kms.v1.IImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportcryptokeyversionrequest)

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.kms.v1.IImportCryptoKeyVersionRequest);

Constructs a new ImportCryptoKeyVersionRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportcryptokeyversionrequest)`   
Properties to set  
  
## Properties 

### algorithm
    
    
    public algorithm: (google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm|keyof typeof google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm);

ImportCryptoKeyVersionRequest algorithm.

### cryptoKeyVersion
    
    
    public cryptoKeyVersion: string;

ImportCryptoKeyVersionRequest cryptoKeyVersion.

### importJob
    
    
    public importJob: string;

ImportCryptoKeyVersionRequest importJob.

### parent
    
    
    public parent: string;

ImportCryptoKeyVersionRequest parent.

### rsaAesWrappedKey
    
    
    public rsaAesWrappedKey?: (Uint8Array|Buffer|string|null);

ImportCryptoKeyVersionRequest rsaAesWrappedKey.

### trustedWrappingEnabled
    
    
    public trustedWrappingEnabled: boolean;

ImportCryptoKeyVersionRequest trustedWrappingEnabled.

### wrappedKey
    
    
    public wrappedKey: (Uint8Array|Buffer|string);

ImportCryptoKeyVersionRequest wrappedKey.

### wrappedKeyMaterial
    
    
    public wrappedKeyMaterial?: "rsaAesWrappedKey";

ImportCryptoKeyVersionRequest wrappedKeyMaterial.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.kms.v1.IImportCryptoKeyVersionRequest): google.cloud.kms.v1.ImportCryptoKeyVersionRequest;

Creates a new ImportCryptoKeyVersionRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportcryptokeyversionrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importcryptokeyversionrequest)` | ImportCryptoKeyVersionRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.kms.v1.ImportCryptoKeyVersionRequest;

Decodes an ImportCryptoKeyVersionRequest message from the specified reader or buffer.

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
`[ImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importcryptokeyversionrequest)` | ImportCryptoKeyVersionRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.kms.v1.ImportCryptoKeyVersionRequest;

Decodes an ImportCryptoKeyVersionRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importcryptokeyversionrequest)` | ImportCryptoKeyVersionRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.kms.v1.IImportCryptoKeyVersionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImportCryptoKeyVersionRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportcryptokeyversionrequest)`   
ImportCryptoKeyVersionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.kms.v1.IImportCryptoKeyVersionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImportCryptoKeyVersionRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportcryptokeyversionrequest)`   
ImportCryptoKeyVersionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.kms.v1.ImportCryptoKeyVersionRequest;

Creates an ImportCryptoKeyVersionRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importcryptokeyversionrequest)` | ImportCryptoKeyVersionRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ImportCryptoKeyVersionRequest

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

Converts this ImportCryptoKeyVersionRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.kms.v1.ImportCryptoKeyVersionRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ImportCryptoKeyVersionRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importcryptokeyversionrequest)`   
ImportCryptoKeyVersionRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ImportCryptoKeyVersionRequest message.

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
