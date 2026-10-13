---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/geopoint/
title: Class GeoPoint (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:34.841056+00:00
---

# Class GeoPoint (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/geopoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class GeoPoint (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

An immutable object representing a geographic location in Firestore. The location is represented as a latitude/longitude pair.

## Implements

Serializable

firestore.GeoPoint

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(latitude, longitude)
    
    
    constructor(latitude: number, longitude: number);

Creates a [GeoPoint][GeoPoint](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/geopoint).

**Parameters**  
---  
**Name** | **Description**  
`latitude` |  `number`   
The latitude as a number between -90 and 90.  
`longitude` |  `number`   
The longitude as a number between -180 and 180.  
**Example**
    
    
    let data = {
      google: new Firestore.GeoPoint(37.422, 122.084)
    };
    
    firestore.doc('col/doc').set(data).then(() => {
      console.log(`Location is ${data.google.latitude}, ` +
        `${data.google.longitude}`);
    });
    

## Properties 

### latitude
    
    
    get latitude(): number;

The latitude as a number between -90 and 90.

{number} GeoPoint#latitude

### longitude
    
    
    get longitude(): number;

The longitude as a number between -180 and 180.

{number} GeoPoint#longitude

## Methods 

### isEqual(other)
    
    
    isEqual(other: firestore.GeoPoint): boolean;

Returns true if this `GeoPoint` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `firestore.GeoPoint`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} true if this `GeoPoint` is equal to the provided value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
