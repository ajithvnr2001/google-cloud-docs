---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient
title: Google Cloud OS Config v1alpha API - Class OsConfigZonalServiceClient (2.0.0-alpha07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:35.966935+00:00
---

# Google Cloud OS Config v1alpha API - Class OsConfigZonalServiceClient (2.0.0-alpha07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud OS Config v1alpha API - Class OsConfigZonalServiceClient (2.0.0-alpha07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient)
  * [ 2.0.0-alpha06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/2.0.0-alpha06/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient)
  * [ 1.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/1.0.0-alpha04/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient)


    
    
    public abstract class OsConfigZonalServiceClient

Reference documentation and code samples for the Google Cloud OS Config v1alpha API class OsConfigZonalServiceClient.

OsConfigZonalService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OsConfigZonalServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[OsConfigZonalServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClientImpl)

## Namespace

[Google.Cloud.OsConfig.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha)

## Assembly

Google.Cloud.OsConfig.V1Alpha.dll

## Remarks

Zonal OS Config API

The OS Config service is the server-side component that allows users to manage package installations and patch jobs for Compute Engine VM instances.

## Properties 

### CreateOSPolicyAssignmentOperationsClient
    
    
    public virtual OperationsClient CreateOSPolicyAssignmentOperationsClient { get; }

The long-running operations client for `CreateOSPolicyAssignment`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the OsConfigZonalService service, which is a host of "osconfig.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default OsConfigZonalService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default OsConfigZonalService scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteOSPolicyAssignmentOperationsClient
    
    
    public virtual OperationsClient DeleteOSPolicyAssignmentOperationsClient { get; }

The long-running operations client for `DeleteOSPolicyAssignment`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual OsConfigZonalService.OsConfigZonalServiceClient GrpcClient { get; }

The underlying gRPC OsConfigZonalService client

**Property Value**  
---  
**Type** | **Description**  
`[OsConfigZonalService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalService)[OsConfigZonalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalService.OsConfigZonalServiceClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
### UpdateOSPolicyAssignmentOperationsClient
    
    
    public virtual OperationsClient UpdateOSPolicyAssignmentOperationsClient { get; }

The long-running operations client for `UpdateOSPolicyAssignment`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static OsConfigZonalServiceClient Create()

Synchronously creates a [OsConfigZonalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [OsConfigZonalServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient)` | The created [OsConfigZonalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<OsConfigZonalServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [OsConfigZonalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [OsConfigZonalServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OsConfigZonalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient)` | The task representing the created [OsConfigZonalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient).  
  
### CreateOSPolicyAssignment(LocationName, OSPolicyAssignment, string, CallSettings)
    
    
    public virtual Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> CreateOSPolicyAssignment(LocationName parent, OSPolicyAssignment osPolicyAssignment, string osPolicyAssignmentId, CallSettings callSettings = null)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name in the form: projects/{project}/locations/{location}  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)`  
Required. The OS policy assignment to be created.  
`osPolicyAssignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the OS policy assignment in the project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the project.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    OSPolicyAssignment osPolicyAssignment = new OSPolicyAssignment();
    string osPolicyAssignmentId = "";
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = osConfigZonalServiceClient.CreateOSPolicyAssignment(parent, osPolicyAssignment, osPolicyAssignmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = osConfigZonalServiceClient.PollOnceCreateOSPolicyAssignment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### CreateOSPolicyAssignment(CreateOSPolicyAssignmentRequest, CallSettings)
    
    
    public virtual Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> CreateOSPolicyAssignment(CreateOSPolicyAssignmentRequest request, CallSettings callSettings = null)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CreateOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    CreateOSPolicyAssignmentRequest request = new CreateOSPolicyAssignmentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        OsPolicyAssignment = new OSPolicyAssignment(),
        OsPolicyAssignmentId = "",
    };
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = osConfigZonalServiceClient.CreateOSPolicyAssignment(request);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = osConfigZonalServiceClient.PollOnceCreateOSPolicyAssignment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### CreateOSPolicyAssignment(string, OSPolicyAssignment, string, CallSettings)
    
    
    public virtual Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> CreateOSPolicyAssignment(string parent, OSPolicyAssignment osPolicyAssignment, string osPolicyAssignmentId, CallSettings callSettings = null)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name in the form: projects/{project}/locations/{location}  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)`  
Required. The OS policy assignment to be created.  
`osPolicyAssignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the OS policy assignment in the project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the project.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    OSPolicyAssignment osPolicyAssignment = new OSPolicyAssignment();
    string osPolicyAssignmentId = "";
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = osConfigZonalServiceClient.CreateOSPolicyAssignment(parent, osPolicyAssignment, osPolicyAssignmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = osConfigZonalServiceClient.PollOnceCreateOSPolicyAssignment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### CreateOSPolicyAssignmentAsync(LocationName, OSPolicyAssignment, string, CallSettings)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> CreateOSPolicyAssignmentAsync(LocationName parent, OSPolicyAssignment osPolicyAssignment, string osPolicyAssignmentId, CallSettings callSettings = null)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name in the form: projects/{project}/locations/{location}  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)`  
Required. The OS policy assignment to be created.  
`osPolicyAssignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the OS policy assignment in the project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the project.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    OSPolicyAssignment osPolicyAssignment = new OSPolicyAssignment();
    string osPolicyAssignmentId = "";
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.CreateOSPolicyAssignmentAsync(parent, osPolicyAssignment, osPolicyAssignmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceCreateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### CreateOSPolicyAssignmentAsync(LocationName, OSPolicyAssignment, string, CancellationToken)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> CreateOSPolicyAssignmentAsync(LocationName parent, OSPolicyAssignment osPolicyAssignment, string osPolicyAssignmentId, CancellationToken cancellationToken)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name in the form: projects/{project}/locations/{location}  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)`  
Required. The OS policy assignment to be created.  
`osPolicyAssignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the OS policy assignment in the project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the project.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    OSPolicyAssignment osPolicyAssignment = new OSPolicyAssignment();
    string osPolicyAssignmentId = "";
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.CreateOSPolicyAssignmentAsync(parent, osPolicyAssignment, osPolicyAssignmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceCreateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### CreateOSPolicyAssignmentAsync(CreateOSPolicyAssignmentRequest, CallSettings)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> CreateOSPolicyAssignmentAsync(CreateOSPolicyAssignmentRequest request, CallSettings callSettings = null)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CreateOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateOSPolicyAssignmentRequest request = new CreateOSPolicyAssignmentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        OsPolicyAssignment = new OSPolicyAssignment(),
        OsPolicyAssignmentId = "",
    };
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.CreateOSPolicyAssignmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceCreateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### CreateOSPolicyAssignmentAsync(CreateOSPolicyAssignmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> CreateOSPolicyAssignmentAsync(CreateOSPolicyAssignmentRequest request, CancellationToken cancellationToken)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CreateOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateOSPolicyAssignmentRequest request = new CreateOSPolicyAssignmentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        OsPolicyAssignment = new OSPolicyAssignment(),
        OsPolicyAssignmentId = "",
    };
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.CreateOSPolicyAssignmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceCreateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### CreateOSPolicyAssignmentAsync(string, OSPolicyAssignment, string, CallSettings)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> CreateOSPolicyAssignmentAsync(string parent, OSPolicyAssignment osPolicyAssignment, string osPolicyAssignmentId, CallSettings callSettings = null)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name in the form: projects/{project}/locations/{location}  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)`  
Required. The OS policy assignment to be created.  
`osPolicyAssignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the OS policy assignment in the project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the project.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    OSPolicyAssignment osPolicyAssignment = new OSPolicyAssignment();
    string osPolicyAssignmentId = "";
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.CreateOSPolicyAssignmentAsync(parent, osPolicyAssignment, osPolicyAssignmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceCreateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### CreateOSPolicyAssignmentAsync(string, OSPolicyAssignment, string, CancellationToken)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> CreateOSPolicyAssignmentAsync(string parent, OSPolicyAssignment osPolicyAssignment, string osPolicyAssignmentId, CancellationToken cancellationToken)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name in the form: projects/{project}/locations/{location}  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)`  
Required. The OS policy assignment to be created.  
`osPolicyAssignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the OS policy assignment in the project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the project.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    OSPolicyAssignment osPolicyAssignment = new OSPolicyAssignment();
    string osPolicyAssignmentId = "";
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.CreateOSPolicyAssignmentAsync(parent, osPolicyAssignment, osPolicyAssignmentId);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceCreateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### DeleteOSPolicyAssignment(DeleteOSPolicyAssignmentRequest, CallSettings)
    
    
    public virtual Operation<Empty, OSPolicyAssignmentOperationMetadata> DeleteOSPolicyAssignment(DeleteOSPolicyAssignmentRequest request, CallSettings callSettings = null)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.DeleteOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    DeleteOSPolicyAssignmentRequest request = new DeleteOSPolicyAssignmentRequest
    {
        OSPolicyAssignmentName = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]"),
    };
    // Make the request
    Operation<Empty, OSPolicyAssignmentOperationMetadata> response = osConfigZonalServiceClient.DeleteOSPolicyAssignment(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OSPolicyAssignmentOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OSPolicyAssignmentOperationMetadata> retrievedResponse = osConfigZonalServiceClient.PollOnceDeleteOSPolicyAssignment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteOSPolicyAssignment(OSPolicyAssignmentName, CallSettings)
    
    
    public virtual Operation<Empty, OSPolicyAssignmentOperationMetadata> DeleteOSPolicyAssignment(OSPolicyAssignmentName name, CallSettings callSettings = null)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)`  
Required. The name of the OS policy assignment to be deleted  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    OSPolicyAssignmentName name = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
    // Make the request
    Operation<Empty, OSPolicyAssignmentOperationMetadata> response = osConfigZonalServiceClient.DeleteOSPolicyAssignment(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OSPolicyAssignmentOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OSPolicyAssignmentOperationMetadata> retrievedResponse = osConfigZonalServiceClient.PollOnceDeleteOSPolicyAssignment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteOSPolicyAssignment(string, CallSettings)
    
    
    public virtual Operation<Empty, OSPolicyAssignmentOperationMetadata> DeleteOSPolicyAssignment(string name, CallSettings callSettings = null)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the OS policy assignment to be deleted  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/osPolicyAssignments/[OS_POLICY_ASSIGNMENT]";
    // Make the request
    Operation<Empty, OSPolicyAssignmentOperationMetadata> response = osConfigZonalServiceClient.DeleteOSPolicyAssignment(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OSPolicyAssignmentOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OSPolicyAssignmentOperationMetadata> retrievedResponse = osConfigZonalServiceClient.PollOnceDeleteOSPolicyAssignment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteOSPolicyAssignmentAsync(DeleteOSPolicyAssignmentRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OSPolicyAssignmentOperationMetadata>> DeleteOSPolicyAssignmentAsync(DeleteOSPolicyAssignmentRequest request, CallSettings callSettings = null)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.DeleteOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteOSPolicyAssignmentRequest request = new DeleteOSPolicyAssignmentRequest
    {
        OSPolicyAssignmentName = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]"),
    };
    // Make the request
    Operation<Empty, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.DeleteOSPolicyAssignmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceDeleteOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteOSPolicyAssignmentAsync(DeleteOSPolicyAssignmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OSPolicyAssignmentOperationMetadata>> DeleteOSPolicyAssignmentAsync(DeleteOSPolicyAssignmentRequest request, CancellationToken cancellationToken)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.DeleteOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteOSPolicyAssignmentRequest request = new DeleteOSPolicyAssignmentRequest
    {
        OSPolicyAssignmentName = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]"),
    };
    // Make the request
    Operation<Empty, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.DeleteOSPolicyAssignmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceDeleteOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteOSPolicyAssignmentAsync(OSPolicyAssignmentName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OSPolicyAssignmentOperationMetadata>> DeleteOSPolicyAssignmentAsync(OSPolicyAssignmentName name, CallSettings callSettings = null)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)`  
Required. The name of the OS policy assignment to be deleted  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    OSPolicyAssignmentName name = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
    // Make the request
    Operation<Empty, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.DeleteOSPolicyAssignmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceDeleteOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteOSPolicyAssignmentAsync(OSPolicyAssignmentName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OSPolicyAssignmentOperationMetadata>> DeleteOSPolicyAssignmentAsync(OSPolicyAssignmentName name, CancellationToken cancellationToken)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)`  
Required. The name of the OS policy assignment to be deleted  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    OSPolicyAssignmentName name = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
    // Make the request
    Operation<Empty, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.DeleteOSPolicyAssignmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceDeleteOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteOSPolicyAssignmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OSPolicyAssignmentOperationMetadata>> DeleteOSPolicyAssignmentAsync(string name, CallSettings callSettings = null)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the OS policy assignment to be deleted  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/osPolicyAssignments/[OS_POLICY_ASSIGNMENT]";
    // Make the request
    Operation<Empty, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.DeleteOSPolicyAssignmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceDeleteOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteOSPolicyAssignmentAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OSPolicyAssignmentOperationMetadata>> DeleteOSPolicyAssignmentAsync(string name, CancellationToken cancellationToken)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the OS policy assignment to be deleted  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/osPolicyAssignments/[OS_POLICY_ASSIGNMENT]";
    // Make the request
    Operation<Empty, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.DeleteOSPolicyAssignmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceDeleteOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetInstanceOSPoliciesCompliance(GetInstanceOSPoliciesComplianceRequest, CallSettings)
    
    
    [Obsolete]
    public virtual InstanceOSPoliciesCompliance GetInstanceOSPoliciesCompliance(GetInstanceOSPoliciesComplianceRequest request, CallSettings callSettings = null)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInstanceOSPoliciesComplianceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | The RPC response.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
                // Initialize request argument(s)
    #pragma warning disable CS0612
                GetInstanceOSPoliciesComplianceRequest request = new GetInstanceOSPoliciesComplianceRequest { };
    #pragma warning restore CS0612
                // Make the request
    #pragma warning disable CS0612
                InstanceOSPoliciesCompliance response = osConfigZonalServiceClient.GetInstanceOSPoliciesCompliance(request);
    #pragma warning restore CS0612
    

### GetInstanceOSPoliciesCompliance(InstanceOSPoliciesComplianceName, CallSettings)
    
    
    [Obsolete]
    public virtual InstanceOSPoliciesCompliance GetInstanceOSPoliciesCompliance(InstanceOSPoliciesComplianceName name, CallSettings callSettings = null)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceOSPoliciesComplianceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesComplianceName)`  
Required. API resource name for instance OS policies compliance resource. Format: `projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}` For `{project}`, either Compute Engine project-number or project-id can be provided. For `{instance}`, either Compute Engine VM instance-id or instance-name can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | The RPC response.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
                // Initialize request argument(s)
                InstanceOSPoliciesComplianceName name = InstanceOSPoliciesComplianceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
                // Make the request
    #pragma warning disable CS0612
                InstanceOSPoliciesCompliance response = osConfigZonalServiceClient.GetInstanceOSPoliciesCompliance(name);
    #pragma warning restore CS0612
    

### GetInstanceOSPoliciesCompliance(string, CallSettings)
    
    
    [Obsolete]
    public virtual InstanceOSPoliciesCompliance GetInstanceOSPoliciesCompliance(string name, CallSettings callSettings = null)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for instance OS policies compliance resource. Format: `projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}` For `{project}`, either Compute Engine project-number or project-id can be provided. For `{instance}`, either Compute Engine VM instance-id or instance-name can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | The RPC response.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
                // Initialize request argument(s)
                string name = "projects/[PROJECT]/locations/[LOCATION]/instanceOSPoliciesCompliances/[INSTANCE]";
                // Make the request
    #pragma warning disable CS0612
                InstanceOSPoliciesCompliance response = osConfigZonalServiceClient.GetInstanceOSPoliciesCompliance(name);
    #pragma warning restore CS0612
    

### GetInstanceOSPoliciesComplianceAsync(GetInstanceOSPoliciesComplianceRequest, CallSettings)
    
    
    [Obsolete]
    public virtual Task<InstanceOSPoliciesCompliance> GetInstanceOSPoliciesComplianceAsync(GetInstanceOSPoliciesComplianceRequest request, CallSettings callSettings = null)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInstanceOSPoliciesComplianceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
                // Initialize request argument(s)
    #pragma warning disable CS0612
                GetInstanceOSPoliciesComplianceRequest request = new GetInstanceOSPoliciesComplianceRequest { };
    #pragma warning restore CS0612
                // Make the request
    #pragma warning disable CS0612
                InstanceOSPoliciesCompliance response = await osConfigZonalServiceClient.GetInstanceOSPoliciesComplianceAsync(request);
    #pragma warning restore CS0612
    

### GetInstanceOSPoliciesComplianceAsync(GetInstanceOSPoliciesComplianceRequest, CancellationToken)
    
    
    [Obsolete]
    public virtual Task<InstanceOSPoliciesCompliance> GetInstanceOSPoliciesComplianceAsync(GetInstanceOSPoliciesComplianceRequest request, CancellationToken cancellationToken)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInstanceOSPoliciesComplianceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
                // Initialize request argument(s)
    #pragma warning disable CS0612
                GetInstanceOSPoliciesComplianceRequest request = new GetInstanceOSPoliciesComplianceRequest { };
    #pragma warning restore CS0612
                // Make the request
    #pragma warning disable CS0612
                InstanceOSPoliciesCompliance response = await osConfigZonalServiceClient.GetInstanceOSPoliciesComplianceAsync(request);
    #pragma warning restore CS0612
    

### GetInstanceOSPoliciesComplianceAsync(InstanceOSPoliciesComplianceName, CallSettings)
    
    
    [Obsolete]
    public virtual Task<InstanceOSPoliciesCompliance> GetInstanceOSPoliciesComplianceAsync(InstanceOSPoliciesComplianceName name, CallSettings callSettings = null)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceOSPoliciesComplianceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesComplianceName)`  
Required. API resource name for instance OS policies compliance resource. Format: `projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}` For `{project}`, either Compute Engine project-number or project-id can be provided. For `{instance}`, either Compute Engine VM instance-id or instance-name can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
                // Initialize request argument(s)
                InstanceOSPoliciesComplianceName name = InstanceOSPoliciesComplianceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
                // Make the request
    #pragma warning disable CS0612
                InstanceOSPoliciesCompliance response = await osConfigZonalServiceClient.GetInstanceOSPoliciesComplianceAsync(name);
    #pragma warning restore CS0612
    

### GetInstanceOSPoliciesComplianceAsync(InstanceOSPoliciesComplianceName, CancellationToken)
    
    
    [Obsolete]
    public virtual Task<InstanceOSPoliciesCompliance> GetInstanceOSPoliciesComplianceAsync(InstanceOSPoliciesComplianceName name, CancellationToken cancellationToken)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceOSPoliciesComplianceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesComplianceName)`  
Required. API resource name for instance OS policies compliance resource. Format: `projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}` For `{project}`, either Compute Engine project-number or project-id can be provided. For `{instance}`, either Compute Engine VM instance-id or instance-name can be provided.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
                // Initialize request argument(s)
                InstanceOSPoliciesComplianceName name = InstanceOSPoliciesComplianceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
                // Make the request
    #pragma warning disable CS0612
                InstanceOSPoliciesCompliance response = await osConfigZonalServiceClient.GetInstanceOSPoliciesComplianceAsync(name);
    #pragma warning restore CS0612
    

### GetInstanceOSPoliciesComplianceAsync(string, CallSettings)
    
    
    [Obsolete]
    public virtual Task<InstanceOSPoliciesCompliance> GetInstanceOSPoliciesComplianceAsync(string name, CallSettings callSettings = null)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for instance OS policies compliance resource. Format: `projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}` For `{project}`, either Compute Engine project-number or project-id can be provided. For `{instance}`, either Compute Engine VM instance-id or instance-name can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
                // Initialize request argument(s)
                string name = "projects/[PROJECT]/locations/[LOCATION]/instanceOSPoliciesCompliances/[INSTANCE]";
                // Make the request
    #pragma warning disable CS0612
                InstanceOSPoliciesCompliance response = await osConfigZonalServiceClient.GetInstanceOSPoliciesComplianceAsync(name);
    #pragma warning restore CS0612
    

### GetInstanceOSPoliciesComplianceAsync(string, CancellationToken)
    
    
    [Obsolete]
    public virtual Task<InstanceOSPoliciesCompliance> GetInstanceOSPoliciesComplianceAsync(string name, CancellationToken cancellationToken)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for instance OS policies compliance resource. Format: `projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}` For `{project}`, either Compute Engine project-number or project-id can be provided. For `{instance}`, either Compute Engine VM instance-id or instance-name can be provided.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
                // Initialize request argument(s)
                string name = "projects/[PROJECT]/locations/[LOCATION]/instanceOSPoliciesCompliances/[INSTANCE]";
                // Make the request
    #pragma warning disable CS0612
                InstanceOSPoliciesCompliance response = await osConfigZonalServiceClient.GetInstanceOSPoliciesComplianceAsync(name);
    #pragma warning restore CS0612
    

### GetInventory(GetInventoryRequest, CallSettings)
    
    
    public virtual Inventory GetInventory(GetInventoryRequest request, CallSettings callSettings = null)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    GetInventoryRequest request = new GetInventoryRequest
    {
        InventoryName = InventoryName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        View = InventoryView.Unspecified,
    };
    // Make the request
    Inventory response = osConfigZonalServiceClient.GetInventory(request);
    

### GetInventory(InventoryName, CallSettings)
    
    
    public virtual Inventory GetInventory(InventoryName name, CallSettings callSettings = null)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InventoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InventoryName)`  
Required. API resource name for inventory resource. Format: `projects/{project}/locations/{location}/instances/{instance}/inventory` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    InventoryName name = InventoryName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Inventory response = osConfigZonalServiceClient.GetInventory(name);
    

### GetInventory(string, CallSettings)
    
    
    public virtual Inventory GetInventory(string name, CallSettings callSettings = null)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for inventory resource. Format: `projects/{project}/locations/{location}/instances/{instance}/inventory` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/inventory";
    // Make the request
    Inventory response = osConfigZonalServiceClient.GetInventory(name);
    

### GetInventoryAsync(GetInventoryRequest, CallSettings)
    
    
    public virtual Task<Inventory> GetInventoryAsync(GetInventoryRequest request, CallSettings callSettings = null)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetInventoryRequest request = new GetInventoryRequest
    {
        InventoryName = InventoryName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        View = InventoryView.Unspecified,
    };
    // Make the request
    Inventory response = await osConfigZonalServiceClient.GetInventoryAsync(request);
    

### GetInventoryAsync(GetInventoryRequest, CancellationToken)
    
    
    public virtual Task<Inventory> GetInventoryAsync(GetInventoryRequest request, CancellationToken cancellationToken)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetInventoryRequest request = new GetInventoryRequest
    {
        InventoryName = InventoryName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        View = InventoryView.Unspecified,
    };
    // Make the request
    Inventory response = await osConfigZonalServiceClient.GetInventoryAsync(request);
    

### GetInventoryAsync(InventoryName, CallSettings)
    
    
    public virtual Task<Inventory> GetInventoryAsync(InventoryName name, CallSettings callSettings = null)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InventoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InventoryName)`  
Required. API resource name for inventory resource. Format: `projects/{project}/locations/{location}/instances/{instance}/inventory` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    InventoryName name = InventoryName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Inventory response = await osConfigZonalServiceClient.GetInventoryAsync(name);
    

### GetInventoryAsync(InventoryName, CancellationToken)
    
    
    public virtual Task<Inventory> GetInventoryAsync(InventoryName name, CancellationToken cancellationToken)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InventoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InventoryName)`  
Required. API resource name for inventory resource. Format: `projects/{project}/locations/{location}/instances/{instance}/inventory` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    InventoryName name = InventoryName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Inventory response = await osConfigZonalServiceClient.GetInventoryAsync(name);
    

### GetInventoryAsync(string, CallSettings)
    
    
    public virtual Task<Inventory> GetInventoryAsync(string name, CallSettings callSettings = null)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for inventory resource. Format: `projects/{project}/locations/{location}/instances/{instance}/inventory` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/inventory";
    // Make the request
    Inventory response = await osConfigZonalServiceClient.GetInventoryAsync(name);
    

### GetInventoryAsync(string, CancellationToken)
    
    
    public virtual Task<Inventory> GetInventoryAsync(string name, CancellationToken cancellationToken)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for inventory resource. Format: `projects/{project}/locations/{location}/instances/{instance}/inventory` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/inventory";
    // Make the request
    Inventory response = await osConfigZonalServiceClient.GetInventoryAsync(name);
    

### GetOSPolicyAssignment(GetOSPolicyAssignmentRequest, CallSettings)
    
    
    public virtual OSPolicyAssignment GetOSPolicyAssignment(GetOSPolicyAssignmentRequest request, CallSettings callSettings = null)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    GetOSPolicyAssignmentRequest request = new GetOSPolicyAssignmentRequest
    {
        OSPolicyAssignmentName = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]"),
    };
    // Make the request
    OSPolicyAssignment response = osConfigZonalServiceClient.GetOSPolicyAssignment(request);
    

### GetOSPolicyAssignment(OSPolicyAssignmentName, CallSettings)
    
    
    public virtual OSPolicyAssignment GetOSPolicyAssignment(OSPolicyAssignmentName name, CallSettings callSettings = null)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)`  
Required. The resource name of OS policy assignment. Format: `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    OSPolicyAssignmentName name = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
    // Make the request
    OSPolicyAssignment response = osConfigZonalServiceClient.GetOSPolicyAssignment(name);
    

### GetOSPolicyAssignment(string, CallSettings)
    
    
    public virtual OSPolicyAssignment GetOSPolicyAssignment(string name, CallSettings callSettings = null)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of OS policy assignment. Format: `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/osPolicyAssignments/[OS_POLICY_ASSIGNMENT]";
    // Make the request
    OSPolicyAssignment response = osConfigZonalServiceClient.GetOSPolicyAssignment(name);
    

### GetOSPolicyAssignmentAsync(GetOSPolicyAssignmentRequest, CallSettings)
    
    
    public virtual Task<OSPolicyAssignment> GetOSPolicyAssignmentAsync(GetOSPolicyAssignmentRequest request, CallSettings callSettings = null)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetOSPolicyAssignmentRequest request = new GetOSPolicyAssignmentRequest
    {
        OSPolicyAssignmentName = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]"),
    };
    // Make the request
    OSPolicyAssignment response = await osConfigZonalServiceClient.GetOSPolicyAssignmentAsync(request);
    

### GetOSPolicyAssignmentAsync(GetOSPolicyAssignmentRequest, CancellationToken)
    
    
    public virtual Task<OSPolicyAssignment> GetOSPolicyAssignmentAsync(GetOSPolicyAssignmentRequest request, CancellationToken cancellationToken)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetOSPolicyAssignmentRequest request = new GetOSPolicyAssignmentRequest
    {
        OSPolicyAssignmentName = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]"),
    };
    // Make the request
    OSPolicyAssignment response = await osConfigZonalServiceClient.GetOSPolicyAssignmentAsync(request);
    

### GetOSPolicyAssignmentAsync(OSPolicyAssignmentName, CallSettings)
    
    
    public virtual Task<OSPolicyAssignment> GetOSPolicyAssignmentAsync(OSPolicyAssignmentName name, CallSettings callSettings = null)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)`  
Required. The resource name of OS policy assignment. Format: `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    OSPolicyAssignmentName name = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
    // Make the request
    OSPolicyAssignment response = await osConfigZonalServiceClient.GetOSPolicyAssignmentAsync(name);
    

### GetOSPolicyAssignmentAsync(OSPolicyAssignmentName, CancellationToken)
    
    
    public virtual Task<OSPolicyAssignment> GetOSPolicyAssignmentAsync(OSPolicyAssignmentName name, CancellationToken cancellationToken)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)`  
Required. The resource name of OS policy assignment. Format: `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    OSPolicyAssignmentName name = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
    // Make the request
    OSPolicyAssignment response = await osConfigZonalServiceClient.GetOSPolicyAssignmentAsync(name);
    

### GetOSPolicyAssignmentAsync(string, CallSettings)
    
    
    public virtual Task<OSPolicyAssignment> GetOSPolicyAssignmentAsync(string name, CallSettings callSettings = null)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of OS policy assignment. Format: `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/osPolicyAssignments/[OS_POLICY_ASSIGNMENT]";
    // Make the request
    OSPolicyAssignment response = await osConfigZonalServiceClient.GetOSPolicyAssignmentAsync(name);
    

### GetOSPolicyAssignmentAsync(string, CancellationToken)
    
    
    public virtual Task<OSPolicyAssignment> GetOSPolicyAssignmentAsync(string name, CancellationToken cancellationToken)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of OS policy assignment. Format: `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/osPolicyAssignments/[OS_POLICY_ASSIGNMENT]";
    // Make the request
    OSPolicyAssignment response = await osConfigZonalServiceClient.GetOSPolicyAssignmentAsync(name);
    

### GetOSPolicyAssignmentReport(GetOSPolicyAssignmentReportRequest, CallSettings)
    
    
    public virtual OSPolicyAssignmentReport GetOSPolicyAssignmentReport(GetOSPolicyAssignmentReportRequest request, CallSettings callSettings = null)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetOSPolicyAssignmentReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    GetOSPolicyAssignmentReportRequest request = new GetOSPolicyAssignmentReportRequest
    {
        OSPolicyAssignmentReportName = OSPolicyAssignmentReportName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]"),
    };
    // Make the request
    OSPolicyAssignmentReport response = osConfigZonalServiceClient.GetOSPolicyAssignmentReport(request);
    

### GetOSPolicyAssignmentReport(OSPolicyAssignmentReportName, CallSettings)
    
    
    public virtual OSPolicyAssignmentReport GetOSPolicyAssignmentReport(OSPolicyAssignmentReportName name, CallSettings callSettings = null)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReportName)`  
Required. API resource name for OS policy assignment report. Format: `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance_id}`, either Compute Engine `instance-id` or `instance-name` can be provided. For `{assignment_id}`, the OSPolicyAssignment id must be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    OSPolicyAssignmentReportName name = OSPolicyAssignmentReportName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]");
    // Make the request
    OSPolicyAssignmentReport response = osConfigZonalServiceClient.GetOSPolicyAssignmentReport(name);
    

### GetOSPolicyAssignmentReport(string, CallSettings)
    
    
    public virtual OSPolicyAssignmentReport GetOSPolicyAssignmentReport(string name, CallSettings callSettings = null)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for OS policy assignment report. Format: `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance_id}`, either Compute Engine `instance-id` or `instance-name` can be provided. For `{assignment_id}`, the OSPolicyAssignment id must be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/osPolicyAssignments/[ASSIGNMENT]/report";
    // Make the request
    OSPolicyAssignmentReport response = osConfigZonalServiceClient.GetOSPolicyAssignmentReport(name);
    

### GetOSPolicyAssignmentReportAsync(GetOSPolicyAssignmentReportRequest, CallSettings)
    
    
    public virtual Task<OSPolicyAssignmentReport> GetOSPolicyAssignmentReportAsync(GetOSPolicyAssignmentReportRequest request, CallSettings callSettings = null)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetOSPolicyAssignmentReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetOSPolicyAssignmentReportRequest request = new GetOSPolicyAssignmentReportRequest
    {
        OSPolicyAssignmentReportName = OSPolicyAssignmentReportName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]"),
    };
    // Make the request
    OSPolicyAssignmentReport response = await osConfigZonalServiceClient.GetOSPolicyAssignmentReportAsync(request);
    

### GetOSPolicyAssignmentReportAsync(GetOSPolicyAssignmentReportRequest, CancellationToken)
    
    
    public virtual Task<OSPolicyAssignmentReport> GetOSPolicyAssignmentReportAsync(GetOSPolicyAssignmentReportRequest request, CancellationToken cancellationToken)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetOSPolicyAssignmentReportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetOSPolicyAssignmentReportRequest request = new GetOSPolicyAssignmentReportRequest
    {
        OSPolicyAssignmentReportName = OSPolicyAssignmentReportName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]"),
    };
    // Make the request
    OSPolicyAssignmentReport response = await osConfigZonalServiceClient.GetOSPolicyAssignmentReportAsync(request);
    

### GetOSPolicyAssignmentReportAsync(OSPolicyAssignmentReportName, CallSettings)
    
    
    public virtual Task<OSPolicyAssignmentReport> GetOSPolicyAssignmentReportAsync(OSPolicyAssignmentReportName name, CallSettings callSettings = null)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReportName)`  
Required. API resource name for OS policy assignment report. Format: `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance_id}`, either Compute Engine `instance-id` or `instance-name` can be provided. For `{assignment_id}`, the OSPolicyAssignment id must be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    OSPolicyAssignmentReportName name = OSPolicyAssignmentReportName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]");
    // Make the request
    OSPolicyAssignmentReport response = await osConfigZonalServiceClient.GetOSPolicyAssignmentReportAsync(name);
    

### GetOSPolicyAssignmentReportAsync(OSPolicyAssignmentReportName, CancellationToken)
    
    
    public virtual Task<OSPolicyAssignmentReport> GetOSPolicyAssignmentReportAsync(OSPolicyAssignmentReportName name, CancellationToken cancellationToken)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReportName)`  
Required. API resource name for OS policy assignment report. Format: `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance_id}`, either Compute Engine `instance-id` or `instance-name` can be provided. For `{assignment_id}`, the OSPolicyAssignment id must be provided.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    OSPolicyAssignmentReportName name = OSPolicyAssignmentReportName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]");
    // Make the request
    OSPolicyAssignmentReport response = await osConfigZonalServiceClient.GetOSPolicyAssignmentReportAsync(name);
    

### GetOSPolicyAssignmentReportAsync(string, CallSettings)
    
    
    public virtual Task<OSPolicyAssignmentReport> GetOSPolicyAssignmentReportAsync(string name, CallSettings callSettings = null)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for OS policy assignment report. Format: `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance_id}`, either Compute Engine `instance-id` or `instance-name` can be provided. For `{assignment_id}`, the OSPolicyAssignment id must be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/osPolicyAssignments/[ASSIGNMENT]/report";
    // Make the request
    OSPolicyAssignmentReport response = await osConfigZonalServiceClient.GetOSPolicyAssignmentReportAsync(name);
    

### GetOSPolicyAssignmentReportAsync(string, CancellationToken)
    
    
    public virtual Task<OSPolicyAssignmentReport> GetOSPolicyAssignmentReportAsync(string name, CancellationToken cancellationToken)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for OS policy assignment report. Format: `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance_id}`, either Compute Engine `instance-id` or `instance-name` can be provided. For `{assignment_id}`, the OSPolicyAssignment id must be provided.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/osPolicyAssignments/[ASSIGNMENT]/report";
    // Make the request
    OSPolicyAssignmentReport response = await osConfigZonalServiceClient.GetOSPolicyAssignmentReportAsync(name);
    

### GetVulnerabilityReport(GetVulnerabilityReportRequest, CallSettings)
    
    
    public virtual VulnerabilityReport GetVulnerabilityReport(GetVulnerabilityReportRequest request, CallSettings callSettings = null)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVulnerabilityReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetVulnerabilityReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    GetVulnerabilityReportRequest request = new GetVulnerabilityReportRequest
    {
        VulnerabilityReportName = VulnerabilityReportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    VulnerabilityReport response = osConfigZonalServiceClient.GetVulnerabilityReport(request);
    

### GetVulnerabilityReport(VulnerabilityReportName, CallSettings)
    
    
    public virtual VulnerabilityReport GetVulnerabilityReport(VulnerabilityReportName name, CallSettings callSettings = null)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[VulnerabilityReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReportName)`  
Required. API resource name for vulnerability resource. Format: `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    VulnerabilityReportName name = VulnerabilityReportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    VulnerabilityReport response = osConfigZonalServiceClient.GetVulnerabilityReport(name);
    

### GetVulnerabilityReport(string, CallSettings)
    
    
    public virtual VulnerabilityReport GetVulnerabilityReport(string name, CallSettings callSettings = null)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for vulnerability resource. Format: `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/vulnerabilityReport";
    // Make the request
    VulnerabilityReport response = osConfigZonalServiceClient.GetVulnerabilityReport(name);
    

### GetVulnerabilityReportAsync(GetVulnerabilityReportRequest, CallSettings)
    
    
    public virtual Task<VulnerabilityReport> GetVulnerabilityReportAsync(GetVulnerabilityReportRequest request, CallSettings callSettings = null)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVulnerabilityReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetVulnerabilityReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetVulnerabilityReportRequest request = new GetVulnerabilityReportRequest
    {
        VulnerabilityReportName = VulnerabilityReportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    VulnerabilityReport response = await osConfigZonalServiceClient.GetVulnerabilityReportAsync(request);
    

### GetVulnerabilityReportAsync(GetVulnerabilityReportRequest, CancellationToken)
    
    
    public virtual Task<VulnerabilityReport> GetVulnerabilityReportAsync(GetVulnerabilityReportRequest request, CancellationToken cancellationToken)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVulnerabilityReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetVulnerabilityReportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetVulnerabilityReportRequest request = new GetVulnerabilityReportRequest
    {
        VulnerabilityReportName = VulnerabilityReportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    VulnerabilityReport response = await osConfigZonalServiceClient.GetVulnerabilityReportAsync(request);
    

### GetVulnerabilityReportAsync(VulnerabilityReportName, CallSettings)
    
    
    public virtual Task<VulnerabilityReport> GetVulnerabilityReportAsync(VulnerabilityReportName name, CallSettings callSettings = null)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[VulnerabilityReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReportName)`  
Required. API resource name for vulnerability resource. Format: `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    VulnerabilityReportName name = VulnerabilityReportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    VulnerabilityReport response = await osConfigZonalServiceClient.GetVulnerabilityReportAsync(name);
    

### GetVulnerabilityReportAsync(VulnerabilityReportName, CancellationToken)
    
    
    public virtual Task<VulnerabilityReport> GetVulnerabilityReportAsync(VulnerabilityReportName name, CancellationToken cancellationToken)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[VulnerabilityReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReportName)`  
Required. API resource name for vulnerability resource. Format: `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    VulnerabilityReportName name = VulnerabilityReportName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    VulnerabilityReport response = await osConfigZonalServiceClient.GetVulnerabilityReportAsync(name);
    

### GetVulnerabilityReportAsync(string, CallSettings)
    
    
    public virtual Task<VulnerabilityReport> GetVulnerabilityReportAsync(string name, CallSettings callSettings = null)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for vulnerability resource. Format: `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/vulnerabilityReport";
    // Make the request
    VulnerabilityReport response = await osConfigZonalServiceClient.GetVulnerabilityReportAsync(name);
    

### GetVulnerabilityReportAsync(string, CancellationToken)
    
    
    public virtual Task<VulnerabilityReport> GetVulnerabilityReportAsync(string name, CancellationToken cancellationToken)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. API resource name for vulnerability resource. Format: `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/vulnerabilityReport";
    // Make the request
    VulnerabilityReport response = await osConfigZonalServiceClient.GetVulnerabilityReportAsync(name);
    

### ListInstanceOSPoliciesCompliances(LocationName, string, int?, CallSettings)
    
    
    [Obsolete]
    public virtual PagedEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> ListInstanceOSPoliciesCompliances(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List OS policies compliance data for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}` For `{project}`, either Compute Engine project-number or project-id can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInstanceOSPoliciesCompliancesResponse)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A pageable sequence of [InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance) resources.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
                // Initialize request argument(s)
                LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
                // Make the request
    #pragma warning disable CS0612
                PagedEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> response = osConfigZonalServiceClient.ListInstanceOSPoliciesCompliances(parent);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
    #pragma warning disable CS0612
                foreach (InstanceOSPoliciesCompliance item in response)
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
    #pragma warning disable CS0612
                foreach (ListInstanceOSPoliciesCompliancesResponse page in response.AsRawResponses())
    #pragma warning restore CS0612
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
    #pragma warning disable CS0612
                    foreach (InstanceOSPoliciesCompliance item in page)
    #pragma warning restore CS0612
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
    #pragma warning disable CS0612
                Page<InstanceOSPoliciesCompliance> singlePage = response.ReadPage(pageSize);
    #pragma warning restore CS0612
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    #pragma warning disable CS0612
                foreach (InstanceOSPoliciesCompliance item in singlePage)
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListInstanceOSPoliciesCompliances(ListInstanceOSPoliciesCompliancesRequest, CallSettings)
    
    
    [Obsolete]
    public virtual PagedEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> ListInstanceOSPoliciesCompliances(ListInstanceOSPoliciesCompliancesRequest request, CallSettings callSettings = null)

List OS policies compliance data for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInstanceOSPoliciesCompliancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInstanceOSPoliciesCompliancesResponse)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A pageable sequence of [InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance) resources.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
                // Initialize request argument(s)
    #pragma warning disable CS0612
                ListInstanceOSPoliciesCompliancesRequest request = new ListInstanceOSPoliciesCompliancesRequest { };
    #pragma warning restore CS0612
                // Make the request
    #pragma warning disable CS0612
                PagedEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> response = osConfigZonalServiceClient.ListInstanceOSPoliciesCompliances(request);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
    #pragma warning disable CS0612
                foreach (InstanceOSPoliciesCompliance item in response)
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
    #pragma warning disable CS0612
                foreach (ListInstanceOSPoliciesCompliancesResponse page in response.AsRawResponses())
    #pragma warning restore CS0612
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
    #pragma warning disable CS0612
                    foreach (InstanceOSPoliciesCompliance item in page)
    #pragma warning restore CS0612
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
    #pragma warning disable CS0612
                Page<InstanceOSPoliciesCompliance> singlePage = response.ReadPage(pageSize);
    #pragma warning restore CS0612
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    #pragma warning disable CS0612
                foreach (InstanceOSPoliciesCompliance item in singlePage)
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListInstanceOSPoliciesCompliances(string, string, int?, CallSettings)
    
    
    [Obsolete]
    public virtual PagedEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> ListInstanceOSPoliciesCompliances(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List OS policies compliance data for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}` For `{project}`, either Compute Engine project-number or project-id can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInstanceOSPoliciesCompliancesResponse)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A pageable sequence of [InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance) resources.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]";
                // Make the request
    #pragma warning disable CS0612
                PagedEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> response = osConfigZonalServiceClient.ListInstanceOSPoliciesCompliances(parent);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
    #pragma warning disable CS0612
                foreach (InstanceOSPoliciesCompliance item in response)
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
    #pragma warning disable CS0612
                foreach (ListInstanceOSPoliciesCompliancesResponse page in response.AsRawResponses())
    #pragma warning restore CS0612
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
    #pragma warning disable CS0612
                    foreach (InstanceOSPoliciesCompliance item in page)
    #pragma warning restore CS0612
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
    #pragma warning disable CS0612
                Page<InstanceOSPoliciesCompliance> singlePage = response.ReadPage(pageSize);
    #pragma warning restore CS0612
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    #pragma warning disable CS0612
                foreach (InstanceOSPoliciesCompliance item in singlePage)
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListInstanceOSPoliciesCompliancesAsync(LocationName, string, int?, CallSettings)
    
    
    [Obsolete]
    public virtual PagedAsyncEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> ListInstanceOSPoliciesCompliancesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List OS policies compliance data for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}` For `{project}`, either Compute Engine project-number or project-id can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInstanceOSPoliciesCompliancesResponse)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A pageable asynchronous sequence of [InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance) resources.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
                // Initialize request argument(s)
                LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
                // Make the request
    #pragma warning disable CS0612
                PagedAsyncEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> response = osConfigZonalServiceClient.ListInstanceOSPoliciesCompliancesAsync(parent);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
    #pragma warning disable CS0612
                await response.ForEachAsync((InstanceOSPoliciesCompliance item) =>
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                });
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
    #pragma warning disable CS0612
                await response.AsRawResponses().ForEachAsync((ListInstanceOSPoliciesCompliancesResponse page) =>
    #pragma warning restore CS0612
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
    #pragma warning disable CS0612
                    foreach (InstanceOSPoliciesCompliance item in page)
    #pragma warning restore CS0612
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                });
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
    #pragma warning disable CS0612
                Page<InstanceOSPoliciesCompliance> singlePage = await response.ReadPageAsync(pageSize);
    #pragma warning restore CS0612
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    #pragma warning disable CS0612
                foreach (InstanceOSPoliciesCompliance item in singlePage)
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListInstanceOSPoliciesCompliancesAsync(ListInstanceOSPoliciesCompliancesRequest, CallSettings)
    
    
    [Obsolete]
    public virtual PagedAsyncEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> ListInstanceOSPoliciesCompliancesAsync(ListInstanceOSPoliciesCompliancesRequest request, CallSettings callSettings = null)

List OS policies compliance data for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInstanceOSPoliciesCompliancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInstanceOSPoliciesCompliancesResponse)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A pageable asynchronous sequence of [InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance) resources.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
                // Initialize request argument(s)
    #pragma warning disable CS0612
                ListInstanceOSPoliciesCompliancesRequest request = new ListInstanceOSPoliciesCompliancesRequest { };
    #pragma warning restore CS0612
                // Make the request
    #pragma warning disable CS0612
                PagedAsyncEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> response = osConfigZonalServiceClient.ListInstanceOSPoliciesCompliancesAsync(request);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
    #pragma warning disable CS0612
                await response.ForEachAsync((InstanceOSPoliciesCompliance item) =>
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                });
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
    #pragma warning disable CS0612
                await response.AsRawResponses().ForEachAsync((ListInstanceOSPoliciesCompliancesResponse page) =>
    #pragma warning restore CS0612
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
    #pragma warning disable CS0612
                    foreach (InstanceOSPoliciesCompliance item in page)
    #pragma warning restore CS0612
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                });
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
    #pragma warning disable CS0612
                Page<InstanceOSPoliciesCompliance> singlePage = await response.ReadPageAsync(pageSize);
    #pragma warning restore CS0612
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    #pragma warning disable CS0612
                foreach (InstanceOSPoliciesCompliance item in singlePage)
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListInstanceOSPoliciesCompliancesAsync(string, string, int?, CallSettings)
    
    
    [Obsolete]
    public virtual PagedAsyncEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> ListInstanceOSPoliciesCompliancesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List OS policies compliance data for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}` For `{project}`, either Compute Engine project-number or project-id can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInstanceOSPoliciesCompliancesResponse)[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance)` | A pageable asynchronous sequence of [InstanceOSPoliciesCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPoliciesCompliance) resources.  
**Example**
    
    
                // Create client
                OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]";
                // Make the request
    #pragma warning disable CS0612
                PagedAsyncEnumerable<ListInstanceOSPoliciesCompliancesResponse, InstanceOSPoliciesCompliance> response = osConfigZonalServiceClient.ListInstanceOSPoliciesCompliancesAsync(parent);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
    #pragma warning disable CS0612
                await response.ForEachAsync((InstanceOSPoliciesCompliance item) =>
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                });
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
    #pragma warning disable CS0612
                await response.AsRawResponses().ForEachAsync((ListInstanceOSPoliciesCompliancesResponse page) =>
    #pragma warning restore CS0612
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
    #pragma warning disable CS0612
                    foreach (InstanceOSPoliciesCompliance item in page)
    #pragma warning restore CS0612
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                });
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
    #pragma warning disable CS0612
                Page<InstanceOSPoliciesCompliance> singlePage = await response.ReadPageAsync(pageSize);
    #pragma warning restore CS0612
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    #pragma warning disable CS0612
                foreach (InstanceOSPoliciesCompliance item in singlePage)
    #pragma warning restore CS0612
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListInventories(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListInventoriesResponse, Inventory> ListInventories(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List inventory data for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceName)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInventoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInventoriesResponse)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A pageable sequence of [Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedEnumerable<ListInventoriesResponse, Inventory> response = osConfigZonalServiceClient.ListInventories(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Inventory item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListInventoriesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Inventory item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Inventory> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Inventory item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInventories(ListInventoriesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListInventoriesResponse, Inventory> ListInventories(ListInventoriesRequest request, CallSettings callSettings = null)

List inventory data for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInventoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInventoriesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInventoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInventoriesResponse)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A pageable sequence of [Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    ListInventoriesRequest request = new ListInventoriesRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        View = InventoryView.Unspecified,
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListInventoriesResponse, Inventory> response = osConfigZonalServiceClient.ListInventories(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Inventory item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListInventoriesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Inventory item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Inventory> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Inventory item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInventories(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListInventoriesResponse, Inventory> ListInventories(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List inventory data for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInventoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInventoriesResponse)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A pageable sequence of [Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedEnumerable<ListInventoriesResponse, Inventory> response = osConfigZonalServiceClient.ListInventories(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Inventory item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListInventoriesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Inventory item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Inventory> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Inventory item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInventoriesAsync(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInventoriesResponse, Inventory> ListInventoriesAsync(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List inventory data for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceName)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInventoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInventoriesResponse)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A pageable asynchronous sequence of [Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedAsyncEnumerable<ListInventoriesResponse, Inventory> response = osConfigZonalServiceClient.ListInventoriesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Inventory item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListInventoriesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Inventory item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Inventory> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Inventory item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInventoriesAsync(ListInventoriesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInventoriesResponse, Inventory> ListInventoriesAsync(ListInventoriesRequest request, CallSettings callSettings = null)

List inventory data for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInventoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInventoriesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInventoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInventoriesResponse)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A pageable asynchronous sequence of [Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListInventoriesRequest request = new ListInventoriesRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        View = InventoryView.Unspecified,
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListInventoriesResponse, Inventory> response = osConfigZonalServiceClient.ListInventoriesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Inventory item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListInventoriesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Inventory item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Inventory> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Inventory item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInventoriesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInventoriesResponse, Inventory> ListInventoriesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List inventory data for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInventoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListInventoriesResponse)[Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory)` | A pageable asynchronous sequence of [Inventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.Inventory) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedAsyncEnumerable<ListInventoriesResponse, Inventory> response = osConfigZonalServiceClient.ListInventoriesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Inventory item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListInventoriesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Inventory item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Inventory> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Inventory item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentReports(InstanceOSPolicyAssignmentName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> ListOSPolicyAssignmentReports(InstanceOSPolicyAssignmentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either `instance-name`, `instance-id`, or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all instances in the project/location. For `{assignment}`, either `assignment-id` or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all OSPolicyAssignments in the project/location. Either {instance} or {assignment} must be `-`. For example: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports` returns all reports for the instance `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports` returns all the reports for the given assignment across all instances. `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports` returns all the reports for all assignments across all instances.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentReportsResponse)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A pageable sequence of [OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    InstanceOSPolicyAssignmentName parent = InstanceOSPolicyAssignmentName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]");
    // Make the request
    PagedEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> response = osConfigZonalServiceClient.ListOSPolicyAssignmentReports(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (OSPolicyAssignmentReport item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListOSPolicyAssignmentReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignmentReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignmentReport> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignmentReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentReports(ListOSPolicyAssignmentReportsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> ListOSPolicyAssignmentReports(ListOSPolicyAssignmentReportsRequest request, CallSettings callSettings = null)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentReportsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentReportsResponse)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A pageable sequence of [OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    ListOSPolicyAssignmentReportsRequest request = new ListOSPolicyAssignmentReportsRequest
    {
        ParentAsInstanceOSPolicyAssignmentName = InstanceOSPolicyAssignmentName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> response = osConfigZonalServiceClient.ListOSPolicyAssignmentReports(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (OSPolicyAssignmentReport item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListOSPolicyAssignmentReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignmentReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignmentReport> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignmentReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentReports(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> ListOSPolicyAssignmentReports(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either `instance-name`, `instance-id`, or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all instances in the project/location. For `{assignment}`, either `assignment-id` or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all OSPolicyAssignments in the project/location. Either {instance} or {assignment} must be `-`. For example: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports` returns all reports for the instance `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports` returns all the reports for the given assignment across all instances. `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports` returns all the reports for all assignments across all instances.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentReportsResponse)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A pageable sequence of [OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/osPolicyAssignments/[ASSIGNMENT]";
    // Make the request
    PagedEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> response = osConfigZonalServiceClient.ListOSPolicyAssignmentReports(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (OSPolicyAssignmentReport item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListOSPolicyAssignmentReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignmentReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignmentReport> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignmentReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentReportsAsync(InstanceOSPolicyAssignmentName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> ListOSPolicyAssignmentReportsAsync(InstanceOSPolicyAssignmentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either `instance-name`, `instance-id`, or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all instances in the project/location. For `{assignment}`, either `assignment-id` or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all OSPolicyAssignments in the project/location. Either {instance} or {assignment} must be `-`. For example: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports` returns all reports for the instance `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports` returns all the reports for the given assignment across all instances. `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports` returns all the reports for all assignments across all instances.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentReportsResponse)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A pageable asynchronous sequence of [OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceOSPolicyAssignmentName parent = InstanceOSPolicyAssignmentName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]");
    // Make the request
    PagedAsyncEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> response = osConfigZonalServiceClient.ListOSPolicyAssignmentReportsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((OSPolicyAssignmentReport item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListOSPolicyAssignmentReportsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignmentReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignmentReport> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignmentReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentReportsAsync(ListOSPolicyAssignmentReportsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> ListOSPolicyAssignmentReportsAsync(ListOSPolicyAssignmentReportsRequest request, CallSettings callSettings = null)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentReportsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentReportsResponse)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A pageable asynchronous sequence of [OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListOSPolicyAssignmentReportsRequest request = new ListOSPolicyAssignmentReportsRequest
    {
        ParentAsInstanceOSPolicyAssignmentName = InstanceOSPolicyAssignmentName.FromProjectLocationInstanceAssignment("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> response = osConfigZonalServiceClient.ListOSPolicyAssignmentReportsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((OSPolicyAssignmentReport item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListOSPolicyAssignmentReportsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignmentReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignmentReport> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignmentReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentReportsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> ListOSPolicyAssignmentReportsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either `instance-name`, `instance-id`, or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all instances in the project/location. For `{assignment}`, either `assignment-id` or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all OSPolicyAssignments in the project/location. Either {instance} or {assignment} must be `-`. For example: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports` returns all reports for the instance `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports` returns all the reports for the given assignment across all instances. `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports` returns all the reports for all assignments across all instances.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentReportsResponse)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)` | A pageable asynchronous sequence of [OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/osPolicyAssignments/[ASSIGNMENT]";
    // Make the request
    PagedAsyncEnumerable<ListOSPolicyAssignmentReportsResponse, OSPolicyAssignmentReport> response = osConfigZonalServiceClient.ListOSPolicyAssignmentReportsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((OSPolicyAssignmentReport item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListOSPolicyAssignmentReportsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignmentReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignmentReport> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignmentReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentRevisions(ListOSPolicyAssignmentRevisionsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> ListOSPolicyAssignmentRevisions(ListOSPolicyAssignmentRevisionsRequest request, CallSettings callSettings = null)

List the OS policy assignment revisions for a given OS policy assignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentRevisionsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    ListOSPolicyAssignmentRevisionsRequest request = new ListOSPolicyAssignmentRevisionsRequest
    {
        OSPolicyAssignmentName = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]"),
    };
    // Make the request
    PagedEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignmentRevisions(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (OSPolicyAssignment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListOSPolicyAssignmentRevisionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentRevisions(OSPolicyAssignmentName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> ListOSPolicyAssignmentRevisions(OSPolicyAssignmentName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List the OS policy assignment revisions for a given OS policy assignment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)`  
Required. The name of the OS policy assignment to list revisions for.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentRevisionsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    OSPolicyAssignmentName name = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
    // Make the request
    PagedEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignmentRevisions(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (OSPolicyAssignment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListOSPolicyAssignmentRevisionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentRevisions(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> ListOSPolicyAssignmentRevisions(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List the OS policy assignment revisions for a given OS policy assignment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the OS policy assignment to list revisions for.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentRevisionsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/osPolicyAssignments/[OS_POLICY_ASSIGNMENT]";
    // Make the request
    PagedEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignmentRevisions(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (OSPolicyAssignment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListOSPolicyAssignmentRevisionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentRevisionsAsync(ListOSPolicyAssignmentRevisionsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> ListOSPolicyAssignmentRevisionsAsync(ListOSPolicyAssignmentRevisionsRequest request, CallSettings callSettings = null)

List the OS policy assignment revisions for a given OS policy assignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentRevisionsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable asynchronous sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListOSPolicyAssignmentRevisionsRequest request = new ListOSPolicyAssignmentRevisionsRequest
    {
        OSPolicyAssignmentName = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((OSPolicyAssignment item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListOSPolicyAssignmentRevisionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentRevisionsAsync(OSPolicyAssignmentName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> ListOSPolicyAssignmentRevisionsAsync(OSPolicyAssignmentName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List the OS policy assignment revisions for a given OS policy assignment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)`  
Required. The name of the OS policy assignment to list revisions for.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentRevisionsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable asynchronous sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    OSPolicyAssignmentName name = OSPolicyAssignmentName.FromProjectLocationOsPolicyAssignment("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
    // Make the request
    PagedAsyncEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((OSPolicyAssignment item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListOSPolicyAssignmentRevisionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentRevisionsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> ListOSPolicyAssignmentRevisionsAsync(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List the OS policy assignment revisions for a given OS policy assignment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the OS policy assignment to list revisions for.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentRevisionsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable asynchronous sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/osPolicyAssignments/[OS_POLICY_ASSIGNMENT]";
    // Make the request
    PagedAsyncEnumerable<ListOSPolicyAssignmentRevisionsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((OSPolicyAssignment item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListOSPolicyAssignmentRevisionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignments(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> ListOSPolicyAssignments(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignments(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (OSPolicyAssignment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListOSPolicyAssignmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignments(ListOSPolicyAssignmentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> ListOSPolicyAssignments(ListOSPolicyAssignmentsRequest request, CallSettings callSettings = null)

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    ListOSPolicyAssignmentsRequest request = new ListOSPolicyAssignmentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignments(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (OSPolicyAssignment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListOSPolicyAssignmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignments(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> ListOSPolicyAssignments(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignments(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (OSPolicyAssignment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListOSPolicyAssignmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> ListOSPolicyAssignmentsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable asynchronous sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignmentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((OSPolicyAssignment item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListOSPolicyAssignmentsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentsAsync(ListOSPolicyAssignmentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> ListOSPolicyAssignmentsAsync(ListOSPolicyAssignmentsRequest request, CallSettings callSettings = null)

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable asynchronous sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListOSPolicyAssignmentsRequest request = new ListOSPolicyAssignmentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignmentsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((OSPolicyAssignment item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListOSPolicyAssignmentsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListOSPolicyAssignmentsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> ListOSPolicyAssignmentsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListOSPolicyAssignmentsResponse)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)` | A pageable asynchronous sequence of [OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListOSPolicyAssignmentsResponse, OSPolicyAssignment> response = osConfigZonalServiceClient.ListOSPolicyAssignmentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((OSPolicyAssignment item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListOSPolicyAssignmentsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (OSPolicyAssignment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<OSPolicyAssignment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (OSPolicyAssignment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVulnerabilityReports(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> ListVulnerabilityReports(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List vulnerability reports for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceName)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListVulnerabilityReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListVulnerabilityReportsResponse)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A pageable sequence of [VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> response = osConfigZonalServiceClient.ListVulnerabilityReports(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (VulnerabilityReport item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListVulnerabilityReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (VulnerabilityReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<VulnerabilityReport> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (VulnerabilityReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVulnerabilityReports(ListVulnerabilityReportsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> ListVulnerabilityReports(ListVulnerabilityReportsRequest request, CallSettings callSettings = null)

List vulnerability reports for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVulnerabilityReportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListVulnerabilityReportsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListVulnerabilityReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListVulnerabilityReportsResponse)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A pageable sequence of [VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    ListVulnerabilityReportsRequest request = new ListVulnerabilityReportsRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> response = osConfigZonalServiceClient.ListVulnerabilityReports(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (VulnerabilityReport item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListVulnerabilityReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (VulnerabilityReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<VulnerabilityReport> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (VulnerabilityReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVulnerabilityReports(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> ListVulnerabilityReports(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List vulnerability reports for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListVulnerabilityReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListVulnerabilityReportsResponse)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A pageable sequence of [VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> response = osConfigZonalServiceClient.ListVulnerabilityReports(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (VulnerabilityReport item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListVulnerabilityReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (VulnerabilityReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<VulnerabilityReport> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (VulnerabilityReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVulnerabilityReportsAsync(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> ListVulnerabilityReportsAsync(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List vulnerability reports for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceName)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListVulnerabilityReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListVulnerabilityReportsResponse)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A pageable asynchronous sequence of [VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedAsyncEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> response = osConfigZonalServiceClient.ListVulnerabilityReportsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((VulnerabilityReport item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListVulnerabilityReportsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (VulnerabilityReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<VulnerabilityReport> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (VulnerabilityReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVulnerabilityReportsAsync(ListVulnerabilityReportsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> ListVulnerabilityReportsAsync(ListVulnerabilityReportsRequest request, CallSettings callSettings = null)

List vulnerability reports for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVulnerabilityReportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListVulnerabilityReportsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListVulnerabilityReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListVulnerabilityReportsResponse)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A pageable asynchronous sequence of [VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListVulnerabilityReportsRequest request = new ListVulnerabilityReportsRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> response = osConfigZonalServiceClient.ListVulnerabilityReportsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((VulnerabilityReport item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListVulnerabilityReportsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (VulnerabilityReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<VulnerabilityReport> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (VulnerabilityReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVulnerabilityReportsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> ListVulnerabilityReportsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List vulnerability reports for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListVulnerabilityReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.ListVulnerabilityReportsResponse)[VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport)` | A pageable asynchronous sequence of [VulnerabilityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.VulnerabilityReport) resources.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedAsyncEnumerable<ListVulnerabilityReportsResponse, VulnerabilityReport> response = osConfigZonalServiceClient.ListVulnerabilityReportsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((VulnerabilityReport item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListVulnerabilityReportsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (VulnerabilityReport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<VulnerabilityReport> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (VulnerabilityReport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateOSPolicyAssignment(string, CallSettings)
    
    
    public virtual Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> PollOnceCreateOSPolicyAssignment(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateOSPolicyAssignment`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateOSPolicyAssignmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> PollOnceCreateOSPolicyAssignmentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateOSPolicyAssignment`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteOSPolicyAssignment(string, CallSettings)
    
    
    public virtual Operation<Empty, OSPolicyAssignmentOperationMetadata> PollOnceDeleteOSPolicyAssignment(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteOSPolicyAssignment`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteOSPolicyAssignmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OSPolicyAssignmentOperationMetadata>> PollOnceDeleteOSPolicyAssignmentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteOSPolicyAssignment`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateOSPolicyAssignment(string, CallSettings)
    
    
    public virtual Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> PollOnceUpdateOSPolicyAssignment(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateOSPolicyAssignment`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateOSPolicyAssignmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> PollOnceUpdateOSPolicyAssignmentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateOSPolicyAssignment`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient#Google_Cloud_OsConfig_V1Alpha_OsConfigZonalServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient#Google_Cloud_OsConfig_V1Alpha_OsConfigZonalServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient#Google_Cloud_OsConfig_V1Alpha_OsConfigZonalServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OsConfigZonalServiceClient#Google_Cloud_OsConfig_V1Alpha_OsConfigZonalServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateOSPolicyAssignment(OSPolicyAssignment, FieldMask, CallSettings)
    
    
    public virtual Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> UpdateOSPolicyAssignment(OSPolicyAssignment osPolicyAssignment, FieldMask updateMask, CallSettings callSettings = null)

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)`  
Required. The updated OS policy assignment.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask that controls which fields of the assignment should be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    OSPolicyAssignment osPolicyAssignment = new OSPolicyAssignment();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = osConfigZonalServiceClient.UpdateOSPolicyAssignment(osPolicyAssignment, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = osConfigZonalServiceClient.PollOnceUpdateOSPolicyAssignment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateOSPolicyAssignment(UpdateOSPolicyAssignmentRequest, CallSettings)
    
    
    public virtual Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> UpdateOSPolicyAssignment(UpdateOSPolicyAssignmentRequest request, CallSettings callSettings = null)

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.UpdateOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = OsConfigZonalServiceClient.Create();
    // Initialize request argument(s)
    UpdateOSPolicyAssignmentRequest request = new UpdateOSPolicyAssignmentRequest
    {
        OsPolicyAssignment = new OSPolicyAssignment(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = osConfigZonalServiceClient.UpdateOSPolicyAssignment(request);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = osConfigZonalServiceClient.PollOnceUpdateOSPolicyAssignment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateOSPolicyAssignmentAsync(OSPolicyAssignment, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> UpdateOSPolicyAssignmentAsync(OSPolicyAssignment osPolicyAssignment, FieldMask updateMask, CallSettings callSettings = null)

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)`  
Required. The updated OS policy assignment.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask that controls which fields of the assignment should be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    OSPolicyAssignment osPolicyAssignment = new OSPolicyAssignment();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.UpdateOSPolicyAssignmentAsync(osPolicyAssignment, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceUpdateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateOSPolicyAssignmentAsync(OSPolicyAssignment, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> UpdateOSPolicyAssignmentAsync(OSPolicyAssignment osPolicyAssignment, FieldMask updateMask, CancellationToken cancellationToken)

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)`  
Required. The updated OS policy assignment.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask that controls which fields of the assignment should be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    OSPolicyAssignment osPolicyAssignment = new OSPolicyAssignment();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.UpdateOSPolicyAssignmentAsync(osPolicyAssignment, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceUpdateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateOSPolicyAssignmentAsync(UpdateOSPolicyAssignmentRequest, CallSettings)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> UpdateOSPolicyAssignmentAsync(UpdateOSPolicyAssignmentRequest request, CallSettings callSettings = null)

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.UpdateOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateOSPolicyAssignmentRequest request = new UpdateOSPolicyAssignmentRequest
    {
        OsPolicyAssignment = new OSPolicyAssignment(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.UpdateOSPolicyAssignmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceUpdateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateOSPolicyAssignmentAsync(UpdateOSPolicyAssignmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata>> UpdateOSPolicyAssignmentAsync(UpdateOSPolicyAssignmentRequest request, CancellationToken cancellationToken)

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.UpdateOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[OSPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignment)[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    OsConfigZonalServiceClient osConfigZonalServiceClient = await OsConfigZonalServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateOSPolicyAssignmentRequest request = new UpdateOSPolicyAssignmentRequest
    {
        OsPolicyAssignment = new OSPolicyAssignment(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> response = await osConfigZonalServiceClient.UpdateOSPolicyAssignmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    OSPolicyAssignment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> retrievedResponse = await osConfigZonalServiceClient.PollOnceUpdateOSPolicyAssignmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        OSPolicyAssignment retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
