---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient
title: Model Armor v1beta API - Class ModelArmorClient (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:28.910516+00:00
---

# Model Armor v1beta API - Class ModelArmorClient (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class ModelArmorClient (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public abstract class ModelArmorClient

Reference documentation and code samples for the Model Armor v1beta API class ModelArmorClient.

ModelArmor client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ModelArmorClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ModelArmorClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClientImpl)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Remarks

Service describing handlers for resources

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ModelArmor service, which is a host of "modelarmor.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ModelArmor scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ModelArmor scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual ModelArmor.ModelArmorClient GrpcClient { get; }

The underlying gRPC ModelArmor client

**Property Value**  
---  
**Type** | **Description**  
`[ModelArmor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor)[ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor.ModelArmorClient)` |   
  
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
    
    
    public static ModelArmorClient Create()

Synchronously creates a [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ModelArmorClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient)` | The created [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ModelArmorClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ModelArmorClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient)` | The task representing the created [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient).  
  
### CreateTemplate(LocationName, Template, string, CallSettings)
    
    
    public virtual Template CreateTemplate(LocationName parent, Template template, string templateId, CallSettings callSettings = null)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`template` | `[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)`  
Required. The resource being created  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and template_id from the method_signature of Create RPC  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Template template = new Template();
    string templateId = "";
    // Make the request
    Template response = modelArmorClient.CreateTemplate(parent, template, templateId);
    

### CreateTemplate(CreateTemplateRequest, CallSettings)
    
    
    public virtual Template CreateTemplate(CreateTemplateRequest request, CallSettings callSettings = null)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.CreateTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    CreateTemplateRequest request = new CreateTemplateRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        TemplateId = "",
        Template = new Template(),
        RequestId = "",
    };
    // Make the request
    Template response = modelArmorClient.CreateTemplate(request);
    

### CreateTemplate(string, Template, string, CallSettings)
    
    
    public virtual Template CreateTemplate(string parent, Template template, string templateId, CallSettings callSettings = null)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`template` | `[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)`  
Required. The resource being created  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and template_id from the method_signature of Create RPC  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Template template = new Template();
    string templateId = "";
    // Make the request
    Template response = modelArmorClient.CreateTemplate(parent, template, templateId);
    

### CreateTemplateAsync(LocationName, Template, string, CallSettings)
    
    
    public virtual Task<Template> CreateTemplateAsync(LocationName parent, Template template, string templateId, CallSettings callSettings = null)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`template` | `[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)`  
Required. The resource being created  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and template_id from the method_signature of Create RPC  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Template template = new Template();
    string templateId = "";
    // Make the request
    Template response = await modelArmorClient.CreateTemplateAsync(parent, template, templateId);
    

### CreateTemplateAsync(LocationName, Template, string, CancellationToken)
    
    
    public virtual Task<Template> CreateTemplateAsync(LocationName parent, Template template, string templateId, CancellationToken cancellationToken)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`template` | `[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)`  
Required. The resource being created  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and template_id from the method_signature of Create RPC  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Template template = new Template();
    string templateId = "";
    // Make the request
    Template response = await modelArmorClient.CreateTemplateAsync(parent, template, templateId);
    

### CreateTemplateAsync(CreateTemplateRequest, CallSettings)
    
    
    public virtual Task<Template> CreateTemplateAsync(CreateTemplateRequest request, CallSettings callSettings = null)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.CreateTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    CreateTemplateRequest request = new CreateTemplateRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        TemplateId = "",
        Template = new Template(),
        RequestId = "",
    };
    // Make the request
    Template response = await modelArmorClient.CreateTemplateAsync(request);
    

### CreateTemplateAsync(CreateTemplateRequest, CancellationToken)
    
    
    public virtual Task<Template> CreateTemplateAsync(CreateTemplateRequest request, CancellationToken cancellationToken)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.CreateTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    CreateTemplateRequest request = new CreateTemplateRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        TemplateId = "",
        Template = new Template(),
        RequestId = "",
    };
    // Make the request
    Template response = await modelArmorClient.CreateTemplateAsync(request);
    

### CreateTemplateAsync(string, Template, string, CallSettings)
    
    
    public virtual Task<Template> CreateTemplateAsync(string parent, Template template, string templateId, CallSettings callSettings = null)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`template` | `[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)`  
Required. The resource being created  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and template_id from the method_signature of Create RPC  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Template template = new Template();
    string templateId = "";
    // Make the request
    Template response = await modelArmorClient.CreateTemplateAsync(parent, template, templateId);
    

### CreateTemplateAsync(string, Template, string, CancellationToken)
    
    
    public virtual Task<Template> CreateTemplateAsync(string parent, Template template, string templateId, CancellationToken cancellationToken)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`template` | `[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)`  
Required. The resource being created  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and template_id from the method_signature of Create RPC  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Template template = new Template();
    string templateId = "";
    // Make the request
    Template response = await modelArmorClient.CreateTemplateAsync(parent, template, templateId);
    

### DeleteTemplate(DeleteTemplateRequest, CallSettings)
    
    
    public virtual void DeleteTemplate(DeleteTemplateRequest request, CallSettings callSettings = null)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DeleteTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    DeleteTemplateRequest request = new DeleteTemplateRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
        RequestId = "",
    };
    // Make the request
    modelArmorClient.DeleteTemplate(request);
    

### DeleteTemplate(TemplateName, CallSettings)
    
    
    public virtual void DeleteTemplate(TemplateName name, CallSettings callSettings = null)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.TemplateName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    TemplateName name = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]");
    // Make the request
    modelArmorClient.DeleteTemplate(name);
    

### DeleteTemplate(string, CallSettings)
    
    
    public virtual void DeleteTemplate(string name, CallSettings callSettings = null)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/templates/[TEMPLATE]";
    // Make the request
    modelArmorClient.DeleteTemplate(name);
    

### DeleteTemplateAsync(DeleteTemplateRequest, CallSettings)
    
    
    public virtual Task DeleteTemplateAsync(DeleteTemplateRequest request, CallSettings callSettings = null)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DeleteTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    DeleteTemplateRequest request = new DeleteTemplateRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
        RequestId = "",
    };
    // Make the request
    await modelArmorClient.DeleteTemplateAsync(request);
    

### DeleteTemplateAsync(DeleteTemplateRequest, CancellationToken)
    
    
    public virtual Task DeleteTemplateAsync(DeleteTemplateRequest request, CancellationToken cancellationToken)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DeleteTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    DeleteTemplateRequest request = new DeleteTemplateRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
        RequestId = "",
    };
    // Make the request
    await modelArmorClient.DeleteTemplateAsync(request);
    

### DeleteTemplateAsync(TemplateName, CallSettings)
    
    
    public virtual Task DeleteTemplateAsync(TemplateName name, CallSettings callSettings = null)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.TemplateName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    TemplateName name = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]");
    // Make the request
    await modelArmorClient.DeleteTemplateAsync(name);
    

### DeleteTemplateAsync(TemplateName, CancellationToken)
    
    
    public virtual Task DeleteTemplateAsync(TemplateName name, CancellationToken cancellationToken)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.TemplateName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    TemplateName name = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]");
    // Make the request
    await modelArmorClient.DeleteTemplateAsync(name);
    

### DeleteTemplateAsync(string, CallSettings)
    
    
    public virtual Task DeleteTemplateAsync(string name, CallSettings callSettings = null)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/templates/[TEMPLATE]";
    // Make the request
    await modelArmorClient.DeleteTemplateAsync(name);
    

### DeleteTemplateAsync(string, CancellationToken)
    
    
    public virtual Task DeleteTemplateAsync(string name, CancellationToken cancellationToken)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/templates/[TEMPLATE]";
    // Make the request
    await modelArmorClient.DeleteTemplateAsync(name);
    

### GetFloorSetting(FloorSettingName, CallSettings)
    
    
    public virtual FloorSetting GetFloorSetting(FloorSettingName name, CallSettings callSettings = null)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FloorSettingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSettingName)`  
Required. The name of the floor setting to get, example projects/123/floorsetting.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    FloorSettingName name = FloorSettingName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    FloorSetting response = modelArmorClient.GetFloorSetting(name);
    

### GetFloorSetting(GetFloorSettingRequest, CallSettings)
    
    
    public virtual FloorSetting GetFloorSetting(GetFloorSettingRequest request, CallSettings callSettings = null)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetFloorSettingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    GetFloorSettingRequest request = new GetFloorSettingRequest
    {
        FloorSettingName = FloorSettingName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    FloorSetting response = modelArmorClient.GetFloorSetting(request);
    

### GetFloorSetting(string, CallSettings)
    
    
    public virtual FloorSetting GetFloorSetting(string name, CallSettings callSettings = null)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the floor setting to get, example projects/123/floorsetting.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/floorSetting";
    // Make the request
    FloorSetting response = modelArmorClient.GetFloorSetting(name);
    

### GetFloorSettingAsync(FloorSettingName, CallSettings)
    
    
    public virtual Task<FloorSetting> GetFloorSettingAsync(FloorSettingName name, CallSettings callSettings = null)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FloorSettingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSettingName)`  
Required. The name of the floor setting to get, example projects/123/floorsetting.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    FloorSettingName name = FloorSettingName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    FloorSetting response = await modelArmorClient.GetFloorSettingAsync(name);
    

### GetFloorSettingAsync(FloorSettingName, CancellationToken)
    
    
    public virtual Task<FloorSetting> GetFloorSettingAsync(FloorSettingName name, CancellationToken cancellationToken)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FloorSettingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSettingName)`  
Required. The name of the floor setting to get, example projects/123/floorsetting.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    FloorSettingName name = FloorSettingName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    FloorSetting response = await modelArmorClient.GetFloorSettingAsync(name);
    

### GetFloorSettingAsync(GetFloorSettingRequest, CallSettings)
    
    
    public virtual Task<FloorSetting> GetFloorSettingAsync(GetFloorSettingRequest request, CallSettings callSettings = null)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetFloorSettingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    GetFloorSettingRequest request = new GetFloorSettingRequest
    {
        FloorSettingName = FloorSettingName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    FloorSetting response = await modelArmorClient.GetFloorSettingAsync(request);
    

### GetFloorSettingAsync(GetFloorSettingRequest, CancellationToken)
    
    
    public virtual Task<FloorSetting> GetFloorSettingAsync(GetFloorSettingRequest request, CancellationToken cancellationToken)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetFloorSettingRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    GetFloorSettingRequest request = new GetFloorSettingRequest
    {
        FloorSettingName = FloorSettingName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    FloorSetting response = await modelArmorClient.GetFloorSettingAsync(request);
    

### GetFloorSettingAsync(string, CallSettings)
    
    
    public virtual Task<FloorSetting> GetFloorSettingAsync(string name, CallSettings callSettings = null)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the floor setting to get, example projects/123/floorsetting.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/floorSetting";
    // Make the request
    FloorSetting response = await modelArmorClient.GetFloorSettingAsync(name);
    

### GetFloorSettingAsync(string, CancellationToken)
    
    
    public virtual Task<FloorSetting> GetFloorSettingAsync(string name, CancellationToken cancellationToken)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the floor setting to get, example projects/123/floorsetting.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/floorSetting";
    // Make the request
    FloorSetting response = await modelArmorClient.GetFloorSettingAsync(name);
    

### GetTemplate(GetTemplateRequest, CallSettings)
    
    
    public virtual Template GetTemplate(GetTemplateRequest request, CallSettings callSettings = null)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    GetTemplateRequest request = new GetTemplateRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
    };
    // Make the request
    Template response = modelArmorClient.GetTemplate(request);
    

### GetTemplate(TemplateName, CallSettings)
    
    
    public virtual Template GetTemplate(TemplateName name, CallSettings callSettings = null)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.TemplateName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    TemplateName name = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]");
    // Make the request
    Template response = modelArmorClient.GetTemplate(name);
    

### GetTemplate(string, CallSettings)
    
    
    public virtual Template GetTemplate(string name, CallSettings callSettings = null)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/templates/[TEMPLATE]";
    // Make the request
    Template response = modelArmorClient.GetTemplate(name);
    

### GetTemplateAsync(GetTemplateRequest, CallSettings)
    
    
    public virtual Task<Template> GetTemplateAsync(GetTemplateRequest request, CallSettings callSettings = null)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    GetTemplateRequest request = new GetTemplateRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
    };
    // Make the request
    Template response = await modelArmorClient.GetTemplateAsync(request);
    

### GetTemplateAsync(GetTemplateRequest, CancellationToken)
    
    
    public virtual Task<Template> GetTemplateAsync(GetTemplateRequest request, CancellationToken cancellationToken)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    GetTemplateRequest request = new GetTemplateRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
    };
    // Make the request
    Template response = await modelArmorClient.GetTemplateAsync(request);
    

### GetTemplateAsync(TemplateName, CallSettings)
    
    
    public virtual Task<Template> GetTemplateAsync(TemplateName name, CallSettings callSettings = null)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.TemplateName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    TemplateName name = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]");
    // Make the request
    Template response = await modelArmorClient.GetTemplateAsync(name);
    

### GetTemplateAsync(TemplateName, CancellationToken)
    
    
    public virtual Task<Template> GetTemplateAsync(TemplateName name, CancellationToken cancellationToken)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.TemplateName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    TemplateName name = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]");
    // Make the request
    Template response = await modelArmorClient.GetTemplateAsync(name);
    

### GetTemplateAsync(string, CallSettings)
    
    
    public virtual Task<Template> GetTemplateAsync(string name, CallSettings callSettings = null)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/templates/[TEMPLATE]";
    // Make the request
    Template response = await modelArmorClient.GetTemplateAsync(name);
    

### GetTemplateAsync(string, CancellationToken)
    
    
    public virtual Task<Template> GetTemplateAsync(string name, CancellationToken cancellationToken)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/templates/[TEMPLATE]";
    // Make the request
    Template response = await modelArmorClient.GetTemplateAsync(name);
    

### ListTemplates(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListTemplatesResponse, Template> ListTemplates(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListTemplatesRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A pageable sequence of [Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template) resources.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListTemplatesResponse, Template> response = modelArmorClient.ListTemplates(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Template item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListTemplatesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Template item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Template> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Template item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTemplates(ListTemplatesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListTemplatesResponse, Template> ListTemplates(ListTemplatesRequest request, CallSettings callSettings = null)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A pageable sequence of [Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template) resources.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    ListTemplatesRequest request = new ListTemplatesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListTemplatesResponse, Template> response = modelArmorClient.ListTemplates(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Template item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListTemplatesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Template item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Template> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Template item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTemplates(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListTemplatesResponse, Template> ListTemplates(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListTemplatesRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A pageable sequence of [Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template) resources.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListTemplatesResponse, Template> response = modelArmorClient.ListTemplates(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Template item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListTemplatesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Template item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Template> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Template item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTemplatesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTemplatesResponse, Template> ListTemplatesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListTemplatesRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A pageable asynchronous sequence of [Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template) resources.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListTemplatesResponse, Template> response = modelArmorClient.ListTemplatesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Template item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListTemplatesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Template item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Template> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Template item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTemplatesAsync(ListTemplatesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTemplatesResponse, Template> ListTemplatesAsync(ListTemplatesRequest request, CallSettings callSettings = null)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A pageable asynchronous sequence of [Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template) resources.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    ListTemplatesRequest request = new ListTemplatesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListTemplatesResponse, Template> response = modelArmorClient.ListTemplatesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Template item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListTemplatesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Template item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Template> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Template item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTemplatesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTemplatesResponse, Template> ListTemplatesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListTemplatesRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A pageable asynchronous sequence of [Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template) resources.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListTemplatesResponse, Template> response = modelArmorClient.ListTemplatesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Template item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListTemplatesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Template item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Template> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Template item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SanitizeModelResponse(SanitizeModelResponseRequest, CallSettings)
    
    
    public virtual SanitizeModelResponseResponse SanitizeModelResponse(SanitizeModelResponseRequest request, CallSettings callSettings = null)

Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    SanitizeModelResponseRequest request = new SanitizeModelResponseRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
        ModelResponseData = new DataItem(),
        UserPrompt = "",
        MultiLanguageDetectionMetadata = new MultiLanguageDetectionMetadata(),
        StreamingMode = StreamingMode.Unspecified,
    };
    // Make the request
    SanitizeModelResponseResponse response = modelArmorClient.SanitizeModelResponse(request);
    

### SanitizeModelResponseAsync(SanitizeModelResponseRequest, CallSettings)
    
    
    public virtual Task<SanitizeModelResponseResponse> SanitizeModelResponseAsync(SanitizeModelResponseRequest request, CallSettings callSettings = null)

Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    SanitizeModelResponseRequest request = new SanitizeModelResponseRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
        ModelResponseData = new DataItem(),
        UserPrompt = "",
        MultiLanguageDetectionMetadata = new MultiLanguageDetectionMetadata(),
        StreamingMode = StreamingMode.Unspecified,
    };
    // Make the request
    SanitizeModelResponseResponse response = await modelArmorClient.SanitizeModelResponseAsync(request);
    

### SanitizeModelResponseAsync(SanitizeModelResponseRequest, CancellationToken)
    
    
    public virtual Task<SanitizeModelResponseResponse> SanitizeModelResponseAsync(SanitizeModelResponseRequest request, CancellationToken cancellationToken)

Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    SanitizeModelResponseRequest request = new SanitizeModelResponseRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
        ModelResponseData = new DataItem(),
        UserPrompt = "",
        MultiLanguageDetectionMetadata = new MultiLanguageDetectionMetadata(),
        StreamingMode = StreamingMode.Unspecified,
    };
    // Make the request
    SanitizeModelResponseResponse response = await modelArmorClient.SanitizeModelResponseAsync(request);
    

### SanitizeUserPrompt(SanitizeUserPromptRequest, CallSettings)
    
    
    public virtual SanitizeUserPromptResponse SanitizeUserPrompt(SanitizeUserPromptRequest request, CallSettings callSettings = null)

Sanitizes User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    SanitizeUserPromptRequest request = new SanitizeUserPromptRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
        UserPromptData = new DataItem(),
        MultiLanguageDetectionMetadata = new MultiLanguageDetectionMetadata(),
        StreamingMode = StreamingMode.Unspecified,
    };
    // Make the request
    SanitizeUserPromptResponse response = modelArmorClient.SanitizeUserPrompt(request);
    

### SanitizeUserPromptAsync(SanitizeUserPromptRequest, CallSettings)
    
    
    public virtual Task<SanitizeUserPromptResponse> SanitizeUserPromptAsync(SanitizeUserPromptRequest request, CallSettings callSettings = null)

Sanitizes User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    SanitizeUserPromptRequest request = new SanitizeUserPromptRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
        UserPromptData = new DataItem(),
        MultiLanguageDetectionMetadata = new MultiLanguageDetectionMetadata(),
        StreamingMode = StreamingMode.Unspecified,
    };
    // Make the request
    SanitizeUserPromptResponse response = await modelArmorClient.SanitizeUserPromptAsync(request);
    

### SanitizeUserPromptAsync(SanitizeUserPromptRequest, CancellationToken)
    
    
    public virtual Task<SanitizeUserPromptResponse> SanitizeUserPromptAsync(SanitizeUserPromptRequest request, CancellationToken cancellationToken)

Sanitizes User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    SanitizeUserPromptRequest request = new SanitizeUserPromptRequest
    {
        TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
        UserPromptData = new DataItem(),
        MultiLanguageDetectionMetadata = new MultiLanguageDetectionMetadata(),
        StreamingMode = StreamingMode.Unspecified,
    };
    // Make the request
    SanitizeUserPromptResponse response = await modelArmorClient.SanitizeUserPromptAsync(request);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient#Google_Cloud_ModelArmor_V1Beta_ModelArmorClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient#Google_Cloud_ModelArmor_V1Beta_ModelArmorClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient#Google_Cloud_ModelArmor_V1Beta_ModelArmorClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient#Google_Cloud_ModelArmor_V1Beta_ModelArmorClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### StreamSanitizeModelResponse(CallSettings, BidirectionalStreamingSettings)
    
    
    public virtual ModelArmorClient.StreamSanitizeModelResponseStream StreamSanitizeModelResponse(CallSettings callSettings = null, BidirectionalStreamingSettings streamingSettings = null)

Streaming version of Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
`streamingSettings` | `[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)`  
If not null, applies streaming overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient)[StreamSanitizeModelResponseStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient.StreamSanitizeModelResponseStream)` | The client-server stream.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize streaming call, retrieving the stream object
    using ModelArmorClient.StreamSanitizeModelResponseStream response = modelArmorClient.StreamSanitizeModelResponse();
    
    // Sending requests and retrieving responses can be arbitrarily interleaved
    // Exact sequence will depend on client/server behavior
    
    // Create task to do something with responses from server
    Task responseHandlerTask = Task.Run(async () =>
    {
        // Note that C# 8 code can use await foreach
        AsyncResponseStream<SanitizeModelResponseResponse> responseStream = response.GetResponseStream();
        while (await responseStream.MoveNextAsync())
        {
            SanitizeModelResponseResponse responseItem = responseStream.Current;
            // Do something with streamed response
        }
        // The response stream has completed
    });
    
    // Send requests to the server
    bool done = false;
    while (!done)
    {
        // Initialize a request
        SanitizeModelResponseRequest request = new SanitizeModelResponseRequest
        {
            TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
            ModelResponseData = new DataItem(),
            UserPrompt = "",
            MultiLanguageDetectionMetadata = new MultiLanguageDetectionMetadata(),
            StreamingMode = StreamingMode.Unspecified,
        };
        // Stream a request to the server
        await response.WriteAsync(request);
        // Set "done" to true when sending requests is complete
    }
    
    // Complete writing requests to the stream
    await response.WriteCompleteAsync();
    // Await the response handler
    // This will complete once all server responses have been processed
    await responseHandlerTask;
    

### StreamSanitizeUserPrompt(CallSettings, BidirectionalStreamingSettings)
    
    
    public virtual ModelArmorClient.StreamSanitizeUserPromptStream StreamSanitizeUserPrompt(CallSettings callSettings = null, BidirectionalStreamingSettings streamingSettings = null)

Streaming version of Sanitize User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
`streamingSettings` | `[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)`  
If not null, applies streaming overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient)[StreamSanitizeUserPromptStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient.StreamSanitizeUserPromptStream)` | The client-server stream.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize streaming call, retrieving the stream object
    using ModelArmorClient.StreamSanitizeUserPromptStream response = modelArmorClient.StreamSanitizeUserPrompt();
    
    // Sending requests and retrieving responses can be arbitrarily interleaved
    // Exact sequence will depend on client/server behavior
    
    // Create task to do something with responses from server
    Task responseHandlerTask = Task.Run(async () =>
    {
        // Note that C# 8 code can use await foreach
        AsyncResponseStream<SanitizeUserPromptResponse> responseStream = response.GetResponseStream();
        while (await responseStream.MoveNextAsync())
        {
            SanitizeUserPromptResponse responseItem = responseStream.Current;
            // Do something with streamed response
        }
        // The response stream has completed
    });
    
    // Send requests to the server
    bool done = false;
    while (!done)
    {
        // Initialize a request
        SanitizeUserPromptRequest request = new SanitizeUserPromptRequest
        {
            TemplateName = TemplateName.FromProjectLocationTemplate("[PROJECT]", "[LOCATION]", "[TEMPLATE]"),
            UserPromptData = new DataItem(),
            MultiLanguageDetectionMetadata = new MultiLanguageDetectionMetadata(),
            StreamingMode = StreamingMode.Unspecified,
        };
        // Stream a request to the server
        await response.WriteAsync(request);
        // Set "done" to true when sending requests is complete
    }
    
    // Complete writing requests to the stream
    await response.WriteCompleteAsync();
    // Await the response handler
    // This will complete once all server responses have been processed
    await responseHandlerTask;
    

### UpdateFloorSetting(FloorSetting, FieldMask, CallSettings)
    
    
    public virtual FloorSetting UpdateFloorSetting(FloorSetting floorSetting, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`floorSetting` | `[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)`  
Required. The floor setting being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the FloorSetting resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    FloorSetting floorSetting = new FloorSetting();
    FieldMask updateMask = new FieldMask();
    // Make the request
    FloorSetting response = modelArmorClient.UpdateFloorSetting(floorSetting, updateMask);
    

### UpdateFloorSetting(UpdateFloorSettingRequest, CallSettings)
    
    
    public virtual FloorSetting UpdateFloorSetting(UpdateFloorSettingRequest request, CallSettings callSettings = null)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateFloorSettingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    UpdateFloorSettingRequest request = new UpdateFloorSettingRequest
    {
        FloorSetting = new FloorSetting(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    FloorSetting response = modelArmorClient.UpdateFloorSetting(request);
    

### UpdateFloorSettingAsync(FloorSetting, FieldMask, CallSettings)
    
    
    public virtual Task<FloorSetting> UpdateFloorSettingAsync(FloorSetting floorSetting, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`floorSetting` | `[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)`  
Required. The floor setting being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the FloorSetting resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    FloorSetting floorSetting = new FloorSetting();
    FieldMask updateMask = new FieldMask();
    // Make the request
    FloorSetting response = await modelArmorClient.UpdateFloorSettingAsync(floorSetting, updateMask);
    

### UpdateFloorSettingAsync(FloorSetting, FieldMask, CancellationToken)
    
    
    public virtual Task<FloorSetting> UpdateFloorSettingAsync(FloorSetting floorSetting, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`floorSetting` | `[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)`  
Required. The floor setting being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the FloorSetting resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    FloorSetting floorSetting = new FloorSetting();
    FieldMask updateMask = new FieldMask();
    // Make the request
    FloorSetting response = await modelArmorClient.UpdateFloorSettingAsync(floorSetting, updateMask);
    

### UpdateFloorSettingAsync(UpdateFloorSettingRequest, CallSettings)
    
    
    public virtual Task<FloorSetting> UpdateFloorSettingAsync(UpdateFloorSettingRequest request, CallSettings callSettings = null)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateFloorSettingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFloorSettingRequest request = new UpdateFloorSettingRequest
    {
        FloorSetting = new FloorSetting(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    FloorSetting response = await modelArmorClient.UpdateFloorSettingAsync(request);
    

### UpdateFloorSettingAsync(UpdateFloorSettingRequest, CancellationToken)
    
    
    public virtual Task<FloorSetting> UpdateFloorSettingAsync(UpdateFloorSettingRequest request, CancellationToken cancellationToken)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateFloorSettingRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFloorSettingRequest request = new UpdateFloorSettingRequest
    {
        FloorSetting = new FloorSetting(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    FloorSetting response = await modelArmorClient.UpdateFloorSettingAsync(request);
    

### UpdateTemplate(Template, FieldMask, CallSettings)
    
    
    public virtual Template UpdateTemplate(Template template, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`template` | `[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Template resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    Template template = new Template();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Template response = modelArmorClient.UpdateTemplate(template, updateMask);
    

### UpdateTemplate(UpdateTemplateRequest, CallSettings)
    
    
    public virtual Template UpdateTemplate(UpdateTemplateRequest request, CallSettings callSettings = null)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = ModelArmorClient.Create();
    // Initialize request argument(s)
    UpdateTemplateRequest request = new UpdateTemplateRequest
    {
        UpdateMask = new FieldMask(),
        Template = new Template(),
        RequestId = "",
    };
    // Make the request
    Template response = modelArmorClient.UpdateTemplate(request);
    

### UpdateTemplateAsync(Template, FieldMask, CallSettings)
    
    
    public virtual Task<Template> UpdateTemplateAsync(Template template, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`template` | `[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Template resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    Template template = new Template();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Template response = await modelArmorClient.UpdateTemplateAsync(template, updateMask);
    

### UpdateTemplateAsync(Template, FieldMask, CancellationToken)
    
    
    public virtual Task<Template> UpdateTemplateAsync(Template template, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`template` | `[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Template resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    Template template = new Template();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Template response = await modelArmorClient.UpdateTemplateAsync(template, updateMask);
    

### UpdateTemplateAsync(UpdateTemplateRequest, CallSettings)
    
    
    public virtual Task<Template> UpdateTemplateAsync(UpdateTemplateRequest request, CallSettings callSettings = null)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    UpdateTemplateRequest request = new UpdateTemplateRequest
    {
        UpdateMask = new FieldMask(),
        Template = new Template(),
        RequestId = "",
    };
    // Make the request
    Template response = await modelArmorClient.UpdateTemplateAsync(request);
    

### UpdateTemplateAsync(UpdateTemplateRequest, CancellationToken)
    
    
    public virtual Task<Template> UpdateTemplateAsync(UpdateTemplateRequest request, CancellationToken cancellationToken)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateTemplateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ModelArmorClient modelArmorClient = await ModelArmorClient.CreateAsync();
    // Initialize request argument(s)
    UpdateTemplateRequest request = new UpdateTemplateRequest
    {
        UpdateMask = new FieldMask(),
        Template = new Template(),
        RequestId = "",
    };
    // Make the request
    Template response = await modelArmorClient.UpdateTemplateAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
