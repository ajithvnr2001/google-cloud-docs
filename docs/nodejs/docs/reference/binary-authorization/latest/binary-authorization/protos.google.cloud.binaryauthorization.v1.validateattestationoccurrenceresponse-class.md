---
url: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrenceresponse-class
title: Class protos.google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:07.248781+00:00
---

# Class protos.google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrenceresponse-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.5.0  4.4.0  4.2.0  3.7.0  2.5.0  2.2.1  2.1.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.6 

Represents a ValidateAttestationOccurrenceResponse.

## Implements

[protos.google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrenceresponse)

## Package

[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceResponse);

Constructs a new ValidateAttestationOccurrenceResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrenceresponse)`   
Properties to set  
  
## Properties 

### denialReason
    
    
    public denialReason: string;

ValidateAttestationOccurrenceResponse denialReason.

### result
    
    
    public result: (google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse.Result|keyof typeof google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse.Result);

ValidateAttestationOccurrenceResponse result.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceResponse): google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse;

Creates a new ValidateAttestationOccurrenceResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrenceresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrenceresponse-class)` | ValidateAttestationOccurrenceResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse;

Decodes a ValidateAttestationOccurrenceResponse message from the specified reader or buffer.

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
`[ValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrenceresponse-class)` | ValidateAttestationOccurrenceResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse;

Decodes a ValidateAttestationOccurrenceResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrenceresponse-class)` | ValidateAttestationOccurrenceResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ValidateAttestationOccurrenceResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrenceresponse)`   
ValidateAttestationOccurrenceResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ValidateAttestationOccurrenceResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrenceresponse)`   
ValidateAttestationOccurrenceResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse;

Creates a ValidateAttestationOccurrenceResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrenceresponse-class)` | ValidateAttestationOccurrenceResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ValidateAttestationOccurrenceResponse

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

Converts this ValidateAttestationOccurrenceResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ValidateAttestationOccurrenceResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrenceresponse-class)`   
ValidateAttestationOccurrenceResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ValidateAttestationOccurrenceResponse message.

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
