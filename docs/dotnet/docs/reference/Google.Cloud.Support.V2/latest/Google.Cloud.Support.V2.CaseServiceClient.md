---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient
title: Google Cloud Support v2 API - Class CaseServiceClient (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:00.973029+00:00
---

# Google Cloud Support v2 API - Class CaseServiceClient (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Support v2 API - Class CaseServiceClient (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class CaseServiceClient

Reference documentation and code samples for the Google Cloud Support v2 API class CaseServiceClient.

CaseService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CaseServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[CaseServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClientImpl)

## Namespace

[Google.Cloud.Support.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2)

## Assembly

Google.Cloud.Support.V2.dll

## Remarks

A service to manage Google Cloud support cases.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the CaseService service, which is a host of "cloudsupport.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default CaseService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default CaseService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual CaseService.CaseServiceClient GrpcClient { get; }

The underlying gRPC CaseService client

**Property Value**  
---  
**Type** | **Description**  
`[CaseService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseService)[CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseService.CaseServiceClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### CloseCase(CloseCaseRequest, CallSettings)
    
    
    public virtual Case CloseCase(CloseCaseRequest request, CallSettings callSettings = null)

Close a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloseCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CloseCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    CloseCaseRequest request = new CloseCaseRequest
    {
        CaseName = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]"),
    };
    // Make the request
    Case response = caseServiceClient.CloseCase(request);
    

### CloseCaseAsync(CloseCaseRequest, CallSettings)
    
    
    public virtual Task<Case> CloseCaseAsync(CloseCaseRequest request, CallSettings callSettings = null)

Close a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloseCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CloseCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    CloseCaseRequest request = new CloseCaseRequest
    {
        CaseName = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]"),
    };
    // Make the request
    Case response = await caseServiceClient.CloseCaseAsync(request);
    

### CloseCaseAsync(CloseCaseRequest, CancellationToken)
    
    
    public virtual Task<Case> CloseCaseAsync(CloseCaseRequest request, CancellationToken cancellationToken)

Close a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloseCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CloseCaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    CloseCaseRequest request = new CloseCaseRequest
    {
        CaseName = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]"),
    };
    // Make the request
    Case response = await caseServiceClient.CloseCaseAsync(request);
    

### Create()
    
    
    public static CaseServiceClient Create()

Synchronously creates a [CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CaseServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient)` | The created [CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<CaseServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CaseServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient)` | The task representing the created [CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient).  
  
### CreateCase(OrganizationName, Case, CallSettings)
    
    
    public virtual Case CreateCase(OrganizationName parent, Case @case, CallSettings callSettings = null)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)`  
Required. The name of the parent under which the case should be created.  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    OrganizationName parent = OrganizationName.FromOrganization("[ORGANIZATION]");
    Case @case = new Case();
    // Make the request
    Case response = caseServiceClient.CreateCase(parent, @case);
    

### CreateCase(ProjectName, Case, CallSettings)
    
    
    public virtual Case CreateCase(ProjectName parent, Case @case, CallSettings callSettings = null)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The name of the parent under which the case should be created.  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    Case @case = new Case();
    // Make the request
    Case response = caseServiceClient.CreateCase(parent, @case);
    

### CreateCase(CreateCaseRequest, CallSettings)
    
    
    public virtual Case CreateCase(CreateCaseRequest request, CallSettings callSettings = null)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    CreateCaseRequest request = new CreateCaseRequest
    {
        ParentAsOrganizationName = OrganizationName.FromOrganization("[ORGANIZATION]"),
        Case = new Case(),
    };
    // Make the request
    Case response = caseServiceClient.CreateCase(request);
    

### CreateCase(string, Case, CallSettings)
    
    
    public virtual Case CreateCase(string parent, Case @case, CallSettings callSettings = null)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent under which the case should be created.  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]";
    Case @case = new Case();
    // Make the request
    Case response = caseServiceClient.CreateCase(parent, @case);
    

### CreateCaseAsync(OrganizationName, Case, CallSettings)
    
    
    public virtual Task<Case> CreateCaseAsync(OrganizationName parent, Case @case, CallSettings callSettings = null)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)`  
Required. The name of the parent under which the case should be created.  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationName parent = OrganizationName.FromOrganization("[ORGANIZATION]");
    Case @case = new Case();
    // Make the request
    Case response = await caseServiceClient.CreateCaseAsync(parent, @case);
    

### CreateCaseAsync(OrganizationName, Case, CancellationToken)
    
    
    public virtual Task<Case> CreateCaseAsync(OrganizationName parent, Case @case, CancellationToken cancellationToken)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)`  
Required. The name of the parent under which the case should be created.  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to be created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationName parent = OrganizationName.FromOrganization("[ORGANIZATION]");
    Case @case = new Case();
    // Make the request
    Case response = await caseServiceClient.CreateCaseAsync(parent, @case);
    

### CreateCaseAsync(ProjectName, Case, CallSettings)
    
    
    public virtual Task<Case> CreateCaseAsync(ProjectName parent, Case @case, CallSettings callSettings = null)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The name of the parent under which the case should be created.  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    Case @case = new Case();
    // Make the request
    Case response = await caseServiceClient.CreateCaseAsync(parent, @case);
    

### CreateCaseAsync(ProjectName, Case, CancellationToken)
    
    
    public virtual Task<Case> CreateCaseAsync(ProjectName parent, Case @case, CancellationToken cancellationToken)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The name of the parent under which the case should be created.  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to be created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    Case @case = new Case();
    // Make the request
    Case response = await caseServiceClient.CreateCaseAsync(parent, @case);
    

### CreateCaseAsync(CreateCaseRequest, CallSettings)
    
    
    public virtual Task<Case> CreateCaseAsync(CreateCaseRequest request, CallSettings callSettings = null)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateCaseRequest request = new CreateCaseRequest
    {
        ParentAsOrganizationName = OrganizationName.FromOrganization("[ORGANIZATION]"),
        Case = new Case(),
    };
    // Make the request
    Case response = await caseServiceClient.CreateCaseAsync(request);
    

### CreateCaseAsync(CreateCaseRequest, CancellationToken)
    
    
    public virtual Task<Case> CreateCaseAsync(CreateCaseRequest request, CancellationToken cancellationToken)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateCaseRequest request = new CreateCaseRequest
    {
        ParentAsOrganizationName = OrganizationName.FromOrganization("[ORGANIZATION]"),
        Case = new Case(),
    };
    // Make the request
    Case response = await caseServiceClient.CreateCaseAsync(request);
    

### CreateCaseAsync(string, Case, CallSettings)
    
    
    public virtual Task<Case> CreateCaseAsync(string parent, Case @case, CallSettings callSettings = null)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent under which the case should be created.  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]";
    Case @case = new Case();
    // Make the request
    Case response = await caseServiceClient.CreateCaseAsync(parent, @case);
    

### CreateCaseAsync(string, Case, CancellationToken)
    
    
    public virtual Task<Case> CreateCaseAsync(string parent, Case @case, CancellationToken cancellationToken)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent under which the case should be created.  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to be created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]";
    Case @case = new Case();
    // Make the request
    Case response = await caseServiceClient.CreateCaseAsync(parent, @case);
    

### EscalateCase(EscalateCaseRequest, CallSettings)
    
    
    public virtual Case EscalateCase(EscalateCaseRequest request, CallSettings callSettings = null)

Escalate a case, starting the Google Cloud Support escalation management process.

This operation is only available for some support services. Go to <https://cloud.google.com/support> and look for 'Technical support escalations' in the feature list to find out which ones let you do that.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EscalateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.EscalateCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    EscalateCaseRequest request = new EscalateCaseRequest
    {
        CaseName = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]"),
        Escalation = new Escalation(),
    };
    // Make the request
    Case response = caseServiceClient.EscalateCase(request);
    

### EscalateCaseAsync(EscalateCaseRequest, CallSettings)
    
    
    public virtual Task<Case> EscalateCaseAsync(EscalateCaseRequest request, CallSettings callSettings = null)

Escalate a case, starting the Google Cloud Support escalation management process.

This operation is only available for some support services. Go to <https://cloud.google.com/support> and look for 'Technical support escalations' in the feature list to find out which ones let you do that.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EscalateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.EscalateCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    EscalateCaseRequest request = new EscalateCaseRequest
    {
        CaseName = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]"),
        Escalation = new Escalation(),
    };
    // Make the request
    Case response = await caseServiceClient.EscalateCaseAsync(request);
    

### EscalateCaseAsync(EscalateCaseRequest, CancellationToken)
    
    
    public virtual Task<Case> EscalateCaseAsync(EscalateCaseRequest request, CancellationToken cancellationToken)

Escalate a case, starting the Google Cloud Support escalation management process.

This operation is only available for some support services. Go to <https://cloud.google.com/support> and look for 'Technical support escalations' in the feature list to find out which ones let you do that.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EscalateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.EscalateCaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    EscalateCaseRequest request = new EscalateCaseRequest
    {
        CaseName = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]"),
        Escalation = new Escalation(),
    };
    // Make the request
    Case response = await caseServiceClient.EscalateCaseAsync(request);
    

### GetCase(CaseName, CallSettings)
    
    
    public virtual Case GetCase(CaseName name, CallSettings callSettings = null)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseName)`  
Required. The full name of a case to be retrieved.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    CaseName name = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]");
    // Make the request
    Case response = caseServiceClient.GetCase(name);
    

### GetCase(GetCaseRequest, CallSettings)
    
    
    public virtual Case GetCase(GetCaseRequest request, CallSettings callSettings = null)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    GetCaseRequest request = new GetCaseRequest
    {
        CaseName = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]"),
    };
    // Make the request
    Case response = caseServiceClient.GetCase(request);
    

### GetCase(string, CallSettings)
    
    
    public virtual Case GetCase(string name, CallSettings callSettings = null)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The full name of a case to be retrieved.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/cases/[CASE]";
    // Make the request
    Case response = caseServiceClient.GetCase(name);
    

### GetCaseAsync(CaseName, CallSettings)
    
    
    public virtual Task<Case> GetCaseAsync(CaseName name, CallSettings callSettings = null)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseName)`  
Required. The full name of a case to be retrieved.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    CaseName name = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]");
    // Make the request
    Case response = await caseServiceClient.GetCaseAsync(name);
    

### GetCaseAsync(CaseName, CancellationToken)
    
    
    public virtual Task<Case> GetCaseAsync(CaseName name, CancellationToken cancellationToken)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseName)`  
Required. The full name of a case to be retrieved.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    CaseName name = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]");
    // Make the request
    Case response = await caseServiceClient.GetCaseAsync(name);
    

### GetCaseAsync(GetCaseRequest, CallSettings)
    
    
    public virtual Task<Case> GetCaseAsync(GetCaseRequest request, CallSettings callSettings = null)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetCaseRequest request = new GetCaseRequest
    {
        CaseName = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]"),
    };
    // Make the request
    Case response = await caseServiceClient.GetCaseAsync(request);
    

### GetCaseAsync(GetCaseRequest, CancellationToken)
    
    
    public virtual Task<Case> GetCaseAsync(GetCaseRequest request, CancellationToken cancellationToken)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetCaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetCaseRequest request = new GetCaseRequest
    {
        CaseName = CaseName.FromOrganizationCase("[ORGANIZATION]", "[CASE]"),
    };
    // Make the request
    Case response = await caseServiceClient.GetCaseAsync(request);
    

### GetCaseAsync(string, CallSettings)
    
    
    public virtual Task<Case> GetCaseAsync(string name, CallSettings callSettings = null)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The full name of a case to be retrieved.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/cases/[CASE]";
    // Make the request
    Case response = await caseServiceClient.GetCaseAsync(name);
    

### GetCaseAsync(string, CancellationToken)
    
    
    public virtual Task<Case> GetCaseAsync(string name, CancellationToken cancellationToken)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The full name of a case to be retrieved.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/cases/[CASE]";
    // Make the request
    Case response = await caseServiceClient.GetCaseAsync(name);
    

### ListCases(OrganizationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCasesResponse, Case> ListCases(OrganizationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)`  
Required. The name of a parent to list cases under.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    OrganizationName parent = OrganizationName.FromOrganization("[ORGANIZATION]");
    // Make the request
    PagedEnumerable<ListCasesResponse, Case> response = caseServiceClient.ListCases(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCases(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCasesResponse, Case> ListCases(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The name of a parent to list cases under.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedEnumerable<ListCasesResponse, Case> response = caseServiceClient.ListCases(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCases(ListCasesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListCasesResponse, Case> ListCases(ListCasesRequest request, CallSettings callSettings = null)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    ListCasesRequest request = new ListCasesRequest
    {
        ParentAsOrganizationName = OrganizationName.FromOrganization("[ORGANIZATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListCasesResponse, Case> response = caseServiceClient.ListCases(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCases(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCasesResponse, Case> ListCases(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of a parent to list cases under.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]";
    // Make the request
    PagedEnumerable<ListCasesResponse, Case> response = caseServiceClient.ListCases(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCasesAsync(OrganizationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCasesResponse, Case> ListCasesAsync(OrganizationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)`  
Required. The name of a parent to list cases under.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable asynchronous sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationName parent = OrganizationName.FromOrganization("[ORGANIZATION]");
    // Make the request
    PagedAsyncEnumerable<ListCasesResponse, Case> response = caseServiceClient.ListCasesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCasesAsync(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCasesResponse, Case> ListCasesAsync(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The name of a parent to list cases under.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable asynchronous sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedAsyncEnumerable<ListCasesResponse, Case> response = caseServiceClient.ListCasesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCasesAsync(ListCasesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCasesResponse, Case> ListCasesAsync(ListCasesRequest request, CallSettings callSettings = null)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable asynchronous sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListCasesRequest request = new ListCasesRequest
    {
        ParentAsOrganizationName = OrganizationName.FromOrganization("[ORGANIZATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListCasesResponse, Case> response = caseServiceClient.ListCasesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCasesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCasesResponse, Case> ListCasesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of a parent to list cases under.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable asynchronous sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]";
    // Make the request
    PagedAsyncEnumerable<ListCasesResponse, Case> response = caseServiceClient.ListCasesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCaseClassifications(SearchCaseClassificationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchCaseClassificationsResponse, CaseClassification> SearchCaseClassifications(SearchCaseClassificationsRequest request, CallSettings callSettings = null)

Retrieve valid classifications to use when creating a support case.

Classifications are hierarchical. Each classification is a string containing all levels of the hierarchy separated by `" > "`. For example, `"Technical Issue > Compute > Compute Engine"`.

Classification IDs returned by this endpoint are valid for at least six months. When a classification is deactivated, this endpoint immediately stops returning it. After six months, `case.create` requests using the classification will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCaseClassificationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchCaseClassificationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsResponse)[CaseClassification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseClassification)` | A pageable sequence of [CaseClassification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseClassification) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    SearchCaseClassificationsRequest request = new SearchCaseClassificationsRequest { Query = "", };
    // Make the request
    PagedEnumerable<SearchCaseClassificationsResponse, CaseClassification> response = caseServiceClient.SearchCaseClassifications(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CaseClassification item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchCaseClassificationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CaseClassification item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CaseClassification> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CaseClassification item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCaseClassificationsAsync(SearchCaseClassificationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchCaseClassificationsResponse, CaseClassification> SearchCaseClassificationsAsync(SearchCaseClassificationsRequest request, CallSettings callSettings = null)

Retrieve valid classifications to use when creating a support case.

Classifications are hierarchical. Each classification is a string containing all levels of the hierarchy separated by `" > "`. For example, `"Technical Issue > Compute > Compute Engine"`.

Classification IDs returned by this endpoint are valid for at least six months. When a classification is deactivated, this endpoint immediately stops returning it. After six months, `case.create` requests using the classification will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCaseClassificationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchCaseClassificationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsResponse)[CaseClassification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseClassification)` | A pageable asynchronous sequence of [CaseClassification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseClassification) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    SearchCaseClassificationsRequest request = new SearchCaseClassificationsRequest { Query = "", };
    // Make the request
    PagedAsyncEnumerable<SearchCaseClassificationsResponse, CaseClassification> response = caseServiceClient.SearchCaseClassificationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CaseClassification item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchCaseClassificationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CaseClassification item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CaseClassification> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CaseClassification item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCases(SearchCasesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchCasesResponse, Case> SearchCases(SearchCasesRequest request, CallSettings callSettings = null)

Search for cases using a query.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    SearchCasesRequest request = new SearchCasesRequest
    {
        Query = "",
        Parent = "",
    };
    // Make the request
    PagedEnumerable<SearchCasesResponse, Case> response = caseServiceClient.SearchCases(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCasesAsync(SearchCasesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchCasesResponse, Case> SearchCasesAsync(SearchCasesRequest request, CallSettings callSettings = null)

Search for cases using a query.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesResponse)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A pageable asynchronous sequence of [Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case) resources.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    SearchCasesRequest request = new SearchCasesRequest
    {
        Query = "",
        Parent = "",
    };
    // Make the request
    PagedAsyncEnumerable<SearchCasesResponse, Case> response = caseServiceClient.SearchCasesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Case item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchCasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Case item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Case> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Case item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient#Google_Cloud_Support_V2_CaseServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient#Google_Cloud_Support_V2_CaseServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient#Google_Cloud_Support_V2_CaseServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseServiceClient#Google_Cloud_Support_V2_CaseServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateCase(Case, FieldMask, CallSettings)
    
    
    public virtual Case UpdateCase(Case @case, FieldMask updateMask, CallSettings callSettings = null)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
A list of attributes of the case that should be updated. Supported values are `priority`, `display_name`, and `subscriber_email_addresses`. If no fields are specified, all supported fields are updated. Be careful - if you do not provide a field mask, then you might accidentally clear some fields. For example, if you leave the field mask empty and do not provide a value for `subscriber_email_addresses`, then `subscriber_email_addresses` is updated to empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    Case @case = new Case();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Case response = caseServiceClient.UpdateCase(@case, updateMask);
    

### UpdateCase(UpdateCaseRequest, CallSettings)
    
    
    public virtual Case UpdateCase(UpdateCaseRequest request, CallSettings callSettings = null)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.UpdateCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = CaseServiceClient.Create();
    // Initialize request argument(s)
    UpdateCaseRequest request = new UpdateCaseRequest
    {
        Case = new Case(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Case response = caseServiceClient.UpdateCase(request);
    

### UpdateCaseAsync(Case, FieldMask, CallSettings)
    
    
    public virtual Task<Case> UpdateCaseAsync(Case @case, FieldMask updateMask, CallSettings callSettings = null)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
A list of attributes of the case that should be updated. Supported values are `priority`, `display_name`, and `subscriber_email_addresses`. If no fields are specified, all supported fields are updated. Be careful - if you do not provide a field mask, then you might accidentally clear some fields. For example, if you leave the field mask empty and do not provide a value for `subscriber_email_addresses`, then `subscriber_email_addresses` is updated to empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    Case @case = new Case();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Case response = await caseServiceClient.UpdateCaseAsync(@case, updateMask);
    

### UpdateCaseAsync(Case, FieldMask, CancellationToken)
    
    
    public virtual Task<Case> UpdateCaseAsync(Case @case, FieldMask updateMask, CancellationToken cancellationToken)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`case` | `[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)`  
Required. The case to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
A list of attributes of the case that should be updated. Supported values are `priority`, `display_name`, and `subscriber_email_addresses`. If no fields are specified, all supported fields are updated. Be careful - if you do not provide a field mask, then you might accidentally clear some fields. For example, if you leave the field mask empty and do not provide a value for `subscriber_email_addresses`, then `subscriber_email_addresses` is updated to empty.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    Case @case = new Case();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Case response = await caseServiceClient.UpdateCaseAsync(@case, updateMask);
    

### UpdateCaseAsync(UpdateCaseRequest, CallSettings)
    
    
    public virtual Task<Case> UpdateCaseAsync(UpdateCaseRequest request, CallSettings callSettings = null)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.UpdateCaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCaseRequest request = new UpdateCaseRequest
    {
        Case = new Case(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Case response = await caseServiceClient.UpdateCaseAsync(request);
    

### UpdateCaseAsync(UpdateCaseRequest, CancellationToken)
    
    
    public virtual Task<Case> UpdateCaseAsync(UpdateCaseRequest request, CancellationToken cancellationToken)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.UpdateCaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CaseServiceClient caseServiceClient = await CaseServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCaseRequest request = new UpdateCaseRequest
    {
        Case = new Case(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Case response = await caseServiceClient.UpdateCaseAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
