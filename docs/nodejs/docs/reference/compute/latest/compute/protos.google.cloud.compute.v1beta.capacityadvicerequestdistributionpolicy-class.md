---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.capacityadvicerequestdistributionpolicy-class
title: Class protos.google.cloud.compute.v1beta.CapacityAdviceRequestDistributionPolicy (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:46.602338+00:00
---

# Class protos.google.cloud.compute.v1beta.CapacityAdviceRequestDistributionPolicy (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.capacityadvicerequestdistributionpolicy-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1beta.CapacityAdviceRequestDistributionPolicy (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a CapacityAdviceRequestDistributionPolicy.

## Implements

[protos.google.cloud.compute.v1beta.ICapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.icapacityadvicerequestdistributionpolicy)

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.compute.v1beta.ICapacityAdviceRequestDistributionPolicy);

Constructs a new CapacityAdviceRequestDistributionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.icapacityadvicerequestdistributionpolicy)`   
Properties to set  
  
## Properties 

### targetShape
    
    
    public targetShape?: (string|null);

CapacityAdviceRequestDistributionPolicy targetShape.

### zones
    
    
    public zones: google.cloud.compute.v1beta.ICapacityAdviceRequestDistributionPolicyZoneConfiguration[];

CapacityAdviceRequestDistributionPolicy zones.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.compute.v1beta.ICapacityAdviceRequestDistributionPolicy): google.cloud.compute.v1beta.CapacityAdviceRequestDistributionPolicy;

Creates a new CapacityAdviceRequestDistributionPolicy instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.icapacityadvicerequestdistributionpolicy)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.capacityadvicerequestdistributionpolicy-class)` | CapacityAdviceRequestDistributionPolicy instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.compute.v1beta.CapacityAdviceRequestDistributionPolicy;

Decodes a CapacityAdviceRequestDistributionPolicy message from the specified reader or buffer.

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
`[CapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.capacityadvicerequestdistributionpolicy-class)` | CapacityAdviceRequestDistributionPolicy  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.compute.v1beta.CapacityAdviceRequestDistributionPolicy;

Decodes a CapacityAdviceRequestDistributionPolicy message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.capacityadvicerequestdistributionpolicy-class)` | CapacityAdviceRequestDistributionPolicy  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.compute.v1beta.ICapacityAdviceRequestDistributionPolicy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CapacityAdviceRequestDistributionPolicy message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.icapacityadvicerequestdistributionpolicy)`   
CapacityAdviceRequestDistributionPolicy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.compute.v1beta.ICapacityAdviceRequestDistributionPolicy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CapacityAdviceRequestDistributionPolicy message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.icapacityadvicerequestdistributionpolicy)`   
CapacityAdviceRequestDistributionPolicy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.compute.v1beta.CapacityAdviceRequestDistributionPolicy;

Creates a CapacityAdviceRequestDistributionPolicy message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.capacityadvicerequestdistributionpolicy-class)` | CapacityAdviceRequestDistributionPolicy  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CapacityAdviceRequestDistributionPolicy

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

Converts this CapacityAdviceRequestDistributionPolicy to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.compute.v1beta.CapacityAdviceRequestDistributionPolicy, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CapacityAdviceRequestDistributionPolicy message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CapacityAdviceRequestDistributionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.capacityadvicerequestdistributionpolicy-class)`   
CapacityAdviceRequestDistributionPolicy  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CapacityAdviceRequestDistributionPolicy message.

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
