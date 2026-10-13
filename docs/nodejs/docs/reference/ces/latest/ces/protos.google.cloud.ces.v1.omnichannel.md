---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.omnichannel
title: Class protos.google.cloud.ces.v1.Omnichannel (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:39.893383+00:00
---

# Class protos.google.cloud.ces.v1.Omnichannel (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.omnichannel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.Omnichannel (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an Omnichannel.

## Implements

[protos.google.cloud.ces.v1.IOmnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iomnichannel)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IOmnichannel);

Constructs a new Omnichannel.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOmnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iomnichannel)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Omnichannel createTime.

### description
    
    
    public description: string;

Omnichannel description.

### displayName
    
    
    public displayName: string;

Omnichannel displayName.

### etag
    
    
    public etag: string;

Omnichannel etag.

### integrationConfig
    
    
    public integrationConfig?: (google.cloud.ces.v1.IOmnichannelIntegrationConfig|null);

Omnichannel integrationConfig.

### name
    
    
    public name: string;

Omnichannel name.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Omnichannel updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IOmnichannel): google.cloud.ces.v1.Omnichannel;

Creates a new Omnichannel instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOmnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iomnichannel)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Omnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.omnichannel)` | Omnichannel instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.Omnichannel;

Decodes an Omnichannel message from the specified reader or buffer.

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
`[Omnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.omnichannel)` | Omnichannel  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.Omnichannel;

Decodes an Omnichannel message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Omnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.omnichannel)` | Omnichannel  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IOmnichannel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Omnichannel message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOmnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iomnichannel)`   
Omnichannel message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IOmnichannel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Omnichannel message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOmnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iomnichannel)`   
Omnichannel message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.Omnichannel;

Creates an Omnichannel message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Omnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.omnichannel)` | Omnichannel  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Omnichannel

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

Converts this Omnichannel to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.Omnichannel, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Omnichannel message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Omnichannel](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.omnichannel)`   
Omnichannel  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Omnichannel message.

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
