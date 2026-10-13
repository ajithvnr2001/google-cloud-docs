---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient
title: Identity and Access Management (IAM) v3beta API - Class PrincipalAccessBoundaryPoliciesClient (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:29.561718+00:00
---

# Identity and Access Management (IAM) v3beta API - Class PrincipalAccessBoundaryPoliciesClient (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3beta API - Class PrincipalAccessBoundaryPoliciesClient (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public abstract class PrincipalAccessBoundaryPoliciesClient

Reference documentation and code samples for the Identity and Access Management (IAM) v3beta API class PrincipalAccessBoundaryPoliciesClient.

PrincipalAccessBoundaryPolicies client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PrincipalAccessBoundaryPoliciesClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[PrincipalAccessBoundaryPoliciesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClientImpl)

## Namespace

[Google.Cloud.Iam.V3Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta)

## Assembly

Google.Cloud.Iam.V3Beta.dll

## Remarks

Manages Identity and Access Management (IAM) principal access boundary policies.

## Properties 

### CreatePrincipalAccessBoundaryPolicyOperationsClient
    
    
    public virtual OperationsClient CreatePrincipalAccessBoundaryPolicyOperationsClient { get; }

The long-running operations client for `CreatePrincipalAccessBoundaryPolicy`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the PrincipalAccessBoundaryPolicies service, which is a host of "iam.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default PrincipalAccessBoundaryPolicies scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default PrincipalAccessBoundaryPolicies scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeletePrincipalAccessBoundaryPolicyOperationsClient
    
    
    public virtual OperationsClient DeletePrincipalAccessBoundaryPolicyOperationsClient { get; }

The long-running operations client for `DeletePrincipalAccessBoundaryPolicy`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesClient GrpcClient { get; }

The underlying gRPC PrincipalAccessBoundaryPolicies client

**Property Value**  
---  
**Type** | **Description**  
`[PrincipalAccessBoundaryPolicies](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicies)[PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicies.PrincipalAccessBoundaryPoliciesClient)` |   
  
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
  
### UpdatePrincipalAccessBoundaryPolicyOperationsClient
    
    
    public virtual OperationsClient UpdatePrincipalAccessBoundaryPolicyOperationsClient { get; }

The long-running operations client for `UpdatePrincipalAccessBoundaryPolicy`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static PrincipalAccessBoundaryPoliciesClient Create()

Synchronously creates a [PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [PrincipalAccessBoundaryPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient)` | The created [PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<PrincipalAccessBoundaryPoliciesClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [PrincipalAccessBoundaryPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient)` | The task representing the created [PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient).  
  
### CreatePrincipalAccessBoundaryPolicy(CreatePrincipalAccessBoundaryPolicyRequest, CallSettings)
    
    
    public virtual Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> CreatePrincipalAccessBoundaryPolicy(CreatePrincipalAccessBoundaryPolicyRequest request, CallSettings callSettings = null)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.CreatePrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    CreatePrincipalAccessBoundaryPolicyRequest request = new CreatePrincipalAccessBoundaryPolicyRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        PrincipalAccessBoundaryPolicyId = "",
        PrincipalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy(),
        ValidateOnly = false,
    };
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = principalAccessBoundaryPoliciesClient.CreatePrincipalAccessBoundaryPolicy(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = principalAccessBoundaryPoliciesClient.PollOnceCreatePrincipalAccessBoundaryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrincipalAccessBoundaryPolicy(OrganizationLocationName, PrincipalAccessBoundaryPolicy, string, CallSettings)
    
    
    public virtual Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> CreatePrincipalAccessBoundaryPolicy(OrganizationLocationName parent, PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy, string principalAccessBoundaryPolicyId, CallSettings callSettings = null)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OrganizationLocationName)`  
Required. The parent resource where this principal access boundary policy will be created. Only organizations are supported. Format: `organizations/{organization_id}/locations/{location}`  
`principalAccessBoundaryPolicy` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
Required. The principal access boundary policy to create.  
`principalAccessBoundaryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the principal access boundary policy, which will become the final component of the principal access boundary policy's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /[a-z][a-z0-9-.]{2,62}/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy();
    string principalAccessBoundaryPolicyId = "";
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = principalAccessBoundaryPoliciesClient.CreatePrincipalAccessBoundaryPolicy(parent, principalAccessBoundaryPolicy, principalAccessBoundaryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = principalAccessBoundaryPoliciesClient.PollOnceCreatePrincipalAccessBoundaryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrincipalAccessBoundaryPolicy(string, PrincipalAccessBoundaryPolicy, string, CallSettings)
    
    
    public virtual Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> CreatePrincipalAccessBoundaryPolicy(string parent, PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy, string principalAccessBoundaryPolicyId, CallSettings callSettings = null)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this principal access boundary policy will be created. Only organizations are supported. Format: `organizations/{organization_id}/locations/{location}`  
`principalAccessBoundaryPolicy` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
Required. The principal access boundary policy to create.  
`principalAccessBoundaryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the principal access boundary policy, which will become the final component of the principal access boundary policy's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /[a-z][a-z0-9-.]{2,62}/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy();
    string principalAccessBoundaryPolicyId = "";
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = principalAccessBoundaryPoliciesClient.CreatePrincipalAccessBoundaryPolicy(parent, principalAccessBoundaryPolicy, principalAccessBoundaryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = principalAccessBoundaryPoliciesClient.PollOnceCreatePrincipalAccessBoundaryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrincipalAccessBoundaryPolicyAsync(CreatePrincipalAccessBoundaryPolicyRequest, CallSettings)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> CreatePrincipalAccessBoundaryPolicyAsync(CreatePrincipalAccessBoundaryPolicyRequest request, CallSettings callSettings = null)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.CreatePrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    CreatePrincipalAccessBoundaryPolicyRequest request = new CreatePrincipalAccessBoundaryPolicyRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        PrincipalAccessBoundaryPolicyId = "",
        PrincipalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy(),
        ValidateOnly = false,
    };
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.CreatePrincipalAccessBoundaryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceCreatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrincipalAccessBoundaryPolicyAsync(CreatePrincipalAccessBoundaryPolicyRequest, CancellationToken)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> CreatePrincipalAccessBoundaryPolicyAsync(CreatePrincipalAccessBoundaryPolicyRequest request, CancellationToken cancellationToken)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.CreatePrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    CreatePrincipalAccessBoundaryPolicyRequest request = new CreatePrincipalAccessBoundaryPolicyRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        PrincipalAccessBoundaryPolicyId = "",
        PrincipalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy(),
        ValidateOnly = false,
    };
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.CreatePrincipalAccessBoundaryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceCreatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrincipalAccessBoundaryPolicyAsync(OrganizationLocationName, PrincipalAccessBoundaryPolicy, string, CallSettings)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> CreatePrincipalAccessBoundaryPolicyAsync(OrganizationLocationName parent, PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy, string principalAccessBoundaryPolicyId, CallSettings callSettings = null)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OrganizationLocationName)`  
Required. The parent resource where this principal access boundary policy will be created. Only organizations are supported. Format: `organizations/{organization_id}/locations/{location}`  
`principalAccessBoundaryPolicy` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
Required. The principal access boundary policy to create.  
`principalAccessBoundaryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the principal access boundary policy, which will become the final component of the principal access boundary policy's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /[a-z][a-z0-9-.]{2,62}/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy();
    string principalAccessBoundaryPolicyId = "";
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.CreatePrincipalAccessBoundaryPolicyAsync(parent, principalAccessBoundaryPolicy, principalAccessBoundaryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceCreatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrincipalAccessBoundaryPolicyAsync(OrganizationLocationName, PrincipalAccessBoundaryPolicy, string, CancellationToken)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> CreatePrincipalAccessBoundaryPolicyAsync(OrganizationLocationName parent, PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy, string principalAccessBoundaryPolicyId, CancellationToken cancellationToken)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OrganizationLocationName)`  
Required. The parent resource where this principal access boundary policy will be created. Only organizations are supported. Format: `organizations/{organization_id}/locations/{location}`  
`principalAccessBoundaryPolicy` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
Required. The principal access boundary policy to create.  
`principalAccessBoundaryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the principal access boundary policy, which will become the final component of the principal access boundary policy's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /[a-z][a-z0-9-.]{2,62}/.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy();
    string principalAccessBoundaryPolicyId = "";
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.CreatePrincipalAccessBoundaryPolicyAsync(parent, principalAccessBoundaryPolicy, principalAccessBoundaryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceCreatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrincipalAccessBoundaryPolicyAsync(string, PrincipalAccessBoundaryPolicy, string, CallSettings)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> CreatePrincipalAccessBoundaryPolicyAsync(string parent, PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy, string principalAccessBoundaryPolicyId, CallSettings callSettings = null)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this principal access boundary policy will be created. Only organizations are supported. Format: `organizations/{organization_id}/locations/{location}`  
`principalAccessBoundaryPolicy` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
Required. The principal access boundary policy to create.  
`principalAccessBoundaryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the principal access boundary policy, which will become the final component of the principal access boundary policy's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /[a-z][a-z0-9-.]{2,62}/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy();
    string principalAccessBoundaryPolicyId = "";
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.CreatePrincipalAccessBoundaryPolicyAsync(parent, principalAccessBoundaryPolicy, principalAccessBoundaryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceCreatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrincipalAccessBoundaryPolicyAsync(string, PrincipalAccessBoundaryPolicy, string, CancellationToken)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> CreatePrincipalAccessBoundaryPolicyAsync(string parent, PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy, string principalAccessBoundaryPolicyId, CancellationToken cancellationToken)

Creates a principal access boundary policy, and returns a long running operation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this principal access boundary policy will be created. Only organizations are supported. Format: `organizations/{organization_id}/locations/{location}`  
`principalAccessBoundaryPolicy` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
Required. The principal access boundary policy to create.  
`principalAccessBoundaryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the principal access boundary policy, which will become the final component of the principal access boundary policy's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /[a-z][a-z0-9-.]{2,62}/.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy();
    string principalAccessBoundaryPolicyId = "";
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.CreatePrincipalAccessBoundaryPolicyAsync(parent, principalAccessBoundaryPolicy, principalAccessBoundaryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceCreatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrincipalAccessBoundaryPolicy(DeletePrincipalAccessBoundaryPolicyRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeletePrincipalAccessBoundaryPolicy(DeletePrincipalAccessBoundaryPolicyRequest request, CallSettings callSettings = null)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.DeletePrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    DeletePrincipalAccessBoundaryPolicyRequest request = new DeletePrincipalAccessBoundaryPolicyRequest
    {
        PrincipalAccessBoundaryPolicyName = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]"),
        Etag = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = principalAccessBoundaryPoliciesClient.DeletePrincipalAccessBoundaryPolicy(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = principalAccessBoundaryPoliciesClient.PollOnceDeletePrincipalAccessBoundaryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrincipalAccessBoundaryPolicy(PrincipalAccessBoundaryPolicyName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeletePrincipalAccessBoundaryPolicy(PrincipalAccessBoundaryPolicyName name, CallSettings callSettings = null)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)`  
Required. The name of the principal access boundary policy to delete. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicyName name = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]");
    // Make the request
    Operation<Empty, OperationMetadata> response = principalAccessBoundaryPoliciesClient.DeletePrincipalAccessBoundaryPolicy(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = principalAccessBoundaryPoliciesClient.PollOnceDeletePrincipalAccessBoundaryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrincipalAccessBoundaryPolicy(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeletePrincipalAccessBoundaryPolicy(string name, CallSettings callSettings = null)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the principal access boundary policy to delete. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/principalAccessBoundaryPolicies/[PRINCIPAL_ACCESS_BOUNDARY_POLICY]";
    // Make the request
    Operation<Empty, OperationMetadata> response = principalAccessBoundaryPoliciesClient.DeletePrincipalAccessBoundaryPolicy(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = principalAccessBoundaryPoliciesClient.PollOnceDeletePrincipalAccessBoundaryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrincipalAccessBoundaryPolicyAsync(DeletePrincipalAccessBoundaryPolicyRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrincipalAccessBoundaryPolicyAsync(DeletePrincipalAccessBoundaryPolicyRequest request, CallSettings callSettings = null)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.DeletePrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    DeletePrincipalAccessBoundaryPolicyRequest request = new DeletePrincipalAccessBoundaryPolicyRequest
    {
        PrincipalAccessBoundaryPolicyName = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]"),
        Etag = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.DeletePrincipalAccessBoundaryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceDeletePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrincipalAccessBoundaryPolicyAsync(DeletePrincipalAccessBoundaryPolicyRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrincipalAccessBoundaryPolicyAsync(DeletePrincipalAccessBoundaryPolicyRequest request, CancellationToken cancellationToken)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.DeletePrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    DeletePrincipalAccessBoundaryPolicyRequest request = new DeletePrincipalAccessBoundaryPolicyRequest
    {
        PrincipalAccessBoundaryPolicyName = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]"),
        Etag = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.DeletePrincipalAccessBoundaryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceDeletePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicyName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicyName name, CallSettings callSettings = null)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)`  
Required. The name of the principal access boundary policy to delete. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicyName name = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.DeletePrincipalAccessBoundaryPolicyAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceDeletePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicyName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicyName name, CancellationToken cancellationToken)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)`  
Required. The name of the principal access boundary policy to delete. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicyName name = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.DeletePrincipalAccessBoundaryPolicyAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceDeletePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrincipalAccessBoundaryPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrincipalAccessBoundaryPolicyAsync(string name, CallSettings callSettings = null)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the principal access boundary policy to delete. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/principalAccessBoundaryPolicies/[PRINCIPAL_ACCESS_BOUNDARY_POLICY]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.DeletePrincipalAccessBoundaryPolicyAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceDeletePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrincipalAccessBoundaryPolicyAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrincipalAccessBoundaryPolicyAsync(string name, CancellationToken cancellationToken)

Deletes a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the principal access boundary policy to delete. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/principalAccessBoundaryPolicies/[PRINCIPAL_ACCESS_BOUNDARY_POLICY]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.DeletePrincipalAccessBoundaryPolicyAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceDeletePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetPrincipalAccessBoundaryPolicy(GetPrincipalAccessBoundaryPolicyRequest, CallSettings)
    
    
    public virtual PrincipalAccessBoundaryPolicy GetPrincipalAccessBoundaryPolicy(GetPrincipalAccessBoundaryPolicyRequest request, CallSettings callSettings = null)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.GetPrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    GetPrincipalAccessBoundaryPolicyRequest request = new GetPrincipalAccessBoundaryPolicyRequest
    {
        PrincipalAccessBoundaryPolicyName = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]"),
    };
    // Make the request
    PrincipalAccessBoundaryPolicy response = principalAccessBoundaryPoliciesClient.GetPrincipalAccessBoundaryPolicy(request);
    

### GetPrincipalAccessBoundaryPolicy(PrincipalAccessBoundaryPolicyName, CallSettings)
    
    
    public virtual PrincipalAccessBoundaryPolicy GetPrincipalAccessBoundaryPolicy(PrincipalAccessBoundaryPolicyName name, CallSettings callSettings = null)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)`  
Required. The name of the principal access boundary policy to retrieve. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicyName name = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]");
    // Make the request
    PrincipalAccessBoundaryPolicy response = principalAccessBoundaryPoliciesClient.GetPrincipalAccessBoundaryPolicy(name);
    

### GetPrincipalAccessBoundaryPolicy(string, CallSettings)
    
    
    public virtual PrincipalAccessBoundaryPolicy GetPrincipalAccessBoundaryPolicy(string name, CallSettings callSettings = null)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the principal access boundary policy to retrieve. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/principalAccessBoundaryPolicies/[PRINCIPAL_ACCESS_BOUNDARY_POLICY]";
    // Make the request
    PrincipalAccessBoundaryPolicy response = principalAccessBoundaryPoliciesClient.GetPrincipalAccessBoundaryPolicy(name);
    

### GetPrincipalAccessBoundaryPolicyAsync(GetPrincipalAccessBoundaryPolicyRequest, CallSettings)
    
    
    public virtual Task<PrincipalAccessBoundaryPolicy> GetPrincipalAccessBoundaryPolicyAsync(GetPrincipalAccessBoundaryPolicyRequest request, CallSettings callSettings = null)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.GetPrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    GetPrincipalAccessBoundaryPolicyRequest request = new GetPrincipalAccessBoundaryPolicyRequest
    {
        PrincipalAccessBoundaryPolicyName = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]"),
    };
    // Make the request
    PrincipalAccessBoundaryPolicy response = await principalAccessBoundaryPoliciesClient.GetPrincipalAccessBoundaryPolicyAsync(request);
    

### GetPrincipalAccessBoundaryPolicyAsync(GetPrincipalAccessBoundaryPolicyRequest, CancellationToken)
    
    
    public virtual Task<PrincipalAccessBoundaryPolicy> GetPrincipalAccessBoundaryPolicyAsync(GetPrincipalAccessBoundaryPolicyRequest request, CancellationToken cancellationToken)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.GetPrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    GetPrincipalAccessBoundaryPolicyRequest request = new GetPrincipalAccessBoundaryPolicyRequest
    {
        PrincipalAccessBoundaryPolicyName = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]"),
    };
    // Make the request
    PrincipalAccessBoundaryPolicy response = await principalAccessBoundaryPoliciesClient.GetPrincipalAccessBoundaryPolicyAsync(request);
    

### GetPrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicyName, CallSettings)
    
    
    public virtual Task<PrincipalAccessBoundaryPolicy> GetPrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicyName name, CallSettings callSettings = null)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)`  
Required. The name of the principal access boundary policy to retrieve. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicyName name = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]");
    // Make the request
    PrincipalAccessBoundaryPolicy response = await principalAccessBoundaryPoliciesClient.GetPrincipalAccessBoundaryPolicyAsync(name);
    

### GetPrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicyName, CancellationToken)
    
    
    public virtual Task<PrincipalAccessBoundaryPolicy> GetPrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicyName name, CancellationToken cancellationToken)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)`  
Required. The name of the principal access boundary policy to retrieve. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicyName name = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]");
    // Make the request
    PrincipalAccessBoundaryPolicy response = await principalAccessBoundaryPoliciesClient.GetPrincipalAccessBoundaryPolicyAsync(name);
    

### GetPrincipalAccessBoundaryPolicyAsync(string, CallSettings)
    
    
    public virtual Task<PrincipalAccessBoundaryPolicy> GetPrincipalAccessBoundaryPolicyAsync(string name, CallSettings callSettings = null)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the principal access boundary policy to retrieve. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/principalAccessBoundaryPolicies/[PRINCIPAL_ACCESS_BOUNDARY_POLICY]";
    // Make the request
    PrincipalAccessBoundaryPolicy response = await principalAccessBoundaryPoliciesClient.GetPrincipalAccessBoundaryPolicyAsync(name);
    

### GetPrincipalAccessBoundaryPolicyAsync(string, CancellationToken)
    
    
    public virtual Task<PrincipalAccessBoundaryPolicy> GetPrincipalAccessBoundaryPolicyAsync(string name, CancellationToken cancellationToken)

Gets a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the principal access boundary policy to retrieve. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/principalAccessBoundaryPolicies/[PRINCIPAL_ACCESS_BOUNDARY_POLICY]";
    // Make the request
    PrincipalAccessBoundaryPolicy response = await principalAccessBoundaryPoliciesClient.GetPrincipalAccessBoundaryPolicyAsync(name);
    

### ListPrincipalAccessBoundaryPolicies(ListPrincipalAccessBoundaryPoliciesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> ListPrincipalAccessBoundaryPolicies(ListPrincipalAccessBoundaryPoliciesRequest request, CallSettings callSettings = null)

Lists principal access boundary policies.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrincipalAccessBoundaryPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPrincipalAccessBoundaryPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPrincipalAccessBoundaryPoliciesResponse)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A pageable sequence of [PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    ListPrincipalAccessBoundaryPoliciesRequest request = new ListPrincipalAccessBoundaryPoliciesRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> response = principalAccessBoundaryPoliciesClient.ListPrincipalAccessBoundaryPolicies(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PrincipalAccessBoundaryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListPrincipalAccessBoundaryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrincipalAccessBoundaryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrincipalAccessBoundaryPolicy> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrincipalAccessBoundaryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrincipalAccessBoundaryPolicies(OrganizationLocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> ListPrincipalAccessBoundaryPolicies(OrganizationLocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists principal access boundary policies.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OrganizationLocationName)`  
Required. The parent resource, which owns the collection of principal access boundary policies. Format: `organizations/{organization_id}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPrincipalAccessBoundaryPoliciesResponse)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A pageable sequence of [PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> response = principalAccessBoundaryPoliciesClient.ListPrincipalAccessBoundaryPolicies(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PrincipalAccessBoundaryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListPrincipalAccessBoundaryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrincipalAccessBoundaryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrincipalAccessBoundaryPolicy> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrincipalAccessBoundaryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrincipalAccessBoundaryPolicies(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> ListPrincipalAccessBoundaryPolicies(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists principal access boundary policies.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource, which owns the collection of principal access boundary policies. Format: `organizations/{organization_id}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPrincipalAccessBoundaryPoliciesResponse)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A pageable sequence of [PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> response = principalAccessBoundaryPoliciesClient.ListPrincipalAccessBoundaryPolicies(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PrincipalAccessBoundaryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListPrincipalAccessBoundaryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrincipalAccessBoundaryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrincipalAccessBoundaryPolicy> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrincipalAccessBoundaryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrincipalAccessBoundaryPoliciesAsync(ListPrincipalAccessBoundaryPoliciesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> ListPrincipalAccessBoundaryPoliciesAsync(ListPrincipalAccessBoundaryPoliciesRequest request, CallSettings callSettings = null)

Lists principal access boundary policies.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrincipalAccessBoundaryPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPrincipalAccessBoundaryPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPrincipalAccessBoundaryPoliciesResponse)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A pageable asynchronous sequence of [PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    ListPrincipalAccessBoundaryPoliciesRequest request = new ListPrincipalAccessBoundaryPoliciesRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> response = principalAccessBoundaryPoliciesClient.ListPrincipalAccessBoundaryPoliciesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (PrincipalAccessBoundaryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListPrincipalAccessBoundaryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrincipalAccessBoundaryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrincipalAccessBoundaryPolicy> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrincipalAccessBoundaryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrincipalAccessBoundaryPoliciesAsync(OrganizationLocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> ListPrincipalAccessBoundaryPoliciesAsync(OrganizationLocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists principal access boundary policies.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OrganizationLocationName)`  
Required. The parent resource, which owns the collection of principal access boundary policies. Format: `organizations/{organization_id}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPrincipalAccessBoundaryPoliciesResponse)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A pageable asynchronous sequence of [PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> response = principalAccessBoundaryPoliciesClient.ListPrincipalAccessBoundaryPoliciesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (PrincipalAccessBoundaryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListPrincipalAccessBoundaryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrincipalAccessBoundaryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrincipalAccessBoundaryPolicy> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrincipalAccessBoundaryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrincipalAccessBoundaryPoliciesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> ListPrincipalAccessBoundaryPoliciesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists principal access boundary policies.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource, which owns the collection of principal access boundary policies. Format: `organizations/{organization_id}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.ListPrincipalAccessBoundaryPoliciesResponse)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)` | A pageable asynchronous sequence of [PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListPrincipalAccessBoundaryPoliciesResponse, PrincipalAccessBoundaryPolicy> response = principalAccessBoundaryPoliciesClient.ListPrincipalAccessBoundaryPoliciesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (PrincipalAccessBoundaryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListPrincipalAccessBoundaryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrincipalAccessBoundaryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrincipalAccessBoundaryPolicy> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrincipalAccessBoundaryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreatePrincipalAccessBoundaryPolicy(string, CallSettings)
    
    
    public virtual Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> PollOnceCreatePrincipalAccessBoundaryPolicy(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreatePrincipalAccessBoundaryPolicy`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreatePrincipalAccessBoundaryPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> PollOnceCreatePrincipalAccessBoundaryPolicyAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreatePrincipalAccessBoundaryPolicy`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeletePrincipalAccessBoundaryPolicy(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeletePrincipalAccessBoundaryPolicy(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeletePrincipalAccessBoundaryPolicy`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeletePrincipalAccessBoundaryPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeletePrincipalAccessBoundaryPolicyAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeletePrincipalAccessBoundaryPolicy`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdatePrincipalAccessBoundaryPolicy(string, CallSettings)
    
    
    public virtual Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> PollOnceUpdatePrincipalAccessBoundaryPolicy(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdatePrincipalAccessBoundaryPolicy`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdatePrincipalAccessBoundaryPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> PollOnceUpdatePrincipalAccessBoundaryPolicyAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdatePrincipalAccessBoundaryPolicy`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### SearchPrincipalAccessBoundaryPolicyBindings(PrincipalAccessBoundaryPolicyName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> SearchPrincipalAccessBoundaryPolicyBindings(PrincipalAccessBoundaryPolicyName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)`  
Required. The name of the principal access boundary policy. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchPrincipalAccessBoundaryPolicyBindingsResponse)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding)` | A pageable sequence of [PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicyName name = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]");
    // Make the request
    PagedEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> response = principalAccessBoundaryPoliciesClient.SearchPrincipalAccessBoundaryPolicyBindings(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PolicyBinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchPrincipalAccessBoundaryPolicyBindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PolicyBinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PolicyBinding> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PolicyBinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchPrincipalAccessBoundaryPolicyBindings(SearchPrincipalAccessBoundaryPolicyBindingsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> SearchPrincipalAccessBoundaryPolicyBindings(SearchPrincipalAccessBoundaryPolicyBindingsRequest request, CallSettings callSettings = null)

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchPrincipalAccessBoundaryPolicyBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchPrincipalAccessBoundaryPolicyBindingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchPrincipalAccessBoundaryPolicyBindingsResponse)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding)` | A pageable sequence of [PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    SearchPrincipalAccessBoundaryPolicyBindingsRequest request = new SearchPrincipalAccessBoundaryPolicyBindingsRequest
    {
        PrincipalAccessBoundaryPolicyName = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]"),
    };
    // Make the request
    PagedEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> response = principalAccessBoundaryPoliciesClient.SearchPrincipalAccessBoundaryPolicyBindings(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PolicyBinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchPrincipalAccessBoundaryPolicyBindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PolicyBinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PolicyBinding> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PolicyBinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchPrincipalAccessBoundaryPolicyBindings(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> SearchPrincipalAccessBoundaryPolicyBindings(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the principal access boundary policy. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchPrincipalAccessBoundaryPolicyBindingsResponse)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding)` | A pageable sequence of [PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/principalAccessBoundaryPolicies/[PRINCIPAL_ACCESS_BOUNDARY_POLICY]";
    // Make the request
    PagedEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> response = principalAccessBoundaryPoliciesClient.SearchPrincipalAccessBoundaryPolicyBindings(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PolicyBinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchPrincipalAccessBoundaryPolicyBindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PolicyBinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PolicyBinding> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PolicyBinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchPrincipalAccessBoundaryPolicyBindingsAsync(PrincipalAccessBoundaryPolicyName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> SearchPrincipalAccessBoundaryPolicyBindingsAsync(PrincipalAccessBoundaryPolicyName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)`  
Required. The name of the principal access boundary policy. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchPrincipalAccessBoundaryPolicyBindingsResponse)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding)` | A pageable asynchronous sequence of [PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicyName name = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]");
    // Make the request
    PagedAsyncEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> response = principalAccessBoundaryPoliciesClient.SearchPrincipalAccessBoundaryPolicyBindingsAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (PolicyBinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchPrincipalAccessBoundaryPolicyBindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PolicyBinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PolicyBinding> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PolicyBinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchPrincipalAccessBoundaryPolicyBindingsAsync(SearchPrincipalAccessBoundaryPolicyBindingsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> SearchPrincipalAccessBoundaryPolicyBindingsAsync(SearchPrincipalAccessBoundaryPolicyBindingsRequest request, CallSettings callSettings = null)

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchPrincipalAccessBoundaryPolicyBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchPrincipalAccessBoundaryPolicyBindingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchPrincipalAccessBoundaryPolicyBindingsResponse)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding)` | A pageable asynchronous sequence of [PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    SearchPrincipalAccessBoundaryPolicyBindingsRequest request = new SearchPrincipalAccessBoundaryPolicyBindingsRequest
    {
        PrincipalAccessBoundaryPolicyName = PrincipalAccessBoundaryPolicyName.FromOrganizationLocationPrincipalAccessBoundaryPolicy("[ORGANIZATION]", "[LOCATION]", "[PRINCIPAL_ACCESS_BOUNDARY_POLICY]"),
    };
    // Make the request
    PagedAsyncEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> response = principalAccessBoundaryPoliciesClient.SearchPrincipalAccessBoundaryPolicyBindingsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (PolicyBinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchPrincipalAccessBoundaryPolicyBindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PolicyBinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PolicyBinding> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PolicyBinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchPrincipalAccessBoundaryPolicyBindingsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> SearchPrincipalAccessBoundaryPolicyBindingsAsync(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the principal access boundary policy. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchPrincipalAccessBoundaryPolicyBindingsResponse)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding)` | A pageable asynchronous sequence of [PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBinding) resources.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/principalAccessBoundaryPolicies/[PRINCIPAL_ACCESS_BOUNDARY_POLICY]";
    // Make the request
    PagedAsyncEnumerable<SearchPrincipalAccessBoundaryPolicyBindingsResponse, PolicyBinding> response = principalAccessBoundaryPoliciesClient.SearchPrincipalAccessBoundaryPolicyBindingsAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (PolicyBinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchPrincipalAccessBoundaryPolicyBindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PolicyBinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PolicyBinding> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PolicyBinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient#Google_Cloud_Iam_V3Beta_PrincipalAccessBoundaryPoliciesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient#Google_Cloud_Iam_V3Beta_PrincipalAccessBoundaryPoliciesClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient#Google_Cloud_Iam_V3Beta_PrincipalAccessBoundaryPoliciesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient#Google_Cloud_Iam_V3Beta_PrincipalAccessBoundaryPoliciesClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdatePrincipalAccessBoundaryPolicy(PrincipalAccessBoundaryPolicy, FieldMask, CallSettings)
    
    
    public virtual Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> UpdatePrincipalAccessBoundaryPolicy(PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy, FieldMask updateMask, CallSettings callSettings = null)

Updates a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`principalAccessBoundaryPolicy` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
Required. The principal access boundary policy to update. The principal access boundary policy's `name` field is used to identify the policy to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = principalAccessBoundaryPoliciesClient.UpdatePrincipalAccessBoundaryPolicy(principalAccessBoundaryPolicy, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = principalAccessBoundaryPoliciesClient.PollOnceUpdatePrincipalAccessBoundaryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### UpdatePrincipalAccessBoundaryPolicy(UpdatePrincipalAccessBoundaryPolicyRequest, CallSettings)
    
    
    public virtual Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> UpdatePrincipalAccessBoundaryPolicy(UpdatePrincipalAccessBoundaryPolicyRequest request, CallSettings callSettings = null)

Updates a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdatePrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = PrincipalAccessBoundaryPoliciesClient.Create();
    // Initialize request argument(s)
    UpdatePrincipalAccessBoundaryPolicyRequest request = new UpdatePrincipalAccessBoundaryPolicyRequest
    {
        PrincipalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy(),
        ValidateOnly = false,
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = principalAccessBoundaryPoliciesClient.UpdatePrincipalAccessBoundaryPolicy(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = principalAccessBoundaryPoliciesClient.PollOnceUpdatePrincipalAccessBoundaryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### UpdatePrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicy, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> UpdatePrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy, FieldMask updateMask, CallSettings callSettings = null)

Updates a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`principalAccessBoundaryPolicy` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
Required. The principal access boundary policy to update. The principal access boundary policy's `name` field is used to identify the policy to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.UpdatePrincipalAccessBoundaryPolicyAsync(principalAccessBoundaryPolicy, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceUpdatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### UpdatePrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicy, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> UpdatePrincipalAccessBoundaryPolicyAsync(PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy, FieldMask updateMask, CancellationToken cancellationToken)

Updates a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`principalAccessBoundaryPolicy` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
Required. The principal access boundary policy to update. The principal access boundary policy's `name` field is used to identify the policy to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    PrincipalAccessBoundaryPolicy principalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.UpdatePrincipalAccessBoundaryPolicyAsync(principalAccessBoundaryPolicy, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceUpdatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### UpdatePrincipalAccessBoundaryPolicyAsync(UpdatePrincipalAccessBoundaryPolicyRequest, CallSettings)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> UpdatePrincipalAccessBoundaryPolicyAsync(UpdatePrincipalAccessBoundaryPolicyRequest request, CallSettings callSettings = null)

Updates a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdatePrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    UpdatePrincipalAccessBoundaryPolicyRequest request = new UpdatePrincipalAccessBoundaryPolicyRequest
    {
        PrincipalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy(),
        ValidateOnly = false,
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.UpdatePrincipalAccessBoundaryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceUpdatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### UpdatePrincipalAccessBoundaryPolicyAsync(UpdatePrincipalAccessBoundaryPolicyRequest, CancellationToken)
    
    
    public virtual Task<Operation<PrincipalAccessBoundaryPolicy, OperationMetadata>> UpdatePrincipalAccessBoundaryPolicyAsync(UpdatePrincipalAccessBoundaryPolicyRequest request, CancellationToken cancellationToken)

Updates a principal access boundary policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdatePrincipalAccessBoundaryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    PrincipalAccessBoundaryPoliciesClient principalAccessBoundaryPoliciesClient = await PrincipalAccessBoundaryPoliciesClient.CreateAsync();
    // Initialize request argument(s)
    UpdatePrincipalAccessBoundaryPolicyRequest request = new UpdatePrincipalAccessBoundaryPolicyRequest
    {
        PrincipalAccessBoundaryPolicy = new PrincipalAccessBoundaryPolicy(),
        ValidateOnly = false,
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> response = await principalAccessBoundaryPoliciesClient.UpdatePrincipalAccessBoundaryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrincipalAccessBoundaryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrincipalAccessBoundaryPolicy, OperationMetadata> retrievedResponse = await principalAccessBoundaryPoliciesClient.PollOnceUpdatePrincipalAccessBoundaryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrincipalAccessBoundaryPolicy retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
