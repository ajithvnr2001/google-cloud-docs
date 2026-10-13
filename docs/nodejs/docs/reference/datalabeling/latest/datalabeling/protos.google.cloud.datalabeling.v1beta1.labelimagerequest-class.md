---
url: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labelimagerequest-class
title: Class protos.google.cloud.datalabeling.v1beta1.LabelImageRequest (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:59.969809+00:00
---

# Class protos.google.cloud.datalabeling.v1beta1.LabelImageRequest (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labelimagerequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datalabeling.v1beta1.LabelImageRequest (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.2.2  3.1.1  2.3.0  2.2.7 

Represents a LabelImageRequest.

## Implements

[protos.google.cloud.datalabeling.v1beta1.ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)

## Package

[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datalabeling.v1beta1.ILabelImageRequest);

Constructs a new LabelImageRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)`   
Properties to set  
  
## Properties 

### basicConfig
    
    
    public basicConfig?: (google.cloud.datalabeling.v1beta1.IHumanAnnotationConfig|null);

LabelImageRequest basicConfig.

### boundingPolyConfig
    
    
    public boundingPolyConfig?: (google.cloud.datalabeling.v1beta1.IBoundingPolyConfig|null);

LabelImageRequest boundingPolyConfig.

### feature
    
    
    public feature: (google.cloud.datalabeling.v1beta1.LabelImageRequest.Feature|keyof typeof google.cloud.datalabeling.v1beta1.LabelImageRequest.Feature);

LabelImageRequest feature.

### imageClassificationConfig
    
    
    public imageClassificationConfig?: (google.cloud.datalabeling.v1beta1.IImageClassificationConfig|null);

LabelImageRequest imageClassificationConfig.

### parent
    
    
    public parent: string;

LabelImageRequest parent.

### polylineConfig
    
    
    public polylineConfig?: (google.cloud.datalabeling.v1beta1.IPolylineConfig|null);

LabelImageRequest polylineConfig.

### requestConfig
    
    
    public requestConfig?: ("imageClassificationConfig"|"boundingPolyConfig"|"polylineConfig"|"segmentationConfig");

LabelImageRequest requestConfig.

### segmentationConfig
    
    
    public segmentationConfig?: (google.cloud.datalabeling.v1beta1.ISegmentationConfig|null);

LabelImageRequest segmentationConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datalabeling.v1beta1.ILabelImageRequest): google.cloud.datalabeling.v1beta1.LabelImageRequest;

Creates a new LabelImageRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labelimagerequest-class)` | LabelImageRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datalabeling.v1beta1.LabelImageRequest;

Decodes a LabelImageRequest message from the specified reader or buffer.

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
`[LabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labelimagerequest-class)` | LabelImageRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datalabeling.v1beta1.LabelImageRequest;

Decodes a LabelImageRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labelimagerequest-class)` | LabelImageRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datalabeling.v1beta1.ILabelImageRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LabelImageRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)`   
LabelImageRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datalabeling.v1beta1.ILabelImageRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LabelImageRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)`   
LabelImageRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datalabeling.v1beta1.LabelImageRequest;

Creates a LabelImageRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labelimagerequest-class)` | LabelImageRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LabelImageRequest

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

Converts this LabelImageRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datalabeling.v1beta1.LabelImageRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LabelImageRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labelimagerequest-class)`   
LabelImageRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LabelImageRequest message.

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
