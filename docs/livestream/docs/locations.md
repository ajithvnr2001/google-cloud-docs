---
url: https://docs.cloud.google.com/livestream/docs/locations/
title: Live Stream API locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:46:17.329679+00:00
---

# Live Stream API locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Resources ](https://docs.cloud.google.com/livestream/docs/resources)



Send feedback 

#  Live Stream API locations Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes the geographic availability of the Live Stream API. Google Cloud uses independent regions to define the geographic location of physical computing resources. Each region is divided into multiple zones. For more information, see [Regions and zones](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) on the Geography, regions, and zones page.

This guide also describes issues to consider when planning how to manage the locations of your input endpoints and channels.

## Before you begin

Make sure you are familiar with the introductory concepts and terminology in the Live Stream API. For more information, see the [Overview](https://docs.cloud.google.com/livestream/docs/overview).

## Managing live stream location

To start a live stream, you first create a Cloud Storage bucket, an input endpoint, and channel resource. The channel transcodes your input stream into an output stream and stores the live stream manifest and segment files in your Cloud Storage bucket. For the best performance results, make sure you create your input endpoint and channel as close as possible to the location where the live stream files are stored in Cloud Storage.

After you create an input endpoint or channel, you can't change their locations.

For more information on optimizing the location of data stored in Cloud Storage and a list of available locations, see [Bucket locations](https://docs.cloud.google.com/storage/docs/locations).

To learn how to move data stored in Cloud Storage between bucket locations, see [Copying, renaming, and moving objects](https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects).

## Regions

The following table lists the regions in the Americas where the Live Stream API is available.

Region description | Region name  
---|---  
Iowa, USA | `us-central1`  
Oregon, USA | `us-west1`  
Los Angeles, USA | `us-west2`  
South Carolina, USA | `us-east1`  
Northern Virginia, USA | `us-east4`  
Montréal, Canada | `northamerica-northeast1`  
São Paulo, Brazil | `southamerica-east1`  
  
The following table lists the regions in Asia Pacific where the Live Stream API is available.

Region description | Region name  
---|---  
Taiwan | `asia-east1`  
Hong Kong | `asia-east2`  
Tokyo | `asia-northeast1`  
Mumbai | `asia-south1`  
Singapore | `asia-southeast1`  
  
The following table lists the regions in Australia where the Live Stream API is available.

Region description | Region name  
---|---  
Sydney | `australia-southeast1`  
  
The following table lists the regions in Europe where the Live Stream API is available.

Region description | Region name  
---|---  
Finland | `europe-north1`  
Belgium | `europe-west1`  
London | `europe-west2`  
Frankfurt | `europe-west3`  
Netherlands | `europe-west4`  
  
## Location considerations

When you choose a location to start your live stream, you might want to consider factors such as the following:

  * Latency
  * Cost
  * Resiliency
  * Co-location with other Google Cloud services, such as Cloud Storage



## What's next

  * [Quickstarts](https://docs.cloud.google.com/livestream/docs/quickstarts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
