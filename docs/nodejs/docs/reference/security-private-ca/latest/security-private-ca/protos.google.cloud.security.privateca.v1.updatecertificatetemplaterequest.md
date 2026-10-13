---
url: https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.updatecertificatetemplaterequest
title: Class protos.google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:48.369233+00:00
---

# Class protos.google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.updatecertificatetemplaterequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  7.2.0  5.2.0  4.4.0  4.3.0  4.2.0  4.1.2  3.1.0  3.0.0  2.5.0  2.4.1  2.3.7 

Represents an UpdateCertificateTemplateRequest.

## Implements

[protos.google.cloud.security.privateca.v1.IUpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.iupdatecertificatetemplaterequest)

## Package

[@google-cloud/security-private-ca](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.security.privateca.v1.IUpdateCertificateTemplateRequest);

Constructs a new UpdateCertificateTemplateRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.iupdatecertificatetemplaterequest)`   
Properties to set  
  
## Properties 

### certificateTemplate
    
    
    public certificateTemplate?: (google.cloud.security.privateca.v1.ICertificateTemplate|null);

UpdateCertificateTemplateRequest certificateTemplate.

### requestId
    
    
    public requestId: string;

UpdateCertificateTemplateRequest requestId.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateCertificateTemplateRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.security.privateca.v1.IUpdateCertificateTemplateRequest): google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest;

Creates a new UpdateCertificateTemplateRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.iupdatecertificatetemplaterequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.updatecertificatetemplaterequest)` | UpdateCertificateTemplateRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest;

Decodes an UpdateCertificateTemplateRequest message from the specified reader or buffer.

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
`[UpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.updatecertificatetemplaterequest)` | UpdateCertificateTemplateRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest;

Decodes an UpdateCertificateTemplateRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.updatecertificatetemplaterequest)` | UpdateCertificateTemplateRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.security.privateca.v1.IUpdateCertificateTemplateRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateCertificateTemplateRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.iupdatecertificatetemplaterequest)`   
UpdateCertificateTemplateRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.security.privateca.v1.IUpdateCertificateTemplateRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateCertificateTemplateRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.iupdatecertificatetemplaterequest)`   
UpdateCertificateTemplateRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest;

Creates an UpdateCertificateTemplateRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.updatecertificatetemplaterequest)` | UpdateCertificateTemplateRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateCertificateTemplateRequest

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

Converts this UpdateCertificateTemplateRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateCertificateTemplateRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateCertificateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/security-private-ca/protos.google.cloud.security.privateca.v1.updatecertificatetemplaterequest)`   
UpdateCertificateTemplateRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateCertificateTemplateRequest message.

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
