---
url: https://docs.cloud.google.com/media-cdn/docs/playback-tracing/
title: Playback tracing \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:47.128311+00:00
---

# Playback tracing  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/playback-tracing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)



Send feedback 

#  Playback tracing Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Playback tracing is not available during the current release of Media CDN.

With Media CDN, you can use Google's extensive logging infrastructure and low-latency log delivery to associate per-request logs to a single _playback_ event. This helps you understand how traffic was served—the edge location, network conditions, origin selection, and any errors—across the lifetime of a playback.

This is achieved as follows:

  * Allowing you to supply a client-generated playback ID across multiple requests.
  * Integrating with [Cloud Logging](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to query across playbacks and individual requests.
  * Exporting and querying with [BigQuery](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-create), or with your platform of choice. Scaled data analysis lets you look at aggregate latencies and served formats across the lifetime of the playback.



Combined with near real-time logging, playback tracing lets you correlate playback sessions and the overall quality of experience by location, stream, or client network, and act on issues quickly.

### Trace a playback

To associate multiple requests with a user-facing playback session, you generate an ID for that playback in your client. Playback tracing works by including the value of a header or query parameter in all associated request logs.

Players like [Shaka](https://github.com/google/shaka-player), [ExoPlayer](https://exoplayer.dev/), and Apple's [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) let you hook playback start events and append query parameters and HTTP headers to requests made for that streaming media source.

The header and query parameters are defined as follows:

  * A HTTP request header: `Playback-Trace-ID`
  * A URL query parameter: `playback-trace-id=`



The HTTP header is used instead of the query parameter, if both exist in a request.

  * The playback ID must not be less than 12 bytes (96-bits) long, no greater than 32 bytes (256-bits), and generated from a random source.
  * Playback IDs that are shorter than 12 bytes aren't logged. This is to avoid collisions.
  * Playback IDs longer than 32 bytes are truncated to their first 32 bytes.



Playback IDs should be unique over the course of a 7-day period. After the 7-day period, when playback IDs are re-used or collide, each set of requests is treated as a separate playback.

### Example: Generate a playback ID in Shaka Player

To benefit from playback tracing at scale, each user video playback needs to include a playback ID for all requests made for segments (and optionally, manifests). This playback ID must be the same for all requests within a playback in order to roll up aggregate statistics.

The following example:

  * Generates a playback ID on video load.
  * Only sends it on segment fetches, not for manifests.



If you want to use an existing playback ID, such as one provided by your Content Management System and client-side analytics, populate `playbackSessionId` with that value.
    
    
    let playbackSessionId;
    
    player.addEventListener('loading', () => {
      const randomBuffer = crypto.getRandomValues(new Uint8Array(16));
      playbackSessionId = shaka.util.Uint8ArrayUtils.toBase64(randomBuffer);
    });
    
    player.getNetworkingEngine().registerRequestFilter((type, request) => {
      // Remove this "type" check if you want the header on every request.
      // Alternately, you can check the request.uris array to send the
      // header to some servers and not others.
      if (type == shaka.net.NetworkingEngine.RequestType.SEGMENT) {
        request.headers['CPN'] = playbackSessionId;
      }
    });
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
