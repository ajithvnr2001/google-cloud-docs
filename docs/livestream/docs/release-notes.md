---
url: https://docs.cloud.google.com/livestream/docs/release-notes/
title: Live Stream API release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:04.541751+00:00
---

# Live Stream API release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Resources ](https://docs.cloud.google.com/livestream/docs/resources)



Send feedback 

#  Live Stream API release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Live Stream API. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/livestream-release-notes.xml) directly. 

## September 01, 2025

Feature

You can now [distribute live stream content to remote endpoints](https://docs.cloud.google.com/livestream/docs/how-to/distribute-live-streams) by using the Secure Reliable Transport (SRT) protocol or the Real-Time Messaging Protocol (RTMP).

Feature

You can now [create AI-generated captions and translated captions](https://docs.cloud.google.com/livestream/docs/how-to/configure-captions-and-translations) for a live stream.

Feature

Added support for [H.265 (HEVC) inputs and outputs](https://docs.cloud.google.com/livestream/docs/how-to/create-channels#create_channel_h265), which allows for more efficient compression.

Feature

Added support for UHD (4K) inputs and outputs.

Feature

You can now update the encryption key of your encrypted live stream contents while the channel is running.

Feature

You can now generate Web Video Text Tracks format (WebVTT) subtitles from cea608 or cea708 embedded captions in the input stream.

Feature

You can now preview your input streams with ultra-low latency, which allows you to take corrective actions and maintain high-quality viewing experience for your viewers.

## November 18, 2024

Feature

You can now [create a DVR session](https://docs.cloud.google.com/livestream/docs/how-to/create-dvr-session) for a past, current, or future live stream.

## November 08, 2024

Announcement

The Live Stream API is now available in `asia-south1` and `europe-north1`. For more information, see [Live Stream API locations](https://docs.cloud.google.com/livestream/docs/locations).

## August 16, 2024

Feature

You can now [create static overlays](https://docs.cloud.google.com/livestream/docs/how-to/create-overlays) and position them on top of a live stream.

## May 29, 2024

Feature

You can now [create video on demand (VOD) clips from a live stream](https://docs.cloud.google.com/livestream/docs/how-to/live-to-vod).

## July 31, 2023

Feature

[Slates](https://docs.cloud.google.com/livestream/docs/how-to/insert-slate) are now supported. Slates are video or image content that can replace the main live stream content whenever you want (for example, if you are experiencing technical issues on the input stream).

## June 20, 2023

Feature

You can now use VPC Service Controls to [secure your live streams](https://cloud.google.com/livestream/docs/how-to/vpc/secure-pipeline).

## February 21, 2023

Feature

Added [content encryption](https://docs.cloud.google.com/livestream/docs/how-to/encrypt-content) support

Feature

Added new channel events: [mute](https://docs.cloud.google.com/livestream/docs/how-to/create-channel-events#mute-event), [unmute](https://docs.cloud.google.com/livestream/docs/how-to/create-channel-events#unmute-event), [return to program](https://docs.cloud.google.com/livestream/docs/how-to/create-channel-events#return-to-program-event), and [switch input](https://docs.cloud.google.com/livestream/docs/how-to/create-channel-events#switch-input-event)

Feature

Added the [timecode feature](https://docs.cloud.google.com/livestream/docs/how-to/use-timecode) which supports synchronizing media workflows with live stream content

Feature

Added [audio loudness normalization](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#audio) and [audio gain control](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#AudioMapping.FIELDS.gain_db)

## June 13, 2022

Announcement

[Live Stream API](https://docs.cloud.google.com/livestream/docs) is now in GA.

Change

[Pricing](https://cloud.google.com/livestream/pricing) is now regional. See [Locations](https://docs.cloud.google.com/livestream/docs/locations) for available regions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
