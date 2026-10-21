---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/android/
title: Use the IMA DAI SDK on Android \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:21.427675+00:00
---

# Use the IMA DAI SDK on Android  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/android/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Use the IMA DAI SDK on Android Stay organized with collections  Save and categorize content based on your preferences. 

## Play VOD streams registered with Google Cloud Video Stitcher API

This guide demonstrates how to use the IMA DAI SDK for Android to request and play a [Google Cloud VOD stream session](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/overview). 

This guide expands on the basic example from the [Get started guide](https://developers.google.com/interactive-media-ads/docs/sdks/android/dai) for IMA DAI.

For information on integrating with other platforms or on using the IMA client-side SDKs, see [Interactive Media Ads SDKs](https://developers.google.com/interactive-media-ads).

If you would like to view or follow along with a completed sample integration, download the [Cloud video stitcher example](https://github.com/googleads/googleads-ima-android-dai/tree/main/CloudVideoStitcherExample).

**Note:** The IMA DAI SDK for Android supports both HLS and DASH streams. 

This guide explains how to configure exoplayer and IMA DAI SDK to play an HLS stream. For an example of a video player supporting both HLS and DASH streams, see our [Advanced Example](https://github.com/googleads/googleads-ima-android-dai/blob/main/AdvancedExample/app/src/main/java/com/google/ads/interactivemedia/v3/samples/samplevideoplayer/SampleVideoPlayer.java#L151-L166). 

## Set up a Google Cloud project

Enter the following variables for use in the IMA SDK:

Location
    The [Google Cloud region](https://cloud.google.com/video-stitcher/docs/locations) where your VOD config was created: `LOCATION`
Project number
    The Google Cloud project number using the Video Stitcher API: `PROJECT_NUMBER`
OAuth token
    

A service account's short lived OAuth token with the Video Stitcher user role: 
    
    
    OAUTH_TOKEN

    

Read more about [creating short-lived OAuth tokens](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/prepare-client-app-gam#generate-oauth-tokens). The OAuth token can be reused across multiple requests as long as it has not expired.

Network code
    

The Ad Manager network code for requesting ads: `NETWORK_CODE`

VOD config ID
    

The VOD config ID for the VOD stream: `VOD_CONFIG_ID`

Read more about creating the VOD config ID in the [Cloud stitching create a VOD config guide](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/create-vod-configs#create-vod-config).

## Set up the basic example

Go to the [IMA Android DAI GitHub release page](https://github.com/googleads/googleads-ima-android-dai/releases) and download the basic example. This example is an Android app that you can open in Android Studio for testing purposes.

**Important:** It's important for your app to send ID3 events using [`VideoStreamPlayerCallback.onUserTextReceived()`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/android/api/reference/com/google/ads/interactivemedia/v3/api/player/VideoStreamPlayer.VideoStreamPlayerCallback.html#public-abstract-void-onusertextreceived-string-usertext) for IMA DAI to function. See this [Full service DAI code snippet example](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/android?service=full#videoplayerappsampleadswrapperjava_2).

To test with a non-Cloud Video Stitcher VOD stream, set the `CONTENT_TYPE` constant in SampleAdsWrapper.java to either `ContentType.VOD_HLS`, or `ContentType.VOD_DASH`, to load the appropriate CMS ID and video ID for the stream. Then in SampleVideoPlayer.java, set `currentlyPlayingStreamType` to either `CONTENT_TYPE_HLS`, or `CONTENT_TYPE_DASH` ,to properly handle the metadata of your chosen stream type.

If everything is working properly, clicking the play button on the video player begins the short film "Tears of Steel", with a pre-roll ad break.

## Request a VOD stream

To replace the sample stream with your ad stitched VOD stream, use [`sdkFactory.createVideoStitcherVodStreamRequest()`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/android/api/reference/com/google/ads/interactivemedia/v3/api/ImaSdkFactory.html#public-streamrequest-createvideostitchervodstreamrequest-string-networkcode,-string-region,-string-projectnumber,-string-oauthtoken,-string-vodconfigid) to create an ad session with Google Ad Manager. You can use the Google Ad Manager UI to [locate the generated DAI sessions](https://support.google.com/admanager/answer/7257678) for monitoring and debugging.

`sdkFactory.createVideoStitcherVodStreamRequest()` is available on IMA DAI SDK v3.30.0 or higher.

To use [`sdkFactory.createVideoStitcherVodStreamRequest()`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/android/api/reference/com/google/ads/interactivemedia/v3/api/ImaSdkFactory.html#public-streamrequest-createvideostitchervodstreamrequest-string-networkcode,-string-region,-string-projectnumber,-string-oauthtoken,-string-vodconfigid) with the `vodConfigId` parameter, IMA DAI SDK version 3.33.0 or higher is required.

In the existing sample, there are conditional statements for requesting a VOD stream or a livestream. To make it work with the Google Cloud Video Stitcher API, you need to add a new path to return a `StreamRequest` created using `sdkFactory.createVideoStitcherVodStreamRequest()`.

Here's an example:

**videoplayerapp/SampleAdsWrapper.java**
    
    
    ...
    private enum ContentType {
      LIVE_HLS,
      LIVE_DASH,
    **// Add a VOD HLS Google Cloud type. DASH streams are also supported.
      VOD_HLS_GOOGLE_CLOUD,
      VOD_DASH_GOOGLE_CLOUD,**
      VOD_HLS,
      VOD_DASH,
    }
    
    **// Set CONTENT_TYPE to the associated enum for the
    // stream type you would like to test.
    private static final ContentType CONTENT_TYPE =
        ContentType.VOD_HLS_GOOGLE_CLOUD;**
    ...
    
    @Nullable
      private StreamRequest buildStreamRequest() {
        StreamRequest request;
        switch (CONTENT_TYPE) {
          ...
          **case VOD_HLS_GOOGLE_CLOUD:
          case VOD_DASH_GOOGLE_CLOUD:
            // VOD HLS or DASH stream generated by the
            // Google Cloud Video Stitcher API.
            request = sdkFactory.createVideoStitcherVodStreamRequest(
              "NETWORK_CODE",
              "LOCATION",
              "PROJECT_NUMBER",
              "OAUTH_TOKEN",
              "VOD_CONFIG_ID"
            );
            if (CONTENT_TYPE == ContentType.VOD_HLS_GOOGLE_CLOUD) {
              request.setFormat(StreamFormat.HLS);
            } else {
              request.setFormat(StreamFormat.DASH);
            }
            return request;**
        }
        // Content type not selected.
        return null;
      }
      ...
    

Reload the app to request and play your custom VOD stream.

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
    

## Clean up

Now that you have successfully hosted a VOD stream using the Google Cloud Video Stitcher API and requested it using the IMA DAI SDK for Android, it's important to clean up any serving resources.

Follow the [VOD clean up](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/clean-up) guide to remove any unneeded resources and assets. 

[ Previous arrow_back  Prepare for your client application to work with Google Ad Manager  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/prepare-client-app-gam)

[ Next Chromecast  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/cast)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
