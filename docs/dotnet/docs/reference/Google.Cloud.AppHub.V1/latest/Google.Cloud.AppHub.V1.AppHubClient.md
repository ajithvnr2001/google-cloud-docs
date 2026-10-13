---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient
title: App Hub v1 API - Class AppHubClient (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:28.649525+00:00
---

# App Hub v1 API - Class AppHubClient (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Hub v1 API - Class AppHubClient (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class AppHubClient

Reference documentation and code samples for the App Hub v1 API class AppHubClient.

AppHub client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AppHubClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AppHubClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClientImpl)

## Namespace

[Google.Cloud.AppHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1)

## Assembly

Google.Cloud.AppHub.V1.dll

## Remarks

The App Hub API allows you to manage App Hub resources.

## Properties 

### CreateApplicationOperationsClient
    
    
    public virtual OperationsClient CreateApplicationOperationsClient { get; }

The long-running operations client for `CreateApplication`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateServiceOperationsClient
    
    
    public virtual OperationsClient CreateServiceOperationsClient { get; }

The long-running operations client for `CreateService`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateServiceProjectAttachmentOperationsClient
    
    
    public virtual OperationsClient CreateServiceProjectAttachmentOperationsClient { get; }

The long-running operations client for `CreateServiceProjectAttachment`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateWorkloadOperationsClient
    
    
    public virtual OperationsClient CreateWorkloadOperationsClient { get; }

The long-running operations client for `CreateWorkload`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AppHub service, which is a host of "apphub.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AppHub scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AppHub scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteApplicationOperationsClient
    
    
    public virtual OperationsClient DeleteApplicationOperationsClient { get; }

The long-running operations client for `DeleteApplication`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteServiceOperationsClient
    
    
    public virtual OperationsClient DeleteServiceOperationsClient { get; }

The long-running operations client for `DeleteService`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteServiceProjectAttachmentOperationsClient
    
    
    public virtual OperationsClient DeleteServiceProjectAttachmentOperationsClient { get; }

The long-running operations client for `DeleteServiceProjectAttachment`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteWorkloadOperationsClient
    
    
    public virtual OperationsClient DeleteWorkloadOperationsClient { get; }

The long-running operations client for `DeleteWorkload`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual AppHub.AppHubClient GrpcClient { get; }

The underlying gRPC AppHub client

**Property Value**  
---  
**Type** | **Description**  
`[AppHub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHub)[AppHubClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHub.AppHubClient)` |   
  
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
  
### UpdateApplicationOperationsClient
    
    
    public virtual OperationsClient UpdateApplicationOperationsClient { get; }

The long-running operations client for `UpdateApplication`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateBoundaryOperationsClient
    
    
    public virtual OperationsClient UpdateBoundaryOperationsClient { get; }

The long-running operations client for `UpdateBoundary`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateServiceOperationsClient
    
    
    public virtual OperationsClient UpdateServiceOperationsClient { get; }

The long-running operations client for `UpdateService`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateWorkloadOperationsClient
    
    
    public virtual OperationsClient UpdateWorkloadOperationsClient { get; }

The long-running operations client for `UpdateWorkload`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static AppHubClient Create()

Synchronously creates a [AppHubClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AppHubClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AppHubClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient)` | The created [AppHubClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient).  
  
### CreateApplication(LocationName, Application, string, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> CreateApplication(LocationName parent, Application application, string applicationId, CallSettings callSettings = null)

Creates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to create Application in. Expected format: `projects/{project}/locations/{location}`.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)`  
Required. The resource being created  
`applicationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Application identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Application application = new Application();
    string applicationId = "";
    // Make the request
    Operation<Application, OperationMetadata> response = appHubClient.CreateApplication(parent, application, applicationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplication(CreateApplicationRequest, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> CreateApplication(CreateApplicationRequest request, CallSettings callSettings = null)

Creates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    CreateApplicationRequest request = new CreateApplicationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ApplicationId = "",
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = appHubClient.CreateApplication(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplication(string, Application, string, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> CreateApplication(string parent, Application application, string applicationId, CallSettings callSettings = null)

Creates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to create Application in. Expected format: `projects/{project}/locations/{location}`.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)`  
Required. The resource being created  
`applicationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Application identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Application application = new Application();
    string applicationId = "";
    // Make the request
    Operation<Application, OperationMetadata> response = appHubClient.CreateApplication(parent, application, applicationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(LocationName, Application, string, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(LocationName parent, Application application, string applicationId, CallSettings callSettings = null)

Creates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to create Application in. Expected format: `projects/{project}/locations/{location}`.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)`  
Required. The resource being created  
`applicationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Application identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Application application = new Application();
    string applicationId = "";
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.CreateApplicationAsync(parent, application, applicationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(LocationName, Application, string, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(LocationName parent, Application application, string applicationId, CancellationToken cancellationToken)

Creates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to create Application in. Expected format: `projects/{project}/locations/{location}`.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)`  
Required. The resource being created  
`applicationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Application identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Application application = new Application();
    string applicationId = "";
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.CreateApplicationAsync(parent, application, applicationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(CreateApplicationRequest, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(CreateApplicationRequest request, CallSettings callSettings = null)

Creates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    CreateApplicationRequest request = new CreateApplicationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ApplicationId = "",
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.CreateApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(CreateApplicationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(CreateApplicationRequest request, CancellationToken cancellationToken)

Creates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    CreateApplicationRequest request = new CreateApplicationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ApplicationId = "",
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.CreateApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(string, Application, string, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(string parent, Application application, string applicationId, CallSettings callSettings = null)

Creates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to create Application in. Expected format: `projects/{project}/locations/{location}`.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)`  
Required. The resource being created  
`applicationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Application identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Application application = new Application();
    string applicationId = "";
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.CreateApplicationAsync(parent, application, applicationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(string, Application, string, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(string parent, Application application, string applicationId, CancellationToken cancellationToken)

Creates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to create Application in. Expected format: `projects/{project}/locations/{location}`.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)`  
Required. The resource being created  
`applicationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Application identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Application application = new Application();
    string applicationId = "";
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.CreateApplicationAsync(parent, application, applicationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateAsync(CancellationToken)
    
    
    public static Task<AppHubClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AppHubClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AppHubClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppHubClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient)` | The task representing the created [AppHubClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient).  
  
### CreateService(ApplicationName, Service, string, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> CreateService(ApplicationName parent, Service service, string serviceId, CallSettings callSettings = null)

Creates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the parent Application to create the Service in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)`  
Required. The resource being created.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Service identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = appHubClient.CreateService(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateService(CreateServiceRequest, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> CreateService(CreateServiceRequest request, CallSettings callSettings = null)

Creates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    CreateServiceRequest request = new CreateServiceRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ServiceId = "",
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = appHubClient.CreateService(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateService(string, Service, string, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> CreateService(string parent, Service service, string serviceId, CallSettings callSettings = null)

Creates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the parent Application to create the Service in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)`  
Required. The resource being created.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Service identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = appHubClient.CreateService(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(ApplicationName, Service, string, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(ApplicationName parent, Service service, string serviceId, CallSettings callSettings = null)

Creates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the parent Application to create the Service in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)`  
Required. The resource being created.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Service identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.CreateServiceAsync(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(ApplicationName, Service, string, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(ApplicationName parent, Service service, string serviceId, CancellationToken cancellationToken)

Creates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the parent Application to create the Service in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)`  
Required. The resource being created.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Service identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.CreateServiceAsync(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(CreateServiceRequest, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(CreateServiceRequest request, CallSettings callSettings = null)

Creates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    CreateServiceRequest request = new CreateServiceRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ServiceId = "",
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.CreateServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(CreateServiceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(CreateServiceRequest request, CancellationToken cancellationToken)

Creates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    CreateServiceRequest request = new CreateServiceRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ServiceId = "",
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.CreateServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(string, Service, string, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(string parent, Service service, string serviceId, CallSettings callSettings = null)

Creates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the parent Application to create the Service in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)`  
Required. The resource being created.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Service identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.CreateServiceAsync(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(string, Service, string, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(string parent, Service service, string serviceId, CancellationToken cancellationToken)

Creates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the parent Application to create the Service in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)`  
Required. The resource being created.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Service identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.CreateServiceAsync(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceProjectAttachment(LocationName, ServiceProjectAttachment, string, CallSettings)
    
    
    public virtual Operation<ServiceProjectAttachment, OperationMetadata> CreateServiceProjectAttachment(LocationName parent, ServiceProjectAttachment serviceProjectAttachment, string serviceProjectAttachmentId, CallSettings callSettings = null)

Attaches a service project to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to which service project is being attached. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`serviceProjectAttachment` | `[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)`  
Required. The resource being created.  
`serviceProjectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The service project attachment identifier must contain the project id of the service project specified in the service_project_attachment.service_project field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ServiceProjectAttachment serviceProjectAttachment = new ServiceProjectAttachment();
    string serviceProjectAttachmentId = "";
    // Make the request
    Operation<ServiceProjectAttachment, OperationMetadata> response = appHubClient.CreateServiceProjectAttachment(parent, serviceProjectAttachment, serviceProjectAttachmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<ServiceProjectAttachment, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ServiceProjectAttachment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ServiceProjectAttachment, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateServiceProjectAttachment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ServiceProjectAttachment retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceProjectAttachment(CreateServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual Operation<ServiceProjectAttachment, OperationMetadata> CreateServiceProjectAttachment(CreateServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Attaches a service project to the host project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    CreateServiceProjectAttachmentRequest request = new CreateServiceProjectAttachmentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ServiceProjectAttachmentId = "",
        ServiceProjectAttachment = new ServiceProjectAttachment(),
        RequestId = "",
    };
    // Make the request
    Operation<ServiceProjectAttachment, OperationMetadata> response = appHubClient.CreateServiceProjectAttachment(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ServiceProjectAttachment, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ServiceProjectAttachment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ServiceProjectAttachment, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateServiceProjectAttachment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ServiceProjectAttachment retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceProjectAttachment(string, ServiceProjectAttachment, string, CallSettings)
    
    
    public virtual Operation<ServiceProjectAttachment, OperationMetadata> CreateServiceProjectAttachment(string parent, ServiceProjectAttachment serviceProjectAttachment, string serviceProjectAttachmentId, CallSettings callSettings = null)

Attaches a service project to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to which service project is being attached. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`serviceProjectAttachment` | `[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)`  
Required. The resource being created.  
`serviceProjectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The service project attachment identifier must contain the project id of the service project specified in the service_project_attachment.service_project field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ServiceProjectAttachment serviceProjectAttachment = new ServiceProjectAttachment();
    string serviceProjectAttachmentId = "";
    // Make the request
    Operation<ServiceProjectAttachment, OperationMetadata> response = appHubClient.CreateServiceProjectAttachment(parent, serviceProjectAttachment, serviceProjectAttachmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<ServiceProjectAttachment, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ServiceProjectAttachment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ServiceProjectAttachment, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateServiceProjectAttachment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ServiceProjectAttachment retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceProjectAttachmentAsync(LocationName, ServiceProjectAttachment, string, CallSettings)
    
    
    public virtual Task<Operation<ServiceProjectAttachment, OperationMetadata>> CreateServiceProjectAttachmentAsync(LocationName parent, ServiceProjectAttachment serviceProjectAttachment, string serviceProjectAttachmentId, CallSettings callSettings = null)

Attaches a service project to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to which service project is being attached. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`serviceProjectAttachment` | `[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)`  
Required. The resource being created.  
`serviceProjectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The service project attachment identifier must contain the project id of the service project specified in the service_project_attachment.service_project field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ServiceProjectAttachment serviceProjectAttachment = new ServiceProjectAttachment();
    string serviceProjectAttachmentId = "";
    // Make the request
    Operation<ServiceProjectAttachment, OperationMetadata> response = await appHubClient.CreateServiceProjectAttachmentAsync(parent, serviceProjectAttachment, serviceProjectAttachmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<ServiceProjectAttachment, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ServiceProjectAttachment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ServiceProjectAttachment, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ServiceProjectAttachment retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceProjectAttachmentAsync(LocationName, ServiceProjectAttachment, string, CancellationToken)
    
    
    public virtual Task<Operation<ServiceProjectAttachment, OperationMetadata>> CreateServiceProjectAttachmentAsync(LocationName parent, ServiceProjectAttachment serviceProjectAttachment, string serviceProjectAttachmentId, CancellationToken cancellationToken)

Attaches a service project to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to which service project is being attached. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`serviceProjectAttachment` | `[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)`  
Required. The resource being created.  
`serviceProjectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The service project attachment identifier must contain the project id of the service project specified in the service_project_attachment.service_project field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ServiceProjectAttachment serviceProjectAttachment = new ServiceProjectAttachment();
    string serviceProjectAttachmentId = "";
    // Make the request
    Operation<ServiceProjectAttachment, OperationMetadata> response = await appHubClient.CreateServiceProjectAttachmentAsync(parent, serviceProjectAttachment, serviceProjectAttachmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<ServiceProjectAttachment, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ServiceProjectAttachment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ServiceProjectAttachment, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ServiceProjectAttachment retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceProjectAttachmentAsync(CreateServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual Task<Operation<ServiceProjectAttachment, OperationMetadata>> CreateServiceProjectAttachmentAsync(CreateServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Attaches a service project to the host project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    CreateServiceProjectAttachmentRequest request = new CreateServiceProjectAttachmentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ServiceProjectAttachmentId = "",
        ServiceProjectAttachment = new ServiceProjectAttachment(),
        RequestId = "",
    };
    // Make the request
    Operation<ServiceProjectAttachment, OperationMetadata> response = await appHubClient.CreateServiceProjectAttachmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ServiceProjectAttachment, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ServiceProjectAttachment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ServiceProjectAttachment, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ServiceProjectAttachment retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceProjectAttachmentAsync(CreateServiceProjectAttachmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<ServiceProjectAttachment, OperationMetadata>> CreateServiceProjectAttachmentAsync(CreateServiceProjectAttachmentRequest request, CancellationToken cancellationToken)

Attaches a service project to the host project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    CreateServiceProjectAttachmentRequest request = new CreateServiceProjectAttachmentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ServiceProjectAttachmentId = "",
        ServiceProjectAttachment = new ServiceProjectAttachment(),
        RequestId = "",
    };
    // Make the request
    Operation<ServiceProjectAttachment, OperationMetadata> response = await appHubClient.CreateServiceProjectAttachmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ServiceProjectAttachment, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ServiceProjectAttachment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ServiceProjectAttachment, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ServiceProjectAttachment retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceProjectAttachmentAsync(string, ServiceProjectAttachment, string, CallSettings)
    
    
    public virtual Task<Operation<ServiceProjectAttachment, OperationMetadata>> CreateServiceProjectAttachmentAsync(string parent, ServiceProjectAttachment serviceProjectAttachment, string serviceProjectAttachmentId, CallSettings callSettings = null)

Attaches a service project to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to which service project is being attached. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`serviceProjectAttachment` | `[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)`  
Required. The resource being created.  
`serviceProjectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The service project attachment identifier must contain the project id of the service project specified in the service_project_attachment.service_project field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ServiceProjectAttachment serviceProjectAttachment = new ServiceProjectAttachment();
    string serviceProjectAttachmentId = "";
    // Make the request
    Operation<ServiceProjectAttachment, OperationMetadata> response = await appHubClient.CreateServiceProjectAttachmentAsync(parent, serviceProjectAttachment, serviceProjectAttachmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<ServiceProjectAttachment, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ServiceProjectAttachment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ServiceProjectAttachment, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ServiceProjectAttachment retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceProjectAttachmentAsync(string, ServiceProjectAttachment, string, CancellationToken)
    
    
    public virtual Task<Operation<ServiceProjectAttachment, OperationMetadata>> CreateServiceProjectAttachmentAsync(string parent, ServiceProjectAttachment serviceProjectAttachment, string serviceProjectAttachmentId, CancellationToken cancellationToken)

Attaches a service project to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to which service project is being attached. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`serviceProjectAttachment` | `[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)`  
Required. The resource being created.  
`serviceProjectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The service project attachment identifier must contain the project id of the service project specified in the service_project_attachment.service_project field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ServiceProjectAttachment serviceProjectAttachment = new ServiceProjectAttachment();
    string serviceProjectAttachmentId = "";
    // Make the request
    Operation<ServiceProjectAttachment, OperationMetadata> response = await appHubClient.CreateServiceProjectAttachmentAsync(parent, serviceProjectAttachment, serviceProjectAttachmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<ServiceProjectAttachment, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ServiceProjectAttachment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ServiceProjectAttachment, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ServiceProjectAttachment retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkload(ApplicationName, Workload, string, CallSettings)
    
    
    public virtual Operation<Workload, OperationMetadata> CreateWorkload(ApplicationName parent, Workload workload, string workloadId, CallSettings callSettings = null)

Creates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the Application to create Workload in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)`  
Required. The resource being created.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Workload identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    Workload workload = new Workload();
    string workloadId = "";
    // Make the request
    Operation<Workload, OperationMetadata> response = appHubClient.CreateWorkload(parent, workload, workloadId);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkload(CreateWorkloadRequest, CallSettings)
    
    
    public virtual Operation<Workload, OperationMetadata> CreateWorkload(CreateWorkloadRequest request, CallSettings callSettings = null)

Creates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    CreateWorkloadRequest request = new CreateWorkloadRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        WorkloadId = "",
        Workload = new Workload(),
        RequestId = "",
    };
    // Make the request
    Operation<Workload, OperationMetadata> response = appHubClient.CreateWorkload(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkload(string, Workload, string, CallSettings)
    
    
    public virtual Operation<Workload, OperationMetadata> CreateWorkload(string parent, Workload workload, string workloadId, CallSettings callSettings = null)

Creates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Application to create Workload in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)`  
Required. The resource being created.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Workload identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    Workload workload = new Workload();
    string workloadId = "";
    // Make the request
    Operation<Workload, OperationMetadata> response = appHubClient.CreateWorkload(parent, workload, workloadId);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = appHubClient.PollOnceCreateWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(ApplicationName, Workload, string, CallSettings)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> CreateWorkloadAsync(ApplicationName parent, Workload workload, string workloadId, CallSettings callSettings = null)

Creates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the Application to create Workload in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)`  
Required. The resource being created.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Workload identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    Workload workload = new Workload();
    string workloadId = "";
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.CreateWorkloadAsync(parent, workload, workloadId);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(ApplicationName, Workload, string, CancellationToken)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> CreateWorkloadAsync(ApplicationName parent, Workload workload, string workloadId, CancellationToken cancellationToken)

Creates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the Application to create Workload in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)`  
Required. The resource being created.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Workload identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    Workload workload = new Workload();
    string workloadId = "";
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.CreateWorkloadAsync(parent, workload, workloadId);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(CreateWorkloadRequest, CallSettings)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> CreateWorkloadAsync(CreateWorkloadRequest request, CallSettings callSettings = null)

Creates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    CreateWorkloadRequest request = new CreateWorkloadRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        WorkloadId = "",
        Workload = new Workload(),
        RequestId = "",
    };
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.CreateWorkloadAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(CreateWorkloadRequest, CancellationToken)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> CreateWorkloadAsync(CreateWorkloadRequest request, CancellationToken cancellationToken)

Creates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.CreateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    CreateWorkloadRequest request = new CreateWorkloadRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        WorkloadId = "",
        Workload = new Workload(),
        RequestId = "",
    };
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.CreateWorkloadAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(string, Workload, string, CallSettings)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> CreateWorkloadAsync(string parent, Workload workload, string workloadId, CallSettings callSettings = null)

Creates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Application to create Workload in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)`  
Required. The resource being created.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Workload identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    Workload workload = new Workload();
    string workloadId = "";
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.CreateWorkloadAsync(parent, workload, workloadId);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### CreateWorkloadAsync(string, Workload, string, CancellationToken)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> CreateWorkloadAsync(string parent, Workload workload, string workloadId, CancellationToken cancellationToken)

Creates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Application to create Workload in. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)`  
Required. The resource being created.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Workload identifier. Must contain only lowercase letters, numbers or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    Workload workload = new Workload();
    string workloadId = "";
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.CreateWorkloadAsync(parent, workload, workloadId);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceCreateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplication(ApplicationName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApplication(ApplicationName name, CallSettings callSettings = null)

Deletes an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the Application to delete. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteApplication(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplication(DeleteApplicationRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApplication(DeleteApplicationRequest request, CallSettings callSettings = null)

Deletes an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    DeleteApplicationRequest request = new DeleteApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteApplication(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplication(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApplication(string name, CallSettings callSettings = null)

Deletes an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Application to delete. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteApplication(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(ApplicationName name, CallSettings callSettings = null)

Deletes an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the Application to delete. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(ApplicationName name, CancellationToken cancellationToken)

Deletes an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the Application to delete. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(DeleteApplicationRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(DeleteApplicationRequest request, CallSettings callSettings = null)

Deletes an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DeleteApplicationRequest request = new DeleteApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(DeleteApplicationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(DeleteApplicationRequest request, CancellationToken cancellationToken)

Deletes an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DeleteApplicationRequest request = new DeleteApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(string name, CallSettings callSettings = null)

Deletes an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Application to delete. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(string name, CancellationToken cancellationToken)

Deletes an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Application to delete. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteService(DeleteServiceRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteService(DeleteServiceRequest request, CallSettings callSettings = null)

Deletes a Service from an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    DeleteServiceRequest request = new DeleteServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteService(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteService(ServiceName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteService(ServiceName name, CallSettings callSettings = null)

Deletes a Service from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceName)`  
Required. Fully qualified name of the Service to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteService(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteService(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteService(string name, CallSettings callSettings = null)

Deletes a Service from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Service to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/services/[SERVICE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteService(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(DeleteServiceRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(DeleteServiceRequest request, CallSettings callSettings = null)

Deletes a Service from an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DeleteServiceRequest request = new DeleteServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(DeleteServiceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(DeleteServiceRequest request, CancellationToken cancellationToken)

Deletes a Service from an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DeleteServiceRequest request = new DeleteServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(ServiceName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(ServiceName name, CallSettings callSettings = null)

Deletes a Service from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceName)`  
Required. Fully qualified name of the Service to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(ServiceName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(ServiceName name, CancellationToken cancellationToken)

Deletes a Service from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceName)`  
Required. Fully qualified name of the Service to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(string name, CallSettings callSettings = null)

Deletes a Service from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Service to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/services/[SERVICE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(string name, CancellationToken cancellationToken)

Deletes a Service from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Service to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/services/[SERVICE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceProjectAttachment(DeleteServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteServiceProjectAttachment(DeleteServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Deletes a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    DeleteServiceProjectAttachmentRequest request = new DeleteServiceProjectAttachmentRequest
    {
        ServiceProjectAttachmentName = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteServiceProjectAttachment(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteServiceProjectAttachment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceProjectAttachment(ServiceProjectAttachmentName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteServiceProjectAttachment(ServiceProjectAttachmentName name, CallSettings callSettings = null)

Deletes a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceProjectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachmentName)`  
Required. Fully qualified name of the service project attachment to delete. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ServiceProjectAttachmentName name = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteServiceProjectAttachment(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteServiceProjectAttachment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceProjectAttachment(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteServiceProjectAttachment(string name, CallSettings callSettings = null)

Deletes a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the service project attachment to delete. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/serviceProjectAttachments/[SERVICE_PROJECT_ATTACHMENT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteServiceProjectAttachment(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteServiceProjectAttachment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceProjectAttachmentAsync(DeleteServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceProjectAttachmentAsync(DeleteServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Deletes a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DeleteServiceProjectAttachmentRequest request = new DeleteServiceProjectAttachmentRequest
    {
        ServiceProjectAttachmentName = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceProjectAttachmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceProjectAttachmentAsync(DeleteServiceProjectAttachmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceProjectAttachmentAsync(DeleteServiceProjectAttachmentRequest request, CancellationToken cancellationToken)

Deletes a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DeleteServiceProjectAttachmentRequest request = new DeleteServiceProjectAttachmentRequest
    {
        ServiceProjectAttachmentName = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceProjectAttachmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceProjectAttachmentAsync(ServiceProjectAttachmentName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceProjectAttachmentAsync(ServiceProjectAttachmentName name, CallSettings callSettings = null)

Deletes a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceProjectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachmentName)`  
Required. Fully qualified name of the service project attachment to delete. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ServiceProjectAttachmentName name = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceProjectAttachmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceProjectAttachmentAsync(ServiceProjectAttachmentName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceProjectAttachmentAsync(ServiceProjectAttachmentName name, CancellationToken cancellationToken)

Deletes a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceProjectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachmentName)`  
Required. Fully qualified name of the service project attachment to delete. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ServiceProjectAttachmentName name = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceProjectAttachmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceProjectAttachmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceProjectAttachmentAsync(string name, CallSettings callSettings = null)

Deletes a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the service project attachment to delete. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/serviceProjectAttachments/[SERVICE_PROJECT_ATTACHMENT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceProjectAttachmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceProjectAttachmentAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceProjectAttachmentAsync(string name, CancellationToken cancellationToken)

Deletes a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the service project attachment to delete. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/serviceProjectAttachments/[SERVICE_PROJECT_ATTACHMENT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteServiceProjectAttachmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteServiceProjectAttachmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkload(DeleteWorkloadRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteWorkload(DeleteWorkloadRequest request, CallSettings callSettings = null)

Deletes a Workload from an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    DeleteWorkloadRequest request = new DeleteWorkloadRequest
    {
        WorkloadName = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteWorkload(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkload(WorkloadName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteWorkload(WorkloadName name, CallSettings callSettings = null)

Deletes a Workload from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.WorkloadName)`  
Required. Fully qualified name of the Workload to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]");
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteWorkload(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkload(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteWorkload(string name, CallSettings callSettings = null)

Deletes a Workload from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Workload to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/workloads/[WORKLOAD]";
    // Make the request
    Operation<Empty, OperationMetadata> response = appHubClient.DeleteWorkload(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appHubClient.PollOnceDeleteWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkloadAsync(DeleteWorkloadRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteWorkloadAsync(DeleteWorkloadRequest request, CallSettings callSettings = null)

Deletes a Workload from an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DeleteWorkloadRequest request = new DeleteWorkloadRequest
    {
        WorkloadName = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteWorkloadAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkloadAsync(DeleteWorkloadRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteWorkloadAsync(DeleteWorkloadRequest request, CancellationToken cancellationToken)

Deletes a Workload from an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DeleteWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DeleteWorkloadRequest request = new DeleteWorkloadRequest
    {
        WorkloadName = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteWorkloadAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkloadAsync(WorkloadName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteWorkloadAsync(WorkloadName name, CallSettings callSettings = null)

Deletes a Workload from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.WorkloadName)`  
Required. Fully qualified name of the Workload to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteWorkloadAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkloadAsync(WorkloadName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteWorkloadAsync(WorkloadName name, CancellationToken cancellationToken)

Deletes a Workload from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.WorkloadName)`  
Required. Fully qualified name of the Workload to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteWorkloadAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkloadAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteWorkloadAsync(string name, CallSettings callSettings = null)

Deletes a Workload from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Workload to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/workloads/[WORKLOAD]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteWorkloadAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteWorkloadAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteWorkloadAsync(string name, CancellationToken cancellationToken)

Deletes a Workload from an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Workload to delete from an Application. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/workloads/[WORKLOAD]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appHubClient.DeleteWorkloadAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appHubClient.PollOnceDeleteWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DetachServiceProjectAttachment(LocationName, CallSettings)
    
    
    public virtual DetachServiceProjectAttachmentResponse DetachServiceProjectAttachment(LocationName name, CallSettings callSettings = null)

Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Service project id and location to detach from a host project. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DetachServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName name = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    DetachServiceProjectAttachmentResponse response = appHubClient.DetachServiceProjectAttachment(name);
    

### DetachServiceProjectAttachment(DetachServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual DetachServiceProjectAttachmentResponse DetachServiceProjectAttachment(DetachServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DetachServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DetachServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    DetachServiceProjectAttachmentRequest request = new DetachServiceProjectAttachmentRequest
    {
        LocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    DetachServiceProjectAttachmentResponse response = appHubClient.DetachServiceProjectAttachment(request);
    

### DetachServiceProjectAttachment(string, CallSettings)
    
    
    public virtual DetachServiceProjectAttachmentResponse DetachServiceProjectAttachment(string name, CallSettings callSettings = null)

Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Service project id and location to detach from a host project. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DetachServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    DetachServiceProjectAttachmentResponse response = appHubClient.DetachServiceProjectAttachment(name);
    

### DetachServiceProjectAttachmentAsync(LocationName, CallSettings)
    
    
    public virtual Task<DetachServiceProjectAttachmentResponse> DetachServiceProjectAttachmentAsync(LocationName name, CallSettings callSettings = null)

Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Service project id and location to detach from a host project. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DetachServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName name = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    DetachServiceProjectAttachmentResponse response = await appHubClient.DetachServiceProjectAttachmentAsync(name);
    

### DetachServiceProjectAttachmentAsync(LocationName, CancellationToken)
    
    
    public virtual Task<DetachServiceProjectAttachmentResponse> DetachServiceProjectAttachmentAsync(LocationName name, CancellationToken cancellationToken)

Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Service project id and location to detach from a host project. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DetachServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName name = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    DetachServiceProjectAttachmentResponse response = await appHubClient.DetachServiceProjectAttachmentAsync(name);
    

### DetachServiceProjectAttachmentAsync(DetachServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual Task<DetachServiceProjectAttachmentResponse> DetachServiceProjectAttachmentAsync(DetachServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DetachServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DetachServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DetachServiceProjectAttachmentRequest request = new DetachServiceProjectAttachmentRequest
    {
        LocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    DetachServiceProjectAttachmentResponse response = await appHubClient.DetachServiceProjectAttachmentAsync(request);
    

### DetachServiceProjectAttachmentAsync(DetachServiceProjectAttachmentRequest, CancellationToken)
    
    
    public virtual Task<DetachServiceProjectAttachmentResponse> DetachServiceProjectAttachmentAsync(DetachServiceProjectAttachmentRequest request, CancellationToken cancellationToken)

Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DetachServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DetachServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DetachServiceProjectAttachmentRequest request = new DetachServiceProjectAttachmentRequest
    {
        LocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    DetachServiceProjectAttachmentResponse response = await appHubClient.DetachServiceProjectAttachmentAsync(request);
    

### DetachServiceProjectAttachmentAsync(string, CallSettings)
    
    
    public virtual Task<DetachServiceProjectAttachmentResponse> DetachServiceProjectAttachmentAsync(string name, CallSettings callSettings = null)

Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Service project id and location to detach from a host project. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DetachServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    DetachServiceProjectAttachmentResponse response = await appHubClient.DetachServiceProjectAttachmentAsync(name);
    

### DetachServiceProjectAttachmentAsync(string, CancellationToken)
    
    
    public virtual Task<DetachServiceProjectAttachmentResponse> DetachServiceProjectAttachmentAsync(string name, CancellationToken cancellationToken)

Detaches a service project from a host project. You can call this API from any service project without needing access to the host project that it is attached to.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Service project id and location to detach from a host project. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DetachServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DetachServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    DetachServiceProjectAttachmentResponse response = await appHubClient.DetachServiceProjectAttachmentAsync(name);
    

### GetApplication(ApplicationName, CallSettings)
    
    
    public virtual Application GetApplication(ApplicationName name, CallSettings callSettings = null)

Gets an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the Application to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Application response = appHubClient.GetApplication(name);
    

### GetApplication(GetApplicationRequest, CallSettings)
    
    
    public virtual Application GetApplication(GetApplicationRequest request, CallSettings callSettings = null)

Gets an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    GetApplicationRequest request = new GetApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
    };
    // Make the request
    Application response = appHubClient.GetApplication(request);
    

### GetApplication(string, CallSettings)
    
    
    public virtual Application GetApplication(string name, CallSettings callSettings = null)

Gets an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Application to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Application response = appHubClient.GetApplication(name);
    

### GetApplicationAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Application> GetApplicationAsync(ApplicationName name, CallSettings callSettings = null)

Gets an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the Application to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Application response = await appHubClient.GetApplicationAsync(name);
    

### GetApplicationAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Application> GetApplicationAsync(ApplicationName name, CancellationToken cancellationToken)

Gets an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the Application to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Application response = await appHubClient.GetApplicationAsync(name);
    

### GetApplicationAsync(GetApplicationRequest, CallSettings)
    
    
    public virtual Task<Application> GetApplicationAsync(GetApplicationRequest request, CallSettings callSettings = null)

Gets an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetApplicationRequest request = new GetApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
    };
    // Make the request
    Application response = await appHubClient.GetApplicationAsync(request);
    

### GetApplicationAsync(GetApplicationRequest, CancellationToken)
    
    
    public virtual Task<Application> GetApplicationAsync(GetApplicationRequest request, CancellationToken cancellationToken)

Gets an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetApplicationRequest request = new GetApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
    };
    // Make the request
    Application response = await appHubClient.GetApplicationAsync(request);
    

### GetApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Application> GetApplicationAsync(string name, CallSettings callSettings = null)

Gets an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Application to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Application response = await appHubClient.GetApplicationAsync(name);
    

### GetApplicationAsync(string, CancellationToken)
    
    
    public virtual Task<Application> GetApplicationAsync(string name, CancellationToken cancellationToken)

Gets an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Application to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Application response = await appHubClient.GetApplicationAsync(name);
    

### GetBoundary(BoundaryName, CallSettings)
    
    
    public virtual Boundary GetBoundary(BoundaryName name, CallSettings callSettings = null)

Gets a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BoundaryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.BoundaryName)`  
Required. The name of the boundary to retrieve. Format: `projects/{project}/locations/{location}/boundary`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    BoundaryName name = BoundaryName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Boundary response = appHubClient.GetBoundary(name);
    

### GetBoundary(GetBoundaryRequest, CallSettings)
    
    
    public virtual Boundary GetBoundary(GetBoundaryRequest request, CallSettings callSettings = null)

Gets a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBoundaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetBoundaryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    GetBoundaryRequest request = new GetBoundaryRequest
    {
        BoundaryName = BoundaryName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    Boundary response = appHubClient.GetBoundary(request);
    

### GetBoundary(string, CallSettings)
    
    
    public virtual Boundary GetBoundary(string name, CallSettings callSettings = null)

Gets a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the boundary to retrieve. Format: `projects/{project}/locations/{location}/boundary`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/boundary";
    // Make the request
    Boundary response = appHubClient.GetBoundary(name);
    

### GetBoundaryAsync(BoundaryName, CallSettings)
    
    
    public virtual Task<Boundary> GetBoundaryAsync(BoundaryName name, CallSettings callSettings = null)

Gets a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BoundaryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.BoundaryName)`  
Required. The name of the boundary to retrieve. Format: `projects/{project}/locations/{location}/boundary`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    BoundaryName name = BoundaryName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Boundary response = await appHubClient.GetBoundaryAsync(name);
    

### GetBoundaryAsync(BoundaryName, CancellationToken)
    
    
    public virtual Task<Boundary> GetBoundaryAsync(BoundaryName name, CancellationToken cancellationToken)

Gets a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BoundaryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.BoundaryName)`  
Required. The name of the boundary to retrieve. Format: `projects/{project}/locations/{location}/boundary`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    BoundaryName name = BoundaryName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Boundary response = await appHubClient.GetBoundaryAsync(name);
    

### GetBoundaryAsync(GetBoundaryRequest, CallSettings)
    
    
    public virtual Task<Boundary> GetBoundaryAsync(GetBoundaryRequest request, CallSettings callSettings = null)

Gets a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBoundaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetBoundaryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetBoundaryRequest request = new GetBoundaryRequest
    {
        BoundaryName = BoundaryName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    Boundary response = await appHubClient.GetBoundaryAsync(request);
    

### GetBoundaryAsync(GetBoundaryRequest, CancellationToken)
    
    
    public virtual Task<Boundary> GetBoundaryAsync(GetBoundaryRequest request, CancellationToken cancellationToken)

Gets a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBoundaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetBoundaryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetBoundaryRequest request = new GetBoundaryRequest
    {
        BoundaryName = BoundaryName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    Boundary response = await appHubClient.GetBoundaryAsync(request);
    

### GetBoundaryAsync(string, CallSettings)
    
    
    public virtual Task<Boundary> GetBoundaryAsync(string name, CallSettings callSettings = null)

Gets a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the boundary to retrieve. Format: `projects/{project}/locations/{location}/boundary`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/boundary";
    // Make the request
    Boundary response = await appHubClient.GetBoundaryAsync(name);
    

### GetBoundaryAsync(string, CancellationToken)
    
    
    public virtual Task<Boundary> GetBoundaryAsync(string name, CancellationToken cancellationToken)

Gets a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the boundary to retrieve. Format: `projects/{project}/locations/{location}/boundary`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/boundary";
    // Make the request
    Boundary response = await appHubClient.GetBoundaryAsync(name);
    

### GetDiscoveredService(DiscoveredServiceName, CallSettings)
    
    
    public virtual DiscoveredService GetDiscoveredService(DiscoveredServiceName name, CallSettings callSettings = null)

Gets a Discovered Service in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DiscoveredServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredServiceName)`  
Required. Fully qualified name of the Discovered Service to fetch. Expected format: `projects/{project}/locations/{location}/discoveredServices/{discoveredService}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    DiscoveredServiceName name = DiscoveredServiceName.FromProjectLocationDiscoveredService("[PROJECT]", "[LOCATION]", "[DISCOVERED_SERVICE]");
    // Make the request
    DiscoveredService response = appHubClient.GetDiscoveredService(name);
    

### GetDiscoveredService(GetDiscoveredServiceRequest, CallSettings)
    
    
    public virtual DiscoveredService GetDiscoveredService(GetDiscoveredServiceRequest request, CallSettings callSettings = null)

Gets a Discovered Service in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDiscoveredServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetDiscoveredServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    GetDiscoveredServiceRequest request = new GetDiscoveredServiceRequest
    {
        DiscoveredServiceName = DiscoveredServiceName.FromProjectLocationDiscoveredService("[PROJECT]", "[LOCATION]", "[DISCOVERED_SERVICE]"),
    };
    // Make the request
    DiscoveredService response = appHubClient.GetDiscoveredService(request);
    

### GetDiscoveredService(string, CallSettings)
    
    
    public virtual DiscoveredService GetDiscoveredService(string name, CallSettings callSettings = null)

Gets a Discovered Service in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Discovered Service to fetch. Expected format: `projects/{project}/locations/{location}/discoveredServices/{discoveredService}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/discoveredServices/[DISCOVERED_SERVICE]";
    // Make the request
    DiscoveredService response = appHubClient.GetDiscoveredService(name);
    

### GetDiscoveredServiceAsync(DiscoveredServiceName, CallSettings)
    
    
    public virtual Task<DiscoveredService> GetDiscoveredServiceAsync(DiscoveredServiceName name, CallSettings callSettings = null)

Gets a Discovered Service in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DiscoveredServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredServiceName)`  
Required. Fully qualified name of the Discovered Service to fetch. Expected format: `projects/{project}/locations/{location}/discoveredServices/{discoveredService}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DiscoveredServiceName name = DiscoveredServiceName.FromProjectLocationDiscoveredService("[PROJECT]", "[LOCATION]", "[DISCOVERED_SERVICE]");
    // Make the request
    DiscoveredService response = await appHubClient.GetDiscoveredServiceAsync(name);
    

### GetDiscoveredServiceAsync(DiscoveredServiceName, CancellationToken)
    
    
    public virtual Task<DiscoveredService> GetDiscoveredServiceAsync(DiscoveredServiceName name, CancellationToken cancellationToken)

Gets a Discovered Service in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DiscoveredServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredServiceName)`  
Required. Fully qualified name of the Discovered Service to fetch. Expected format: `projects/{project}/locations/{location}/discoveredServices/{discoveredService}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DiscoveredServiceName name = DiscoveredServiceName.FromProjectLocationDiscoveredService("[PROJECT]", "[LOCATION]", "[DISCOVERED_SERVICE]");
    // Make the request
    DiscoveredService response = await appHubClient.GetDiscoveredServiceAsync(name);
    

### GetDiscoveredServiceAsync(GetDiscoveredServiceRequest, CallSettings)
    
    
    public virtual Task<DiscoveredService> GetDiscoveredServiceAsync(GetDiscoveredServiceRequest request, CallSettings callSettings = null)

Gets a Discovered Service in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDiscoveredServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetDiscoveredServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetDiscoveredServiceRequest request = new GetDiscoveredServiceRequest
    {
        DiscoveredServiceName = DiscoveredServiceName.FromProjectLocationDiscoveredService("[PROJECT]", "[LOCATION]", "[DISCOVERED_SERVICE]"),
    };
    // Make the request
    DiscoveredService response = await appHubClient.GetDiscoveredServiceAsync(request);
    

### GetDiscoveredServiceAsync(GetDiscoveredServiceRequest, CancellationToken)
    
    
    public virtual Task<DiscoveredService> GetDiscoveredServiceAsync(GetDiscoveredServiceRequest request, CancellationToken cancellationToken)

Gets a Discovered Service in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDiscoveredServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetDiscoveredServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetDiscoveredServiceRequest request = new GetDiscoveredServiceRequest
    {
        DiscoveredServiceName = DiscoveredServiceName.FromProjectLocationDiscoveredService("[PROJECT]", "[LOCATION]", "[DISCOVERED_SERVICE]"),
    };
    // Make the request
    DiscoveredService response = await appHubClient.GetDiscoveredServiceAsync(request);
    

### GetDiscoveredServiceAsync(string, CallSettings)
    
    
    public virtual Task<DiscoveredService> GetDiscoveredServiceAsync(string name, CallSettings callSettings = null)

Gets a Discovered Service in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Discovered Service to fetch. Expected format: `projects/{project}/locations/{location}/discoveredServices/{discoveredService}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/discoveredServices/[DISCOVERED_SERVICE]";
    // Make the request
    DiscoveredService response = await appHubClient.GetDiscoveredServiceAsync(name);
    

### GetDiscoveredServiceAsync(string, CancellationToken)
    
    
    public virtual Task<DiscoveredService> GetDiscoveredServiceAsync(string name, CancellationToken cancellationToken)

Gets a Discovered Service in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Discovered Service to fetch. Expected format: `projects/{project}/locations/{location}/discoveredServices/{discoveredService}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/discoveredServices/[DISCOVERED_SERVICE]";
    // Make the request
    DiscoveredService response = await appHubClient.GetDiscoveredServiceAsync(name);
    

### GetDiscoveredWorkload(DiscoveredWorkloadName, CallSettings)
    
    
    public virtual DiscoveredWorkload GetDiscoveredWorkload(DiscoveredWorkloadName name, CallSettings callSettings = null)

Gets a Discovered Workload in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DiscoveredWorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkloadName)`  
Required. Fully qualified name of the Discovered Workload to fetch. Expected format: `projects/{project}/locations/{location}/discoveredWorkloads/{discoveredWorkload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    DiscoveredWorkloadName name = DiscoveredWorkloadName.FromProjectLocationDiscoveredWorkload("[PROJECT]", "[LOCATION]", "[DISCOVERED_WORKLOAD]");
    // Make the request
    DiscoveredWorkload response = appHubClient.GetDiscoveredWorkload(name);
    

### GetDiscoveredWorkload(GetDiscoveredWorkloadRequest, CallSettings)
    
    
    public virtual DiscoveredWorkload GetDiscoveredWorkload(GetDiscoveredWorkloadRequest request, CallSettings callSettings = null)

Gets a Discovered Workload in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDiscoveredWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetDiscoveredWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    GetDiscoveredWorkloadRequest request = new GetDiscoveredWorkloadRequest
    {
        DiscoveredWorkloadName = DiscoveredWorkloadName.FromProjectLocationDiscoveredWorkload("[PROJECT]", "[LOCATION]", "[DISCOVERED_WORKLOAD]"),
    };
    // Make the request
    DiscoveredWorkload response = appHubClient.GetDiscoveredWorkload(request);
    

### GetDiscoveredWorkload(string, CallSettings)
    
    
    public virtual DiscoveredWorkload GetDiscoveredWorkload(string name, CallSettings callSettings = null)

Gets a Discovered Workload in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Discovered Workload to fetch. Expected format: `projects/{project}/locations/{location}/discoveredWorkloads/{discoveredWorkload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/discoveredWorkloads/[DISCOVERED_WORKLOAD]";
    // Make the request
    DiscoveredWorkload response = appHubClient.GetDiscoveredWorkload(name);
    

### GetDiscoveredWorkloadAsync(DiscoveredWorkloadName, CallSettings)
    
    
    public virtual Task<DiscoveredWorkload> GetDiscoveredWorkloadAsync(DiscoveredWorkloadName name, CallSettings callSettings = null)

Gets a Discovered Workload in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DiscoveredWorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkloadName)`  
Required. Fully qualified name of the Discovered Workload to fetch. Expected format: `projects/{project}/locations/{location}/discoveredWorkloads/{discoveredWorkload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DiscoveredWorkloadName name = DiscoveredWorkloadName.FromProjectLocationDiscoveredWorkload("[PROJECT]", "[LOCATION]", "[DISCOVERED_WORKLOAD]");
    // Make the request
    DiscoveredWorkload response = await appHubClient.GetDiscoveredWorkloadAsync(name);
    

### GetDiscoveredWorkloadAsync(DiscoveredWorkloadName, CancellationToken)
    
    
    public virtual Task<DiscoveredWorkload> GetDiscoveredWorkloadAsync(DiscoveredWorkloadName name, CancellationToken cancellationToken)

Gets a Discovered Workload in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DiscoveredWorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkloadName)`  
Required. Fully qualified name of the Discovered Workload to fetch. Expected format: `projects/{project}/locations/{location}/discoveredWorkloads/{discoveredWorkload}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    DiscoveredWorkloadName name = DiscoveredWorkloadName.FromProjectLocationDiscoveredWorkload("[PROJECT]", "[LOCATION]", "[DISCOVERED_WORKLOAD]");
    // Make the request
    DiscoveredWorkload response = await appHubClient.GetDiscoveredWorkloadAsync(name);
    

### GetDiscoveredWorkloadAsync(GetDiscoveredWorkloadRequest, CallSettings)
    
    
    public virtual Task<DiscoveredWorkload> GetDiscoveredWorkloadAsync(GetDiscoveredWorkloadRequest request, CallSettings callSettings = null)

Gets a Discovered Workload in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDiscoveredWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetDiscoveredWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetDiscoveredWorkloadRequest request = new GetDiscoveredWorkloadRequest
    {
        DiscoveredWorkloadName = DiscoveredWorkloadName.FromProjectLocationDiscoveredWorkload("[PROJECT]", "[LOCATION]", "[DISCOVERED_WORKLOAD]"),
    };
    // Make the request
    DiscoveredWorkload response = await appHubClient.GetDiscoveredWorkloadAsync(request);
    

### GetDiscoveredWorkloadAsync(GetDiscoveredWorkloadRequest, CancellationToken)
    
    
    public virtual Task<DiscoveredWorkload> GetDiscoveredWorkloadAsync(GetDiscoveredWorkloadRequest request, CancellationToken cancellationToken)

Gets a Discovered Workload in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDiscoveredWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetDiscoveredWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetDiscoveredWorkloadRequest request = new GetDiscoveredWorkloadRequest
    {
        DiscoveredWorkloadName = DiscoveredWorkloadName.FromProjectLocationDiscoveredWorkload("[PROJECT]", "[LOCATION]", "[DISCOVERED_WORKLOAD]"),
    };
    // Make the request
    DiscoveredWorkload response = await appHubClient.GetDiscoveredWorkloadAsync(request);
    

### GetDiscoveredWorkloadAsync(string, CallSettings)
    
    
    public virtual Task<DiscoveredWorkload> GetDiscoveredWorkloadAsync(string name, CallSettings callSettings = null)

Gets a Discovered Workload in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Discovered Workload to fetch. Expected format: `projects/{project}/locations/{location}/discoveredWorkloads/{discoveredWorkload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/discoveredWorkloads/[DISCOVERED_WORKLOAD]";
    // Make the request
    DiscoveredWorkload response = await appHubClient.GetDiscoveredWorkloadAsync(name);
    

### GetDiscoveredWorkloadAsync(string, CancellationToken)
    
    
    public virtual Task<DiscoveredWorkload> GetDiscoveredWorkloadAsync(string name, CancellationToken cancellationToken)

Gets a Discovered Workload in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Discovered Workload to fetch. Expected format: `projects/{project}/locations/{location}/discoveredWorkloads/{discoveredWorkload}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/discoveredWorkloads/[DISCOVERED_WORKLOAD]";
    // Make the request
    DiscoveredWorkload response = await appHubClient.GetDiscoveredWorkloadAsync(name);
    

### GetExtendedMetadataSchema(ExtendedMetadataSchemaName, CallSettings)
    
    
    public virtual ExtendedMetadataSchema GetExtendedMetadataSchema(ExtendedMetadataSchemaName name, CallSettings callSettings = null)

Gets an Extended Metadata Schema.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ExtendedMetadataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchemaName)`  
Required. Schema resource name. Format: `projects/{project}/locations/{location}/extendedMetadataSchemas/{extended_metadata_schema}`. `{extended_metadata_schema}` has the format `"apphub.googleapis.com/{SchemaName}"`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ExtendedMetadataSchemaName name = ExtendedMetadataSchemaName.FromProjectLocationExtendedMetadataSchema("[PROJECT]", "[LOCATION]", "[EXTENDED_METADATA_SCHEMA]");
    // Make the request
    ExtendedMetadataSchema response = appHubClient.GetExtendedMetadataSchema(name);
    

### GetExtendedMetadataSchema(GetExtendedMetadataSchemaRequest, CallSettings)
    
    
    public virtual ExtendedMetadataSchema GetExtendedMetadataSchema(GetExtendedMetadataSchemaRequest request, CallSettings callSettings = null)

Gets an Extended Metadata Schema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExtendedMetadataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetExtendedMetadataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    GetExtendedMetadataSchemaRequest request = new GetExtendedMetadataSchemaRequest
    {
        ExtendedMetadataSchemaName = ExtendedMetadataSchemaName.FromProjectLocationExtendedMetadataSchema("[PROJECT]", "[LOCATION]", "[EXTENDED_METADATA_SCHEMA]"),
    };
    // Make the request
    ExtendedMetadataSchema response = appHubClient.GetExtendedMetadataSchema(request);
    

### GetExtendedMetadataSchema(string, CallSettings)
    
    
    public virtual ExtendedMetadataSchema GetExtendedMetadataSchema(string name, CallSettings callSettings = null)

Gets an Extended Metadata Schema.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Schema resource name. Format: `projects/{project}/locations/{location}/extendedMetadataSchemas/{extended_metadata_schema}`. `{extended_metadata_schema}` has the format `"apphub.googleapis.com/{SchemaName}"`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/extendedMetadataSchemas/[EXTENDED_METADATA_SCHEMA]";
    // Make the request
    ExtendedMetadataSchema response = appHubClient.GetExtendedMetadataSchema(name);
    

### GetExtendedMetadataSchemaAsync(ExtendedMetadataSchemaName, CallSettings)
    
    
    public virtual Task<ExtendedMetadataSchema> GetExtendedMetadataSchemaAsync(ExtendedMetadataSchemaName name, CallSettings callSettings = null)

Gets an Extended Metadata Schema.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ExtendedMetadataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchemaName)`  
Required. Schema resource name. Format: `projects/{project}/locations/{location}/extendedMetadataSchemas/{extended_metadata_schema}`. `{extended_metadata_schema}` has the format `"apphub.googleapis.com/{SchemaName}"`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ExtendedMetadataSchemaName name = ExtendedMetadataSchemaName.FromProjectLocationExtendedMetadataSchema("[PROJECT]", "[LOCATION]", "[EXTENDED_METADATA_SCHEMA]");
    // Make the request
    ExtendedMetadataSchema response = await appHubClient.GetExtendedMetadataSchemaAsync(name);
    

### GetExtendedMetadataSchemaAsync(ExtendedMetadataSchemaName, CancellationToken)
    
    
    public virtual Task<ExtendedMetadataSchema> GetExtendedMetadataSchemaAsync(ExtendedMetadataSchemaName name, CancellationToken cancellationToken)

Gets an Extended Metadata Schema.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ExtendedMetadataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchemaName)`  
Required. Schema resource name. Format: `projects/{project}/locations/{location}/extendedMetadataSchemas/{extended_metadata_schema}`. `{extended_metadata_schema}` has the format `"apphub.googleapis.com/{SchemaName}"`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ExtendedMetadataSchemaName name = ExtendedMetadataSchemaName.FromProjectLocationExtendedMetadataSchema("[PROJECT]", "[LOCATION]", "[EXTENDED_METADATA_SCHEMA]");
    // Make the request
    ExtendedMetadataSchema response = await appHubClient.GetExtendedMetadataSchemaAsync(name);
    

### GetExtendedMetadataSchemaAsync(GetExtendedMetadataSchemaRequest, CallSettings)
    
    
    public virtual Task<ExtendedMetadataSchema> GetExtendedMetadataSchemaAsync(GetExtendedMetadataSchemaRequest request, CallSettings callSettings = null)

Gets an Extended Metadata Schema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExtendedMetadataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetExtendedMetadataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetExtendedMetadataSchemaRequest request = new GetExtendedMetadataSchemaRequest
    {
        ExtendedMetadataSchemaName = ExtendedMetadataSchemaName.FromProjectLocationExtendedMetadataSchema("[PROJECT]", "[LOCATION]", "[EXTENDED_METADATA_SCHEMA]"),
    };
    // Make the request
    ExtendedMetadataSchema response = await appHubClient.GetExtendedMetadataSchemaAsync(request);
    

### GetExtendedMetadataSchemaAsync(GetExtendedMetadataSchemaRequest, CancellationToken)
    
    
    public virtual Task<ExtendedMetadataSchema> GetExtendedMetadataSchemaAsync(GetExtendedMetadataSchemaRequest request, CancellationToken cancellationToken)

Gets an Extended Metadata Schema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExtendedMetadataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetExtendedMetadataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetExtendedMetadataSchemaRequest request = new GetExtendedMetadataSchemaRequest
    {
        ExtendedMetadataSchemaName = ExtendedMetadataSchemaName.FromProjectLocationExtendedMetadataSchema("[PROJECT]", "[LOCATION]", "[EXTENDED_METADATA_SCHEMA]"),
    };
    // Make the request
    ExtendedMetadataSchema response = await appHubClient.GetExtendedMetadataSchemaAsync(request);
    

### GetExtendedMetadataSchemaAsync(string, CallSettings)
    
    
    public virtual Task<ExtendedMetadataSchema> GetExtendedMetadataSchemaAsync(string name, CallSettings callSettings = null)

Gets an Extended Metadata Schema.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Schema resource name. Format: `projects/{project}/locations/{location}/extendedMetadataSchemas/{extended_metadata_schema}`. `{extended_metadata_schema}` has the format `"apphub.googleapis.com/{SchemaName}"`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/extendedMetadataSchemas/[EXTENDED_METADATA_SCHEMA]";
    // Make the request
    ExtendedMetadataSchema response = await appHubClient.GetExtendedMetadataSchemaAsync(name);
    

### GetExtendedMetadataSchemaAsync(string, CancellationToken)
    
    
    public virtual Task<ExtendedMetadataSchema> GetExtendedMetadataSchemaAsync(string name, CancellationToken cancellationToken)

Gets an Extended Metadata Schema.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Schema resource name. Format: `projects/{project}/locations/{location}/extendedMetadataSchemas/{extended_metadata_schema}`. `{extended_metadata_schema}` has the format `"apphub.googleapis.com/{SchemaName}"`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/extendedMetadataSchemas/[EXTENDED_METADATA_SCHEMA]";
    // Make the request
    ExtendedMetadataSchema response = await appHubClient.GetExtendedMetadataSchemaAsync(name);
    

### GetService(GetServiceRequest, CallSettings)
    
    
    public virtual Service GetService(GetServiceRequest request, CallSettings callSettings = null)

Gets a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    GetServiceRequest request = new GetServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]"),
    };
    // Make the request
    Service response = appHubClient.GetService(request);
    

### GetService(ServiceName, CallSettings)
    
    
    public virtual Service GetService(ServiceName name, CallSettings callSettings = null)

Gets a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceName)`  
Required. Fully qualified name of the Service to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]");
    // Make the request
    Service response = appHubClient.GetService(name);
    

### GetService(string, CallSettings)
    
    
    public virtual Service GetService(string name, CallSettings callSettings = null)

Gets a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Service to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/services/[SERVICE]";
    // Make the request
    Service response = appHubClient.GetService(name);
    

### GetServiceAsync(GetServiceRequest, CallSettings)
    
    
    public virtual Task<Service> GetServiceAsync(GetServiceRequest request, CallSettings callSettings = null)

Gets a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetServiceRequest request = new GetServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]"),
    };
    // Make the request
    Service response = await appHubClient.GetServiceAsync(request);
    

### GetServiceAsync(GetServiceRequest, CancellationToken)
    
    
    public virtual Task<Service> GetServiceAsync(GetServiceRequest request, CancellationToken cancellationToken)

Gets a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetServiceRequest request = new GetServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]"),
    };
    // Make the request
    Service response = await appHubClient.GetServiceAsync(request);
    

### GetServiceAsync(ServiceName, CallSettings)
    
    
    public virtual Task<Service> GetServiceAsync(ServiceName name, CallSettings callSettings = null)

Gets a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceName)`  
Required. Fully qualified name of the Service to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]");
    // Make the request
    Service response = await appHubClient.GetServiceAsync(name);
    

### GetServiceAsync(ServiceName, CancellationToken)
    
    
    public virtual Task<Service> GetServiceAsync(ServiceName name, CancellationToken cancellationToken)

Gets a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceName)`  
Required. Fully qualified name of the Service to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationApplicationService("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[SERVICE]");
    // Make the request
    Service response = await appHubClient.GetServiceAsync(name);
    

### GetServiceAsync(string, CallSettings)
    
    
    public virtual Task<Service> GetServiceAsync(string name, CallSettings callSettings = null)

Gets a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Service to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/services/[SERVICE]";
    // Make the request
    Service response = await appHubClient.GetServiceAsync(name);
    

### GetServiceAsync(string, CancellationToken)
    
    
    public virtual Task<Service> GetServiceAsync(string name, CancellationToken cancellationToken)

Gets a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Service to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/services/[SERVICE]";
    // Make the request
    Service response = await appHubClient.GetServiceAsync(name);
    

### GetServiceProjectAttachment(GetServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual ServiceProjectAttachment GetServiceProjectAttachment(GetServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Gets a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    GetServiceProjectAttachmentRequest request = new GetServiceProjectAttachmentRequest
    {
        ServiceProjectAttachmentName = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]"),
    };
    // Make the request
    ServiceProjectAttachment response = appHubClient.GetServiceProjectAttachment(request);
    

### GetServiceProjectAttachment(ServiceProjectAttachmentName, CallSettings)
    
    
    public virtual ServiceProjectAttachment GetServiceProjectAttachment(ServiceProjectAttachmentName name, CallSettings callSettings = null)

Gets a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceProjectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachmentName)`  
Required. Fully qualified name of the service project attachment to retrieve. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ServiceProjectAttachmentName name = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]");
    // Make the request
    ServiceProjectAttachment response = appHubClient.GetServiceProjectAttachment(name);
    

### GetServiceProjectAttachment(string, CallSettings)
    
    
    public virtual ServiceProjectAttachment GetServiceProjectAttachment(string name, CallSettings callSettings = null)

Gets a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the service project attachment to retrieve. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/serviceProjectAttachments/[SERVICE_PROJECT_ATTACHMENT]";
    // Make the request
    ServiceProjectAttachment response = appHubClient.GetServiceProjectAttachment(name);
    

### GetServiceProjectAttachmentAsync(GetServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual Task<ServiceProjectAttachment> GetServiceProjectAttachmentAsync(GetServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Gets a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetServiceProjectAttachmentRequest request = new GetServiceProjectAttachmentRequest
    {
        ServiceProjectAttachmentName = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]"),
    };
    // Make the request
    ServiceProjectAttachment response = await appHubClient.GetServiceProjectAttachmentAsync(request);
    

### GetServiceProjectAttachmentAsync(GetServiceProjectAttachmentRequest, CancellationToken)
    
    
    public virtual Task<ServiceProjectAttachment> GetServiceProjectAttachmentAsync(GetServiceProjectAttachmentRequest request, CancellationToken cancellationToken)

Gets a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetServiceProjectAttachmentRequest request = new GetServiceProjectAttachmentRequest
    {
        ServiceProjectAttachmentName = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]"),
    };
    // Make the request
    ServiceProjectAttachment response = await appHubClient.GetServiceProjectAttachmentAsync(request);
    

### GetServiceProjectAttachmentAsync(ServiceProjectAttachmentName, CallSettings)
    
    
    public virtual Task<ServiceProjectAttachment> GetServiceProjectAttachmentAsync(ServiceProjectAttachmentName name, CallSettings callSettings = null)

Gets a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceProjectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachmentName)`  
Required. Fully qualified name of the service project attachment to retrieve. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ServiceProjectAttachmentName name = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]");
    // Make the request
    ServiceProjectAttachment response = await appHubClient.GetServiceProjectAttachmentAsync(name);
    

### GetServiceProjectAttachmentAsync(ServiceProjectAttachmentName, CancellationToken)
    
    
    public virtual Task<ServiceProjectAttachment> GetServiceProjectAttachmentAsync(ServiceProjectAttachmentName name, CancellationToken cancellationToken)

Gets a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceProjectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachmentName)`  
Required. Fully qualified name of the service project attachment to retrieve. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ServiceProjectAttachmentName name = ServiceProjectAttachmentName.FromProjectLocationServiceProjectAttachment("[PROJECT]", "[LOCATION]", "[SERVICE_PROJECT_ATTACHMENT]");
    // Make the request
    ServiceProjectAttachment response = await appHubClient.GetServiceProjectAttachmentAsync(name);
    

### GetServiceProjectAttachmentAsync(string, CallSettings)
    
    
    public virtual Task<ServiceProjectAttachment> GetServiceProjectAttachmentAsync(string name, CallSettings callSettings = null)

Gets a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the service project attachment to retrieve. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/serviceProjectAttachments/[SERVICE_PROJECT_ATTACHMENT]";
    // Make the request
    ServiceProjectAttachment response = await appHubClient.GetServiceProjectAttachmentAsync(name);
    

### GetServiceProjectAttachmentAsync(string, CancellationToken)
    
    
    public virtual Task<ServiceProjectAttachment> GetServiceProjectAttachmentAsync(string name, CancellationToken cancellationToken)

Gets a service project attachment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the service project attachment to retrieve. Expected format: `projects/{project}/locations/{location}/serviceProjectAttachments/{serviceProjectAttachment}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/serviceProjectAttachments/[SERVICE_PROJECT_ATTACHMENT]";
    // Make the request
    ServiceProjectAttachment response = await appHubClient.GetServiceProjectAttachmentAsync(name);
    

### GetWorkload(GetWorkloadRequest, CallSettings)
    
    
    public virtual Workload GetWorkload(GetWorkloadRequest request, CallSettings callSettings = null)

Gets a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    GetWorkloadRequest request = new GetWorkloadRequest
    {
        WorkloadName = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]"),
    };
    // Make the request
    Workload response = appHubClient.GetWorkload(request);
    

### GetWorkload(WorkloadName, CallSettings)
    
    
    public virtual Workload GetWorkload(WorkloadName name, CallSettings callSettings = null)

Gets a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.WorkloadName)`  
Required. Fully qualified name of the Workload to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]");
    // Make the request
    Workload response = appHubClient.GetWorkload(name);
    

### GetWorkload(string, CallSettings)
    
    
    public virtual Workload GetWorkload(string name, CallSettings callSettings = null)

Gets a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Workload to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/workloads/[WORKLOAD]";
    // Make the request
    Workload response = appHubClient.GetWorkload(name);
    

### GetWorkloadAsync(GetWorkloadRequest, CallSettings)
    
    
    public virtual Task<Workload> GetWorkloadAsync(GetWorkloadRequest request, CallSettings callSettings = null)

Gets a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetWorkloadRequest request = new GetWorkloadRequest
    {
        WorkloadName = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]"),
    };
    // Make the request
    Workload response = await appHubClient.GetWorkloadAsync(request);
    

### GetWorkloadAsync(GetWorkloadRequest, CancellationToken)
    
    
    public virtual Task<Workload> GetWorkloadAsync(GetWorkloadRequest request, CancellationToken cancellationToken)

Gets a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    GetWorkloadRequest request = new GetWorkloadRequest
    {
        WorkloadName = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]"),
    };
    // Make the request
    Workload response = await appHubClient.GetWorkloadAsync(request);
    

### GetWorkloadAsync(WorkloadName, CallSettings)
    
    
    public virtual Task<Workload> GetWorkloadAsync(WorkloadName name, CallSettings callSettings = null)

Gets a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.WorkloadName)`  
Required. Fully qualified name of the Workload to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]");
    // Make the request
    Workload response = await appHubClient.GetWorkloadAsync(name);
    

### GetWorkloadAsync(WorkloadName, CancellationToken)
    
    
    public virtual Task<Workload> GetWorkloadAsync(WorkloadName name, CancellationToken cancellationToken)

Gets a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.WorkloadName)`  
Required. Fully qualified name of the Workload to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromProjectLocationApplicationWorkload("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[WORKLOAD]");
    // Make the request
    Workload response = await appHubClient.GetWorkloadAsync(name);
    

### GetWorkloadAsync(string, CallSettings)
    
    
    public virtual Task<Workload> GetWorkloadAsync(string name, CallSettings callSettings = null)

Gets a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Workload to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/workloads/[WORKLOAD]";
    // Make the request
    Workload response = await appHubClient.GetWorkloadAsync(name);
    

### GetWorkloadAsync(string, CancellationToken)
    
    
    public virtual Task<Workload> GetWorkloadAsync(string name, CancellationToken cancellationToken)

Gets a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the Workload to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/workloads/[WORKLOAD]";
    // Make the request
    Workload response = await appHubClient.GetWorkloadAsync(name);
    

### ListApplications(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListApplicationsResponse, Application> ListApplications(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Applications in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to list Applications on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A pageable sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListApplicationsResponse, Application> response = appHubClient.ListApplications(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplications(ListApplicationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListApplicationsResponse, Application> ListApplications(ListApplicationsRequest request, CallSettings callSettings = null)

Lists Applications in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListApplicationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListApplicationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A pageable sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ListApplicationsRequest request = new ListApplicationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListApplicationsResponse, Application> response = appHubClient.ListApplications(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplications(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListApplicationsResponse, Application> ListApplications(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Applications in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to list Applications on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A pageable sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListApplicationsResponse, Application> response = appHubClient.ListApplications(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplicationsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListApplicationsResponse, Application> ListApplicationsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Applications in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to list Applications on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A pageable asynchronous sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListApplicationsResponse, Application> response = appHubClient.ListApplicationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplicationsAsync(ListApplicationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListApplicationsResponse, Application> ListApplicationsAsync(ListApplicationsRequest request, CallSettings callSettings = null)

Lists Applications in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListApplicationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListApplicationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A pageable asynchronous sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ListApplicationsRequest request = new ListApplicationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListApplicationsResponse, Application> response = appHubClient.ListApplicationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplicationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListApplicationsResponse, Application> ListApplicationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Applications in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to list Applications on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)` | A pageable asynchronous sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListApplicationsResponse, Application> response = appHubClient.ListApplicationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredServices(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDiscoveredServicesResponse, DiscoveredService> ListDiscoveredServices(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Discovered Services that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to list Discovered Services on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDiscoveredServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredServicesResponse)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A pageable sequence of [DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListDiscoveredServicesResponse, DiscoveredService> response = appHubClient.ListDiscoveredServices(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DiscoveredService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDiscoveredServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredService> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredServices(ListDiscoveredServicesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDiscoveredServicesResponse, DiscoveredService> ListDiscoveredServices(ListDiscoveredServicesRequest request, CallSettings callSettings = null)

Lists Discovered Services that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDiscoveredServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredServicesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDiscoveredServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredServicesResponse)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A pageable sequence of [DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ListDiscoveredServicesRequest request = new ListDiscoveredServicesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListDiscoveredServicesResponse, DiscoveredService> response = appHubClient.ListDiscoveredServices(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DiscoveredService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDiscoveredServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredService> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredServices(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDiscoveredServicesResponse, DiscoveredService> ListDiscoveredServices(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Discovered Services that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to list Discovered Services on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDiscoveredServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredServicesResponse)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A pageable sequence of [DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListDiscoveredServicesResponse, DiscoveredService> response = appHubClient.ListDiscoveredServices(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DiscoveredService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDiscoveredServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredService> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredServicesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDiscoveredServicesResponse, DiscoveredService> ListDiscoveredServicesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Discovered Services that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to list Discovered Services on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDiscoveredServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredServicesResponse)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A pageable asynchronous sequence of [DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListDiscoveredServicesResponse, DiscoveredService> response = appHubClient.ListDiscoveredServicesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DiscoveredService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDiscoveredServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredService> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredServicesAsync(ListDiscoveredServicesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDiscoveredServicesResponse, DiscoveredService> ListDiscoveredServicesAsync(ListDiscoveredServicesRequest request, CallSettings callSettings = null)

Lists Discovered Services that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDiscoveredServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredServicesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDiscoveredServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredServicesResponse)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A pageable asynchronous sequence of [DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ListDiscoveredServicesRequest request = new ListDiscoveredServicesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListDiscoveredServicesResponse, DiscoveredService> response = appHubClient.ListDiscoveredServicesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DiscoveredService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDiscoveredServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredService> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredServicesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDiscoveredServicesResponse, DiscoveredService> ListDiscoveredServicesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Discovered Services that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to list Discovered Services on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDiscoveredServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredServicesResponse)[DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService)` | A pageable asynchronous sequence of [DiscoveredService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredService) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListDiscoveredServicesResponse, DiscoveredService> response = appHubClient.ListDiscoveredServicesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DiscoveredService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDiscoveredServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredService> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredWorkloads(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> ListDiscoveredWorkloads(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Discovered Workloads that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to list Discovered Workloads on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDiscoveredWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredWorkloadsResponse)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A pageable sequence of [DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> response = appHubClient.ListDiscoveredWorkloads(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DiscoveredWorkload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDiscoveredWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredWorkload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredWorkloads(ListDiscoveredWorkloadsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> ListDiscoveredWorkloads(ListDiscoveredWorkloadsRequest request, CallSettings callSettings = null)

Lists Discovered Workloads that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDiscoveredWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDiscoveredWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredWorkloadsResponse)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A pageable sequence of [DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ListDiscoveredWorkloadsRequest request = new ListDiscoveredWorkloadsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> response = appHubClient.ListDiscoveredWorkloads(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DiscoveredWorkload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDiscoveredWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredWorkload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredWorkloads(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> ListDiscoveredWorkloads(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Discovered Workloads that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to list Discovered Workloads on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDiscoveredWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredWorkloadsResponse)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A pageable sequence of [DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> response = appHubClient.ListDiscoveredWorkloads(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DiscoveredWorkload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDiscoveredWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredWorkload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredWorkloadsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> ListDiscoveredWorkloadsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Discovered Workloads that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to list Discovered Workloads on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDiscoveredWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredWorkloadsResponse)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A pageable asynchronous sequence of [DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> response = appHubClient.ListDiscoveredWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DiscoveredWorkload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDiscoveredWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredWorkload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredWorkloadsAsync(ListDiscoveredWorkloadsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> ListDiscoveredWorkloadsAsync(ListDiscoveredWorkloadsRequest request, CallSettings callSettings = null)

Lists Discovered Workloads that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDiscoveredWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDiscoveredWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredWorkloadsResponse)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A pageable asynchronous sequence of [DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ListDiscoveredWorkloadsRequest request = new ListDiscoveredWorkloadsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> response = appHubClient.ListDiscoveredWorkloadsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DiscoveredWorkload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDiscoveredWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredWorkload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDiscoveredWorkloadsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> ListDiscoveredWorkloadsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Discovered Workloads that can be added to an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to list Discovered Workloads on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDiscoveredWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListDiscoveredWorkloadsResponse)[DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload)` | A pageable asynchronous sequence of [DiscoveredWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.DiscoveredWorkload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListDiscoveredWorkloadsResponse, DiscoveredWorkload> response = appHubClient.ListDiscoveredWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DiscoveredWorkload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDiscoveredWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DiscoveredWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DiscoveredWorkload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DiscoveredWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExtendedMetadataSchemas(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> ListExtendedMetadataSchemas(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Extended Metadata Schemas available in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to list Extended Metadata Schemas on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListExtendedMetadataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListExtendedMetadataSchemasResponse)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A pageable sequence of [ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> response = appHubClient.ListExtendedMetadataSchemas(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ExtendedMetadataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListExtendedMetadataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExtendedMetadataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExtendedMetadataSchema> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExtendedMetadataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExtendedMetadataSchemas(ListExtendedMetadataSchemasRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> ListExtendedMetadataSchemas(ListExtendedMetadataSchemasRequest request, CallSettings callSettings = null)

Lists Extended Metadata Schemas available in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExtendedMetadataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListExtendedMetadataSchemasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListExtendedMetadataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListExtendedMetadataSchemasResponse)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A pageable sequence of [ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ListExtendedMetadataSchemasRequest request = new ListExtendedMetadataSchemasRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> response = appHubClient.ListExtendedMetadataSchemas(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ExtendedMetadataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListExtendedMetadataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExtendedMetadataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExtendedMetadataSchema> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExtendedMetadataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExtendedMetadataSchemas(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> ListExtendedMetadataSchemas(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Extended Metadata Schemas available in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to list Extended Metadata Schemas on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListExtendedMetadataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListExtendedMetadataSchemasResponse)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A pageable sequence of [ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> response = appHubClient.ListExtendedMetadataSchemas(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ExtendedMetadataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListExtendedMetadataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExtendedMetadataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExtendedMetadataSchema> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExtendedMetadataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExtendedMetadataSchemasAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> ListExtendedMetadataSchemasAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Extended Metadata Schemas available in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Project and location to list Extended Metadata Schemas on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListExtendedMetadataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListExtendedMetadataSchemasResponse)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A pageable asynchronous sequence of [ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> response = appHubClient.ListExtendedMetadataSchemasAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ExtendedMetadataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListExtendedMetadataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExtendedMetadataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExtendedMetadataSchema> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExtendedMetadataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExtendedMetadataSchemasAsync(ListExtendedMetadataSchemasRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> ListExtendedMetadataSchemasAsync(ListExtendedMetadataSchemasRequest request, CallSettings callSettings = null)

Lists Extended Metadata Schemas available in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExtendedMetadataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListExtendedMetadataSchemasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListExtendedMetadataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListExtendedMetadataSchemasResponse)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A pageable asynchronous sequence of [ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ListExtendedMetadataSchemasRequest request = new ListExtendedMetadataSchemasRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> response = appHubClient.ListExtendedMetadataSchemasAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ExtendedMetadataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListExtendedMetadataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExtendedMetadataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExtendedMetadataSchema> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExtendedMetadataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExtendedMetadataSchemasAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> ListExtendedMetadataSchemasAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Extended Metadata Schemas available in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Project and location to list Extended Metadata Schemas on. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListExtendedMetadataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListExtendedMetadataSchemasResponse)[ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema)` | A pageable asynchronous sequence of [ExtendedMetadataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ExtendedMetadataSchema) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListExtendedMetadataSchemasResponse, ExtendedMetadataSchema> response = appHubClient.ListExtendedMetadataSchemasAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ExtendedMetadataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListExtendedMetadataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExtendedMetadataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExtendedMetadataSchema> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExtendedMetadataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServiceProjectAttachments(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> ListServiceProjectAttachments(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists service projects attached to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to list service project attachments. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListServiceProjectAttachmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServiceProjectAttachmentsResponse)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A pageable sequence of [ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> response = appHubClient.ListServiceProjectAttachments(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ServiceProjectAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListServiceProjectAttachmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceProjectAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceProjectAttachment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceProjectAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServiceProjectAttachments(ListServiceProjectAttachmentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> ListServiceProjectAttachments(ListServiceProjectAttachmentsRequest request, CallSettings callSettings = null)

Lists service projects attached to the host project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServiceProjectAttachmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServiceProjectAttachmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListServiceProjectAttachmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServiceProjectAttachmentsResponse)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A pageable sequence of [ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ListServiceProjectAttachmentsRequest request = new ListServiceProjectAttachmentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> response = appHubClient.ListServiceProjectAttachments(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ServiceProjectAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListServiceProjectAttachmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceProjectAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceProjectAttachment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceProjectAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServiceProjectAttachments(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> ListServiceProjectAttachments(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists service projects attached to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to list service project attachments. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListServiceProjectAttachmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServiceProjectAttachmentsResponse)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A pageable sequence of [ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> response = appHubClient.ListServiceProjectAttachments(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ServiceProjectAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListServiceProjectAttachmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceProjectAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceProjectAttachment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceProjectAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServiceProjectAttachmentsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> ListServiceProjectAttachmentsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists service projects attached to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to list service project attachments. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListServiceProjectAttachmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServiceProjectAttachmentsResponse)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A pageable asynchronous sequence of [ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> response = appHubClient.ListServiceProjectAttachmentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ServiceProjectAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListServiceProjectAttachmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceProjectAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceProjectAttachment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceProjectAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServiceProjectAttachmentsAsync(ListServiceProjectAttachmentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> ListServiceProjectAttachmentsAsync(ListServiceProjectAttachmentsRequest request, CallSettings callSettings = null)

Lists service projects attached to the host project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServiceProjectAttachmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServiceProjectAttachmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListServiceProjectAttachmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServiceProjectAttachmentsResponse)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A pageable asynchronous sequence of [ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ListServiceProjectAttachmentsRequest request = new ListServiceProjectAttachmentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> response = appHubClient.ListServiceProjectAttachmentsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ServiceProjectAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListServiceProjectAttachmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceProjectAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceProjectAttachment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceProjectAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServiceProjectAttachmentsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> ListServiceProjectAttachmentsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists service projects attached to the host project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to list service project attachments. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListServiceProjectAttachmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServiceProjectAttachmentsResponse)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` | A pageable asynchronous sequence of [ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListServiceProjectAttachmentsResponse, ServiceProjectAttachment> response = appHubClient.ListServiceProjectAttachmentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ServiceProjectAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListServiceProjectAttachmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceProjectAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceProjectAttachment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceProjectAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServices(ApplicationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListServicesResponse, Service> ListServices(ApplicationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Services in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the parent Application to list Services for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A pageable sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    PagedEnumerable<ListServicesResponse, Service> response = appHubClient.ListServices(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Service item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServices(ListServicesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListServicesResponse, Service> ListServices(ListServicesRequest request, CallSettings callSettings = null)

Lists Services in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServicesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A pageable sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ListServicesRequest request = new ListServicesRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListServicesResponse, Service> response = appHubClient.ListServices(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Service item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServices(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListServicesResponse, Service> ListServices(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Services in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the parent Application to list Services for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A pageable sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    PagedEnumerable<ListServicesResponse, Service> response = appHubClient.ListServices(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Service item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServicesAsync(ApplicationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListServicesResponse, Service> ListServicesAsync(ApplicationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Services in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the parent Application to list Services for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A pageable asynchronous sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    PagedAsyncEnumerable<ListServicesResponse, Service> response = appHubClient.ListServicesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Service item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServicesAsync(ListServicesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListServicesResponse, Service> ListServicesAsync(ListServicesRequest request, CallSettings callSettings = null)

Lists Services in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServicesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A pageable asynchronous sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ListServicesRequest request = new ListServicesRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListServicesResponse, Service> response = appHubClient.ListServicesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Service item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServicesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListServicesResponse, Service> ListServicesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Services in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the parent Application to list Services for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)` | A pageable asynchronous sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    PagedAsyncEnumerable<ListServicesResponse, Service> response = appHubClient.ListServicesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Service item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(ApplicationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, Workload> ListWorkloads(ApplicationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Workloads in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the parent Application to list Workloads for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A pageable sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    PagedEnumerable<ListWorkloadsResponse, Workload> response = appHubClient.ListWorkloads(parent);
    
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
    

### ListWorkloads(ListWorkloadsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, Workload> ListWorkloads(ListWorkloadsRequest request, CallSettings callSettings = null)

Lists Workloads in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A pageable sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    ListWorkloadsRequest request = new ListWorkloadsRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListWorkloadsResponse, Workload> response = appHubClient.ListWorkloads(request);
    
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

Lists Workloads in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the parent Application to list Workloads for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A pageable sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    PagedEnumerable<ListWorkloadsResponse, Workload> response = appHubClient.ListWorkloads(parent);
    
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
    

### ListWorkloadsAsync(ApplicationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, Workload> ListWorkloadsAsync(ApplicationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Workloads in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)`  
Required. Fully qualified name of the parent Application to list Workloads for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A pageable asynchronous sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    PagedAsyncEnumerable<ListWorkloadsResponse, Workload> response = appHubClient.ListWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Workload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListWorkloadsResponse page in response.AsRawResponses())
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
    

### ListWorkloadsAsync(ListWorkloadsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, Workload> ListWorkloadsAsync(ListWorkloadsRequest request, CallSettings callSettings = null)

Lists Workloads in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A pageable asynchronous sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    ListWorkloadsRequest request = new ListWorkloadsRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListWorkloadsResponse, Workload> response = appHubClient.ListWorkloadsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Workload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListWorkloadsResponse page in response.AsRawResponses())
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

Lists Workloads in an Application.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Fully qualified name of the parent Application to list Workloads for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)` | A pageable asynchronous sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload) resources.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    PagedAsyncEnumerable<ListWorkloadsResponse, Workload> response = appHubClient.ListWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Workload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListWorkloadsResponse page in response.AsRawResponses())
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
    

### LookupDiscoveredService(LocationName, string, CallSettings)
    
    
    public virtual LookupDiscoveredServiceResponse LookupDiscoveredService(LocationName parent, string uri, CallSettings callSettings = null)

Lists a Discovered Service in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to lookup Discovered Service in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find DiscoveredService for. Accepts both project number and project ID and does translation when needed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupDiscoveredServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string uri = "";
    // Make the request
    LookupDiscoveredServiceResponse response = appHubClient.LookupDiscoveredService(parent, uri);
    

### LookupDiscoveredService(LookupDiscoveredServiceRequest, CallSettings)
    
    
    public virtual LookupDiscoveredServiceResponse LookupDiscoveredService(LookupDiscoveredServiceRequest request, CallSettings callSettings = null)

Lists a Discovered Service in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupDiscoveredServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupDiscoveredServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LookupDiscoveredServiceRequest request = new LookupDiscoveredServiceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Uri = "",
    };
    // Make the request
    LookupDiscoveredServiceResponse response = appHubClient.LookupDiscoveredService(request);
    

### LookupDiscoveredService(string, string, CallSettings)
    
    
    public virtual LookupDiscoveredServiceResponse LookupDiscoveredService(string parent, string uri, CallSettings callSettings = null)

Lists a Discovered Service in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to lookup Discovered Service in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find DiscoveredService for. Accepts both project number and project ID and does translation when needed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupDiscoveredServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string uri = "";
    // Make the request
    LookupDiscoveredServiceResponse response = appHubClient.LookupDiscoveredService(parent, uri);
    

### LookupDiscoveredServiceAsync(LocationName, string, CallSettings)
    
    
    public virtual Task<LookupDiscoveredServiceResponse> LookupDiscoveredServiceAsync(LocationName parent, string uri, CallSettings callSettings = null)

Lists a Discovered Service in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to lookup Discovered Service in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find DiscoveredService for. Accepts both project number and project ID and does translation when needed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string uri = "";
    // Make the request
    LookupDiscoveredServiceResponse response = await appHubClient.LookupDiscoveredServiceAsync(parent, uri);
    

### LookupDiscoveredServiceAsync(LocationName, string, CancellationToken)
    
    
    public virtual Task<LookupDiscoveredServiceResponse> LookupDiscoveredServiceAsync(LocationName parent, string uri, CancellationToken cancellationToken)

Lists a Discovered Service in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to lookup Discovered Service in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find DiscoveredService for. Accepts both project number and project ID and does translation when needed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string uri = "";
    // Make the request
    LookupDiscoveredServiceResponse response = await appHubClient.LookupDiscoveredServiceAsync(parent, uri);
    

### LookupDiscoveredServiceAsync(LookupDiscoveredServiceRequest, CallSettings)
    
    
    public virtual Task<LookupDiscoveredServiceResponse> LookupDiscoveredServiceAsync(LookupDiscoveredServiceRequest request, CallSettings callSettings = null)

Lists a Discovered Service in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupDiscoveredServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LookupDiscoveredServiceRequest request = new LookupDiscoveredServiceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Uri = "",
    };
    // Make the request
    LookupDiscoveredServiceResponse response = await appHubClient.LookupDiscoveredServiceAsync(request);
    

### LookupDiscoveredServiceAsync(LookupDiscoveredServiceRequest, CancellationToken)
    
    
    public virtual Task<LookupDiscoveredServiceResponse> LookupDiscoveredServiceAsync(LookupDiscoveredServiceRequest request, CancellationToken cancellationToken)

Lists a Discovered Service in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupDiscoveredServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LookupDiscoveredServiceRequest request = new LookupDiscoveredServiceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Uri = "",
    };
    // Make the request
    LookupDiscoveredServiceResponse response = await appHubClient.LookupDiscoveredServiceAsync(request);
    

### LookupDiscoveredServiceAsync(string, string, CallSettings)
    
    
    public virtual Task<LookupDiscoveredServiceResponse> LookupDiscoveredServiceAsync(string parent, string uri, CallSettings callSettings = null)

Lists a Discovered Service in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to lookup Discovered Service in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find DiscoveredService for. Accepts both project number and project ID and does translation when needed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string uri = "";
    // Make the request
    LookupDiscoveredServiceResponse response = await appHubClient.LookupDiscoveredServiceAsync(parent, uri);
    

### LookupDiscoveredServiceAsync(string, string, CancellationToken)
    
    
    public virtual Task<LookupDiscoveredServiceResponse> LookupDiscoveredServiceAsync(string parent, string uri, CancellationToken cancellationToken)

Lists a Discovered Service in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to lookup Discovered Service in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find DiscoveredService for. Accepts both project number and project ID and does translation when needed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredServiceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string uri = "";
    // Make the request
    LookupDiscoveredServiceResponse response = await appHubClient.LookupDiscoveredServiceAsync(parent, uri);
    

### LookupDiscoveredWorkload(LocationName, string, CallSettings)
    
    
    public virtual LookupDiscoveredWorkloadResponse LookupDiscoveredWorkload(LocationName parent, string uri, CallSettings callSettings = null)

Lists a Discovered Workload in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to lookup Discovered Workload in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find Discovered Workload for. Accepts both project number and project ID and does translation when needed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupDiscoveredWorkloadResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string uri = "";
    // Make the request
    LookupDiscoveredWorkloadResponse response = appHubClient.LookupDiscoveredWorkload(parent, uri);
    

### LookupDiscoveredWorkload(LookupDiscoveredWorkloadRequest, CallSettings)
    
    
    public virtual LookupDiscoveredWorkloadResponse LookupDiscoveredWorkload(LookupDiscoveredWorkloadRequest request, CallSettings callSettings = null)

Lists a Discovered Workload in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupDiscoveredWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupDiscoveredWorkloadResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LookupDiscoveredWorkloadRequest request = new LookupDiscoveredWorkloadRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Uri = "",
    };
    // Make the request
    LookupDiscoveredWorkloadResponse response = appHubClient.LookupDiscoveredWorkload(request);
    

### LookupDiscoveredWorkload(string, string, CallSettings)
    
    
    public virtual LookupDiscoveredWorkloadResponse LookupDiscoveredWorkload(string parent, string uri, CallSettings callSettings = null)

Lists a Discovered Workload in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to lookup Discovered Workload in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find Discovered Workload for. Accepts both project number and project ID and does translation when needed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupDiscoveredWorkloadResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string uri = "";
    // Make the request
    LookupDiscoveredWorkloadResponse response = appHubClient.LookupDiscoveredWorkload(parent, uri);
    

### LookupDiscoveredWorkloadAsync(LocationName, string, CallSettings)
    
    
    public virtual Task<LookupDiscoveredWorkloadResponse> LookupDiscoveredWorkloadAsync(LocationName parent, string uri, CallSettings callSettings = null)

Lists a Discovered Workload in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to lookup Discovered Workload in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find Discovered Workload for. Accepts both project number and project ID and does translation when needed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredWorkloadResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string uri = "";
    // Make the request
    LookupDiscoveredWorkloadResponse response = await appHubClient.LookupDiscoveredWorkloadAsync(parent, uri);
    

### LookupDiscoveredWorkloadAsync(LocationName, string, CancellationToken)
    
    
    public virtual Task<LookupDiscoveredWorkloadResponse> LookupDiscoveredWorkloadAsync(LocationName parent, string uri, CancellationToken cancellationToken)

Lists a Discovered Workload in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Host project ID and location to lookup Discovered Workload in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find Discovered Workload for. Accepts both project number and project ID and does translation when needed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredWorkloadResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string uri = "";
    // Make the request
    LookupDiscoveredWorkloadResponse response = await appHubClient.LookupDiscoveredWorkloadAsync(parent, uri);
    

### LookupDiscoveredWorkloadAsync(LookupDiscoveredWorkloadRequest, CallSettings)
    
    
    public virtual Task<LookupDiscoveredWorkloadResponse> LookupDiscoveredWorkloadAsync(LookupDiscoveredWorkloadRequest request, CallSettings callSettings = null)

Lists a Discovered Workload in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupDiscoveredWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredWorkloadResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LookupDiscoveredWorkloadRequest request = new LookupDiscoveredWorkloadRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Uri = "",
    };
    // Make the request
    LookupDiscoveredWorkloadResponse response = await appHubClient.LookupDiscoveredWorkloadAsync(request);
    

### LookupDiscoveredWorkloadAsync(LookupDiscoveredWorkloadRequest, CancellationToken)
    
    
    public virtual Task<LookupDiscoveredWorkloadResponse> LookupDiscoveredWorkloadAsync(LookupDiscoveredWorkloadRequest request, CancellationToken cancellationToken)

Lists a Discovered Workload in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupDiscoveredWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredWorkloadResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LookupDiscoveredWorkloadRequest request = new LookupDiscoveredWorkloadRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Uri = "",
    };
    // Make the request
    LookupDiscoveredWorkloadResponse response = await appHubClient.LookupDiscoveredWorkloadAsync(request);
    

### LookupDiscoveredWorkloadAsync(string, string, CallSettings)
    
    
    public virtual Task<LookupDiscoveredWorkloadResponse> LookupDiscoveredWorkloadAsync(string parent, string uri, CallSettings callSettings = null)

Lists a Discovered Workload in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to lookup Discovered Workload in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find Discovered Workload for. Accepts both project number and project ID and does translation when needed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredWorkloadResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string uri = "";
    // Make the request
    LookupDiscoveredWorkloadResponse response = await appHubClient.LookupDiscoveredWorkloadAsync(parent, uri);
    

### LookupDiscoveredWorkloadAsync(string, string, CancellationToken)
    
    
    public virtual Task<LookupDiscoveredWorkloadResponse> LookupDiscoveredWorkloadAsync(string parent, string uri, CancellationToken cancellationToken)

Lists a Discovered Workload in a host project and location, with a given resource URI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Host project ID and location to lookup Discovered Workload in. Expected format: `projects/{project}/locations/{location}`.  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource URI to find Discovered Workload for. Accepts both project number and project ID and does translation when needed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupDiscoveredWorkloadResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupDiscoveredWorkloadResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string uri = "";
    // Make the request
    LookupDiscoveredWorkloadResponse response = await appHubClient.LookupDiscoveredWorkloadAsync(parent, uri);
    

### LookupServiceProjectAttachment(LocationName, CallSettings)
    
    
    public virtual LookupServiceProjectAttachmentResponse LookupServiceProjectAttachment(LocationName name, CallSettings callSettings = null)

Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Service project ID and location to lookup service project attachment for. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LocationName name = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    LookupServiceProjectAttachmentResponse response = appHubClient.LookupServiceProjectAttachment(name);
    

### LookupServiceProjectAttachment(LookupServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual LookupServiceProjectAttachmentResponse LookupServiceProjectAttachment(LookupServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    LookupServiceProjectAttachmentRequest request = new LookupServiceProjectAttachmentRequest
    {
        LocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    LookupServiceProjectAttachmentResponse response = appHubClient.LookupServiceProjectAttachment(request);
    

### LookupServiceProjectAttachment(string, CallSettings)
    
    
    public virtual LookupServiceProjectAttachmentResponse LookupServiceProjectAttachment(string name, CallSettings callSettings = null)

Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Service project ID and location to lookup service project attachment for. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    LookupServiceProjectAttachmentResponse response = appHubClient.LookupServiceProjectAttachment(name);
    

### LookupServiceProjectAttachmentAsync(LocationName, CallSettings)
    
    
    public virtual Task<LookupServiceProjectAttachmentResponse> LookupServiceProjectAttachmentAsync(LocationName name, CallSettings callSettings = null)

Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Service project ID and location to lookup service project attachment for. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName name = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    LookupServiceProjectAttachmentResponse response = await appHubClient.LookupServiceProjectAttachmentAsync(name);
    

### LookupServiceProjectAttachmentAsync(LocationName, CancellationToken)
    
    
    public virtual Task<LookupServiceProjectAttachmentResponse> LookupServiceProjectAttachmentAsync(LocationName name, CancellationToken cancellationToken)

Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Service project ID and location to lookup service project attachment for. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LocationName name = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    LookupServiceProjectAttachmentResponse response = await appHubClient.LookupServiceProjectAttachmentAsync(name);
    

### LookupServiceProjectAttachmentAsync(LookupServiceProjectAttachmentRequest, CallSettings)
    
    
    public virtual Task<LookupServiceProjectAttachmentResponse> LookupServiceProjectAttachmentAsync(LookupServiceProjectAttachmentRequest request, CallSettings callSettings = null)

Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LookupServiceProjectAttachmentRequest request = new LookupServiceProjectAttachmentRequest
    {
        LocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    LookupServiceProjectAttachmentResponse response = await appHubClient.LookupServiceProjectAttachmentAsync(request);
    

### LookupServiceProjectAttachmentAsync(LookupServiceProjectAttachmentRequest, CancellationToken)
    
    
    public virtual Task<LookupServiceProjectAttachmentResponse> LookupServiceProjectAttachmentAsync(LookupServiceProjectAttachmentRequest request, CancellationToken cancellationToken)

Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupServiceProjectAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    LookupServiceProjectAttachmentRequest request = new LookupServiceProjectAttachmentRequest
    {
        LocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    LookupServiceProjectAttachmentResponse response = await appHubClient.LookupServiceProjectAttachmentAsync(request);
    

### LookupServiceProjectAttachmentAsync(string, CallSettings)
    
    
    public virtual Task<LookupServiceProjectAttachmentResponse> LookupServiceProjectAttachmentAsync(string name, CallSettings callSettings = null)

Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Service project ID and location to lookup service project attachment for. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    LookupServiceProjectAttachmentResponse response = await appHubClient.LookupServiceProjectAttachmentAsync(name);
    

### LookupServiceProjectAttachmentAsync(string, CancellationToken)
    
    
    public virtual Task<LookupServiceProjectAttachmentResponse> LookupServiceProjectAttachmentAsync(string name, CancellationToken cancellationToken)

Lists a service project attachment for a given service project. You can call this API from any project to find if it is attached to a host project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Service project ID and location to lookup service project attachment for. Only global location is supported. Expected format: `projects/{project}/locations/{location}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    LookupServiceProjectAttachmentResponse response = await appHubClient.LookupServiceProjectAttachmentAsync(name);
    

### PollOnceCreateApplication(string, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> PollOnceCreateApplication(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateApplication` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> PollOnceCreateApplicationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateApplication`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateService(string, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> PollOnceCreateService(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateService`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateServiceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> PollOnceCreateServiceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateService`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateServiceProjectAttachment(string, CallSettings)
    
    
    public virtual Operation<ServiceProjectAttachment, OperationMetadata> PollOnceCreateServiceProjectAttachment(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateServiceProjectAttachment`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateServiceProjectAttachmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ServiceProjectAttachment, OperationMetadata>> PollOnceCreateServiceProjectAttachmentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateServiceProjectAttachment`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateWorkload(string, CallSettings)
    
    
    public virtual Operation<Workload, OperationMetadata> PollOnceCreateWorkload(string operationName, CallSettings callSettings = null)

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateWorkloadAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> PollOnceCreateWorkloadAsync(string operationName, CallSettings callSettings = null)

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteApplication(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteApplication(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteApplication` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteApplicationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteApplication`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteService(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteService(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteService`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteServiceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteServiceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteService`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteServiceProjectAttachment(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteServiceProjectAttachment(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteServiceProjectAttachment`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteServiceProjectAttachmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteServiceProjectAttachmentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteServiceProjectAttachment`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteWorkload(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteWorkload(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteWorkload`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteWorkloadAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteWorkloadAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteWorkload`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateApplication(string, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> PollOnceUpdateApplication(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateApplication` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> PollOnceUpdateApplicationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateApplication`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateBoundary(string, CallSettings)
    
    
    public virtual Operation<Boundary, OperationMetadata> PollOnceUpdateBoundary(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateBoundary`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateBoundaryAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Boundary, OperationMetadata>> PollOnceUpdateBoundaryAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateBoundary`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateService(string, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> PollOnceUpdateService(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateService`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateServiceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> PollOnceUpdateServiceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateService`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateWorkload(string, CallSettings)
    
    
    public virtual Operation<Workload, OperationMetadata> PollOnceUpdateWorkload(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateWorkload`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateWorkloadAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> PollOnceUpdateWorkloadAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateWorkload`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient#Google_Cloud_AppHub_V1_AppHubClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient#Google_Cloud_AppHub_V1_AppHubClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient#Google_Cloud_AppHub_V1_AppHubClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.AppHubClient#Google_Cloud_AppHub_V1_AppHubClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateApplication(Application, FieldMask, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> UpdateApplication(Application application, FieldMask updateMask, CallSettings callSettings = null)

Updates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Application resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    Application application = new Application();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Application, OperationMetadata> response = appHubClient.UpdateApplication(application, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appHubClient.PollOnceUpdateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplication(UpdateApplicationRequest, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> UpdateApplication(UpdateApplicationRequest request, CallSettings callSettings = null)

Updates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    UpdateApplicationRequest request = new UpdateApplicationRequest
    {
        UpdateMask = new FieldMask(),
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = appHubClient.UpdateApplication(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appHubClient.PollOnceUpdateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationAsync(Application, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> UpdateApplicationAsync(Application application, FieldMask updateMask, CallSettings callSettings = null)

Updates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Application resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    Application application = new Application();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.UpdateApplicationAsync(application, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationAsync(Application, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> UpdateApplicationAsync(Application application, FieldMask updateMask, CancellationToken cancellationToken)

Updates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Application resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    Application application = new Application();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.UpdateApplicationAsync(application, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationAsync(UpdateApplicationRequest, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> UpdateApplicationAsync(UpdateApplicationRequest request, CallSettings callSettings = null)

Updates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    UpdateApplicationRequest request = new UpdateApplicationRequest
    {
        UpdateMask = new FieldMask(),
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.UpdateApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationAsync(UpdateApplicationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> UpdateApplicationAsync(UpdateApplicationRequest request, CancellationToken cancellationToken)

Updates an Application in a host project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    UpdateApplicationRequest request = new UpdateApplicationRequest
    {
        UpdateMask = new FieldMask(),
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = await appHubClient.UpdateApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBoundary(Boundary, FieldMask, CallSettings)
    
    
    public virtual Operation<Boundary, OperationMetadata> UpdateBoundary(Boundary boundary, FieldMask updateMask, CallSettings callSettings = null)

Updates a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`boundary` | `[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)`  
Required. The boundary to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Boundary resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    Boundary boundary = new Boundary();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Boundary, OperationMetadata> response = appHubClient.UpdateBoundary(boundary, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Boundary, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Boundary result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Boundary, OperationMetadata> retrievedResponse = appHubClient.PollOnceUpdateBoundary(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Boundary retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBoundary(UpdateBoundaryRequest, CallSettings)
    
    
    public virtual Operation<Boundary, OperationMetadata> UpdateBoundary(UpdateBoundaryRequest request, CallSettings callSettings = null)

Updates a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBoundaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateBoundaryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    UpdateBoundaryRequest request = new UpdateBoundaryRequest
    {
        UpdateMask = new FieldMask(),
        Boundary = new Boundary(),
        RequestId = "",
    };
    // Make the request
    Operation<Boundary, OperationMetadata> response = appHubClient.UpdateBoundary(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Boundary, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Boundary result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Boundary, OperationMetadata> retrievedResponse = appHubClient.PollOnceUpdateBoundary(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Boundary retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBoundaryAsync(Boundary, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Boundary, OperationMetadata>> UpdateBoundaryAsync(Boundary boundary, FieldMask updateMask, CallSettings callSettings = null)

Updates a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`boundary` | `[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)`  
Required. The boundary to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Boundary resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    Boundary boundary = new Boundary();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Boundary, OperationMetadata> response = await appHubClient.UpdateBoundaryAsync(boundary, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Boundary, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Boundary result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Boundary, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateBoundaryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Boundary retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBoundaryAsync(Boundary, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Boundary, OperationMetadata>> UpdateBoundaryAsync(Boundary boundary, FieldMask updateMask, CancellationToken cancellationToken)

Updates a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`boundary` | `[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)`  
Required. The boundary to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Boundary resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    Boundary boundary = new Boundary();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Boundary, OperationMetadata> response = await appHubClient.UpdateBoundaryAsync(boundary, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Boundary, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Boundary result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Boundary, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateBoundaryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Boundary retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBoundaryAsync(UpdateBoundaryRequest, CallSettings)
    
    
    public virtual Task<Operation<Boundary, OperationMetadata>> UpdateBoundaryAsync(UpdateBoundaryRequest request, CallSettings callSettings = null)

Updates a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBoundaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateBoundaryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    UpdateBoundaryRequest request = new UpdateBoundaryRequest
    {
        UpdateMask = new FieldMask(),
        Boundary = new Boundary(),
        RequestId = "",
    };
    // Make the request
    Operation<Boundary, OperationMetadata> response = await appHubClient.UpdateBoundaryAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Boundary, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Boundary result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Boundary, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateBoundaryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Boundary retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBoundaryAsync(UpdateBoundaryRequest, CancellationToken)
    
    
    public virtual Task<Operation<Boundary, OperationMetadata>> UpdateBoundaryAsync(UpdateBoundaryRequest request, CancellationToken cancellationToken)

Updates a Boundary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBoundaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateBoundaryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Boundary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Boundary)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    UpdateBoundaryRequest request = new UpdateBoundaryRequest
    {
        UpdateMask = new FieldMask(),
        Boundary = new Boundary(),
        RequestId = "",
    };
    // Make the request
    Operation<Boundary, OperationMetadata> response = await appHubClient.UpdateBoundaryAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Boundary, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Boundary result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Boundary, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateBoundaryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Boundary retrievedResult = retrievedResponse.Result;
    }
    

### UpdateService(Service, FieldMask, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> UpdateService(Service service, FieldMask updateMask, CallSettings callSettings = null)

Updates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Service resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    Service service = new Service();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Service, OperationMetadata> response = appHubClient.UpdateService(service, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = appHubClient.PollOnceUpdateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateService(UpdateServiceRequest, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> UpdateService(UpdateServiceRequest request, CallSettings callSettings = null)

Updates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    UpdateServiceRequest request = new UpdateServiceRequest
    {
        UpdateMask = new FieldMask(),
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = appHubClient.UpdateService(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = appHubClient.PollOnceUpdateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateServiceAsync(Service, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> UpdateServiceAsync(Service service, FieldMask updateMask, CallSettings callSettings = null)

Updates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Service resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    Service service = new Service();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.UpdateServiceAsync(service, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateServiceAsync(Service, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> UpdateServiceAsync(Service service, FieldMask updateMask, CancellationToken cancellationToken)

Updates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Service resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    Service service = new Service();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.UpdateServiceAsync(service, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateServiceAsync(UpdateServiceRequest, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> UpdateServiceAsync(UpdateServiceRequest request, CallSettings callSettings = null)

Updates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    UpdateServiceRequest request = new UpdateServiceRequest
    {
        UpdateMask = new FieldMask(),
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.UpdateServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateServiceAsync(UpdateServiceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> UpdateServiceAsync(UpdateServiceRequest request, CancellationToken cancellationToken)

Updates a Service in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    UpdateServiceRequest request = new UpdateServiceRequest
    {
        UpdateMask = new FieldMask(),
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = await appHubClient.UpdateServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateWorkload(UpdateWorkloadRequest, CallSettings)
    
    
    public virtual Operation<Workload, OperationMetadata> UpdateWorkload(UpdateWorkloadRequest request, CallSettings callSettings = null)

Updates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    UpdateWorkloadRequest request = new UpdateWorkloadRequest
    {
        UpdateMask = new FieldMask(),
        Workload = new Workload(),
        RequestId = "",
    };
    // Make the request
    Operation<Workload, OperationMetadata> response = appHubClient.UpdateWorkload(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = appHubClient.PollOnceUpdateWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### UpdateWorkload(Workload, FieldMask, CallSettings)
    
    
    public virtual Operation<Workload, OperationMetadata> UpdateWorkload(Workload workload, FieldMask updateMask, CallSettings callSettings = null)

Updates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Workload resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = AppHubClient.Create();
    // Initialize request argument(s)
    Workload workload = new Workload();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Workload, OperationMetadata> response = appHubClient.UpdateWorkload(workload, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = appHubClient.PollOnceUpdateWorkload(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### UpdateWorkloadAsync(UpdateWorkloadRequest, CallSettings)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> UpdateWorkloadAsync(UpdateWorkloadRequest request, CallSettings callSettings = null)

Updates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    UpdateWorkloadRequest request = new UpdateWorkloadRequest
    {
        UpdateMask = new FieldMask(),
        Workload = new Workload(),
        RequestId = "",
    };
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.UpdateWorkloadAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### UpdateWorkloadAsync(UpdateWorkloadRequest, CancellationToken)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> UpdateWorkloadAsync(UpdateWorkloadRequest request, CancellationToken cancellationToken)

Updates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.UpdateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    UpdateWorkloadRequest request = new UpdateWorkloadRequest
    {
        UpdateMask = new FieldMask(),
        Workload = new Workload(),
        RequestId = "",
    };
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.UpdateWorkloadAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### UpdateWorkloadAsync(Workload, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> UpdateWorkloadAsync(Workload workload, FieldMask updateMask, CallSettings callSettings = null)

Updates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Workload resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    Workload workload = new Workload();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.UpdateWorkloadAsync(workload, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

### UpdateWorkloadAsync(Workload, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Workload, OperationMetadata>> UpdateWorkloadAsync(Workload workload, FieldMask updateMask, CancellationToken cancellationToken)

Updates a Workload in an Application.

**Parameters**  
---  
**Name** | **Description**  
`workload` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Workload resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. The API changes the values of the fields as specified in the update_mask. The API ignores the values of all fields not covered by the update_mask. You can also unset a field by not specifying it in the updated message, but adding the field to the mask. This clears whatever value the field previously had.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.Workload)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppHubClient appHubClient = await AppHubClient.CreateAsync();
    // Initialize request argument(s)
    Workload workload = new Workload();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Workload, OperationMetadata> response = await appHubClient.UpdateWorkloadAsync(workload, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Workload, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Workload result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Workload, OperationMetadata> retrievedResponse = await appHubClient.PollOnceUpdateWorkloadAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Workload retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
