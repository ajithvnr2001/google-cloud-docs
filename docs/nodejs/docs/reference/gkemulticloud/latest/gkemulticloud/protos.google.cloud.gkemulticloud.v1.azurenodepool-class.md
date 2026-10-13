---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurenodepool-class
title: Class protos.google.cloud.gkemulticloud.v1.AzureNodePool (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:46.521504+00:00
---

# Class protos.google.cloud.gkemulticloud.v1.AzureNodePool (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurenodepool-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkemulticloud.v1.AzureNodePool (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

Represents an AzureNodePool.

## Implements

[protos.google.cloud.gkemulticloud.v1.IAzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurenodepool)

## Package

[@google-cloud/gkemulticloud](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkemulticloud.v1.IAzureNodePool);

Constructs a new AzureNodePool.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurenodepool)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

AzureNodePool annotations.

### autoscaling
    
    
    public autoscaling?: (google.cloud.gkemulticloud.v1.IAzureNodePoolAutoscaling|null);

AzureNodePool autoscaling.

### azureAvailabilityZone
    
    
    public azureAvailabilityZone: string;

AzureNodePool azureAvailabilityZone.

### config
    
    
    public config?: (google.cloud.gkemulticloud.v1.IAzureNodeConfig|null);

AzureNodePool config.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AzureNodePool createTime.

### errors
    
    
    public errors: google.cloud.gkemulticloud.v1.IAzureNodePoolError[];

AzureNodePool errors.

### etag
    
    
    public etag: string;

AzureNodePool etag.

### management
    
    
    public management?: (google.cloud.gkemulticloud.v1.IAzureNodeManagement|null);

AzureNodePool management.

### maxPodsConstraint
    
    
    public maxPodsConstraint?: (google.cloud.gkemulticloud.v1.IMaxPodsConstraint|null);

AzureNodePool maxPodsConstraint.

### name
    
    
    public name: string;

AzureNodePool name.

### reconciling
    
    
    public reconciling: boolean;

AzureNodePool reconciling.

### state
    
    
    public state: (google.cloud.gkemulticloud.v1.AzureNodePool.State|keyof typeof google.cloud.gkemulticloud.v1.AzureNodePool.State);

AzureNodePool state.

### subnetId
    
    
    public subnetId: string;

AzureNodePool subnetId.

### uid
    
    
    public uid: string;

AzureNodePool uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

AzureNodePool updateTime.

### version
    
    
    public version: string;

AzureNodePool version.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkemulticloud.v1.IAzureNodePool): google.cloud.gkemulticloud.v1.AzureNodePool;

Creates a new AzureNodePool instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurenodepool)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurenodepool-class)` | AzureNodePool instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkemulticloud.v1.AzureNodePool;

Decodes an AzureNodePool message from the specified reader or buffer.

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
`[AzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurenodepool-class)` | AzureNodePool  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkemulticloud.v1.AzureNodePool;

Decodes an AzureNodePool message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurenodepool-class)` | AzureNodePool  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkemulticloud.v1.IAzureNodePool, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AzureNodePool message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurenodepool)`   
AzureNodePool message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkemulticloud.v1.IAzureNodePool, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AzureNodePool message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurenodepool)`   
AzureNodePool message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkemulticloud.v1.AzureNodePool;

Creates an AzureNodePool message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurenodepool-class)` | AzureNodePool  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AzureNodePool

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

Converts this AzureNodePool to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkemulticloud.v1.AzureNodePool, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AzureNodePool message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AzureNodePool](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurenodepool-class)`   
AzureNodePool  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AzureNodePool message.

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
