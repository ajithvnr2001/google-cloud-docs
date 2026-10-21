---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/LocationMetadata/
title: LocationMetadata \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:37:01.463009+00:00
---

# LocationMetadata  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/LocationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)



Send feedback 

#  LocationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * LatLng
    * JSON representation



Metadata for the given `[google.cloud.location.Location](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/ListLocationsResponse#Location)`.

JSON representation  
---  
      
    
    {
      "partitionId": string,
      "standardEnvironmentAvailable": boolean,
      "flexibleEnvironmentAvailable": boolean,
      "coordinates": {
        object([LatLng](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/LocationMetadata#LatLng))
      },
    }  
  
Fields  
---  
`partitionId` |  `string` App Engine partition corresponding to the given location. Example: "s".Note: This field is used in responses only. Any value specified here in a request is ignored.  
`standardEnvironmentAvailable` |  `boolean` App Engine Standard Environment is available in the given location.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`flexibleEnvironmentAvailable` |  `boolean` App Engine Flexible Environment is available in the given location.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`coordinates` |  `object(`[LatLng](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/LocationMetadata#LatLng)`)` Note: This field is used in responses only. Any value specified here in a request is ignored.   
  
## LatLng

An object representing a latitude/longitude pair. This is expressed as a pair of doubles representing degrees latitude and degrees longitude. Unless specified otherwise, this must conform to the [WGS84 standard](http://www.unoosa.org/pdf/icg/2012/template/WGS_84.pdf). Values must be within normalized ranges.

Example of normalization code in Python:
    
    
    def NormalizeLongitude(longitude):
      """Wraps decimal degrees longitude to [-180.0, 180.0]."""
      q, r = divmod(longitude, 360.0)
      if r > 180.0 or (r == 180.0 and q <= -1.0):
        return r - 360.0
      return r
    
    def NormalizeLatLng(latitude, longitude):
      """Wraps decimal degrees latitude and longitude to
      [-90.0, 90.0] and [-180.0, 180.0], respectively."""
      r = latitude % 360.0
      if r <= 90.0:
        return r, NormalizeLongitude(longitude)
      elif r >= 270.0:
        return r - 360, NormalizeLongitude(longitude)
      else:
        return 180 - r, NormalizeLongitude(longitude + 180.0)
    
    assert 180.0 == NormalizeLongitude(180.0)
    assert -180.0 == NormalizeLongitude(-180.0)
    assert -179.0 == NormalizeLongitude(181.0)
    assert (0.0, 0.0) == NormalizeLatLng(360.0, 0.0)
    assert (0.0, 0.0) == NormalizeLatLng(-360.0, 0.0)
    assert (85.0, 180.0) == NormalizeLatLng(95.0, 0.0)
    assert (-85.0, -170.0) == NormalizeLatLng(-95.0, 10.0)
    assert (90.0, 10.0) == NormalizeLatLng(90.0, 10.0)
    assert (-90.0, -10.0) == NormalizeLatLng(-90.0, -10.0)
    assert (0.0, -170.0) == NormalizeLatLng(-180.0, 10.0)
    assert (0.0, -170.0) == NormalizeLatLng(180.0, 10.0)
    assert (-90.0, 10.0) == NormalizeLatLng(270.0, 10.0)
    assert (90.0, 10.0) == NormalizeLatLng(-270.0, 10.0)
    

The code in logs/storage/validator/logs_validator_traits.cc treats this type as if it were annotated as ST_LOCATION.

JSON representation  
---  
      
    
    {
      "latitude": number,
      "longitude": number,
    }  
  
Fields  
---  
`latitude` |  `number` The latitude in degrees. It must be in the range [-90.0, +90.0].   
`longitude` |  `number` The longitude in degrees. It must be in the range [-180.0, +180.0].   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
