---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.type
title: Package google.type \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:53:40.971352+00:00
---

# Package google.type  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.type

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)



Send feedback 

#  Package google.type Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Date](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.type#google.type.Date)` (message)
  * `[LatLng](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.type#google.type.LatLng)` (message)



## Date

Represents a whole calendar date, e.g. date of birth. The time of day and time zone are either specified elsewhere or are not significant. The date is relative to the Proleptic Gregorian Calendar. The day may be 0 to represent a year and month where the day is not significant, e.g. credit card expiration date. The year may be 0 to represent a month and day independent of year, e.g. anniversary date. Related types are `google.type.TimeOfDay` and `google.protobuf.Timestamp`.

Fields  
---  
`year` |  `int32` Year of date. Must be from 1 to 9999, or 0 if specifying a date without a year.   
`month` |  `int32` Month of year. Must be from 1 to 12.   
`day` |  `int32` Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a year/month where the day is not significant.   
  
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

Fields  
---  
`latitude` |  `double` The latitude in degrees. It must be in the range [-90.0, +90.0].   
`longitude` |  `double` The longitude in degrees. It must be in the range [-180.0, +180.0].   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
