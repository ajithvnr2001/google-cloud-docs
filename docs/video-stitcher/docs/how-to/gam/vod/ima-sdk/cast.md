---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/cast/
title: Use the IMA DAI SDK on Chromecast \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:40.237574+00:00
---

# Use the IMA DAI SDK on Chromecast  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/cast/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Use the IMA DAI SDK on Chromecast Stay organized with collections  Save and categorize content based on your preferences. 

## Play VOD streams registered with Google Cloud Video Stitcher API

This guide demonstrates how to use the IMA DAI SDK for CAF Web Receivers to request and play a [Google Cloud VOD stream session](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/overview).

This guide expands on the basic example from full service DAI, adding support for streams registered with the Google Cloud Video Stitcher API.

**Note:** The IMA DAI SDK for CAF supports both HLS and DASH streams, with no implementation differences. 

Ensure your streaming format is supported by [CAF web receivers](https://developers.google.com/cast/docs/media/streaming_protocols) before continuing.

For information on integrating with other platforms or on using the IMA client-side SDKs, see [Interactive Media Ads SDKs](https://developers.google.com/interactive-media-ads).

## Background

Before using this guide, familiarize yourself with the [Chromecast Application Framework's Web Receiver](https://developers.google.com/cast/docs/web_receiver) protocol.

This guide assumes a basic level of familiarity with CAF receiver concepts, such as [message interceptors](https://developers.google.com/cast/docs/web_receiver/core_features#message_interception), [`MediaInformation`](https://developers.google.com/cast/docs/reference/web_receiver/cast.framework.messages.MediaInformation) objects, and using the [Cast Command and Control tool](https://developers.google.com/cast/docs/debugging/cac_tool) to emulate a CAF sender.

## App components and architecture

Implementing VOD stream playback with the [Google Cloud Video Stitcher API](https://cloud.google.com/video-stitcher/docs/concepts/overview) with the IMA CAF DAI SDK involves two main components as demonstrated in this guide:

  * [`VideoStitcherVodStreamRequest`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/cast/reference/js/VideoStitcherVodStreamRequest): An object that defines a stream request to Google's servers.
  * [`StreamManager`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/cast/reference/js/StreamManager): An object that handles communication between the video stream and the IMA DAI SDK, such as firing tracking pings and forwarding stream events to the publisher.



## Set up a Google Cloud project

Enter the following variables for use in the IMA SDK:

  * **Location** \- The Google Cloud region where your VOD config was created.

`LOCATION`

  * **Project Number** : The Google Cloud project number using the Video Stitcher API.

`PROJECT_NUMBER`

  * **OAuth Token** : A service account's short lived OAuth Token with the Video Stitcher user role. Read more about [creating short-lived credentials for service accounts](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials).

`OAUTH_TOKEN`

  * **Network Code** : Google Ad Manager network code for requesting ads.

`NETWORK_CODE`

  * **VOD Config ID** \- The VOD config ID for the VOD stream.

`VOD_CONFIG_ID`

Read more about creating the VOD config ID in the [Cloud stitching create a VOD config guide](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/create-vod-configs#create-vod-config).

`VOD_URI`




## Set up a custom cast receiver

To develop a custom cast receiver, you need the following:

  * A [Cast Developer Console](https://cast.google.com/publish/) account with test devices in an allowlist.

  * A hosted [web receiver app](https://developers.google.com/cast/docs/web_receiver/basic#create_a_basic_web_receiver_app) that is registered with your Cast Developer Console, and which can be modified to host the code provided by this guide.

  * A sending app configured to use your web receiver app. For the purposes of this example, this guide uses the [Cast Command and Control tool](https://developers.google.com/cast/docs/debugging/cac_tool) as the sender.




## Prepare a sender to pass stream data to the receiver

First, configure your sender app to make a load request to your web receiver, containing the following fields in your platform's [`MediaInformation`](https://developers.google.com/cast/docs/reference/web_receiver/cast.framework.messages.MediaInformation) object.

Field | Contents  
---|---  
`contentId` | A unique identifier for this media item, as defined in the [Cast reference documentation](https://developers.google.com/cast/docs/reference/web_sender/chrome.cast.media.MediaInfo#contentId). This ID shouldn't be reused for multiple items in the same media queue. `CONTENT_ID`  
`contentUrl` | Optional Backup stream URL to play if the DAI stream fails to load. `BACKUP_STREAM_URL`  
`contentType` | Optional Mimetype of the backup stream URL to play if the DAI stream fails to load. `BACKUP_STREAM_MIMETYPE`  
`streamType` | The string literal or constant used for this value varies by sender platform. `VOD`  
`customData` |  The `customData` field contains a key-value store of additional required fields. In this case, `customData` contains the DAI stream data that you collected. | Field | Contents  
---|---  
`region` | `LOCATION`  
`projectNumber` | `PROJECT_NUMBER`  
`oAuthToken` | `OAUTH_TOKEN`  
`networkCode` | `NETWORK_CODE`  
`vodConfigId` | `VOD_CONFIG_ID`  
  
Here are some code samples to help you get started:

### Web

To configure these values in a Cast web sender, first create a [`MediaInfo`](https://developers.google.com/cast/docs/reference/web_sender/chrome.cast.media.MediaInfo) object with the required data, then make a [load request](https://developers.google.com/cast/docs/web_sender/integrate#media_control) to the web receiver.
    
    
    // Create mediaInfo object
    const mediaInfo = new chrome.cast.media.MediaInfo("CONTENT_ID");
    mediaInfo.contentUrl = "BACKUP_STREAM_URL";
    mediaInfo.contentType = "BACKUP_STREAM_MIMETYPE";
    mediaInfo.streamType = chrome.cast.media.StreamType.VOD;
    mediaInfo.customData = {
      region: "LOCATION",
      projectNumber: "PROJECT_NUMBER",
      oAuthToken: "OAUTH_TOKEN",
      networkCode: "NETWORK_CODE",
      vodConfigId: "VOD_CONFIG_ID"
    };
    
    // Make load request to cast web receiver
    const castSession = cast.framework.CastContext.getInstance().getCurrentSession();
    const request = new chrome.cast.media.LoadRequest(mediaInfo);
    castSession.loadMedia(request).then(
      () => { console.log('Load succeed'); },
      (errorCode) => { console.log('Error code: ' + errorCode); });
    

### Android

To configure these values in a Cast web sender, first create a [`MediaInfo`](https://developers.google.com/android/reference/com/google/android/gms/cast/MediaInfo) object with the required data, then make a [load request](https://developers.google.com/cast/docs/android_sender/integrate#load_media) to the web receiver.
    
    
    JSONObject customData = new JSONObject()
      .put("region", "LOCATION")
      .put("projectNumber", "PROJECT_NUMBER")
      .put("oAuthToken", "OAUTH_TOKEN")
      .put("networkCode", "NETWORK_CODE")
      .put("vodConfigId", "VOD_CONFIG_ID");
    
    MediaInfo mediaInfo = MediaInfo.Builder("CONTENT_ID")
      .setContentUrl("BACKUP_STREAM_URL")
      .setContentType("BACKUP_STREAM_MIMETYPE")
      .setStreamType(MediaInfo.STREAM_TYPE_VOD)
      .setCustomData(customData)
      .build();
    
    RemoteMediaClient remoteMediaClient = mCastSession.getRemoteMediaClient();
    remoteMediaClient.load(new MediaLoadRequestData.Builder().setMediaInfo(mediaInfo).build());
    

### iOS (Obj-C)

To configure these values in a Cast web sender, first create a [`GCKMediaInformation`](https://developers.google.com/cast/docs/reference/ios/interface_g_c_k_media_information) object with the required data, then make a [load request](https://developers.google.com/cast/docs/ios_sender/integrate#load_media) to the web receiver.
    
    
    NSURL url = [NSURL URLWithString:@"BACKUP_STREAM_URL"];
    NSDictionary *customData = @{
      @"region": @"LOCATION",
      @"projectNumber": @"PROJECT_NUMBER",
      @"oAuthToken": @"OAUTH_TOKEN",
      @"networkCode": @"NETWORK_CODE",
      @"vodConfigId": @"VOD_CONFIG_ID"
    };
    
    GCKMediaInformationBuilder *mediaInfoBuilder =
      [[GCKMediaInformationBuilder alloc] initWithContentID: @"CONTENT_ID"];
    mediaInfoBuilder.contentURL = url;
    mediaInfoBuilder.contentType = @"BACKUP_STREAM_MIMETYPE";
    mediaInfoBuilder.streamType = GCKMediaStreamTypeNone;
    mediaInfoBuilder.customData = customData;
    self.mediaInformation = [mediaInfoBuilder build];
    
    GCKRequest *request = [self.sessionManager.currentSession.remoteMediaClient loadMedia:self.mediaInformation];
    if (request != nil) {
      request.delegate = self;
    }
    

### iOS (Swift)

To configure these values in a Cast web sender, first create a [`GCKMediaInformation`](https://developers.google.com/cast/docs/reference/ios/interface_g_c_k_media_information) object with the required data, then make a [load request](https://developers.google.com/cast/docs/ios_sender/integrate#load_media) to the web receiver.
    
    
    let url = URL.init(string: "BACKUP_STREAM_URL")
    guard let mediaURL = url else {
      print("invalid mediaURL")
      return
    }
    
    let customData = [
      "region": "LOCATION",
      "projectNumber": "PROJECT_NUMBER",
      "oAuthToken": "OAUTH_TOKEN",
      "networkCode": "NETWORK_CODE",
      "vodConfigId": "VOD_CONFIG_ID"
    ]
    
    let mediaInfoBuilder = GCKMediaInformationBuilder.init(contentId: "CONTENT_ID")
    mediaInfoBuilder.contentURL = mediaUrl
    mediaInfoBuilder.contentType = "BACKUP_STREAM_MIMETYPE"
    mediaInfoBuilder.streamType = GCKMediaStreamType.none
    mediaInfoBuilder.customData = customData
    mediaInformation = mediaInfoBuilder.build()
    
    guard let mediaInfo = mediaInformation else {
      print("invalid mediaInformation")
      return
    }
    
    if let request = sessionManager.currentSession?.remoteMediaClient?.loadMedia(mediaInfo) {
      request.delegate = self
    }
    

### CAC tool

To configure these values in the [Cast Command and Control tool](https://developers.google.com/cast/docs/debugging/cac_tool), click the Load Media tab, and set the custom load request type to LOAD. Then replace the JSON data in the text area with this JSON:
    
    
    {
      "media": {
        "contentId": "CONTENT_ID",
        "contentUrl": "BACKUP_STREAM_URL",
        "contentType": "BACKUP_STREAM_MIMETYPE",
        "streamType": "VOD",
        "customData": {
          "region": "LOCATION",
          "projectNumber": "PROJECT_NUMBER",
          "oAuthToken": "OAUTH_TOKEN",
          "networkCode": "NETWORK_CODE",
          "vodConfigId": "VOD_CONFIG_ID"
        }
      }
    }
    

This custom load request can be sent to the receiver to test the rest of the steps.

## Create a custom CAF web receiver

Create a custom web receiver, as seen in the [CAF SDK Custom Web Receiver Guide](https://developers.google.com/cast/docs/web_receiver/basic#create_a_basic_web_receiver_app).

Your receiver's code should look like the following:
    
    
    <html>
    <head>
      <script
          src="//www.gstatic.com/cast/sdk/libs/caf_receiver/v3/cast_receiver_framework.js">
      </script>
    </head>
    <body>
      <cast-media-player></cast-media-player>
      <script>
        const castContext = cast.framework.CastReceiverContext.getInstance()
        castContext.start();
      </script>
    </body>
    </html>
    

## Import the IMA DAI SDK and get the Player Manager

Add a script tag to import the IMA DAI SDK for CAF to your web receiver, just after the script loading CAF. Then in the script tag that follows, store the receiver context and player manager as constants before starting the receiver.
    
    
    <html>
    <head>
      **< script
          src="//www.gstatic.com/cast/sdk/libs/caf_receiver/v3/cast_receiver_framework.js"></script>**
      <script src="//imasdk.googleapis.com/js/sdkloader/cast_dai.js"></script>
    </head>
    <body>
      <cast-media-player></cast-media-player>
      <script>
        const castContext = cast.framework.CastReceiverContext.getInstance();
        **const playerManager = castContext.getPlayerManager();**
    
        castContext.start();
      </script>
    </body>
    </html>
    

## Initialize the IMA Stream Manager

Initialize the IMA Stream Manager.
    
    
    <html>
    <head>
      <script type="text/javascript"
          src="//www.gstatic.com/cast/sdk/libs/caf_receiver/v3/cast_receiver_framework.js"></script>
      <script src="//imasdk.googleapis.com/js/sdkloader/cast_dai.js"></script>
    </head>
    <body>
      <cast-media-player></cast-media-player>
      <script>
        const castContext = cast.framework.CastReceiverContext.getInstance();
        const playerManager = castContext.getPlayerManager();
        **const streamManager = new google.ima.cast.dai.api.StreamManager();**
    
        castContext.start();
      </script>
    </body>
    </html>
    

## Create the Stream Manager Load Interceptor

Before your media items are passed to CAF, create your stream request in a [LOAD message interceptor](https://developers.google.com/cast/docs/web_receiver/core_features#message_interception).
    
    
        const castContext = cast.framework.CastReceiverContext.getInstance();
        const playerManager = castContext.getPlayerManager();
        const streamManager = new google.ima.cast.dai.api.StreamManager();
    
       **** /**
         * Creates a VOD stream request object for the Video Stitcher API.
         * @param {!LoadRequestData} castRequest The request object from the cast sender
         * @return {StreamRequest} an IMA stream request
         */
        const createStreamRequest = (castRequest) => { /* ... */};
    
        /**
         * Initates a DAI stream request for the final stream manifest.
         * @param {!LoadRequestData} castRequest The request object from the cast sender
         * @return {Promise<LoadRequestData>} a promise that resolves to an updated castRequest, containing the DAI stream manifest
         */
        const createDAICastRequest = (castRequest) => {
            return streamManager.requestStream(castRequest, createStreamRequest(castRequest))
              .then((castRequestWithStreamData) => {
                console.log('Successfully made DAI stream request.');
                return castRequestWithStreamData;
              })
              .catch((error) => {
                console.log('Failed to make DAI stream request.');
                // CAF will automatically fallback to the content URL
                // that it can read from the castRequest object.
                return castRequest;
              });
        };
    
        playerManager.setMessageInterceptor(
            cast.framework.messages.MessageType.LOAD, createDAICastRequest);
    
        castContext.start();
    

## Create the stream request

Complete the `createStreamRequest` function to create a Video Stitcher API VOD stream request, based on the CAF load request.
    
    
        /**
         * Creates a VOD stream request object for the Video Stitcher API.
         * @param {!LoadRequestData} castRequest The request object from the cast sender
         * @return {StreamRequest} an IMA stream request
         */**    const createStreamRequest = (castRequest) => {
          const streamRequest = new google.ima.cast.dai.api.VideoStitcherVodStreamRequest();
          const customData = castRequest.media.customData;
    
          streamRequest.region = customData.region;
          streamRequest.projectNumber = customData.projectNumber;
          streamRequest.oAuthToken = customData.oAuthToken;
          streamRequest.networkCode = customData.networkCode;
          streamRequest.vodConfigId = customData.vodConfigId;
          streamRequest.videoStitcherSessionOptions = {};
    
          return streamRequest;
        };**
    

### (Optional) Add streaming session options

Customize your stream request by adding session options to override the default Cloud Video Stitcher API configuration using [`VideoStitcherVodStreamRequest.videoStitcherSessionOptions`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/cast/reference/js/VideoStitcherVodStreamRequest#videoStitcherSessionOptions). If you provide an unrecognized option, the Cloud Video Stitcher API will respond with an HTTP 400 error. Consult the [troubleshooting guide](https://cloud.google.com/video-stitcher/docs/troubleshooting) for assistance.

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
    

[ Previous arrow_back  Android  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/android)

[ Next HTML5  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/html5)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
