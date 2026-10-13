---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download.IMediaDownloader
title: Interface IMediaDownloader (1.73.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:32.952830+00:00
---

# Interface IMediaDownloader (1.73.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download.IMediaDownloader

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Interface IMediaDownloader (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.73.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download.IMediaDownloader)
  * [ 1.69.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.69.0/Google.Apis.Download.IMediaDownloader)
  * [ 1.68.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.68.0/Google.Apis.Download.IMediaDownloader)
  * [ 1.60.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.60.0/Google.Apis.Download.IMediaDownloader)
  * [ 1.59.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.59.0/Google.Apis.Download.IMediaDownloader)
  * [ 1.55.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.55.0/Google.Apis.Download.IMediaDownloader)
  * [ 1.50.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.50.0/Google.Apis.Download.IMediaDownloader)


    
    
    public interface IMediaDownloader

Media download which uses download file part by part, by [ChunkSize](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download.IMediaDownloader#Google_Apis_Download_IMediaDownloader_ChunkSize).

## Namespace

[Google.Apis.Download](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download)

## Assembly

Google.Apis.dll

## Properties 

### ChunkSize
    
    
    int ChunkSize { get; set; }

Gets or sets the chunk size to download, it defines the size of each part.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Methods 

### Download(string, Stream)
    
    
    IDownloadProgress Download(string url, Stream stream)

Downloads synchronously the given URL to the given stream.

**Parameters**  
---  
**Name** | **Description**  
`url` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
  
`stream` | `[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IDownloadProgress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download.IDownloadProgress)` |   
  
### DownloadAsync(string, Stream)
    
    
    Task<IDownloadProgress> DownloadAsync(string url, Stream stream)

Downloads asynchronously the given URL to the given stream.

**Parameters**  
---  
**Name** | **Description**  
`url` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
  
`stream` | `[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IDownloadProgress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download.IDownloadProgress)` |   
  
### DownloadAsync(string, Stream, CancellationToken)
    
    
    Task<IDownloadProgress> DownloadAsync(string url, Stream stream, CancellationToken cancellationToken)

Downloads asynchronously the given URL to the given stream. This download method supports a cancellation token to cancel a request before it was completed.

**Parameters**  
---  
**Name** | **Description**  
`url` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
  
`stream` | `[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)`  
  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IDownloadProgress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download.IDownloadProgress)` |   
**Remarks**

In case the download fails [Exception](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download.IDownloadProgress#Google_Apis_Download_IDownloadProgress_Exception) will contain the exception that cause the failure. The only exception which will be thrown is [TaskCanceledException](https://learn.microsoft.com/dotnet/api/system.threading.tasks.taskcanceledexception) which indicates that the task was canceled.

## Events 

### ProgressChanged
    
    
    event Action<IDownloadProgress> ProgressChanged

An event which notifies when the download status has been changed.

**Event Type**  
---  
**Type** | **Description**  
`[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[IDownloadProgress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Download.IDownloadProgress)` |   
  
## Extension Method

[Utilities.ThrowIfNull<T>(T, string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Util.Utilities#Google_Apis_Util_Utilities_ThrowIfNull__1___0_System_String_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
