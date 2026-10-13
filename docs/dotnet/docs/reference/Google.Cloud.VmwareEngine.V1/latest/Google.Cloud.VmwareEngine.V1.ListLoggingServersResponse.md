---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse
title: VMware Engine v1 API - Class ListLoggingServersResponse (1.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:40.844887+00:00
---

# VMware Engine v1 API - Class ListLoggingServersResponse (1.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  VMware Engine v1 API - Class ListLoggingServersResponse (1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.6.0/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.5.0/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.4.0/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.3.0/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.2.0/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.1.0/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.0.0/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse)


    
    
    public sealed class ListLoggingServersResponse : IMessage<ListLoggingServersResponse>, IEquatable<ListLoggingServersResponse>, IDeepCloneable<ListLoggingServersResponse>, IBufferMessage, IMessage, IPageResponse<LoggingServer>, IEnumerable<LoggingServer>, IEnumerable

Reference documentation and code samples for the VMware Engine v1 API class ListLoggingServersResponse.

Response message for [VmwareEngine.ListLoggingServers][google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers]

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListLoggingServersResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListLoggingServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListLoggingServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListLoggingServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[LoggingServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.LoggingServer), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[LoggingServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.LoggingServer), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VmwareEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1)

## Assembly

Google.Cloud.VmwareEngine.V1.dll

## Constructors 

### ListLoggingServersResponse()
    
    
    public ListLoggingServersResponse()

### ListLoggingServersResponse(ListLoggingServersResponse)
    
    
    public ListLoggingServersResponse(ListLoggingServersResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListLoggingServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ListLoggingServersResponse)`  
  
  
## Properties 

### LoggingServers
    
    
    public RepeatedField<LoggingServer> LoggingServers { get; }

A list of Logging Servers.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[LoggingServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.LoggingServer)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token, which can be send as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Unreachable
    
    
    public RepeatedField<string> Unreachable { get; }

Locations that could not be reached when making an aggregated query using wildcards.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<LoggingServer> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[LoggingServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.LoggingServer)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
