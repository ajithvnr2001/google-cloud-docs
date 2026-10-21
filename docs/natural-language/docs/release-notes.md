---
url: https://docs.cloud.google.com/natural-language/docs/release-notes/
title: Natural Language release notes \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:17:13.823478+00:00
---

# Natural Language release notes  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Resources ](https://docs.cloud.google.com/natural-language/docs/resources)



Send feedback 

#  Natural Language release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Natural Language. We recommend that Natural Language developers periodically check this list for any new announcements. Major changes will also be announced via the [cloud-nl-discuss](https://groups.google.com/forum/#!forum/cloud-nl-discuss) mailing list.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/language-release-notes.xml) directly. 

## August 28, 2023

Feature

The Natural Language API v2 is now available in [Public Preview](https://cloud.google.com/products#product-launch-stages). This new version of the API supports Sentiment Analysis, Entity Analysis, Text Moderation, and Content Classification. This version has major updates for Sentiment Analysis and Entity Analysis, which include performance upgrades and general improvements. All API calls now return `language_code` .

Change

Entity analysis uses a new PaLM-based model for improved quality. Please note the following updates:

  * **language** field is now called "language_code"
  * No **salience** field.
  * No **wikipedia_url** as metadata.
  * Parsing improvements for the following entity types: PHONE_NUMBER, ADDRESS, DATE, NUMBER, PRICE
  * New **probability** score field is returned for all entities where NUMBER, PHONE_NUMBER, ADDRESS, PRICE, DATE will always be 1.0.



Change

Sentiment analysis uses a new PaLM-based model for improved quality. The `language` field is now called `language_code`.

## January 31, 2023

Feature

Natural Language Content Classification v2 model is now [Generally Available](https://cloud.google.com/products#product-launch-stages). This model supports an expanded taxonomy with 1091 content categories and 11 languages. The model is distilled from a Large Language Model with improved performance over the v1 offering.

## October 18, 2022

Feature

Natural Language Content Classification v2 model is now in Public [Preview](https://cloud.google.com/products#product-launch-stages). This model supports an expanded taxonomy with 1091 content categories and 11 languages. The model is distilled from a Large Language Model with improved performance over the v1 offering.

## March 20, 2020

Change

The Natural Language API now supports [additional languages](https://docs.cloud.google.com/natural-language/docs/languages#sentiment_analysis) for sentiment analysis.

## February 20, 2020

Feature

The Natural Language API now offers two [multiregion endpoints](https://docs.cloud.google.com/natural-language/docs/locations) (`us-language.googleapis.com` and `eu-language.googleapis.com`). Using a multiregion endpoint enables you to configure the Natural Language API to store and perform machine learning on your data in the United States or European Union.

## May 03, 2019

Feature

The Natural Language API now supports [Spanish](https://docs.cloud.google.com/natural-language/docs/languages) for entity sentiment analysis.

## April 04, 2019

Feature

The Natural Language API now supports [Russian](https://docs.cloud.google.com/natural-language/docs/languages) for entity analysis and syntactic analysis, and Japanese for entity sentiment analysis.

Feature

The `analyzeEntities` method identifies and returns [additional entity types](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity#Type): phone numbers, addresses, dates, prices, and numbers.

## November 16, 2017

Feature

The Natural Language API has released the new `classifyText` method that analyzes text content and returns a content category for the content. For more information, see [Content Classification](https://docs.cloud.google.com/natural-language/docs/basics#content-classification).

Feature

Cloud Natural Language API version 1.2 GA release.

## September 19, 2017

Feature

The Natural Language API `v1` now supports entity sentiment analysis with the `analyzeEntitySentiment` method. Entity sentiment analysis is currently only available for the English language. For more information, see [Entity Sentiment Analysis](https://docs.cloud.google.com/natural-language/docs/basics#entity-sentiment-analysis).

Feature

The Natural Language API `v1beta2` has added beta support for a new `classifyText` method that analyzes text content and returns a content category for the content. For more information, see [Content Classification](https://docs.cloud.google.com/natural-language/docs/basics#content-classification).

## August 04, 2017

Feature

The following languages are now fully supported for entity, sentiment, and syntax analysis: * Chinese (Simplified and Traditional) * French * German * Italian * Korean * Portuguese

Change

Sentiment analysis has been updated. You might see minor differences in score and magnitude from the same request made to previous releases.

Change

Entity analysis has been updated. You might see minor differences in metadata (Wikipedia URLs, knowledge graph MIDs) of entities identified in a block of text from the same request made to the previous releases.

## May 02, 2017

Feature

Cloud Natural Language API `v1beta2` release. Added beta support for entity, sentiment, and syntax analysis for the following languages: * Chinese (Simplified and Traditional) * French * German * Italian * Korean * Portuguese

Feature

Added beta support for entity sentiment analysis (`analyzeEntitySentiment`). Entity sentiment analysis is currently only available for the English language. For more information, see [Entity Sentiment Analysis](https://docs.cloud.google.com/natural-language/docs/basics#entity-sentiment-analysis).

Change

The `v1beta2` release includes updated document sentiment analysis. You might see differing results from the same request made to the Natural Language API `v1` and `v1beta2` releases.

Change

The `v1beta2` release includes updated entity analysis. You might see minor differences in metadata (Wikipedia URLs, knowledge graph MIDs) from the same request made to the Natural Language API `v1` and `v1beta2` releases.

Deprecated

The Natural Language API `v1beta1` release has been deprecated.

## November 15, 2016

Feature

Promoted the Cloud Natural Language API from Beta (v1beta1) to General Availability (v1). Updates for v1 from the previous v1beta1 API endpoint include the features listed below.

Feature

The sentiment analysis feature has these enhancements: * Support for Japanese (`ja`) and Spanish (`es`) * Availability of [sentence level sentiment](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSentiment#response-body) * Support for [EncodingType](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/EncodingType) within a Sentiment Analysis request to calculate offsets for sentence-level sentiment *Addition of a `score` field within the [`Sentiment`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Sentiment) type to replace the previous `polarity` field

Feature

Syntactic analysis has these enhancements: * Added a new [`analyzeSyntax`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSyntax) method * Added morphology support to returned [tokens](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Token)

Feature

The entity analysis feature has these enhancements: * Added Google Knowledge Graph MID values, if available, to the [`metadata` field for each `Entity`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity) returned * Returns [Entity Mention Types](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity#type_1) for both proper nouns and common nouns (known as "nominals")

Deprecated

Removed the `polarity` field within the [`Sentiment`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Sentiment) type in favor of the new `score` field.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
