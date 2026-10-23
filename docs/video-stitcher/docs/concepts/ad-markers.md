---
url: https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-markers/
title: Ad markers \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:08.646237+00:00
---

# Ad markers  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-markers/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Ad markers Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes the ad markers supported by the Video Stitcher API. The Video Stitcher API identifies ad break boundaries by ad markers in a livestream's source HLS/DASH manifest and performs ad stitching within an ad break for every session of the livestream.

## Before you begin

Make sure you are familiar with the introductory concepts and terminology in the Video Stitcher API. For more information, see the technical [Overview](https://docs.cloud.google.com/video-stitcher/docs/concepts/overview).

See SCTE-35 specification [Digital Program Insertion Cueing Message For Cable](https://www.scte.org/standards/library/catalog/scte-35-digital-program-insertion-cueing-message/).

## SCTE-35 commands

Livestream ad markers are represented by standard SCTE-35 signals. Within the list of SCTE-35 commands, the Video Stitcher API supports the following two commands:

  * `splice_insert`
  * `time_signal`



With `time_signal`, you can provide additional arbitrary metadata for the associated ad break in the first segmentation unique program identifier (UPID).

The Video Stitcher API expects the `segmentation_upid_type` to be `0x0C`, which stands for `MPU()`. The `private_data` in the `MPU()` should be a base64-encoded JSON string, in which certain JSON keys are reserved for the following specific purposes:

  * `%%AD_TAG_ID%%`: Specifies the ad tag to use for the ad break. The ad tag ID should be one of the keys in the live session's `adTagMacros`.
  * `%%SLATE_ID%%`: Specifies the slate to use for the ad break. The slate ID must match the ID for a slate that has already been created in the same Google Cloud project.



All other key value pairs in the UPID payload are used for ad tag macro replacement.

For example, if an ad tag URI is `https://example.com?key=[foo]`, and the `private_data` is `eyJmb28iOiJiYXIifQ==`, which is the base64 representation of `{"foo":"bar"}`, the Video Stitcher API replaces `[foo]` with `bar`, and makes an ad tag request to `https://example.com?key=bar`.

### Google Ad Manager integration

For the Google Ad Manager integration workflow, SCTE35 messages may contain certain values which could be replaced in the ad tag. See the [list of supported macros](https://support.google.com/admanager/answer/13049027).

Ensure that the `adTagUri` [registered on the live config](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-configs) contains the chosen macros.

For example, if the SCTE35 message passes a value for `%%SPLICE_INSERT_EVENT_ID%%`, make sure the macro exists on the `adTagUri` as illustrated by the following example:
    
    
    AD_TAG_URI&macro=%%SPLICE_INSERT_EVENT_ID%%

When the Video Stitcher API requests the ad metadata and the `splice_insert` SCTE35 message has `splice_insert_event_id` set to `123`, it uses the following ad tag:
    
    
    AD_TAG_URI&macro=**123**

## HLS ad markers

### EXT-X-DATERANGE

Using `#EXT-X-DATERANGE` is specified in the [HTTP Live Streaming specification](https://tools.ietf.org/html/draft-pantos-http-live-streaming-23#section-4.3.2.7.1):

  * An `#EXT-X-DATERANGE` tag with attribute `SCTE35-OUT` indicates the immediate start splice point of an ad break.
  * An `#EXT-X-DATERANGE` tag with attribute `SCTE35-IN` indicates the immediate end splice point of an ad break.
  * The values for `SCTE35-OUT` and `SCTE35-IN` are expected to be hex-encoded.



Example:
    
    
    #EXT-X-DATERANGE:ID="111",START-DATE=START_DATE,SCTE35-OUT=0xFC302000000000000000FFF00F050000006F7FFF7E002932E0000000000000235EE5EF
    ...
    #EXT-X-DATERANGE:ID="111",START-DATE=START_DATE,END-DATE=END_DATE,SCTE35-IN=0xFC302000000000000000FFF00F050000006F7F7F7E002932E0000000000000D56C4036
    

The `#EXT-X-DATERANGE` tag only applies to the next segment in the variant playlist, even when the `START-DATE` does not match the timestamp of the segment.

### EXT-X-CUE-OUT and EXT-X-CUE-IN

An `#EXT-X-CUE-OUT` tag indicates the immediate start of an ad break, and an `#EXT-X-CUE-IN` tag indicates the immediate end of an ad break.

An `#EXT-OATCLS-SCTE35` tag can be used for SCTE-35 message, and the value is expected to be base64-encoded.

Example (without SCTE-35 message):
    
    
    #EXT-X-CUE-OUT:DURATION=30
    ...
    #EXT-X-CUE-IN
    

Example (with SCTE-35 message):
    
    
    #EXT-OATCLS-SCTE35:/DBBAAAAAAAAAP/wBQb+AAaXgAArAilDVUVJAAAAb3//AAApMuAMFXslJUFEX1RBR19JRCUlOnRhZy0xfTQAALOJefk=
    #EXT-X-CUE-OUT:30
    ...
    #EXT-X-CUE-IN
    

If the duration of an `EXT-X-CUE-OUT` tag is specified, then that value takes precedence even if the ad break duration in the SCTE-35 message conflicts with it. If the duration of the `EXT-X-CUE-OUT` tag is not specified and one is specified in the associated SCTE-35 message, then the value from the SCTE-35 message is used.

## DASH ad markers

Currently, the Video Stitcher API only supports multi-period DASH manifests. In a multi-period DASH manifest, an ad break should be represented by a `Period` with an event stream containing a cue-out marker. A cue-in marker is not required as the end of the ad break period indicates the end of the ad break.

If multiple cue-out events are presented in an ad break period's SCTE-35 event stream, the Video Stitcher API will only use the first one. The presentation time of the cue-out event is ignored as the break start time is the same as the period's start time.

The following is a list of supported `schemeIdUri` for an SCTE-35 event stream:

  * `urn:scte:scte35:2014:xml+bin`
  * `urn:scte:scte35:2013:xml`



### urn:scte:scte35:2014:xml+bin

An event stream whose `schemeIdUri` is set to `urn:scte:scte35:2014:xml+bin` contains events representing SCTE-35 messages in base64-encoded binary.

Example:
    
    
      <Period start="PT444334H55M0.010S" id="break-1">
        <EventStream schemeIdUri="urn:scte:scte35:2014:xml+bin" timescale="90000">
          <Event presentationTime="0" duration="5400000" id="1">
            <Signal xmlns="urn:scte:scte35:2014:xml+bin">
              <Binary xmlns="urn:scte:scte35:2014:xml+bin">/DBTAAAAAAAAAP/wBQb+AAaXgAA9AjtDVUVJAAAAAH//AABSZcAMJ3siJSVBRF9UQUdfSUQlJSI6InRhZy0xIiwiZGFzaCI6InRydWUifTQAABxkspA=</Binary>
            </Signal>
          </Event>
        </EventStream>
        ...
      </Period>
    

### urn:scte:scte35:2013:xml

An event stream whose `schemeIdUri` is set to `urn:scte:scte35:2013:xml` contains events representing SCTE-35 messages in clear XML.

Example:
    
    
      <Period start="PT444334H55M0.010S" id="break-1">
        <EventStream timescale="90000" schemeIdUri="urn:scte:scte35:2013:xml">
          <Event duration="5400000">
            <scte35:SpliceInfoSection protocolVersion="0" ptsAdjustment="140429" tier="4095">
              <scte35:SpliceInsert spliceEventId="1" spliceEventCancelIndicator="false" outOfNetworkIndicator="true" spliceImmediateFlag="false" uniqueProgramId="1" availNum="1" availsExpected="1">
                <scte35:Program><scte35:SpliceTime ptsTime="5672624400"/></scte35:Program>
                <scte35:BreakDuration autoReturn="true" duration="5400000"/>
              </scte35:SpliceInsert>
            </scte35:SpliceInfoSection>
          </Event>
        </EventStream>
        ...
      </Period>
    

## Early ad break notification for livestreams

For live stitching, ad tags are processed synchronously when the Video Stitcher API receives the cue-out ad marker in a livestream's manifest. This synchronous processing triggers a large number of ad tag requests and causes long delays for the live session's playback requests if the stream is highly populated.

Early ad break notification (EABN) gives the Video Stitcher API more time to prepare ads by notifying the API of an upcoming ad break.

### HLS early ad break notification

To notify the API of an upcoming ad break so the API can prepare ads in advance, a livestream's HLS playlist must:

  * Use `#EXT-X-DATERANGE` or `EXT-X-CUE-OUT` as the ad marker
  * Repeat a cue-out ad marker in the livestream's source manifest



#### #EXT-X-DATERANGE

When the source encoder schedules an upcoming ad break, it can insert an `#EXT-X-DATERANGE` cue-out marker into the source manifest. The marker's `X-TYPE` attribute indicates the type of ad marker; for early ad break notification, the value for `X-TYPE` is expected to be `EABN`. The marker's `START-TIME` attribute indicates the actual or planned ad break start time. The marker's `DURATION` attribute is required to indicate the duration of the ad break. This marker is called an _EABN cue-out_.

At the actual start of the ad break, the source encoder must insert an `#EXT-X-DATERANGE` cue-out marker into the source manifest. The marker's `ID` attribute must be the same as the corresponding EABN cue-out. The marker's `START-TIME` must be the same as the segment's media time at which this marker is inserted. This marker is called an _immediate cue-out_.

The following sample manifest contains one EABN cue-out, one immediate cue-out, and one cue-in:
    
    
    #EXTM3U
    #EXT-X-TARGETDURATION:4
    #EXT-X-VERSION:7
    #EXT-X-PROGRAM-DATE-TIME:2020-11-08T21:11:20.976Z
    #EXT-X-MEDIA-SEQUENCE:239959
    #EXT-X-DISCONTINUITY-SEQUENCE:2
    #EXT-X-DATERANGE:ID="2415919105",X-TYPE="EABN",START-DATE="2020-11-08T21:11:28.976Z",DURATION=29.988,SCTE35-OUT=0xFC303...
    #EXTINF:4.000,
    1028/segment_239959.ts
    #EXTINF:4.000,
    1028/segment_239960.ts
    #EXT-X-DATERANGE:ID="2415919105",START-DATE="2020-11-08T21:11:28.976Z",DURATION=29.988,SCTE35-OUT=0xFC303...
    #EXTINF:4.000,
    1028/segment_239961.ts
    #EXTINF:4.000,
    1028/segment_239962.ts
    #EXTINF:4.000,
    1028/segment_239963.ts
    ...
    #EXT-X-DATERANGE:ID="2415919105",END-DATE="2020-11-08T21:11:48.976Z",SCTE35-IN=0xFC303...
    #EXTINF:4.000,
    1028/segment_239968.ts
    

#### #EXT-X-CUE-OUT

  * Use `#EXT-X-CUE-OUT` as the ad marker
  * Repeat a cue-out ad marker in the livestream's source manifest



When the source encoder schedules an upcoming ad break, it can also insert an `#EXT-X-CUE-OUT` cue-out marker into the source manifest. The marker's `X-TYPE` attribute indicates the type of ad marker; for early ad break notification, the value for `X-TYPE` is expected to be `EABN`. The marker's `DURATION` attribute must indicate the duration of the ad break. This marker is called an _EABN cue-out_.

At the actual start of the ad break, the source encoder must insert an `#EXT-X-CUE-OUT` cue-out marker into the source manifest. The marker's `ID` attribute must be the same as the corresponding EABN cue-out. This marker is called an _immediate cue-out_.

The following sample manifest contains one EABN cue-out, one immediate cue-out, and one cue-in:
    
    
    #EXTM3U
    #EXT-X-TARGETDURATION:4
    #EXT-X-VERSION:7
    #EXT-X-PROGRAM-DATE-TIME:2020-11-08T21:11:20.976Z
    #EXT-X-MEDIA-SEQUENCE:239959
    #EXT-X-DISCONTINUITY-SEQUENCE:2
    #EXT-OATCLS-SCTE35:0xFC303...
    #EXT-X-CUE-OUT:ID="2415919105",X-TYPE="EABN",DURATION=29.988
    #EXTINF:4.000,
    1028/segment_239959.ts
    #EXTINF:4.000,
    1028/segment_239960.ts
    #EXT-OATCLS-SCTE35:0xFC303...
    #EXT-X-CUE-OUT:ID="2415919105",DURATION=29.988
    #EXTINF:4.000,
    1028/segment_239961.ts
    #EXTINF:4.000,
    1028/segment_239962.ts
    #EXTINF:4.000,
    1028/segment_239963.ts
    ...
    #EXT-X-CUE-IN:ID="2415919105"
    #EXTINF:4.000,
    1028/segment_239968.ts
    

### DASH early ad break notification

To notify the API of an upcoming ad break so the API can prepare ads in advance, a DASH livestream manifest must repeat ad marker Event in the `Main Period` and the `Ad Break Period`.

The first appearance in the `Main Period` notifies the API of an upcoming ad break, and the second appearance in the `Ad Break Period` indicates the immediate start of the ad break.

The following is a sample manifest:
    
    
    <MPD>
    <Period id="1">
       <!-- Main Period -->
       <EventStream timescale="90000"  schemeIdUri="urn:scte:scte35:2013:xml">
         <Event duration="5400000" presentationTime="53460000" id="1">
           <scte35:SpliceInfoSection>
              <scte35:SpliceInsert outOfNetworkIndicator="true" spliceImmediateFlag="true">
                <scte35:BreakDuration autoReturn="true" duration="5400000"/>
                </scte35:SpliceInsert>
            </scte35:SpliceInfoSection>
          </Event>
        </EventStream>
       ...
    </Period>
    
    <Period start="PT9M54S" id="2">
        <!-- Ad Break Period -->
       <EventStream timescale="90000"  schemeIdUri="urn:scte:scte35:2013:xml">
         <Event duration="5400000" id="1">
           <scte35:SpliceInfoSection>
              <scte35:SpliceInsert outOfNetworkIndicator="true" spliceImmediateFlag="true">
                <scte35:BreakDuration autoReturn="true" duration="5400000"/>
                </scte35:SpliceInsert>
            </scte35:SpliceInfoSection>
          </Event>
        </EventStream>
       ...
    </Period>
    
    <Period start="PT10M54S" id="3">
        <!-- Main Period -->
        ...
    </Period>
    </MPD>
    

## What's next

Learn how to complete specific [Video Stitcher API tasks](https://docs.cloud.google.com/video-stitcher/docs/how-to).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
