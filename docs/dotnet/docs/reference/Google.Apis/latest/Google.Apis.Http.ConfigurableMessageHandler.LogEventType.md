---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Http.ConfigurableMessageHandler.LogEventType
title: Enum ConfigurableMessageHandler.LogEventType (1.73.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:32.377969+00:00
---

# Enum ConfigurableMessageHandler.LogEventType (1.73.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Http.ConfigurableMessageHandler.LogEventType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Enum ConfigurableMessageHandler.LogEventType (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.73.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Http.ConfigurableMessageHandler.LogEventType)
  * [ 1.69.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.69.0/Google.Apis.Http.ConfigurableMessageHandler.LogEventType)
  * [ 1.68.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.68.0/Google.Apis.Http.ConfigurableMessageHandler.LogEventType)
  * [ 1.60.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.60.0/Google.Apis.Http.ConfigurableMessageHandler.LogEventType)
  * [ 1.59.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.59.0/Google.Apis.Http.ConfigurableMessageHandler.LogEventType)
  * [ 1.55.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.55.0/Google.Apis.Http.ConfigurableMessageHandler.LogEventType)
  * [ 1.50.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.50.0/Google.Apis.Http.ConfigurableMessageHandler.LogEventType)


    
    
    [Flags]
    public enum ConfigurableMessageHandler.LogEventType

Specifies the type(s) of request/response events to log.

## Namespace

[Google.Apis.Http](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Http)

## Assembly

Google.Apis.Core.dll

## Fields   
  
---  
**Name** | **Description**  
`None` | Log no request/response information.  
`RequestBody` | Log the request body. The body is assumed to be ASCII, and non-printable charaters are replaced by '.'. Warning: This causes the body content to be buffered in memory, so use with care for large requests.  
`RequestHeaders` | Log the request headers.  
`RequestUri` | Log the request URI.  
`ResponseAbnormal` | Log abnormal response messages.  
`ResponseBody` | Log the response body. The body is assumed to be ASCII, and non-printable characters are replaced by '.'. Warning: This causes the body content to be buffered in memory, so use with care for large responses.  
`ResponseHeaders` | Log the response headers.  
`ResponseStatus` | Log the response status.  
  
## Extension Method

[Utilities.ThrowIfNull<ConfigurableMessageHandler.LogEventType>(ConfigurableMessageHandler.LogEventType, string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Util.Utilities#Google_Apis_Util_Utilities_ThrowIfNull__1___0_System_String_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
