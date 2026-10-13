---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient
title: Google Cloud Key Management Service v1 API - Class AutokeyClient (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:55.839979+00:00
---

# Google Cloud Key Management Service v1 API - Class AutokeyClient (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class AutokeyClient (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public abstract class AutokeyClient

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class AutokeyClient.

Autokey client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutokeyClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AutokeyClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClientImpl)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Remarks

Provides interfaces for using [Cloud KMS Autokey](https://cloud.google.com/kms/help/autokey) to provision new [CryptoKeys][google.cloud.kms.v1.CryptoKey], ready for Customer Managed Encryption Key (CMEK) use, on-demand. To support certain client tooling, this feature is modeled around a [KeyHandle][google.cloud.kms.v1.KeyHandle] resource: creating a [KeyHandle][google.cloud.kms.v1.KeyHandle] in a resource project and given location triggers Cloud KMS Autokey to provision a [CryptoKey][google.cloud.kms.v1.CryptoKey] in the configured key project and the same location.

Prior to use in a given resource project, [UpdateAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig] should have been called on an ancestor folder, setting the key project where Cloud KMS Autokey should create new [CryptoKeys][google.cloud.kms.v1.CryptoKey]. See documentation for additional prerequisites. To check what key project, if any, is currently configured on a resource project's ancestor folder, see [ShowEffectiveAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig].

## Properties 

### CreateKeyHandleOperationsClient
    
    
    public virtual OperationsClient CreateKeyHandleOperationsClient { get; }

The long-running operations client for `CreateKeyHandle`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Autokey service, which is a host of "cloudkms.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Autokey scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Autokey scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/cloudkms>



### GrpcClient
    
    
    public virtual Autokey.AutokeyClient GrpcClient { get; }

The underlying gRPC Autokey client

**Property Value**  
---  
**Type** | **Description**  
`[Autokey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Autokey)[AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Autokey.AutokeyClient)` |   
  
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
    
    
    public static AutokeyClient Create()

Synchronously creates a [AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AutokeyClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient)` | The created [AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AutokeyClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AutokeyClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient)` | The task representing the created [AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient).  
  
### CreateKeyHandle(LocationName, KeyHandle, string, CallSettings)
    
    
    public virtual Operation<KeyHandle, CreateKeyHandleMetadata> CreateKeyHandle(LocationName parent, KeyHandle keyHandle, string keyHandleId, CallSettings callSettings = null)

Creates a new [KeyHandle][google.cloud.kms.v1.KeyHandle], triggering the provisioning of a new [CryptoKey][google.cloud.kms.v1.CryptoKey] for CMEK use with the given resource type in the configured key project and the same location. [GetOperation][google.longrunning.Operations.GetOperation] should be used to resolve the resulting long-running operation and get the resulting [KeyHandle][google.cloud.kms.v1.KeyHandle] and [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Name of the resource project and location to create the [KeyHandle][google.cloud.kms.v1.KeyHandle] in, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`keyHandle` | `[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)`  
Required. [KeyHandle][google.cloud.kms.v1.KeyHandle] to create.  
`keyHandleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the [KeyHandle][google.cloud.kms.v1.KeyHandle]. Must be unique to the resource project and location. If not provided by the caller, a new UUID is used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = AutokeyClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    KeyHandle keyHandle = new KeyHandle();
    string keyHandleId = "";
    // Make the request
    Operation<KeyHandle, CreateKeyHandleMetadata> response = autokeyClient.CreateKeyHandle(parent, keyHandle, keyHandleId);
    
    // Poll until the returned long-running operation is complete
    Operation<KeyHandle, CreateKeyHandleMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    KeyHandle result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<KeyHandle, CreateKeyHandleMetadata> retrievedResponse = autokeyClient.PollOnceCreateKeyHandle(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        KeyHandle retrievedResult = retrievedResponse.Result;
    }
    

### CreateKeyHandle(CreateKeyHandleRequest, CallSettings)
    
    
    public virtual Operation<KeyHandle, CreateKeyHandleMetadata> CreateKeyHandle(CreateKeyHandleRequest request, CallSettings callSettings = null)

Creates a new [KeyHandle][google.cloud.kms.v1.KeyHandle], triggering the provisioning of a new [CryptoKey][google.cloud.kms.v1.CryptoKey] for CMEK use with the given resource type in the configured key project and the same location. [GetOperation][google.longrunning.Operations.GetOperation] should be used to resolve the resulting long-running operation and get the resulting [KeyHandle][google.cloud.kms.v1.KeyHandle] and [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateKeyHandleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = AutokeyClient.Create();
    // Initialize request argument(s)
    CreateKeyHandleRequest request = new CreateKeyHandleRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        KeyHandleId = "",
        KeyHandle = new KeyHandle(),
    };
    // Make the request
    Operation<KeyHandle, CreateKeyHandleMetadata> response = autokeyClient.CreateKeyHandle(request);
    
    // Poll until the returned long-running operation is complete
    Operation<KeyHandle, CreateKeyHandleMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    KeyHandle result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<KeyHandle, CreateKeyHandleMetadata> retrievedResponse = autokeyClient.PollOnceCreateKeyHandle(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        KeyHandle retrievedResult = retrievedResponse.Result;
    }
    

### CreateKeyHandle(string, KeyHandle, string, CallSettings)
    
    
    public virtual Operation<KeyHandle, CreateKeyHandleMetadata> CreateKeyHandle(string parent, KeyHandle keyHandle, string keyHandleId, CallSettings callSettings = null)

Creates a new [KeyHandle][google.cloud.kms.v1.KeyHandle], triggering the provisioning of a new [CryptoKey][google.cloud.kms.v1.CryptoKey] for CMEK use with the given resource type in the configured key project and the same location. [GetOperation][google.longrunning.Operations.GetOperation] should be used to resolve the resulting long-running operation and get the resulting [KeyHandle][google.cloud.kms.v1.KeyHandle] and [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource project and location to create the [KeyHandle][google.cloud.kms.v1.KeyHandle] in, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`keyHandle` | `[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)`  
Required. [KeyHandle][google.cloud.kms.v1.KeyHandle] to create.  
`keyHandleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the [KeyHandle][google.cloud.kms.v1.KeyHandle]. Must be unique to the resource project and location. If not provided by the caller, a new UUID is used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = AutokeyClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    KeyHandle keyHandle = new KeyHandle();
    string keyHandleId = "";
    // Make the request
    Operation<KeyHandle, CreateKeyHandleMetadata> response = autokeyClient.CreateKeyHandle(parent, keyHandle, keyHandleId);
    
    // Poll until the returned long-running operation is complete
    Operation<KeyHandle, CreateKeyHandleMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    KeyHandle result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<KeyHandle, CreateKeyHandleMetadata> retrievedResponse = autokeyClient.PollOnceCreateKeyHandle(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        KeyHandle retrievedResult = retrievedResponse.Result;
    }
    

### CreateKeyHandleAsync(LocationName, KeyHandle, string, CallSettings)
    
    
    public virtual Task<Operation<KeyHandle, CreateKeyHandleMetadata>> CreateKeyHandleAsync(LocationName parent, KeyHandle keyHandle, string keyHandleId, CallSettings callSettings = null)

Creates a new [KeyHandle][google.cloud.kms.v1.KeyHandle], triggering the provisioning of a new [CryptoKey][google.cloud.kms.v1.CryptoKey] for CMEK use with the given resource type in the configured key project and the same location. [GetOperation][google.longrunning.Operations.GetOperation] should be used to resolve the resulting long-running operation and get the resulting [KeyHandle][google.cloud.kms.v1.KeyHandle] and [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Name of the resource project and location to create the [KeyHandle][google.cloud.kms.v1.KeyHandle] in, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`keyHandle` | `[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)`  
Required. [KeyHandle][google.cloud.kms.v1.KeyHandle] to create.  
`keyHandleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the [KeyHandle][google.cloud.kms.v1.KeyHandle]. Must be unique to the resource project and location. If not provided by the caller, a new UUID is used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    KeyHandle keyHandle = new KeyHandle();
    string keyHandleId = "";
    // Make the request
    Operation<KeyHandle, CreateKeyHandleMetadata> response = await autokeyClient.CreateKeyHandleAsync(parent, keyHandle, keyHandleId);
    
    // Poll until the returned long-running operation is complete
    Operation<KeyHandle, CreateKeyHandleMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    KeyHandle result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<KeyHandle, CreateKeyHandleMetadata> retrievedResponse = await autokeyClient.PollOnceCreateKeyHandleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        KeyHandle retrievedResult = retrievedResponse.Result;
    }
    

### CreateKeyHandleAsync(LocationName, KeyHandle, string, CancellationToken)
    
    
    public virtual Task<Operation<KeyHandle, CreateKeyHandleMetadata>> CreateKeyHandleAsync(LocationName parent, KeyHandle keyHandle, string keyHandleId, CancellationToken cancellationToken)

Creates a new [KeyHandle][google.cloud.kms.v1.KeyHandle], triggering the provisioning of a new [CryptoKey][google.cloud.kms.v1.CryptoKey] for CMEK use with the given resource type in the configured key project and the same location. [GetOperation][google.longrunning.Operations.GetOperation] should be used to resolve the resulting long-running operation and get the resulting [KeyHandle][google.cloud.kms.v1.KeyHandle] and [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Name of the resource project and location to create the [KeyHandle][google.cloud.kms.v1.KeyHandle] in, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`keyHandle` | `[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)`  
Required. [KeyHandle][google.cloud.kms.v1.KeyHandle] to create.  
`keyHandleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the [KeyHandle][google.cloud.kms.v1.KeyHandle]. Must be unique to the resource project and location. If not provided by the caller, a new UUID is used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    KeyHandle keyHandle = new KeyHandle();
    string keyHandleId = "";
    // Make the request
    Operation<KeyHandle, CreateKeyHandleMetadata> response = await autokeyClient.CreateKeyHandleAsync(parent, keyHandle, keyHandleId);
    
    // Poll until the returned long-running operation is complete
    Operation<KeyHandle, CreateKeyHandleMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    KeyHandle result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<KeyHandle, CreateKeyHandleMetadata> retrievedResponse = await autokeyClient.PollOnceCreateKeyHandleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        KeyHandle retrievedResult = retrievedResponse.Result;
    }
    

### CreateKeyHandleAsync(CreateKeyHandleRequest, CallSettings)
    
    
    public virtual Task<Operation<KeyHandle, CreateKeyHandleMetadata>> CreateKeyHandleAsync(CreateKeyHandleRequest request, CallSettings callSettings = null)

Creates a new [KeyHandle][google.cloud.kms.v1.KeyHandle], triggering the provisioning of a new [CryptoKey][google.cloud.kms.v1.CryptoKey] for CMEK use with the given resource type in the configured key project and the same location. [GetOperation][google.longrunning.Operations.GetOperation] should be used to resolve the resulting long-running operation and get the resulting [KeyHandle][google.cloud.kms.v1.KeyHandle] and [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateKeyHandleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    CreateKeyHandleRequest request = new CreateKeyHandleRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        KeyHandleId = "",
        KeyHandle = new KeyHandle(),
    };
    // Make the request
    Operation<KeyHandle, CreateKeyHandleMetadata> response = await autokeyClient.CreateKeyHandleAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<KeyHandle, CreateKeyHandleMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    KeyHandle result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<KeyHandle, CreateKeyHandleMetadata> retrievedResponse = await autokeyClient.PollOnceCreateKeyHandleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        KeyHandle retrievedResult = retrievedResponse.Result;
    }
    

### CreateKeyHandleAsync(CreateKeyHandleRequest, CancellationToken)
    
    
    public virtual Task<Operation<KeyHandle, CreateKeyHandleMetadata>> CreateKeyHandleAsync(CreateKeyHandleRequest request, CancellationToken cancellationToken)

Creates a new [KeyHandle][google.cloud.kms.v1.KeyHandle], triggering the provisioning of a new [CryptoKey][google.cloud.kms.v1.CryptoKey] for CMEK use with the given resource type in the configured key project and the same location. [GetOperation][google.longrunning.Operations.GetOperation] should be used to resolve the resulting long-running operation and get the resulting [KeyHandle][google.cloud.kms.v1.KeyHandle] and [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateKeyHandleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    CreateKeyHandleRequest request = new CreateKeyHandleRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        KeyHandleId = "",
        KeyHandle = new KeyHandle(),
    };
    // Make the request
    Operation<KeyHandle, CreateKeyHandleMetadata> response = await autokeyClient.CreateKeyHandleAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<KeyHandle, CreateKeyHandleMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    KeyHandle result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<KeyHandle, CreateKeyHandleMetadata> retrievedResponse = await autokeyClient.PollOnceCreateKeyHandleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        KeyHandle retrievedResult = retrievedResponse.Result;
    }
    

### CreateKeyHandleAsync(string, KeyHandle, string, CallSettings)
    
    
    public virtual Task<Operation<KeyHandle, CreateKeyHandleMetadata>> CreateKeyHandleAsync(string parent, KeyHandle keyHandle, string keyHandleId, CallSettings callSettings = null)

Creates a new [KeyHandle][google.cloud.kms.v1.KeyHandle], triggering the provisioning of a new [CryptoKey][google.cloud.kms.v1.CryptoKey] for CMEK use with the given resource type in the configured key project and the same location. [GetOperation][google.longrunning.Operations.GetOperation] should be used to resolve the resulting long-running operation and get the resulting [KeyHandle][google.cloud.kms.v1.KeyHandle] and [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource project and location to create the [KeyHandle][google.cloud.kms.v1.KeyHandle] in, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`keyHandle` | `[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)`  
Required. [KeyHandle][google.cloud.kms.v1.KeyHandle] to create.  
`keyHandleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the [KeyHandle][google.cloud.kms.v1.KeyHandle]. Must be unique to the resource project and location. If not provided by the caller, a new UUID is used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    KeyHandle keyHandle = new KeyHandle();
    string keyHandleId = "";
    // Make the request
    Operation<KeyHandle, CreateKeyHandleMetadata> response = await autokeyClient.CreateKeyHandleAsync(parent, keyHandle, keyHandleId);
    
    // Poll until the returned long-running operation is complete
    Operation<KeyHandle, CreateKeyHandleMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    KeyHandle result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<KeyHandle, CreateKeyHandleMetadata> retrievedResponse = await autokeyClient.PollOnceCreateKeyHandleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        KeyHandle retrievedResult = retrievedResponse.Result;
    }
    

### CreateKeyHandleAsync(string, KeyHandle, string, CancellationToken)
    
    
    public virtual Task<Operation<KeyHandle, CreateKeyHandleMetadata>> CreateKeyHandleAsync(string parent, KeyHandle keyHandle, string keyHandleId, CancellationToken cancellationToken)

Creates a new [KeyHandle][google.cloud.kms.v1.KeyHandle], triggering the provisioning of a new [CryptoKey][google.cloud.kms.v1.CryptoKey] for CMEK use with the given resource type in the configured key project and the same location. [GetOperation][google.longrunning.Operations.GetOperation] should be used to resolve the resulting long-running operation and get the resulting [KeyHandle][google.cloud.kms.v1.KeyHandle] and [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource project and location to create the [KeyHandle][google.cloud.kms.v1.KeyHandle] in, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`keyHandle` | `[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)`  
Required. [KeyHandle][google.cloud.kms.v1.KeyHandle] to create.  
`keyHandleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the [KeyHandle][google.cloud.kms.v1.KeyHandle]. Must be unique to the resource project and location. If not provided by the caller, a new UUID is used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    KeyHandle keyHandle = new KeyHandle();
    string keyHandleId = "";
    // Make the request
    Operation<KeyHandle, CreateKeyHandleMetadata> response = await autokeyClient.CreateKeyHandleAsync(parent, keyHandle, keyHandleId);
    
    // Poll until the returned long-running operation is complete
    Operation<KeyHandle, CreateKeyHandleMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    KeyHandle result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<KeyHandle, CreateKeyHandleMetadata> retrievedResponse = await autokeyClient.PollOnceCreateKeyHandleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        KeyHandle retrievedResult = retrievedResponse.Result;
    }
    

### GetKeyHandle(GetKeyHandleRequest, CallSettings)
    
    
    public virtual KeyHandle GetKeyHandle(GetKeyHandleRequest request, CallSettings callSettings = null)

Returns the [KeyHandle][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetKeyHandleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetKeyHandleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = AutokeyClient.Create();
    // Initialize request argument(s)
    GetKeyHandleRequest request = new GetKeyHandleRequest
    {
        KeyHandleName = KeyHandleName.FromProjectLocationKeyHandle("[PROJECT]", "[LOCATION]", "[KEY_HANDLE]"),
    };
    // Make the request
    KeyHandle response = autokeyClient.GetKeyHandle(request);
    

### GetKeyHandle(KeyHandleName, CallSettings)
    
    
    public virtual KeyHandle GetKeyHandle(KeyHandleName name, CallSettings callSettings = null)

Returns the [KeyHandle][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[KeyHandleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandleName)`  
Required. Name of the [KeyHandle][google.cloud.kms.v1.KeyHandle] resource, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}/keyHandles/{KEY_HANDLE_ID}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = AutokeyClient.Create();
    // Initialize request argument(s)
    KeyHandleName name = KeyHandleName.FromProjectLocationKeyHandle("[PROJECT]", "[LOCATION]", "[KEY_HANDLE]");
    // Make the request
    KeyHandle response = autokeyClient.GetKeyHandle(name);
    

### GetKeyHandle(string, CallSettings)
    
    
    public virtual KeyHandle GetKeyHandle(string name, CallSettings callSettings = null)

Returns the [KeyHandle][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the [KeyHandle][google.cloud.kms.v1.KeyHandle] resource, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}/keyHandles/{KEY_HANDLE_ID}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | The RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = AutokeyClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/keyHandles/[KEY_HANDLE]";
    // Make the request
    KeyHandle response = autokeyClient.GetKeyHandle(name);
    

### GetKeyHandleAsync(GetKeyHandleRequest, CallSettings)
    
    
    public virtual Task<KeyHandle> GetKeyHandleAsync(GetKeyHandleRequest request, CallSettings callSettings = null)

Returns the [KeyHandle][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetKeyHandleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetKeyHandleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    GetKeyHandleRequest request = new GetKeyHandleRequest
    {
        KeyHandleName = KeyHandleName.FromProjectLocationKeyHandle("[PROJECT]", "[LOCATION]", "[KEY_HANDLE]"),
    };
    // Make the request
    KeyHandle response = await autokeyClient.GetKeyHandleAsync(request);
    

### GetKeyHandleAsync(GetKeyHandleRequest, CancellationToken)
    
    
    public virtual Task<KeyHandle> GetKeyHandleAsync(GetKeyHandleRequest request, CancellationToken cancellationToken)

Returns the [KeyHandle][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetKeyHandleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetKeyHandleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    GetKeyHandleRequest request = new GetKeyHandleRequest
    {
        KeyHandleName = KeyHandleName.FromProjectLocationKeyHandle("[PROJECT]", "[LOCATION]", "[KEY_HANDLE]"),
    };
    // Make the request
    KeyHandle response = await autokeyClient.GetKeyHandleAsync(request);
    

### GetKeyHandleAsync(KeyHandleName, CallSettings)
    
    
    public virtual Task<KeyHandle> GetKeyHandleAsync(KeyHandleName name, CallSettings callSettings = null)

Returns the [KeyHandle][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[KeyHandleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandleName)`  
Required. Name of the [KeyHandle][google.cloud.kms.v1.KeyHandle] resource, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}/keyHandles/{KEY_HANDLE_ID}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    KeyHandleName name = KeyHandleName.FromProjectLocationKeyHandle("[PROJECT]", "[LOCATION]", "[KEY_HANDLE]");
    // Make the request
    KeyHandle response = await autokeyClient.GetKeyHandleAsync(name);
    

### GetKeyHandleAsync(KeyHandleName, CancellationToken)
    
    
    public virtual Task<KeyHandle> GetKeyHandleAsync(KeyHandleName name, CancellationToken cancellationToken)

Returns the [KeyHandle][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[KeyHandleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandleName)`  
Required. Name of the [KeyHandle][google.cloud.kms.v1.KeyHandle] resource, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}/keyHandles/{KEY_HANDLE_ID}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    KeyHandleName name = KeyHandleName.FromProjectLocationKeyHandle("[PROJECT]", "[LOCATION]", "[KEY_HANDLE]");
    // Make the request
    KeyHandle response = await autokeyClient.GetKeyHandleAsync(name);
    

### GetKeyHandleAsync(string, CallSettings)
    
    
    public virtual Task<KeyHandle> GetKeyHandleAsync(string name, CallSettings callSettings = null)

Returns the [KeyHandle][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the [KeyHandle][google.cloud.kms.v1.KeyHandle] resource, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}/keyHandles/{KEY_HANDLE_ID}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/keyHandles/[KEY_HANDLE]";
    // Make the request
    KeyHandle response = await autokeyClient.GetKeyHandleAsync(name);
    

### GetKeyHandleAsync(string, CancellationToken)
    
    
    public virtual Task<KeyHandle> GetKeyHandleAsync(string name, CancellationToken cancellationToken)

Returns the [KeyHandle][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the [KeyHandle][google.cloud.kms.v1.KeyHandle] resource, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}/keyHandles/{KEY_HANDLE_ID}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/keyHandles/[KEY_HANDLE]";
    // Make the request
    KeyHandle response = await autokeyClient.GetKeyHandleAsync(name);
    

### ListKeyHandles(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListKeyHandlesResponse, KeyHandle> ListKeyHandles(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists [KeyHandles][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Name of the resource project and location from which to list [KeyHandles][google.cloud.kms.v1.KeyHandle], e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListKeyHandlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesResponse)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A pageable sequence of [KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle) resources.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = AutokeyClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListKeyHandlesResponse, KeyHandle> response = autokeyClient.ListKeyHandles(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (KeyHandle item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListKeyHandlesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyHandle item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyHandle> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyHandle item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListKeyHandles(ListKeyHandlesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListKeyHandlesResponse, KeyHandle> ListKeyHandles(ListKeyHandlesRequest request, CallSettings callSettings = null)

Lists [KeyHandles][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListKeyHandlesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListKeyHandlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesResponse)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A pageable sequence of [KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle) resources.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = AutokeyClient.Create();
    // Initialize request argument(s)
    ListKeyHandlesRequest request = new ListKeyHandlesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListKeyHandlesResponse, KeyHandle> response = autokeyClient.ListKeyHandles(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (KeyHandle item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListKeyHandlesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyHandle item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyHandle> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyHandle item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListKeyHandles(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListKeyHandlesResponse, KeyHandle> ListKeyHandles(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists [KeyHandles][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource project and location from which to list [KeyHandles][google.cloud.kms.v1.KeyHandle], e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListKeyHandlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesResponse)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A pageable sequence of [KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle) resources.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = AutokeyClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListKeyHandlesResponse, KeyHandle> response = autokeyClient.ListKeyHandles(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (KeyHandle item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListKeyHandlesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyHandle item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyHandle> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyHandle item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListKeyHandlesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListKeyHandlesResponse, KeyHandle> ListKeyHandlesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists [KeyHandles][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Name of the resource project and location from which to list [KeyHandles][google.cloud.kms.v1.KeyHandle], e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListKeyHandlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesResponse)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A pageable asynchronous sequence of [KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle) resources.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListKeyHandlesResponse, KeyHandle> response = autokeyClient.ListKeyHandlesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (KeyHandle item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListKeyHandlesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyHandle item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyHandle> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyHandle item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListKeyHandlesAsync(ListKeyHandlesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListKeyHandlesResponse, KeyHandle> ListKeyHandlesAsync(ListKeyHandlesRequest request, CallSettings callSettings = null)

Lists [KeyHandles][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListKeyHandlesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListKeyHandlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesResponse)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A pageable asynchronous sequence of [KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle) resources.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    ListKeyHandlesRequest request = new ListKeyHandlesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListKeyHandlesResponse, KeyHandle> response = autokeyClient.ListKeyHandlesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (KeyHandle item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListKeyHandlesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyHandle item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyHandle> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyHandle item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListKeyHandlesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListKeyHandlesResponse, KeyHandle> ListKeyHandlesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists [KeyHandles][google.cloud.kms.v1.KeyHandle].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource project and location from which to list [KeyHandles][google.cloud.kms.v1.KeyHandle], e.g. `projects/{PROJECT_ID}/locations/{LOCATION}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListKeyHandlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesResponse)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)` | A pageable asynchronous sequence of [KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle) resources.  
**Example**
    
    
    // Create client
    AutokeyClient autokeyClient = await AutokeyClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListKeyHandlesResponse, KeyHandle> response = autokeyClient.ListKeyHandlesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (KeyHandle item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListKeyHandlesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyHandle item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyHandle> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyHandle item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateKeyHandle(string, CallSettings)
    
    
    public virtual Operation<KeyHandle, CreateKeyHandleMetadata> PollOnceCreateKeyHandle(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateKeyHandle`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | The result of polling the operation.  
  
### PollOnceCreateKeyHandleAsync(string, CallSettings)
    
    
    public virtual Task<Operation<KeyHandle, CreateKeyHandleMetadata>> PollOnceCreateKeyHandleAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateKeyHandle`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)[CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient#Google_Cloud_Kms_V1_AutokeyClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient#Google_Cloud_Kms_V1_AutokeyClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient#Google_Cloud_Kms_V1_AutokeyClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient#Google_Cloud_Kms_V1_AutokeyClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
