---
url: https://docs.cloud.google.com/video-intelligence/docs/release-notes/
title: Video Intelligence release notes \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:57.251056+00:00
---

# Video Intelligence release notes  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/release-notes/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Resources ](https://docs.cloud.google.com/video-intelligence/docs/resources)



Send feedback 

#  Video Intelligence release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Video Intelligence. We recommend that Video Intelligence developers periodically check this list for any new announcements. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/video-release-notes.xml) directly. 

## October 15, 2026

Deprecated

We are deprecating the emotion label response in the API. Going forward, the API will return `UNKNOWN` for all emotion related labels.

## November 01, 2021

Feature

**AutoML Action Recognition** : The Streaming API is a Beta feature of Video Intelligence API for real-time versions of several capabilities such as object tracking and label detection. This current launch adds streaming support for AutoML Action Recognition models. Customers can now specify their own custom AutoML model when performing [action recognition](https://docs.cloud.google.com/video-intelligence/docs/streaming/action-recognition) on a stream.

## October 08, 2021

Change

The SHOT_CHANGE_DETECTION model will undergo an upgrade over the next 90 days to a newer version. The API interface and client library will remain the same as the previous version.

Note that you have 30 days from today to test the new model by specifying "builtin/latest" in the model field of the config object for shot change detection. At the end of 30 days, the new model will be promoted to the default model accessible as "builtin/stable". After that event, the original model, currently accessible by default or using "builtin/stable" will still be available for another 60 days using "builtin/legacy".

Until this 30 day period ends, the model formerly accessible as "builtin/latest" will be available as "builtin/legacy". Thank you for your feedback on that model, now labeled "builtin/legacy" version. The new model launched today as "builtin/latest" has been improved over this model as well as the current default "builtin/stable" model.

If you encounter problems with this upgrade, contact the Video Intelligence API engineering team by submitting a ticket in the [private issue tracker](https://issuetracker.google.com/issues/new?component=190865&template=1161103&pli=1).

## September 20, 2021

Change

The CELEBRITY_RECOGNITION model will undergo an upgrade to a newer version over the next 90 days. The API interface and client library will remain same as the previous version. The API follows the same Service Level Agreement (SLA). You have 30 days from this release date to test the new model. To do so, specify "builtin/latest" in the model field of the Feature object while requesting image annotation. After the end of this 30-day period, the new version will be promoted to the default model and accessible as "builtin/stable". Going forward, the original model will still be available for another 60 days using "builtin/legacy". If you encounter problems with this upgrade, contact the Video Intelligence API engineering team by submitting a ticket in the private issue tracker.

## May 04, 2021

Feature

The following features are available in the Video Intelligence API version v1:

**Face detection** : Locate faces within a video, and identify attributes such as glasses being worn. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/face-detection)

**Person detection** : Locate people in a video, and identify attributes and 2D landmarks. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/people-detection)

This GA launch brings significant quality improvement to both features.

## September 14, 2020

Issue

Bug fix for shot change detection API: Tuned internal model parameters to reduce false positives under certain scenarios.

## May 21, 2020

Feature

The following features are available in the Video Intelligence API version v1p3beta1:

**Face detection** : Locate faces within a video, and identify attributes such as glasses being worn. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/face-detection)

**Person detection** : Locate people in a video, and identify attributes and 2D landmarks. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/people-detection)

## March 31, 2020

Feature

The following GA feature is available in the Video Intelligence API version v1:

**Logo recognition** : Detect, track, and recognize the presence of over 100,000 brands and logos in video content. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/logo-recognition)

## October 30, 2019

Feature

Cloud Video Intelligence now offers [celebrity recognition](https://docs.cloud.google.com/video-intelligence/docs/celebrity-recognition) to select media & entertainment companies and their designated partners. With celebrity recognition, you can inspect your video content to detect and track human faces that appear in the input video or video segment. The Video Intelligence API then compares the faces against a database of celebrities. This feature is in beta; access to the feature is restricted.

## October 04, 2019

Feature

Logo recognition is now available as a beta feature. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/logo-recognition).

## September 17, 2019

Feature

You can now specify which model you want to use with [`LABEL_DETECTION`](https://docs.cloud.google.com/video-intelligence/docs/analyze-labels) and [`SHOT_CHANGE`](https://docs.cloud.google.com/video-intelligence/docs/analyze-shots). To specify a model using the v1 version of the service, set the `model` field of the [`LabelDetectionConfig`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#labeldetectionconfig) or [`ShotChangeDetectionConfig`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#shotchangedetectionconfig) to either `builtin/stable` or `builtin/latest`.

Feature

You can now specify your own custom AutoML model when performing [label detection](https://docs.cloud.google.com/video-intelligence/docs/streaming/label-analysis) or [object tracking](https://docs.cloud.google.com/video-intelligence/docs/streaming/object-tracking) on a stream. This feature is in beta.

Feature

Cloud Video Intelligence rolled out improved models for video annotation using the [`OBJECT_TRACKING`](https://docs.cloud.google.com/video-intelligence/docs/object-tracking) and [`TEXT_DETECTION`](https://docs.cloud.google.com/video-intelligence/docs/text-detection) with the v1 version of the service.

## June 26, 2019

Change

Results returned from asynchronous annotation now provide resource names in the following format `project/PROJECT_NAME/location/us-west1/operation/OPERATION_ID`.

## April 10, 2019

Feature

Live streaming video annotation is available as a beta feature. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/streaming/live-streaming-overview).

Feature

Object tracking is generally available for use. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/object-tracking).

Feature

Streaming from a file is available as a beta feature. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/streaming/streaming).

Feature

Text detection (OCR) is generally available for use. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/text-detection).

## December 07, 2018

Feature

The Video Intelligence API enables you to transcribe text from speech in the audio of a video. Speech transcription can recognize multiple speakers, filter out profanity, add punctuation to the transcribed text, and more. For more information, see [Speech Transcription](https://docs.cloud.google.com/video-intelligence/docs/transcription). This feature is generally available.

## October 26, 2018

Feature

Cloud Video Intelligence allows you to [track an object](https://docs.cloud.google.com/video-intelligence/docs/object-tracking) from one moment to the next in a video. This feature is in beta.

Feature

You can use the Video Intelligence API to [detect text (OCR)](https://docs.cloud.google.com/video-intelligence/docs/text-detection) in a video. This feature is in beta.

## August 08, 2018

Feature

Speech transcription is available as a beta feature. [Learn more](https://docs.cloud.google.com/video-intelligence/docs/transcription).

## June 27, 2018

Change

An improved label detection model is now available. The new model:

  * Leverages audio content in videos to improve label detection.
  * Is trained using more features and better calibration ground truth.



To instruct the Cloud Video Intelligence API to use the new label detection model when servicing your annotation request, set the `model` field of your [`LabelDetectionConfig`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#labeldetectionconfig) to `builtin/latest`. 

We'll support both the current model and the new model the next 90 days. After 90 days the current label detection model will be deprecated and only the new label detection model will be used for all label detection requests.

## November 30, 2017

Change

**Video Intelligence API is GA** : The Video Intelligence API has graduated out of beta and has reached v1. All API endpoints are updated to use `https://videointelligence.googleapis.com/v1/`.

## September 21, 2017

Change

**Explicit content detection** : SafeSearch has been renamed to Explicit Content Detection. Explicit Content Detection inspects an input video for frame-level imagery that could be considered adult content.

Explicit Content Detection is performed by using the [annotate](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method and specifying an [EXPLICIT_CONTENT_DETECTION](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#Feature) request.

Change

The [`ExplicitContentAnnotation`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/Shared.Types/AnnotateVideoResponse#ExplicitContentAnnotation) and [`ExplicitContentFrame`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/Shared.Types/AnnotateVideoResponse#ExplicitContentFrame) types replace the `SafeSearchAnnotation` type. The `adult` field has been renamed to `pornographyLikelihood` and the `time` field has been renamed to `timeOffset`. The `spoof`, `medical`, `violent`, and `racy` fields have also been removed. The `timeOffset` field returns a value of type `Duration` instead of type `int64`.

Change

The `labelAnnotations` field returned in the response for a video annotation request has been replaced with the `segmentLabelAnnotations`, `shotLabelAnnotations`, and `frameLabelAnnotations` fields. This provides specific label annotations for each level of the video. The `LabelLevel` enum has been removed.

All annotations have been updated to return an array of [`LabelFrame`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/Shared.Types/AnnotateVideoResponse#labelframe) types, an array of [`LabelSegment`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/Shared.Types/AnnotateVideoResponse#LabelSegment) types, a list of entities, and a list of entity categories. Each `LabelFrame` and `LabelSegment` includes a confidence value.

The field description has been replaced with an [`Entity`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/Shared.Types/AnnotateVideoResponse#entity) type, which includes both the `description` and an `entity_id` field. You can use the entity id to find more information for some entities in the [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).

The [`LabelDetectionMode`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#LabelDetectionMode) enum remains unchanged and can be set as the `label_detection_mode` field of the [`LabelDetectionConfig`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#LabelDetectionConfig) for your request, along with the `stationary_camera` field. This configurations applies only to labels. Other video intelligence features do not yet have yet any feature-specific configuration options.

Change

The [`VideoSegment`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/Shared.Types/AnnotateVideoResponse#VideoSegment) type is now used only in the context configuration ([`VideoContext`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#VideoContext)) of the [`AnnotateVideoRequest`](https://docs.cloud.google.com/video-intelligence/docs/reference/rpc/google.cloud.videointelligence.v1#google.cloud.videointelligence.v1.AnnotateVideoRequest) type to allow you to pass multiple video segments in a request.

## June 26, 2017

Feature

**SafeSearch detection** : SafeSearch inspects an input video for frame-level imagery that could be considered adult content.

SafeSearch is performed through the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#Feature) method using a [`SAFE_SEARCH_DETECTION`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) request.

## May 18, 2017

Feature

Cloud Video Intelligence API is available for beta.

Feature

**Label detection** : Label detection inspects an input video and detects entities that occur throughout the length of the video or video segment. Label detection is performed through the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method using a [`LABEL_DETECTION`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#Feature) request.

Feature

**Shot change detection** : Shot detection inspects an input video, and detects changes in shots (scenes) that occur throughout the length of the video or video segment. Shot detection is performed through the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method using a [`SHOT_CHANGE_DETECTION`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#Feature) request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
