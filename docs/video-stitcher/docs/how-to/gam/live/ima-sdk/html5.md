---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/html5/
title: Use the IMA DAI SDK with an HTML5 client \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:22.404496+00:00
---

# Use the IMA DAI SDK with an HTML5 client  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/html5/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Use the IMA DAI SDK with an HTML5 client Stay organized with collections  Save and categorize content based on your preferences. 

## Play livestreams registered with the Google Cloud Video Stitcher API

This guide demonstrates how to use the IMA DAI SDK for HTML5 to request and play a livestream for an event registered with the [Google Cloud Video Stitcher API](https://cloud.google.com/video-stitcher/docs/how-to/gam/live/overview), and how to insert an ad break during playback. 

This guide expands on the basic example from the [Get started guide](https://developers.google.com/interactive-media-ads/docs/sdks/html5/dai) for IMA DAI.

For information on integrating with other platforms or on using the IMA client-side SDKs, see [Interactive Media Ads SDKs](https://developers.google.com/interactive-media-ads).

To view or follow a completed sample integration, download the Cloud video stitcher example for [HLS](https://github.com/googleads/googleads-ima-html5-dai/tree/main/cloudstitching/hls_js) or [DASH](https://github.com/googleads/googleads-ima-html5-dai/tree/main/cloudstitching/dash_js).

**Note:** The IMA DAI SDK for HTML5 supports both HLS and DASH streams, but playing each requires a different media player or extension like [HLS.js](https://github.com/video-dev/hls.js/) or [DASH.js](https://github.com/Dash-Industry-Forum/dash.js/), with varying implementations. 

This guide explains how to configure HLS.js and IMA DAI SDK to play an HLS stream, with important notes about implementation differences for DASH. 

See the [IMA DASH.js sample app](https://github.com/googleads/googleads-ima-html5-dai/tree/main/dash_js/simple) for a starting point to implement DASH DAI streams with IMA. 

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

## Configure a development environment

**Key Point:** The IMA DAI `VideoStitcherLiveStreamRequest` class supports both HLS streams and [multiple-period DASH streams](https://support.google.com/admanager/answer/9087202). Ad breaks are inserted only between DASH periods.

The IMA sample apps only demonstrate HLS stream requests. You can still use DASH streams when constructing the `VideoStitcherLiveStreamRequest` class. When setting up your DASH-compatible player, you need to set up a listener for your video player's progress events that can provide the video's metadata to [`StreamManager.processMetadata()`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/html5/reference/js/StreamManager#processMetadata). This function takes three parameters:

  1. `type`: A string which must be set to `'ID3'` for HLS streams and `'urn:google:dai:2018'` for DASH streams.

  2. `data`: For DASH event messages, this is the message data string.

  3. `timestamp`: A number that is the event message start time for DASH streams.




Send the metadata as soon and as often as your player events can provide. If metadata is missing or not correct, the IMA DAI SDK might not trigger ad events, leading to improperly reported ad events.

Download the [IMA DAI examples for HTML5](https://github.com/googleads/googleads-ima-html5-dai/releases) and extract the HLS.js Simple sample into a new folder. This example is a web app that you can host locally for testing purposes.

To host the example locally, navigate to the new folder, and run the following python command to start a web server:
    
    
    python3 -m http.server 8000

`http.server` is only available in Python 3.x. You can use any other web server, such as the Apache HTTP Server or Node JS.

Open a web browser and navigate to `localhost:8000` to see a video player. Your browser must support the [HLS.js](https://nochev.github.io/hls.js/docs/html/) library.

If everything is working properly, clicking the **play** button on the video player begins the short film "Tears of Steel" after a short ad. This content is delivered using a video on demand (VOD) stream.

## Request a livestream

To replace the sample VOD stream with your livestream, use the [`VideoStitcherLiveStreamRequest`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/html5/reference/js/VideoStitcherLiveStreamRequest) class that automatically creates an ad session with Google Ad Manager. You can use the Google Ad Manager UI to [locate the generated DAI sessions](https://support.google.com/admanager/answer/7257678) for monitoring and debugging.

In the existing sample, there are functions for requesting a VOD stream or a livestream. To make it work with the Google Cloud Video Stitcher API, you need to add a new function to return a [`VideoStitcherLiveStreamRequest`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/html5/reference/js/VideoStitcherLiveStreamRequest) object.

Here's an example:
    
    
    // StreamManager which will be used to request ad-enabled streams.
    let streamManager;
    ...
    function initPlayer() {
      videoElement = document.getElementById('video');
      adUiElement = document.getElementById('adUi');
      streamManager = new google.ima.dai.api.StreamManager(
        videoElement,
        adUiElement
      );
      streamManager.addEventListener(
          [
            google.ima.dai.api.StreamEvent.Type.LOADED,
            google.ima.dai.api.StreamEvent.Type.ERROR,
            google.ima.dai.api.StreamEvent.Type.AD_BREAK_STARTED,
            google.ima.dai.api.StreamEvent.Type.AD_BREAK_ENDED
          ],
          onStreamEvent, false);
    
      hls.on(Hls.Events.FRAG_PARSING_METADATA, function(event, data) {
        if (streamManager && data) {
          // For each ID3 tag in our metadata, we pass in the type - ID3, the
          // tag data (a byte array), and the presentation timestamp (PTS).
          data.samples.forEach(function(sample) {
            streamManager.processMetadata('ID3', sample.data, sample.pts);
          });
        }
      });
    
      videoElement.addEventListener('pause', () => {
        playButton.style.display = 'block';
      });
    
      playButton.addEventListener('click', initiatePlayback);
    }
    
    function initiatePlayback() {
      **requestVideoStitcherStream();**
    
      playButton.style.display = "none";
      playButton.removeEventListener('click', initiatePlayback);
      playButton.addEventListener('click', resumePlayback);
    }
    ...
    ** function requestVideoStitcherStream() {
      const streamRequest = new google.ima.dai.api.VideoStitcherLiveStreamRequest();
      streamRequest.liveStreamEventId = 'LIVE_CONFIG_ID';
      streamRequest.region = 'LOCATION';
      streamRequest.projectNumber = 'PROJECT_NUMBER';
      streamRequest.oAuthToken = 'OAUTH_TOKEN';
      streamRequest.networkCode = 'NETWORK_CODE';
      streamRequest.customAssetKey = 'CUSTOM_ASSET_KEY';
    
      streamManager.requestStream(streamRequest);
    }**
    

For local testing, if the livestream files are located in a Cloud Storage bucket, then you need to [enable CORS](https://cloud.google.com/storage/docs/using-cors) for origin `http://localhost:8000`.

Reload the page. Then, you can request and play custom livestreams.

### (Optional) Add streaming session options

Customize your stream request by adding session options to override the default Cloud Video Stitcher API configuration using [`VideoStitcherLiveStreamRequest.videoStitcherSessionOptions`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/html5/reference/js/VideoStitcherLiveStreamRequest#videoStitcherSessionOptions). If you provide an unrecognized option, the Cloud Video Stitcher API will respond with an HTTP 400 error. Consult the [troubleshooting guide](https://cloud.google.com/video-stitcher/docs/troubleshooting) for assistance.

For example, you can override the [manifest options](https://cloud.google.com/video-stitcher/docs/concepts/manifest-options) with the following code snippet, which requests two stream manifests with renditions ordered from lowest bitrate to highest.
    
    
    ...
    
    **// The following session options are examples. Use session options
    // that are compatible with your video stream.
    streamRequest.videoStitcherSessionOptions = {
      "manifestOptions": {
        "bitrateOrder": "ascending"
      }
    };**
    
    streamManager.requestStream(streamRequest);
    

## Insert an ad break

The Google Cloud Video Stitcher API inserts ads retrieved from the ad tag for each ad break. Ad breaks are denoted in the manifest using ad markers. Ad markers are inserted by the live stream encoder.

  * If you are using your own live stream, you need to insert the ad marker. For more information on the supported HLS and DASH ad markers, see the [ad markers documentation](https://cloud.google.com/video-stitcher/docs/concepts/ad-markers).

  * If you created a live stream using the Google Cloud Livestream API, [insert an ad break channel event](https://cloud.google.com/livestream/docs/how-to/create-channel-events#create_channel_event).




The ad is played immediately after the ad break is inserted.

## Clean up

Now that you have successfully hosted a live stream using the Google Cloud Video Stitcher API and requested it using the IMA DAI SDK for HTML5, it's important to clean up any serving resources.

Follow the [livestream clean up](https://cloud.google.com/video-stitcher/docs/how-to/gam/live/clean-up) guide to remove any unneeded resources and assets. 

Finally, in the terminal window where you started the Python 3 web server, use the command `ctrl+C` to end the local server.

[ Previous arrow_back  Chromecast  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/cast)

[ Next iOS  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/ios)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
