---
url: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrencerequest
title: Class protos.google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:07.139026+00:00
---

# Class protos.google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrencerequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.5.0  4.4.0  4.2.0  3.7.0  2.5.0  2.2.1  2.1.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.6 

Represents a ValidateAttestationOccurrenceRequest.

## Implements

[protos.google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrencerequest)

## Package

[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceRequest);

Constructs a new ValidateAttestationOccurrenceRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrencerequest)`   
Properties to set  
  
## Properties 

### attestation
    
    
    public attestation?: (grafeas.v1.IAttestationOccurrence|null);

ValidateAttestationOccurrenceRequest attestation.

### attestor
    
    
    public attestor: string;

ValidateAttestationOccurrenceRequest attestor.

### occurrenceNote
    
    
    public occurrenceNote: string;

ValidateAttestationOccurrenceRequest occurrenceNote.

### occurrenceResourceUri
    
    
    public occurrenceResourceUri: string;

ValidateAttestationOccurrenceRequest occurrenceResourceUri.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceRequest): google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceRequest;

Creates a new ValidateAttestationOccurrenceRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrencerequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrencerequest)` | ValidateAttestationOccurrenceRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceRequest;

Decodes a ValidateAttestationOccurrenceRequest message from the specified reader or buffer.

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
`[ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrencerequest)` | ValidateAttestationOccurrenceRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceRequest;

Decodes a ValidateAttestationOccurrenceRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrencerequest)` | ValidateAttestationOccurrenceRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ValidateAttestationOccurrenceRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrencerequest)`   
ValidateAttestationOccurrenceRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ValidateAttestationOccurrenceRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrencerequest)`   
ValidateAttestationOccurrenceRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceRequest;

Creates a ValidateAttestationOccurrenceRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrencerequest)` | ValidateAttestationOccurrenceRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ValidateAttestationOccurrenceRequest

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

Converts this ValidateAttestationOccurrenceRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ValidateAttestationOccurrenceRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrencerequest)`   
ValidateAttestationOccurrenceRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ValidateAttestationOccurrenceRequest message.

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
