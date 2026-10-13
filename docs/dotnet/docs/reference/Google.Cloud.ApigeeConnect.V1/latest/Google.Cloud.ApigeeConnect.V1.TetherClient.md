---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient
title: Apigee Connect v1 API - Class TetherClient (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:28.520497+00:00
---

# Apigee Connect v1 API - Class TetherClient (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Apigee Connect v1 API - Class TetherClient (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.4.0/Google.Cloud.ApigeeConnect.V1.TetherClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.3.0/Google.Cloud.ApigeeConnect.V1.TetherClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.2.0/Google.Cloud.ApigeeConnect.V1.TetherClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.1.0/Google.Cloud.ApigeeConnect.V1.TetherClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.0.0/Google.Cloud.ApigeeConnect.V1.TetherClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/1.1.0/Google.Cloud.ApigeeConnect.V1.TetherClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/1.0.0/Google.Cloud.ApigeeConnect.V1.TetherClient)


    
    
    public abstract class TetherClient

Reference documentation and code samples for the Apigee Connect v1 API class TetherClient.

Tether client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TetherClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[TetherClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClientImpl)

## Namespace

[Google.Cloud.ApigeeConnect.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1)

## Assembly

Google.Cloud.ApigeeConnect.V1.dll

## Remarks

Tether provides a way for the control plane to send HTTP API requests to services in data planes that runs in a remote datacenter without requiring customers to open firewalls on their runtime plane.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Tether service, which is a host of "apigeeconnect.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Tether scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Tether scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual Tether.TetherClient GrpcClient { get; }

The underlying gRPC Tether client

**Property Value**  
---  
**Type** | **Description**  
`[Tether](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Tether)[TetherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Tether.TetherClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static TetherClient Create()

Synchronously creates a [TetherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [TetherClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[TetherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient)` | The created [TetherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<TetherClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [TetherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [TetherClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TetherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient)` | The task representing the created [TetherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient).  
  
### Egress(CallSettings, BidirectionalStreamingSettings)
    
    
    public virtual TetherClient.EgressStream Egress(CallSettings callSettings = null, BidirectionalStreamingSettings streamingSettings = null)

Egress streams egress requests and responses. Logically, this is not actually a streaming request, but uses streaming as a mechanism to flip the client-server relationship of gRPC so that the server can act as a client. The listener, the RPC server, accepts connections from the dialer, the RPC client. The listener streams http requests and the dialer streams http responses.

**Parameters**  
---  
**Name** | **Description**  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
`streamingSettings` | `[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)`  
If not null, applies streaming overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TetherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient)[EgressStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient.EgressStream)` | The client-server stream.  
**Example**
    
    
    // Create client
    gcav::TetherClient tetherClient = gcav::TetherClient.Create();
    // Initialize streaming call, retrieving the stream object
    using gcav::TetherClient.EgressStream response = tetherClient.Egress();
    
    // Sending requests and retrieving responses can be arbitrarily interleaved
    // Exact sequence will depend on client/server behavior
    
    // Create task to do something with responses from server
    Task responseHandlerTask = Task.Run(async () =>
    {
        // Note that C# 8 code can use await foreach
        AsyncResponseStream<gcav::EgressRequest> responseStream = response.GetResponseStream();
        while (await responseStream.MoveNextAsync())
        {
            gcav::EgressRequest responseItem = responseStream.Current;
            // Do something with streamed response
        }
        // The response stream has completed
    });
    
    // Send requests to the server
    bool done = false;
    while (!done)
    {
        // Initialize a request
        gcav::EgressResponse request = new gcav::EgressResponse
        {
            Id = "",
            HttpResponse = new gcav::HttpResponse(),
            Status = new Status(),
            Project = "",
            TraceId = "",
            Endpoint = gcav::TetherEndpoint.Unspecified,
            Name = "",
        };
        // Stream a request to the server
        await response.WriteAsync(request);
        // Set "done" to true when sending requests is complete
    }
    
    // Complete writing requests to the stream
    await response.WriteCompleteAsync();
    // Await the response handler
    // This will complete once all server responses have been processed
    await responseHandlerTask;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient#Google_Cloud_ApigeeConnect_V1_TetherClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient#Google_Cloud_ApigeeConnect_V1_TetherClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient#Google_Cloud_ApigeeConnect_V1_TetherClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.TetherClient#Google_Cloud_ApigeeConnect_V1_TetherClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
