---
url: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.igeocoderesult
title: Interface protos.google.maps.geocode.v4.IGeocodeResult (0.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:45.708125+00:00
---

# Interface protos.google.maps.geocode.v4.IGeocodeResult (0.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.maps.geocode.v4.igeocoderesult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.maps.geocode.v4.IGeocodeResult (0.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

Properties of a GeocodeResult.

## Package

[@google-cloud/geocode](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)

## Properties 

### addressComponents
    
    
    addressComponents?: (google.maps.geocode.v4.GeocodeResult.IAddressComponent[]|null);

GeocodeResult addressComponents

### bounds
    
    
    bounds?: (google.geo.type.IViewport|null);

GeocodeResult bounds

### formattedAddress
    
    
    formattedAddress?: (string|null);

GeocodeResult formattedAddress

### granularity
    
    
    granularity?: (google.maps.geocode.v4.GeocodeResult.Granularity|keyof typeof google.maps.geocode.v4.GeocodeResult.Granularity|null);

GeocodeResult granularity

### location
    
    
    location?: (google.type.ILatLng|null);

GeocodeResult location

### place
    
    
    place?: (string|null);

GeocodeResult place

### placeId
    
    
    placeId?: (string|null);

GeocodeResult placeId

### plusCode
    
    
    plusCode?: (google.maps.geocode.v4.IPlusCode|null);

GeocodeResult plusCode

### postalAddress
    
    
    postalAddress?: (google.type.IPostalAddress|null);

GeocodeResult postalAddress

### postalCodeLocalities
    
    
    postalCodeLocalities?: (google.type.ILocalizedText[]|null);

GeocodeResult postalCodeLocalities

### types
    
    
    types?: (string[]|null);

GeocodeResult types

### viewport
    
    
    viewport?: (google.geo.type.IViewport|null);

GeocodeResult viewport

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
