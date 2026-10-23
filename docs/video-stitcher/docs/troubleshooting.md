---
url: https://docs.cloud.google.com/video-stitcher/docs/troubleshooting/
title: Troubleshoot \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:06.820604+00:00
---

# Troubleshoot  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/troubleshooting/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with the Video Stitcher API. The errors shown on this page are specific to the Video Stitcher API. For information on generic errors across Google APIs, see the Cloud APIs [Errors](https://docs.cloud.google.com/apis/design/errors) page.

Only the first error is returned. If a request encounters multiple errors, you need to fix the returned error and retry the request to see the next error.

## Unable to fetch playlist when creating a session

The following issue occurs when the Video Stitcher API is unable to fetch the video manifest from the specified `sourceUri`.
    
    
    {
      "error": {
        "code": 404,
        "message": "got status code 403 when fetching playlist from URI \"https://example.com/manifest.m3u8\"",
        "status": "NOT_FOUND",
      }
    }
    

To resolve this issue, follow the steps below:

  1. Verify that the provided `sourceUri` links to a valid video manifest.

     * Use `curl` with the `sourceUri`. If the manifest is intended to be publicly accessible, ensure that the URL can be reached publicly.
     * If the `sourceUri` is correct and the video manifest requires URL signing, proceed to the next step.
  2. Ensure that the CDN key has been registered with the Video Stitcher API in the same region as the request.

     * [Verify that the CDN key configuration](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#list_cdn_keys) matching the `sourceUri` hostname exists. If the configuration doesn't exist, [register the CDN key](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#register_cdn_key) with the Video Stitcher API. Wait at least 5 minutes for the configuration to propagate to the service.
     * If the configuration exists, proceed to the next step.
  3. If you suspect the private key used for signing the URL is incorrect, you may want to [update the registered CDN key](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#update_cdn_key) with the correct private key.




## CDN key is outdated

If you recently registered or updated a CDN key and the Video Stitcher API has not started signing URLs using the new configuration, then follow the steps below to diagnose the issue:

  1. If the CDN key was recently registered with the Video Stitcher API, then wait at least 5 minutes to allow the update to propagate. If the issue persist, proceed to the next step.

  2. Verify that only one CDN key is registered for one hostname for the region. If multiple CDN keys have been registered with the same hostname, the Video Stitcher API will select one of the CDN keys to sign the URL with.

     * Ensure that only one CDN key has been registered with a specified hostname for a given region. [Delete the obsolete CDN key](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#delete_cdn_key).



## No ads inserted in a live session

If no ads were inserted in a live session, use the following steps to diagnose the issue:

  1. Verify that the source livestreams inserted ad breaks in the manifest. The following [ad markers](https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-markers) need to exist in the livestream video manifest to indicate to the Video Stitcher API to replace source video segments with ad segments.

     * If the source video manifest does not have any ad markers, either your encoder hasn't triggered an ad break or needs to be changed to insert the supported [ad markers](https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-markers).

     * If ad markers are clearly visible in the source manifest, then proceed to the next step.

  2. Verify that the provided ad tag returns a non-empty VAST response.

     * Copy the ad tag into a web browser (for example, Chrome) address bar and verifies that it returns a non-empty VAST response. The following is an empty VAST response:
           
           <VAST version="3.0"/>
           

     * If an empty VAST response is returned, then the issue is the ad tag. Verify that the ad tag is set up correctly with the ad servers.

     * If the VAST response is populated, use `curl` to request the ad tag. Some ad servers require the `User-Agent` [header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) to be provided. Try the following `curl` command:
           
           curl AD_TAG_URI
           

     * If the `curl` command returns an empty VAST response, add the `User-Agent` header to the `curl` command:
           
           curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" \
               AD_TAG_URI
           

     * If a populated VAST response is returned, then the issue is that the `User-Agent` header needs to be passed to the Video Stitcher API when creating the live session. The Video Stitcher API uses that header when executing the ad tag to retrieve ads.

     * If an empty response is still returned, then the issue is with the given ad tag. Confirm with the customer that the ad tag is correct and that any [ad tag macro](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions#ad-tag-macros) values are correct as well.

     * If the customer's ad tag issues have been resolved, but ads have not been inserted, proceed to the next step.

  3. [Inspect the live session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions#inspect-live-sessions). If the affected session is showing that ads are returned from the ad servers, then proceed to the next step.

  4. The next potential cause for missing ads is due to [ad re-encoding](https://docs.cloud.google.com/video-stitcher/docs/concepts/overview#ad_re-encoding). The API will re-encode ads during its first encounter to encode the ad to match the source video. Usually, ads take a few minutes to encode. Retry creating a new session after a few minutes to see if ads are inserted.

If no ads were inserted, the issue may be due to an ad failing to encode. The ad media URLs may not be reachable. In this case, the customer needs to work with the ad provider to determine what's wrong with their ad media.




## No ads inserted in a VOD session

  1. Verify that the provided ad tag returns a non-empty VAST or VMAP response. Use the provided ad tag with the following directions:

     * Copy the ad tag into a web browser (for example, Chrome) address bar and verifies that it returns a non-empty VAST, VMAP, or SmartXML response. The following is an empty VAST response:
     * Put the ad tag into a web browser (ie. Chrome, Firefox, etc) address bar and verifies that it returns a non empty VAST, VMAP, or SmartXML response. An empty VAST response looks like:
           
           <VAST version="3.0"/>
           

The following is an empty VMAP response:
           
           <VMAP xmlns:vmap="http://www.iab.net/vmap-1.0" version="1.0"/>
           

     * If an empty VAST response is returned, then the issue is the ad tag. Verify that the ad tag is set up correctly with the ad servers.

     * If the VAST response is populated, use `curl` to request the ad tag. Some ad servers require the `User-Agent` [header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) to be provided. Try the following `curl` command:
           
           curl AD_TAG_URI
           

     * If the `curl` command returns an empty VAST response, add the `User-Agent` header to the `curl` command:
           
           curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" \
               AD_TAG_URI
           

     * If a populated VAST or VMAP response is returned, then the issue is that the `User-Agent` header needs to be passed to the Video Stitcher API when creating the VOD session. The Video Stitcher API uses that header when executing the ad tag to retrieve ads.

     * If an empty response is still returned, then the issue is with the given ad tag. Confirm with the customer that the ad tag is correct and that any [ad tag macro](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions#ad-tag-macros) values are correct as well.

     * If the customer's ad tag issues have been resolved, but ads have not been inserted, proceed to the next step.

  2. [Inspect the VOD session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions#inspect-vod-sessions). If the affected session is showing that ads are returned from the ad servers, then proceed to the next step.

  3. The next potential cause for missing ads is due to [ad re-encoding](https://docs.cloud.google.com/video-stitcher/docs/concepts/overview#ad_re-encoding). The API will re-encode ads during its first encounter to encode the ad to match the source video. Usually, ads take a few minutes to encode. Retry creating a new session after a few minutes to see if ads are inserted.

If no ads were inserted, the issue may be due to an ad failing to encode. The ad media URLs may not be reachable. In this case, the customer needs to work with the ad provider to determine what's wrong with their ad media.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
