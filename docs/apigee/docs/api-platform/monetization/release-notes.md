---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/release-notes/
title: Apigee Monetization release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:27.897089+00:00
---

# Apigee Monetization release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee Monetization release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Apigee Monetization in 2022 and later. We recommend that users periodically check this list for any new announcements, or subscribe to this page using a feed reader to get notifications of updates. What is a feed reader?

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

  
See also:   


  * [2021 and prior Release notes](https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes)
  * [Known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)

  
rss_feed Subscribe: 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/apigee-monetization-release-notes.xml) directly. 

## December 19, 2025

Announcement

On December 19, 2025, we released an updated version of Apigee Monetization.

**Note:** Rollouts of this release to production instances have begun. Rollout may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

Monetization now supports AppGroups. Use AppGroups to manage API product subscriptions for all app developers in the AppGroup at the same time.

For more information, see [Use AppGroups to manage API product subscriptions](https://cloud.google.com/apigee/docs/api-platform/monetization/overview#use-appgroups-to-manage-api-product-subscriptions).

## July 26, 2024

Announcement

On July 26, 2024, we released an updated version of Apigee Monetization.

Feature

Monetization functionality, including rate plan creation and managing rate plans for API Products, is now available in the Apigee UI in Cloud Console.

For information, see [Manage Rate Plans](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-rate-plans) and [Create API Products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products).

Feature

Monetization now supports data residency. Data residency meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Monetization data is stored. For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

## November 14, 2022

Announcement

On November 14, 2022 we released an updated version of the Apigee Monetization software.

Feature

**Added support for a new recurring fees**

Apigee X now supports optional recurring fees charged to API developers. For more information on fees, see [Understanding billing](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview#understanding-billing).

## November 10, 2022

Announcement

On November 10, 2022 we released an updated version of the Apigee Monetization software.

Feature

**Added support for a new setup fee**

Apigee X now supports an optional setup fee charged to new API developers. For more information on fees, see [Understanding billing](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview#understanding-billing).

## May 18, 2022

Announcement

On May 18, 2022 we released an updated version of the Apigee Monetization software.

Feature

**Export support for additional monetization-related values**

Apigee X now supports export of additional fee-based values for organizations using monetization. For more information, see [Generating monetization reports](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/generate-reports).

## November 03, 2021

Announcement

On November 3, 2021 we released an updated version of the Apigee Monetization software.

Feature

**Volume banded consumption pricing**

[Rate plan](https://docs.cloud.google.com/apigee/docs-preview/api-platform/monetization/manage-rate-plans#create) supports the new **Banded** type of consumption based fees. You can configure variable fees for each monetized transaction based on a band. A band refers to an API consumption range, and you can configure a different fee for each band.

Feature

**Revenue sharing with developers**

The revenue sharing feature enables developers to receive a percentage of the total revenue generated. As an API provider, you can configure **Revenue share** in your [rate plan](https://docs.cloud.google.com/apigee/docs-preview/api-platform/monetization/manage-rate-plans#create) to share a specific percentage of the revenue with your developer partners.

Deprecated

**The`rateplans` API doesn't support the `paymentFundingModel` field.**

Feature

**Criteria for successful transaction**

You can specify if a transaction must be monetized or not by configuring the [transactionSuccess](https://docs.cloud.google.com/apigee/docs-preview/api-platform/reference/policies/data-capture-policy#mint-var) monetization variable in your DataCapture policy.

Feature

**DataCapture policy captures monetization variables**

You can configure the DataCapture policy to capture a transaction's monetization information such as revenue, currency, price multiplier, and status. For more information, see [Monetization variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy#datacollector).

Feature

**Prepaid billing**

Apigee now supports the prepaid billing of developers, as well as postpaid billing. In prepaid billing, app developers pay in advance even before using your API products. The upfront payment made by the developers is available in the developer's wallet, which can have different currencies. You can track a developer's balance in real time and block API calls if a developer has insufficient funds.

Feature

**Dynamic consumption pricing**

To calculate the cost of a transaction, you can specify a multiplier ([perUnitPriceMultiplier](https://docs.cloud.google.com/apigee/docs-preview/api-platform/reference/policies/data-capture-policy#mint-var)) value on top of the pre-configured base price in your DataCapture policy.

Fixed

Bug ID | Description  
---|---  
**199807323** | **A prepaid developer is set as a postpaid developer after updates to the prepaid developer.**  
**198549304, 197730687, 196937143, 188370635, 187890034** | **Apigee displays improved error messages during rate plan creation.**  
**192987085** | **Fixed the ApiProductNotFound exception, which occurred when you deleted an API product but the deletion of associated rate plans was pending.**  
**188407113** | **Invalid value in the`ConsumptionPricingType` during rate plan creation displayed the `500` status code. Now the status code for an invalid value is `4xx`.**  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
