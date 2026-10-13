---
url: https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.hydrationstatus
title: Class protos.google.cloud.telcoautomation.v1alpha1.HydrationStatus (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:07.882963+00:00
---

# Class protos.google.cloud.telcoautomation.v1alpha1.HydrationStatus (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.hydrationstatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.telcoautomation.v1alpha1.HydrationStatus (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.1.0 

Represents a HydrationStatus.

## Implements

[protos.google.cloud.telcoautomation.v1alpha1.IHydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.ihydrationstatus)

## Package

[@google-cloud/telcoautomation](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.telcoautomation.v1alpha1.IHydrationStatus);

Constructs a new HydrationStatus.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.ihydrationstatus)`   
Properties to set  
  
## Properties 

### siteVersion
    
    
    public siteVersion?: (google.cloud.telcoautomation.v1alpha1.ISiteVersion|null);

HydrationStatus siteVersion.

### status
    
    
    public status: string;

HydrationStatus status.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.telcoautomation.v1alpha1.IHydrationStatus): google.cloud.telcoautomation.v1alpha1.HydrationStatus;

Creates a new HydrationStatus instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.ihydrationstatus)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[HydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.hydrationstatus)` | HydrationStatus instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.telcoautomation.v1alpha1.HydrationStatus;

Decodes a HydrationStatus message from the specified reader or buffer.

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
`[HydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.hydrationstatus)` | HydrationStatus  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.telcoautomation.v1alpha1.HydrationStatus;

Decodes a HydrationStatus message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[HydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.hydrationstatus)` | HydrationStatus  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.telcoautomation.v1alpha1.IHydrationStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HydrationStatus message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.ihydrationstatus)`   
HydrationStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.telcoautomation.v1alpha1.IHydrationStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HydrationStatus message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.ihydrationstatus)`   
HydrationStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.telcoautomation.v1alpha1.HydrationStatus;

Creates a HydrationStatus message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[HydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.hydrationstatus)` | HydrationStatus  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for HydrationStatus

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

Converts this HydrationStatus to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.telcoautomation.v1alpha1.HydrationStatus, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a HydrationStatus message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[HydrationStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.hydrationstatus)`   
HydrationStatus  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a HydrationStatus message.

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
