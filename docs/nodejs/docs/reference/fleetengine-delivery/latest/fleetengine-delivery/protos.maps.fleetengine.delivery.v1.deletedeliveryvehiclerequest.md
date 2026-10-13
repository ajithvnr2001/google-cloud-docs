---
url: https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.deletedeliveryvehiclerequest
title: Class protos.maps.fleetengine.delivery.v1.DeleteDeliveryVehicleRequest (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:06.718217+00:00
---

# Class protos.maps.fleetengine.delivery.v1.DeleteDeliveryVehicleRequest (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.deletedeliveryvehiclerequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.maps.fleetengine.delivery.v1.DeleteDeliveryVehicleRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.3.0  0.2.0  0.1.0 

Represents a DeleteDeliveryVehicleRequest.

## Implements

[protos.maps.fleetengine.delivery.v1.IDeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.ideletedeliveryvehiclerequest)

## Package

[@googlemaps/fleetengine-delivery](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: maps.fleetengine.delivery.v1.IDeleteDeliveryVehicleRequest);

Constructs a new DeleteDeliveryVehicleRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.ideletedeliveryvehiclerequest)`   
Properties to set  
  
## Properties 

### header
    
    
    public header?: (maps.fleetengine.delivery.v1.IDeliveryRequestHeader|null);

DeleteDeliveryVehicleRequest header.

### name
    
    
    public name: string;

DeleteDeliveryVehicleRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: maps.fleetengine.delivery.v1.IDeleteDeliveryVehicleRequest): maps.fleetengine.delivery.v1.DeleteDeliveryVehicleRequest;

Creates a new DeleteDeliveryVehicleRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.ideletedeliveryvehiclerequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.deletedeliveryvehiclerequest)` | DeleteDeliveryVehicleRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): maps.fleetengine.delivery.v1.DeleteDeliveryVehicleRequest;

Decodes a DeleteDeliveryVehicleRequest message from the specified reader or buffer.

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
`[DeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.deletedeliveryvehiclerequest)` | DeleteDeliveryVehicleRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): maps.fleetengine.delivery.v1.DeleteDeliveryVehicleRequest;

Decodes a DeleteDeliveryVehicleRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.deletedeliveryvehiclerequest)` | DeleteDeliveryVehicleRequest  
  
### encode(message, writer)
    
    
    public static encode(message: maps.fleetengine.delivery.v1.IDeleteDeliveryVehicleRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteDeliveryVehicleRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.ideletedeliveryvehiclerequest)`   
DeleteDeliveryVehicleRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: maps.fleetengine.delivery.v1.IDeleteDeliveryVehicleRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteDeliveryVehicleRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.ideletedeliveryvehiclerequest)`   
DeleteDeliveryVehicleRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): maps.fleetengine.delivery.v1.DeleteDeliveryVehicleRequest;

Creates a DeleteDeliveryVehicleRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.deletedeliveryvehiclerequest)` | DeleteDeliveryVehicleRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeleteDeliveryVehicleRequest

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

Converts this DeleteDeliveryVehicleRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: maps.fleetengine.delivery.v1.DeleteDeliveryVehicleRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeleteDeliveryVehicleRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeleteDeliveryVehicleRequest](https://docs.cloud.google.com/nodejs/docs/reference/fleetengine-delivery/latest/fleetengine-delivery/protos.maps.fleetengine.delivery.v1.deletedeliveryvehiclerequest)`   
DeleteDeliveryVehicleRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeleteDeliveryVehicleRequest message.

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
