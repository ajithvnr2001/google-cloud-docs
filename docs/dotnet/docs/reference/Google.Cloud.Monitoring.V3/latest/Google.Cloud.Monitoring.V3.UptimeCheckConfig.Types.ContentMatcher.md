---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher
title: Google Cloud Monitoring v3 API - Class UptimeCheckConfig.Types.ContentMatcher (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:41.131578+00:00
---

# Google Cloud Monitoring v3 API - Class UptimeCheckConfig.Types.ContentMatcher (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Monitoring v3 API - Class UptimeCheckConfig.Types.ContentMatcher (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.16.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.15.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.14.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.13.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.12.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.11.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.10.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.9.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.8.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.7.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.6.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.5.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.4.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.3.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.2.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.1.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.0.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.6.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.5.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.4.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.3.0/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)


    
    
    public sealed class UptimeCheckConfig.Types.ContentMatcher : IMessage<UptimeCheckConfig.Types.ContentMatcher>, IEquatable<UptimeCheckConfig.Types.ContentMatcher>, IDeepCloneable<UptimeCheckConfig.Types.ContentMatcher>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Monitoring v3 API class UptimeCheckConfig.Types.ContentMatcher.

Optional. Used to perform content matching. This allows matching based on substrings and regular expressions, together with their negations. Only the first 4&nbsp;MB of an HTTP or HTTPS check's response (and the first 1&nbsp;MB of a TCP check's response) are examined for purposes of content matching.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UptimeCheckConfig.Types.ContentMatcher

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UptimeCheckConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types)[ContentMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UptimeCheckConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types)[ContentMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UptimeCheckConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types)[ContentMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Monitoring.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3)

## Assembly

Google.Cloud.Monitoring.V3.dll

## Constructors 

### ContentMatcher()
    
    
    public ContentMatcher()

### ContentMatcher(ContentMatcher)
    
    
    public ContentMatcher(UptimeCheckConfig.Types.ContentMatcher other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UptimeCheckConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types)[ContentMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)`  
  
  
## Properties 

### AdditionalMatcherInfoCase
    
    
    public UptimeCheckConfig.Types.ContentMatcher.AdditionalMatcherInfoOneofCase AdditionalMatcherInfoCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[UptimeCheckConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types)[ContentMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)[AdditionalMatcherInfoOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher.AdditionalMatcherInfoOneofCase)` |   
  
### Content
    
    
    public string Content { get; set; }

String, regex or JSON content to match. Maximum 1024 bytes. An empty `content` string indicates no content matching is to be performed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### JsonPathMatcher
    
    
    public UptimeCheckConfig.Types.ContentMatcher.Types.JsonPathMatcher JsonPathMatcher { get; set; }

Matcher information for `MATCHES_JSON_PATH` and `NOT_MATCHES_JSON_PATH`

**Property Value**  
---  
**Type** | **Description**  
`[UptimeCheckConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types)[ContentMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher.Types)[JsonPathMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher.Types.JsonPathMatcher)` |   
  
### Matcher
    
    
    public UptimeCheckConfig.Types.ContentMatcher.Types.ContentMatcherOption Matcher { get; set; }

The type of content matcher that will be applied to the server output, compared to the `content` string when the check is run.

**Property Value**  
---  
**Type** | **Description**  
`[UptimeCheckConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types)[ContentMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher.Types)[ContentMatcherOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.UptimeCheckConfig.Types.ContentMatcher.Types.ContentMatcherOption)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
