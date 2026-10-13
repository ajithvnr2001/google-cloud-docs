---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.reservationblock-class
title: Class protos.google.cloud.compute.v1beta.ReservationBlock (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:35.718301+00:00
---

# Class protos.google.cloud.compute.v1beta.ReservationBlock (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.reservationblock-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1beta.ReservationBlock (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a ReservationBlock.

## Implements

[protos.google.cloud.compute.v1beta.IReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ireservationblock)

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.compute.v1beta.IReservationBlock);

Constructs a new ReservationBlock.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ireservationblock)`   
Properties to set  
  
## Properties 

### count
    
    
    public count?: (number|null);

ReservationBlock count.

### creationTimestamp
    
    
    public creationTimestamp?: (string|null);

ReservationBlock creationTimestamp.

### healthInfo
    
    
    public healthInfo?: (google.cloud.compute.v1beta.IReservationBlockHealthInfo|null);

ReservationBlock healthInfo.

### id
    
    
    public id?: (number|Long|string|null);

ReservationBlock id.

### inUseCount
    
    
    public inUseCount?: (number|null);

ReservationBlock inUseCount.

### inUseHostCount
    
    
    public inUseHostCount?: (number|null);

ReservationBlock inUseHostCount.

### kind
    
    
    public kind?: (string|null);

ReservationBlock kind.

### name
    
    
    public name?: (string|null);

ReservationBlock name.

### physicalTopology
    
    
    public physicalTopology?: (google.cloud.compute.v1beta.IReservationBlockPhysicalTopology|null);

ReservationBlock physicalTopology.

### reservationMaintenance
    
    
    public reservationMaintenance?: (google.cloud.compute.v1beta.IGroupMaintenanceInfo|null);

ReservationBlock reservationMaintenance.

### reservationSubBlockCount
    
    
    public reservationSubBlockCount?: (number|null);

ReservationBlock reservationSubBlockCount.

### reservationSubBlockInUseCount
    
    
    public reservationSubBlockInUseCount?: (number|null);

ReservationBlock reservationSubBlockInUseCount.

### selfLink
    
    
    public selfLink?: (string|null);

ReservationBlock selfLink.

### selfLinkWithId
    
    
    public selfLinkWithId?: (string|null);

ReservationBlock selfLinkWithId.

### status
    
    
    public status?: (string|null);

ReservationBlock status.

### zone
    
    
    public zone?: (string|null);

ReservationBlock zone.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.compute.v1beta.IReservationBlock): google.cloud.compute.v1beta.ReservationBlock;

Creates a new ReservationBlock instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ireservationblock)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.reservationblock-class)` | ReservationBlock instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.compute.v1beta.ReservationBlock;

Decodes a ReservationBlock message from the specified reader or buffer.

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
`[ReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.reservationblock-class)` | ReservationBlock  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.compute.v1beta.ReservationBlock;

Decodes a ReservationBlock message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.reservationblock-class)` | ReservationBlock  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.compute.v1beta.IReservationBlock, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ReservationBlock message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ireservationblock)`   
ReservationBlock message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.compute.v1beta.IReservationBlock, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ReservationBlock message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ireservationblock)`   
ReservationBlock message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.compute.v1beta.ReservationBlock;

Creates a ReservationBlock message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.reservationblock-class)` | ReservationBlock  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ReservationBlock

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

Converts this ReservationBlock to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.compute.v1beta.ReservationBlock, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ReservationBlock message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ReservationBlock](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.reservationblock-class)`   
ReservationBlock  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ReservationBlock message.

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
