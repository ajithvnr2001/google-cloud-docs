---
url: https://docs.cloud.google.com/livestream/docs/scte-ad-break-markers/
title: In-band SCTE-35 commands used for ad breaks \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:08:55.664637+00:00
---

# In-band SCTE-35 commands used for ad breaks  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/scte-ad-break-markers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  In-band SCTE-35 commands used for ad breaks Stay organized with collections  Save and categorize content based on your preferences. 

The Live Stream API supports two methods for inserting ad breaks into a live stream:

  * Creating an [ad break channel event](https://docs.cloud.google.com/livestream/docs/how-to/create-channel-events#ad-break-event)
  * Inserting an in-band SCTE-35 command



This page describes the in-band SCTE-35 command used for ad breaks.

Ad markers are carried on the input stream and must be compliant with the SCTE-35 specification [Digital Program Insertion Cueing Message For Cable](https://www.scte.org/standards/library/catalog/scte-35-digital-program-insertion-cueing-message/). SCTE-35 data can be carried on an MPEG-TS elementary data stream using an elementary stream type equal to `0x86`. Only SRT input streams can be used to ingest inband SCTE-35 commands.

The Live Stream API parses all PIDs in the TS elementary stream.

Within the list of SCTE-35 commands, the Live Stream API supports the `splice_insert` command as defined in SCTE-35.

## HLS manifest file

For HLS, each splice command generates a `#EXT-X-CUE-OUT/#EXT-X-CUE-OUT-CONT/#EXT-X-CUE-IN` marker in the manifest playlist. The splice command also generates a `#EXT-OATCLS-SCTE35` entry with the SCTE-35 data encoded in base64 format, as seen in the following:
    
    
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:44:44.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000007.m4s
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:44:48.143Z
    #EXTINF:1.212833
    720p60_h264_fmp4-0000000008.m4s
    #EXT-OATCLS-SCTE35:/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-CUE-OUT:45.000000
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:44:49.356Z
    #EXTINF:2.787167
    720p60_h264_fmp4-0000000009.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=2.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:44:52.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000010.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=6.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:44:56.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000011.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=10.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:00.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000012.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=14.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:04.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000013.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=18.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:08.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000014.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=22.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:12.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000015.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=26.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:16.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000016.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=30.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:20.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000017.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=34.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:24.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000018.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=38.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:28.143Z
    #EXTINF:4.000000
    720p60_h264_fmp4-0000000019.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=42.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:32.143Z
    #EXTINF:2.000000
    720p60_h264_fmp4-0000000020.m4s
    #EXT-X-CUE-OUT-CONT:ElapsedTime=44.787167,Duration=45.000000,SCTE35=/DAlAAAAAAAAAP/wFAVDE1agf+//yBysA/4APcxQAAAAAAAAXhEvvQ==
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:34.143Z
    #EXTINF:0.212833
    720p60_h264_fmp4-0000000021.m4s
    #EXT-X-CUE-IN
    #EXT-X-PROGRAM-DATE-TIME:2023-05-19T17:45:34.358Z
    #EXTINF:3.784522
    720p60_h264_fmp4-0000000022.m4s
    

## DASH manifest file

For DASH, each splice command generates a new period with an `<EventStream>` section in the MPD file, as seen in the following:
    
    
    <Period id="Dash-32.475" start="PT32.475S">
      <AdaptationSet segmentAlignment="true" maxWidth="1280" maxHeight="720">
        <Representation mimeType="video/mp4" id="720p60_h264_fmp4" codecs="avc1.4d001f" width="1280" height="720" startWithSAP="1" bandwidth="2100000">
          <SegmentTemplate timescale="1000000" initialization="720p60_h264_fmp4/720p60_h264_fmp4-initialization_segment_0000000000.m4s" media="720p60_h264_fmp4/720p60_h264_fmp4-$Number%010d$.m4s" startNumber="9" presentationTimeOffset="1684475755212833">
            <SegmentTimeline>
              <S t="1684475755212833" d="2787167"/>
              <S t="1684475758000000" d="4000000" r="9"/>
              <S t="1684475798000000" d="2000000"/>
              <S t="1684475800000000" d="212833"/>
            </SegmentTimeline>
          </SegmentTemplate>
        </Representation>
        <Representation mimeType="video/mp4" id="360p30_h264_fmp4" codecs="avc1.4d001e" width="640" height="360" startWithSAP="1" bandwidth="600000">
          <SegmentTemplate timescale="1000000" initialization="360p30_h264_fmp4/360p30_h264_fmp4-initialization_segment_0000000000.m4s" media="360p30_h264_fmp4/360p30_h264_fmp4-$Number%010d$.m4s" startNumber="9" presentationTimeOffset="1684475755212833">
            <SegmentTimeline>
              <S t="1684475755212833" d="2787167"/>
              <S t="1684475758000000" d="4000000" r="9"/>
              <S t="1684475798000000" d="2000000"/>
              <S t="1684475800000000" d="212833"/>
            </SegmentTimeline>
          </SegmentTemplate>
        </Representation>
      </AdaptationSet>
      <AdaptationSet segmentAlignment="true" mimeType="audio/mp4" id="1" label="441k_160_aac_fmp4">
        <Representation id="441k_160_aac_fmp4" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="160000">
          <SegmentTemplate timescale="1000000" initialization="441k_160_aac_fmp4/441k_160_aac_fmp4-initialization_segment_0000000000.m4s" media="441k_160_aac_fmp4/441k_160_aac_fmp4-$Number%010d$.m4s" startNumber="9" presentationTimeOffset="1684475755212833">
            <SegmentTimeline>
              <S t="1684475755212833" d="2787167"/>
              <S t="1684475758000000" d="4000000" r="9"/>
              <S t="1684475798000000" d="2000000"/>
              <S t="1684475800000000" d="212833"/>
            </SegmentTimeline>
          </SegmentTemplate>
        </Representation>
      </AdaptationSet>
      <AdaptationSet segmentAlignment="true" mimeType="audio/mp4" id="2" label="48k_160_aac_fmp4">
        <Representation id="48k_160_aac_fmp4" codecs="mp4a.40.2" audioSamplingRate="48000" startWithSAP="1" bandwidth="128000">
          <SegmentTemplate timescale="1000000" initialization="48k_160_aac_fmp4/48k_160_aac_fmp4-initialization_segment_0000000000.m4s" media="48k_160_aac_fmp4/48k_160_aac_fmp4-$Number%010d$.m4s" startNumber="9" presentationTimeOffset="1684475755212833">
            <SegmentTimeline>
              <S t="1684475755212833" d="2787167"/>
              <S t="1684475758000000" d="4000000" r="9"/>
              <S t="1684475798000000" d="2000000"/>
              <S t="1684475800000000" d="212833"/>
            </SegmentTimeline>
          </SegmentTemplate>
        </Representation>
      </AdaptationSet>
      <AdaptationSet contentType="text" lang="en-US" segmentAlignment="true">
        <Representation mimeType="text/vtt" id="caption_webvtt_en_webvtt" bandwidth="4698">
          <SegmentTemplate timescale="1000000" media="caption_webvtt_en_webvtt/caption_webvtt_en_webvtt-$Number%010d$.vtt" startNumber="9" presentationTimeOffset="1684475755212833">
            <SegmentTimeline>
              <S t="1684475755212833" d="2787167"/>
              <S t="1684475758000000" d="4000000" r="9"/>
              <S t="1684475798000000" d="2000000"/>
              <S t="1684475800000000" d="212833"/>
            </SegmentTimeline>
          </SegmentTemplate>
        </Representation>
      </AdaptationSet>
      <AdaptationSet contentType="text" lang="es-CO" segmentAlignment="true">
        <Representation mimeType="text/vtt" id="caption_webvtt_es_webvtt" bandwidth="5450">
          <SegmentTemplate timescale="1000000" media="caption_webvtt_es_webvtt/caption_webvtt_es_webvtt-$Number%010d$.vtt" startNumber="9" presentationTimeOffset="1684475755212833">
            <SegmentTimeline>
              <S t="1684475755212833" d="2787167"/>
              <S t="1684475758000000" d="4000000" r="9"/>
              <S t="1684475798000000" d="2000000"/>
              <S t="1684475800000000" d="212833"/>
            </SegmentTimeline>
          </SegmentTemplate>
        </Representation>
      </AdaptationSet>
      <AdaptationSet contentType="text" lang="zh-CN" segmentAlignment="true">
        <Representation mimeType="text/vtt" id="caption_webvtt_zh_webvtt" bandwidth="7329">
          <SegmentTemplate timescale="1000000" media="caption_webvtt_zh_webvtt/caption_webvtt_zh_webvtt-$Number%010d$.vtt" startNumber="9" presentationTimeOffset="1684475755212833">
            <SegmentTimeline>
              <S t="1684475755212833" d="2787167"/>
              <S t="1684475758000000" d="4000000" r="9"/>
              <S t="1684475798000000" d="2000000"/>
              <S t="1684475800000000" d="212833"/>
            </SegmentTimeline>
          </SegmentTemplate>
        </Representation>
      </AdaptationSet>
      <EventStream timescale="1000000" schemeIdUri="urn:scte:scte35:2013:xml">
        <Event duration="45000000" id="1684475755">
          <SpliceInfoSection xmlns="http://www.scte.org/schemas/35">
            <SpliceInsert outOfNetworkIndicator="true" spliceImmediateFlag="true">
              <BreakDuration autoReturn="true" duration="45000000"/>
            </SpliceInsert>
          </SpliceInfoSection>
        </Event>
      </EventStream>
    </Period>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
