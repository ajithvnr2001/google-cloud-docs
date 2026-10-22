---
url: https://docs.cloud.google.com/blockchain-analytics/docs/release-notes/
title: Blockchain Analytics release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:46.268290+00:00
---

# Blockchain Analytics release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Resources ](https://docs.cloud.google.com/blockchain-analytics/docs/resources)



Send feedback 

#  Blockchain Analytics release notes Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page documents production updates to Blockchain Analytics. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

You can also subscribe to this page using a feed reader to get notifications of updates. What is a feed reader?

### What is a feed reader?

Really simple syndication (RSS) feed readers aggregate content from websites that you specify.

Feed reader notifications can be email-, browser-, desktop-, or mobile-based. Some readers are free, or have free versions, and some require a subscription.

A few examples:

  * [Feedly](https://feedly.com)
  * [Feedreader](https://feedreader.com)
  * [Feeder](https://feeder.co/)



More information on RSS:

  * [RSS](https://en.wikipedia.org/wiki/RSS)
  * [ Comparison of feed aggregators](https://en.wikipedia.org/wiki/Comparison_of_feed_aggregators)



Close

rss_feed Subscribe: 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/blockchain-analytics-release-notes.xml) directly. 

## January 18, 2024

Fixed

Blockchain Analytics' Ethereum Goerli nodes are synced with the network and indexing has resumed after the Dencun Hardfork.

## January 17, 2024

Issue

Users may experience data staleness with the Ethereum Goerli dataset. Goerli experienced a chain split earlier today due to the Dencun Hardfork. While the Goerli network has reached consensus, the Goerli nodes powering Blockchain Analytics data indexing have not yet synced with the network.

## December 27, 2023

Issue

On December 16, 2023, Cronos mainnet executed an [emergency hardfork](https://github.com/crypto-org-chain/cronos/releases/tag/v1.0.14) at block height `11608760`. Cronos nodes used for Blockchain Analytics have not been upgraded to use the new v1.0.14 binary. As a result, the Cronos dataset provides data up to pre-hardfork block height `11608760`.

## November 30, 2023

Deprecated

Due to ongoing system migration, the legacy Analytics Hub Listing for [Arbitrum One](https://console.cloud.google.com/bigquery/analytics-hub/exchanges/projects/938420344946/locations/us/dataExchanges/preview_google_cloud_blockchain_analytics_189b1d89e86/listings/public_preview_blockchain_analytics_arbitrum_one_chain_18add05adee?e=13863869&mods=component_inspector&project=goog-blockchain) is now deprecated and has been replaced with the [new Analytics Hub Listing](https://console.cloud.google.com/bigquery/analytics-hub/exchanges/projects/938420344946/locations/us/dataExchanges/preview_google_cloud_blockchain_analytics_189b1d89e86/listings/public_preview_blockchain_analytics_arbitrum_one_18c1d985346?e=13863869&mods=component_inspector&project=goog-blockchain).

Issue

Due to an ongoing system migration, users may experience data staleness and data absence intermittently throughout next week

## November 29, 2023

Change

We are performing a scheduled system upgrade on 11/29/2023 from 4:00PM EST to 6:00PM EST. During this upgrade, you may experience increased data staleness and data absences. We apologize for any inconvenience this may cause.

What to Expect: 

  * Data staleness may increase, causing delays in data retrieval and updates.
  * Data absences may occur, meaning that certain blockchain data may be unavailable for a period of time.



## July 17, 2023

Announcement

On July 17, 2023 we released the preview version of Blockchain Analytics. 

Blockchain Analytics offers indexed blockchain data made available through [BigQuery](https://docs.cloud.google.com/bigquery/docs) for easy analysis through SQL. Starting with [Ethereum](https://ethereum.org/en/developers/), Blockchain Analytics offers you access to reliable data without the overhead of operating nodes or developing and maintaining an indexer. 

**Documentation:** [What is Blockchain Analytics?](https://docs.cloud.google.com/blockchain-analytics/docs/overview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
