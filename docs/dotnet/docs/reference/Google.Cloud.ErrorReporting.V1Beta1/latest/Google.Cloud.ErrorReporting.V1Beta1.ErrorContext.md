---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ErrorContext
title: Google Cloud Error Reporting v1beta1 API - Class ErrorContext (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:31.645648+00:00
---

# Google Cloud Error Reporting v1beta1 API - Class ErrorContext (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ErrorContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Error Reporting v1beta1 API - Class ErrorContext (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ErrorContext)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/3.0.0-beta05/Google.Cloud.ErrorReporting.V1Beta1.ErrorContext)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/2.0.0-beta05/Google.Cloud.ErrorReporting.V1Beta1.ErrorContext)


    
    
    public sealed class ErrorContext : IMessage<ErrorContext>, IEquatable<ErrorContext>, IDeepCloneable<ErrorContext>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Error Reporting v1beta1 API class ErrorContext.

A description of the context in which an error occurred. This data should be provided by the application when reporting an error, unless the error report has been generated automatically from Google App Engine logs.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ErrorContext

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ErrorContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ErrorContext), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ErrorContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ErrorContext), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ErrorContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ErrorContext), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ErrorReporting.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1)

## Assembly

Google.Cloud.ErrorReporting.V1Beta1.dll

## Constructors 

### ErrorContext()
    
    
    public ErrorContext()

### ErrorContext(ErrorContext)
    
    
    public ErrorContext(ErrorContext other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ErrorContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ErrorContext)`  
  
  
## Properties 

### HttpRequest
    
    
    public HttpRequestContext HttpRequest { get; set; }

The HTTP request which was processed when the error was triggered.

**Property Value**  
---  
**Type** | **Description**  
`[HttpRequestContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.HttpRequestContext)` |   
  
### ReportLocation
    
    
    public SourceLocation ReportLocation { get; set; }

The location in the source code where the decision was made to report the error, usually the place where it was logged. For a logged exception this would be the source line where the exception is logged, usually close to the place where it was caught.

**Property Value**  
---  
**Type** | **Description**  
`[SourceLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.SourceLocation)` |   
  
### User
    
    
    public string User { get; set; }

The user who caused or was affected by the crash. This can be a user ID, an email address, or an arbitrary token that uniquely identifies the user. When sending an error report, leave this field empty if the user was not logged in. In this case the Error Reporting system will use other data, such as remote IP address, to distinguish affected users. See `affected_users_count` in `ErrorGroupStats`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
