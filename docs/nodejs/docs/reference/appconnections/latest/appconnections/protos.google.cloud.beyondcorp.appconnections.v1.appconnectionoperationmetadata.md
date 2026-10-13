---
url: https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.appconnectionoperationmetadata
title: Class protos.google.cloud.beyondcorp.appconnections.v1.AppConnectionOperationMetadata (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:39.242893+00:00
---

# Class protos.google.cloud.beyondcorp.appconnections.v1.AppConnectionOperationMetadata (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.appconnectionoperationmetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.beyondcorp.appconnections.v1.AppConnectionOperationMetadata (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  0.3.2  0.2.3 

Represents an AppConnectionOperationMetadata.

## Implements

[protos.google.cloud.beyondcorp.appconnections.v1.IAppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.iappconnectionoperationmetadata)

## Package

[@google-cloud/appconnections](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.beyondcorp.appconnections.v1.IAppConnectionOperationMetadata);

Constructs a new AppConnectionOperationMetadata.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.iappconnectionoperationmetadata)`   
Properties to set  
  
## Properties 

### apiVersion
    
    
    public apiVersion: string;

AppConnectionOperationMetadata apiVersion.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AppConnectionOperationMetadata createTime.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

AppConnectionOperationMetadata endTime.

### requestedCancellation
    
    
    public requestedCancellation: boolean;

AppConnectionOperationMetadata requestedCancellation.

### statusMessage
    
    
    public statusMessage: string;

AppConnectionOperationMetadata statusMessage.

### target
    
    
    public target: string;

AppConnectionOperationMetadata target.

### verb
    
    
    public verb: string;

AppConnectionOperationMetadata verb.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.beyondcorp.appconnections.v1.IAppConnectionOperationMetadata): google.cloud.beyondcorp.appconnections.v1.AppConnectionOperationMetadata;

Creates a new AppConnectionOperationMetadata instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.iappconnectionoperationmetadata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.appconnectionoperationmetadata)` | AppConnectionOperationMetadata instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.beyondcorp.appconnections.v1.AppConnectionOperationMetadata;

Decodes an AppConnectionOperationMetadata message from the specified reader or buffer.

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
`[AppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.appconnectionoperationmetadata)` | AppConnectionOperationMetadata  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.beyondcorp.appconnections.v1.AppConnectionOperationMetadata;

Decodes an AppConnectionOperationMetadata message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.appconnectionoperationmetadata)` | AppConnectionOperationMetadata  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.beyondcorp.appconnections.v1.IAppConnectionOperationMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppConnectionOperationMetadata message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.iappconnectionoperationmetadata)`   
AppConnectionOperationMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.beyondcorp.appconnections.v1.IAppConnectionOperationMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppConnectionOperationMetadata message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.iappconnectionoperationmetadata)`   
AppConnectionOperationMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.beyondcorp.appconnections.v1.AppConnectionOperationMetadata;

Creates an AppConnectionOperationMetadata message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.appconnectionoperationmetadata)` | AppConnectionOperationMetadata  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AppConnectionOperationMetadata

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

Converts this AppConnectionOperationMetadata to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.beyondcorp.appconnections.v1.AppConnectionOperationMetadata, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AppConnectionOperationMetadata message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AppConnectionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/appconnections/latest/appconnections/protos.google.cloud.beyondcorp.appconnections.v1.appconnectionoperationmetadata)`   
AppConnectionOperationMetadata  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AppConnectionOperationMetadata message.

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
