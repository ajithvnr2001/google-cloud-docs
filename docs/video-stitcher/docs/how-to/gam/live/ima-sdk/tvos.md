---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/tvos/
title: Use the IMA DAI SDK on tvOS \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:03.059109+00:00
---

# Use the IMA DAI SDK on tvOS  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/tvos/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Use the IMA DAI SDK on tvOS Stay organized with collections  Save and categorize content based on your preferences. 

## Play live streams registered with Google Cloud Video Stitcher API

This guide demonstrates how to use the IMA DAI SDK for tvOS to request and play a livestream for an event registered with the [Google Cloud Video Stitcher API](https://cloud.google.com/video-stitcher/docs/how-to/gam/live/overview), and how to insert an ad break during playback. 

This guide expands on the basic example from the [Get started guide](https://developers.google.com/interactive-media-ads/docs/sdks/tvos/dai) for IMA DAI.

For information on integrating with other platforms or on using the IMA client-side SDKs, see [Interactive Media Ads SDKs](https://developers.google.com/interactive-media-ads).

If you would like to view or follow along with a completed sample integration, download the Cloud video stitcher example for [Objective-C](https://github.com/googleads/googleads-ima-tvos-dai/tree/main/Objective-C/VideoStitcherExample) or [Swift](https://github.com/googleads/googleads-ima-tvos-dai/tree/main/Swift/VideoStitcherExample).

**Note:** Apple only provides frameworks to support [HTTP Live Streaming (HLS)](https://developer.apple.com/documentation/http_live_streaming), such as AVKit, AVFoundation, and WebKit. These frameworks won't work with DASH stream format. 

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

## Download and prepare the basic example

Download the [IMA DAI examples for tvOS](https://github.com/googleads/googleads-ima-tvos-dai/releases) and extract the Basic Example into a new folder. This example is an Xcode project that relies on Cocoapods to load the IMA SDK.

**Important:** IMA DAI SDK [v4.12.0](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/tvos/history) or later is required. Update the pod file as needed.

To prepare the sample to run, make sure [CocoaPods is installed](https://guides.cocoapods.org/using/getting-started.html), then open the basic example's folder in the terminal and run the following command:
    
    
    pod install --repo-update

Once that command completes, you see a file named `BasicExample.xcworkspace` in your project folder. Open this file in Xcode and run the sample to ensure that the test video and ads play as expected.

## Request a livestream

To replace the sample stream with your livestream, you need to use the `IMAVideoStitcherLiveStreamRequest` class that automatically creates an ad session with Google Ad Manager. You can use the Google Ad Manager UI to [locate the generated DAI sessions](https://support.google.com/admanager/answer/7257678) for monitoring and debugging purposes.

In the existing sample, there are examples for requesting a VOD stream or a livestream from Google's DAI servers. To make the sample work with the Google Cloud Video Stitcher API, you will need to replace the current `requestStream` function with one that uses the `IMAVideoStitcherLiveStreamRequest` class:

#### ViewController.m
    
    
    #import <GoogleInteractiveMediaAds/GoogleInteractiveMediaAds.h>
    ** static NSString *const kLiveConfigId = @"LIVE_CONFIG_ID";
    static NSString *const kLocation = @"LOCATION";
    static NSString *const kProjectNumber = @"PROJECT_NUMBER";
    static NSString *const kOAuthToken = @"OAUTH_TOKEN";
    static NSString *const kNetworkCode = @"NETWORK_CODE";
    static NSString *const kCustomAssetKey = @"CUSTOM_ASSET_KEY";
    **
    static NSString *const kBackupStreamURLString =
        @"http://googleimadev-vh.akamaihd.net/i/big_buck_bunny/bbb-,480p,720p,1080p,.mov.csmil/"
        @"master.m3u8";
    
    @interface ViewController () <IMAAdsLoaderDelegate, IMAStreamManagerDelegate>
    ...
    - (void)requestStream {
      IMAAVPlayerVideoDisplay *videoDisplay =
          [[IMAAVPlayerVideoDisplay alloc] initWithAVPlayer:self.playerViewController.player];
      IMAAdDisplayContainer *adDisplayContainer =
          [[IMAAdDisplayContainer alloc] initWithAdContainer:self.adContainerView];
    **  IMAVideoStitcherLiveStreamRequest *request =
          [[IMAVideoStitcherLiveStreamRequest alloc] initWithLiveStreamEventID:kLiveConfigId
                                                                        region:kLocation
                                                                 projectNumber:kProjectNumber
                                                                    OAuthToken:kOAuthToken
                                                                   networkCode:kNetworkCode
                                                                customAssetKey:kCustomAssetKey
                                                            adDisplayContainer:self.adDisplayContainer
                                                                  videoDisplay:self.videoDisplay
                                                                   userContext:nil,
                                                   videoStitcherSessionOptions:nil];
    **
      [self.adsLoader requestStreamWithRequest:request];
    }
    

### (Optional) Add streaming session options

Customize your stream request by adding session options to override the default Cloud Video Stitcher API configuration by populating the [`videoStitcherSessionOptions`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/tvos/reference/Classes/IMAVideoStitcherLiveStreamRequest#videostitchersessionoptions) parameter in your [IMAVideoStitcherLiveStreamRequest](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/tvos/reference/Classes/IMAVideoStitcherLiveStreamRequest). If you provide an unrecognized option, the Cloud Video Stitcher API will respond with an HTTP 400 error. Consult the [troubleshooting guide](https://cloud.google.com/video-stitcher/docs/troubleshooting) for assistance.

For example, you can override the [manifest options](https://cloud.google.com/video-stitcher/docs/concepts/manifest-options) with the following code snippet, which requests two stream manifests with renditions ordered from lowest bitrate to highest.

### Objective-C
    
    
     **// Define session options JSON string.
     // The following session options are examples. Use session options
     // that are compatible with your video stream.
     NSString *sessionOptionsStr =
       @"{"
       "  \"manifestOptions\": {"
       "    \"bitrateOrder\": \"ascending\""
       "  }"
       "}";
     // convert JSON NSString to NSDictionary
     NSData *sessionOptionsData = [sessionOptionsStr dataUsingEncoding:NSUTF8StringEncoding];
     NSError *error = nil;
     NSDictionary *sessionOptions = [NSJSONSerialization
                           JSONObjectWithData:sessionOptionsData
                           options:0
                           error:&error];**
     // make stream request
     IMAVideoStitcherLiveStreamRequest *streamRequest =
         [[IMAVideoStitcherLiveStreamRequest alloc] initWithLiveStreamEventID:kLiveConfigID
                                                                       region:kLocation
                                                               projectNumber:kProjectNumber
                                                                   OAuthToken:kOAuthToken
                                                                 networkCode:kNetworkCode
                                                               customAssetKey:kCustomAssetKey
                                                           adDisplayContainer:adDisplayContainer
                                                                 videoDisplay:imaVideoDisplay
                                                                 userContext:nil
                                                 **videoStitcherSessionOptions :sessionOptions**];
     [self.adsLoader requestStreamWithRequest:streamRequest];
    

### Swift
    
    
     **// Define session options JSON string.
     // The following session options are examples. Use session options
     // that are compatible with your video stream.
     let sessionOptionsStr = """
         {
           "manifestOptions": {
             "bitrateOrder": "ascending"
           }
         }
         """
     // convert JSON string to dictionary
     guard let sessionOptionsData = sessionOptionsStr.data(using: .utf8, allowLossyConversion: false) else { return nil }
     let sessionOptions = try? JSONSerialization.jsonObject(with: sessionOptionsData, options: .mutableContainers)
     // make stream request**
     let streamRequest = IMAVideoStitcherLiveStreamRequest(
       liveStreamEventID:ViewController.liveConfigID
       region:ViewController.location
       projectNumber:ViewController.projectNumber
       OAuthToken:ViewController.oAuthToken
       networkCode:ViewController.networkCode
       customAssetKey:ViewController.customAssetKey
       adDisplayContainer:adDisplayContainer
       videoDisplay:imaVideoDisplay
       userContext:nil
       **videoStitcherSessionOptions :sessionOptions**)
     adsLoader?.requestStream(with: streamRequest)
    

Run the project, then you can request and play your custom livestream.

## Insert an ad break

The Google Cloud Video Stitcher API inserts ads retrieved from the ad tag for each ad break. Ad breaks are denoted in the manifest using ad markers. Ad markers are inserted by the live stream encoder.

  * If you are using your own live stream, you need to insert the ad marker. For more information on the supported HLS and DASH ad markers, see the [ad markers documentation](https://cloud.google.com/video-stitcher/docs/concepts/ad-markers).

  * If you created a live stream using the Google Cloud Livestream API, [insert an ad break channel event](https://cloud.google.com/livestream/docs/how-to/create-channel-events#create_channel_event).




The ad is played immediately after the ad break is inserted.

## Clean up

Now that you have successfully hosted a live stream using the Google Cloud Video Stitcher API and requested it using the IMA DAI SDK for tvOS, it's important to clean up any serving resources.

Follow the [livestream clean up](https://cloud.google.com/video-stitcher/docs/how-to/gam/live/clean-up) guide to remove any unneeded resources and assets. 

[ Previous arrow_back  Roku  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/roku)

[ Next Use a custom integration  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/dai-api/use-custom-integration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
