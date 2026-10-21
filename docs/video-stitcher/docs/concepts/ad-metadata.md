---
url: https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-metadata/
title: Ad metadata \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:57.854602+00:00
---

# Ad metadata  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-metadata/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Ad metadata Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes the supported ad metadata feature of the Video Stitcher API. Ad metadata is extracted from a VAST ad in an ad tag response, containing ad tracking events and companion ads. The ad tag url is configured in the session creation request. For more information, see [Manage a live session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions) and [Manage a VOD session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions).

## Before you begin

Make sure you are familiar with the introductory concepts and terminology in the Video Stitcher API. For more information, see the technical [overview](https://docs.cloud.google.com/video-stitcher/docs/concepts/overview).

## Introduction

Ad metadata contains ad tracking events and companion ads associated with a stitched ad. An ad tracking event contains a callback ping used to track the VAST ad and viewer interaction. A companion ad is an ad to supplement the parent VAST ad. In client-side tracking mode, you are responsible to trigger events based on the viewer's behavior.

## Server-side ad tracking

In server-side tracking mode, each ad segment URI is wrapped in a redirect URI and the Video Stitcher API will handle the processing of progress events whenever the player requests those segments. However, activity events, such as `pause`, are not handled by the Video Stitcher API.

## Client-side ad tracking

In client-side tracking mode, the client is responsible for triggering the events. For more details, see the [event documentation](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Event).

Progress events are events that should be triggered when the specified time has elapsed during the ad. For example, event `Start` should be triggered at the beginning of the ad. For more details about progress events, see the [progress event object](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/ProgressEvent).

Activity events are events that should be triggered when a viewer conducts a specific activity. For example, event `pause` should be triggered when the viewer pauses the ad video. For more details about activity events, see the [activity event object](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Event).

### VOD client-side ad tracking

An interstitials object is returned in the response of a VOD session create request. For instruction on how to create a VOD session, see how to [create a VOD session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions#create-session).

Interstitials contains the metadata for each inserted ad. When client ad tracking mode is enabled, the client is responsible for triggering tracking events when necessary. For more details, see the [interstitials object](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Interstitials).

### Live client-side ad tracking

The Video Stitcher API continuously inserts ads into a livestream; ad metadata information is generated whenever a new ad is inserted.

For HLS, the `AdMetadataURI` to fetch ad metadata can be found in the `#EXT-X-DATERANGE` tag.

For DASH, the `AdMetadataURI` to fetch ad metadata can be found in the `<EventStream>` element for each `<Period>` element.

For more details, see [how to handle live client-side tracking](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions#handle-client-side-ad-tracking).

## Companion ads

Companion ads are supplemental ads that may appear along with inserted linear ads. For more details, see the [companion ads object](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/CompanionAds).

## What's next

  * Learn how to complete specific [Video Stitcher API tasks](https://docs.cloud.google.com/video-stitcher/docs/how-to).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
