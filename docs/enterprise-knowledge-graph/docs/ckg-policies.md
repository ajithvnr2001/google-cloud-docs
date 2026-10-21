---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/ckg-policies/
title: Additional Product Requirements \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:23:59.138109+00:00
---

# Additional Product Requirements  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/ckg-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Guides ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)



Send feedback 

#  Additional Product Requirements Stay organized with collections  Save and categorize content based on your preferences. 

Requirements are listed that are specific to all applications developed with Google Knowledge Graph Search API. This API is also subject to the [Google Cloud Terms of Service](https://cloud.google.com/terms) and [Google Cloud Service Specific Terms](https://cloud.google.com/terms/service-terms).

## Fetching, caching, or storage of content

Applications using the Google Knowledge Graph Search API are bound by the terms of your Agreement with Google. Subject to the terms of your Agreement, you must follow the conditions and data license requirements returned by the API per attribute.

For example, when querying `Stanford University`, the `detailedDescription` is attached with the data license. Follow the Creative Commons Attribution ShareAlike 3.0 Unported License (CC BY-SA 3.0) requirements from the provider.
    
    
      "license": "https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License"
    

For the `name` field, check if there is a license attached to the field from `additionalProperty`. In the following example, the `name` field comes from the [Google Places API](https://developers.google.com/maps/documentation/places/web-service). Follow the license and data restrictions outlined in [Google Maps Platform Terms of Service](https://cloud.google.com/maps-platform/terms).
    
    
      "additionalProperty": {
       "@type": "PropertyValue",
       "name": "nameLicense",
       "value": "https://cloud.google.com/maps-platform/terms"
      }
    

For [Cloud KG MID](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/mid) and other attributes that don't have an attached license, you can cache and store the returned data. However, treat the Cloud KG MID as the primary identifier, because company names and descriptions might change over time. Querying the Google Knowledge Graph Search API in real time can help confirm that you are using the most recent updates.

## Displaying Google Knowledge Graph Search API results

You can display Google Knowledge Graph Search API results on your application, subject to the license requirements returned in the API.

## Attribution requirements

You don't have to make an attribution unless the license associated with the data points specifically requires that you do so.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
