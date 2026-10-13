---
url: https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.placeprediction
title: Class protos.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.PlacePrediction (3.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:03.617503+00:00
---

# Class protos.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.PlacePrediction (3.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.placeprediction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.PlacePrediction (3.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.0.1 (latest)  2.4.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0 

Represents a PlacePrediction.

## Implements

[protos.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.IPlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.iplaceprediction)

## Package

[@googlemaps/places](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.places.v1.AutocompletePlacesResponse.Suggestion.IPlacePrediction);

Constructs a new PlacePrediction.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.iplaceprediction)`   
Properties to set  
  
## Properties 

### distanceMeters
    
    
    public distanceMeters: number;

PlacePrediction distanceMeters.

### place
    
    
    public place: string;

PlacePrediction place.

### placeId
    
    
    public placeId: string;

PlacePrediction placeId.

### structuredFormat
    
    
    public structuredFormat?: (google.maps.places.v1.AutocompletePlacesResponse.Suggestion.IStructuredFormat|null);

PlacePrediction structuredFormat.

### text
    
    
    public text?: (google.maps.places.v1.AutocompletePlacesResponse.Suggestion.IFormattableText|null);

PlacePrediction text.

### types
    
    
    public types: string[];

PlacePrediction types.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.places.v1.AutocompletePlacesResponse.Suggestion.IPlacePrediction): google.maps.places.v1.AutocompletePlacesResponse.Suggestion.PlacePrediction;

Creates a new PlacePrediction instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.iplaceprediction)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.placeprediction)` | PlacePrediction instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.places.v1.AutocompletePlacesResponse.Suggestion.PlacePrediction;

Decodes a PlacePrediction message from the specified reader or buffer.

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
`[PlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.placeprediction)` | PlacePrediction  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.places.v1.AutocompletePlacesResponse.Suggestion.PlacePrediction;

Decodes a PlacePrediction message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.placeprediction)` | PlacePrediction  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.places.v1.AutocompletePlacesResponse.Suggestion.IPlacePrediction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PlacePrediction message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.iplaceprediction)`   
PlacePrediction message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.places.v1.AutocompletePlacesResponse.Suggestion.IPlacePrediction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PlacePrediction message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.iplaceprediction)`   
PlacePrediction message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.places.v1.AutocompletePlacesResponse.Suggestion.PlacePrediction;

Creates a PlacePrediction message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.placeprediction)` | PlacePrediction  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PlacePrediction

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

Converts this PlacePrediction to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.places.v1.AutocompletePlacesResponse.Suggestion.PlacePrediction, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PlacePrediction message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PlacePrediction](https://docs.cloud.google.com/nodejs/docs/reference/places/latest/places/protos.google.maps.places.v1.autocompleteplacesresponse.suggestion.placeprediction)`   
PlacePrediction  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PlacePrediction message.

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
