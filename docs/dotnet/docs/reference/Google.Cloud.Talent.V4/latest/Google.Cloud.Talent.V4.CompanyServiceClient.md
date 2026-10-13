---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient
title: Google Cloud Talent Solution v4 API - Class CompanyServiceClient (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:56.002585+00:00
---

# Google Cloud Talent Solution v4 API - Class CompanyServiceClient (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Talent Solution v4 API - Class CompanyServiceClient (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/2.7.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/2.6.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/2.5.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/2.4.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/2.3.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/2.2.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/2.1.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/2.0.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/1.4.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/1.3.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/1.2.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/1.1.0/Google.Cloud.Talent.V4.CompanyServiceClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/1.0.0/Google.Cloud.Talent.V4.CompanyServiceClient)


    
    
    public abstract class CompanyServiceClient

Reference documentation and code samples for the Google Cloud Talent Solution v4 API class CompanyServiceClient.

CompanyService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CompanyServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[CompanyServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClientImpl)

## Namespace

[Google.Cloud.Talent.V4](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4)

## Assembly

Google.Cloud.Talent.V4.dll

## Remarks

A service that handles company management, including CRUD and enumeration.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the CompanyService service, which is a host of "jobs.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default CompanyService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default CompanyService scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/jobs>



### GrpcClient
    
    
    public virtual CompanyService.CompanyServiceClient GrpcClient { get; }

The underlying gRPC CompanyService client

**Property Value**  
---  
**Type** | **Description**  
`[CompanyService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyService)[CompanyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyService.CompanyServiceClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static CompanyServiceClient Create()

Synchronously creates a [CompanyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CompanyServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient)` | The created [CompanyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<CompanyServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [CompanyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CompanyServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient)` | The task representing the created [CompanyServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient).  
  
### CreateCompany(CreateCompanyRequest, CallSettings)
    
    
    public virtual Company CreateCompany(CreateCompanyRequest request, CallSettings callSettings = null)

Creates a new company entity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CreateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    CreateCompanyRequest request = new CreateCompanyRequest
    {
        ParentAsTenantName = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]"),
        Company = new Company(),
    };
    // Make the request
    Company response = companyServiceClient.CreateCompany(request);
    

### CreateCompany(TenantName, Company, CallSettings)
    
    
    public virtual Company CreateCompany(TenantName parent, Company company, CallSettings callSettings = null)

Creates a new company entity.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.TenantName)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`company` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)`  
Required. The company to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    TenantName parent = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]");
    Company company = new Company();
    // Make the request
    Company response = companyServiceClient.CreateCompany(parent, company);
    

### CreateCompany(string, Company, CallSettings)
    
    
    public virtual Company CreateCompany(string parent, Company company, CallSettings callSettings = null)

Creates a new company entity.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`company` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)`  
Required. The company to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/tenants/[TENANT]";
    Company company = new Company();
    // Make the request
    Company response = companyServiceClient.CreateCompany(parent, company);
    

### CreateCompanyAsync(CreateCompanyRequest, CallSettings)
    
    
    public virtual Task<Company> CreateCompanyAsync(CreateCompanyRequest request, CallSettings callSettings = null)

Creates a new company entity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CreateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateCompanyRequest request = new CreateCompanyRequest
    {
        ParentAsTenantName = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]"),
        Company = new Company(),
    };
    // Make the request
    Company response = await companyServiceClient.CreateCompanyAsync(request);
    

### CreateCompanyAsync(CreateCompanyRequest, CancellationToken)
    
    
    public virtual Task<Company> CreateCompanyAsync(CreateCompanyRequest request, CancellationToken cancellationToken)

Creates a new company entity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CreateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateCompanyRequest request = new CreateCompanyRequest
    {
        ParentAsTenantName = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]"),
        Company = new Company(),
    };
    // Make the request
    Company response = await companyServiceClient.CreateCompanyAsync(request);
    

### CreateCompanyAsync(TenantName, Company, CallSettings)
    
    
    public virtual Task<Company> CreateCompanyAsync(TenantName parent, Company company, CallSettings callSettings = null)

Creates a new company entity.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.TenantName)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`company` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)`  
Required. The company to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    TenantName parent = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]");
    Company company = new Company();
    // Make the request
    Company response = await companyServiceClient.CreateCompanyAsync(parent, company);
    

### CreateCompanyAsync(TenantName, Company, CancellationToken)
    
    
    public virtual Task<Company> CreateCompanyAsync(TenantName parent, Company company, CancellationToken cancellationToken)

Creates a new company entity.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.TenantName)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`company` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)`  
Required. The company to be created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    TenantName parent = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]");
    Company company = new Company();
    // Make the request
    Company response = await companyServiceClient.CreateCompanyAsync(parent, company);
    

### CreateCompanyAsync(string, Company, CallSettings)
    
    
    public virtual Task<Company> CreateCompanyAsync(string parent, Company company, CallSettings callSettings = null)

Creates a new company entity.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`company` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)`  
Required. The company to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/tenants/[TENANT]";
    Company company = new Company();
    // Make the request
    Company response = await companyServiceClient.CreateCompanyAsync(parent, company);
    

### CreateCompanyAsync(string, Company, CancellationToken)
    
    
    public virtual Task<Company> CreateCompanyAsync(string parent, Company company, CancellationToken cancellationToken)

Creates a new company entity.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`company` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)`  
Required. The company to be created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/tenants/[TENANT]";
    Company company = new Company();
    // Make the request
    Company response = await companyServiceClient.CreateCompanyAsync(parent, company);
    

### DeleteCompany(CompanyName, CallSettings)
    
    
    public virtual void DeleteCompany(CompanyName name, CallSettings callSettings = null)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyName)`  
Required. The resource name of the company to be deleted. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    CompanyName name = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]");
    // Make the request
    companyServiceClient.DeleteCompany(name);
    

### DeleteCompany(DeleteCompanyRequest, CallSettings)
    
    
    public virtual void DeleteCompany(DeleteCompanyRequest request, CallSettings callSettings = null)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.DeleteCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    DeleteCompanyRequest request = new DeleteCompanyRequest
    {
        CompanyName = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]"),
    };
    // Make the request
    companyServiceClient.DeleteCompany(request);
    

### DeleteCompany(string, CallSettings)
    
    
    public virtual void DeleteCompany(string name, CallSettings callSettings = null)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the company to be deleted. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/tenants/[TENANT]/companies/[COMPANY]";
    // Make the request
    companyServiceClient.DeleteCompany(name);
    

### DeleteCompanyAsync(CompanyName, CallSettings)
    
    
    public virtual Task DeleteCompanyAsync(CompanyName name, CallSettings callSettings = null)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyName)`  
Required. The resource name of the company to be deleted. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    CompanyName name = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]");
    // Make the request
    await companyServiceClient.DeleteCompanyAsync(name);
    

### DeleteCompanyAsync(CompanyName, CancellationToken)
    
    
    public virtual Task DeleteCompanyAsync(CompanyName name, CancellationToken cancellationToken)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyName)`  
Required. The resource name of the company to be deleted. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    CompanyName name = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]");
    // Make the request
    await companyServiceClient.DeleteCompanyAsync(name);
    

### DeleteCompanyAsync(DeleteCompanyRequest, CallSettings)
    
    
    public virtual Task DeleteCompanyAsync(DeleteCompanyRequest request, CallSettings callSettings = null)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.DeleteCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteCompanyRequest request = new DeleteCompanyRequest
    {
        CompanyName = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]"),
    };
    // Make the request
    await companyServiceClient.DeleteCompanyAsync(request);
    

### DeleteCompanyAsync(DeleteCompanyRequest, CancellationToken)
    
    
    public virtual Task DeleteCompanyAsync(DeleteCompanyRequest request, CancellationToken cancellationToken)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.DeleteCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteCompanyRequest request = new DeleteCompanyRequest
    {
        CompanyName = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]"),
    };
    // Make the request
    await companyServiceClient.DeleteCompanyAsync(request);
    

### DeleteCompanyAsync(string, CallSettings)
    
    
    public virtual Task DeleteCompanyAsync(string name, CallSettings callSettings = null)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the company to be deleted. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/tenants/[TENANT]/companies/[COMPANY]";
    // Make the request
    await companyServiceClient.DeleteCompanyAsync(name);
    

### DeleteCompanyAsync(string, CancellationToken)
    
    
    public virtual Task DeleteCompanyAsync(string name, CancellationToken cancellationToken)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the company to be deleted. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/tenants/[TENANT]/companies/[COMPANY]";
    // Make the request
    await companyServiceClient.DeleteCompanyAsync(name);
    

### GetCompany(CompanyName, CallSettings)
    
    
    public virtual Company GetCompany(CompanyName name, CallSettings callSettings = null)

Retrieves specified company.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyName)`  
Required. The resource name of the company to be retrieved. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/api-test-project/tenants/foo/companies/bar".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    CompanyName name = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]");
    // Make the request
    Company response = companyServiceClient.GetCompany(name);
    

### GetCompany(GetCompanyRequest, CallSettings)
    
    
    public virtual Company GetCompany(GetCompanyRequest request, CallSettings callSettings = null)

Retrieves specified company.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.GetCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    GetCompanyRequest request = new GetCompanyRequest
    {
        CompanyName = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]"),
    };
    // Make the request
    Company response = companyServiceClient.GetCompany(request);
    

### GetCompany(string, CallSettings)
    
    
    public virtual Company GetCompany(string name, CallSettings callSettings = null)

Retrieves specified company.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the company to be retrieved. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/api-test-project/tenants/foo/companies/bar".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/tenants/[TENANT]/companies/[COMPANY]";
    // Make the request
    Company response = companyServiceClient.GetCompany(name);
    

### GetCompanyAsync(CompanyName, CallSettings)
    
    
    public virtual Task<Company> GetCompanyAsync(CompanyName name, CallSettings callSettings = null)

Retrieves specified company.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyName)`  
Required. The resource name of the company to be retrieved. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/api-test-project/tenants/foo/companies/bar".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    CompanyName name = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]");
    // Make the request
    Company response = await companyServiceClient.GetCompanyAsync(name);
    

### GetCompanyAsync(CompanyName, CancellationToken)
    
    
    public virtual Task<Company> GetCompanyAsync(CompanyName name, CancellationToken cancellationToken)

Retrieves specified company.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyName)`  
Required. The resource name of the company to be retrieved. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/api-test-project/tenants/foo/companies/bar".  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    CompanyName name = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]");
    // Make the request
    Company response = await companyServiceClient.GetCompanyAsync(name);
    

### GetCompanyAsync(GetCompanyRequest, CallSettings)
    
    
    public virtual Task<Company> GetCompanyAsync(GetCompanyRequest request, CallSettings callSettings = null)

Retrieves specified company.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.GetCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetCompanyRequest request = new GetCompanyRequest
    {
        CompanyName = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]"),
    };
    // Make the request
    Company response = await companyServiceClient.GetCompanyAsync(request);
    

### GetCompanyAsync(GetCompanyRequest, CancellationToken)
    
    
    public virtual Task<Company> GetCompanyAsync(GetCompanyRequest request, CancellationToken cancellationToken)

Retrieves specified company.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.GetCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetCompanyRequest request = new GetCompanyRequest
    {
        CompanyName = CompanyName.FromProjectTenantCompany("[PROJECT]", "[TENANT]", "[COMPANY]"),
    };
    // Make the request
    Company response = await companyServiceClient.GetCompanyAsync(request);
    

### GetCompanyAsync(string, CallSettings)
    
    
    public virtual Task<Company> GetCompanyAsync(string name, CallSettings callSettings = null)

Retrieves specified company.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the company to be retrieved. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/api-test-project/tenants/foo/companies/bar".  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/tenants/[TENANT]/companies/[COMPANY]";
    // Make the request
    Company response = await companyServiceClient.GetCompanyAsync(name);
    

### GetCompanyAsync(string, CancellationToken)
    
    
    public virtual Task<Company> GetCompanyAsync(string name, CancellationToken cancellationToken)

Retrieves specified company.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the company to be retrieved. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/api-test-project/tenants/foo/companies/bar".  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/tenants/[TENANT]/companies/[COMPANY]";
    // Make the request
    Company response = await companyServiceClient.GetCompanyAsync(name);
    

### ListCompanies(ListCompaniesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListCompaniesResponse, Company> ListCompanies(ListCompaniesRequest request, CallSettings callSettings = null)

Lists all companies associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCompaniesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.ListCompaniesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCompaniesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.ListCompaniesResponse)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A pageable sequence of [Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company) resources.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    ListCompaniesRequest request = new ListCompaniesRequest
    {
        ParentAsTenantName = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]"),
        RequireOpenJobs = false,
    };
    // Make the request
    PagedEnumerable<ListCompaniesResponse, Company> response = companyServiceClient.ListCompanies(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Company item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCompaniesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Company item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Company> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Company item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompanies(TenantName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCompaniesResponse, Company> ListCompanies(TenantName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all companies associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.TenantName)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCompaniesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.ListCompaniesResponse)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A pageable sequence of [Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company) resources.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    TenantName parent = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]");
    // Make the request
    PagedEnumerable<ListCompaniesResponse, Company> response = companyServiceClient.ListCompanies(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Company item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCompaniesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Company item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Company> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Company item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompanies(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCompaniesResponse, Company> ListCompanies(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all companies associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCompaniesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.ListCompaniesResponse)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A pageable sequence of [Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company) resources.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/tenants/[TENANT]";
    // Make the request
    PagedEnumerable<ListCompaniesResponse, Company> response = companyServiceClient.ListCompanies(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Company item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCompaniesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Company item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Company> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Company item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompaniesAsync(ListCompaniesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCompaniesResponse, Company> ListCompaniesAsync(ListCompaniesRequest request, CallSettings callSettings = null)

Lists all companies associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCompaniesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.ListCompaniesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCompaniesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.ListCompaniesResponse)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A pageable asynchronous sequence of [Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company) resources.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListCompaniesRequest request = new ListCompaniesRequest
    {
        ParentAsTenantName = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]"),
        RequireOpenJobs = false,
    };
    // Make the request
    PagedAsyncEnumerable<ListCompaniesResponse, Company> response = companyServiceClient.ListCompaniesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Company item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListCompaniesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Company item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Company> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Company item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompaniesAsync(TenantName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCompaniesResponse, Company> ListCompaniesAsync(TenantName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all companies associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[TenantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.TenantName)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCompaniesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.ListCompaniesResponse)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A pageable asynchronous sequence of [Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company) resources.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    TenantName parent = TenantName.FromProjectTenant("[PROJECT]", "[TENANT]");
    // Make the request
    PagedAsyncEnumerable<ListCompaniesResponse, Company> response = companyServiceClient.ListCompaniesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Company item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListCompaniesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Company item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Company> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Company item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompaniesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCompaniesResponse, Company> ListCompaniesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all companies associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCompaniesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.ListCompaniesResponse)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A pageable asynchronous sequence of [Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company) resources.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/tenants/[TENANT]";
    // Make the request
    PagedAsyncEnumerable<ListCompaniesResponse, Company> response = companyServiceClient.ListCompaniesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Company item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListCompaniesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Company item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Company> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Company item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient#Google_Cloud_Talent_V4_CompanyServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient#Google_Cloud_Talent_V4_CompanyServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient#Google_Cloud_Talent_V4_CompanyServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.CompanyServiceClient#Google_Cloud_Talent_V4_CompanyServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateCompany(Company, FieldMask, CallSettings)
    
    
    public virtual Company UpdateCompany(Company company, FieldMask updateMask, CallSettings callSettings = null)

Updates specified company.

**Parameters**  
---  
**Name** | **Description**  
`company` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)`  
Required. The company resource to replace the current resource in the system.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Strongly recommended for the best service experience. If [update_mask][google.cloud.talent.v4.UpdateCompanyRequest.update_mask] is provided, only the specified fields in [company][google.cloud.talent.v4.UpdateCompanyRequest.company] are updated. Otherwise all the fields are updated. A field mask to specify the company fields to be updated. Only top level fields of [Company][google.cloud.talent.v4.Company] are supported.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    Company company = new Company();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Company response = companyServiceClient.UpdateCompany(company, updateMask);
    

### UpdateCompany(UpdateCompanyRequest, CallSettings)
    
    
    public virtual Company UpdateCompany(UpdateCompanyRequest request, CallSettings callSettings = null)

Updates specified company.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.UpdateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = CompanyServiceClient.Create();
    // Initialize request argument(s)
    UpdateCompanyRequest request = new UpdateCompanyRequest
    {
        Company = new Company(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Company response = companyServiceClient.UpdateCompany(request);
    

### UpdateCompanyAsync(Company, FieldMask, CallSettings)
    
    
    public virtual Task<Company> UpdateCompanyAsync(Company company, FieldMask updateMask, CallSettings callSettings = null)

Updates specified company.

**Parameters**  
---  
**Name** | **Description**  
`company` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)`  
Required. The company resource to replace the current resource in the system.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Strongly recommended for the best service experience. If [update_mask][google.cloud.talent.v4.UpdateCompanyRequest.update_mask] is provided, only the specified fields in [company][google.cloud.talent.v4.UpdateCompanyRequest.company] are updated. Otherwise all the fields are updated. A field mask to specify the company fields to be updated. Only top level fields of [Company][google.cloud.talent.v4.Company] are supported.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    Company company = new Company();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Company response = await companyServiceClient.UpdateCompanyAsync(company, updateMask);
    

### UpdateCompanyAsync(Company, FieldMask, CancellationToken)
    
    
    public virtual Task<Company> UpdateCompanyAsync(Company company, FieldMask updateMask, CancellationToken cancellationToken)

Updates specified company.

**Parameters**  
---  
**Name** | **Description**  
`company` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)`  
Required. The company resource to replace the current resource in the system.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Strongly recommended for the best service experience. If [update_mask][google.cloud.talent.v4.UpdateCompanyRequest.update_mask] is provided, only the specified fields in [company][google.cloud.talent.v4.UpdateCompanyRequest.company] are updated. Otherwise all the fields are updated. A field mask to specify the company fields to be updated. Only top level fields of [Company][google.cloud.talent.v4.Company] are supported.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    Company company = new Company();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Company response = await companyServiceClient.UpdateCompanyAsync(company, updateMask);
    

### UpdateCompanyAsync(UpdateCompanyRequest, CallSettings)
    
    
    public virtual Task<Company> UpdateCompanyAsync(UpdateCompanyRequest request, CallSettings callSettings = null)

Updates specified company.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.UpdateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCompanyRequest request = new UpdateCompanyRequest
    {
        Company = new Company(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Company response = await companyServiceClient.UpdateCompanyAsync(request);
    

### UpdateCompanyAsync(UpdateCompanyRequest, CancellationToken)
    
    
    public virtual Task<Company> UpdateCompanyAsync(UpdateCompanyRequest request, CancellationToken cancellationToken)

Updates specified company.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.UpdateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4/latest/Google.Cloud.Talent.V4.Company)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanyServiceClient companyServiceClient = await CompanyServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCompanyRequest request = new UpdateCompanyRequest
    {
        Company = new Company(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Company response = await companyServiceClient.UpdateCompanyAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
