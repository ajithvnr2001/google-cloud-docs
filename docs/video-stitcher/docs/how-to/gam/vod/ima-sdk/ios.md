---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/ios/
title: Use the IMA DAI SDK on iOS \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:28.752563+00:00
---

# Use the IMA DAI SDK on iOS  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/ios/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Use the IMA DAI SDK on iOS Stay organized with collections  Save and categorize content based on your preferences. 

## Play VOD streams registered with Google Cloud Video Stitcher API

This guide demonstrates how to use the IMA DAI SDK for iOS to request and play a [Google Cloud VOD stream session](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/overview). 

This guide expands on the basic example from the [Get started guide](https://developers.google.com/interactive-media-ads/docs/sdks/ios/dai) for IMA DAI.

For information on integrating with other platforms or on using the IMA client-side SDKs, see [Interactive Media Ads SDKs](https://developers.google.com/interactive-media-ads).

If you would like to view or follow along with a completed sample integration, download the Cloud video stitcher example for [Objective-C](https://github.com/googleads/googleads-ima-ios-dai/tree/main/Objective-C/VideoStitcherExample) or [Swift](https://github.com/googleads/googleads-ima-ios-dai/tree/main/Swift/VideoStitcherExample).

**Note:** Apple only provides frameworks to support [HTTP Live Streaming (HLS)](https://developer.apple.com/documentation/http_live_streaming), such as AVKit, AVFoundation, and WebKit. These frameworks won't work with DASH stream format. 

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

User context
    The user context for tracking requests. Can be `nil`. _Defaults to`nil` in this guide._

## Set up the basic example

Go to the [IMA iOS DAI GitHub release page](https://github.com/googleads/googleads-ima-ios-dai/releases) and download the basic Objective-C example. This example is an iOS Xcode project that relies on Cocoapods to load the IMA DAI SDK. If you're using Swift, IMA doesn't have an iOS sample app, but check out the Swift code snippet later in this guide for how to implement an `IMAVideoStitcherVODStreamRequest` in your own app.

**Important:** IMA DAI SDK [v3.23.0](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/ios/history) or later is required. Update the pod file as needed.

To prepare the sample to run, make sure [CocoaPods is installed](https://guides.cocoapods.org/using/getting-started.html), then open the basic example's folder in the terminal and run the following command:
    
    
    pod install --repo-update

Once that command completes, you see a file named **BasicExample.xcworkspace** in your project folder. Open this file in Xcode and run the sample to ensure that the test video and ads play as expected.

## Request a VOD stream

To replace the sample stream with your ad stitched VOD stream, use [`IMAVideoStitcherVODStreamRequest`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/ios/reference/Classes/IMAVideoStitcherVODStreamRequest) to create an ad session with Google Ad Manager. You can use the Google Ad Manager UI to [locate the generated DAI sessions](https://support.google.com/admanager/answer/7257678) for monitoring and debugging.

In the existing sample, there are examples for requesting a VOD stream or a livestream from Google's DAI servers. To make it work with the Google Cloud Video Stitcher API, you need to replace the current `requestStream` function with one that uses the `IMAVideoStitcherVODStreamRequest` class.

Here's an example:

### Objective-C

**ViewController.m**
    
    
    ...
    
    #import <GoogleInteractiveMediaAds/GoogleInteractiveMediaAds.h>
    **/// The Stream's VOD config ID.
    static NSString *const kVODConfigID = @"VOD_CONFIG_ID";
    /// The Network Code used by the Video Stitcher API.
    static NSString *const kNetworkCode = @"NETWORK_CODE";
    /// The Google Cloud project using the Video Stitcher API.
    static NSString *const kProjectNumber = @"PROJECT_NUMBER";
    /// The Google Cloud region containing your project.
    static NSString *const kLocation = @"LOCATION";
    /// An OAuth Token created by a Google Cloud account with Video Stitcher API
    /// permissions.
    static NSString *const kOAuthToken = @"OAUTH_TOKEN";**
    
    /// Fallback URL in case something goes wrong in loading the stream. If all goes well, this will not
    /// be used.
    static NSString *const kBackupStreamURLString =
        @"http://googleimadev-vh.akamaihd.net/i/big_buck_bunny/bbb-,480p,720p,1080p,.mov.csmil/"
        @"master.m3u8";
    @interface ViewController () <IMAAdsLoaderDelegate, IMAStreamManagerDelegate>
    
    ...
    
    - (void)requestStream {
        // Create an ad display container for ad rendering.
        IMAAdDisplayContainer *adDisplayContainer =
            [[IMAAdDisplayContainer alloc] initWithAdContainer:self.videoView
                                                viewController:self
                                                companionSlots:nil];
        // Create an IMAAVPlayerVideoDisplay to give the SDK access to your video player.
        IMAAVPlayerVideoDisplay *imaVideoDisplay =
            [[IMAAVPlayerVideoDisplay alloc] initWithAVPlayer:self.contentPlayer];
        **IMAVideoStitcherVODStreamRequest *streamRequest =
            [[IMAVideoStitcherVODStreamRequest alloc] initWithVODConfigID:kVODConfigID
                                                                 region:kLocation
                                                          projectNumber:kProjectNumber
                                                             OAuthToken:kOAuthToken
                                                            networkCode:kNetworkCode
                                                     adDisplayContainer:adDisplayContainer
                                                           videoDisplay:imaVideoDisplay
                                                            userContext:nil
                                            videoStitcherSessionOptions:nil];**
        [self.adsLoader requestStreamWithRequest:streamRequest];
    }
    
    ...
    

### Swift

**ViewController.swift**
    
    
    ...
    
    class ViewController: UIViewController, IMAAdsLoaderDelegate, IMAStreamManagerDelegate {
      **/// The Stream's VOD config ID.
      static let vodConfigID = "VOD_CONFIG_ID"
      /// The Network Code used by the Video Stitcher API.
      static let networkCode = "NETWORK_CODE"
      /// The Google Cloud project using the Video Stitcher API.
      static let projectNumber = "PROJECT_NUMBER"
      /// The Google Cloud region containing your project.
      static let location = "LOCATION"
      /// An OAuth Token created by a Google Cloud account with Video Stitcher API
      /// permissions.
      static let oAuthToken = "OAUTH_TOKEN"**
    
      /// Fallback URL in case something goes wrong in loading the stream. If all goes well, this will
      /// not be used.
      static let backupStreamURLString = """
        http://googleimadev-vh.akamaihd.net/i/big_buck_bunny/\
        bbb-,480p,720p,1080p,.mov.csmil/master.m3u8
        """
    
      ...
    
      func requestStream() {
        // Create an ad display container for ad rendering.
        adDisplayContainer = IMAAdDisplayContainer(
          adContainer: videoView,
          viewController: self,
          companionSlots: nil)
        // Create an IMAAVPlayerVideoDisplay to give the SDK access to your video player.
        let imaVideoDisplay = IMAAVPlayerVideoDisplay(avPlayer: contentPlayer!)
        **// Create a VOD stream request.
        let streamRequest = IMAVideoStitcherVODStreamRequest(
          VODConfigID: ViewController.vodConfigID,
          region: ViewController.location,
          projectNumber: ViewController.projectNumber,
          oAuthToken: ViewController.oAuthToken,
          networkCode: ViewController.networkCode,
          adDisplayContainer: adDisplayContainer!,
          videoDisplay: imaVideoDisplay,
          userContext: nil,
          videoStitcherSessionOptions: nil)**
        adsLoader?.requestStream(with: streamRequest)
      }
    
      ...
    

Run the project, then you can request and play your custom VOD stream.

### (Optional) Add streaming session options

Customize your stream request by adding session options to override the default Cloud Video Stitcher API configuration by populating the [`videoStitcherSessionOptions`](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/ios/reference/Classes/IMAVideoStitcherVODStreamRequest#videostitchersessionoptions) parameter in your [IMAVideoStitcherVODStreamRequest](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/ios/reference/Classes/IMAVideoStitcherVODStreamRequest). If you provide an unrecognized option, the Cloud Video Stitcher API will respond with an HTTP 400 error. Consult the [troubleshooting guide](https://cloud.google.com/video-stitcher/docs/troubleshooting) for assistance.

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
                           error:&error];
     // make stream request**
     IMAVideoStitcherVODStreamRequest *streamRequest =
         [[IMAVideoStitcherVODStreamRequest alloc] initWithVODConfigID:kVODConfigID
                                                               region:kLocation
                                                         projectNumber:kProjectNumber
                                                           OAuthToken:kOAuthToken
                                                           networkCode:kNetworkCode
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
     let streamRequest = IMAVideoStitcherVODStreamRequest(
       vodConfigID:ViewController.vodConfigID
       region:ViewController.location
       projectNumber:ViewController.projectNumber
       OAuthToken:ViewController.oAuthToken
       networkCode:ViewController.networkCode
       adDisplayContainer:adDisplayContainer
       videoDisplay:imaVideoDisplay
       userContext:nil
       **videoStitcherSessionOptions :sessionOptions**)
     adsLoader?.requestStream(with: streamRequest)
    

## Clean up

Now that you have successfully hosted a VOD stream using the Google Cloud Video Stitcher API and requested it using the IMA DAI SDK for iOS, it's important to clean up any serving resources.

Follow the [VOD clean up](https://cloud.google.com/video-stitcher/docs/how-to/gam/vod/clean-up) guide to remove any unneeded resources and assets. 

[ Previous arrow_back  HTML5  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/html5)

[ Next Roku  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/ima-sdk/roku)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
