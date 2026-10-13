---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRunLog
title: Web Security Scanner v1 API - Class ScanRunLog (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:58.217542+00:00
---

# Web Security Scanner v1 API - Class ScanRunLog (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRunLog

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Web Security Scanner v1 API - Class ScanRunLog (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.5.0/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.4.0/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.3.0/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.2.0/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.1.0/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.0.0/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/1.2.0/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/1.1.0/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/1.0.0/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)


    
    
    public sealed class ScanRunLog : IMessage<ScanRunLog>, IEquatable<ScanRunLog>, IDeepCloneable<ScanRunLog>, IBufferMessage, IMessage

Reference documentation and code samples for the Web Security Scanner v1 API class ScanRunLog.

A ScanRunLog is an output-only proto used for Stackdriver customer logging. It is used for logs covering the start and end of scan pipelines. Other than an added summary, this is a subset of the ScanRun. Representation in logs is either a proto Struct, or converted to JSON. Next id: 9

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ScanRunLog

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ScanRunLog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRunLog), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ScanRunLog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRunLog), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ScanRunLog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRunLog), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.WebSecurityScanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1)

## Assembly

Google.Cloud.WebSecurityScanner.V1.dll

## Constructors 

### ScanRunLog()
    
    
    public ScanRunLog()

### ScanRunLog(ScanRunLog)
    
    
    public ScanRunLog(ScanRunLog other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ScanRunLog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRunLog)`  
  
  
## Properties 

### ErrorTrace
    
    
    public ScanRunErrorTrace ErrorTrace { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[ScanRunErrorTrace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRunErrorTrace)` |   
  
### ExecutionState
    
    
    public ScanRun.Types.ExecutionState ExecutionState { get; set; }

The execution state of the ScanRun.

**Property Value**  
---  
**Type** | **Description**  
`[ScanRun](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRun)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRun.Types)[ExecutionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRun.Types.ExecutionState)` |   
  
### HasFindings
    
    
    public bool HasFindings { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Name
    
    
    public string Name { get; set; }

The resource name of the ScanRun being logged.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResultState
    
    
    public ScanRun.Types.ResultState ResultState { get; set; }

The result state of the ScanRun.

**Property Value**  
---  
**Type** | **Description**  
`[ScanRun](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRun)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRun.Types)[ResultState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ScanRun.Types.ResultState)` |   
  
### Summary
    
    
    public string Summary { get; set; }

Human friendly message about the event.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UrlsCrawledCount
    
    
    public long UrlsCrawledCount { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### UrlsTestedCount
    
    
    public long UrlsTestedCount { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
