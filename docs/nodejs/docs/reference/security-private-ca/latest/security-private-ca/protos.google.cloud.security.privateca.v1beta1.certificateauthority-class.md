---
url: https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.certificateauthority-class
title: Class protos.google.cloud.security.privateca.v1beta1.CertificateAuthority (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:46.053435+00:00
---

# Class protos.google.cloud.security.privateca.v1beta1.CertificateAuthority (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.certificateauthority-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.security.privateca.v1beta1.CertificateAuthority (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  7.2.0  5.2.0  4.4.0  4.3.0  4.2.0  4.1.2  3.1.0  3.0.0  2.5.0  2.4.1  2.3.7 

Represents a CertificateAuthority.

## Implements

[protos.google.cloud.security.privateca.v1beta1.ICertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icertificateauthority)

## Package

[@google-cloud/security-private-ca](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.security.privateca.v1beta1.ICertificateAuthority);

Constructs a new CertificateAuthority.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icertificateauthority)`   
Properties to set  
  
## Properties 

### accessUrls
    
    
    public accessUrls?: (google.cloud.security.privateca.v1beta1.CertificateAuthority.IAccessUrls|null);

CertificateAuthority accessUrls.

### caCertificateDescriptions
    
    
    public caCertificateDescriptions: google.cloud.security.privateca.v1beta1.ICertificateDescription[];

CertificateAuthority caCertificateDescriptions.

### certificatePolicy
    
    
    public certificatePolicy?: (google.cloud.security.privateca.v1beta1.CertificateAuthority.ICertificateAuthorityPolicy|null);

CertificateAuthority certificatePolicy.

### config
    
    
    public config?: (google.cloud.security.privateca.v1beta1.ICertificateConfig|null);

CertificateAuthority config.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

CertificateAuthority createTime.

### deleteTime
    
    
    public deleteTime?: (google.protobuf.ITimestamp|null);

CertificateAuthority deleteTime.

### gcsBucket
    
    
    public gcsBucket: string;

CertificateAuthority gcsBucket.

### issuingOptions
    
    
    public issuingOptions?: (google.cloud.security.privateca.v1beta1.CertificateAuthority.IIssuingOptions|null);

CertificateAuthority issuingOptions.

### keySpec
    
    
    public keySpec?: (google.cloud.security.privateca.v1beta1.CertificateAuthority.IKeyVersionSpec|null);

CertificateAuthority keySpec.

### labels
    
    
    public labels: { [k: string]: string };

CertificateAuthority labels.

### lifetime
    
    
    public lifetime?: (google.protobuf.IDuration|null);

CertificateAuthority lifetime.

### name
    
    
    public name: string;

CertificateAuthority name.

### pemCaCertificates
    
    
    public pemCaCertificates: string[];

CertificateAuthority pemCaCertificates.

### state
    
    
    public state: (google.cloud.security.privateca.v1beta1.CertificateAuthority.State|keyof typeof google.cloud.security.privateca.v1beta1.CertificateAuthority.State);

CertificateAuthority state.

### subordinateConfig
    
    
    public subordinateConfig?: (google.cloud.security.privateca.v1beta1.ISubordinateConfig|null);

CertificateAuthority subordinateConfig.

### tier
    
    
    public tier: (google.cloud.security.privateca.v1beta1.CertificateAuthority.Tier|keyof typeof google.cloud.security.privateca.v1beta1.CertificateAuthority.Tier);

CertificateAuthority tier.

### type
    
    
    public type: (google.cloud.security.privateca.v1beta1.CertificateAuthority.Type|keyof typeof google.cloud.security.privateca.v1beta1.CertificateAuthority.Type);

CertificateAuthority type.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

CertificateAuthority updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.security.privateca.v1beta1.ICertificateAuthority): google.cloud.security.privateca.v1beta1.CertificateAuthority;

Creates a new CertificateAuthority instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icertificateauthority)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.certificateauthority-class)` | CertificateAuthority instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.security.privateca.v1beta1.CertificateAuthority;

Decodes a CertificateAuthority message from the specified reader or buffer.

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
`[CertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.certificateauthority-class)` | CertificateAuthority  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.security.privateca.v1beta1.CertificateAuthority;

Decodes a CertificateAuthority message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.certificateauthority-class)` | CertificateAuthority  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.security.privateca.v1beta1.ICertificateAuthority, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CertificateAuthority message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icertificateauthority)`   
CertificateAuthority message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.security.privateca.v1beta1.ICertificateAuthority, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CertificateAuthority message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icertificateauthority)`   
CertificateAuthority message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.security.privateca.v1beta1.CertificateAuthority;

Creates a CertificateAuthority message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.certificateauthority-class)` | CertificateAuthority  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CertificateAuthority

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

Converts this CertificateAuthority to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.security.privateca.v1beta1.CertificateAuthority, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CertificateAuthority message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.certificateauthority-class)`   
CertificateAuthority  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CertificateAuthority message.

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
