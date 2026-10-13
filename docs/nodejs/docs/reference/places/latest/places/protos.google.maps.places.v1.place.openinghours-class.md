---
url: https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.openinghours-class
title: Class protos.google.maps.places.v1.Place.OpeningHours (3.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:01.413637+00:00
---

# Class protos.google.maps.places.v1.Place.OpeningHours (3.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.openinghours-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.places.v1.Place.OpeningHours (3.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.0.1 (latest)  2.4.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0 

Represents an OpeningHours.

## Implements

[protos.google.maps.places.v1.Place.IOpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.iopeninghours)

## Package

[@googlemaps/places](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.places.v1.Place.IOpeningHours);

Constructs a new OpeningHours.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.iopeninghours)`   
Properties to set  
  
## Properties 

### nextCloseTime
    
    
    public nextCloseTime?: (google.protobuf.ITimestamp|null);

OpeningHours nextCloseTime.

### nextOpenTime
    
    
    public nextOpenTime?: (google.protobuf.ITimestamp|null);

OpeningHours nextOpenTime.

### openNow
    
    
    public openNow?: (boolean|null);

OpeningHours openNow.

### periods
    
    
    public periods: google.maps.places.v1.Place.OpeningHours.IPeriod[];

OpeningHours periods.

### secondaryHoursType
    
    
    public secondaryHoursType: (google.maps.places.v1.Place.OpeningHours.SecondaryHoursType|keyof typeof google.maps.places.v1.Place.OpeningHours.SecondaryHoursType);

OpeningHours secondaryHoursType.

### specialDays
    
    
    public specialDays: google.maps.places.v1.Place.OpeningHours.ISpecialDay[];

OpeningHours specialDays.

### weekdayDescriptions
    
    
    public weekdayDescriptions: string[];

OpeningHours weekdayDescriptions.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.places.v1.Place.IOpeningHours): google.maps.places.v1.Place.OpeningHours;

Creates a new OpeningHours instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.iopeninghours)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.openinghours-class)` | OpeningHours instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.places.v1.Place.OpeningHours;

Decodes an OpeningHours message from the specified reader or buffer.

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
`[OpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.openinghours-class)` | OpeningHours  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.places.v1.Place.OpeningHours;

Decodes an OpeningHours message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.openinghours-class)` | OpeningHours  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.places.v1.Place.IOpeningHours, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OpeningHours message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.iopeninghours)`   
OpeningHours message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.places.v1.Place.IOpeningHours, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OpeningHours message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.iopeninghours)`   
OpeningHours message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.places.v1.Place.OpeningHours;

Creates an OpeningHours message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.openinghours-class)` | OpeningHours  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OpeningHours

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

Converts this OpeningHours to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.places.v1.Place.OpeningHours, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OpeningHours message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OpeningHours](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.place.openinghours-class)`   
OpeningHours  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OpeningHours message.

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
