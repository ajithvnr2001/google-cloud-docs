---
url: https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.getcertificatemaprequest
title: Class protos.google.cloud.certificatemanager.v1.GetCertificateMapRequest (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:15.219296+00:00
---

# Class protos.google.cloud.certificatemanager.v1.GetCertificateMapRequest (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.getcertificatemaprequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.certificatemanager.v1.GetCertificateMapRequest (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.3  0.7.2  0.6.2  0.5.0  0.1.0 

Represents a GetCertificateMapRequest.

## Implements

[protos.google.cloud.certificatemanager.v1.IGetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificatemaprequest)

## Package

[@google-cloud/certificate-manager](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.certificatemanager.v1.IGetCertificateMapRequest);

Constructs a new GetCertificateMapRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificatemaprequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

GetCertificateMapRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.certificatemanager.v1.IGetCertificateMapRequest): google.cloud.certificatemanager.v1.GetCertificateMapRequest;

Creates a new GetCertificateMapRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificatemaprequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.getcertificatemaprequest)` | GetCertificateMapRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.certificatemanager.v1.GetCertificateMapRequest;

Decodes a GetCertificateMapRequest message from the specified reader or buffer.

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
`[GetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.getcertificatemaprequest)` | GetCertificateMapRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.certificatemanager.v1.GetCertificateMapRequest;

Decodes a GetCertificateMapRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.getcertificatemaprequest)` | GetCertificateMapRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.certificatemanager.v1.IGetCertificateMapRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetCertificateMapRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificatemaprequest)`   
GetCertificateMapRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.certificatemanager.v1.IGetCertificateMapRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetCertificateMapRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificatemaprequest)`   
GetCertificateMapRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.certificatemanager.v1.GetCertificateMapRequest;

Creates a GetCertificateMapRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.getcertificatemaprequest)` | GetCertificateMapRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GetCertificateMapRequest

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

Converts this GetCertificateMapRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.certificatemanager.v1.GetCertificateMapRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GetCertificateMapRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.getcertificatemaprequest)`   
GetCertificateMapRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GetCertificateMapRequest message.

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
