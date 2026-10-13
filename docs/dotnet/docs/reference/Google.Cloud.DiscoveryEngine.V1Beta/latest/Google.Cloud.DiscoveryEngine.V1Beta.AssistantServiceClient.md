---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient
title: Discovery Engine v1beta API - Class AssistantServiceClient (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:18.752818+00:00
---

# Discovery Engine v1beta API - Class AssistantServiceClient (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class AssistantServiceClient (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public abstract class AssistantServiceClient

Reference documentation and code samples for the Discovery Engine v1beta API class AssistantServiceClient.

AssistantService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AssistantServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AssistantServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClientImpl)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Remarks

Service for managing Assistant configuration and assisting users.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AssistantService service, which is a host of "discoveryengine.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AssistantService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AssistantService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/discoveryengine.assist.readwrite>
  * <https://www.googleapis.com/auth/discoveryengine.readwrite>
  * <https://www.googleapis.com/auth/discoveryengine.serving.readwrite>



### GrpcClient
    
    
    public virtual AssistantService.AssistantServiceClient GrpcClient { get; }

The underlying gRPC AssistantService client

**Property Value**  
---  
**Type** | **Description**  
`[AssistantService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantService)[AssistantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantService.AssistantServiceClient)` |   
  
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
    
    
    public static AssistantServiceClient Create()

Synchronously creates a [AssistantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AssistantServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AssistantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient)` | The created [AssistantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient).  
  
### CreateAssistant(CreateAssistantRequest, CallSettings)
    
    
    public virtual Assistant CreateAssistant(CreateAssistantRequest request, CallSettings callSettings = null)

Creates an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | The RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    CreateAssistantRequest request = new CreateAssistantRequest
    {
        ParentAsEngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
        Assistant = new Assistant(),
        AssistantId = "",
    };
    // Make the request
    Assistant response = assistantServiceClient.CreateAssistant(request);
    

### CreateAssistantAsync(CreateAssistantRequest, CallSettings)
    
    
    public virtual Task<Assistant> CreateAssistantAsync(CreateAssistantRequest request, CallSettings callSettings = null)

Creates an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateAssistantRequest request = new CreateAssistantRequest
    {
        ParentAsEngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
        Assistant = new Assistant(),
        AssistantId = "",
    };
    // Make the request
    Assistant response = await assistantServiceClient.CreateAssistantAsync(request);
    

### CreateAssistantAsync(CreateAssistantRequest, CancellationToken)
    
    
    public virtual Task<Assistant> CreateAssistantAsync(CreateAssistantRequest request, CancellationToken cancellationToken)

Creates an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateAssistantRequest request = new CreateAssistantRequest
    {
        ParentAsEngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
        Assistant = new Assistant(),
        AssistantId = "",
    };
    // Make the request
    Assistant response = await assistantServiceClient.CreateAssistantAsync(request);
    

### CreateAsync(CancellationToken)
    
    
    public static Task<AssistantServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AssistantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AssistantServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AssistantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient)` | The task representing the created [AssistantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient).  
  
### DeleteAssistant(AssistantName, CallSettings)
    
    
    public virtual void DeleteAssistant(AssistantName name, CallSettings callSettings = null)

Deletes an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssistantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantName)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}` If the caller does not have permission to delete the [Assistant][google.cloud.discoveryengine.v1beta.Assistant], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to delete does not exist, a NOT_FOUND error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    AssistantName name = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]");
    // Make the request
    assistantServiceClient.DeleteAssistant(name);
    

### DeleteAssistant(DeleteAssistantRequest, CallSettings)
    
    
    public virtual void DeleteAssistant(DeleteAssistantRequest request, CallSettings callSettings = null)

Deletes an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    DeleteAssistantRequest request = new DeleteAssistantRequest
    {
        AssistantName = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]"),
    };
    // Make the request
    assistantServiceClient.DeleteAssistant(request);
    

### DeleteAssistant(string, CallSettings)
    
    
    public virtual void DeleteAssistant(string name, CallSettings callSettings = null)

Deletes an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}` If the caller does not have permission to delete the [Assistant][google.cloud.discoveryengine.v1beta.Assistant], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to delete does not exist, a NOT_FOUND error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]/assistants/[ASSISTANT]";
    // Make the request
    assistantServiceClient.DeleteAssistant(name);
    

### DeleteAssistantAsync(AssistantName, CallSettings)
    
    
    public virtual Task DeleteAssistantAsync(AssistantName name, CallSettings callSettings = null)

Deletes an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssistantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantName)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}` If the caller does not have permission to delete the [Assistant][google.cloud.discoveryengine.v1beta.Assistant], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to delete does not exist, a NOT_FOUND error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    AssistantName name = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]");
    // Make the request
    await assistantServiceClient.DeleteAssistantAsync(name);
    

### DeleteAssistantAsync(AssistantName, CancellationToken)
    
    
    public virtual Task DeleteAssistantAsync(AssistantName name, CancellationToken cancellationToken)

Deletes an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssistantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantName)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}` If the caller does not have permission to delete the [Assistant][google.cloud.discoveryengine.v1beta.Assistant], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to delete does not exist, a NOT_FOUND error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    AssistantName name = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]");
    // Make the request
    await assistantServiceClient.DeleteAssistantAsync(name);
    

### DeleteAssistantAsync(DeleteAssistantRequest, CallSettings)
    
    
    public virtual Task DeleteAssistantAsync(DeleteAssistantRequest request, CallSettings callSettings = null)

Deletes an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAssistantRequest request = new DeleteAssistantRequest
    {
        AssistantName = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]"),
    };
    // Make the request
    await assistantServiceClient.DeleteAssistantAsync(request);
    

### DeleteAssistantAsync(DeleteAssistantRequest, CancellationToken)
    
    
    public virtual Task DeleteAssistantAsync(DeleteAssistantRequest request, CancellationToken cancellationToken)

Deletes an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAssistantRequest request = new DeleteAssistantRequest
    {
        AssistantName = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]"),
    };
    // Make the request
    await assistantServiceClient.DeleteAssistantAsync(request);
    

### DeleteAssistantAsync(string, CallSettings)
    
    
    public virtual Task DeleteAssistantAsync(string name, CallSettings callSettings = null)

Deletes an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}` If the caller does not have permission to delete the [Assistant][google.cloud.discoveryengine.v1beta.Assistant], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to delete does not exist, a NOT_FOUND error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]/assistants/[ASSISTANT]";
    // Make the request
    await assistantServiceClient.DeleteAssistantAsync(name);
    

### DeleteAssistantAsync(string, CancellationToken)
    
    
    public virtual Task DeleteAssistantAsync(string name, CancellationToken cancellationToken)

Deletes an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}` If the caller does not have permission to delete the [Assistant][google.cloud.discoveryengine.v1beta.Assistant], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to delete does not exist, a NOT_FOUND error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]/assistants/[ASSISTANT]";
    // Make the request
    await assistantServiceClient.DeleteAssistantAsync(name);
    

### GetAssistant(AssistantName, CallSettings)
    
    
    public virtual Assistant GetAssistant(AssistantName name, CallSettings callSettings = null)

Gets an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssistantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantName)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | The RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    AssistantName name = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]");
    // Make the request
    Assistant response = assistantServiceClient.GetAssistant(name);
    

### GetAssistant(GetAssistantRequest, CallSettings)
    
    
    public virtual Assistant GetAssistant(GetAssistantRequest request, CallSettings callSettings = null)

Gets an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | The RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    GetAssistantRequest request = new GetAssistantRequest
    {
        AssistantName = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]"),
    };
    // Make the request
    Assistant response = assistantServiceClient.GetAssistant(request);
    

### GetAssistant(string, CallSettings)
    
    
    public virtual Assistant GetAssistant(string name, CallSettings callSettings = null)

Gets an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | The RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]/assistants/[ASSISTANT]";
    // Make the request
    Assistant response = assistantServiceClient.GetAssistant(name);
    

### GetAssistantAsync(AssistantName, CallSettings)
    
    
    public virtual Task<Assistant> GetAssistantAsync(AssistantName name, CallSettings callSettings = null)

Gets an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssistantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantName)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    AssistantName name = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]");
    // Make the request
    Assistant response = await assistantServiceClient.GetAssistantAsync(name);
    

### GetAssistantAsync(AssistantName, CancellationToken)
    
    
    public virtual Task<Assistant> GetAssistantAsync(AssistantName name, CancellationToken cancellationToken)

Gets an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssistantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantName)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    AssistantName name = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]");
    // Make the request
    Assistant response = await assistantServiceClient.GetAssistantAsync(name);
    

### GetAssistantAsync(GetAssistantRequest, CallSettings)
    
    
    public virtual Task<Assistant> GetAssistantAsync(GetAssistantRequest request, CallSettings callSettings = null)

Gets an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAssistantRequest request = new GetAssistantRequest
    {
        AssistantName = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]"),
    };
    // Make the request
    Assistant response = await assistantServiceClient.GetAssistantAsync(request);
    

### GetAssistantAsync(GetAssistantRequest, CancellationToken)
    
    
    public virtual Task<Assistant> GetAssistantAsync(GetAssistantRequest request, CancellationToken cancellationToken)

Gets an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAssistantRequest request = new GetAssistantRequest
    {
        AssistantName = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]"),
    };
    // Make the request
    Assistant response = await assistantServiceClient.GetAssistantAsync(request);
    

### GetAssistantAsync(string, CallSettings)
    
    
    public virtual Task<Assistant> GetAssistantAsync(string name, CallSettings callSettings = null)

Gets an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]/assistants/[ASSISTANT]";
    // Make the request
    Assistant response = await assistantServiceClient.GetAssistantAsync(name);
    

### GetAssistantAsync(string, CancellationToken)
    
    
    public virtual Task<Assistant> GetAssistantAsync(string name, CancellationToken cancellationToken)

Gets an [Assistant][google.cloud.discoveryengine.v1beta.Assistant].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of [Assistant][google.cloud.discoveryengine.v1beta.Assistant]. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]/assistants/[ASSISTANT]";
    // Make the request
    Assistant response = await assistantServiceClient.GetAssistantAsync(name);
    

### ListAssistants(EngineName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAssistantsResponse, Assistant> ListAssistants(EngineName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all [Assistant][google.cloud.discoveryengine.v1beta.Assistant]s under an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAssistantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListAssistantsResponse)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A pageable sequence of [Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant) resources.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    EngineName parent = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    PagedEnumerable<ListAssistantsResponse, Assistant> response = assistantServiceClient.ListAssistants(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Assistant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAssistantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Assistant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Assistant> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Assistant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssistants(ListAssistantsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAssistantsResponse, Assistant> ListAssistants(ListAssistantsRequest request, CallSettings callSettings = null)

Lists all [Assistant][google.cloud.discoveryengine.v1beta.Assistant]s under an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAssistantsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListAssistantsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAssistantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListAssistantsResponse)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A pageable sequence of [Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant) resources.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    ListAssistantsRequest request = new ListAssistantsRequest
    {
        ParentAsEngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    PagedEnumerable<ListAssistantsResponse, Assistant> response = assistantServiceClient.ListAssistants(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Assistant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAssistantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Assistant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Assistant> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Assistant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssistants(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAssistantsResponse, Assistant> ListAssistants(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all [Assistant][google.cloud.discoveryengine.v1beta.Assistant]s under an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAssistantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListAssistantsResponse)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A pageable sequence of [Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant) resources.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    PagedEnumerable<ListAssistantsResponse, Assistant> response = assistantServiceClient.ListAssistants(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Assistant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAssistantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Assistant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Assistant> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Assistant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssistantsAsync(EngineName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAssistantsResponse, Assistant> ListAssistantsAsync(EngineName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all [Assistant][google.cloud.discoveryengine.v1beta.Assistant]s under an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAssistantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListAssistantsResponse)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A pageable asynchronous sequence of [Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant) resources.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName parent = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    PagedAsyncEnumerable<ListAssistantsResponse, Assistant> response = assistantServiceClient.ListAssistantsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Assistant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAssistantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Assistant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Assistant> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Assistant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssistantsAsync(ListAssistantsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAssistantsResponse, Assistant> ListAssistantsAsync(ListAssistantsRequest request, CallSettings callSettings = null)

Lists all [Assistant][google.cloud.discoveryengine.v1beta.Assistant]s under an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAssistantsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListAssistantsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAssistantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListAssistantsResponse)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A pageable asynchronous sequence of [Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant) resources.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListAssistantsRequest request = new ListAssistantsRequest
    {
        ParentAsEngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListAssistantsResponse, Assistant> response = assistantServiceClient.ListAssistantsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Assistant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAssistantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Assistant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Assistant> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Assistant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssistantsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAssistantsResponse, Assistant> ListAssistantsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all [Assistant][google.cloud.discoveryengine.v1beta.Assistant]s under an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAssistantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListAssistantsResponse)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A pageable asynchronous sequence of [Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant) resources.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    PagedAsyncEnumerable<ListAssistantsResponse, Assistant> response = assistantServiceClient.ListAssistantsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Assistant item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAssistantsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Assistant item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Assistant> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Assistant item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_AssistantServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_AssistantServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_AssistantServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_AssistantServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### StreamAssist(StreamAssistRequest, CallSettings)
    
    
    public virtual AssistantServiceClient.StreamAssistStream StreamAssist(StreamAssistRequest request, CallSettings callSettings = null)

Assists the user with a query in a streaming fashion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StreamAssistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.StreamAssistRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AssistantServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient)[StreamAssistStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AssistantServiceClient.StreamAssistStream)` | The server stream.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    StreamAssistRequest request = new StreamAssistRequest
    {
        AssistantName = AssistantName.FromProjectLocationCollectionEngineAssistant("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]"),
        Query = new Query(),
        SessionAsSessionName = SessionName.FromProjectLocationDataStoreSession("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]"),
        UserMetadata = new AssistUserMetadata(),
        ToolsSpec = new StreamAssistRequest.Types.ToolsSpec(),
        GenerationSpec = new StreamAssistRequest.Types.GenerationSpec(),
        AgentsSpec = new StreamAssistRequest.Types.AgentsSpec(),
    };
    // Make the request, returning a streaming response
    using AssistantServiceClient.StreamAssistStream response = assistantServiceClient.StreamAssist(request);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<StreamAssistResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        StreamAssistResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### UpdateAssistant(Assistant, FieldMask, CallSettings)
    
    
    public virtual Assistant UpdateAssistant(Assistant assistant, FieldMask updateMask, CallSettings callSettings = null)

Updates an [Assistant][google.cloud.discoveryengine.v1beta.Assistant]

**Parameters**  
---  
**Name** | **Description**  
`assistant` | `[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)`  
Required. The [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to update. The [Assistant][google.cloud.discoveryengine.v1beta.Assistant]'s `name` field is used to identify the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to update. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}` If the caller does not have permission to update the [Assistant][google.cloud.discoveryengine.v1beta.Assistant], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | The RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    Assistant assistant = new Assistant();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Assistant response = assistantServiceClient.UpdateAssistant(assistant, updateMask);
    

### UpdateAssistant(UpdateAssistantRequest, CallSettings)
    
    
    public virtual Assistant UpdateAssistant(UpdateAssistantRequest request, CallSettings callSettings = null)

Updates an [Assistant][google.cloud.discoveryengine.v1beta.Assistant]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | The RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = AssistantServiceClient.Create();
    // Initialize request argument(s)
    UpdateAssistantRequest request = new UpdateAssistantRequest
    {
        Assistant = new Assistant(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Assistant response = assistantServiceClient.UpdateAssistant(request);
    

### UpdateAssistantAsync(Assistant, FieldMask, CallSettings)
    
    
    public virtual Task<Assistant> UpdateAssistantAsync(Assistant assistant, FieldMask updateMask, CallSettings callSettings = null)

Updates an [Assistant][google.cloud.discoveryengine.v1beta.Assistant]

**Parameters**  
---  
**Name** | **Description**  
`assistant` | `[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)`  
Required. The [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to update. The [Assistant][google.cloud.discoveryengine.v1beta.Assistant]'s `name` field is used to identify the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to update. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}` If the caller does not have permission to update the [Assistant][google.cloud.discoveryengine.v1beta.Assistant], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    Assistant assistant = new Assistant();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Assistant response = await assistantServiceClient.UpdateAssistantAsync(assistant, updateMask);
    

### UpdateAssistantAsync(Assistant, FieldMask, CancellationToken)
    
    
    public virtual Task<Assistant> UpdateAssistantAsync(Assistant assistant, FieldMask updateMask, CancellationToken cancellationToken)

Updates an [Assistant][google.cloud.discoveryengine.v1beta.Assistant]

**Parameters**  
---  
**Name** | **Description**  
`assistant` | `[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)`  
Required. The [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to update. The [Assistant][google.cloud.discoveryengine.v1beta.Assistant]'s `name` field is used to identify the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to update. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}` If the caller does not have permission to update the [Assistant][google.cloud.discoveryengine.v1beta.Assistant], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Assistant][google.cloud.discoveryengine.v1beta.Assistant] to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    Assistant assistant = new Assistant();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Assistant response = await assistantServiceClient.UpdateAssistantAsync(assistant, updateMask);
    

### UpdateAssistantAsync(UpdateAssistantRequest, CallSettings)
    
    
    public virtual Task<Assistant> UpdateAssistantAsync(UpdateAssistantRequest request, CallSettings callSettings = null)

Updates an [Assistant][google.cloud.discoveryengine.v1beta.Assistant]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAssistantRequest request = new UpdateAssistantRequest
    {
        Assistant = new Assistant(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Assistant response = await assistantServiceClient.UpdateAssistantAsync(request);
    

### UpdateAssistantAsync(UpdateAssistantRequest, CancellationToken)
    
    
    public virtual Task<Assistant> UpdateAssistantAsync(UpdateAssistantRequest request, CancellationToken cancellationToken)

Updates an [Assistant][google.cloud.discoveryengine.v1beta.Assistant]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAssistantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateAssistantRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assistant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Assistant)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AssistantServiceClient assistantServiceClient = await AssistantServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAssistantRequest request = new UpdateAssistantRequest
    {
        Assistant = new Assistant(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Assistant response = await assistantServiceClient.UpdateAssistantAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
