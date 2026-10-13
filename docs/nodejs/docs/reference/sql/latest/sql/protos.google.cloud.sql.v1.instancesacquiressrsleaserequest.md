---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.instancesacquiressrsleaserequest
title: Class protos.google.cloud.sql.v1.InstancesAcquireSsrsLeaseRequest (0.29.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:13.124700+00:00
---

# Class protos.google.cloud.sql.v1.InstancesAcquireSsrsLeaseRequest (0.29.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.instancesacquiressrsleaserequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.sql.v1.InstancesAcquireSsrsLeaseRequest (0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

Represents an InstancesAcquireSsrsLeaseRequest.

## Implements

[protos.google.cloud.sql.v1.IInstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.iinstancesacquiressrsleaserequest)

## Package

[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.sql.v1.IInstancesAcquireSsrsLeaseRequest);

Constructs a new InstancesAcquireSsrsLeaseRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.iinstancesacquiressrsleaserequest)`   
Properties to set  
  
## Properties 

### acquireSsrsLeaseContext
    
    
    public acquireSsrsLeaseContext?: (google.cloud.sql.v1.IAcquireSsrsLeaseContext|null);

InstancesAcquireSsrsLeaseRequest acquireSsrsLeaseContext.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.sql.v1.IInstancesAcquireSsrsLeaseRequest): google.cloud.sql.v1.InstancesAcquireSsrsLeaseRequest;

Creates a new InstancesAcquireSsrsLeaseRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.iinstancesacquiressrsleaserequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[InstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.instancesacquiressrsleaserequest)` | InstancesAcquireSsrsLeaseRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.sql.v1.InstancesAcquireSsrsLeaseRequest;

Decodes an InstancesAcquireSsrsLeaseRequest message from the specified reader or buffer.

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
`[InstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.instancesacquiressrsleaserequest)` | InstancesAcquireSsrsLeaseRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.sql.v1.InstancesAcquireSsrsLeaseRequest;

Decodes an InstancesAcquireSsrsLeaseRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[InstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.instancesacquiressrsleaserequest)` | InstancesAcquireSsrsLeaseRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.sql.v1.IInstancesAcquireSsrsLeaseRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InstancesAcquireSsrsLeaseRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.iinstancesacquiressrsleaserequest)`   
InstancesAcquireSsrsLeaseRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.sql.v1.IInstancesAcquireSsrsLeaseRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InstancesAcquireSsrsLeaseRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.iinstancesacquiressrsleaserequest)`   
InstancesAcquireSsrsLeaseRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.sql.v1.InstancesAcquireSsrsLeaseRequest;

Creates an InstancesAcquireSsrsLeaseRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[InstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.instancesacquiressrsleaserequest)` | InstancesAcquireSsrsLeaseRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for InstancesAcquireSsrsLeaseRequest

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

Converts this InstancesAcquireSsrsLeaseRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.sql.v1.InstancesAcquireSsrsLeaseRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an InstancesAcquireSsrsLeaseRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[InstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.instancesacquiressrsleaserequest)`   
InstancesAcquireSsrsLeaseRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an InstancesAcquireSsrsLeaseRequest message.

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
