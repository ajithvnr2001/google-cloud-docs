---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient
title: Vertex AI v1beta1 API - Class ModelGardenServiceClient (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:47.338846+00:00
---

# Vertex AI v1beta1 API - Class ModelGardenServiceClient (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ModelGardenServiceClient (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public abstract class ModelGardenServiceClient

Reference documentation and code samples for the Vertex AI v1beta1 API class ModelGardenServiceClient.

ModelGardenService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ModelGardenServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ModelGardenServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClientImpl)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Remarks

The interface of Model Garden Service.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ModelGardenService service, which is a host of "aiplatform.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ModelGardenService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ModelGardenService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeployOperationsClient
    
    
    public virtual OperationsClient DeployOperationsClient { get; }

The long-running operations client for `Deploy`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeployPublisherModelOperationsClient
    
    
    public virtual OperationsClient DeployPublisherModelOperationsClient { get; }

The long-running operations client for `DeployPublisherModel`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ExportPublisherModelOperationsClient
    
    
    public virtual OperationsClient ExportPublisherModelOperationsClient { get; }

The long-running operations client for `ExportPublisherModel`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual ModelGardenService.ModelGardenServiceClient GrpcClient { get; }

The underlying gRPC ModelGardenService client

**Property Value**  
---  
**Type** | **Description**  
`[ModelGardenService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenService)[ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenService.ModelGardenServiceClient)` |   
  
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

### AcceptPublisherModelEula(ProjectName, PublisherModelName, CallSettings)
    
    
    public virtual PublisherModelEulaAcceptance AcceptPublisherModelEula(ProjectName parent, PublisherModelName publisherModel, CallSettings callSettings = null)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[PublisherModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelName)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    PublisherModelName publisherModel = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]");
    // Make the request
    PublisherModelEulaAcceptance response = modelGardenServiceClient.AcceptPublisherModelEula(parent, publisherModel);
    

### AcceptPublisherModelEula(AcceptPublisherModelEulaRequest, CallSettings)
    
    
    public virtual PublisherModelEulaAcceptance AcceptPublisherModelEula(AcceptPublisherModelEulaRequest request, CallSettings callSettings = null)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptPublisherModelEulaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AcceptPublisherModelEulaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    AcceptPublisherModelEulaRequest request = new AcceptPublisherModelEulaRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        PublisherModelAsPublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
    };
    // Make the request
    PublisherModelEulaAcceptance response = modelGardenServiceClient.AcceptPublisherModelEula(request);
    

### AcceptPublisherModelEula(string, string, CallSettings)
    
    
    public virtual PublisherModelEulaAcceptance AcceptPublisherModelEula(string parent, string publisherModel, CallSettings callSettings = null)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    string publisherModel = "publishers/[PUBLISHER]/models/[MODEL]";
    // Make the request
    PublisherModelEulaAcceptance response = modelGardenServiceClient.AcceptPublisherModelEula(parent, publisherModel);
    

### AcceptPublisherModelEulaAsync(ProjectName, PublisherModelName, CallSettings)
    
    
    public virtual Task<PublisherModelEulaAcceptance> AcceptPublisherModelEulaAsync(ProjectName parent, PublisherModelName publisherModel, CallSettings callSettings = null)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[PublisherModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelName)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    PublisherModelName publisherModel = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]");
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.AcceptPublisherModelEulaAsync(parent, publisherModel);
    

### AcceptPublisherModelEulaAsync(ProjectName, PublisherModelName, CancellationToken)
    
    
    public virtual Task<PublisherModelEulaAcceptance> AcceptPublisherModelEulaAsync(ProjectName parent, PublisherModelName publisherModel, CancellationToken cancellationToken)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[PublisherModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelName)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    PublisherModelName publisherModel = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]");
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.AcceptPublisherModelEulaAsync(parent, publisherModel);
    

### AcceptPublisherModelEulaAsync(AcceptPublisherModelEulaRequest, CallSettings)
    
    
    public virtual Task<PublisherModelEulaAcceptance> AcceptPublisherModelEulaAsync(AcceptPublisherModelEulaRequest request, CallSettings callSettings = null)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptPublisherModelEulaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AcceptPublisherModelEulaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    AcceptPublisherModelEulaRequest request = new AcceptPublisherModelEulaRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        PublisherModelAsPublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
    };
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.AcceptPublisherModelEulaAsync(request);
    

### AcceptPublisherModelEulaAsync(AcceptPublisherModelEulaRequest, CancellationToken)
    
    
    public virtual Task<PublisherModelEulaAcceptance> AcceptPublisherModelEulaAsync(AcceptPublisherModelEulaRequest request, CancellationToken cancellationToken)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptPublisherModelEulaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AcceptPublisherModelEulaRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    AcceptPublisherModelEulaRequest request = new AcceptPublisherModelEulaRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        PublisherModelAsPublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
    };
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.AcceptPublisherModelEulaAsync(request);
    

### AcceptPublisherModelEulaAsync(string, string, CallSettings)
    
    
    public virtual Task<PublisherModelEulaAcceptance> AcceptPublisherModelEulaAsync(string parent, string publisherModel, CallSettings callSettings = null)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    string publisherModel = "publishers/[PUBLISHER]/models/[MODEL]";
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.AcceptPublisherModelEulaAsync(parent, publisherModel);
    

### AcceptPublisherModelEulaAsync(string, string, CancellationToken)
    
    
    public virtual Task<PublisherModelEulaAcceptance> AcceptPublisherModelEulaAsync(string parent, string publisherModel, CancellationToken cancellationToken)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    string publisherModel = "publishers/[PUBLISHER]/models/[MODEL]";
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.AcceptPublisherModelEulaAsync(parent, publisherModel);
    

### CheckPublisherModelEulaAcceptance(ProjectName, PublisherModelName, CallSettings)
    
    
    public virtual PublisherModelEulaAcceptance CheckPublisherModelEulaAcceptance(ProjectName parent, PublisherModelName publisherModel, CallSettings callSettings = null)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[PublisherModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelName)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    PublisherModelName publisherModel = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]");
    // Make the request
    PublisherModelEulaAcceptance response = modelGardenServiceClient.CheckPublisherModelEulaAcceptance(parent, publisherModel);
    

### CheckPublisherModelEulaAcceptance(CheckPublisherModelEulaAcceptanceRequest, CallSettings)
    
    
    public virtual PublisherModelEulaAcceptance CheckPublisherModelEulaAcceptance(CheckPublisherModelEulaAcceptanceRequest request, CallSettings callSettings = null)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckPublisherModelEulaAcceptanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CheckPublisherModelEulaAcceptanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    CheckPublisherModelEulaAcceptanceRequest request = new CheckPublisherModelEulaAcceptanceRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        PublisherModelAsPublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
    };
    // Make the request
    PublisherModelEulaAcceptance response = modelGardenServiceClient.CheckPublisherModelEulaAcceptance(request);
    

### CheckPublisherModelEulaAcceptance(string, string, CallSettings)
    
    
    public virtual PublisherModelEulaAcceptance CheckPublisherModelEulaAcceptance(string parent, string publisherModel, CallSettings callSettings = null)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    string publisherModel = "publishers/[PUBLISHER]/models/[MODEL]";
    // Make the request
    PublisherModelEulaAcceptance response = modelGardenServiceClient.CheckPublisherModelEulaAcceptance(parent, publisherModel);
    

### CheckPublisherModelEulaAcceptanceAsync(ProjectName, PublisherModelName, CallSettings)
    
    
    public virtual Task<PublisherModelEulaAcceptance> CheckPublisherModelEulaAcceptanceAsync(ProjectName parent, PublisherModelName publisherModel, CallSettings callSettings = null)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[PublisherModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelName)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    PublisherModelName publisherModel = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]");
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.CheckPublisherModelEulaAcceptanceAsync(parent, publisherModel);
    

### CheckPublisherModelEulaAcceptanceAsync(ProjectName, PublisherModelName, CancellationToken)
    
    
    public virtual Task<PublisherModelEulaAcceptance> CheckPublisherModelEulaAcceptanceAsync(ProjectName parent, PublisherModelName publisherModel, CancellationToken cancellationToken)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[PublisherModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelName)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    PublisherModelName publisherModel = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]");
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.CheckPublisherModelEulaAcceptanceAsync(parent, publisherModel);
    

### CheckPublisherModelEulaAcceptanceAsync(CheckPublisherModelEulaAcceptanceRequest, CallSettings)
    
    
    public virtual Task<PublisherModelEulaAcceptance> CheckPublisherModelEulaAcceptanceAsync(CheckPublisherModelEulaAcceptanceRequest request, CallSettings callSettings = null)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckPublisherModelEulaAcceptanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CheckPublisherModelEulaAcceptanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    CheckPublisherModelEulaAcceptanceRequest request = new CheckPublisherModelEulaAcceptanceRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        PublisherModelAsPublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
    };
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.CheckPublisherModelEulaAcceptanceAsync(request);
    

### CheckPublisherModelEulaAcceptanceAsync(CheckPublisherModelEulaAcceptanceRequest, CancellationToken)
    
    
    public virtual Task<PublisherModelEulaAcceptance> CheckPublisherModelEulaAcceptanceAsync(CheckPublisherModelEulaAcceptanceRequest request, CancellationToken cancellationToken)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckPublisherModelEulaAcceptanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CheckPublisherModelEulaAcceptanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    CheckPublisherModelEulaAcceptanceRequest request = new CheckPublisherModelEulaAcceptanceRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        PublisherModelAsPublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
    };
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.CheckPublisherModelEulaAcceptanceAsync(request);
    

### CheckPublisherModelEulaAcceptanceAsync(string, string, CallSettings)
    
    
    public virtual Task<PublisherModelEulaAcceptance> CheckPublisherModelEulaAcceptanceAsync(string parent, string publisherModel, CallSettings callSettings = null)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    string publisherModel = "publishers/[PUBLISHER]/models/[MODEL]";
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.CheckPublisherModelEulaAcceptanceAsync(parent, publisherModel);
    

### CheckPublisherModelEulaAcceptanceAsync(string, string, CancellationToken)
    
    
    public virtual Task<PublisherModelEulaAcceptance> CheckPublisherModelEulaAcceptanceAsync(string parent, string publisherModel, CancellationToken cancellationToken)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project requesting access for named model. The format is `projects/{project}`.  
`publisherModel` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    string publisherModel = "publishers/[PUBLISHER]/models/[MODEL]";
    // Make the request
    PublisherModelEulaAcceptance response = await modelGardenServiceClient.CheckPublisherModelEulaAcceptanceAsync(parent, publisherModel);
    

### Create()
    
    
    public static ModelGardenServiceClient Create()

Synchronously creates a [ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ModelGardenServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClientBuilder) .

**Returns**  
---  
**Type** | **Description**  
`[ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient)` | The created [ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ModelGardenServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ModelGardenServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClientBuilder) .

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient)` | The task representing the created [ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient).  
  
### Deploy(DeployRequest, CallSettings)
    
    
    public virtual Operation<DeployResponse, DeployOperationMetadata> Deploy(DeployRequest request, CallSettings callSettings = null)

Deploys a model to a new endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployResponse)[DeployOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    DeployRequest request = new DeployRequest
    {
        PublisherModelNameAsPublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
        DestinationAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ModelConfig = new DeployRequest.Types.ModelConfig(),
        EndpointConfig = new DeployRequest.Types.EndpointConfig(),
        DeployConfig = new DeployRequest.Types.DeployConfig(),
    };
    // Make the request
    Operation<DeployResponse, DeployOperationMetadata> response = modelGardenServiceClient.Deploy(request);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployResponse, DeployOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    DeployResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployResponse, DeployOperationMetadata> retrievedResponse = modelGardenServiceClient.PollOnceDeploy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployAsync(DeployRequest, CallSettings)
    
    
    public virtual Task<Operation<DeployResponse, DeployOperationMetadata>> DeployAsync(DeployRequest request, CallSettings callSettings = null)

Deploys a model to a new endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployResponse)[DeployOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeployRequest request = new DeployRequest
    {
        PublisherModelNameAsPublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
        DestinationAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ModelConfig = new DeployRequest.Types.ModelConfig(),
        EndpointConfig = new DeployRequest.Types.EndpointConfig(),
        DeployConfig = new DeployRequest.Types.DeployConfig(),
    };
    // Make the request
    Operation<DeployResponse, DeployOperationMetadata> response = await modelGardenServiceClient.DeployAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployResponse, DeployOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DeployResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployResponse, DeployOperationMetadata> retrievedResponse = await modelGardenServiceClient.PollOnceDeployAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployAsync(DeployRequest, CancellationToken)
    
    
    public virtual Task<Operation<DeployResponse, DeployOperationMetadata>> DeployAsync(DeployRequest request, CancellationToken cancellationToken)

Deploys a model to a new endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployResponse)[DeployOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeployRequest request = new DeployRequest
    {
        PublisherModelNameAsPublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
        DestinationAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ModelConfig = new DeployRequest.Types.ModelConfig(),
        EndpointConfig = new DeployRequest.Types.EndpointConfig(),
        DeployConfig = new DeployRequest.Types.DeployConfig(),
    };
    // Make the request
    Operation<DeployResponse, DeployOperationMetadata> response = await modelGardenServiceClient.DeployAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployResponse, DeployOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DeployResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployResponse, DeployOperationMetadata> retrievedResponse = await modelGardenServiceClient.PollOnceDeployAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployPublisherModel(DeployPublisherModelRequest, CallSettings)
    
    
    [Obsolete]
    public virtual Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> DeployPublisherModel(DeployPublisherModelRequest request, CallSettings callSettings = null)

Deploys publisher models.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelResponse)[DeployPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelOperationMetadata)` | The RPC response.  
**Example**
    
    
                // Create client
                ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
                // Initialize request argument(s)
    #pragma warning disable CS0612
                DeployPublisherModelRequest request = new DeployPublisherModelRequest { };
    #pragma warning restore CS0612
                // Make the request
    #pragma warning disable CS0612
                Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> response = modelGardenServiceClient.DeployPublisherModel(request);
    #pragma warning restore CS0612
    
                // Poll until the returned long-running operation is complete
    #pragma warning disable CS0612
                Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> completedResponse = response.PollUntilCompleted();
    #pragma warning restore CS0612
                // Retrieve the operation result
    #pragma warning disable CS0612
                DeployPublisherModelResponse result = completedResponse.Result;
    #pragma warning restore CS0612
    
                // Or get the name of the operation
                string operationName = response.Name;
                // This name can be stored, then the long-running operation retrieved later by name
    #pragma warning disable CS0612
                Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> retrievedResponse = modelGardenServiceClient.PollOnceDeployPublisherModel(operationName);
    #pragma warning restore CS0612
                // Check if the retrieved long-running operation has completed
                if (retrievedResponse.IsCompleted)
                {
                    // If it has completed, then access the result
    #pragma warning disable CS0612
                    DeployPublisherModelResponse retrievedResult = retrievedResponse.Result;
    #pragma warning restore CS0612
                }
    

### DeployPublisherModelAsync(DeployPublisherModelRequest, CallSettings)
    
    
    [Obsolete]
    public virtual Task<Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata>> DeployPublisherModelAsync(DeployPublisherModelRequest request, CallSettings callSettings = null)

Deploys publisher models.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelResponse)[DeployPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
                // Initialize request argument(s)
    #pragma warning disable CS0612
                DeployPublisherModelRequest request = new DeployPublisherModelRequest { };
    #pragma warning restore CS0612
                // Make the request
    #pragma warning disable CS0612
                Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> response = await modelGardenServiceClient.DeployPublisherModelAsync(request);
    #pragma warning restore CS0612
    
                // Poll until the returned long-running operation is complete
    #pragma warning disable CS0612
                Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    #pragma warning restore CS0612
                // Retrieve the operation result
    #pragma warning disable CS0612
                DeployPublisherModelResponse result = completedResponse.Result;
    #pragma warning restore CS0612
    
                // Or get the name of the operation
                string operationName = response.Name;
                // This name can be stored, then the long-running operation retrieved later by name
    #pragma warning disable CS0612
                Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> retrievedResponse = await modelGardenServiceClient.PollOnceDeployPublisherModelAsync(operationName);
    #pragma warning restore CS0612
                // Check if the retrieved long-running operation has completed
                if (retrievedResponse.IsCompleted)
                {
                    // If it has completed, then access the result
    #pragma warning disable CS0612
                    DeployPublisherModelResponse retrievedResult = retrievedResponse.Result;
    #pragma warning restore CS0612
                }
    

### DeployPublisherModelAsync(DeployPublisherModelRequest, CancellationToken)
    
    
    [Obsolete]
    public virtual Task<Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata>> DeployPublisherModelAsync(DeployPublisherModelRequest request, CancellationToken cancellationToken)

Deploys publisher models.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelResponse)[DeployPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
                // Initialize request argument(s)
    #pragma warning disable CS0612
                DeployPublisherModelRequest request = new DeployPublisherModelRequest { };
    #pragma warning restore CS0612
                // Make the request
    #pragma warning disable CS0612
                Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> response = await modelGardenServiceClient.DeployPublisherModelAsync(request);
    #pragma warning restore CS0612
    
                // Poll until the returned long-running operation is complete
    #pragma warning disable CS0612
                Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    #pragma warning restore CS0612
                // Retrieve the operation result
    #pragma warning disable CS0612
                DeployPublisherModelResponse result = completedResponse.Result;
    #pragma warning restore CS0612
    
                // Or get the name of the operation
                string operationName = response.Name;
                // This name can be stored, then the long-running operation retrieved later by name
    #pragma warning disable CS0612
                Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> retrievedResponse = await modelGardenServiceClient.PollOnceDeployPublisherModelAsync(operationName);
    #pragma warning restore CS0612
                // Check if the retrieved long-running operation has completed
                if (retrievedResponse.IsCompleted)
                {
                    // If it has completed, then access the result
    #pragma warning disable CS0612
                    DeployPublisherModelResponse retrievedResult = retrievedResponse.Result;
    #pragma warning restore CS0612
                }
    

### ExportPublisherModel(ExportPublisherModelRequest, CallSettings)
    
    
    public virtual Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> ExportPublisherModel(ExportPublisherModelRequest request, CallSettings callSettings = null)

Exports a publisher model to a user provided Google Cloud Storage bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelResponse)[ExportPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    ExportPublisherModelRequest request = new ExportPublisherModelRequest
    {
        Name = "",
        Destination = new GcsDestination(),
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> response = modelGardenServiceClient.ExportPublisherModel(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportPublisherModelResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> retrievedResponse = modelGardenServiceClient.PollOnceExportPublisherModel(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportPublisherModelResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportPublisherModelAsync(ExportPublisherModelRequest, CallSettings)
    
    
    public virtual Task<Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata>> ExportPublisherModelAsync(ExportPublisherModelRequest request, CallSettings callSettings = null)

Exports a publisher model to a user provided Google Cloud Storage bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelResponse)[ExportPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    ExportPublisherModelRequest request = new ExportPublisherModelRequest
    {
        Name = "",
        Destination = new GcsDestination(),
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> response = await modelGardenServiceClient.ExportPublisherModelAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportPublisherModelResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> retrievedResponse = await modelGardenServiceClient.PollOnceExportPublisherModelAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportPublisherModelResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportPublisherModelAsync(ExportPublisherModelRequest, CancellationToken)
    
    
    public virtual Task<Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata>> ExportPublisherModelAsync(ExportPublisherModelRequest request, CancellationToken cancellationToken)

Exports a publisher model to a user provided Google Cloud Storage bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelResponse)[ExportPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    ExportPublisherModelRequest request = new ExportPublisherModelRequest
    {
        Name = "",
        Destination = new GcsDestination(),
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> response = await modelGardenServiceClient.ExportPublisherModelAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportPublisherModelResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> retrievedResponse = await modelGardenServiceClient.PollOnceExportPublisherModelAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportPublisherModelResponse retrievedResult = retrievedResponse.Result;
    }
    

### GetPublisherModel(GetPublisherModelRequest, CallSettings)
    
    
    public virtual PublisherModel GetPublisherModel(GetPublisherModelRequest request, CallSettings callSettings = null)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetPublisherModelRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    GetPublisherModelRequest request = new GetPublisherModelRequest
    {
        PublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
        LanguageCode = "",
        View = PublisherModelView.Unspecified,
        IsHuggingFaceModel = false,
        HuggingFaceToken = "",
        IncludeEquivalentModelGardenModelDeploymentConfigs = false,
    };
    // Make the request
    PublisherModel response = modelGardenServiceClient.GetPublisherModel(request);
    

### GetPublisherModel(PublisherModelName, CallSettings)
    
    
    public virtual PublisherModel GetPublisherModel(PublisherModelName name, CallSettings callSettings = null)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PublisherModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelName)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    PublisherModelName name = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]");
    // Make the request
    PublisherModel response = modelGardenServiceClient.GetPublisherModel(name);
    

### GetPublisherModel(string, CallSettings)
    
    
    public virtual PublisherModel GetPublisherModel(string name, CallSettings callSettings = null)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    string name = "publishers/[PUBLISHER]/models/[MODEL]";
    // Make the request
    PublisherModel response = modelGardenServiceClient.GetPublisherModel(name);
    

### GetPublisherModelAsync(GetPublisherModelRequest, CallSettings)
    
    
    public virtual Task<PublisherModel> GetPublisherModelAsync(GetPublisherModelRequest request, CallSettings callSettings = null)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetPublisherModelRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetPublisherModelRequest request = new GetPublisherModelRequest
    {
        PublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
        LanguageCode = "",
        View = PublisherModelView.Unspecified,
        IsHuggingFaceModel = false,
        HuggingFaceToken = "",
        IncludeEquivalentModelGardenModelDeploymentConfigs = false,
    };
    // Make the request
    PublisherModel response = await modelGardenServiceClient.GetPublisherModelAsync(request);
    

### GetPublisherModelAsync(GetPublisherModelRequest, CancellationToken)
    
    
    public virtual Task<PublisherModel> GetPublisherModelAsync(GetPublisherModelRequest request, CancellationToken cancellationToken)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetPublisherModelRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetPublisherModelRequest request = new GetPublisherModelRequest
    {
        PublisherModelName = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]"),
        LanguageCode = "",
        View = PublisherModelView.Unspecified,
        IsHuggingFaceModel = false,
        HuggingFaceToken = "",
        IncludeEquivalentModelGardenModelDeploymentConfigs = false,
    };
    // Make the request
    PublisherModel response = await modelGardenServiceClient.GetPublisherModelAsync(request);
    

### GetPublisherModelAsync(PublisherModelName, CallSettings)
    
    
    public virtual Task<PublisherModel> GetPublisherModelAsync(PublisherModelName name, CallSettings callSettings = null)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PublisherModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelName)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    PublisherModelName name = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]");
    // Make the request
    PublisherModel response = await modelGardenServiceClient.GetPublisherModelAsync(name);
    

### GetPublisherModelAsync(PublisherModelName, CancellationToken)
    
    
    public virtual Task<PublisherModel> GetPublisherModelAsync(PublisherModelName name, CancellationToken cancellationToken)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PublisherModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelName)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    PublisherModelName name = PublisherModelName.FromPublisherModel("[PUBLISHER]", "[MODEL]");
    // Make the request
    PublisherModel response = await modelGardenServiceClient.GetPublisherModelAsync(name);
    

### GetPublisherModelAsync(string, CallSettings)
    
    
    public virtual Task<PublisherModel> GetPublisherModelAsync(string name, CallSettings callSettings = null)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "publishers/[PUBLISHER]/models/[MODEL]";
    // Make the request
    PublisherModel response = await modelGardenServiceClient.GetPublisherModelAsync(name);
    

### GetPublisherModelAsync(string, CancellationToken)
    
    
    public virtual Task<PublisherModel> GetPublisherModelAsync(string name, CancellationToken cancellationToken)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "publishers/[PUBLISHER]/models/[MODEL]";
    // Make the request
    PublisherModel response = await modelGardenServiceClient.GetPublisherModelAsync(name);
    

### ListPublisherModels(ListPublisherModelsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListPublisherModelsResponse, PublisherModel> ListPublisherModels(ListPublisherModelsRequest request, CallSettings callSettings = null)

Lists publisher models in Model Garden.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPublisherModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListPublisherModelsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPublisherModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListPublisherModelsResponse)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A pageable sequence of [PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel) resources.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    ListPublisherModelsRequest request = new ListPublisherModelsRequest
    {
        Parent = "",
        Filter = "",
        View = PublisherModelView.Unspecified,
        OrderBy = "",
        LanguageCode = "",
        ListAllVersions = false,
    };
    // Make the request
    PagedEnumerable<ListPublisherModelsResponse, PublisherModel> response = modelGardenServiceClient.ListPublisherModels(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PublisherModel item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListPublisherModelsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PublisherModel item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PublisherModel> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PublisherModel item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPublisherModels(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListPublisherModelsResponse, PublisherModel> ListPublisherModels(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists publisher models in Model Garden.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Publisher from which to list the PublisherModels. Format: `publishers/{publisher}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPublisherModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListPublisherModelsResponse)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A pageable sequence of [PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel) resources.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = ModelGardenServiceClient.Create();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedEnumerable<ListPublisherModelsResponse, PublisherModel> response = modelGardenServiceClient.ListPublisherModels(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PublisherModel item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListPublisherModelsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PublisherModel item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PublisherModel> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PublisherModel item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPublisherModelsAsync(ListPublisherModelsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPublisherModelsResponse, PublisherModel> ListPublisherModelsAsync(ListPublisherModelsRequest request, CallSettings callSettings = null)

Lists publisher models in Model Garden.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPublisherModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListPublisherModelsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPublisherModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListPublisherModelsResponse)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A pageable asynchronous sequence of [PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel) resources.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListPublisherModelsRequest request = new ListPublisherModelsRequest
    {
        Parent = "",
        Filter = "",
        View = PublisherModelView.Unspecified,
        OrderBy = "",
        LanguageCode = "",
        ListAllVersions = false,
    };
    // Make the request
    PagedAsyncEnumerable<ListPublisherModelsResponse, PublisherModel> response = modelGardenServiceClient.ListPublisherModelsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (PublisherModel item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListPublisherModelsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PublisherModel item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PublisherModel> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PublisherModel item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPublisherModelsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPublisherModelsResponse, PublisherModel> ListPublisherModelsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists publisher models in Model Garden.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Publisher from which to list the PublisherModels. Format: `publishers/{publisher}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPublisherModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListPublisherModelsResponse)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | A pageable asynchronous sequence of [PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel) resources.  
**Example**
    
    
    // Create client
    ModelGardenServiceClient modelGardenServiceClient = await ModelGardenServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedAsyncEnumerable<ListPublisherModelsResponse, PublisherModel> response = modelGardenServiceClient.ListPublisherModelsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (PublisherModel item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListPublisherModelsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PublisherModel item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PublisherModel> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PublisherModel item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceDeploy(string, CallSettings)
    
    
    public virtual Operation<DeployResponse, DeployOperationMetadata> PollOnceDeploy(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Deploy`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployResponse)[DeployOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeployAsync(string, CallSettings)
    
    
    public virtual Task<Operation<DeployResponse, DeployOperationMetadata>> PollOnceDeployAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Deploy` .

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployResponse)[DeployOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeployPublisherModel(string, CallSettings)
    
    
    [Obsolete]
    public virtual Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata> PollOnceDeployPublisherModel(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeployPublisherModel` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelResponse)[DeployPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeployPublisherModelAsync(string, CallSettings)
    
    
    [Obsolete]
    public virtual Task<Operation<DeployPublisherModelResponse, DeployPublisherModelOperationMetadata>> PollOnceDeployPublisherModelAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeployPublisherModel`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelResponse)[DeployPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceExportPublisherModel(string, CallSettings)
    
    
    public virtual Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata> PollOnceExportPublisherModel(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ExportPublisherModel` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelResponse)[ExportPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelOperationMetadata)` | The result of polling the operation.  
  
### PollOnceExportPublisherModelAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ExportPublisherModelResponse, ExportPublisherModelOperationMetadata>> PollOnceExportPublisherModelAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ExportPublisherModel`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportPublisherModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelResponse)[ExportPublisherModelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelOperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient#Google_Cloud_AIPlatform_V1Beta1_ModelGardenServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient#Google_Cloud_AIPlatform_V1Beta1_ModelGardenServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient#Google_Cloud_AIPlatform_V1Beta1_ModelGardenServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient#Google_Cloud_AIPlatform_V1Beta1_ModelGardenServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
