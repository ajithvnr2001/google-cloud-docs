---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types.TextMessageCitationAnchor
title: Data Analytics API with Gemini v1beta API - Class CitationAnchor.Types.TextMessageCitationAnchor (1.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:09.244435+00:00
---

# Data Analytics API with Gemini v1beta API - Class CitationAnchor.Types.TextMessageCitationAnchor (1.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types.TextMessageCitationAnchor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Analytics API with Gemini v1beta API - Class CitationAnchor.Types.TextMessageCitationAnchor (1.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta12 (latest)  1.0.0-beta11 
    
    
    public sealed class CitationAnchor.Types.TextMessageCitationAnchor : IMessage<CitationAnchor.Types.TextMessageCitationAnchor>, IEquatable<CitationAnchor.Types.TextMessageCitationAnchor>, IDeepCloneable<CitationAnchor.Types.TextMessageCitationAnchor>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Analytics API with Gemini v1beta API class CitationAnchor.Types.TextMessageCitationAnchor.

Citation anchor within a TextMessage.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CitationAnchor.Types.TextMessageCitationAnchor

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CitationAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types)[TextMessageCitationAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types.TextMessageCitationAnchor), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CitationAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types)[TextMessageCitationAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types.TextMessageCitationAnchor), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CitationAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types)[TextMessageCitationAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types.TextMessageCitationAnchor), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GeminiDataAnalytics.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta)

## Assembly

Google.Cloud.GeminiDataAnalytics.V1Beta.dll

## Constructors 

### TextMessageCitationAnchor()
    
    
    public TextMessageCitationAnchor()

### TextMessageCitationAnchor(TextMessageCitationAnchor)
    
    
    public TextMessageCitationAnchor(CitationAnchor.Types.TextMessageCitationAnchor other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CitationAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types)[TextMessageCitationAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.CitationAnchor.Types.TextMessageCitationAnchor)`  
  
  
## Properties 

### EndOffsetBytes
    
    
    public int EndOffsetBytes { get; set; }

Output only. The offset, measured in UTF-8 bytes, within the part string where the citation ends (exclusive). Example: For the text "Hello, world" where "world" is cited, the start offset bytes (inclusive) is 7 and the end offset bytes (exclusive) is 12.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PartIndex
    
    
    public int PartIndex { get; set; }

Output only. The 0-based index of the part within the TextMessage.parts field.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SourceIds
    
    
    public RepeatedField<string> SourceIds { get; }

Output only. The ids of the sources that are cited.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StartOffsetBytes
    
    
    public int StartOffsetBytes { get; set; }

Output only. The offset, measured in UTF-8 bytes, within the part string where the citation begins (inclusive). Example: For the text "Hello, world" where "world" is cited, the start offset bytes (inclusive) is 7 and the end offset bytes (exclusive) is 12.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
