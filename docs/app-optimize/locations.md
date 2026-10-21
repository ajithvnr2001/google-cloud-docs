---
url: https://docs.cloud.google.com/app-optimize/locations/
title: App Optimize API locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:41:10.249634+00:00
---

# App Optimize API locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Resources ](https://docs.cloud.google.com/app-optimize/quotas)



Send feedback 

#  App Optimize API locations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how locations apply to App Optimize API.

## API endpoint and resource locations

App Optimize API uses a global API endpoint for report management. All API requests for creating and managing reports are directed to the `global` location in the URL path—for example:
    
    
    https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports
    

Replace PROJECT_ID with the ID of the Google Cloud project you're using with App Optimize API.

Despite the API endpoint being global, App Optimize API takes into account the regions and zones of your Google Cloud resources. This means you can analyze your cost and usage data by location, by including the `location` dimension in your reports.

## App Hub locations

App Optimize API can report on your App Hub applications, including those created using Application Design Center. App Hub supports both global and regional applications, and where they are deployed is reflected in your report data.

To understand the difference between global and regional applications in App Hub, see [Global and regional applications](https://docs.cloud.google.com/app-hub/docs/global-regional-applications). The Google Cloud regions that support regional App Hub resources are listed in [App Hub Locations](https://docs.cloud.google.com/app-hub/docs/locations).

For more information about Google Cloud regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
