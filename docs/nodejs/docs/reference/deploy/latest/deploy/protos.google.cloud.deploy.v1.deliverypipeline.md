---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deliverypipeline
title: Class protos.google.cloud.deploy.v1.DeliveryPipeline (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:01:35.508214+00:00
---

# Class protos.google.cloud.deploy.v1.DeliveryPipeline (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deliverypipeline

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.deploy.v1.DeliveryPipeline (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

Represents a DeliveryPipeline.

## Implements

[protos.google.cloud.deploy.v1.IDeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideliverypipeline)

## Package

[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.deploy.v1.IDeliveryPipeline);

Constructs a new DeliveryPipeline.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideliverypipeline)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

DeliveryPipeline annotations.

### condition
    
    
    public condition?: (google.cloud.deploy.v1.IPipelineCondition|null);

DeliveryPipeline condition.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

DeliveryPipeline createTime.

### description
    
    
    public description: string;

DeliveryPipeline description.

### etag
    
    
    public etag: string;

DeliveryPipeline etag.

### labels
    
    
    public labels: { [k: string]: string };

DeliveryPipeline labels.

### name
    
    
    public name: string;

DeliveryPipeline name.

### pipeline
    
    
    public pipeline?: "serialPipeline";

DeliveryPipeline pipeline.

### serialPipeline
    
    
    public serialPipeline?: (google.cloud.deploy.v1.ISerialPipeline|null);

DeliveryPipeline serialPipeline.

### suspended
    
    
    public suspended: boolean;

DeliveryPipeline suspended.

### uid
    
    
    public uid: string;

DeliveryPipeline uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

DeliveryPipeline updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.deploy.v1.IDeliveryPipeline): google.cloud.deploy.v1.DeliveryPipeline;

Creates a new DeliveryPipeline instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideliverypipeline)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deliverypipeline)` | DeliveryPipeline instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.deploy.v1.DeliveryPipeline;

Decodes a DeliveryPipeline message from the specified reader or buffer.

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
`[DeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deliverypipeline)` | DeliveryPipeline  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.deploy.v1.DeliveryPipeline;

Decodes a DeliveryPipeline message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deliverypipeline)` | DeliveryPipeline  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.deploy.v1.IDeliveryPipeline, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeliveryPipeline message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideliverypipeline)`   
DeliveryPipeline message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.deploy.v1.IDeliveryPipeline, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeliveryPipeline message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideliverypipeline)`   
DeliveryPipeline message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.deploy.v1.DeliveryPipeline;

Creates a DeliveryPipeline message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deliverypipeline)` | DeliveryPipeline  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeliveryPipeline

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

Converts this DeliveryPipeline to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.deploy.v1.DeliveryPipeline, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeliveryPipeline message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeliveryPipeline](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deliverypipeline)`   
DeliveryPipeline  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeliveryPipeline message.

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
