---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client
title: Binary Authorization v1beta1 API - Class BinauthzManagementServiceV1Beta1Client (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:48.962654+00:00
---

# Binary Authorization v1beta1 API - Class BinauthzManagementServiceV1Beta1Client (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1beta1 API - Class BinauthzManagementServiceV1Beta1Client (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta05 
    
    
    public abstract class BinauthzManagementServiceV1Beta1Client

Reference documentation and code samples for the Binary Authorization v1beta1 API class BinauthzManagementServiceV1Beta1Client.

BinauthzManagementServiceV1Beta1 client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BinauthzManagementServiceV1Beta1Client

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[BinauthzManagementServiceV1Beta1ClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1ClientImpl)

## Namespace

[Google.Cloud.BinaryAuthorization.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1)

## Assembly

Google.Cloud.BinaryAuthorization.V1Beta1.dll

## Remarks

Google Cloud Management Service for Binary Authorization admission policies and attestation authorities.

This API implements a REST model with the following objects:

  * [Policy][google.cloud.binaryauthorization.v1beta1.Policy]
  * [Attestor][google.cloud.binaryauthorization.v1beta1.Attestor]



## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the BinauthzManagementServiceV1Beta1 service, which is a host of "binaryauthorization.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default BinauthzManagementServiceV1Beta1 scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default BinauthzManagementServiceV1Beta1 scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client GrpcClient { get; }

The underlying gRPC BinauthzManagementServiceV1Beta1 client

**Property Value**  
---  
**Type** | **Description**  
`[BinauthzManagementServiceV1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1)[BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client)` |   
  
### IAMPolicyClient
    
    
    public virtual IAMPolicyClient IAMPolicyClient { get; }

The [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static BinauthzManagementServiceV1Beta1Client Create()

Synchronously creates a [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [BinauthzManagementServiceV1Beta1ClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1ClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client)` | The created [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<BinauthzManagementServiceV1Beta1Client> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [BinauthzManagementServiceV1Beta1ClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1ClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client)` | The task representing the created [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client).  
  
### CreateAttestor(ProjectName, string, Attestor, CallSettings)
    
    
    public virtual Attestor CreateAttestor(ProjectName parent, string attestorId, Attestor attestor, CallSettings callSettings = null)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The parent of this [attestor][google.cloud.binaryauthorization.v1beta1.Attestor].  
`attestorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] ID.  
`attestor` | `[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)`  
Required. The initial [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] value. The service will overwrite the [attestor name][google.cloud.binaryauthorization.v1beta1.Attestor.name] field with the resource name, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    string attestorId = "";
    Attestor attestor = new Attestor();
    // Make the request
    Attestor response = binauthzManagementServiceV1Beta1Client.CreateAttestor(parent, attestorId, attestor);
    

### CreateAttestor(CreateAttestorRequest, CallSettings)
    
    
    public virtual Attestor CreateAttestor(CreateAttestorRequest request, CallSettings callSettings = null)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.CreateAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    CreateAttestorRequest request = new CreateAttestorRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AttestorId = "",
        Attestor = new Attestor(),
    };
    // Make the request
    Attestor response = binauthzManagementServiceV1Beta1Client.CreateAttestor(request);
    

### CreateAttestor(string, string, Attestor, CallSettings)
    
    
    public virtual Attestor CreateAttestor(string parent, string attestorId, Attestor attestor, CallSettings callSettings = null)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of this [attestor][google.cloud.binaryauthorization.v1beta1.Attestor].  
`attestorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] ID.  
`attestor` | `[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)`  
Required. The initial [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] value. The service will overwrite the [attestor name][google.cloud.binaryauthorization.v1beta1.Attestor.name] field with the resource name, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    string attestorId = "";
    Attestor attestor = new Attestor();
    // Make the request
    Attestor response = binauthzManagementServiceV1Beta1Client.CreateAttestor(parent, attestorId, attestor);
    

### CreateAttestorAsync(ProjectName, string, Attestor, CallSettings)
    
    
    public virtual Task<Attestor> CreateAttestorAsync(ProjectName parent, string attestorId, Attestor attestor, CallSettings callSettings = null)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The parent of this [attestor][google.cloud.binaryauthorization.v1beta1.Attestor].  
`attestorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] ID.  
`attestor` | `[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)`  
Required. The initial [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] value. The service will overwrite the [attestor name][google.cloud.binaryauthorization.v1beta1.Attestor.name] field with the resource name, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    string attestorId = "";
    Attestor attestor = new Attestor();
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.CreateAttestorAsync(parent, attestorId, attestor);
    

### CreateAttestorAsync(ProjectName, string, Attestor, CancellationToken)
    
    
    public virtual Task<Attestor> CreateAttestorAsync(ProjectName parent, string attestorId, Attestor attestor, CancellationToken cancellationToken)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The parent of this [attestor][google.cloud.binaryauthorization.v1beta1.Attestor].  
`attestorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] ID.  
`attestor` | `[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)`  
Required. The initial [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] value. The service will overwrite the [attestor name][google.cloud.binaryauthorization.v1beta1.Attestor.name] field with the resource name, in the format `projects/*/attestors/*`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    string attestorId = "";
    Attestor attestor = new Attestor();
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.CreateAttestorAsync(parent, attestorId, attestor);
    

### CreateAttestorAsync(CreateAttestorRequest, CallSettings)
    
    
    public virtual Task<Attestor> CreateAttestorAsync(CreateAttestorRequest request, CallSettings callSettings = null)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.CreateAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    CreateAttestorRequest request = new CreateAttestorRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AttestorId = "",
        Attestor = new Attestor(),
    };
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.CreateAttestorAsync(request);
    

### CreateAttestorAsync(CreateAttestorRequest, CancellationToken)
    
    
    public virtual Task<Attestor> CreateAttestorAsync(CreateAttestorRequest request, CancellationToken cancellationToken)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.CreateAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    CreateAttestorRequest request = new CreateAttestorRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AttestorId = "",
        Attestor = new Attestor(),
    };
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.CreateAttestorAsync(request);
    

### CreateAttestorAsync(string, string, Attestor, CallSettings)
    
    
    public virtual Task<Attestor> CreateAttestorAsync(string parent, string attestorId, Attestor attestor, CallSettings callSettings = null)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of this [attestor][google.cloud.binaryauthorization.v1beta1.Attestor].  
`attestorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] ID.  
`attestor` | `[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)`  
Required. The initial [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] value. The service will overwrite the [attestor name][google.cloud.binaryauthorization.v1beta1.Attestor.name] field with the resource name, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    string attestorId = "";
    Attestor attestor = new Attestor();
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.CreateAttestorAsync(parent, attestorId, attestor);
    

### CreateAttestorAsync(string, string, Attestor, CancellationToken)
    
    
    public virtual Task<Attestor> CreateAttestorAsync(string parent, string attestorId, Attestor attestor, CancellationToken cancellationToken)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of this [attestor][google.cloud.binaryauthorization.v1beta1.Attestor].  
`attestorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] ID.  
`attestor` | `[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)`  
Required. The initial [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] value. The service will overwrite the [attestor name][google.cloud.binaryauthorization.v1beta1.Attestor.name] field with the resource name, in the format `projects/*/attestors/*`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    string attestorId = "";
    Attestor attestor = new Attestor();
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.CreateAttestorAsync(parent, attestorId, attestor);
    

### DeleteAttestor(AttestorName, CallSettings)
    
    
    public virtual void DeleteAttestor(AttestorName name, CallSettings callSettings = null)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorName)`  
Required. The name of the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] to delete, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    AttestorName name = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]");
    // Make the request
    binauthzManagementServiceV1Beta1Client.DeleteAttestor(name);
    

### DeleteAttestor(DeleteAttestorRequest, CallSettings)
    
    
    public virtual void DeleteAttestor(DeleteAttestorRequest request, CallSettings callSettings = null)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.DeleteAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    DeleteAttestorRequest request = new DeleteAttestorRequest
    {
        AttestorName = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]"),
    };
    // Make the request
    binauthzManagementServiceV1Beta1Client.DeleteAttestor(request);
    

### DeleteAttestor(string, CallSettings)
    
    
    public virtual void DeleteAttestor(string name, CallSettings callSettings = null)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] to delete, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/attestors/[ATTESTOR]";
    // Make the request
    binauthzManagementServiceV1Beta1Client.DeleteAttestor(name);
    

### DeleteAttestorAsync(AttestorName, CallSettings)
    
    
    public virtual Task DeleteAttestorAsync(AttestorName name, CallSettings callSettings = null)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorName)`  
Required. The name of the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] to delete, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    AttestorName name = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]");
    // Make the request
    await binauthzManagementServiceV1Beta1Client.DeleteAttestorAsync(name);
    

### DeleteAttestorAsync(AttestorName, CancellationToken)
    
    
    public virtual Task DeleteAttestorAsync(AttestorName name, CancellationToken cancellationToken)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorName)`  
Required. The name of the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] to delete, in the format `projects/*/attestors/*`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    AttestorName name = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]");
    // Make the request
    await binauthzManagementServiceV1Beta1Client.DeleteAttestorAsync(name);
    

### DeleteAttestorAsync(DeleteAttestorRequest, CallSettings)
    
    
    public virtual Task DeleteAttestorAsync(DeleteAttestorRequest request, CallSettings callSettings = null)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.DeleteAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    DeleteAttestorRequest request = new DeleteAttestorRequest
    {
        AttestorName = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]"),
    };
    // Make the request
    await binauthzManagementServiceV1Beta1Client.DeleteAttestorAsync(request);
    

### DeleteAttestorAsync(DeleteAttestorRequest, CancellationToken)
    
    
    public virtual Task DeleteAttestorAsync(DeleteAttestorRequest request, CancellationToken cancellationToken)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.DeleteAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    DeleteAttestorRequest request = new DeleteAttestorRequest
    {
        AttestorName = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]"),
    };
    // Make the request
    await binauthzManagementServiceV1Beta1Client.DeleteAttestorAsync(request);
    

### DeleteAttestorAsync(string, CallSettings)
    
    
    public virtual Task DeleteAttestorAsync(string name, CallSettings callSettings = null)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] to delete, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/attestors/[ATTESTOR]";
    // Make the request
    await binauthzManagementServiceV1Beta1Client.DeleteAttestorAsync(name);
    

### DeleteAttestorAsync(string, CancellationToken)
    
    
    public virtual Task DeleteAttestorAsync(string name, CancellationToken cancellationToken)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] to delete, in the format `projects/*/attestors/*`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/attestors/[ATTESTOR]";
    // Make the request
    await binauthzManagementServiceV1Beta1Client.DeleteAttestorAsync(name);
    

### GetAttestor(AttestorName, CallSettings)
    
    
    public virtual Attestor GetAttestor(AttestorName name, CallSettings callSettings = null)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorName)`  
Required. The name of the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] to retrieve, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    AttestorName name = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]");
    // Make the request
    Attestor response = binauthzManagementServiceV1Beta1Client.GetAttestor(name);
    

### GetAttestor(GetAttestorRequest, CallSettings)
    
    
    public virtual Attestor GetAttestor(GetAttestorRequest request, CallSettings callSettings = null)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    GetAttestorRequest request = new GetAttestorRequest
    {
        AttestorName = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]"),
    };
    // Make the request
    Attestor response = binauthzManagementServiceV1Beta1Client.GetAttestor(request);
    

### GetAttestor(string, CallSettings)
    
    
    public virtual Attestor GetAttestor(string name, CallSettings callSettings = null)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] to retrieve, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/attestors/[ATTESTOR]";
    // Make the request
    Attestor response = binauthzManagementServiceV1Beta1Client.GetAttestor(name);
    

### GetAttestorAsync(AttestorName, CallSettings)
    
    
    public virtual Task<Attestor> GetAttestorAsync(AttestorName name, CallSettings callSettings = null)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorName)`  
Required. The name of the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] to retrieve, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    AttestorName name = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]");
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.GetAttestorAsync(name);
    

### GetAttestorAsync(AttestorName, CancellationToken)
    
    
    public virtual Task<Attestor> GetAttestorAsync(AttestorName name, CancellationToken cancellationToken)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorName)`  
Required. The name of the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] to retrieve, in the format `projects/*/attestors/*`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    AttestorName name = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]");
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.GetAttestorAsync(name);
    

### GetAttestorAsync(GetAttestorRequest, CallSettings)
    
    
    public virtual Task<Attestor> GetAttestorAsync(GetAttestorRequest request, CallSettings callSettings = null)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    GetAttestorRequest request = new GetAttestorRequest
    {
        AttestorName = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]"),
    };
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.GetAttestorAsync(request);
    

### GetAttestorAsync(GetAttestorRequest, CancellationToken)
    
    
    public virtual Task<Attestor> GetAttestorAsync(GetAttestorRequest request, CancellationToken cancellationToken)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    GetAttestorRequest request = new GetAttestorRequest
    {
        AttestorName = AttestorName.FromProjectAttestor("[PROJECT]", "[ATTESTOR]"),
    };
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.GetAttestorAsync(request);
    

### GetAttestorAsync(string, CallSettings)
    
    
    public virtual Task<Attestor> GetAttestorAsync(string name, CallSettings callSettings = null)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] to retrieve, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/attestors/[ATTESTOR]";
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.GetAttestorAsync(name);
    

### GetAttestorAsync(string, CancellationToken)
    
    
    public virtual Task<Attestor> GetAttestorAsync(string name, CancellationToken cancellationToken)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] to retrieve, in the format `projects/*/attestors/*`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/attestors/[ATTESTOR]";
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.GetAttestorAsync(name);
    

### GetPolicy(GetPolicyRequest, CallSettings)
    
    
    public virtual Policy GetPolicy(GetPolicyRequest request, CallSettings callSettings = null)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    GetPolicyRequest request = new GetPolicyRequest
    {
        PolicyName = PolicyName.FromProject("[PROJECT]"),
    };
    // Make the request
    Policy response = binauthzManagementServiceV1Beta1Client.GetPolicy(request);
    

### GetPolicy(PolicyName, CallSettings)
    
    
    public virtual Policy GetPolicy(PolicyName name, CallSettings callSettings = null)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PolicyName)`  
Required. The resource name of the [policy][google.cloud.binaryauthorization.v1beta1.Policy] to retrieve, in the format `projects/*/policy`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    PolicyName name = PolicyName.FromProject("[PROJECT]");
    // Make the request
    Policy response = binauthzManagementServiceV1Beta1Client.GetPolicy(name);
    

### GetPolicy(string, CallSettings)
    
    
    public virtual Policy GetPolicy(string name, CallSettings callSettings = null)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the [policy][google.cloud.binaryauthorization.v1beta1.Policy] to retrieve, in the format `projects/*/policy`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/policy";
    // Make the request
    Policy response = binauthzManagementServiceV1Beta1Client.GetPolicy(name);
    

### GetPolicyAsync(GetPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> GetPolicyAsync(GetPolicyRequest request, CallSettings callSettings = null)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    GetPolicyRequest request = new GetPolicyRequest
    {
        PolicyName = PolicyName.FromProject("[PROJECT]"),
    };
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.GetPolicyAsync(request);
    

### GetPolicyAsync(GetPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> GetPolicyAsync(GetPolicyRequest request, CancellationToken cancellationToken)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    GetPolicyRequest request = new GetPolicyRequest
    {
        PolicyName = PolicyName.FromProject("[PROJECT]"),
    };
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.GetPolicyAsync(request);
    

### GetPolicyAsync(PolicyName, CallSettings)
    
    
    public virtual Task<Policy> GetPolicyAsync(PolicyName name, CallSettings callSettings = null)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PolicyName)`  
Required. The resource name of the [policy][google.cloud.binaryauthorization.v1beta1.Policy] to retrieve, in the format `projects/*/policy`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    PolicyName name = PolicyName.FromProject("[PROJECT]");
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.GetPolicyAsync(name);
    

### GetPolicyAsync(PolicyName, CancellationToken)
    
    
    public virtual Task<Policy> GetPolicyAsync(PolicyName name, CancellationToken cancellationToken)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PolicyName)`  
Required. The resource name of the [policy][google.cloud.binaryauthorization.v1beta1.Policy] to retrieve, in the format `projects/*/policy`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    PolicyName name = PolicyName.FromProject("[PROJECT]");
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.GetPolicyAsync(name);
    

### GetPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Policy> GetPolicyAsync(string name, CallSettings callSettings = null)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the [policy][google.cloud.binaryauthorization.v1beta1.Policy] to retrieve, in the format `projects/*/policy`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/policy";
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.GetPolicyAsync(name);
    

### GetPolicyAsync(string, CancellationToken)
    
    
    public virtual Task<Policy> GetPolicyAsync(string name, CancellationToken cancellationToken)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the [policy][google.cloud.binaryauthorization.v1beta1.Policy] to retrieve, in the format `projects/*/policy`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/policy";
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.GetPolicyAsync(name);
    

### ListAttestors(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAttestorsResponse, Attestor> ListAttestors(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The resource name of the project associated with the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor], in the format `projects/*`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A pageable sequence of [Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor) resources.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedEnumerable<ListAttestorsResponse, Attestor> response = binauthzManagementServiceV1Beta1Client.ListAttestors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Attestor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAttestorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Attestor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Attestor> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Attestor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAttestors(ListAttestorsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAttestorsResponse, Attestor> ListAttestors(ListAttestorsRequest request, CallSettings callSettings = null)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A pageable sequence of [Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor) resources.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    ListAttestorsRequest request = new ListAttestorsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    PagedEnumerable<ListAttestorsResponse, Attestor> response = binauthzManagementServiceV1Beta1Client.ListAttestors(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Attestor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAttestorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Attestor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Attestor> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Attestor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAttestors(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAttestorsResponse, Attestor> ListAttestors(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the project associated with the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor], in the format `projects/*`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A pageable sequence of [Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor) resources.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedEnumerable<ListAttestorsResponse, Attestor> response = binauthzManagementServiceV1Beta1Client.ListAttestors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Attestor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAttestorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Attestor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Attestor> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Attestor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAttestorsAsync(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAttestorsResponse, Attestor> ListAttestorsAsync(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The resource name of the project associated with the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor], in the format `projects/*`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A pageable asynchronous sequence of [Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor) resources.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedAsyncEnumerable<ListAttestorsResponse, Attestor> response = binauthzManagementServiceV1Beta1Client.ListAttestorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Attestor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAttestorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Attestor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Attestor> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Attestor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAttestorsAsync(ListAttestorsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAttestorsResponse, Attestor> ListAttestorsAsync(ListAttestorsRequest request, CallSettings callSettings = null)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A pageable asynchronous sequence of [Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor) resources.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    ListAttestorsRequest request = new ListAttestorsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListAttestorsResponse, Attestor> response = binauthzManagementServiceV1Beta1Client.ListAttestorsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Attestor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAttestorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Attestor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Attestor> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Attestor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAttestorsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAttestorsResponse, Attestor> ListAttestorsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the project associated with the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor], in the format `projects/*`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A pageable asynchronous sequence of [Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor) resources.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedAsyncEnumerable<ListAttestorsResponse, Attestor> response = binauthzManagementServiceV1Beta1Client.ListAttestorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Attestor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAttestorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Attestor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Attestor> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Attestor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client#Google_Cloud_BinaryAuthorization_V1Beta1_BinauthzManagementServiceV1Beta1Client_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client#Google_Cloud_BinaryAuthorization_V1Beta1_BinauthzManagementServiceV1Beta1Client_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client#Google_Cloud_BinaryAuthorization_V1Beta1_BinauthzManagementServiceV1Beta1Client_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client#Google_Cloud_BinaryAuthorization_V1Beta1_BinauthzManagementServiceV1Beta1Client_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateAttestor(Attestor, CallSettings)
    
    
    public virtual Attestor UpdateAttestor(Attestor attestor, CallSettings callSettings = null)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`attestor` | `[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)`  
Required. The updated [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] value. The service will overwrite the [attestor name][google.cloud.binaryauthorization.v1beta1.Attestor.name] field with the resource name in the request URL, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    Attestor attestor = new Attestor();
    // Make the request
    Attestor response = binauthzManagementServiceV1Beta1Client.UpdateAttestor(attestor);
    

### UpdateAttestor(UpdateAttestorRequest, CallSettings)
    
    
    public virtual Attestor UpdateAttestor(UpdateAttestorRequest request, CallSettings callSettings = null)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdateAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    UpdateAttestorRequest request = new UpdateAttestorRequest
    {
        Attestor = new Attestor(),
    };
    // Make the request
    Attestor response = binauthzManagementServiceV1Beta1Client.UpdateAttestor(request);
    

### UpdateAttestorAsync(Attestor, CallSettings)
    
    
    public virtual Task<Attestor> UpdateAttestorAsync(Attestor attestor, CallSettings callSettings = null)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`attestor` | `[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)`  
Required. The updated [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] value. The service will overwrite the [attestor name][google.cloud.binaryauthorization.v1beta1.Attestor.name] field with the resource name in the request URL, in the format `projects/*/attestors/*`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    Attestor attestor = new Attestor();
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.UpdateAttestorAsync(attestor);
    

### UpdateAttestorAsync(Attestor, CancellationToken)
    
    
    public virtual Task<Attestor> UpdateAttestorAsync(Attestor attestor, CancellationToken cancellationToken)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`attestor` | `[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)`  
Required. The updated [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] value. The service will overwrite the [attestor name][google.cloud.binaryauthorization.v1beta1.Attestor.name] field with the resource name in the request URL, in the format `projects/*/attestors/*`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    Attestor attestor = new Attestor();
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.UpdateAttestorAsync(attestor);
    

### UpdateAttestorAsync(UpdateAttestorRequest, CallSettings)
    
    
    public virtual Task<Attestor> UpdateAttestorAsync(UpdateAttestorRequest request, CallSettings callSettings = null)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdateAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    UpdateAttestorRequest request = new UpdateAttestorRequest
    {
        Attestor = new Attestor(),
    };
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.UpdateAttestorAsync(request);
    

### UpdateAttestorAsync(UpdateAttestorRequest, CancellationToken)
    
    
    public virtual Task<Attestor> UpdateAttestorAsync(UpdateAttestorRequest request, CancellationToken cancellationToken)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdateAttestorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    UpdateAttestorRequest request = new UpdateAttestorRequest
    {
        Attestor = new Attestor(),
    };
    // Make the request
    Attestor response = await binauthzManagementServiceV1Beta1Client.UpdateAttestorAsync(request);
    

### UpdatePolicy(Policy, CallSettings)
    
    
    public virtual Policy UpdatePolicy(Policy policy, CallSettings callSettings = null)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)`  
Required. A new or updated [policy][google.cloud.binaryauthorization.v1beta1.Policy] value. The service will overwrite the [policy name][google.cloud.binaryauthorization.v1beta1.Policy.name] field with the resource name in the request URL, in the format `projects/*/policy`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    Policy policy = new Policy();
    // Make the request
    Policy response = binauthzManagementServiceV1Beta1Client.UpdatePolicy(policy);
    

### UpdatePolicy(UpdatePolicyRequest, CallSettings)
    
    
    public virtual Policy UpdatePolicy(UpdatePolicyRequest request, CallSettings callSettings = null)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdatePolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = BinauthzManagementServiceV1Beta1Client.Create();
    // Initialize request argument(s)
    UpdatePolicyRequest request = new UpdatePolicyRequest
    {
        Policy = new Policy(),
    };
    // Make the request
    Policy response = binauthzManagementServiceV1Beta1Client.UpdatePolicy(request);
    

### UpdatePolicyAsync(Policy, CallSettings)
    
    
    public virtual Task<Policy> UpdatePolicyAsync(Policy policy, CallSettings callSettings = null)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)`  
Required. A new or updated [policy][google.cloud.binaryauthorization.v1beta1.Policy] value. The service will overwrite the [policy name][google.cloud.binaryauthorization.v1beta1.Policy.name] field with the resource name in the request URL, in the format `projects/*/policy`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    Policy policy = new Policy();
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.UpdatePolicyAsync(policy);
    

### UpdatePolicyAsync(Policy, CancellationToken)
    
    
    public virtual Task<Policy> UpdatePolicyAsync(Policy policy, CancellationToken cancellationToken)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)`  
Required. A new or updated [policy][google.cloud.binaryauthorization.v1beta1.Policy] value. The service will overwrite the [policy name][google.cloud.binaryauthorization.v1beta1.Policy.name] field with the resource name in the request URL, in the format `projects/*/policy`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    Policy policy = new Policy();
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.UpdatePolicyAsync(policy);
    

### UpdatePolicyAsync(UpdatePolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> UpdatePolicyAsync(UpdatePolicyRequest request, CallSettings callSettings = null)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdatePolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    UpdatePolicyRequest request = new UpdatePolicyRequest
    {
        Policy = new Policy(),
    };
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.UpdatePolicyAsync(request);
    

### UpdatePolicyAsync(UpdatePolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> UpdatePolicyAsync(UpdatePolicyRequest request, CancellationToken cancellationToken)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdatePolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    BinauthzManagementServiceV1Beta1Client binauthzManagementServiceV1Beta1Client = await BinauthzManagementServiceV1Beta1Client.CreateAsync();
    // Initialize request argument(s)
    UpdatePolicyRequest request = new UpdatePolicyRequest
    {
        Policy = new Policy(),
    };
    // Make the request
    Policy response = await binauthzManagementServiceV1Beta1Client.UpdatePolicyAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
