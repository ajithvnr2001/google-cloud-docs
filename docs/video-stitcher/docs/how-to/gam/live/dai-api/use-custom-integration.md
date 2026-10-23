---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/dai-api/use-custom-integration/
title: Use a custom integration \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:19.926026+00:00
---

# Use a custom integration  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/dai-api/use-custom-integration/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Use a custom integration Stay organized with collections  Save and categorize content based on your preferences. 

## Before you begin

This guide covers only the playback instructions in the absence of the [IMA DAI SDK](https://developers.google.com/interactive-media-ads).

Make sure you have already completed the steps in [Integrate Google Ad Manager (GAM) with live streams](https://cloud.google.com/video-stitcher/docs/how-to/gam/live/overview) beforehand.

**Note:** We strongly recommend that you use the IMA DAI SDK on platforms where it is supported.

If the IMA SDK is not available for your intended platform, you'll need your application to call the required APIs and trigger the ad impressions itself.

In order to do this, you'll need the following information:

**Location** |  The [ Google Cloud region ](https://cloud.google.com/video-stitcher/docs/locations) where your live config was created:   
`LOCATION`  
---|---  
**Project number** |  The project number of the Google Cloud project using the Video Stitcher API:   
`PROJECT_NUMBER`  
**OAuth token** |  A service account's short lived OAuth token with the Video Stitcher user role:   

    
    
    OAUTH_TOKEN

  
Read more about [ creating short-lived OAuth tokens](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials). **Key Point:** The OAuth token can be reused across multiple requests as long as it has not expired.   
**Network code** |  The Ad Manager network code for requesting ads:   
`NETWORK_CODE`  
**Live config ID** |  The live config ID you specified when creating your livestream event:   
`LIVE_CONFIG_ID`  
**Custom asset key** |  The Ad Manager custom asset key generated during the process of [ creating a configuration for a livestream event ](https://cloud.google.com/video-stitcher/docs/how-to/gam/live/create-live-configs) with the Video Stitcher API:   
`CUSTOM_ASSET_KEY`  
**Key Point:** Ensure that the network code and custom asset key are the exact same ones that were generated when you created the live config.

## Make a stream registration request to Ad Manager

Make a POST request to the stream registration endpoint. In return, you receive a JSON response containing the stream ID to send to the video stitching API.

### API endpoint
    
    
    **POST:** /ssai/pods/api/v1/network/NETWORK_CODE/custom_asset/CUSTOM_ASSET_KEY/stream
    Host: dai.google.com
    Content-Type: application/x-www-form-urlencoded
    

#### Path parameters

`NETWORK_CODE` |  Your Google Ad Manager 360 network code:   
`NETWORK_CODE`  
---|---  
`CUSTOM_ASSET_KEY` |  The custom identifier associated this event in Google Ad Manager:   
`CUSTOM_ASSET_KEY`  
  
#### Form-encoded body parameters

An optional set of form-encoded [ targeting parameters ](https://support.google.com/admanager/answer/7320899).

### Response JSON

`media_verification_url` |  The base URL to ping playback tracking events. A complete media verification URL is formed by appending an _ad event ID_ to this base URL.   
`MEDIA_VERIFICATION_URL`  
---|---  
`metadata_url` |  The URL to request _ad pod metadata_.   
`METADATA_URL`  
`polling_frequency` |  the recommended frequency in milliseconds to poll the `metadata_url`.   
`POLLING_FREQUENCY`  
`stream_id` |  The string used to identify the current stream session.   
`STREAM_ID`  
`valid_for` |  The amount of time left until the current stream session expires, in `dhms` (days, hours, minutes, seconds) format. For example, `2h0m0.000s` represents a duration of 2 hours.   
`valid_until` |  The time at which the current stream session expires, as an ISO 8601 datetime string in `yyyy-MM-dd'T'hh:mm:ss.sssssssss[+|-]hh:mm` format.   
  
### Example request (cURL)
    
    
    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "cust_params=\"section%3Dsports%26page%3Dgolf%2Ctennis\"" \
      https://dai.google.com/ssai/pods/api/v1/network/51636543/custom_asset/ext-doc-ps-redirect-hls/stream

#### Example response
    
    
    {
      "stream_id":"9fe8fe4f-f12e-4fed-b509-0ca269bb1668:TUL",
      "media_verification_url":"https://dai.google.com/.../media/",
      "metadata_url":"https://dai.google.com/.../metadata",
      "session_update_url":"https://dai.google.com/.../session",
      "polling_frequency":10
    }
    

In case of errors, standard HTTP error codes are returned with no JSON response body.

Parse the JSON response and store the relevant values.

**Tip:** The URLs provided in the API response are subject to change without notice. Therefore, use the URLs as provided in the API response rather than constructing them yourself. This helps ensure that your code continues to work correctly when the URLs change. 

## Generate the session playback URI

Make a POST request to the video stitcher API's `/livesessions` endpoint to create a new live session. In return, you receive a JSON response containing the stream manifest to load into your video player.

### API endpoint
    
    
    **POST:** /v1/projects/PROJECT_NUMBER/locations/LOCATION/liveSessions
    Host: videostitcher.googleapis.com
    Authorization: Bearer OAUTH_TOKEN
    Content-Type: application/json
    

#### Path parameters

`PROJECT_NUMBER` |  The project number of the Google Cloud project using the Video Stitcher API:   
`PROJECT_NUMBER`  
---|---  
`LOCATION` |  The [ Google Cloud region ](https://cloud.google.com/video-stitcher/docs/locations) where your live config was created:   
`LOCATION`  
  
#### Authorization header parameter

`OAUTH_TOKEN` |  A service account's short lived OAuth token with the Video Stitcher user role:   

    
    
    OAUTH_TOKEN  
  
---|---  
  
#### JSON-encoded body parameters

`liveConfig` |  A string containing your **project number** , **location** , and **live config id** with the following format:   
`projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID`  
---|---  
`adTracking` | Set to `"CLIENT"` to enable client-side tracking.  
`gamSettings` |  An object containing the **stream id** with the following format:   
`{"streamId":"STREAM_ID"}`  
  
### Response JSON

`name` | The name of the live session, containing the session ID.  
---|---  
`playUri` |  The URI of the stitched stream manifest, to load into your video player for playback.   
`PLAY_URI`  
`liveConfig` |  The same `liveConfig` string sent to the API in your request body.   
`gamSettings` |  The same `gamSettings` object sent to the API in your request body.   
  
### Example request (cURL)
    
    
    curl -X POST \
         -H "Content-Type: application/json" \
         -H "Authorization: Bearer OAUTH_TOKEN" \
         -d '@request.json' \
      https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveSessions

**request.json**
    
    
    {
      "liveConfig": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
      "adTracking": "CLIENT",
      "gamSettings": {
        "streamId": "STREAM_ID"
      }
    }
    

#### Example Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/liveSessions/SESSION_ID",
      "playUri": PLAY_URI,
      "liveConfig": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID"
      "gamSettings": {
        "streamId": STREAM_ID
      }
    }
    

After the response is received, you can play the ad-stitched live stream by referencing the **session playback URI** from the `playUri` field of the response object.

The Video Stitcher API generates a unique **session ID** for each request, which can be retrieved from the last section of the `name` field of the response object.

An idle session expires after 5 minutes. A session is considered idle if there have not been any manifest fetches within a period of time.

## Poll for new AdBreak metadata

The application is responsible for retrieving metadata for each ad break, so it knows which impressions need to be triggered. To accomplish this you will set a timer to regularly poll the DAI APIs `metadata_url` for new ad information. The interval for polling is specified in the `polling_frequency` field in the stream registration response.

**Important:** Don't generate the metadata request URL yourself, as the format is subject to change without notification. Instead, use the `metadata_url` value returned from your stream registration request.

In return, you receive a JSON object containing the following parameters:

`tags` |  A set of key-value pairs describing ad media events which will occur within the stream. Each key consists of either the first 17 characters of an ad media ID that will appear in the stream's ID3 metadata or, in the case of `progress` events, the entire ad media id. Each value is an object with the following properties: 

  * `ad`: The id of the ad containing the ad media event. 
  * `ad_break_id`: The id of the ad break containing the ad media event. 
  * `type`: The type of ad media event. Values are one of the following: 
    * `start` \- The ad has started
    * `firstquartile` \- The ad is 25% complete.
    * `midpoint` \- The ad is 50% complete.
    * `thirdquartile` \- The ad is 75% complete.
    * `complete` \- The ad has ended.
    * `progress` \- fired every second while an ad is playing.

  
---|---  
`ads` |  A set of key-value pairs describing ads which will appear within the stream. Each key is an ad id. Each value is an object with the following properties: 

  * `ad_break_id`: The id of the ad break containing the ad media event. 
  * `position`: the position of the ad within the ad break. please note that the first ad in a break has a position of `1`. 
  * `duration`: the duration of the ad in floating-point seconds. 
  * `title`: the title of the ad, as defined in the VAST. 
  * `description`: the description of the ad, as defined in the VAST. 
  * `ad_system`: the ad system, as defined in the VAST. 
  * `ad_system`: the ad id, as defined in the VAST. 
  * `ad_system`: the creative id, as defined in the VAST. 
  * `clickthrough_url`: the url to open when a user interacts with the ad. 
  * `universal_ad_id`: an object representing the universal ad id, as defined in the VAST. 

  
`ad_breaks` |  A set of key-value pairs describing ad breaks which will occur within the stream. Each key is an ad break id. Each value is an object with the following properties: 

  * `type`: The type of ad break. Values will be one of the following: 
    * `pre`: Represents a pre-roll ad.
    * `mid`: Represents a mid-roll ad.
    * `post`: Represents a post-roll ad.
  * `duration`: The duration of the ad break in floating-point seconds. 
  * `expected_duration`: The expected duration of the ad break in floating-point seconds. 
  * `ads`: The number of ads contained within the ad break. 

  
  
Store these values after each poll to associate timed metadata events within your video stream.

### Example request (cURL)
    
    
    curl https://dai.google.com/.../metadata/

#### Example response
    
    
    {
       "tags":{
          "google_0492266569":{
             "ad":"0000229836_ad1",
             "ad_break_id":"0000229836",
             "type":"firstquartile"
          },
          "google_1560331148":{
             "ad":"0000229836_ad1",
             "ad_break_id":"0000229836",
             "type":"thirdquartile"
          },
          "google_1877686714378797835":{
             "ad":"0000229836_slate",
             "ad_break_id":"0000229836",
             "type":"progress"
          },
          "google_1vRyQBYPw_7Gg3MrZ6S5EjmV9aLje-YpW8QHed1DSlU":{
             "ad":"0000229835_ad1",
             "ad_break_id":"0000229835",
             "type":"progress"
          },
          "google_2032765498":{
             "ad":"0000229835_ad1",
             "ad_break_id":"0000229835",
             "type":"midpoint"
          },
          ...
          "google_5646900623":{
             "ad":"0000229837_ad1",
             "ad_break_id":"0000229837",
             "type":"complete"
          }
       },
       "ads":{
          "0000229834_ad1":{
             "ad_break_id":"0000229834",
             "position":1,
             "duration":15.01,
             "title":"truman-e2e-creativeset4",
             "description":"truman-e2e-creativeset4 ad",
             "ad_system":"GDFP",
             "ad_id":"39066884",
             "creative_id":"58092079124",
             "clickthrough_url":"https://pubads.g.doubleclick.net/...",
             "universal_ad_id":{
                "id_value":"58092079124",
                "id_registry":"GDFP"
             }
          },
          "0000229834_slate":{
             "ad_break_id":"0000229834",
             "position":-1,
             "duration":14.974977777,
             "slate":true
          },
          ...
       },
       "ad_breaks":{
          "0000229834":{
             "type":"mid",
             "duration":15.01,
             "expected_duration":29.984977776999997,
             "ads":1
          },
          ...
       }
    }
    

## Listen to ID3 events and track playback events

To verify that specific events have occurred in a video stream, follow these steps to handle ID3 events:

  1. Store the media events in a queue, saving each media ID along with its timestamp, if surfaced by the player.
  2. On each time update from the player or at a set frequency (500 ms recommended), check the media events queue for recently played events by comparing the event timestamps to the playhead.
  3. For media events that you confirm have played, check the type by looking up the media ID in the stored ad break tags. Keep in mind that the ad break tags object only contains a truncated version of the media ID, limited to the first 10 digits after the google_ prefix, so there is not a direct match between ID3 media verification IDs and keys in the tags object. This is to prevent event verification pings from being sent before the ID3 event arrives. To generate the complete media verification URL of an ad event, append the full ad event ID to the media_verification_url value from the stream creation response.
  4. Use "progress" events to keep track of whether a user is inside an ad break. Do not send these events to the media verification endpoint to avoid an HTTP error code. For other event types, append the media ID to the media verification url and make a GET request to track playback.
  5. Remove the media event from the queue.



### API endpoint
    
    
    **GET:** MEDIA_VERIFICATION_URLAD_MEDIA_ID
    Host: dai.google.com
    

#### Path parameters

`MEDIA_VERIFICATION_URL` |  The value returned by the stream registration endpoint, in the `media_verification_url` field:   
`MEDIA_VERIFICATION_URL`  
---|---  
`AD_MEDIA_ID` |  The full ad media ID, as it appears in the stream's ID3 metadata:   
`AD_MEDIA_ID`  
  
#### Expected return values

`HTTP/1.1 204 No Content` | Successful empty response.  
---|---  
`HTTP/1.1 404 Not Found` | Media verification ID was not recognized.  
`HTTP/1.1 409 Conflict` | Media verification ID has already been sent.  
  
### Example request (cURL)
    
    
    curl MEDIA_VERIFICATION_URLAD_MEDIA_ID

#### Example response
    
    
    HTTP/1.1 204 No Content
    

## Limitations

If using the API within webviews, the following limitations apply with respect to targeting:

  * **UserAgent** : The user agent parameter is passed as a browser-specific value instead of the underlying platform.
  * **rdid** , **idtype** , **is_lat** : The device ID is not properly passed, which limits the functionality of the following features: 
    * Frequency capping
    * Sequential ad rotation
    * Audience segmentation and targeting



[ Previous arrow_back  tvOS  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/tvos)

[ Next Clean up  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/clean-up)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
