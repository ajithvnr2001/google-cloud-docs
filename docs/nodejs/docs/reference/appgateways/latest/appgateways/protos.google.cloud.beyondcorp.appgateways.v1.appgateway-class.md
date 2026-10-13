---
url: https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.appgateway-class
title: Class protos.google.cloud.beyondcorp.appgateways.v1.AppGateway (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:58.959891+00:00
---

# Class protos.google.cloud.beyondcorp.appgateways.v1.AppGateway (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.appgateway-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.beyondcorp.appgateways.v1.AppGateway (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  0.3.2  0.2.3 

Represents an AppGateway.

## Implements

[protos.google.cloud.beyondcorp.appgateways.v1.IAppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.iappgateway)

## Package

[@google-cloud/appgateways](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.beyondcorp.appgateways.v1.IAppGateway);

Constructs a new AppGateway.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.iappgateway)`   
Properties to set  
  
## Properties 

### allocatedConnections
    
    
    public allocatedConnections: google.cloud.beyondcorp.appgateways.v1.AppGateway.IAllocatedConnection[];

AppGateway allocatedConnections.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AppGateway createTime.

### displayName
    
    
    public displayName: string;

AppGateway displayName.

### hostType
    
    
    public hostType: (google.cloud.beyondcorp.appgateways.v1.AppGateway.HostType|keyof typeof google.cloud.beyondcorp.appgateways.v1.AppGateway.HostType);

AppGateway hostType.

### labels
    
    
    public labels: { [k: string]: string };

AppGateway labels.

### name
    
    
    public name: string;

AppGateway name.

### state
    
    
    public state: (google.cloud.beyondcorp.appgateways.v1.AppGateway.State|keyof typeof google.cloud.beyondcorp.appgateways.v1.AppGateway.State);

AppGateway state.

### type
    
    
    public type: (google.cloud.beyondcorp.appgateways.v1.AppGateway.Type|keyof typeof google.cloud.beyondcorp.appgateways.v1.AppGateway.Type);

AppGateway type.

### uid
    
    
    public uid: string;

AppGateway uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

AppGateway updateTime.

### uri
    
    
    public uri: string;

AppGateway uri.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.beyondcorp.appgateways.v1.IAppGateway): google.cloud.beyondcorp.appgateways.v1.AppGateway;

Creates a new AppGateway instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.iappgateway)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.appgateway-class)` | AppGateway instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.beyondcorp.appgateways.v1.AppGateway;

Decodes an AppGateway message from the specified reader or buffer.

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
`[AppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.appgateway-class)` | AppGateway  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.beyondcorp.appgateways.v1.AppGateway;

Decodes an AppGateway message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.appgateway-class)` | AppGateway  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.beyondcorp.appgateways.v1.IAppGateway, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppGateway message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.iappgateway)`   
AppGateway message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.beyondcorp.appgateways.v1.IAppGateway, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppGateway message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.iappgateway)`   
AppGateway message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.beyondcorp.appgateways.v1.AppGateway;

Creates an AppGateway message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.appgateway-class)` | AppGateway  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AppGateway

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

Converts this AppGateway to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.beyondcorp.appgateways.v1.AppGateway, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AppGateway message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AppGateway](https://docs.cloud.google.com/nodejs/docs/reference/appgateways/latest/appgateways/protos.google.cloud.beyondcorp.appgateways.v1.appgateway-class)`   
AppGateway  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AppGateway message.

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
