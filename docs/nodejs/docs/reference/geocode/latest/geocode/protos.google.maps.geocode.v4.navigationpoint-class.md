---
url: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.navigationpoint-class
title: Class protos.google.maps.geocode.v4.NavigationPoint (0.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:34.315326+00:00
---

# Class protos.google.maps.geocode.v4.NavigationPoint (0.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.navigationpoint-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.geocode.v4.NavigationPoint (0.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a NavigationPoint.

## Implements

[protos.google.maps.geocode.v4.INavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.inavigationpoint)

## Package

[@google-cloud/geocode](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.geocode.v4.INavigationPoint);

Constructs a new NavigationPoint.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.inavigationpoint)`   
Properties to set  
  
## Properties 

### displayName
    
    
    public displayName?: (google.type.ILocalizedText|null);

NavigationPoint displayName.

### location
    
    
    public location?: (google.type.ILatLng|null);

NavigationPoint location.

### navigationPointToken
    
    
    public navigationPointToken: string;

NavigationPoint navigationPointToken.

### travelModes
    
    
    public travelModes: google.maps.geocode.v4.NavigationPoint.TravelMode[];

NavigationPoint travelModes.

### usages
    
    
    public usages: google.maps.geocode.v4.NavigationPoint.Usage[];

NavigationPoint usages.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.geocode.v4.INavigationPoint): google.maps.geocode.v4.NavigationPoint;

Creates a new NavigationPoint instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.inavigationpoint)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[NavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.navigationpoint-class)` | NavigationPoint instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.geocode.v4.NavigationPoint;

Decodes a NavigationPoint message from the specified reader or buffer.

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
`[NavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.navigationpoint-class)` | NavigationPoint  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.geocode.v4.NavigationPoint;

Decodes a NavigationPoint message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[NavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.navigationpoint-class)` | NavigationPoint  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.geocode.v4.INavigationPoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NavigationPoint message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.inavigationpoint)`   
NavigationPoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.geocode.v4.INavigationPoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NavigationPoint message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.inavigationpoint)`   
NavigationPoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.geocode.v4.NavigationPoint;

Creates a NavigationPoint message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[NavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.navigationpoint-class)` | NavigationPoint  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for NavigationPoint

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

Converts this NavigationPoint to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.geocode.v4.NavigationPoint, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a NavigationPoint message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[NavigationPoint](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.navigationpoint-class)`   
NavigationPoint  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a NavigationPoint message.

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
