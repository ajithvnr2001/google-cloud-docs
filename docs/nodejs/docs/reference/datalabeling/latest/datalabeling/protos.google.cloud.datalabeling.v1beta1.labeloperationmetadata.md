---
url: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata
title: Class protos.google.cloud.datalabeling.v1beta1.LabelOperationMetadata (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:00.251069+00:00
---

# Class protos.google.cloud.datalabeling.v1beta1.LabelOperationMetadata (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datalabeling.v1beta1.LabelOperationMetadata (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.2.2  3.1.1  2.3.0  2.2.7 

Represents a LabelOperationMetadata.

## Implements

[protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)

## Package

[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datalabeling.v1beta1.ILabelOperationMetadata);

Constructs a new LabelOperationMetadata.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

LabelOperationMetadata createTime.

### details
    
    
    public details?: ("imageClassificationDetails"|"imageBoundingBoxDetails"|"imageBoundingPolyDetails"|"imageOrientedBoundingBoxDetails"|"imagePolylineDetails"|"imageSegmentationDetails"|"videoClassificationDetails"|"videoObjectDetectionDetails"|"videoObjectTrackingDetails"|"videoEventDetails"|"textClassificationDetails"|"textEntityExtractionDetails");

LabelOperationMetadata details.

### imageBoundingBoxDetails
    
    
    public imageBoundingBoxDetails?: (google.cloud.datalabeling.v1beta1.ILabelImageBoundingBoxOperationMetadata|null);

LabelOperationMetadata imageBoundingBoxDetails.

### imageBoundingPolyDetails
    
    
    public imageBoundingPolyDetails?: (google.cloud.datalabeling.v1beta1.ILabelImageBoundingPolyOperationMetadata|null);

LabelOperationMetadata imageBoundingPolyDetails.

### imageClassificationDetails
    
    
    public imageClassificationDetails?: (google.cloud.datalabeling.v1beta1.ILabelImageClassificationOperationMetadata|null);

LabelOperationMetadata imageClassificationDetails.

### imageOrientedBoundingBoxDetails
    
    
    public imageOrientedBoundingBoxDetails?: (google.cloud.datalabeling.v1beta1.ILabelImageOrientedBoundingBoxOperationMetadata|null);

LabelOperationMetadata imageOrientedBoundingBoxDetails.

### imagePolylineDetails
    
    
    public imagePolylineDetails?: (google.cloud.datalabeling.v1beta1.ILabelImagePolylineOperationMetadata|null);

LabelOperationMetadata imagePolylineDetails.

### imageSegmentationDetails
    
    
    public imageSegmentationDetails?: (google.cloud.datalabeling.v1beta1.ILabelImageSegmentationOperationMetadata|null);

LabelOperationMetadata imageSegmentationDetails.

### partialFailures
    
    
    public partialFailures: google.rpc.IStatus[];

LabelOperationMetadata partialFailures.

### progressPercent
    
    
    public progressPercent: number;

LabelOperationMetadata progressPercent.

### textClassificationDetails
    
    
    public textClassificationDetails?: (google.cloud.datalabeling.v1beta1.ILabelTextClassificationOperationMetadata|null);

LabelOperationMetadata textClassificationDetails.

### textEntityExtractionDetails
    
    
    public textEntityExtractionDetails?: (google.cloud.datalabeling.v1beta1.ILabelTextEntityExtractionOperationMetadata|null);

LabelOperationMetadata textEntityExtractionDetails.

### videoClassificationDetails
    
    
    public videoClassificationDetails?: (google.cloud.datalabeling.v1beta1.ILabelVideoClassificationOperationMetadata|null);

LabelOperationMetadata videoClassificationDetails.

### videoEventDetails
    
    
    public videoEventDetails?: (google.cloud.datalabeling.v1beta1.ILabelVideoEventOperationMetadata|null);

LabelOperationMetadata videoEventDetails.

### videoObjectDetectionDetails
    
    
    public videoObjectDetectionDetails?: (google.cloud.datalabeling.v1beta1.ILabelVideoObjectDetectionOperationMetadata|null);

LabelOperationMetadata videoObjectDetectionDetails.

### videoObjectTrackingDetails
    
    
    public videoObjectTrackingDetails?: (google.cloud.datalabeling.v1beta1.ILabelVideoObjectTrackingOperationMetadata|null);

LabelOperationMetadata videoObjectTrackingDetails.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datalabeling.v1beta1.ILabelOperationMetadata): google.cloud.datalabeling.v1beta1.LabelOperationMetadata;

Creates a new LabelOperationMetadata instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata)` | LabelOperationMetadata instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datalabeling.v1beta1.LabelOperationMetadata;

Decodes a LabelOperationMetadata message from the specified reader or buffer.

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
`[LabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata)` | LabelOperationMetadata  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datalabeling.v1beta1.LabelOperationMetadata;

Decodes a LabelOperationMetadata message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata)` | LabelOperationMetadata  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datalabeling.v1beta1.ILabelOperationMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LabelOperationMetadata message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)`   
LabelOperationMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datalabeling.v1beta1.ILabelOperationMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LabelOperationMetadata message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)`   
LabelOperationMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datalabeling.v1beta1.LabelOperationMetadata;

Creates a LabelOperationMetadata message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata)` | LabelOperationMetadata  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LabelOperationMetadata

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

Converts this LabelOperationMetadata to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datalabeling.v1beta1.LabelOperationMetadata, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LabelOperationMetadata message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata)`   
LabelOperationMetadata  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LabelOperationMetadata message.

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
