---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient
title: Assured Workloads v1 API - Class AssuredWorkloadsServiceClient (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:06.191197+00:00
---

# Assured Workloads v1 API - Class AssuredWorkloadsServiceClient (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Assured Workloads v1 API - Class AssuredWorkloadsServiceClient (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.6.0/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.5.0/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.4.0/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.3.0/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.2.0/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.1.0/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.0.0/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.1.0/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.0.0/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)


    
    
    public abstract class AssuredWorkloadsServiceClient

Reference documentation and code samples for the Assured Workloads v1 API class AssuredWorkloadsServiceClient.

AssuredWorkloadsService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AssuredWorkloadsServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AssuredWorkloadsServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClientImpl)

## Namespace

[Google.Cloud.AssuredWorkloads.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1)

## Assembly

Google.Cloud.AssuredWorkloads.V1.dll

## Remarks

Service to manage AssuredWorkloads.

## Properties 

### CreateWorkloadOperationsClient
    
    
    public virtual OperationsClient CreateWorkloadOperationsClient { get; }

The long-running operations client for `CreateWorkload`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AssuredWorkloadsService service, which is a host of "assuredworkloads.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AssuredWorkloadsService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AssuredWorkloadsService scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual AssuredWorkloadsService.AssuredWorkloadsServiceClient GrpcClient { get; }

The underlying gRPC AssuredWorkloadsService client

**Property Value**  
---  
**Type** | **Description**  
`[AssuredWorkloadsService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsService)[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsService.AssuredWorkloadsServiceClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### AcknowledgeViolation(AcknowledgeViolationRequest, CallSettings)
    
    
    public virtual AcknowledgeViolationResponse AcknowledgeViolation(AcknowledgeViolationRequest request, CallSettings callSettings = null)

Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcknowledgeViolationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AcknowledgeViolationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AcknowledgeViolationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AcknowledgeViolationResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    AcknowledgeViolationRequest request = new AcknowledgeViolationRequest
    {
        Name = "",
        Comment = "",
    };
    // Make the request
    AcknowledgeViolationResponse response = assuredWorkloadsServiceClient.AcknowledgeViolation(request);
    

### AcknowledgeViolationAsync(AcknowledgeViolationRequest, CallSettings)
    
    
    public virtual Task<AcknowledgeViolationResponse> AcknowledgeViolationAsync(AcknowledgeViolationRequest request, CallSettings callSettings = null)

Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcknowledgeViolationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AcknowledgeViolationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AcknowledgeViolationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AcknowledgeViolationResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    AcknowledgeViolationRequest request = new AcknowledgeViolationRequest
    {
        Name = "",
        Comment = "",
    };
    // Make the request
    AcknowledgeViolationResponse response = await assuredWorkloadsServiceClient.AcknowledgeViolationAsync(request);
    

### AcknowledgeViolationAsync(AcknowledgeViolationRequest, CancellationToken)
    
    
    public virtual Task<AcknowledgeViolationResponse> AcknowledgeViolationAsync(AcknowledgeViolationRequest request, CancellationToken cancellationToken)

Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcknowledgeViolationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AcknowledgeViolationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AcknowledgeViolationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AcknowledgeViolationResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    AcknowledgeViolationRequest request = new AcknowledgeViolationRequest
    {
        Name = "",
        Comment = "",
    };
    // Make the request
    AcknowledgeViolationResponse response = await assuredWorkloadsServiceClient.AcknowledgeViolationAsync(request);
    

### Create()
    
    
    public static AssuredWorkloadsServiceClient Create()

Synchronously creates a [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AssuredWorkloadsServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)` | The created [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AssuredWorkloadsServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AssuredWorkloadsServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient)` | The task representing the created [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient).  
  
### CreateWorkload(CreateWorkloadRequest, CallSettings)
    
    
    public virtual Operation<Workload, CreateWorkloadOperationMetadata> CreateWorkload(CreateWorkloadRequest request, CallSettings callSettings = null)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    CreateWorkloadRequest request = new CreateWorkloadRequest
    {
        ParentAsLocationName = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Workload = new Workload(),
        ExternalId = "",
    };
    // Make the request
    Operation<Workload, CreateWorkloadOperationMetadata> response = assuredWorkloadsServiceClient.CreateWorkload(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, CreateWorkloadOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, CreateWorkloadOperationMetadata> retrievedResponse = assuredWorkloadsServiceClient.PollOnceCreateWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkload(LocationName, Workload, CallSettings)
    
    
    public virtual Operation<Workload, CreateWorkloadOperationMetadata> CreateWorkload(LocationName parent, Workload workload, CallSettings callSettings = null)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.LocationName)`  
Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{location_id}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
Required. Assured Workload to create  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    Workload workload = new Workload();
    // Make the request
    Operation<Workload, CreateWorkloadOperationMetadata> response = assuredWorkloadsServiceClient.CreateWorkload(parent, workload);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, CreateWorkloadOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, CreateWorkloadOperationMetadata> retrievedResponse = assuredWorkloadsServiceClient.PollOnceCreateWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkload(string, Workload, CallSettings)
    
    
    public virtual Operation<Workload, CreateWorkloadOperationMetadata> CreateWorkload(string parent, Workload workload, CallSettings callSettings = null)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{location_id}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
Required. Assured Workload to create  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    Workload workload = new Workload();
    // Make the request
    Operation<Workload, CreateWorkloadOperationMetadata> response = assuredWorkloadsServiceClient.CreateWorkload(parent, workload);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, CreateWorkloadOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, CreateWorkloadOperationMetadata> retrievedResponse = assuredWorkloadsServiceClient.PollOnceCreateWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(CreateWorkloadRequest, CallSettings)
    
    
    public virtual Task<Operation<Workload, CreateWorkloadOperationMetadata>> CreateWorkloadAsync(CreateWorkloadRequest request, CallSettings callSettings = null)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateWorkloadRequest request = new CreateWorkloadRequest
    {
        ParentAsLocationName = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Workload = new Workload(),
        ExternalId = "",
    };
    // Make the request
    Operation<Workload, CreateWorkloadOperationMetadata> response = await assuredWorkloadsServiceClient.CreateWorkloadAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, CreateWorkloadOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, CreateWorkloadOperationMetadata> retrievedResponse = await assuredWorkloadsServiceClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(CreateWorkloadRequest, CancellationToken)
    
    
    public virtual Task<Operation<Workload, CreateWorkloadOperationMetadata>> CreateWorkloadAsync(CreateWorkloadRequest request, CancellationToken cancellationToken)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateWorkloadRequest request = new CreateWorkloadRequest
    {
        ParentAsLocationName = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Workload = new Workload(),
        ExternalId = "",
    };
    // Make the request
    Operation<Workload, CreateWorkloadOperationMetadata> response = await assuredWorkloadsServiceClient.CreateWorkloadAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, CreateWorkloadOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, CreateWorkloadOperationMetadata> retrievedResponse = await assuredWorkloadsServiceClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(LocationName, Workload, CallSettings)
    
    
    public virtual Task<Operation<Workload, CreateWorkloadOperationMetadata>> CreateWorkloadAsync(LocationName parent, Workload workload, CallSettings callSettings = null)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.LocationName)`  
Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{location_id}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
Required. Assured Workload to create  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    Workload workload = new Workload();
    // Make the request
    Operation<Workload, CreateWorkloadOperationMetadata> response = await assuredWorkloadsServiceClient.CreateWorkloadAsync(parent, workload);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, CreateWorkloadOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, CreateWorkloadOperationMetadata> retrievedResponse = await assuredWorkloadsServiceClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(LocationName, Workload, CancellationToken)
    
    
    public virtual Task<Operation<Workload, CreateWorkloadOperationMetadata>> CreateWorkloadAsync(LocationName parent, Workload workload, CancellationToken cancellationToken)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.LocationName)`  
Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{location_id}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
Required. Assured Workload to create  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    Workload workload = new Workload();
    // Make the request
    Operation<Workload, CreateWorkloadOperationMetadata> response = await assuredWorkloadsServiceClient.CreateWorkloadAsync(parent, workload);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, CreateWorkloadOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, CreateWorkloadOperationMetadata> retrievedResponse = await assuredWorkloadsServiceClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(string, Workload, CallSettings)
    
    
    public virtual Task<Operation<Workload, CreateWorkloadOperationMetadata>> CreateWorkloadAsync(string parent, Workload workload, CallSettings callSettings = null)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{location_id}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
Required. Assured Workload to create  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    Workload workload = new Workload();
    // Make the request
    Operation<Workload, CreateWorkloadOperationMetadata> response = await assuredWorkloadsServiceClient.CreateWorkloadAsync(parent, workload);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, CreateWorkloadOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, CreateWorkloadOperationMetadata> retrievedResponse = await assuredWorkloadsServiceClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(string, Workload, CancellationToken)
    
    
    public virtual Task<Operation<Workload, CreateWorkloadOperationMetadata>> CreateWorkloadAsync(string parent, Workload workload, CancellationToken cancellationToken)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{location_id}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
Required. Assured Workload to create  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    Workload workload = new Workload();
    // Make the request
    Operation<Workload, CreateWorkloadOperationMetadata> response = await assuredWorkloadsServiceClient.CreateWorkloadAsync(parent, workload);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, CreateWorkloadOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, CreateWorkloadOperationMetadata> retrievedResponse = await assuredWorkloadsServiceClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkload(DeleteWorkloadRequest, CallSettings)
    
    
    public virtual void DeleteWorkload(DeleteWorkloadRequest request, CallSettings callSettings = null)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.DeleteWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    DeleteWorkloadRequest request = new DeleteWorkloadRequest
    {
        WorkloadName = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]"),
        Etag = "",
    };
    // Make the request
    assuredWorkloadsServiceClient.DeleteWorkload(request);
    

### DeleteWorkload(WorkloadName, CallSettings)
    
    
    public virtual void DeleteWorkload(WorkloadName name, CallSettings callSettings = null)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)`  
Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
    // Make the request
    assuredWorkloadsServiceClient.DeleteWorkload(name);
    

### DeleteWorkload(string, CallSettings)
    
    
    public virtual void DeleteWorkload(string name, CallSettings callSettings = null)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]";
    // Make the request
    assuredWorkloadsServiceClient.DeleteWorkload(name);
    

### DeleteWorkloadAsync(DeleteWorkloadRequest, CallSettings)
    
    
    public virtual Task DeleteWorkloadAsync(DeleteWorkloadRequest request, CallSettings callSettings = null)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.DeleteWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteWorkloadRequest request = new DeleteWorkloadRequest
    {
        WorkloadName = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]"),
        Etag = "",
    };
    // Make the request
    await assuredWorkloadsServiceClient.DeleteWorkloadAsync(request);
    

### DeleteWorkloadAsync(DeleteWorkloadRequest, CancellationToken)
    
    
    public virtual Task DeleteWorkloadAsync(DeleteWorkloadRequest request, CancellationToken cancellationToken)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.DeleteWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteWorkloadRequest request = new DeleteWorkloadRequest
    {
        WorkloadName = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]"),
        Etag = "",
    };
    // Make the request
    await assuredWorkloadsServiceClient.DeleteWorkloadAsync(request);
    

### DeleteWorkloadAsync(WorkloadName, CallSettings)
    
    
    public virtual Task DeleteWorkloadAsync(WorkloadName name, CallSettings callSettings = null)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)`  
Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
    // Make the request
    await assuredWorkloadsServiceClient.DeleteWorkloadAsync(name);
    

### DeleteWorkloadAsync(WorkloadName, CancellationToken)
    
    
    public virtual Task DeleteWorkloadAsync(WorkloadName name, CancellationToken cancellationToken)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)`  
Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
    // Make the request
    await assuredWorkloadsServiceClient.DeleteWorkloadAsync(name);
    

### DeleteWorkloadAsync(string, CallSettings)
    
    
    public virtual Task DeleteWorkloadAsync(string name, CallSettings callSettings = null)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]";
    // Make the request
    await assuredWorkloadsServiceClient.DeleteWorkloadAsync(name);
    

### DeleteWorkloadAsync(string, CancellationToken)
    
    
    public virtual Task DeleteWorkloadAsync(string name, CancellationToken cancellationToken)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]";
    // Make the request
    await assuredWorkloadsServiceClient.DeleteWorkloadAsync(name);
    

### GetViolation(GetViolationRequest, CallSettings)
    
    
    public virtual Violation GetViolation(GetViolationRequest request, CallSettings callSettings = null)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetViolationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.GetViolationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    GetViolationRequest request = new GetViolationRequest
    {
        ViolationName = ViolationName.FromOrganizationLocationWorkloadViolation("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]"),
    };
    // Make the request
    Violation response = assuredWorkloadsServiceClient.GetViolation(request);
    

### GetViolation(ViolationName, CallSettings)
    
    
    public virtual Violation GetViolation(ViolationName name, CallSettings callSettings = null)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)`  
Required. The resource name of the Violation to fetch (ie. Violation.name). Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    ViolationName name = ViolationName.FromOrganizationLocationWorkloadViolation("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]");
    // Make the request
    Violation response = assuredWorkloadsServiceClient.GetViolation(name);
    

### GetViolation(string, CallSettings)
    
    
    public virtual Violation GetViolation(string name, CallSettings callSettings = null)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Violation to fetch (ie. Violation.name). Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]/violations/[VIOLATION]";
    // Make the request
    Violation response = assuredWorkloadsServiceClient.GetViolation(name);
    

### GetViolationAsync(GetViolationRequest, CallSettings)
    
    
    public virtual Task<Violation> GetViolationAsync(GetViolationRequest request, CallSettings callSettings = null)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetViolationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.GetViolationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetViolationRequest request = new GetViolationRequest
    {
        ViolationName = ViolationName.FromOrganizationLocationWorkloadViolation("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]"),
    };
    // Make the request
    Violation response = await assuredWorkloadsServiceClient.GetViolationAsync(request);
    

### GetViolationAsync(GetViolationRequest, CancellationToken)
    
    
    public virtual Task<Violation> GetViolationAsync(GetViolationRequest request, CancellationToken cancellationToken)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetViolationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.GetViolationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetViolationRequest request = new GetViolationRequest
    {
        ViolationName = ViolationName.FromOrganizationLocationWorkloadViolation("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]"),
    };
    // Make the request
    Violation response = await assuredWorkloadsServiceClient.GetViolationAsync(request);
    

### GetViolationAsync(ViolationName, CallSettings)
    
    
    public virtual Task<Violation> GetViolationAsync(ViolationName name, CallSettings callSettings = null)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)`  
Required. The resource name of the Violation to fetch (ie. Violation.name). Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    ViolationName name = ViolationName.FromOrganizationLocationWorkloadViolation("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]");
    // Make the request
    Violation response = await assuredWorkloadsServiceClient.GetViolationAsync(name);
    

### GetViolationAsync(ViolationName, CancellationToken)
    
    
    public virtual Task<Violation> GetViolationAsync(ViolationName name, CancellationToken cancellationToken)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)`  
Required. The resource name of the Violation to fetch (ie. Violation.name). Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    ViolationName name = ViolationName.FromOrganizationLocationWorkloadViolation("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]");
    // Make the request
    Violation response = await assuredWorkloadsServiceClient.GetViolationAsync(name);
    

### GetViolationAsync(string, CallSettings)
    
    
    public virtual Task<Violation> GetViolationAsync(string name, CallSettings callSettings = null)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Violation to fetch (ie. Violation.name). Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]/violations/[VIOLATION]";
    // Make the request
    Violation response = await assuredWorkloadsServiceClient.GetViolationAsync(name);
    

### GetViolationAsync(string, CancellationToken)
    
    
    public virtual Task<Violation> GetViolationAsync(string name, CancellationToken cancellationToken)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Violation to fetch (ie. Violation.name). Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]/violations/[VIOLATION]";
    // Make the request
    Violation response = await assuredWorkloadsServiceClient.GetViolationAsync(name);
    

### GetWorkload(GetWorkloadRequest, CallSettings)
    
    
    public virtual Workload GetWorkload(GetWorkloadRequest request, CallSettings callSettings = null)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    GetWorkloadRequest request = new GetWorkloadRequest
    {
        WorkloadName = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]"),
    };
    // Make the request
    Workload response = assuredWorkloadsServiceClient.GetWorkload(request);
    

### GetWorkload(WorkloadName, CallSettings)
    
    
    public virtual Workload GetWorkload(WorkloadName name, CallSettings callSettings = null)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)`  
Required. The resource name of the Workload to fetch. This is the workload's relative path in the API, formatted as "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
    // Make the request
    Workload response = assuredWorkloadsServiceClient.GetWorkload(name);
    

### GetWorkload(string, CallSettings)
    
    
    public virtual Workload GetWorkload(string name, CallSettings callSettings = null)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Workload to fetch. This is the workload's relative path in the API, formatted as "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]";
    // Make the request
    Workload response = assuredWorkloadsServiceClient.GetWorkload(name);
    

### GetWorkloadAsync(GetWorkloadRequest, CallSettings)
    
    
    public virtual Task<Workload> GetWorkloadAsync(GetWorkloadRequest request, CallSettings callSettings = null)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetWorkloadRequest request = new GetWorkloadRequest
    {
        WorkloadName = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]"),
    };
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.GetWorkloadAsync(request);
    

### GetWorkloadAsync(GetWorkloadRequest, CancellationToken)
    
    
    public virtual Task<Workload> GetWorkloadAsync(GetWorkloadRequest request, CancellationToken cancellationToken)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetWorkloadRequest request = new GetWorkloadRequest
    {
        WorkloadName = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]"),
    };
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.GetWorkloadAsync(request);
    

### GetWorkloadAsync(WorkloadName, CallSettings)
    
    
    public virtual Task<Workload> GetWorkloadAsync(WorkloadName name, CallSettings callSettings = null)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)`  
Required. The resource name of the Workload to fetch. This is the workload's relative path in the API, formatted as "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.GetWorkloadAsync(name);
    

### GetWorkloadAsync(WorkloadName, CancellationToken)
    
    
    public virtual Task<Workload> GetWorkloadAsync(WorkloadName name, CancellationToken cancellationToken)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)`  
Required. The resource name of the Workload to fetch. This is the workload's relative path in the API, formatted as "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1".  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.GetWorkloadAsync(name);
    

### GetWorkloadAsync(string, CallSettings)
    
    
    public virtual Task<Workload> GetWorkloadAsync(string name, CallSettings callSettings = null)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Workload to fetch. This is the workload's relative path in the API, formatted as "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]";
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.GetWorkloadAsync(name);
    

### GetWorkloadAsync(string, CancellationToken)
    
    
    public virtual Task<Workload> GetWorkloadAsync(string name, CancellationToken cancellationToken)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Workload to fetch. This is the workload's relative path in the API, formatted as "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1".  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]";
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.GetWorkloadAsync(name);
    

### ListViolations(ListViolationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListViolationsResponse, Violation> ListViolations(ListViolationsRequest request, CallSettings callSettings = null)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListViolationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListViolationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListViolationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListViolationsResponse)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A pageable sequence of [Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    ListViolationsRequest request = new ListViolationsRequest
    {
        ParentAsWorkloadName = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]"),
        Interval = new TimeWindow(),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListViolationsResponse, Violation> response = assuredWorkloadsServiceClient.ListViolations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Violation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListViolationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Violation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Violation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Violation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListViolations(WorkloadName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListViolationsResponse, Violation> ListViolations(WorkloadName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)`  
Required. The Workload name. Format `organizations/{org_id}/locations/{location}/workloads/{workload}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListViolationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListViolationsResponse)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A pageable sequence of [Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    WorkloadName parent = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
    // Make the request
    PagedEnumerable<ListViolationsResponse, Violation> response = assuredWorkloadsServiceClient.ListViolations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Violation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListViolationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Violation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Violation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Violation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListViolations(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListViolationsResponse, Violation> ListViolations(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Workload name. Format `organizations/{org_id}/locations/{location}/workloads/{workload}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListViolationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListViolationsResponse)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A pageable sequence of [Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]";
    // Make the request
    PagedEnumerable<ListViolationsResponse, Violation> response = assuredWorkloadsServiceClient.ListViolations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Violation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListViolationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Violation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Violation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Violation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListViolationsAsync(ListViolationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListViolationsResponse, Violation> ListViolationsAsync(ListViolationsRequest request, CallSettings callSettings = null)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListViolationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListViolationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListViolationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListViolationsResponse)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A pageable asynchronous sequence of [Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListViolationsRequest request = new ListViolationsRequest
    {
        ParentAsWorkloadName = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]"),
        Interval = new TimeWindow(),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListViolationsResponse, Violation> response = assuredWorkloadsServiceClient.ListViolationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Violation item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListViolationsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Violation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Violation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Violation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListViolationsAsync(WorkloadName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListViolationsResponse, Violation> ListViolationsAsync(WorkloadName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)`  
Required. The Workload name. Format `organizations/{org_id}/locations/{location}/workloads/{workload}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListViolationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListViolationsResponse)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A pageable asynchronous sequence of [Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName parent = WorkloadName.FromOrganizationLocationWorkload("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
    // Make the request
    PagedAsyncEnumerable<ListViolationsResponse, Violation> response = assuredWorkloadsServiceClient.ListViolationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Violation item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListViolationsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Violation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Violation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Violation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListViolationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListViolationsResponse, Violation> ListViolationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Workload name. Format `organizations/{org_id}/locations/{location}/workloads/{workload}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListViolationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListViolationsResponse)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)` | A pageable asynchronous sequence of [Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]/workloads/[WORKLOAD]";
    // Make the request
    PagedAsyncEnumerable<ListViolationsResponse, Violation> response = assuredWorkloadsServiceClient.ListViolationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Violation item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListViolationsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Violation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Violation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Violation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(ListWorkloadsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, Workload> ListWorkloads(ListWorkloadsRequest request, CallSettings callSettings = null)

Lists Assured Workloads under a CRM Node.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A pageable sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    ListWorkloadsRequest request = new ListWorkloadsRequest
    {
        ParentAsLocationName = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListWorkloadsResponse, Workload> response = assuredWorkloadsServiceClient.ListWorkloads(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Workload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, Workload> ListWorkloads(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Assured Workloads under a CRM Node.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.LocationName)`  
Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A pageable sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListWorkloadsResponse, Workload> response = assuredWorkloadsServiceClient.ListWorkloads(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Workload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, Workload> ListWorkloads(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Assured Workloads under a CRM Node.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A pageable sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListWorkloadsResponse, Workload> response = assuredWorkloadsServiceClient.ListWorkloads(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Workload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloadsAsync(ListWorkloadsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, Workload> ListWorkloadsAsync(ListWorkloadsRequest request, CallSettings callSettings = null)

Lists Assured Workloads under a CRM Node.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A pageable asynchronous sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListWorkloadsRequest request = new ListWorkloadsRequest
    {
        ParentAsLocationName = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListWorkloadsResponse, Workload> response = assuredWorkloadsServiceClient.ListWorkloadsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Workload item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListWorkloadsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloadsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, Workload> ListWorkloadsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Assured Workloads under a CRM Node.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.LocationName)`  
Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A pageable asynchronous sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListWorkloadsResponse, Workload> response = assuredWorkloadsServiceClient.ListWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Workload item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListWorkloadsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloadsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, Workload> ListWorkloadsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Assured Workloads under a CRM Node.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A pageable asynchronous sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListWorkloadsResponse, Workload> response = assuredWorkloadsServiceClient.ListWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Workload item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListWorkloadsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateWorkload(string, CallSettings)
    
    
    public virtual Operation<Workload, CreateWorkloadOperationMetadata> PollOnceCreateWorkload(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateWorkload`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateWorkloadAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Workload, CreateWorkloadOperationMetadata>> PollOnceCreateWorkloadAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateWorkload`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.CreateWorkloadOperationMetadata)` | A task representing the result of polling the operation.  
  
### RestrictAllowedResources(RestrictAllowedResourcesRequest, CallSettings)
    
    
    public virtual RestrictAllowedResourcesResponse RestrictAllowedResources(RestrictAllowedResourcesRequest request, CallSettings callSettings = null)

Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestrictAllowedResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.RestrictAllowedResourcesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.RestrictAllowedResourcesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    RestrictAllowedResourcesRequest request = new RestrictAllowedResourcesRequest
    {
        Name = "",
        RestrictionType = RestrictAllowedResourcesRequest.Types.RestrictionType.Unspecified,
    };
    // Make the request
    RestrictAllowedResourcesResponse response = assuredWorkloadsServiceClient.RestrictAllowedResources(request);
    

### RestrictAllowedResourcesAsync(RestrictAllowedResourcesRequest, CallSettings)
    
    
    public virtual Task<RestrictAllowedResourcesResponse> RestrictAllowedResourcesAsync(RestrictAllowedResourcesRequest request, CallSettings callSettings = null)

Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestrictAllowedResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.RestrictAllowedResourcesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.RestrictAllowedResourcesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    RestrictAllowedResourcesRequest request = new RestrictAllowedResourcesRequest
    {
        Name = "",
        RestrictionType = RestrictAllowedResourcesRequest.Types.RestrictionType.Unspecified,
    };
    // Make the request
    RestrictAllowedResourcesResponse response = await assuredWorkloadsServiceClient.RestrictAllowedResourcesAsync(request);
    

### RestrictAllowedResourcesAsync(RestrictAllowedResourcesRequest, CancellationToken)
    
    
    public virtual Task<RestrictAllowedResourcesResponse> RestrictAllowedResourcesAsync(RestrictAllowedResourcesRequest request, CancellationToken cancellationToken)

Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestrictAllowedResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.RestrictAllowedResourcesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.RestrictAllowedResourcesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    RestrictAllowedResourcesRequest request = new RestrictAllowedResourcesRequest
    {
        Name = "",
        RestrictionType = RestrictAllowedResourcesRequest.Types.RestrictionType.Unspecified,
    };
    // Make the request
    RestrictAllowedResourcesResponse response = await assuredWorkloadsServiceClient.RestrictAllowedResourcesAsync(request);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient#Google_Cloud_AssuredWorkloads_V1_AssuredWorkloadsServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient#Google_Cloud_AssuredWorkloads_V1_AssuredWorkloadsServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient#Google_Cloud_AssuredWorkloads_V1_AssuredWorkloadsServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.AssuredWorkloadsServiceClient#Google_Cloud_AssuredWorkloads_V1_AssuredWorkloadsServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateWorkload(UpdateWorkloadRequest, CallSettings)
    
    
    public virtual Workload UpdateWorkload(UpdateWorkloadRequest request, CallSettings callSettings = null)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    UpdateWorkloadRequest request = new UpdateWorkloadRequest
    {
        Workload = new Workload(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Workload response = assuredWorkloadsServiceClient.UpdateWorkload(request);
    

### UpdateWorkload(Workload, FieldMask, CallSettings)
    
    
    public virtual Workload UpdateWorkload(Workload workload, FieldMask updateMask, CallSettings callSettings = null)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

**Parameters**  
---  
**Name** | **Description**  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
Required. The workload to update. The workload's `name` field is used to identify the workload to be updated. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = AssuredWorkloadsServiceClient.Create();
    // Initialize request argument(s)
    Workload workload = new Workload();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Workload response = assuredWorkloadsServiceClient.UpdateWorkload(workload, updateMask);
    

### UpdateWorkloadAsync(UpdateWorkloadRequest, CallSettings)
    
    
    public virtual Task<Workload> UpdateWorkloadAsync(UpdateWorkloadRequest request, CallSettings callSettings = null)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateWorkloadRequest request = new UpdateWorkloadRequest
    {
        Workload = new Workload(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.UpdateWorkloadAsync(request);
    

### UpdateWorkloadAsync(UpdateWorkloadRequest, CancellationToken)
    
    
    public virtual Task<Workload> UpdateWorkloadAsync(UpdateWorkloadRequest request, CancellationToken cancellationToken)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateWorkloadRequest request = new UpdateWorkloadRequest
    {
        Workload = new Workload(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.UpdateWorkloadAsync(request);
    

### UpdateWorkloadAsync(Workload, FieldMask, CallSettings)
    
    
    public virtual Task<Workload> UpdateWorkloadAsync(Workload workload, FieldMask updateMask, CallSettings callSettings = null)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

**Parameters**  
---  
**Name** | **Description**  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
Required. The workload to update. The workload's `name` field is used to identify the workload to be updated. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    Workload workload = new Workload();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.UpdateWorkloadAsync(workload, updateMask);
    

### UpdateWorkloadAsync(Workload, FieldMask, CancellationToken)
    
    
    public virtual Task<Workload> UpdateWorkloadAsync(Workload workload, FieldMask updateMask, CancellationToken cancellationToken)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

**Parameters**  
---  
**Name** | **Description**  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
Required. The workload to update. The workload's `name` field is used to identify the workload to be updated. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The list of fields to be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssuredWorkloadsServiceClient assuredWorkloadsServiceClient = await AssuredWorkloadsServiceClient.CreateAsync();
    // Initialize request argument(s)
    Workload workload = new Workload();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Workload response = await assuredWorkloadsServiceClient.UpdateWorkloadAsync(workload, updateMask);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
