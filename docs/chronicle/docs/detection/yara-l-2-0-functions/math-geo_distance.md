---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-geo_distance/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:37.642158+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-geo_distance/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.geo_distance

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    math.geo_distance(longitude1, latitude1, longitude2, latitude2))
    

#### Description

Returns the distance between two geographic locations (coordinates) in meters. Returns -1 if the coordinates are invalid.

#### Parameter data types

`FLOAT`, `FLOAT`, `FLOAT`, `FLOAT`

#### Return type

`FLOAT`

#### Code samples

##### Example 1

The following example returns the distance when all parameters are valid coordinates:
    
    
    math.geo_distance(-122.020287, 37.407574, -122.021810, 37.407574) = 134.564318
    

##### Example 2

The following example returns the distance when one of the parameters is a truncated coordinate:
    
    
    math.geo_distance(-122.000000, 37.407574, -122.021810, 37.407574) = 1926.421905
    

##### Example 3

The following example returns `-1` when one of the parameters is an invalid coordinate:
    
    
    math.geo_distance(0-122.897680, 37.407574, 0-122.021810, 97.407574) = -1.000000
    

##### Example 4

The following example returns `0` when coordinates are the same:
    
    
    math.geo_distance(-122.897680, 37.407574, -122.897680, 37.407574) = 0.000000
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
