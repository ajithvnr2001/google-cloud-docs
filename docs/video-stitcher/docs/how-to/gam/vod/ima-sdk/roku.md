---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/roku/
title: Use the IMA DAI SDK on Roku \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:03.208093+00:00
---

# Use the IMA DAI SDK on Roku  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/roku/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Use the IMA DAI SDK on Roku Stay organized with collections  Save and categorize content based on your preferences. 

## Play VOD streams registered with Google Cloud Video Stitcher API

This guide demonstrates how to use the IMA DAI SDK for Roku to request and play a [Google Cloud VOD stream session](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/overview). 

This guide expands on the basic example from the [Get started guide](https://developers.google.com/interactive-media-ads/docs/sdks/roku/dai) for IMA DAI.

For information on integrating with other platforms or on using the IMA client-side SDKs, see [Interactive Media Ads SDKs](https://developers.google.com/interactive-media-ads).

If you would like to view or follow along with a completed sample integration, download the [Cloud video stitcher example](https://github.com/googleads/googleads-ima-roku-dai/tree/main/video_stitcher_api_example).

**Note:** The IMA DAI SDK for Roku supports both HLS and DASH streams, with no implementation differences. 

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

Download and run the [IMA Roku DAI Basic Example](https://github.com/googleads/googleads-ima-roku-dai/releases). Click the play button on the video player to start the short film "Tears of Steel", which contains ad breaks every 30 seconds.

## Request a VOD stream

Use the [`sdk.createVideoStitcherVodStreamRequestWithVodConfig()`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/roku/apis#ima.StreamRequest.createVideoStitcherVodStreamRequestWithVodConfig) function to replace the sample stream with your ad stitched VOD stream. You can use the Google Ad Manager UI to [locate the generated DAI sessions](https://support.google.com/admanager/answer/7257678) for monitoring and debugging.

In the existing sample, there are conditional statements to determine whether to construct a VOD `StreamRequest` or a live `StreamRequest`. Add a new path to construct a Cloud Video Stitcher VOD `StreamRequest` using the [values generated previously](https://cloud.google.com/video-stitcher/docs/how-to/gam/before-you-begin#set-up-project).

Here's an example:

**basic_example/components/MainScene.xml**
    
    
    <?xml version="1.0" encoding="utf-8" ?>
    <component name="MainScene" extends="Scene" initialFocus = "myVideo">
    <script type="text/brightscript">
    <![CDATA[
      function init()
        m.video = m.top.findNode("myVideo")
        m.video.notificationinterval = 1
        m.testLiveStream = {
          title: "Livestream",
          assetKey: "c-rArva4ShKVIAkNfy6HUQ",
          apiKey: "",
          type: "live"
        }
        m.testVodStream = {
          title: "VOD stream"
          contentSourceId: "2548831",
          videoId: "tears-of-steel",
          apiKey: "",
          type: "vod"
        }
        **m.testVideoStitcherVodStream = {
          title: "My Stream Title",
          vodConfigId: "VOD_CONFIG_ID",
          networkCode: "NETWORK_CODE",
          region: "LOCATION",
          projectNumber: "PROJECT_NUMBER",
          oAuthToken: "OAUTH_TOKEN",
          apiKey: "",
          title: "Video Stitcher VOD Stream",
          type: "stitcherVod"
        }**
    
        loadImaSdk()
      end function
    
      function loadImaSdk() as void
        m.sdkTask = createObject("roSGNode", "imasdk")
        m.sdkTask.observeField("sdkLoaded", "onSdkLoaded")
        m.sdkTask.observeField("errors", "onSdkLoadedError")
    
        ' Set this to the stream data you would like to play.
        selectedStream = m.testVideoStitcherVodStream
        m.videoTitle = selectedStream.title
        m.sdkTask.streamData = selectedStream
    
        m.sdkTask.observeField("urlData", "urlLoadRequested")
        m.sdkTask.video = m.video
        ' Setting control to run starts the task thread.
        m.sdkTask.control = "RUN"
      end function
    

**basic_example/components/Sdk.xml**
    
    
    Sub loadStream()
      sdk = m.sdk
      sdk.initSdk()
      setupVideoPlayer()
    
      request = {}
      streamData = m.top.streamData
      if streamData.type = "live"
        request = sdk.CreateLiveStreamRequest(streamData.assetKey, streamData.apiKey)
      else if streamData.type = "vod"
        request = sdk.CreateVodStreamRequest(streamData.contentSourceId, streamData.videoId, streamData.apiKey)
      **else if streamData.type = "stitcherVod"
        request = sdk.createVideoStitcherVodStreamRequest(
          streamData.vodConfigId,
          streamData.networkCode,
          streamData.region,
          streamData.projectNumber,
          streamData.oAuthToken
        )**
      else
        request = sdk.CreateStreamRequest()
      end if
    
      request.player = m.player
      request.adUiNode = m.top.video
    
      requestResult = sdk.requestStream(request)
      If requestResult <> Invalid
        print "Error requesting stream ";requestResult
      Else
        m.streamManager = Invalid
        While m.streamManager = Invalid
          sleep(50)
          m.streamManager = sdk.getStreamManager()
        End While
        If m.streamManager = Invalid or m.streamManager["type"] <> Invalid or m.streamManager["type"] = "error"
          errors = CreateObject("roArray", 1, True)
          print "error ";m.streamManager["info"]
          errors.push(m.streamManager["info"])
          m.top.errors = errors
        Else
          m.top.streamManagerReady = True
          addCallbacks()
          m.streamManager.start()
        End If
      End If
    End Sub
    

Reload the app to request and play your custom VOD stream.

### (Optional) Add streaming session options

Customize your stream request by adding session options to override the default Cloud Video Stitcher API configuration by populating the [`videoStitcherSessionOptions`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/roku/apis#ima.StreamRequest.videoStitcherSessionOptions) parameter in your [StreamRequest](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/roku/apis#ima.StreamRequest) object.

If you provide an unrecognized option, the Cloud Video Stitcher API will respond with an HTTP 400 error. Consult the [troubleshooting guide](https://cloud.google.com/video-stitcher/docs/troubleshooting) for assistance.

For example, you can override the [manifest options](https://cloud.google.com/video-stitcher/docs/concepts/manifest-options) with the following code snippet, which requests two stream manifests with renditions ordered from lowest bitrate to highest.
    
    
    request = sdk.createVideoStitcherVodStreamRequestWithVodConfig(vodConfigId, networkCode, region, projectNumber, oAuthToken)
    
    request.player = m.player
    request.adUiNode = m.top.video
    
    **' The following session options are examples. Use session options
    ' that are compatible with your video stream.
    sessionOptions = {
      "manifestOptions": {
        "bitrateOrder": "ascending"
      }
    }
    request.videoStitcherSessionOptions = sessionOptions**
    
    requestResult = sdk.requestStream(request)
    

## Clean up

Now that you have successfully hosted a VOD stream using the Google Cloud Video Stitcher API and requested it using the IMA DAI SDK for Roku, it's important to clean up any serving resources.

Follow the [VOD clean up](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/clean-up) guide to remove any unneeded resources and assets. 

[ Previous arrow_back  iOS  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/ios)

[ Next tvOS  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/tvos)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
