---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient
title: Google Cloud Dialogflow v2beta1 API - Class GeneratorsClient (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:31.100836+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class GeneratorsClient (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class GeneratorsClient (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public abstract class GeneratorsClient

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class GeneratorsClient.

Generators client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GeneratorsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[GeneratorsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClientImpl)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Remarks

Generator Service for LLM powered Agent Assist. This service manages the configurations of user owned Generators, such as description, context and instruction, input/output format, etc. The generator resources will be used inside a conversation and will be triggered by TriggerEvent to query LLM for answers.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Generators service, which is a host of "dialogflow.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Generators scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Generators scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/dialogflow>



### GrpcClient
    
    
    public virtual Generators.GeneratorsClient GrpcClient { get; }

The underlying gRPC Generators client

**Property Value**  
---  
**Type** | **Description**  
`[Generators](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generators)[GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generators.GeneratorsClient)` |   
  
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
    
    
    public static GeneratorsClient Create()

Synchronously creates a [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [GeneratorsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient)` | The created [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<GeneratorsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [GeneratorsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient)` | The task representing the created [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient).  
  
### CreateGenerator(ProjectName, Generator, string, CallSettings)
    
    
    public virtual Generator CreateGenerator(ProjectName parent, Generator generator, string generatorId, CallSettings callSettings = null)

Creates a generator.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project/location to create generator for. Format: `projects/<Project ID>/locations/<Location ID>`  
`generator` | `[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)`  
Required. The generator to create.  
`generatorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the generator, which will become the final component of the generator's resource name. The generator ID must be compliant with the regression formula `[a-zA-Z][a-zA-Z0-9_-]*` with the characters length in range of [3,64]. If the field is not provided, an Id will be auto-generated. If the field is provided, the caller is responsible for

  1. the uniqueness of the ID, otherwise the request will be rejected.
  2. the consistency for whether to use custom ID or not under a project to better ensure uniqueness.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | The RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    Generator generator = new Generator();
    string generatorId = "";
    // Make the request
    Generator response = generatorsClient.CreateGenerator(parent, generator, generatorId);
    

### CreateGenerator(CreateGeneratorRequest, CallSettings)
    
    
    public virtual Generator CreateGenerator(CreateGeneratorRequest request, CallSettings callSettings = null)

Creates a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | The RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    CreateGeneratorRequest request = new CreateGeneratorRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Generator = new Generator(),
        GeneratorId = "",
    };
    // Make the request
    Generator response = generatorsClient.CreateGenerator(request);
    

### CreateGenerator(string, Generator, string, CallSettings)
    
    
    public virtual Generator CreateGenerator(string parent, Generator generator, string generatorId, CallSettings callSettings = null)

Creates a generator.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project/location to create generator for. Format: `projects/<Project ID>/locations/<Location ID>`  
`generator` | `[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)`  
Required. The generator to create.  
`generatorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the generator, which will become the final component of the generator's resource name. The generator ID must be compliant with the regression formula `[a-zA-Z][a-zA-Z0-9_-]*` with the characters length in range of [3,64]. If the field is not provided, an Id will be auto-generated. If the field is provided, the caller is responsible for

  1. the uniqueness of the ID, otherwise the request will be rejected.
  2. the consistency for whether to use custom ID or not under a project to better ensure uniqueness.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | The RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    Generator generator = new Generator();
    string generatorId = "";
    // Make the request
    Generator response = generatorsClient.CreateGenerator(parent, generator, generatorId);
    

### CreateGeneratorAsync(ProjectName, Generator, string, CallSettings)
    
    
    public virtual Task<Generator> CreateGeneratorAsync(ProjectName parent, Generator generator, string generatorId, CallSettings callSettings = null)

Creates a generator.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project/location to create generator for. Format: `projects/<Project ID>/locations/<Location ID>`  
`generator` | `[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)`  
Required. The generator to create.  
`generatorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the generator, which will become the final component of the generator's resource name. The generator ID must be compliant with the regression formula `[a-zA-Z][a-zA-Z0-9_-]*` with the characters length in range of [3,64]. If the field is not provided, an Id will be auto-generated. If the field is provided, the caller is responsible for

  1. the uniqueness of the ID, otherwise the request will be rejected.
  2. the consistency for whether to use custom ID or not under a project to better ensure uniqueness.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    Generator generator = new Generator();
    string generatorId = "";
    // Make the request
    Generator response = await generatorsClient.CreateGeneratorAsync(parent, generator, generatorId);
    

### CreateGeneratorAsync(ProjectName, Generator, string, CancellationToken)
    
    
    public virtual Task<Generator> CreateGeneratorAsync(ProjectName parent, Generator generator, string generatorId, CancellationToken cancellationToken)

Creates a generator.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project/location to create generator for. Format: `projects/<Project ID>/locations/<Location ID>`  
`generator` | `[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)`  
Required. The generator to create.  
`generatorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the generator, which will become the final component of the generator's resource name. The generator ID must be compliant with the regression formula `[a-zA-Z][a-zA-Z0-9_-]*` with the characters length in range of [3,64]. If the field is not provided, an Id will be auto-generated. If the field is provided, the caller is responsible for

  1. the uniqueness of the ID, otherwise the request will be rejected.
  2. the consistency for whether to use custom ID or not under a project to better ensure uniqueness.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    Generator generator = new Generator();
    string generatorId = "";
    // Make the request
    Generator response = await generatorsClient.CreateGeneratorAsync(parent, generator, generatorId);
    

### CreateGeneratorAsync(CreateGeneratorRequest, CallSettings)
    
    
    public virtual Task<Generator> CreateGeneratorAsync(CreateGeneratorRequest request, CallSettings callSettings = null)

Creates a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    CreateGeneratorRequest request = new CreateGeneratorRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Generator = new Generator(),
        GeneratorId = "",
    };
    // Make the request
    Generator response = await generatorsClient.CreateGeneratorAsync(request);
    

### CreateGeneratorAsync(CreateGeneratorRequest, CancellationToken)
    
    
    public virtual Task<Generator> CreateGeneratorAsync(CreateGeneratorRequest request, CancellationToken cancellationToken)

Creates a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    CreateGeneratorRequest request = new CreateGeneratorRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Generator = new Generator(),
        GeneratorId = "",
    };
    // Make the request
    Generator response = await generatorsClient.CreateGeneratorAsync(request);
    

### CreateGeneratorAsync(string, Generator, string, CallSettings)
    
    
    public virtual Task<Generator> CreateGeneratorAsync(string parent, Generator generator, string generatorId, CallSettings callSettings = null)

Creates a generator.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project/location to create generator for. Format: `projects/<Project ID>/locations/<Location ID>`  
`generator` | `[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)`  
Required. The generator to create.  
`generatorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the generator, which will become the final component of the generator's resource name. The generator ID must be compliant with the regression formula `[a-zA-Z][a-zA-Z0-9_-]*` with the characters length in range of [3,64]. If the field is not provided, an Id will be auto-generated. If the field is provided, the caller is responsible for

  1. the uniqueness of the ID, otherwise the request will be rejected.
  2. the consistency for whether to use custom ID or not under a project to better ensure uniqueness.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    Generator generator = new Generator();
    string generatorId = "";
    // Make the request
    Generator response = await generatorsClient.CreateGeneratorAsync(parent, generator, generatorId);
    

### CreateGeneratorAsync(string, Generator, string, CancellationToken)
    
    
    public virtual Task<Generator> CreateGeneratorAsync(string parent, Generator generator, string generatorId, CancellationToken cancellationToken)

Creates a generator.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project/location to create generator for. Format: `projects/<Project ID>/locations/<Location ID>`  
`generator` | `[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)`  
Required. The generator to create.  
`generatorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the generator, which will become the final component of the generator's resource name. The generator ID must be compliant with the regression formula `[a-zA-Z][a-zA-Z0-9_-]*` with the characters length in range of [3,64]. If the field is not provided, an Id will be auto-generated. If the field is provided, the caller is responsible for

  1. the uniqueness of the ID, otherwise the request will be rejected.
  2. the consistency for whether to use custom ID or not under a project to better ensure uniqueness.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    Generator generator = new Generator();
    string generatorId = "";
    // Make the request
    Generator response = await generatorsClient.CreateGeneratorAsync(parent, generator, generatorId);
    

### DeleteGenerator(DeleteGeneratorRequest, CallSettings)
    
    
    public virtual void DeleteGenerator(DeleteGeneratorRequest request, CallSettings callSettings = null)

Deletes a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.DeleteGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    DeleteGeneratorRequest request = new DeleteGeneratorRequest
    {
        GeneratorName = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]"),
    };
    // Make the request
    generatorsClient.DeleteGenerator(request);
    

### DeleteGenerator(GeneratorName, CallSettings)
    
    
    public virtual void DeleteGenerator(GeneratorName name, CallSettings callSettings = null)

Deletes a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GeneratorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorName)`  
Required. The generator resource name to delete. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    GeneratorName name = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]");
    // Make the request
    generatorsClient.DeleteGenerator(name);
    

### DeleteGenerator(string, CallSettings)
    
    
    public virtual void DeleteGenerator(string name, CallSettings callSettings = null)

Deletes a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The generator resource name to delete. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/generators/[GENERATOR]";
    // Make the request
    generatorsClient.DeleteGenerator(name);
    

### DeleteGeneratorAsync(DeleteGeneratorRequest, CallSettings)
    
    
    public virtual Task DeleteGeneratorAsync(DeleteGeneratorRequest request, CallSettings callSettings = null)

Deletes a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.DeleteGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteGeneratorRequest request = new DeleteGeneratorRequest
    {
        GeneratorName = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]"),
    };
    // Make the request
    await generatorsClient.DeleteGeneratorAsync(request);
    

### DeleteGeneratorAsync(DeleteGeneratorRequest, CancellationToken)
    
    
    public virtual Task DeleteGeneratorAsync(DeleteGeneratorRequest request, CancellationToken cancellationToken)

Deletes a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.DeleteGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteGeneratorRequest request = new DeleteGeneratorRequest
    {
        GeneratorName = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]"),
    };
    // Make the request
    await generatorsClient.DeleteGeneratorAsync(request);
    

### DeleteGeneratorAsync(GeneratorName, CallSettings)
    
    
    public virtual Task DeleteGeneratorAsync(GeneratorName name, CallSettings callSettings = null)

Deletes a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GeneratorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorName)`  
Required. The generator resource name to delete. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    GeneratorName name = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]");
    // Make the request
    await generatorsClient.DeleteGeneratorAsync(name);
    

### DeleteGeneratorAsync(GeneratorName, CancellationToken)
    
    
    public virtual Task DeleteGeneratorAsync(GeneratorName name, CancellationToken cancellationToken)

Deletes a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GeneratorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorName)`  
Required. The generator resource name to delete. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    GeneratorName name = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]");
    // Make the request
    await generatorsClient.DeleteGeneratorAsync(name);
    

### DeleteGeneratorAsync(string, CallSettings)
    
    
    public virtual Task DeleteGeneratorAsync(string name, CallSettings callSettings = null)

Deletes a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The generator resource name to delete. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/generators/[GENERATOR]";
    // Make the request
    await generatorsClient.DeleteGeneratorAsync(name);
    

### DeleteGeneratorAsync(string, CancellationToken)
    
    
    public virtual Task DeleteGeneratorAsync(string name, CancellationToken cancellationToken)

Deletes a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The generator resource name to delete. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/generators/[GENERATOR]";
    // Make the request
    await generatorsClient.DeleteGeneratorAsync(name);
    

### GetGenerator(GeneratorName, CallSettings)
    
    
    public virtual Generator GetGenerator(GeneratorName name, CallSettings callSettings = null)

Retrieves a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GeneratorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorName)`  
Required. The generator resource name to retrieve. Format: `projects/<Project ID>/locations/<Location ID>`/generators/<Generator ID>`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | The RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    GeneratorName name = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]");
    // Make the request
    Generator response = generatorsClient.GetGenerator(name);
    

### GetGenerator(GetGeneratorRequest, CallSettings)
    
    
    public virtual Generator GetGenerator(GetGeneratorRequest request, CallSettings callSettings = null)

Retrieves a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | The RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    GetGeneratorRequest request = new GetGeneratorRequest
    {
        GeneratorName = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]"),
    };
    // Make the request
    Generator response = generatorsClient.GetGenerator(request);
    

### GetGenerator(string, CallSettings)
    
    
    public virtual Generator GetGenerator(string name, CallSettings callSettings = null)

Retrieves a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The generator resource name to retrieve. Format: `projects/<Project ID>/locations/<Location ID>`/generators/<Generator ID>`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | The RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/generators/[GENERATOR]";
    // Make the request
    Generator response = generatorsClient.GetGenerator(name);
    

### GetGeneratorAsync(GeneratorName, CallSettings)
    
    
    public virtual Task<Generator> GetGeneratorAsync(GeneratorName name, CallSettings callSettings = null)

Retrieves a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GeneratorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorName)`  
Required. The generator resource name to retrieve. Format: `projects/<Project ID>/locations/<Location ID>`/generators/<Generator ID>`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    GeneratorName name = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]");
    // Make the request
    Generator response = await generatorsClient.GetGeneratorAsync(name);
    

### GetGeneratorAsync(GeneratorName, CancellationToken)
    
    
    public virtual Task<Generator> GetGeneratorAsync(GeneratorName name, CancellationToken cancellationToken)

Retrieves a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GeneratorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorName)`  
Required. The generator resource name to retrieve. Format: `projects/<Project ID>/locations/<Location ID>`/generators/<Generator ID>`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    GeneratorName name = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]");
    // Make the request
    Generator response = await generatorsClient.GetGeneratorAsync(name);
    

### GetGeneratorAsync(GetGeneratorRequest, CallSettings)
    
    
    public virtual Task<Generator> GetGeneratorAsync(GetGeneratorRequest request, CallSettings callSettings = null)

Retrieves a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    GetGeneratorRequest request = new GetGeneratorRequest
    {
        GeneratorName = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]"),
    };
    // Make the request
    Generator response = await generatorsClient.GetGeneratorAsync(request);
    

### GetGeneratorAsync(GetGeneratorRequest, CancellationToken)
    
    
    public virtual Task<Generator> GetGeneratorAsync(GetGeneratorRequest request, CancellationToken cancellationToken)

Retrieves a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    GetGeneratorRequest request = new GetGeneratorRequest
    {
        GeneratorName = GeneratorName.FromProjectLocationGenerator("[PROJECT]", "[LOCATION]", "[GENERATOR]"),
    };
    // Make the request
    Generator response = await generatorsClient.GetGeneratorAsync(request);
    

### GetGeneratorAsync(string, CallSettings)
    
    
    public virtual Task<Generator> GetGeneratorAsync(string name, CallSettings callSettings = null)

Retrieves a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The generator resource name to retrieve. Format: `projects/<Project ID>/locations/<Location ID>`/generators/<Generator ID>`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/generators/[GENERATOR]";
    // Make the request
    Generator response = await generatorsClient.GetGeneratorAsync(name);
    

### GetGeneratorAsync(string, CancellationToken)
    
    
    public virtual Task<Generator> GetGeneratorAsync(string name, CancellationToken cancellationToken)

Retrieves a generator.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The generator resource name to retrieve. Format: `projects/<Project ID>/locations/<Location ID>`/generators/<Generator ID>`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/generators/[GENERATOR]";
    // Make the request
    Generator response = await generatorsClient.GetGeneratorAsync(name);
    

### ListGenerators(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListGeneratorsResponse, Generator> ListGenerators(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists generators.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project/location to list generators for. Format: `projects/<Project ID>/locations/<Location ID>`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGeneratorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListGeneratorsResponse)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A pageable sequence of [Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator) resources.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedEnumerable<ListGeneratorsResponse, Generator> response = generatorsClient.ListGenerators(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Generator item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGeneratorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Generator item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Generator> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Generator item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGenerators(ListGeneratorsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListGeneratorsResponse, Generator> ListGenerators(ListGeneratorsRequest request, CallSettings callSettings = null)

Lists generators.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGeneratorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListGeneratorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGeneratorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListGeneratorsResponse)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A pageable sequence of [Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator) resources.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    ListGeneratorsRequest request = new ListGeneratorsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    PagedEnumerable<ListGeneratorsResponse, Generator> response = generatorsClient.ListGenerators(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Generator item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGeneratorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Generator item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Generator> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Generator item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGenerators(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListGeneratorsResponse, Generator> ListGenerators(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists generators.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project/location to list generators for. Format: `projects/<Project ID>/locations/<Location ID>`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGeneratorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListGeneratorsResponse)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A pageable sequence of [Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator) resources.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedEnumerable<ListGeneratorsResponse, Generator> response = generatorsClient.ListGenerators(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Generator item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGeneratorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Generator item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Generator> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Generator item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGeneratorsAsync(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGeneratorsResponse, Generator> ListGeneratorsAsync(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists generators.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project/location to list generators for. Format: `projects/<Project ID>/locations/<Location ID>`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGeneratorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListGeneratorsResponse)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A pageable asynchronous sequence of [Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator) resources.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedAsyncEnumerable<ListGeneratorsResponse, Generator> response = generatorsClient.ListGeneratorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Generator item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGeneratorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Generator item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Generator> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Generator item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGeneratorsAsync(ListGeneratorsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGeneratorsResponse, Generator> ListGeneratorsAsync(ListGeneratorsRequest request, CallSettings callSettings = null)

Lists generators.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGeneratorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListGeneratorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGeneratorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListGeneratorsResponse)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A pageable asynchronous sequence of [Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator) resources.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    ListGeneratorsRequest request = new ListGeneratorsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListGeneratorsResponse, Generator> response = generatorsClient.ListGeneratorsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Generator item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGeneratorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Generator item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Generator> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Generator item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGeneratorsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGeneratorsResponse, Generator> ListGeneratorsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists generators.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project/location to list generators for. Format: `projects/<Project ID>/locations/<Location ID>`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGeneratorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListGeneratorsResponse)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A pageable asynchronous sequence of [Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator) resources.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedAsyncEnumerable<ListGeneratorsResponse, Generator> response = generatorsClient.ListGeneratorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Generator item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGeneratorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Generator item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Generator> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Generator item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient#Google_Cloud_Dialogflow_V2Beta1_GeneratorsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient#Google_Cloud_Dialogflow_V2Beta1_GeneratorsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient#Google_Cloud_Dialogflow_V2Beta1_GeneratorsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorsClient#Google_Cloud_Dialogflow_V2Beta1_GeneratorsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateGenerator(Generator, FieldMask, CallSettings)
    
    
    public virtual Generator UpdateGenerator(Generator generator, FieldMask updateMask, CallSettings callSettings = null)

Updates a generator.

**Parameters**  
---  
**Name** | **Description**  
`generator` | `[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)`  
Required. The generator to update. The name field of generator is to identify the generator to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | The RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    Generator generator = new Generator();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Generator response = generatorsClient.UpdateGenerator(generator, updateMask);
    

### UpdateGenerator(UpdateGeneratorRequest, CallSettings)
    
    
    public virtual Generator UpdateGenerator(UpdateGeneratorRequest request, CallSettings callSettings = null)

Updates a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.UpdateGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | The RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = GeneratorsClient.Create();
    // Initialize request argument(s)
    UpdateGeneratorRequest request = new UpdateGeneratorRequest
    {
        Generator = new Generator(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Generator response = generatorsClient.UpdateGenerator(request);
    

### UpdateGeneratorAsync(Generator, FieldMask, CallSettings)
    
    
    public virtual Task<Generator> UpdateGeneratorAsync(Generator generator, FieldMask updateMask, CallSettings callSettings = null)

Updates a generator.

**Parameters**  
---  
**Name** | **Description**  
`generator` | `[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)`  
Required. The generator to update. The name field of generator is to identify the generator to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    Generator generator = new Generator();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Generator response = await generatorsClient.UpdateGeneratorAsync(generator, updateMask);
    

### UpdateGeneratorAsync(Generator, FieldMask, CancellationToken)
    
    
    public virtual Task<Generator> UpdateGeneratorAsync(Generator generator, FieldMask updateMask, CancellationToken cancellationToken)

Updates a generator.

**Parameters**  
---  
**Name** | **Description**  
`generator` | `[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)`  
Required. The generator to update. The name field of generator is to identify the generator to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    Generator generator = new Generator();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Generator response = await generatorsClient.UpdateGeneratorAsync(generator, updateMask);
    

### UpdateGeneratorAsync(UpdateGeneratorRequest, CallSettings)
    
    
    public virtual Task<Generator> UpdateGeneratorAsync(UpdateGeneratorRequest request, CallSettings callSettings = null)

Updates a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.UpdateGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGeneratorRequest request = new UpdateGeneratorRequest
    {
        Generator = new Generator(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Generator response = await generatorsClient.UpdateGeneratorAsync(request);
    

### UpdateGeneratorAsync(UpdateGeneratorRequest, CancellationToken)
    
    
    public virtual Task<Generator> UpdateGeneratorAsync(UpdateGeneratorRequest request, CancellationToken cancellationToken)

Updates a generator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.UpdateGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Generator)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GeneratorsClient generatorsClient = await GeneratorsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGeneratorRequest request = new UpdateGeneratorRequest
    {
        Generator = new Generator(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Generator response = await generatorsClient.UpdateGeneratorAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
