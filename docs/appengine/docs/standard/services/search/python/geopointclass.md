---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/geopointclass/
title: The GeoPoint Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:49.868592+00:00
---

# The GeoPoint Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/geopointclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The GeoPoint Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `GeoPoint` represents a point on the earth's surface represented by latitude and longitude coordinates.

`GeoPoint` is defined in the module `google.appengine.api.search`.

## Introduction

The GeoPoint class allows you to make map locations searchable. You start by instantiating the GeoPoint class and then pass that object to a specific document field:
    
    
    from google.appengine.api import search
    ...
    # Construct the GeoPoint class
    **geopoint = search.GeoPoint(latitude, longitude)**
    
    fields = [search.TextField(name='name', value=store_name),
              search.TextField(name='address', value=store_address),
              # Construct a GeoField passing geopoint as the value of that field
              **search.GeoField(name='store_location', value=geopoint)**
             ]

For more information about performing location-based searches, please see `[Queries on geopoint fields](https://docs.cloud.google.com/appengine/docs/standard/services/search/query-strings#queries_on_geopoint_fields)`.

## Constructor

The constructor for class `GeoPoint` is defined as follows:

GeoPoint(latitude, longitude)

    

A point on the earth's surface represented by latitude and longitude coordinates.

    

Arguments

latitude
    

The angle between the equatorial plan and a line that passes through the GeoPoint, between -90 and 90 degrees.

longitude
    

The angle east or west from a reference meridian to another meridian that passes through the GeoPoint, between -180 and 180 degrees.

Exceptions

TypeError
    

Any of the parameters has an invalid type, or an unknown attribute was passed.

ValueError
    

An invalid value was passed for one of the parameters.

## Properties

An instance of class `GeoPoint` has the following properties:

latitude
    

An angular distance, in degrees, from the equator. Points located to the south of the equator have negative values, while points located to the north of it have positive values.

longitude
    

An angular distance, in degrees, from the prime meridian. Points located to the west of the prime meridian have positive values, while points located to the east of it have negative values.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
