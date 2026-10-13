---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient
title: Vertex AI v1 API - Class DataFoundryServiceClient (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:05.696767+00:00
---

# Vertex AI v1 API - Class DataFoundryServiceClient (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class DataFoundryServiceClient (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class DataFoundryServiceClient

Reference documentation and code samples for the Vertex AI v1 API class DataFoundryServiceClient.

DataFoundryService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataFoundryServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[DataFoundryServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClientImpl)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Remarks

Service for generating and preparing datasets for Gen AI evaluation.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the DataFoundryService service, which is a host of "aiplatform.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default DataFoundryService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default DataFoundryService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual DataFoundryService.DataFoundryServiceClient GrpcClient { get; }

The underlying gRPC DataFoundryService client

**Property Value**  
---  
**Type** | **Description**  
`[DataFoundryService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryService)[DataFoundryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryService.DataFoundryServiceClient)` |   
  
### IAMPolicyClient
    
    
    public virtual IAMPolicyClient IAMPolicyClient { get; }

The [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static DataFoundryServiceClient Create()

Synchronously creates a [DataFoundryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataFoundryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClientBuilder) .

**Returns**  
---  
**Type** | **Description**  
`[DataFoundryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient)` | The created [DataFoundryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<DataFoundryServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [DataFoundryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataFoundryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClientBuilder) .

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataFoundryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient)` | The task representing the created [DataFoundryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient).  
  
### GenerateSyntheticData(GenerateSyntheticDataRequest, CallSettings)
    
    
    public virtual GenerateSyntheticDataResponse GenerateSyntheticData(GenerateSyntheticDataRequest request, CallSettings callSettings = null)

Generates synthetic data based on the provided configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateSyntheticDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateSyntheticDataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateSyntheticDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateSyntheticDataResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DataFoundryServiceClient dataFoundryServiceClient = DataFoundryServiceClient.Create();
    // Initialize request argument(s)
    GenerateSyntheticDataRequest request = new GenerateSyntheticDataRequest
    {
        LocationAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Count = 0,
        TaskDescription = new TaskDescriptionStrategy(),
        OutputFieldSpecs =
        {
            new OutputFieldSpec(),
        },
        Examples =
        {
            new SyntheticExample(),
        },
    };
    // Make the request
    GenerateSyntheticDataResponse response = dataFoundryServiceClient.GenerateSyntheticData(request);
    

### GenerateSyntheticDataAsync(GenerateSyntheticDataRequest, CallSettings)
    
    
    public virtual Task<GenerateSyntheticDataResponse> GenerateSyntheticDataAsync(GenerateSyntheticDataRequest request, CallSettings callSettings = null)

Generates synthetic data based on the provided configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateSyntheticDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateSyntheticDataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateSyntheticDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateSyntheticDataResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataFoundryServiceClient dataFoundryServiceClient = await DataFoundryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GenerateSyntheticDataRequest request = new GenerateSyntheticDataRequest
    {
        LocationAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Count = 0,
        TaskDescription = new TaskDescriptionStrategy(),
        OutputFieldSpecs =
        {
            new OutputFieldSpec(),
        },
        Examples =
        {
            new SyntheticExample(),
        },
    };
    // Make the request
    GenerateSyntheticDataResponse response = await dataFoundryServiceClient.GenerateSyntheticDataAsync(request);
    

### GenerateSyntheticDataAsync(GenerateSyntheticDataRequest, CancellationToken)
    
    
    public virtual Task<GenerateSyntheticDataResponse> GenerateSyntheticDataAsync(GenerateSyntheticDataRequest request, CancellationToken cancellationToken)

Generates synthetic data based on the provided configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateSyntheticDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateSyntheticDataRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateSyntheticDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateSyntheticDataResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataFoundryServiceClient dataFoundryServiceClient = await DataFoundryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GenerateSyntheticDataRequest request = new GenerateSyntheticDataRequest
    {
        LocationAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Count = 0,
        TaskDescription = new TaskDescriptionStrategy(),
        OutputFieldSpecs =
        {
            new OutputFieldSpec(),
        },
        Examples =
        {
            new SyntheticExample(),
        },
    };
    // Make the request
    GenerateSyntheticDataResponse response = await dataFoundryServiceClient.GenerateSyntheticDataAsync(request);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient#Google_Cloud_AIPlatform_V1_DataFoundryServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient#Google_Cloud_AIPlatform_V1_DataFoundryServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient#Google_Cloud_AIPlatform_V1_DataFoundryServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient#Google_Cloud_AIPlatform_V1_DataFoundryServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
