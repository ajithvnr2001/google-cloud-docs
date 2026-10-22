---
url: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-fetch-multiple-region-links/
title: Search multi-region lineage using client-side fan-out \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:04.141354+00:00
---

# Search multi-region lineage using client-side fan-out  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-fetch-multiple-region-links/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Search multi-region lineage using client-side fan-out Stay organized with collections  Save and categorize content based on your preferences. 

Fetch data lineage links across multiple Google Cloud regions using a fan-out approach. You use the Data Lineage API to retrieve and aggregate lineage data from all available regions.

## Why use client-side fan-out?

The client-side fan-out approach is useful when your data assets are distributed across different locations and you need a unified view of their lineage.

For more information, see [About multi-region lineage search](https://docs.cloud.google.com/knowledge-catalog/docs/multi-region-lineage-overview).

## Step-by-step pseudocode

The procedure makes parallel requests to the `projects.locations.searchLinks` endpoint in each region. You collect results, handle pagination across regions, and aggregate the found links. To ensure consistent pagination for subsequent calls, manage a `regionalPageToken`. This accounts for unreachable regions.

The following pseudocode outlines a procedure you can follow using the Data Lineage API to fetch data lineage links from all available regions.

  1. Input setup: 
     * `linksToFetch` = 5 (number of links to fetch from all regions)
     * `regionalPageToken` = "" (last received regional page token used for pagination)
  2. Create: 
     1. list of all regions to fan-out called `regions`.
     2. list of unreachable regions called `unreachable`.
     3. an empty list of found links called `foundLinks`.
     4. an empty variable `nextPageToken` and `nextRegionalPageToken`.
     5. an empty variable `lastRegion`.
     6. an empty variable `lastRegionLinksCount`.
  3. Sort `regions` alphabetically.
  4. Parse `regionalPageToken`
     1. If it is empty then continue to step 5
     2. If it is not empty then 
        1. parse `regionalPageToken` by splitting it by first dot into two segments
        2. filter out regions by taking only the ones that are after (in alphabetical order) the first segment from parsed `regionalPageToken`.
        3. store the second segment aside to use it in all [projects.locations.searchLinks](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks) calls.
  5. Make a call to [projects.locations.searchLinks](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks) in each region in the `regions` list in parallel.
  6. Wait for all requests to complete.
  7. Filter out successful responses and store failed region names in the `unreachable` list.
  8. For each of the responses (starting with first region in alphabetical order) 
     1. if no links were returned along with a non empty page token 
        1. store region name in `lastRegion`.
        2. save received pageToken in `nextPageToken`.
        3. ignore the remaining responses.
     2. otherwise 
        1. store region name in `lastRegion`.
        2. save received links in `foundLinks` (up to `linksToFetch`).
        3. save received pageToken in `nextPageToken`.
        4. store number of taken links from the response in `lastRegionLinksCount`.
        5. if `foundLinks` is less than `linksToFetch`
           1. continue the pseudocode with the next received response in the alphabetical order.
        6. if `foundLinks` equals `linksToFetch`
           1. make another request to [projects.locations.searchLinks](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks) endpoint in the same region but set the `pageSize` parameter to the value of `lastRegionLinksCount`.
           2. store received pageToken in `nextPageToken`.
           3. continue to step 9
  9. Prepend `nextPageToken` with the `lastRegion` (i.e. `[region].[receivedNextPageToken]`) to create `nextRegionalPageToken` to handle pagination in consecutive calls.



## What's next

  * Learn more [about multi-region lineage search](https://docs.cloud.google.com/knowledge-catalog/docs/multi-region-lineage-overview).

  * Learn how to [search multi-region lineage using server-side automation](https://docs.cloud.google.com/knowledge-catalog/docs/search-lineage-streaming-api).

  * Learn more [about data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
