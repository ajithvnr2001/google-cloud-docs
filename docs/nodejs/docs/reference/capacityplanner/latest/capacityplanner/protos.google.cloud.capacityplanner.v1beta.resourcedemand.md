---
url: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.resourcedemand
title: Class protos.google.cloud.capacityplanner.v1beta.ResourceDemand (0.1.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:24.230558+00:00
---

# Class protos.google.cloud.capacityplanner.v1beta.ResourceDemand (0.1.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.resourcedemand

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.capacityplanner.v1beta.ResourceDemand (0.1.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.2 

Represents a ResourceDemand.

## Package

[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.capacityplanner.v1beta.IResourceDemand);

Constructs a new ResourceDemand.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IResourceDemand](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iresourcedemand)`   
Properties to set  
  
## Properties 

### childResourceDemands
    
    
    public childResourceDemands: google.cloud.capacityplanner.v1beta.IChildResourceDemand[];

ResourceDemand childResourceDemands.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

ResourceDemand createTime.

### demandMetadata
    
    
    public demandMetadata?: (google.cloud.capacityplanner.v1beta.IDemandMetadata|null);

ResourceDemand demandMetadata.

### demandValues
    
    
    public demandValues?: (google.cloud.capacityplanner.v1beta.IDemandValues|null);

ResourceDemand demandValues.

### id
    
    
    public id: string;

ResourceDemand id.

### locationId
    
    
    public locationId?: (google.cloud.capacityplanner.v1beta.ILocationIdentifier|null);

ResourceDemand locationId.

### reporter
    
    
    public reporter?: (google.cloud.capacityplanner.v1beta.IUser|null);

ResourceDemand reporter.

### resourceContainer
    
    
    public resourceContainer?: (google.cloud.capacityplanner.v1beta.IResourceContainer|null);

ResourceDemand resourceContainer.

### resourceId
    
    
    public resourceId?: (google.cloud.capacityplanner.v1beta.IResourceIdentifier|null);

ResourceDemand resourceId.

### state
    
    
    public state: (google.cloud.capacityplanner.v1beta.State|keyof typeof google.cloud.capacityplanner.v1beta.State);

ResourceDemand state.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

ResourceDemand updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.capacityplanner.v1beta.IResourceDemand): google.cloud.capacityplanner.v1beta.ResourceDemand;

Creates a new ResourceDemand instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IResourceDemand](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iresourcedemand)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ResourceDemand](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.resourcedemand)` | ResourceDemand instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.capacityplanner.v1beta.ResourceDemand;

Decodes a ResourceDemand message from the specified reader or buffer.

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
`[ResourceDemand](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.resourcedemand)` | ResourceDemand  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.capacityplanner.v1beta.ResourceDemand;

Decodes a ResourceDemand message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ResourceDemand](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.resourcedemand)` | ResourceDemand  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.capacityplanner.v1beta.IResourceDemand, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ResourceDemand message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IResourceDemand](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iresourcedemand)`   
ResourceDemand message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.capacityplanner.v1beta.IResourceDemand, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ResourceDemand message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IResourceDemand](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iresourcedemand)`   
ResourceDemand message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.capacityplanner.v1beta.ResourceDemand;

Creates a ResourceDemand message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ResourceDemand](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.resourcedemand)` | ResourceDemand  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ResourceDemand

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

Converts this ResourceDemand to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.capacityplanner.v1beta.ResourceDemand, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ResourceDemand message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ResourceDemand](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.resourcedemand)`   
ResourceDemand  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ResourceDemand message.

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
