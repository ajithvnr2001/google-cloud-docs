---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location/
title: Location \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:50.282835+00:00
---

# Location  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  Location Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Information about a location.

JSON representation  
---  
      
    
    {
      "city": string,
      "state": string,
      "countryOrRegion": string,
      "name": string,
      "deskName": string,
      "floorName": string,
      "regionLatitude": number,
      "regionLongitude": number,
      "regionCoordinates": {
        object ([LatLng](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LatLng))
      }
    }  
  
Fields  
---  
`city` |  `string` The city.  
`state` |  `string` The state.  
`countryOrRegion` |  `string` The country or region.  
`name` |  `string` Custom location name (e.g. building or site name like "London Office"). For cloud environments, this is the region (e.g. "us-west2").  
`deskName` |  `string` Desk name or individual location, typically for an employee in an office. (e.g. "IN-BLR-BCPC-11-1121D").  
`floorName` |  `string` Floor name, number or a combination of the two for a building. (e.g. "1-A").  
`regionLatitude  
**(deprecated)**` |  `number` This item is deprecated!Deprecated: use regionCoordinates.  
`regionLongitude  
**(deprecated)**` |  `number` This item is deprecated!Deprecated: use regionCoordinates.  
`regionCoordinates` |  `object (`[LatLng](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LatLng)`)` Coordinates for the associated region. See [](https://cloud.google.com/vision/docs/reference/rest/v1/LatLng)<https://cloud.google.com/vision/docs/reference/rest/v1/LatLng> for a description of the fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-25 UTC."],[],[]] 
