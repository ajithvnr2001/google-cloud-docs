---
url: https://docs.cloud.google.com/firestore/native/docs/geospatial-query/
title: Use geospatial queries \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:45:35.019927+00:00
---

# Use geospatial queries  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/geospatial-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use geospatial queries

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can perform geospatial queries in Firestore to build location aware services. For example, you can find the distance between a user and nearby points of interest, sorting them from nearest to farthest.

## Edition requirements

The geospatial query feature requires a Firestore Enterprise edition database.

## Before you begin

To perform a geospatial query, you must first [create geospatial indexes](https://docs.cloud.google.com/firestore/native/docs/enterprise-indexing#create-geospatial-index) for the fields you need to search through.

## Run a geospatial query

To perform a geospatial query, use the `geoDistance` expression within the `query` parameter of the `search(...)` stage.

Only the less than or equals (`<=`) operator is supported. The distance is measured in meters.

For example, the following query finds all restaurants within 1,000 meters of the listed geopoint.

### Web version 9
    
    
    firestore.pipeline().collection('restaurants')
      .search({
        query: field('location')
          .geoDistance(new GeoPoint(38.989177, -107.065076))
          .lessThan(1000 /* m */)
      });

##### iOS
    
    
    firestore.pipeline().collection("restaurants")
        .search(
            query: Field("location")
                .geoDistance(GeoPoint(latitude: 38.989177, longitude: -107.065076))
                .lessThan(1000)
        )

##### Android
    
    
    firestore.pipeline()
            .collection("restaurants")
            .search(new SearchOptions()
                    .withQuery(field("location")
                            .geoDistance(new GeoPoint(38.989177, -107.065076))
                            .lessThan(1000 /* meters */)));

##### Node.js
    
    
    firestore.pipeline().collection('restaurants')
      .search({
        query: field('location')
          .geoDistance(new GeoPoint(38.989177, -107.065076))
          .lessThan(1000 /* m */)
      });

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
