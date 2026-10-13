---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest
title: Live Stream v1 API - Class Manifest (1.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:40.436093+00:00
---

# Live Stream v1 API - Class Manifest (1.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Live Stream v1 API - Class Manifest (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.11.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.10.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.9.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.8.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.7.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.6.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.5.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.4.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.3.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.2.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.1.0/Google.Cloud.Video.LiveStream.V1.Manifest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.0.0/Google.Cloud.Video.LiveStream.V1.Manifest)


    
    
    public sealed class Manifest : IMessage<Manifest>, IEquatable<Manifest>, IDeepCloneable<Manifest>, IBufferMessage, IMessage

Reference documentation and code samples for the Live Stream v1 API class Manifest.

Manifest configuration.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Manifest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Manifest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Manifest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Manifest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Video.LiveStream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1)

## Assembly

Google.Cloud.Video.LiveStream.V1.dll

## Constructors 

### Manifest()
    
    
    public Manifest()

### Manifest(Manifest)
    
    
    public Manifest(Manifest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Manifest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest)`  
  
  
## Properties 

### FileName
    
    
    public string FileName { get; set; }

The name of the generated file. The default is `manifest` with the extension suffix corresponding to the `Manifest` [type][google.cloud.video.livestream.v1.Manifest.type]. If multiple manifests are added to the channel, each must have a unique file name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Key
    
    
    public string Key { get; set; }

Optional. A unique key for this manifest.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MaxSegmentCount
    
    
    public int MaxSegmentCount { get; set; }

Maximum number of segments that this manifest holds. Once the manifest reaches this maximum number of segments, whenever a new segment is added to the manifest, the oldest segment will be removed from the manifest. The minimum value is 3 and the default value is 5.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MuxStreams
    
    
    public RepeatedField<string> MuxStreams { get; }

Required. List of `MuxStream` [key][google.cloud.video.livestream.v1.MuxStream.key]s that should appear in this manifest.

  * For HLS, either `fmp4` or `ts` mux streams can be specified but not mixed.
  * For DASH, only `fmp4` mux streams can be specified.



**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SegmentKeepDuration
    
    
    public Duration SegmentKeepDuration { get; set; }

How long to keep a segment on the output Google Cloud Storage bucket after it is removed from the manifest. This field should be large enough to cover the manifest propagation delay. Otherwise, a player could receive 404 errors while accessing segments which are listed in the manifest that the player has, but were already deleted from the output Google Cloud Storage bucket. Default value is `60s`.

If both segment_keep_duration and [RetentionConfig.retention_window_duration][google.cloud.video.livestream.v1.RetentionConfig.retention_window_duration] are set, [RetentionConfig.retention_window_duration][google.cloud.video.livestream.v1.RetentionConfig.retention_window_duration] is used and segment_keep_duration is ignored.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### Type
    
    
    public Manifest.Types.ManifestType Type { get; set; }

Required. Type of the manifest, can be `HLS` or `DASH`.

**Property Value**  
---  
**Type** | **Description**  
`[Manifest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest.Types)[ManifestType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest.Types.ManifestType)` |   
  
### UseTimecodeAsTimeline
    
    
    public bool UseTimecodeAsTimeline { get; set; }

Whether to use the timecode, as specified in timecode config, when setting:

  * `availabilityStartTime` attribute in DASH manifests.
  * `#EXT-X-PROGRAM-DATE-TIME` tag in HLS manifests.



If false, ignore the input timecode and use the time from system clock when the manifest is first generated. This is the default behavior.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
