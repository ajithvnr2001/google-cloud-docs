---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.sdkharnesscontainerimage
title: Class protos.google.dataflow.v1beta3.SdkHarnessContainerImage (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:09.947025+00:00
---

# Class protos.google.dataflow.v1beta3.SdkHarnessContainerImage (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.sdkharnesscontainerimage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.dataflow.v1beta3.SdkHarnessContainerImage (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.0.2  2.1.2  2.0.1  1.2.0  1.1.0  1.0.2 

Represents a SdkHarnessContainerImage.

## Implements

[protos.google.dataflow.v1beta3.ISdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isdkharnesscontainerimage)

## Package

[@google-cloud/dataflow](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.dataflow.v1beta3.ISdkHarnessContainerImage);

Constructs a new SdkHarnessContainerImage.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isdkharnesscontainerimage)`   
Properties to set  
  
## Properties 

### capabilities
    
    
    public capabilities: string[];

SdkHarnessContainerImage capabilities.

### containerImage
    
    
    public containerImage: string;

SdkHarnessContainerImage containerImage.

### environmentId
    
    
    public environmentId: string;

SdkHarnessContainerImage environmentId.

### useSingleCorePerContainer
    
    
    public useSingleCorePerContainer: boolean;

SdkHarnessContainerImage useSingleCorePerContainer.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.dataflow.v1beta3.ISdkHarnessContainerImage): google.dataflow.v1beta3.SdkHarnessContainerImage;

Creates a new SdkHarnessContainerImage instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isdkharnesscontainerimage)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.sdkharnesscontainerimage)` | SdkHarnessContainerImage instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.dataflow.v1beta3.SdkHarnessContainerImage;

Decodes a SdkHarnessContainerImage message from the specified reader or buffer.

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
`[SdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.sdkharnesscontainerimage)` | SdkHarnessContainerImage  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.dataflow.v1beta3.SdkHarnessContainerImage;

Decodes a SdkHarnessContainerImage message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.sdkharnesscontainerimage)` | SdkHarnessContainerImage  
  
### encode(message, writer)
    
    
    public static encode(message: google.dataflow.v1beta3.ISdkHarnessContainerImage, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SdkHarnessContainerImage message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isdkharnesscontainerimage)`   
SdkHarnessContainerImage message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.dataflow.v1beta3.ISdkHarnessContainerImage, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SdkHarnessContainerImage message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isdkharnesscontainerimage)`   
SdkHarnessContainerImage message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.dataflow.v1beta3.SdkHarnessContainerImage;

Creates a SdkHarnessContainerImage message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.sdkharnesscontainerimage)` | SdkHarnessContainerImage  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SdkHarnessContainerImage

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

Converts this SdkHarnessContainerImage to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.dataflow.v1beta3.SdkHarnessContainerImage, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SdkHarnessContainerImage message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SdkHarnessContainerImage](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.sdkharnesscontainerimage)`   
SdkHarnessContainerImage  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SdkHarnessContainerImage message.

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
