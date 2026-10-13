---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.containerinfo
title: Class protos.google.appengine.v1.ContainerInfo (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:30.853300+00:00
---

# Class protos.google.appengine.v1.ContainerInfo (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.containerinfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.ContainerInfo (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents a ContainerInfo.

## Implements

[protos.google.appengine.v1.IContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icontainerinfo)

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.appengine.v1.IContainerInfo);

Constructs a new ContainerInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icontainerinfo)`   
Properties to set  
  
## Properties 

### image
    
    
    public image: string;

ContainerInfo image.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.appengine.v1.IContainerInfo): google.appengine.v1.ContainerInfo;

Creates a new ContainerInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icontainerinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.containerinfo)` | ContainerInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.appengine.v1.ContainerInfo;

Decodes a ContainerInfo message from the specified reader or buffer.

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
`[ContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.containerinfo)` | ContainerInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.appengine.v1.ContainerInfo;

Decodes a ContainerInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.containerinfo)` | ContainerInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.appengine.v1.IContainerInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ContainerInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icontainerinfo)`   
ContainerInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.appengine.v1.IContainerInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ContainerInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icontainerinfo)`   
ContainerInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.appengine.v1.ContainerInfo;

Creates a ContainerInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.containerinfo)` | ContainerInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ContainerInfo

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

Converts this ContainerInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.appengine.v1.ContainerInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ContainerInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ContainerInfo](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.containerinfo)`   
ContainerInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ContainerInfo message.

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
