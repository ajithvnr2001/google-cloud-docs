---
url: https://docs.cloud.google.com/video-stitcher/docs/release-notes/
title: Video Stitcher API release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:10.970921+00:00
---

# Video Stitcher API release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/release-notes/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Resources ](https://docs.cloud.google.com/video-stitcher/docs/resources)



Send feedback 

#  Video Stitcher API release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to the Video Stitcher API. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/video-stitcher-release-notes.xml) directly. 

## April 22, 2024

Change

[VOD configs](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs) are now used to [create VOD sessions](https://docs.cloud.google.com/video-stitcher/docs/how-to/creating-vod-sessions). When you create a VOD session, specify a VOD config in the [`vodConfig`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#VodSession.FIELDS.vod_config) field to use the config's `sourceUri` and `adTagUri` fields.

## March 28, 2024

Change

Added a new [`tokenConfig`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.cdnKeys#MediaCdnKey.FIELDS.token_config) field to the Media CDN key. Set this field to sign the URL using the Media CDN token.

## June 27, 2023

Change

The Video Stitcher API now requires that a live stream source manifest references at least one valid segment file. The manifest is specified in the live config's `sourceUri` field.

## April 26, 2023

Announcement

Google Ad Manager integration for [live](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/overview) and [VOD](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/overview) workflows is now generally available (GA). To enable this integration in your project, please reach out to your Account Representative or contact [Sales](https://docs.cloud.google.com/contact) to learn more.

Breaking

[Live configs](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-configs) are now used to [create live sessions](https://docs.cloud.google.com/video-stitcher/docs/how-to/creating-live-sessions).

## March 21, 2023

Breaking

[Slates](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-slates) and [CDN keys](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys) are now created using [long-running operations](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations).

## February 14, 2023

Feature

Video Stitcher API can now insert ads served by Google Ad Manager (GAM) into [live streams](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/overview) and [VOD assets](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/overview).

## September 30, 2022

Feature

The Video Stitcher API now supports CDN keys created for [Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview). See [Create and manage CDN keys](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys) for more information.

## June 15, 2022

Announcement

The Video Stitcher API is generally available (GA).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
