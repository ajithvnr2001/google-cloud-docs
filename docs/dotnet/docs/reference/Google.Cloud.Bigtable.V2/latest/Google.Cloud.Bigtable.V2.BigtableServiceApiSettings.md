---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings
title: Google Bigtable v2 API - Class BigtableServiceApiSettings (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:42.624091+00:00
---

# Google Bigtable v2 API - Class BigtableServiceApiSettings (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class BigtableServiceApiSettings (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class BigtableServiceApiSettings : ServiceSettingsBase

Reference documentation and code samples for the Google Bigtable v2 API class BigtableServiceApiSettings.

Settings for [BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > BigtableServiceApiSettings

## Inherited Members

[ServiceSettingsBase.VersionHeaderBuilder](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_VersionHeaderBuilder)

[ServiceSettingsBase.CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_CallSettings)

[ServiceSettingsBase.Clock](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Clock)

[ServiceSettingsBase.Scheduler](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Scheduler)

[ServiceSettingsBase.Interceptor](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Interceptor)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### BigtableServiceApiSettings()
    
    
    public BigtableServiceApiSettings()

Constructs a new [BigtableServiceApiSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings) object with default settings.

## Properties 

### AppProfileId
    
    
    public string AppProfileId { get; set; }

This value specifies routing for replication. If not specified, the "default" application profile will be used by the server.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CheckAndMutateRowSettings
    
    
    public CallSettings CheckAndMutateRowSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.CheckAndMutateRow` and `BigtableServiceApiClient.CheckAndMutateRowAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 20 seconds.



### ExecuteQuerySettings
    
    
    public CallSettings ExecuteQuerySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.ExecuteQuery` and `BigtableServiceApiClient.ExecuteQueryAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

Timeout: 43200 seconds.

### GenerateInitialChangeStreamPartitionsSettings
    
    
    public CallSettings GenerateInitialChangeStreamPartitionsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.GenerateInitialChangeStreamPartitions` and `BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetClientConfigurationSettings
    
    
    public CallSettings GetClientConfigurationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.GetClientConfiguration` and `BigtableServiceApiClient.GetClientConfigurationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### MaxChannels
    
    
    public uint MaxChannels { get; set; }

The maximum number of channels than will be open concurrently to the Bigtable endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
**Remarks**

Note that channels are managed and shared amongst [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient) instances using the same endpoint and channel options and which use the default credentials. So this property will have no bearing across clients using different options. To create a custom grouping of channels to be managed, create a [GcpCallInvoker](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.Gcp.GcpCallInvoker.html) manually and set the [CallInvoker](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ClientBuilderBase-1.html#Google_Api_Gax_Grpc_ClientBuilderBase_1_CallInvoker) property on a [BigtableClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClientBuilder), then build the client. 

**Example**
    
    
    // client1 and client3 will share the same GcpCallInvoker, since they both
    // use the same default settings. This means they will use the same shared
    // set of gRPC channels to the Bigtable service.
    // client2 and client4 will share a different GcpCallInvoker, since they both
    // use the same custom MaxChannels/PreferredMaxStreamsPerChannel settings.
    BigtableServiceApiSettings settings1 = BigtableServiceApiSettings.GetDefault();
    BigtableClient client1 = new BigtableClientBuilder { Settings = settings1 }.Build();
    
    BigtableServiceApiSettings settings2 = new BigtableServiceApiSettings
    {
        MaxChannels = 10,
        PreferredMaxStreamsPerChannel = 4
    };
    BigtableClient client2 = new BigtableClientBuilder { Settings = settings2 }.Build();
    
    BigtableServiceApiSettings settings3 = BigtableServiceApiSettings.GetDefault();
    BigtableClient client3 = new BigtableClientBuilder { Settings = settings3 }.Build();
    
    BigtableServiceApiSettings settings4 = new BigtableServiceApiSettings
    {
        MaxChannels = 10,
        PreferredMaxStreamsPerChannel = 4
    };
    BigtableClient client4 = new BigtableClientBuilder { Settings = settings4 }.Build();
    
    // client5 will not share a GcpCallInvoker with any of the other clients, since
    // its MaxChannels/PreferredMaxStreamsPerChannel settings differ from the others.
    BigtableServiceApiSettings settings5 = new BigtableServiceApiSettings
    {
        MaxChannels = 15,
        PreferredMaxStreamsPerChannel = 4
    };
    BigtableClient client5 = new BigtableClientBuilder { Settings = settings5 }.Build();
    

### MutateRowSettings
    
    
    public CallSettings MutateRowSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.MutateRow` and `BigtableServiceApiClient.MutateRowAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 10 milliseconds.
  * Retry delay multiplier: 2
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable), [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded). 
  * Timeout: 60 seconds.



### MutateRowsRetrySettings
    
    
    public RetrySettings MutateRowsRetrySettings { get; set; }

[RetrySettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html) for calls to `BigtableClient.MutateRows` and `BigtableClient.MutateRowsAsync` when some of the mutations fail for certain reasons.

**Property Value**  
---  
**Type** | **Description**  
`[RetrySettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html)` |   
**Remarks**

The default `BigtableClient.MutateRows` and `BigtableClient.MutateRowsAsync` [RetrySettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html) are:

  * Max attempts: 5
  * Initial retry delay: 10 milliseconds
  * Retry delay multiplier: 2.0
  * Retry maximum delay: 60000 milliseconds



Retry will be attempted on the following response status codes on individual mutations:

  * [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded)
  * [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable)



**See Also**

[MutateRowsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings#Google_Cloud_Bigtable_V2_BigtableServiceApiSettings_MutateRowsSettings)

### MutateRowsSettings
    
    
    public CallSettings MutateRowsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.MutateRows` and `BigtableServiceApiClient.MutateRowsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### OpenAuthorizedViewSettings
    
    
    public CallSettings OpenAuthorizedViewSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.OpenAuthorizedView` and `BigtableServiceApiClient.OpenAuthorizedViewAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### OpenAuthorizedViewStreamingSettings
    
    
    public BidirectionalStreamingSettings OpenAuthorizedViewStreamingSettings { get; set; }

[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html) for calls to `BigtableServiceApiClient.OpenAuthorizedView` and `BigtableServiceApiClient.OpenAuthorizedViewAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)` |   
**Remarks**

The default local send queue size is 100.

### OpenMaterializedViewSettings
    
    
    public CallSettings OpenMaterializedViewSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.OpenMaterializedView` and `BigtableServiceApiClient.OpenMaterializedViewAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### OpenMaterializedViewStreamingSettings
    
    
    public BidirectionalStreamingSettings OpenMaterializedViewStreamingSettings { get; set; }

[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html) for calls to `BigtableServiceApiClient.OpenMaterializedView` and `BigtableServiceApiClient.OpenMaterializedViewAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)` |   
**Remarks**

The default local send queue size is 100.

### OpenTableSettings
    
    
    public CallSettings OpenTableSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.OpenTable` and `BigtableServiceApiClient.OpenTableAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### OpenTableStreamingSettings
    
    
    public BidirectionalStreamingSettings OpenTableStreamingSettings { get; set; }

[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html) for calls to `BigtableServiceApiClient.OpenTable` and `BigtableServiceApiClient.OpenTableAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)` |   
**Remarks**

The default local send queue size is 100.

### PingAndWarmSettings
    
    
    public CallSettings PingAndWarmSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.PingAndWarm` and `BigtableServiceApiClient.PingAndWarmAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### PreferredMaxStreamsPerChannel
    
    
    public uint PreferredMaxStreamsPerChannel { get; set; }

The number of streams open concurrently in a channel which will trigger a new channel to be opened, as long as fewer than [MaxChannels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings#Google_Cloud_Bigtable_V2_BigtableServiceApiSettings_MaxChannels) are currently open.

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
**Remarks**

Note that channels are managed and shared amongst [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient) instances using the same endpoint and channel options and which use the default credentials. So this property will have no bearing across clients using different options. To create a custom grouping of channels to be managed, create a [GcpCallInvoker](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.Gcp.GcpCallInvoker.html) manually and set the [CallInvoker](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ClientBuilderBase-1.html#Google_Api_Gax_Grpc_ClientBuilderBase_1_CallInvoker) property on a [BigtableClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClientBuilder), then build the client. 

**Example**
    
    
    // client1 and client3 will share the same GcpCallInvoker, since they both
    // use the same default settings. This means they will use the same shared
    // set of gRPC channels to the Bigtable service.
    // client2 and client4 will share a different GcpCallInvoker, since they both
    // use the same custom MaxChannels/PreferredMaxStreamsPerChannel settings.
    BigtableServiceApiSettings settings1 = BigtableServiceApiSettings.GetDefault();
    BigtableClient client1 = new BigtableClientBuilder { Settings = settings1 }.Build();
    
    BigtableServiceApiSettings settings2 = new BigtableServiceApiSettings
    {
        MaxChannels = 10,
        PreferredMaxStreamsPerChannel = 4
    };
    BigtableClient client2 = new BigtableClientBuilder { Settings = settings2 }.Build();
    
    BigtableServiceApiSettings settings3 = BigtableServiceApiSettings.GetDefault();
    BigtableClient client3 = new BigtableClientBuilder { Settings = settings3 }.Build();
    
    BigtableServiceApiSettings settings4 = new BigtableServiceApiSettings
    {
        MaxChannels = 10,
        PreferredMaxStreamsPerChannel = 4
    };
    BigtableClient client4 = new BigtableClientBuilder { Settings = settings4 }.Build();
    
    // client5 will not share a GcpCallInvoker with any of the other clients, since
    // its MaxChannels/PreferredMaxStreamsPerChannel settings differ from the others.
    BigtableServiceApiSettings settings5 = new BigtableServiceApiSettings
    {
        MaxChannels = 15,
        PreferredMaxStreamsPerChannel = 4
    };
    BigtableClient client5 = new BigtableClientBuilder { Settings = settings5 }.Build();
    

### PrepareQuerySettings
    
    
    public CallSettings PrepareQuerySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.PrepareQuery` and `BigtableServiceApiClient.PrepareQueryAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ReadChangeStreamSettings
    
    
    public CallSettings ReadChangeStreamSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.ReadChangeStream` and `BigtableServiceApiClient.ReadChangeStreamAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 43200 seconds.



### ReadModifyWriteRowSettings
    
    
    public CallSettings ReadModifyWriteRowSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.ReadModifyWriteRow` and `BigtableServiceApiClient.ReadModifyWriteRowAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 20 seconds.



### ReadRowsRetrySettings
    
    
    public RetrySettings ReadRowsRetrySettings { get; set; }

[RetrySettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html) for calls to `BigtableClient.ReadRows` when the stream of results ends prematurely.

**Property Value**  
---  
**Type** | **Description**  
`[RetrySettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html)` |   
**Remarks**

The default `BigtableClient.ReadRows` [RetrySettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html) are:

  * Max attempts: 5
  * Initial retry delay: 10 milliseconds
  * Retry delay multiplier: 2.0
  * Retry maximum delay: 60000 milliseconds



Retry will be attempted on the following response status codes on individual mutations:

  * [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded)
  * [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable)
  * [Aborted](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Aborted)



**See Also**

[ReadRowsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings#Google_Cloud_Bigtable_V2_BigtableServiceApiSettings_ReadRowsSettings)

### ReadRowsSettings
    
    
    public CallSettings ReadRowsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.ReadRows` and `BigtableServiceApiClient.ReadRowsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 43200 seconds.



### SampleRowKeysSettings
    
    
    public CallSettings SampleRowKeysSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `BigtableServiceApiClient.SampleRowKeys` and `BigtableServiceApiClient.SampleRowKeysAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public BigtableServiceApiSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings)` | A deep clone of this [BigtableServiceApiSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings) object.  
  
### GetDefault()
    
    
    public static BigtableServiceApiSettings GetDefault()

Get a new instance of the default [BigtableServiceApiSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings).

**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings)` | A new instance of the default [BigtableServiceApiSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
