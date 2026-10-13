---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class
title: Class protos.google.cloud.kms.v1.CryptoKeyVersion (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:08:46.395967+00:00
---

# Class protos.google.cloud.kms.v1.CryptoKeyVersion (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.kms.v1.CryptoKeyVersion (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Represents a CryptoKeyVersion.

## Implements

[protos.google.cloud.kms.v1.ICryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icryptokeyversion)

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.kms.v1.ICryptoKeyVersion);

Constructs a new CryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icryptokeyversion)`   
Properties to set  
  
## Properties 

### algorithm
    
    
    public algorithm: (google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm|keyof typeof google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm);

CryptoKeyVersion algorithm.

### attestation
    
    
    public attestation?: (google.cloud.kms.v1.IKeyOperationAttestation|null);

CryptoKeyVersion attestation.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

CryptoKeyVersion createTime.

### destroyEventTime
    
    
    public destroyEventTime?: (google.protobuf.ITimestamp|null);

CryptoKeyVersion destroyEventTime.

### destroyTime
    
    
    public destroyTime?: (google.protobuf.ITimestamp|null);

CryptoKeyVersion destroyTime.

### externalDestructionFailureReason
    
    
    public externalDestructionFailureReason: string;

CryptoKeyVersion externalDestructionFailureReason.

### externalProtectionLevelOptions
    
    
    public externalProtectionLevelOptions?: (google.cloud.kms.v1.IExternalProtectionLevelOptions|null);

CryptoKeyVersion externalProtectionLevelOptions.

### generateTime
    
    
    public generateTime?: (google.protobuf.ITimestamp|null);

CryptoKeyVersion generateTime.

### generationFailureReason
    
    
    public generationFailureReason: string;

CryptoKeyVersion generationFailureReason.

### hsmTrusted
    
    
    public hsmTrusted: boolean;

CryptoKeyVersion hsmTrusted.

### importFailureReason
    
    
    public importFailureReason: string;

CryptoKeyVersion importFailureReason.

### importJob
    
    
    public importJob: string;

CryptoKeyVersion importJob.

### importTime
    
    
    public importTime?: (google.protobuf.ITimestamp|null);

CryptoKeyVersion importTime.

### name
    
    
    public name: string;

CryptoKeyVersion name.

### protectionLevel
    
    
    public protectionLevel: (google.cloud.kms.v1.ProtectionLevel|keyof typeof google.cloud.kms.v1.ProtectionLevel);

CryptoKeyVersion protectionLevel.

### reimportEligible
    
    
    public reimportEligible: boolean;

CryptoKeyVersion reimportEligible.

### state
    
    
    public state: (google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState|keyof typeof google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState);

CryptoKeyVersion state.

### trustedWrappingEnabled
    
    
    public trustedWrappingEnabled: boolean;

CryptoKeyVersion trustedWrappingEnabled.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.kms.v1.ICryptoKeyVersion): google.cloud.kms.v1.CryptoKeyVersion;

Creates a new CryptoKeyVersion instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icryptokeyversion)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)` | CryptoKeyVersion instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.kms.v1.CryptoKeyVersion;

Decodes a CryptoKeyVersion message from the specified reader or buffer.

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
`[CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)` | CryptoKeyVersion  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.kms.v1.CryptoKeyVersion;

Decodes a CryptoKeyVersion message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)` | CryptoKeyVersion  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.kms.v1.ICryptoKeyVersion, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CryptoKeyVersion message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icryptokeyversion)`   
CryptoKeyVersion message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.kms.v1.ICryptoKeyVersion, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CryptoKeyVersion message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icryptokeyversion)`   
CryptoKeyVersion message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.kms.v1.CryptoKeyVersion;

Creates a CryptoKeyVersion message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)` | CryptoKeyVersion  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CryptoKeyVersion

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

Converts this CryptoKeyVersion to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.kms.v1.CryptoKeyVersion, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CryptoKeyVersion message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)`   
CryptoKeyVersion  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CryptoKeyVersion message.

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
