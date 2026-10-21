---
url: https://docs.cloud.google.com/livestream/docs/how-to/use-timecode/
title: Synchronize media workflows with live stream content using timecode \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:08:55.334162+00:00
---

# Synchronize media workflows with live stream content using timecode  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/use-timecode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Synchronize media workflows with live stream content using timecode Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to synchronize media workflows with live stream content in the Live Stream API using timecode. The timecode feature enables you to pass timecode inputs, provided as in-band data, into playback manifests. You can then synchronize your internal media workflows with the live stream content. For example, you can match independently-generated metadata annotations with the live stream content or align internal broadcast content with the Live Stream API output.

Timecode data needs to be compliant to specification SMPTE 12M (see [ST 12-2:2008](https://ieeexplore.ieee.org/document/7290702)). For H264, timecode data is carried in the picture timing supplemental enhancement information (SEI) message. For H265, timecode data is carried in the timecode SEI message.

## Use embedded timecode

To use timecode embedded in an input stream, add the following [`timecodeConfig`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Channel.FIELDS.timecode_config) to the `Channel` resource:
    
    
    "timecodeConfig": {
      "source": "EMBEDDED_TIMECODE"
    }

The default value for the `source` field is `MEDIA_TIMESTAMP`.

By default, the UTC timezone is used to interpret the timecode. To use a different timezone, set the `timeZone` or the `utcOffset` field:
    
    
    "timecodeConfig": {
      "source": "EMBEDDED_TIMECODE",
    
      "timeZone": {"id": "America/Los_Angeles"}
      // or
      "utcOffset": "-28800s" // -8 hours from UTC
    }

Daylight Savings Time is taken into account when setting the `timeZone` field. See How the input timecode is interpreted for more details.

## Include timecode in output manifests

You can set the [`useTimecodeAsTimeline`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Manifest.FIELDS.use_timecode_as_timeline) field to `true` to include timecode for each output manifest:
    
    
    "manifests": [
      {
        "key": "manifest_hls",
        "file_name": "manifest.m3u8",
        "type": "HLS",
        "muxStreams": ["mux_720p", "mux_540p"],
        "useTimecodeAsTimeline": true
      },
      {
        "key": "manifest_dash",
        "file_name": "manifest.mpd",
        "type": "DASH",
        "muxStreams": ["mux_720p", "mux_540p"],
        "useTimecodeAsTimeline": true
      }
    ]

### HLS manifest file

For HLS live streams, timecode is emitted as a `#EXT-X-PROGRAM-DATE-TIME` tag for each segment in the media M3U8 manifest file and looks similar to the following:
    
    
    #EXTM3U
    #EXT-X-VERSION:7
    #EXT-X-TARGETDURATION:2
    #EXT-X-MEDIA-SEQUENCE:0
    #EXT-X-DISCONTINUITY-SEQUENCE:0
    #EXT-X-PROGRAM-DATE-TIME:2023-04-21T21:49:25.529Z
    #EXTINF:1.265922
    720p60_h264_ts-0000000000.ts
    #EXT-X-PROGRAM-DATE-TIME:2023-04-21T21:49:26.795Z
    #EXTINF:2.000000
    720p60_h264_ts-0000000001.ts
    #EXT-X-PROGRAM-DATE-TIME:2023-04-21T21:49:28.795Z
    #EXTINF:2.000000
    720p60_h264_ts-0000000002.ts
    #EXT-X-PROGRAM-DATE-TIME:2023-04-21T21:49:30.795Z
    #EXTINF:2.000000
    720p60_h264_ts-0000000003.ts
    #EXT-X-PROGRAM-DATE-TIME:2023-04-21T21:49:32.795Z
    #EXTINF:2.000000
    720p60_h264_ts-0000000004.ts
    #EXT-X-PROGRAM-DATE-TIME:2023-04-21T21:49:34.795Z
    #EXTINF:2.000000
    720p60_h264_ts-0000000005.ts
    #EXT-X-PROGRAM-DATE-TIME:2023-04-21T21:49:36.795Z
    #EXTINF:2.000000
    720p60_h264_ts-0000000006.ts
    #EXT-X-PROGRAM-DATE-TIME:2023-04-21T21:49:38.795Z
    

`#EXT-X-PROGRAM-DATE-TIME` contains timecode data generated following ISO8601 format `YYYY-MM-DDThh:mm:ss[.mmm]TZD` where:

  * `YYYY` is the four-digit year
  * `MM` is the two-digit month (for example, 03 is March)
  * `DD` is the two-digit day of the month (01 through 31)
  * `T` is a set character indicating the start of the time element
  * `hh` is the two digits of an hour (00 through 23, AM/PM not included)
  * `mm` is the two digits of a minute (00 through 59)
  * `ss` is the two digits of a second (00 through 59)
  * `mmm` is the three digits of a millisecond (000 through 999)
  * `TZD` is the time zone designator (Z, ±hh:mm). The Z represents UTC, and the \+ or - values indicate how far ahead or behind UTC.



### DASH manifest file

For DASH live streams, the `availabilityStartTime` attribute in the MPD manifest file is set to the initial timecode and looks similar to the following:
    
    
    <MPD xmlns="urn:mpeg:dash:schema:mpd:2011" profiles="urn:mpeg:dash:profile:isoff-live:2011"
     type="dynamic" minBufferTime="PT4S" mediaPresentationDuration="PT0H0M473.262S"
     availabilityStartTime="2023-05-19T17:44:16.881Z">
    

`availabilityStartTime` contains timecode data generated following ISO8601 format `YYYY-MM-DDThh:mm:ss[.mmm]TZD` where:

  * `YYYY` is the four-digit year
  * `MM` is the two-digit month (for example, 03 is March)
  * `DD` is the two-digit day of the month (01 through 31)
  * `T` is a set character indicating the start of the time element
  * `hh` is the two digits of an hour (00 through 23, AM/PM not included)
  * `mm` is the two digits of a minute (00 through 59)
  * `ss` is the two digits of a second (00 through 59)
  * `mmm` is the three digits of a millisecond (000 through 999)
  * `TZD` is the time zone designator (Z, ±hh:mm). The Z represents UTC, and the \+ or - values indicate how far ahead or behind UTC.



## How the timecode data is parsed

Embedded timecode is parsed from the first video frame. The output media timestamps are advanced frame by frame afterward. There is no resynchronization between input and output times until the input stream is disconnected and reconnected.

Since the timestamp of the video is replaced by the timestamp generated from the timecode, [channel events](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.events) must follow the timecode clock to be properly executed at a specified time.

Timing can be aligned on redundant streams if the timecode generator in the production pipeline is the same or is locked on both the primary and backup contribution encoders (see video [What is Output Locking?](https://youtu.be/Vyt65zxvGrs)).

## How the input timecode is interpreted

The timecode in a picture timing SEI message contains time only (`16:30:00;10`). To include timecode in output manifests, both date and time are required, such as the full datetime (`2021-12-06T16:30:00.333Z`) or epoch time (`1638837000333`).

When interpreting the SEI timecode as datetime format, Live Stream API always assumes the incoming input stream is live or near live. Live Stream API uses the time zone specified in the channel's [`timecodeConfig`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#Channel.FIELDS.timecode_config) to interpret the SEI timecode to be as close, but not later than, the current time as possible.

For example, assume Live Stream API receives an input stream at the current time of `2021-12-06T21:00:00Z` in UTC. The following table shows how SEI timecode is converted to datetime format:

Time zone ID | SEI timecode | Interpreted as in local time | Interpreted as in UTC  
---|---|---|---  
`UTC` | `16:30:00;10` | `2021-12-06T16:30:00.333+00:00` | `2021-12-06T16:30:00.333Z`  
`America/Los_Angeles` | `16:30:00;10` | `2021-12-05T16:30:00.333-08:00` | `2021-12-06T00:30:00.333Z`  
`America/New_York` | `16:30:00;10` | `2021-12-05T16:30:00.333-05:00` | `2021-12-05T21:30:00.333Z`  
`Asia/Bangkok` | `16:30:00;10` | `2021-12-06T16:30:00.333+07:00` | `2021-12-06T09:30:00.333Z`  
`America/Los_Angeles` | `03:30:00;10` | `2021-12-06T03:30:00.333-08:00` | `2021-12-06T11:30:00.333Z`  
`Asia/Bangkok` | `03:30:00;10` | `2021-12-07T03:30:00.333+07:00` | `2021-12-06T20:30:00.333Z`  
  
Note that the interpreted times are never later than the current UTC time of `2021-12-06T21:00:00Z`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
