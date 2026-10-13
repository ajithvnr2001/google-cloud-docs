---
url: https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.pluscode
title: Class protos.google.maps.addressvalidation.v1.PlusCode (4.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:46.568756+00:00
---

# Class protos.google.maps.addressvalidation.v1.PlusCode (4.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.pluscode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.addressvalidation.v1.PlusCode (4.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.1 (latest)  1.0.1  0.1.0 

Represents a PlusCode.

## Implements

[protos.google.maps.addressvalidation.v1.IPlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.ipluscode)

## Package

[@googlemaps/addressvalidation](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.addressvalidation.v1.IPlusCode);

Constructs a new PlusCode.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.ipluscode)`   
Properties to set  
  
## Properties 

### compoundCode
    
    
    public compoundCode: string;

PlusCode compoundCode.

### globalCode
    
    
    public globalCode: string;

PlusCode globalCode.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.addressvalidation.v1.IPlusCode): google.maps.addressvalidation.v1.PlusCode;

Creates a new PlusCode instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.ipluscode)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.pluscode)` | PlusCode instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.addressvalidation.v1.PlusCode;

Decodes a PlusCode message from the specified reader or buffer.

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
`[PlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.pluscode)` | PlusCode  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.addressvalidation.v1.PlusCode;

Decodes a PlusCode message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.pluscode)` | PlusCode  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.addressvalidation.v1.IPlusCode, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PlusCode message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.ipluscode)`   
PlusCode message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.addressvalidation.v1.IPlusCode, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PlusCode message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.ipluscode)`   
PlusCode message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.addressvalidation.v1.PlusCode;

Creates a PlusCode message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.pluscode)` | PlusCode  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PlusCode

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

Converts this PlusCode to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.addressvalidation.v1.PlusCode, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PlusCode message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PlusCode](https://docs.cloud.google.com/nodejs/docs/reference/addressvalidation/latest/addressvalidation/protos.google.maps.addressvalidation.v1.pluscode)`   
PlusCode  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PlusCode message.

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
