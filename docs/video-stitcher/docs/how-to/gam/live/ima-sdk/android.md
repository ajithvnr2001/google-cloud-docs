---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/android/
title: Use the IMA DAI SDK on Android \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:04.811258+00:00
---

# Use the IMA DAI SDK on Android  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/android/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Use the IMA DAI SDK on Android Stay organized with collections  Save and categorize content based on your preferences. 

## Play livestreams registered with Google Cloud Video Stitcher API

This guide demonstrates how to use the IMA DAI SDK for Android to request and play a livestream for an event registered with the [Google Cloud Video Stitcher API](https://cloud.google.com/video-stitcher/docs/how-to/gam/live/overview), and how to insert an ad break during playback. 

This guide expands on the basic example from the [Get started guide](https://developers.google.com/interactive-media-ads/docs/sdks/android/dai) for IMA DAI.

For information on integrating with other platforms or on using the IMA client-side SDKs, see [Interactive Media Ads SDKs](https://developers.google.com/interactive-media-ads).

If you would like to view or follow along with a completed sample integration, download the [Cloud video stitcher example](https://github.com/googleads/googleads-ima-android-dai/tree/main/CloudVideoStitcherExample).

**Note:** The IMA DAI SDK for Android supports both HLS and DASH streams. 

This guide explains how to configure exoplayer and IMA DAI SDK to play an HLS stream. For an example of a video player supporting both HLS and DASH streams, see our [Advanced Example](https://github.com/googleads/googleads-ima-android-dai/blob/main/AdvancedExample/app/src/main/java/com/google/ads/interactivemedia/v3/samples/samplevideoplayer/SampleVideoPlayer.java#L151-L166). 

## Set up a Google Cloud project

Enter the following variables for use in the IMA SDK:

Location
    The [Google Cloud region](https://cloud.google.com/video-stitcher/docs/locations) where your live config was created: `LOCATION`
Project number
    The Google Cloud project number using the Video Stitcher API: `PROJECT_NUMBER`
OAuth token
    

A service account's short lived OAuth token with the Video Stitcher user role: 
    
    
    OAUTH_TOKEN

    

Read more about [creating short-lived credentials for service accounts](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials). The OAuth token can be reused across multiple requests as long as it has not expired.

Network code
    

The Ad Manager network code for requesting ads: `NETWORK_CODE`

Live config ID
    The live config ID you specified when creating your livestream event: `LIVE_CONFIG_ID`
Custom asset key
    The Ad Manager custom asset key generated during the process of [creating a configuration for a livestream event](https://cloud.google.com/video-stitcher/docs/how-to/gam/live/create-live-configs) with the Video Stitcher API: `CUSTOM_ASSET_KEY`

## Download the basic example

Download and run the [IMA Android DAI Basic Example](https://github.com/googleads/googleads-ima-android-dai/releases). Click the **play** button on the video player to start the short film "Tears of Steel", which contains ad breaks every 30 seconds.

**Important:** It's important for your app to send ID3 events using [`VideoStreamPlayerCallback.onUserTextReceived()`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/android/api/reference/com/google/ads/interactivemedia/v3/api/player/VideoStreamPlayer.VideoStreamPlayerCallback.html#public-abstract-void-onusertextreceived-string-usertext) for IMA DAI to function. See this [Full service DAI code snippet example](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/android?service=full#videoplayerappsampleadswrapperjava_2).

## Request a livestream

To replace the sample stream with your livestream, you need to use the [`ImaSdkFactory.createVideoStitcherLiveStreamRequest()`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/android/api/reference/com/google/ads/interactivemedia/v3/api/ImaSdkFactoryhtml#createVideoStitcherLiveStreamRequest\(java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String\)) to create an ad session with Google Ad Manager. You can use the Google Ad Manager UI to [locate the generated DAI sessions](https://support.google.com/admanager/answer/7257678) for monitoring and debugging purposes.

In the existing sample, there are conditional statements for requesting a VOD stream or a livestream. To make it work with Google Cloud Video Stitcher API, you need to add a new path to return a `StreamRequest` created using [`ImaSdkFactory.createVideoStitcherLiveStreamRequest()`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/android/api/reference/com/google/ads/interactivemedia/v3/api/ImaSdkFactoryhtml#createVideoStitcherLiveStreamRequest\(java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String\)).

Here's an example:

#### videoplayerapp/SampleAdsWrapper.java
    
    
    private sdkFactory ImaSdkFactory;
    ...
    private enum ContentType {
      LIVE_HLS,
      LIVE_DASH,
    // Add a Live HLS Google Cloud type.
      **LIVE_HLS_GOOGLE_CLOUD ,**
      VOD_HLS,
      VOD_DASH,
    }
    
    // Set CONTENT_TYPE to the associated enum for the
    // stream type you would like to test.
    **private static final ContentType CONTENT_TYPE =
        ContentType.LIVE_HLS_GOOGLE_CLOUD;**
    ...
    
    @Nullable
      private StreamRequest buildStreamRequest() {
        StreamRequest request;
        switch (CONTENT_TYPE) {
          ...
          **case LIVE_HLS_GOOGLE_CLOUD:
            // Live HLS stream generated by the Google Cloud Video Stitcher API.
            request = sdkFactory.createVideoStitcherLiveStreamRequest(
              "NETWORK_CODE",
              "CUSTOM_ASSET_KEY",
              "LIVE_CONFIG_ID",
              "LOCATION",
              "PROJECT_NUMBER",
              "OAUTH_TOKEN"
            );
            request.setFormat(StreamFormat.HLS);
            return request;
        }
        // Content type not selected.
        return null;**
      }
    ...
    

Reload the app to request and play your custom livestream.

### (Optional) Add streaming session options

Customize your stream request by adding session options to override the default Cloud Video Stitcher API configuration using [`StreamRequest.setVideoStitcherSessionOptions()`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/android/api/reference/com/google/ads/interactivemedia/v3/api/StreamRequest.html#public-abstract-void-setvideostitchersessionoptions-mapstring,-object-videostitchersessionoptions). If you provide an unrecognized option, the Cloud Video Stitcher API will respond with an HTTP 400 error. Consult the [troubleshooting guide](https://cloud.google.com/video-stitcher/docs/troubleshooting) for assistance.

For example, you can override the [manifest options](https://cloud.google.com/video-stitcher/docs/concepts/manifest-options) with the following code snippet, which requests two stream manifests with renditions ordered from lowest bitrate to highest.
    
    
    public void requestAndPlayAds() {
      adsLoader.addAdErrorListener(this);
      adsLoader.addAdsLoadedListener(this);
      **StreamRequest streamRequest = buildStreamRequest();
    
      // The following session options are examples. Use session options
      // that are compatible with your video stream.
      Map<String, Object> sessionOptions = Map.of(
        "manifestOptions", Map.of(
          "bitrateOrder", "ascending"
        )
      );
    
      /* sessionOptions JSON structure.
       * {
       *  "manifestOptions": {
       *    "bitrateOrder": "ascending"
       *  }
       * };
       */
    
      streamRequest.setVideoStitcherSessionOptions(sessionOptions);
      adsLoader.requestStream(streamRequest);**
    }
    

## Insert an ad break

The Google Cloud Video Stitcher API inserts ads retrieved from the ad tag for each ad break. Ad breaks are denoted in the manifest using ad markers. Ad markers are inserted by the live stream encoder.

  * If you are using your own live stream, you need to insert the ad marker. For more information on the supported HLS and DASH ad markers, see the [ad markers documentation](https://cloud.google.com/video-stitcher/docs/concepts/ad-markers).

  * If you created a live stream using the Google Cloud Livestream API, [insert an ad break channel event](https://cloud.google.com/livestream/docs/how-to/create-channel-events#create_channel_event).




The ad is played immediately after the ad break is inserted.

## Clean up

Now that you have successfully hosted a live stream using the Google Cloud Video Stitcher API and requested it using the IMA DAI SDK for Android, it's important to clean up any serving resources.

Follow the [livestream clean up](https://cloud.google.com/video-stitcher/docs/how-to/gam/live/clean-up) guide to remove any unneeded resources and assets. 

[ Previous arrow_back  Prepare for your client application to work with Google Ad Manager  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/prepare-client-app-gam)

[ Next Chromecast  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/cast)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
