---
url: https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.createcertificateauthorityrequest
title: Class protos.google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:14.334355+00:00
---

# Class protos.google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.createcertificateauthorityrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  7.2.0  5.2.0  4.4.0  4.3.0  4.2.0  4.1.2  3.1.0  3.0.0  2.5.0  2.4.1  2.3.7 

Represents a CreateCertificateAuthorityRequest.

## Implements

[protos.google.cloud.security.privateca.v1beta1.ICreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icreatecertificateauthorityrequest)

## Package

[@google-cloud/security-private-ca](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.security.privateca.v1beta1.ICreateCertificateAuthorityRequest);

Constructs a new CreateCertificateAuthorityRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icreatecertificateauthorityrequest)`   
Properties to set  
  
## Properties 

### certificateAuthority
    
    
    public certificateAuthority?: (google.cloud.security.privateca.v1beta1.ICertificateAuthority|null);

CreateCertificateAuthorityRequest certificateAuthority.

### certificateAuthorityId
    
    
    public certificateAuthorityId: string;

CreateCertificateAuthorityRequest certificateAuthorityId.

### parent
    
    
    public parent: string;

CreateCertificateAuthorityRequest parent.

### requestId
    
    
    public requestId: string;

CreateCertificateAuthorityRequest requestId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.security.privateca.v1beta1.ICreateCertificateAuthorityRequest): google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest;

Creates a new CreateCertificateAuthorityRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icreatecertificateauthorityrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.createcertificateauthorityrequest)` | CreateCertificateAuthorityRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest;

Decodes a CreateCertificateAuthorityRequest message from the specified reader or buffer.

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
`[CreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.createcertificateauthorityrequest)` | CreateCertificateAuthorityRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest;

Decodes a CreateCertificateAuthorityRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.createcertificateauthorityrequest)` | CreateCertificateAuthorityRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.security.privateca.v1beta1.ICreateCertificateAuthorityRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateCertificateAuthorityRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icreatecertificateauthorityrequest)`   
CreateCertificateAuthorityRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.security.privateca.v1beta1.ICreateCertificateAuthorityRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateCertificateAuthorityRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.icreatecertificateauthorityrequest)`   
CreateCertificateAuthorityRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest;

Creates a CreateCertificateAuthorityRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.createcertificateauthorityrequest)` | CreateCertificateAuthorityRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateCertificateAuthorityRequest

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

Converts this CreateCertificateAuthorityRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.security.privateca.v1beta1.CreateCertificateAuthorityRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateCertificateAuthorityRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1beta1.createcertificateauthorityrequest)`   
CreateCertificateAuthorityRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateCertificateAuthorityRequest message.

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
