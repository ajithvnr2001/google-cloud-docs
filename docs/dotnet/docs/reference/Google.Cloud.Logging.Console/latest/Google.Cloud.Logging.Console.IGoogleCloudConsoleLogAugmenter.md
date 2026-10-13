---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/latest/Google.Cloud.Logging.Console.IGoogleCloudConsoleLogAugmenter
title: Google.Cloud.Logging.Console - Interface IGoogleCloudConsoleLogAugmenter (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:46.922037+00:00
---

# Google.Cloud.Logging.Console - Interface IGoogleCloudConsoleLogAugmenter (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/latest/Google.Cloud.Logging.Console.IGoogleCloudConsoleLogAugmenter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Logging.Console - Interface IGoogleCloudConsoleLogAugmenter (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/latest/Google.Cloud.Logging.Console.IGoogleCloudConsoleLogAugmenter)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.5.0/Google.Cloud.Logging.Console.IGoogleCloudConsoleLogAugmenter)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.4.0/Google.Cloud.Logging.Console.IGoogleCloudConsoleLogAugmenter)
  * [ 1.3.1 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.3.1/Google.Cloud.Logging.Console.IGoogleCloudConsoleLogAugmenter)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.2.0/Google.Cloud.Logging.Console.IGoogleCloudConsoleLogAugmenter)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.1.0/Google.Cloud.Logging.Console.IGoogleCloudConsoleLogAugmenter)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.0.0/Google.Cloud.Logging.Console.IGoogleCloudConsoleLogAugmenter)


    
    
    public interface IGoogleCloudConsoleLogAugmenter

Reference documentation and code samples for the Google.Cloud.Logging.Console interface IGoogleCloudConsoleLogAugmenter.

Allows augmenting formatted log entries with information not included by [GoogleCloudConsoleFormatter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/latest/Google.Cloud.Logging.Console.GoogleCloudConsoleFormatter).

## Namespace

[Google.Cloud.Logging.Console](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/latest/Google.Cloud.Logging.Console)

## Assembly

Google.Cloud.Logging.Console.dll

## Methods 

### AugmentFormattedLogEntry<TState>(in LogEntry<TState>, IExternalScopeProvider, Utf8JsonWriter)
    
    
    void AugmentFormattedLogEntry<TState>(in LogEntry<TState> logEntry, IExternalScopeProvider scopeProvider, Utf8JsonWriter writer)

Augments the formatted log entry with information not included by [GoogleCloudConsoleFormatter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/latest/Google.Cloud.Logging.Console.GoogleCloudConsoleFormatter).

**Parameters**  
---  
**Name** | **Description**  
`logEntry` | `[LogEntry](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.abstractions.logentry-1)`  
The log entry that's being formatted.  
`scopeProvider` | `[IExternalScopeProvider](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.iexternalscopeprovider)`  
The provider of scope data.  
`writer` | `[Utf8JsonWriter](https://learn.microsoft.com/dotnet/api/system.text.json.utf8jsonwriter)`  
The JSON writer containing the start of the formatted log entry, meaning that [WriteStartObject()](https://learn.microsoft.com/dotnet/api/system.text.json.utf8jsonwriter.writestartobject#system-text-json-utf8jsonwriter-writestartobject) has been called for the top level JSON object and some fields have been written but [WriteEndObject()](https://learn.microsoft.com/dotnet/api/system.text.json.utf8jsonwriter.writeendobject) is yet to be called for the top level JSON object. Do not call [WriteEndObject()](https://learn.microsoft.com/dotnet/api/system.text.json.utf8jsonwriter.writeendobject) for the top level JSON object.  
**Type Parameter**  
---  
**Name** | **Description**  
`TState` | The type of the state information attached to the log entry.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
