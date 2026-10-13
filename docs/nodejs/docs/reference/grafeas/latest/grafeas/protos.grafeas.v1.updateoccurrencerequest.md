---
url: https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.updateoccurrencerequest
title: Class protos.grafeas.v1.UpdateOccurrenceRequest (7.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:34.815305+00:00
---

# Class protos.grafeas.v1.UpdateOccurrenceRequest (7.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.updateoccurrencerequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.grafeas.v1.UpdateOccurrenceRequest (7.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.0.1 (latest)  6.0.1  5.5.0  4.5.0  4.2.2  4.1.2  3.6.1  3.5.0  3.4.6 

Represents an UpdateOccurrenceRequest.

## Implements

[protos.grafeas.v1.IUpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.iupdateoccurrencerequest)

## Package

[@google-cloud/grafeas](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: grafeas.v1.IUpdateOccurrenceRequest);

Constructs a new UpdateOccurrenceRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.iupdateoccurrencerequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

UpdateOccurrenceRequest name.

### occurrence
    
    
    public occurrence?: (grafeas.v1.IOccurrence|null);

UpdateOccurrenceRequest occurrence.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateOccurrenceRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: grafeas.v1.IUpdateOccurrenceRequest): grafeas.v1.UpdateOccurrenceRequest;

Creates a new UpdateOccurrenceRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.iupdateoccurrencerequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.updateoccurrencerequest)` | UpdateOccurrenceRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): grafeas.v1.UpdateOccurrenceRequest;

Decodes an UpdateOccurrenceRequest message from the specified reader or buffer.

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
`[UpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.updateoccurrencerequest)` | UpdateOccurrenceRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): grafeas.v1.UpdateOccurrenceRequest;

Decodes an UpdateOccurrenceRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.updateoccurrencerequest)` | UpdateOccurrenceRequest  
  
### encode(message, writer)
    
    
    public static encode(message: grafeas.v1.IUpdateOccurrenceRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateOccurrenceRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.iupdateoccurrencerequest)`   
UpdateOccurrenceRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: grafeas.v1.IUpdateOccurrenceRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateOccurrenceRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.iupdateoccurrencerequest)`   
UpdateOccurrenceRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): grafeas.v1.UpdateOccurrenceRequest;

Creates an UpdateOccurrenceRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.updateoccurrencerequest)` | UpdateOccurrenceRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateOccurrenceRequest

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

Converts this UpdateOccurrenceRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: grafeas.v1.UpdateOccurrenceRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateOccurrenceRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.updateoccurrencerequest)`   
UpdateOccurrenceRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateOccurrenceRequest message.

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
