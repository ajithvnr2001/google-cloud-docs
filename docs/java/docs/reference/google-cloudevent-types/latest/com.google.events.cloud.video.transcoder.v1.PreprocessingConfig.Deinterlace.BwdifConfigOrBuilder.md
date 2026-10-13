---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.video.transcoder.v1.PreprocessingConfig.Deinterlace.BwdifConfigOrBuilder
title: Interface PreprocessingConfig.Deinterlace.BwdifConfigOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:08.567172+00:00
---

# Interface PreprocessingConfig.Deinterlace.BwdifConfigOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.video.transcoder.v1.PreprocessingConfig.Deinterlace.BwdifConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PreprocessingConfig.Deinterlace.BwdifConfigOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.video.transcoder.v1.PreprocessingConfig.Deinterlace.BwdifConfigOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.video.transcoder.v1.PreprocessingConfig.Deinterlace.BwdifConfigOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.video.transcoder.v1.PreprocessingConfig.Deinterlace.BwdifConfigOrBuilder)


    
    
    public static interface PreprocessingConfig.Deinterlace.BwdifConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDeinterlaceAllFrames()
    
    
    public abstract boolean getDeinterlaceAllFrames()

Deinterlace all frames rather than just the frames identified as interlaced. The default is `false`.

`bool deinterlace_all_frames = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The deinterlaceAllFrames.  
  
### getMode()
    
    
    public abstract String getMode()

Specifies the deinterlacing mode to adopt. The default is `send_frame`. Supported values:

  * `send_frame`: Output one frame for each frame
  * `send_field`: Output one frame for each field



`string mode = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mode.  
  
### getModeBytes()
    
    
    public abstract ByteString getModeBytes()

Specifies the deinterlacing mode to adopt. The default is `send_frame`. Supported values:

  * `send_frame`: Output one frame for each frame
  * `send_field`: Output one frame for each field



`string mode = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mode.  
  
### getParity()
    
    
    public abstract String getParity()

The picture field parity assumed for the input interlaced video. The default is `auto`. Supported values:

  * `tff`: Assume the top field is first
  * `bff`: Assume the bottom field is first
  * `auto`: Enable automatic detection of field parity



`string parity = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parity.  
  
### getParityBytes()
    
    
    public abstract ByteString getParityBytes()

The picture field parity assumed for the input interlaced video. The default is `auto`. Supported values:

  * `tff`: Assume the top field is first
  * `bff`: Assume the bottom field is first
  * `auto`: Enable automatic detection of field parity



`string parity = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
