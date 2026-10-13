---
url: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.placeview-class
title: Class protos.google.maps.geocode.v4.PlaceView (0.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:34.437575+00:00
---

# Class protos.google.maps.geocode.v4.PlaceView (0.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.placeview-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.geocode.v4.PlaceView (0.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a PlaceView.

## Implements

[protos.google.maps.geocode.v4.IPlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.iplaceview)

## Package

[@google-cloud/geocode](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.geocode.v4.IPlaceView);

Constructs a new PlaceView.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.iplaceview)`   
Properties to set  
  
## Properties 

### displayName
    
    
    public displayName?: (google.type.ILocalizedText|null);

PlaceView displayName.

### displayPolygon
    
    
    public displayPolygon?: (google.protobuf.IStruct|null);

PlaceView displayPolygon.

### formattedAddress
    
    
    public formattedAddress: string;

PlaceView formattedAddress.

### location
    
    
    public location?: (google.type.ILatLng|null);

PlaceView location.

### place
    
    
    public place: string;

PlaceView place.

### placeId
    
    
    public placeId: string;

PlaceView placeId.

### postalAddress
    
    
    public postalAddress?: (google.type.IPostalAddress|null);

PlaceView postalAddress.

### primaryType
    
    
    public primaryType: string;

PlaceView primaryType.

### structureType
    
    
    public structureType: (google.maps.geocode.v4.PlaceView.StructureType|keyof typeof google.maps.geocode.v4.PlaceView.StructureType);

PlaceView structureType.

### types
    
    
    public types: string[];

PlaceView types.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.geocode.v4.IPlaceView): google.maps.geocode.v4.PlaceView;

Creates a new PlaceView instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.iplaceview)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.placeview-class)` | PlaceView instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.geocode.v4.PlaceView;

Decodes a PlaceView message from the specified reader or buffer.

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
`[PlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.placeview-class)` | PlaceView  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.geocode.v4.PlaceView;

Decodes a PlaceView message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.placeview-class)` | PlaceView  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.geocode.v4.IPlaceView, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PlaceView message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.iplaceview)`   
PlaceView message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.geocode.v4.IPlaceView, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PlaceView message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.iplaceview)`   
PlaceView message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.geocode.v4.PlaceView;

Creates a PlaceView message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.placeview-class)` | PlaceView  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PlaceView

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

Converts this PlaceView to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.geocode.v4.PlaceView, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PlaceView message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PlaceView](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.placeview-class)`   
PlaceView  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PlaceView message.

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
