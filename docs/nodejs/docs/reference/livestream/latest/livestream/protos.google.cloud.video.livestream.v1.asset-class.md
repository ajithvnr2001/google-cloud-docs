---
url: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.asset-class
title: Class protos.google.cloud.video.livestream.v1.Asset (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:08.792694+00:00
---

# Class protos.google.cloud.video.livestream.v1.Asset (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.asset-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.video.livestream.v1.Asset (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.0.2  0.5.1  0.4.1  0.3.4  0.1.0 

Represents an Asset.

## Implements

[protos.google.cloud.video.livestream.v1.IAsset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iasset)

## Package

[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.video.livestream.v1.IAsset);

Constructs a new Asset.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAsset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iasset)`   
Properties to set  
  
## Properties 

### crc32c
    
    
    public crc32c: string;

Asset crc32c.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Asset createTime.

### error
    
    
    public error?: (google.rpc.IStatus|null);

Asset error.

### image
    
    
    public image?: (google.cloud.video.livestream.v1.Asset.IImageAsset|null);

Asset image.

### labels
    
    
    public labels: { [k: string]: string };

Asset labels.

### name
    
    
    public name: string;

Asset name.

### resource
    
    
    public resource?: ("video"|"image");

Asset resource.

### state
    
    
    public state: (google.cloud.video.livestream.v1.Asset.State|keyof typeof google.cloud.video.livestream.v1.Asset.State);

Asset state.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Asset updateTime.

### video
    
    
    public video?: (google.cloud.video.livestream.v1.Asset.IVideoAsset|null);

Asset video.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.video.livestream.v1.IAsset): google.cloud.video.livestream.v1.Asset;

Creates a new Asset instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAsset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iasset)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.asset-class)` | Asset instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.video.livestream.v1.Asset;

Decodes an Asset message from the specified reader or buffer.

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
`[Asset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.asset-class)` | Asset  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.video.livestream.v1.Asset;

Decodes an Asset message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.asset-class)` | Asset  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.video.livestream.v1.IAsset, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Asset message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAsset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iasset)`   
Asset message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.video.livestream.v1.IAsset, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Asset message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAsset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iasset)`   
Asset message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.video.livestream.v1.Asset;

Creates an Asset message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.asset-class)` | Asset  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Asset

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

Converts this Asset to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.video.livestream.v1.Asset, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Asset message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Asset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.asset-class)`   
Asset  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Asset message.

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
