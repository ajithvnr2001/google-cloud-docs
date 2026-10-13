---
url: https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types
title: Package types (0.11.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:30.341780+00:00
---

# Package types (0.11.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.2 (latest)  0.11.1  0.10.0  0.9.0  0.8.0  0.7.18  0.6.1  0.5.1  0.4.0  0.3.2  0.2.1  0.1.2 

API documentation for `video.stitcher_v1.types` package.

## Classes 

### [AdRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.AdRequest)

Details of an ad request to an ad server.

### [AdStitchDetail](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.AdStitchDetail)

Metadata for a stitched ad.

### [AdTracking](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.AdTracking)

Determines the ad tracking policy.

### [AkamaiCdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.AkamaiCdnKey)

Configuration for an Akamai CDN key.

### [CdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CdnKey)

Configuration for a CDN key. Used by the Video Stitcher to sign URIs for fetching video manifests and signing media segments for playback.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Companion](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.Companion)

Metadata for a companion.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CompanionAds](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CompanionAds)

Metadata for companion ads.

### [CreateCdnKeyRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CreateCdnKeyRequest)

Request message for VideoStitcherService.createCdnKey.

### [CreateLiveConfigRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CreateLiveConfigRequest)

Request message for VideoStitcherService.createLiveConfig

### [CreateLiveSessionRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CreateLiveSessionRequest)

Request message for VideoStitcherService.createLiveSession.

### [CreateSlateRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CreateSlateRequest)

Request message for VideoStitcherService.createSlate.

### [CreateVodConfigRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CreateVodConfigRequest)

Request message for VideoStitcherService.createVodConfig

### [CreateVodSessionRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CreateVodSessionRequest)

Request message for VideoStitcherService.createVodSession

### [DeleteCdnKeyRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.DeleteCdnKeyRequest)

Request message for VideoStitcherService.deleteCdnKey.

### [DeleteLiveConfigRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.DeleteLiveConfigRequest)

Request message for VideoStitcherService.deleteLiveConfig.

### [DeleteSlateRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.DeleteSlateRequest)

Request message for VideoStitcherService.deleteSlate.

### [DeleteVodConfigRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.DeleteVodConfigRequest)

Request message for VideoStitcherService.deleteVodConfig.

### [Event](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.Event)

Describes an event and a trigger URI.

### [FetchOptions](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.FetchOptions)

Options on how fetches should be made.

### [GamLiveConfig](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GamLiveConfig)

Metadata used to register a live stream with Google Ad Manager (GAM)

### [GamVodConfig](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GamVodConfig)

Metadata used for GAM ad decisioning.

### [GetCdnKeyRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GetCdnKeyRequest)

Request message for VideoStitcherService.getCdnKey.

### [GetLiveAdTagDetailRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GetLiveAdTagDetailRequest)

Request message for VideoStitcherService.getLiveAdTagDetail

### [GetLiveConfigRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GetLiveConfigRequest)

Request message for VideoStitcherService.getLiveConfig.

### [GetLiveSessionRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GetLiveSessionRequest)

Request message for VideoStitcherService.getSession.

### [GetSlateRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GetSlateRequest)

Request message for VideoStitcherService.getSlate.

### [GetVodAdTagDetailRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GetVodAdTagDetailRequest)

Request message for VideoStitcherService.getVodAdTagDetail

### [GetVodConfigRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GetVodConfigRequest)

Request message for VideoStitcherService.getVodConfig.

### [GetVodSessionRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GetVodSessionRequest)

Request message for VideoStitcherService.getVodSession

### [GetVodStitchDetailRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GetVodStitchDetailRequest)

Request message for VideoStitcherService.getVodStitchDetail.

### [GoogleCdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GoogleCdnKey)

Configuration for a Google Cloud CDN key.

### [HtmlAdResource](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.HtmlAdResource)

Metadata for an HTML ad resource.

### [IframeAdResource](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.IframeAdResource)

Metadata for an IFrame ad resource.

### [Interstitials](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.Interstitials)

Describes what was stitched into a VOD session's manifest.

### [ListCdnKeysRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListCdnKeysRequest)

Request message for VideoStitcherService.listCdnKeys.

### [ListCdnKeysResponse](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListCdnKeysResponse)

Response message for VideoStitcher.ListCdnKeys.

### [ListLiveAdTagDetailsRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsRequest)

Request message for VideoStitcherService.listLiveAdTagDetails.

### [ListLiveAdTagDetailsResponse](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsResponse)

Response message for VideoStitcherService.listLiveAdTagDetails.

### [ListLiveConfigsRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListLiveConfigsRequest)

Request message for VideoStitcherService.listLiveConfig.

### [ListLiveConfigsResponse](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListLiveConfigsResponse)

Response message for VideoStitcher.ListLiveConfig.

### [ListSlatesRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListSlatesRequest)

Request message for VideoStitcherService.listSlates.

### [ListSlatesResponse](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListSlatesResponse)

Response message for VideoStitcherService.listSlates.

### [ListVodAdTagDetailsRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsRequest)

Request message for VideoStitcherService.listVodAdTagDetails.

### [ListVodAdTagDetailsResponse](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsResponse)

Response message for VideoStitcherService.listVodAdTagDetails.

### [ListVodConfigsRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListVodConfigsRequest)

Request message for VideoStitcherService.listVodConfig.

### [ListVodConfigsResponse](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListVodConfigsResponse)

Response message for VideoStitcher.ListVodConfig.

### [ListVodStitchDetailsRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListVodStitchDetailsRequest)

Request message for VideoStitcherService.listVodStitchDetails.

### [ListVodStitchDetailsResponse](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ListVodStitchDetailsResponse)

Response message for VideoStitcherService.listVodStitchDetails.

### [LiveAdTagDetail](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.LiveAdTagDetail)

Information related to the details for one ad tag. This resource is only available for live sessions that do not implement Google Ad Manager ad insertion.

### [LiveConfig](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.LiveConfig)

Metadata for used to register live configs.

### [LiveSession](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.LiveSession)

Metadata for a live session. The session expires 5 minutes after the client stops fetching the session's playlists.

### [ManifestOptions](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ManifestOptions)

Options for manifest generation.

### [MediaCdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.MediaCdnKey)

Configuration for a Media CDN key.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [PrefetchConfig](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.PrefetchConfig)

The configuration for prefetch ads.

### [ProgressEvent](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ProgressEvent)

Indicates a time in which a list of events should be triggered during media playback.

### [RenditionFilter](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.RenditionFilter)

Filters for a video or muxed redition.

### [RequestMetadata](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.RequestMetadata)

Metadata for an ad request.

### [ResponseMetadata](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.ResponseMetadata)

Metadata for the response of an ad request.

### [Slate](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.Slate)

Slate object

### [StaticAdResource](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.StaticAdResource)

Metadata for a static ad resource.

### [UpdateCdnKeyRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.UpdateCdnKeyRequest)

Request message for VideoStitcherService.updateCdnKey.

### [UpdateLiveConfigRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.UpdateLiveConfigRequest)

Request message for VideoStitcherService.updateLiveConfig.

### [UpdateSlateRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.UpdateSlateRequest)

Request message for VideoStitcherService.updateSlate.

### [UpdateVodConfigRequest](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.UpdateVodConfigRequest)

Request message for VideoStitcherService.updateVodConfig.

### [VodAdTagDetail](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.VodAdTagDetail)

Information related to the details for one ad tag. This resource is only available for VOD sessions that do not implement Google Ad Manager ad insertion.

### [VodConfig](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.VodConfig)

Metadata used to register VOD configs.

### [VodSession](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.VodSession)

Metadata for a VOD session. The session expires 4 hours after its creation.

### [VodSessionAd](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.VodSessionAd)

Metadata for an inserted ad in a VOD session.

### [VodSessionAdBreak](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.VodSessionAdBreak)

Metadata for an inserted ad break.

### [VodSessionContent](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.VodSessionContent)

Metadata for the entire stitched content in a VOD session.

### [VodStitchDetail](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.VodStitchDetail)

Information related to the interstitial of a VOD session. This resource is only available for VOD sessions that do not implement Google Ad Manager ad insertion.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
