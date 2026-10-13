---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase
title: Apigee Connect v1 API - Class ConnectionService.ConnectionServiceBase (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:24.084622+00:00
---

# Apigee Connect v1 API - Class ConnectionService.ConnectionServiceBase (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Apigee Connect v1 API - Class ConnectionService.ConnectionServiceBase (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.4.0/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.3.0/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.2.0/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.1.0/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.0.0/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/1.1.0/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/1.0.0/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)


    
    
    [BindServiceMethod(typeof(ConnectionService), "BindService")]
    public abstract class ConnectionService.ConnectionServiceBase

Reference documentation and code samples for the Apigee Connect v1 API class ConnectionService.ConnectionServiceBase.

Base class for server-side implementations of ConnectionService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConnectionService.ConnectionServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApigeeConnect.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1)

## Assembly

Google.Cloud.ApigeeConnect.V1.dll

## Methods 

### ListConnections(ListConnectionsRequest, ServerCallContext)
    
    
    public virtual Task<ListConnectionsResponse> ListConnections(ListConnectionsRequest request, ServerCallContext context)

Lists connections that are currently active for the given Apigee Connect endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
