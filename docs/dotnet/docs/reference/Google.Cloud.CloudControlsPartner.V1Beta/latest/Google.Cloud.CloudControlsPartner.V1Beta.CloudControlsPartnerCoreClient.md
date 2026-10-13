---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient
title: Cloud Controls Partner v1beta API - Class CloudControlsPartnerCoreClient (1.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:57.162511+00:00
---

# Cloud Controls Partner v1beta API - Class CloudControlsPartnerCoreClient (1.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Controls Partner v1beta API - Class CloudControlsPartnerCoreClient (1.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta05 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/1.0.0-beta04/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient)


    
    
    public abstract class CloudControlsPartnerCoreClient

Reference documentation and code samples for the Cloud Controls Partner v1beta API class CloudControlsPartnerCoreClient.

CloudControlsPartnerCore client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudControlsPartnerCoreClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[CloudControlsPartnerCoreClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClientImpl)

## Namespace

[Google.Cloud.CloudControlsPartner.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta)

## Assembly

Google.Cloud.CloudControlsPartner.V1Beta.dll

## Remarks

Service describing handlers for resources

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the CloudControlsPartnerCore service, which is a host of "cloudcontrolspartner.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default CloudControlsPartnerCore scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default CloudControlsPartnerCore scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual CloudControlsPartnerCore.CloudControlsPartnerCoreClient GrpcClient { get; }

The underlying gRPC CloudControlsPartnerCore client

**Property Value**  
---  
**Type** | **Description**  
`[CloudControlsPartnerCore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCore)[CloudControlsPartnerCoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCore.CloudControlsPartnerCoreClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static CloudControlsPartnerCoreClient Create()

Synchronously creates a [CloudControlsPartnerCoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudControlsPartnerCoreClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[CloudControlsPartnerCoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient)` | The created [CloudControlsPartnerCoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<CloudControlsPartnerCoreClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [CloudControlsPartnerCoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudControlsPartnerCoreClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudControlsPartnerCoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient)` | The task representing the created [CloudControlsPartnerCoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient).  
  
### CreateCustomer(CreateCustomerRequest, CallSettings)
    
    
    public virtual Customer CreateCustomer(CreateCustomerRequest request, CallSettings callSettings = null)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CreateCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    CreateCustomerRequest request = new CreateCustomerRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Customer = new Customer(),
        CustomerId = "",
    };
    // Make the request
    Customer response = cloudControlsPartnerCoreClient.CreateCustomer(request);
    

### CreateCustomer(OrganizationLocationName, Customer, string, CallSettings)
    
    
    public virtual Customer CreateCustomer(OrganizationLocationName parent, Customer customer, string customerId, CallSettings callSettings = null)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.OrganizationLocationName)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`customer` | `[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)`  
Required. The customer to create.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The customer id to use for the customer, which will become the final component of the customer's resource name. The specified value must be a valid Google cloud organization id.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    Customer customer = new Customer();
    string customerId = "";
    // Make the request
    Customer response = cloudControlsPartnerCoreClient.CreateCustomer(parent, customer, customerId);
    

### CreateCustomer(string, Customer, string, CallSettings)
    
    
    public virtual Customer CreateCustomer(string parent, Customer customer, string customerId, CallSettings callSettings = null)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`customer` | `[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)`  
Required. The customer to create.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The customer id to use for the customer, which will become the final component of the customer's resource name. The specified value must be a valid Google cloud organization id.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    Customer customer = new Customer();
    string customerId = "";
    // Make the request
    Customer response = cloudControlsPartnerCoreClient.CreateCustomer(parent, customer, customerId);
    

### CreateCustomerAsync(CreateCustomerRequest, CallSettings)
    
    
    public virtual Task<Customer> CreateCustomerAsync(CreateCustomerRequest request, CallSettings callSettings = null)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CreateCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    CreateCustomerRequest request = new CreateCustomerRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Customer = new Customer(),
        CustomerId = "",
    };
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.CreateCustomerAsync(request);
    

### CreateCustomerAsync(CreateCustomerRequest, CancellationToken)
    
    
    public virtual Task<Customer> CreateCustomerAsync(CreateCustomerRequest request, CancellationToken cancellationToken)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CreateCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    CreateCustomerRequest request = new CreateCustomerRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Customer = new Customer(),
        CustomerId = "",
    };
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.CreateCustomerAsync(request);
    

### CreateCustomerAsync(OrganizationLocationName, Customer, string, CallSettings)
    
    
    public virtual Task<Customer> CreateCustomerAsync(OrganizationLocationName parent, Customer customer, string customerId, CallSettings callSettings = null)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.OrganizationLocationName)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`customer` | `[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)`  
Required. The customer to create.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The customer id to use for the customer, which will become the final component of the customer's resource name. The specified value must be a valid Google cloud organization id.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    Customer customer = new Customer();
    string customerId = "";
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.CreateCustomerAsync(parent, customer, customerId);
    

### CreateCustomerAsync(OrganizationLocationName, Customer, string, CancellationToken)
    
    
    public virtual Task<Customer> CreateCustomerAsync(OrganizationLocationName parent, Customer customer, string customerId, CancellationToken cancellationToken)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.OrganizationLocationName)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`customer` | `[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)`  
Required. The customer to create.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The customer id to use for the customer, which will become the final component of the customer's resource name. The specified value must be a valid Google cloud organization id.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    Customer customer = new Customer();
    string customerId = "";
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.CreateCustomerAsync(parent, customer, customerId);
    

### CreateCustomerAsync(string, Customer, string, CallSettings)
    
    
    public virtual Task<Customer> CreateCustomerAsync(string parent, Customer customer, string customerId, CallSettings callSettings = null)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`customer` | `[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)`  
Required. The customer to create.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The customer id to use for the customer, which will become the final component of the customer's resource name. The specified value must be a valid Google cloud organization id.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    Customer customer = new Customer();
    string customerId = "";
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.CreateCustomerAsync(parent, customer, customerId);
    

### CreateCustomerAsync(string, Customer, string, CancellationToken)
    
    
    public virtual Task<Customer> CreateCustomerAsync(string parent, Customer customer, string customerId, CancellationToken cancellationToken)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`customer` | `[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)`  
Required. The customer to create.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The customer id to use for the customer, which will become the final component of the customer's resource name. The specified value must be a valid Google cloud organization id.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    Customer customer = new Customer();
    string customerId = "";
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.CreateCustomerAsync(parent, customer, customerId);
    

### DeleteCustomer(CustomerName, CallSettings)
    
    
    public virtual void DeleteCustomer(CustomerName name, CallSettings callSettings = null)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CustomerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CustomerName)`  
Required. name of the resource to be deleted format: name=organizations/_/locations/_ /customers/*  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    CustomerName name = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]");
    // Make the request
    cloudControlsPartnerCoreClient.DeleteCustomer(name);
    

### DeleteCustomer(DeleteCustomerRequest, CallSettings)
    
    
    public virtual void DeleteCustomer(DeleteCustomerRequest request, CallSettings callSettings = null)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.DeleteCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    DeleteCustomerRequest request = new DeleteCustomerRequest
    {
        CustomerName = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]"),
    };
    // Make the request
    cloudControlsPartnerCoreClient.DeleteCustomer(request);
    

### DeleteCustomer(string, CallSettings)
    
    
    public virtual void DeleteCustomer(string name, CallSettings callSettings = null)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. name of the resource to be deleted format: name=organizations/_/locations/_ /customers/*  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]";
    // Make the request
    cloudControlsPartnerCoreClient.DeleteCustomer(name);
    

### DeleteCustomerAsync(CustomerName, CallSettings)
    
    
    public virtual Task DeleteCustomerAsync(CustomerName name, CallSettings callSettings = null)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CustomerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CustomerName)`  
Required. name of the resource to be deleted format: name=organizations/_/locations/_ /customers/*  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    CustomerName name = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]");
    // Make the request
    await cloudControlsPartnerCoreClient.DeleteCustomerAsync(name);
    

### DeleteCustomerAsync(CustomerName, CancellationToken)
    
    
    public virtual Task DeleteCustomerAsync(CustomerName name, CancellationToken cancellationToken)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CustomerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CustomerName)`  
Required. name of the resource to be deleted format: name=organizations/_/locations/_ /customers/*  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    CustomerName name = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]");
    // Make the request
    await cloudControlsPartnerCoreClient.DeleteCustomerAsync(name);
    

### DeleteCustomerAsync(DeleteCustomerRequest, CallSettings)
    
    
    public virtual Task DeleteCustomerAsync(DeleteCustomerRequest request, CallSettings callSettings = null)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.DeleteCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteCustomerRequest request = new DeleteCustomerRequest
    {
        CustomerName = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]"),
    };
    // Make the request
    await cloudControlsPartnerCoreClient.DeleteCustomerAsync(request);
    

### DeleteCustomerAsync(DeleteCustomerRequest, CancellationToken)
    
    
    public virtual Task DeleteCustomerAsync(DeleteCustomerRequest request, CancellationToken cancellationToken)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.DeleteCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteCustomerRequest request = new DeleteCustomerRequest
    {
        CustomerName = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]"),
    };
    // Make the request
    await cloudControlsPartnerCoreClient.DeleteCustomerAsync(request);
    

### DeleteCustomerAsync(string, CallSettings)
    
    
    public virtual Task DeleteCustomerAsync(string name, CallSettings callSettings = null)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. name of the resource to be deleted format: name=organizations/_/locations/_ /customers/*  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]";
    // Make the request
    await cloudControlsPartnerCoreClient.DeleteCustomerAsync(name);
    

### DeleteCustomerAsync(string, CancellationToken)
    
    
    public virtual Task DeleteCustomerAsync(string name, CancellationToken cancellationToken)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. name of the resource to be deleted format: name=organizations/_/locations/_ /customers/*  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]";
    // Make the request
    await cloudControlsPartnerCoreClient.DeleteCustomerAsync(name);
    

### GetCustomer(CustomerName, CallSettings)
    
    
    public virtual Customer GetCustomer(CustomerName name, CallSettings callSettings = null)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CustomerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CustomerName)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    CustomerName name = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]");
    // Make the request
    Customer response = cloudControlsPartnerCoreClient.GetCustomer(name);
    

### GetCustomer(GetCustomerRequest, CallSettings)
    
    
    public virtual Customer GetCustomer(GetCustomerRequest request, CallSettings callSettings = null)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    GetCustomerRequest request = new GetCustomerRequest
    {
        CustomerName = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]"),
    };
    // Make the request
    Customer response = cloudControlsPartnerCoreClient.GetCustomer(request);
    

### GetCustomer(string, CallSettings)
    
    
    public virtual Customer GetCustomer(string name, CallSettings callSettings = null)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]";
    // Make the request
    Customer response = cloudControlsPartnerCoreClient.GetCustomer(name);
    

### GetCustomerAsync(CustomerName, CallSettings)
    
    
    public virtual Task<Customer> GetCustomerAsync(CustomerName name, CallSettings callSettings = null)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CustomerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CustomerName)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    CustomerName name = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]");
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.GetCustomerAsync(name);
    

### GetCustomerAsync(CustomerName, CancellationToken)
    
    
    public virtual Task<Customer> GetCustomerAsync(CustomerName name, CancellationToken cancellationToken)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CustomerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CustomerName)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    CustomerName name = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]");
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.GetCustomerAsync(name);
    

### GetCustomerAsync(GetCustomerRequest, CallSettings)
    
    
    public virtual Task<Customer> GetCustomerAsync(GetCustomerRequest request, CallSettings callSettings = null)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetCustomerRequest request = new GetCustomerRequest
    {
        CustomerName = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]"),
    };
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.GetCustomerAsync(request);
    

### GetCustomerAsync(GetCustomerRequest, CancellationToken)
    
    
    public virtual Task<Customer> GetCustomerAsync(GetCustomerRequest request, CancellationToken cancellationToken)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetCustomerRequest request = new GetCustomerRequest
    {
        CustomerName = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]"),
    };
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.GetCustomerAsync(request);
    

### GetCustomerAsync(string, CallSettings)
    
    
    public virtual Task<Customer> GetCustomerAsync(string name, CallSettings callSettings = null)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]";
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.GetCustomerAsync(name);
    

### GetCustomerAsync(string, CancellationToken)
    
    
    public virtual Task<Customer> GetCustomerAsync(string name, CancellationToken cancellationToken)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]";
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.GetCustomerAsync(name);
    

### GetEkmConnections(EkmConnectionsName, CallSettings)
    
    
    public virtual EkmConnections GetEkmConnections(EkmConnectionsName name, CallSettings callSettings = null)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EkmConnectionsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnectionsName)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EkmConnections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnections)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    EkmConnectionsName name = EkmConnectionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
    // Make the request
    EkmConnections response = cloudControlsPartnerCoreClient.GetEkmConnections(name);
    

### GetEkmConnections(GetEkmConnectionsRequest, CallSettings)
    
    
    public virtual EkmConnections GetEkmConnections(GetEkmConnectionsRequest request, CallSettings callSettings = null)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEkmConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetEkmConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EkmConnections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnections)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    GetEkmConnectionsRequest request = new GetEkmConnectionsRequest
    {
        EkmConnectionsName = EkmConnectionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
    };
    // Make the request
    EkmConnections response = cloudControlsPartnerCoreClient.GetEkmConnections(request);
    

### GetEkmConnections(string, CallSettings)
    
    
    public virtual EkmConnections GetEkmConnections(string name, CallSettings callSettings = null)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EkmConnections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnections)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]/ekmConnections";
    // Make the request
    EkmConnections response = cloudControlsPartnerCoreClient.GetEkmConnections(name);
    

### GetEkmConnectionsAsync(EkmConnectionsName, CallSettings)
    
    
    public virtual Task<EkmConnections> GetEkmConnectionsAsync(EkmConnectionsName name, CallSettings callSettings = null)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EkmConnectionsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnectionsName)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EkmConnections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnections)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    EkmConnectionsName name = EkmConnectionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
    // Make the request
    EkmConnections response = await cloudControlsPartnerCoreClient.GetEkmConnectionsAsync(name);
    

### GetEkmConnectionsAsync(EkmConnectionsName, CancellationToken)
    
    
    public virtual Task<EkmConnections> GetEkmConnectionsAsync(EkmConnectionsName name, CancellationToken cancellationToken)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EkmConnectionsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnectionsName)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EkmConnections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnections)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    EkmConnectionsName name = EkmConnectionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
    // Make the request
    EkmConnections response = await cloudControlsPartnerCoreClient.GetEkmConnectionsAsync(name);
    

### GetEkmConnectionsAsync(GetEkmConnectionsRequest, CallSettings)
    
    
    public virtual Task<EkmConnections> GetEkmConnectionsAsync(GetEkmConnectionsRequest request, CallSettings callSettings = null)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEkmConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetEkmConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EkmConnections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnections)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetEkmConnectionsRequest request = new GetEkmConnectionsRequest
    {
        EkmConnectionsName = EkmConnectionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
    };
    // Make the request
    EkmConnections response = await cloudControlsPartnerCoreClient.GetEkmConnectionsAsync(request);
    

### GetEkmConnectionsAsync(GetEkmConnectionsRequest, CancellationToken)
    
    
    public virtual Task<EkmConnections> GetEkmConnectionsAsync(GetEkmConnectionsRequest request, CancellationToken cancellationToken)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEkmConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetEkmConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EkmConnections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnections)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetEkmConnectionsRequest request = new GetEkmConnectionsRequest
    {
        EkmConnectionsName = EkmConnectionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
    };
    // Make the request
    EkmConnections response = await cloudControlsPartnerCoreClient.GetEkmConnectionsAsync(request);
    

### GetEkmConnectionsAsync(string, CallSettings)
    
    
    public virtual Task<EkmConnections> GetEkmConnectionsAsync(string name, CallSettings callSettings = null)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EkmConnections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnections)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]/ekmConnections";
    // Make the request
    EkmConnections response = await cloudControlsPartnerCoreClient.GetEkmConnectionsAsync(name);
    

### GetEkmConnectionsAsync(string, CancellationToken)
    
    
    public virtual Task<EkmConnections> GetEkmConnectionsAsync(string name, CancellationToken cancellationToken)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EkmConnections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.EkmConnections)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]/ekmConnections";
    // Make the request
    EkmConnections response = await cloudControlsPartnerCoreClient.GetEkmConnectionsAsync(name);
    

### GetPartner(GetPartnerRequest, CallSettings)
    
    
    public virtual Partner GetPartner(GetPartnerRequest request, CallSettings callSettings = null)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPartnerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetPartnerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Partner)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    GetPartnerRequest request = new GetPartnerRequest
    {
        PartnerName = PartnerName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
    };
    // Make the request
    Partner response = cloudControlsPartnerCoreClient.GetPartner(request);
    

### GetPartner(PartnerName, CallSettings)
    
    
    public virtual Partner GetPartner(PartnerName name, CallSettings callSettings = null)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PartnerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerName)`  
Required. Format: `organizations/{organization}/locations/{location}/partner`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Partner)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    PartnerName name = PartnerName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    Partner response = cloudControlsPartnerCoreClient.GetPartner(name);
    

### GetPartner(string, CallSettings)
    
    
    public virtual Partner GetPartner(string name, CallSettings callSettings = null)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/partner`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Partner)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/partner";
    // Make the request
    Partner response = cloudControlsPartnerCoreClient.GetPartner(name);
    

### GetPartnerAsync(GetPartnerRequest, CallSettings)
    
    
    public virtual Task<Partner> GetPartnerAsync(GetPartnerRequest request, CallSettings callSettings = null)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPartnerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetPartnerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Partner)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetPartnerRequest request = new GetPartnerRequest
    {
        PartnerName = PartnerName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
    };
    // Make the request
    Partner response = await cloudControlsPartnerCoreClient.GetPartnerAsync(request);
    

### GetPartnerAsync(GetPartnerRequest, CancellationToken)
    
    
    public virtual Task<Partner> GetPartnerAsync(GetPartnerRequest request, CancellationToken cancellationToken)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPartnerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetPartnerRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Partner)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetPartnerRequest request = new GetPartnerRequest
    {
        PartnerName = PartnerName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
    };
    // Make the request
    Partner response = await cloudControlsPartnerCoreClient.GetPartnerAsync(request);
    

### GetPartnerAsync(PartnerName, CallSettings)
    
    
    public virtual Task<Partner> GetPartnerAsync(PartnerName name, CallSettings callSettings = null)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PartnerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerName)`  
Required. Format: `organizations/{organization}/locations/{location}/partner`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Partner)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    PartnerName name = PartnerName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    Partner response = await cloudControlsPartnerCoreClient.GetPartnerAsync(name);
    

### GetPartnerAsync(PartnerName, CancellationToken)
    
    
    public virtual Task<Partner> GetPartnerAsync(PartnerName name, CancellationToken cancellationToken)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PartnerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerName)`  
Required. Format: `organizations/{organization}/locations/{location}/partner`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Partner)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    PartnerName name = PartnerName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    Partner response = await cloudControlsPartnerCoreClient.GetPartnerAsync(name);
    

### GetPartnerAsync(string, CallSettings)
    
    
    public virtual Task<Partner> GetPartnerAsync(string name, CallSettings callSettings = null)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/partner`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Partner)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/partner";
    // Make the request
    Partner response = await cloudControlsPartnerCoreClient.GetPartnerAsync(name);
    

### GetPartnerAsync(string, CancellationToken)
    
    
    public virtual Task<Partner> GetPartnerAsync(string name, CancellationToken cancellationToken)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/partner`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Partner)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/partner";
    // Make the request
    Partner response = await cloudControlsPartnerCoreClient.GetPartnerAsync(name);
    

### GetPartnerPermissions(GetPartnerPermissionsRequest, CallSettings)
    
    
    public virtual PartnerPermissions GetPartnerPermissions(GetPartnerPermissionsRequest request, CallSettings callSettings = null)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPartnerPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetPartnerPermissionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PartnerPermissions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissions)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    GetPartnerPermissionsRequest request = new GetPartnerPermissionsRequest
    {
        PartnerPermissionsName = PartnerPermissionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
    };
    // Make the request
    PartnerPermissions response = cloudControlsPartnerCoreClient.GetPartnerPermissions(request);
    

### GetPartnerPermissions(PartnerPermissionsName, CallSettings)
    
    
    public virtual PartnerPermissions GetPartnerPermissions(PartnerPermissionsName name, CallSettings callSettings = null)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PartnerPermissionsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissionsName)`  
Required. Name of the resource to get in the format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PartnerPermissions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissions)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    PartnerPermissionsName name = PartnerPermissionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
    // Make the request
    PartnerPermissions response = cloudControlsPartnerCoreClient.GetPartnerPermissions(name);
    

### GetPartnerPermissions(string, CallSettings)
    
    
    public virtual PartnerPermissions GetPartnerPermissions(string name, CallSettings callSettings = null)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource to get in the format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PartnerPermissions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissions)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]/partnerPermissions";
    // Make the request
    PartnerPermissions response = cloudControlsPartnerCoreClient.GetPartnerPermissions(name);
    

### GetPartnerPermissionsAsync(GetPartnerPermissionsRequest, CallSettings)
    
    
    public virtual Task<PartnerPermissions> GetPartnerPermissionsAsync(GetPartnerPermissionsRequest request, CallSettings callSettings = null)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPartnerPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetPartnerPermissionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PartnerPermissions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissions)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetPartnerPermissionsRequest request = new GetPartnerPermissionsRequest
    {
        PartnerPermissionsName = PartnerPermissionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
    };
    // Make the request
    PartnerPermissions response = await cloudControlsPartnerCoreClient.GetPartnerPermissionsAsync(request);
    

### GetPartnerPermissionsAsync(GetPartnerPermissionsRequest, CancellationToken)
    
    
    public virtual Task<PartnerPermissions> GetPartnerPermissionsAsync(GetPartnerPermissionsRequest request, CancellationToken cancellationToken)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPartnerPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetPartnerPermissionsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PartnerPermissions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissions)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetPartnerPermissionsRequest request = new GetPartnerPermissionsRequest
    {
        PartnerPermissionsName = PartnerPermissionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
    };
    // Make the request
    PartnerPermissions response = await cloudControlsPartnerCoreClient.GetPartnerPermissionsAsync(request);
    

### GetPartnerPermissionsAsync(PartnerPermissionsName, CallSettings)
    
    
    public virtual Task<PartnerPermissions> GetPartnerPermissionsAsync(PartnerPermissionsName name, CallSettings callSettings = null)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PartnerPermissionsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissionsName)`  
Required. Name of the resource to get in the format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PartnerPermissions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissions)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    PartnerPermissionsName name = PartnerPermissionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
    // Make the request
    PartnerPermissions response = await cloudControlsPartnerCoreClient.GetPartnerPermissionsAsync(name);
    

### GetPartnerPermissionsAsync(PartnerPermissionsName, CancellationToken)
    
    
    public virtual Task<PartnerPermissions> GetPartnerPermissionsAsync(PartnerPermissionsName name, CancellationToken cancellationToken)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PartnerPermissionsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissionsName)`  
Required. Name of the resource to get in the format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PartnerPermissions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissions)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    PartnerPermissionsName name = PartnerPermissionsName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
    // Make the request
    PartnerPermissions response = await cloudControlsPartnerCoreClient.GetPartnerPermissionsAsync(name);
    

### GetPartnerPermissionsAsync(string, CallSettings)
    
    
    public virtual Task<PartnerPermissions> GetPartnerPermissionsAsync(string name, CallSettings callSettings = null)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource to get in the format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PartnerPermissions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissions)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]/partnerPermissions";
    // Make the request
    PartnerPermissions response = await cloudControlsPartnerCoreClient.GetPartnerPermissionsAsync(name);
    

### GetPartnerPermissionsAsync(string, CancellationToken)
    
    
    public virtual Task<PartnerPermissions> GetPartnerPermissionsAsync(string name, CancellationToken cancellationToken)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource to get in the format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PartnerPermissions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.PartnerPermissions)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]/partnerPermissions";
    // Make the request
    PartnerPermissions response = await cloudControlsPartnerCoreClient.GetPartnerPermissionsAsync(name);
    

### GetWorkload(GetWorkloadRequest, CallSettings)
    
    
    public virtual Workload GetWorkload(GetWorkloadRequest request, CallSettings callSettings = null)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    GetWorkloadRequest request = new GetWorkloadRequest
    {
        WorkloadName = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
    };
    // Make the request
    Workload response = cloudControlsPartnerCoreClient.GetWorkload(request);
    

### GetWorkload(WorkloadName, CallSettings)
    
    
    public virtual Workload GetWorkload(WorkloadName name, CallSettings callSettings = null)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.WorkloadName)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
    // Make the request
    Workload response = cloudControlsPartnerCoreClient.GetWorkload(name);
    

### GetWorkload(string, CallSettings)
    
    
    public virtual Workload GetWorkload(string name, CallSettings callSettings = null)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]";
    // Make the request
    Workload response = cloudControlsPartnerCoreClient.GetWorkload(name);
    

### GetWorkloadAsync(GetWorkloadRequest, CallSettings)
    
    
    public virtual Task<Workload> GetWorkloadAsync(GetWorkloadRequest request, CallSettings callSettings = null)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetWorkloadRequest request = new GetWorkloadRequest
    {
        WorkloadName = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
    };
    // Make the request
    Workload response = await cloudControlsPartnerCoreClient.GetWorkloadAsync(request);
    

### GetWorkloadAsync(GetWorkloadRequest, CancellationToken)
    
    
    public virtual Task<Workload> GetWorkloadAsync(GetWorkloadRequest request, CancellationToken cancellationToken)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    GetWorkloadRequest request = new GetWorkloadRequest
    {
        WorkloadName = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
    };
    // Make the request
    Workload response = await cloudControlsPartnerCoreClient.GetWorkloadAsync(request);
    

### GetWorkloadAsync(WorkloadName, CallSettings)
    
    
    public virtual Task<Workload> GetWorkloadAsync(WorkloadName name, CallSettings callSettings = null)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.WorkloadName)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
    // Make the request
    Workload response = await cloudControlsPartnerCoreClient.GetWorkloadAsync(name);
    

### GetWorkloadAsync(WorkloadName, CancellationToken)
    
    
    public virtual Task<Workload> GetWorkloadAsync(WorkloadName name, CancellationToken cancellationToken)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.WorkloadName)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    WorkloadName name = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
    // Make the request
    Workload response = await cloudControlsPartnerCoreClient.GetWorkloadAsync(name);
    

### GetWorkloadAsync(string, CallSettings)
    
    
    public virtual Task<Workload> GetWorkloadAsync(string name, CallSettings callSettings = null)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]";
    // Make the request
    Workload response = await cloudControlsPartnerCoreClient.GetWorkloadAsync(name);
    

### GetWorkloadAsync(string, CancellationToken)
    
    
    public virtual Task<Workload> GetWorkloadAsync(string name, CancellationToken cancellationToken)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]";
    // Make the request
    Workload response = await cloudControlsPartnerCoreClient.GetWorkloadAsync(name);
    

### ListAccessApprovalRequests(ListAccessApprovalRequestsRequest, CallSettings)
    
    
    [Obsolete]
    public virtual PagedEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> ListAccessApprovalRequests(ListAccessApprovalRequestsRequest request, CallSettings callSettings = null)

Deprecated: Only returns access approval requests directly associated with an assured workload folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAccessApprovalRequestsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListAccessApprovalRequestsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAccessApprovalRequestsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListAccessApprovalRequestsResponse)[AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest)` | A pageable sequence of [AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest) resources.  
**Example**
    
    
                // Create client
                CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
                // Initialize request argument(s)
                ListAccessApprovalRequestsRequest request = new ListAccessApprovalRequestsRequest
                {
                    ParentAsWorkloadName = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
                    Filter = "",
                    OrderBy = "",
                };
                // Make the request
    #pragma warning disable CS0612
                PagedEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> response = cloudControlsPartnerCoreClient.ListAccessApprovalRequests(request);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
                foreach (AccessApprovalRequest item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                foreach (ListAccessApprovalRequestsResponse page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach (AccessApprovalRequest item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<AccessApprovalRequest> singlePage = response.ReadPage(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach (AccessApprovalRequest item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListAccessApprovalRequests(WorkloadName, string, int?, CallSettings)
    
    
    [Obsolete]
    public virtual PagedEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> ListAccessApprovalRequests(WorkloadName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Deprecated: Only returns access approval requests directly associated with an assured workload folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.WorkloadName)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAccessApprovalRequestsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListAccessApprovalRequestsResponse)[AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest)` | A pageable sequence of [AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest) resources.  
**Example**
    
    
                // Create client
                CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
                // Initialize request argument(s)
                WorkloadName parent = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
                // Make the request
    #pragma warning disable CS0612
                PagedEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> response = cloudControlsPartnerCoreClient.ListAccessApprovalRequests(parent);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
                foreach (AccessApprovalRequest item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                foreach (ListAccessApprovalRequestsResponse page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach (AccessApprovalRequest item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<AccessApprovalRequest> singlePage = response.ReadPage(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach (AccessApprovalRequest item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListAccessApprovalRequests(string, string, int?, CallSettings)
    
    
    [Obsolete]
    public virtual PagedEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> ListAccessApprovalRequests(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Deprecated: Only returns access approval requests directly associated with an assured workload folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAccessApprovalRequestsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListAccessApprovalRequestsResponse)[AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest)` | A pageable sequence of [AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest) resources.  
**Example**
    
    
                // Create client
                CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
                // Initialize request argument(s)
                string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]";
                // Make the request
    #pragma warning disable CS0612
                PagedEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> response = cloudControlsPartnerCoreClient.ListAccessApprovalRequests(parent);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
                foreach (AccessApprovalRequest item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                foreach (ListAccessApprovalRequestsResponse page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach (AccessApprovalRequest item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<AccessApprovalRequest> singlePage = response.ReadPage(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach (AccessApprovalRequest item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListAccessApprovalRequestsAsync(ListAccessApprovalRequestsRequest, CallSettings)
    
    
    [Obsolete]
    public virtual PagedAsyncEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> ListAccessApprovalRequestsAsync(ListAccessApprovalRequestsRequest request, CallSettings callSettings = null)

Deprecated: Only returns access approval requests directly associated with an assured workload folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAccessApprovalRequestsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListAccessApprovalRequestsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAccessApprovalRequestsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListAccessApprovalRequestsResponse)[AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest)` | A pageable asynchronous sequence of [AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest) resources.  
**Example**
    
    
                // Create client
                CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
                // Initialize request argument(s)
                ListAccessApprovalRequestsRequest request = new ListAccessApprovalRequestsRequest
                {
                    ParentAsWorkloadName = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]"),
                    Filter = "",
                    OrderBy = "",
                };
                // Make the request
    #pragma warning disable CS0612
                PagedAsyncEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> response = cloudControlsPartnerCoreClient.ListAccessApprovalRequestsAsync(request);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
                await response.ForEachAsync((AccessApprovalRequest item) =>
                {
                    // Do something with each item
                    Console.WriteLine(item);
                });
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                await response.AsRawResponses().ForEachAsync((ListAccessApprovalRequestsResponse page) =>
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach (AccessApprovalRequest item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                });
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<AccessApprovalRequest> singlePage = await response.ReadPageAsync(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach (AccessApprovalRequest item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListAccessApprovalRequestsAsync(WorkloadName, string, int?, CallSettings)
    
    
    [Obsolete]
    public virtual PagedAsyncEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> ListAccessApprovalRequestsAsync(WorkloadName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Deprecated: Only returns access approval requests directly associated with an assured workload folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.WorkloadName)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAccessApprovalRequestsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListAccessApprovalRequestsResponse)[AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest)` | A pageable asynchronous sequence of [AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest) resources.  
**Example**
    
    
                // Create client
                CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
                // Initialize request argument(s)
                WorkloadName parent = WorkloadName.FromOrganizationLocationCustomerWorkload("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]", "[WORKLOAD]");
                // Make the request
    #pragma warning disable CS0612
                PagedAsyncEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> response = cloudControlsPartnerCoreClient.ListAccessApprovalRequestsAsync(parent);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
                await response.ForEachAsync((AccessApprovalRequest item) =>
                {
                    // Do something with each item
                    Console.WriteLine(item);
                });
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                await response.AsRawResponses().ForEachAsync((ListAccessApprovalRequestsResponse page) =>
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach (AccessApprovalRequest item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                });
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<AccessApprovalRequest> singlePage = await response.ReadPageAsync(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach (AccessApprovalRequest item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListAccessApprovalRequestsAsync(string, string, int?, CallSettings)
    
    
    [Obsolete]
    public virtual PagedAsyncEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> ListAccessApprovalRequestsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Deprecated: Only returns access approval requests directly associated with an assured workload folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAccessApprovalRequestsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListAccessApprovalRequestsResponse)[AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest)` | A pageable asynchronous sequence of [AccessApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.AccessApprovalRequest) resources.  
**Example**
    
    
                // Create client
                CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
                // Initialize request argument(s)
                string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]/workloads/[WORKLOAD]";
                // Make the request
    #pragma warning disable CS0612
                PagedAsyncEnumerable<ListAccessApprovalRequestsResponse, AccessApprovalRequest> response = cloudControlsPartnerCoreClient.ListAccessApprovalRequestsAsync(parent);
    #pragma warning restore CS0612
    
                // Iterate over all response items, lazily performing RPCs as required
                await response.ForEachAsync((AccessApprovalRequest item) =>
                {
                    // Do something with each item
                    Console.WriteLine(item);
                });
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                await response.AsRawResponses().ForEachAsync((ListAccessApprovalRequestsResponse page) =>
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach (AccessApprovalRequest item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                });
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<AccessApprovalRequest> singlePage = await response.ReadPageAsync(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach (AccessApprovalRequest item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
    

### ListCustomers(ListCustomersRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListCustomersResponse, Customer> ListCustomers(ListCustomersRequest request, CallSettings callSettings = null)

Lists customers of a partner identified by its Google Cloud organization ID

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListCustomersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCustomersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListCustomersResponse)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A pageable sequence of [Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    ListCustomersRequest request = new ListCustomersRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListCustomersResponse, Customer> response = cloudControlsPartnerCoreClient.ListCustomers(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Customer item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCustomersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Customer item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Customer> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Customer item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCustomers(OrganizationLocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCustomersResponse, Customer> ListCustomers(OrganizationLocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists customers of a partner identified by its Google Cloud organization ID

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.OrganizationLocationName)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCustomersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListCustomersResponse)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A pageable sequence of [Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListCustomersResponse, Customer> response = cloudControlsPartnerCoreClient.ListCustomers(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Customer item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCustomersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Customer item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Customer> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Customer item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCustomers(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCustomersResponse, Customer> ListCustomers(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists customers of a partner identified by its Google Cloud organization ID

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCustomersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListCustomersResponse)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A pageable sequence of [Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListCustomersResponse, Customer> response = cloudControlsPartnerCoreClient.ListCustomers(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Customer item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCustomersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Customer item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Customer> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Customer item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCustomersAsync(ListCustomersRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCustomersResponse, Customer> ListCustomersAsync(ListCustomersRequest request, CallSettings callSettings = null)

Lists customers of a partner identified by its Google Cloud organization ID

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListCustomersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCustomersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListCustomersResponse)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A pageable asynchronous sequence of [Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    ListCustomersRequest request = new ListCustomersRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListCustomersResponse, Customer> response = cloudControlsPartnerCoreClient.ListCustomersAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Customer item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListCustomersResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Customer item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Customer> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Customer item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCustomersAsync(OrganizationLocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCustomersResponse, Customer> ListCustomersAsync(OrganizationLocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists customers of a partner identified by its Google Cloud organization ID

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.OrganizationLocationName)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCustomersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListCustomersResponse)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A pageable asynchronous sequence of [Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListCustomersResponse, Customer> response = cloudControlsPartnerCoreClient.ListCustomersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Customer item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListCustomersResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Customer item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Customer> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Customer item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCustomersAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCustomersResponse, Customer> ListCustomersAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists customers of a partner identified by its Google Cloud organization ID

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCustomersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListCustomersResponse)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A pageable asynchronous sequence of [Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListCustomersResponse, Customer> response = cloudControlsPartnerCoreClient.ListCustomersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Customer item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListCustomersResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Customer item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Customer> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Customer item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(CustomerName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, Workload> ListWorkloads(CustomerName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists customer workloads for a given customer org id

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CustomerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CustomerName)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A pageable sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    CustomerName parent = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]");
    // Make the request
    PagedEnumerable<ListWorkloadsResponse, Workload> response = cloudControlsPartnerCoreClient.ListWorkloads(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Workload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(ListWorkloadsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, Workload> ListWorkloads(ListWorkloadsRequest request, CallSettings callSettings = null)

Lists customer workloads for a given customer org id

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A pageable sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    ListWorkloadsRequest request = new ListWorkloadsRequest
    {
        ParentAsCustomerName = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListWorkloadsResponse, Workload> response = cloudControlsPartnerCoreClient.ListWorkloads(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Workload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, Workload> ListWorkloads(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists customer workloads for a given customer org id

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A pageable sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]";
    // Make the request
    PagedEnumerable<ListWorkloadsResponse, Workload> response = cloudControlsPartnerCoreClient.ListWorkloads(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Workload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloadsAsync(CustomerName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, Workload> ListWorkloadsAsync(CustomerName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists customer workloads for a given customer org id

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CustomerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CustomerName)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A pageable asynchronous sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    CustomerName parent = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]");
    // Make the request
    PagedAsyncEnumerable<ListWorkloadsResponse, Workload> response = cloudControlsPartnerCoreClient.ListWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Workload item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListWorkloadsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloadsAsync(ListWorkloadsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, Workload> ListWorkloadsAsync(ListWorkloadsRequest request, CallSettings callSettings = null)

Lists customer workloads for a given customer org id

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A pageable asynchronous sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    ListWorkloadsRequest request = new ListWorkloadsRequest
    {
        ParentAsCustomerName = CustomerName.FromOrganizationLocationCustomer("[ORGANIZATION]", "[LOCATION]", "[CUSTOMER]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListWorkloadsResponse, Workload> response = cloudControlsPartnerCoreClient.ListWorkloadsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Workload item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListWorkloadsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloadsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, Workload> ListWorkloadsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists customer workloads for a given customer org id

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.ListWorkloadsResponse)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload)` | A pageable asynchronous sequence of [Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Workload) resources.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]/customers/[CUSTOMER]";
    // Make the request
    PagedAsyncEnumerable<ListWorkloadsResponse, Workload> response = cloudControlsPartnerCoreClient.ListWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Workload item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListWorkloadsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Workload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Workload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Workload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient#Google_Cloud_CloudControlsPartner_V1Beta_CloudControlsPartnerCoreClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient#Google_Cloud_CloudControlsPartner_V1Beta_CloudControlsPartnerCoreClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient#Google_Cloud_CloudControlsPartner_V1Beta_CloudControlsPartnerCoreClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.CloudControlsPartnerCoreClient#Google_Cloud_CloudControlsPartner_V1Beta_CloudControlsPartnerCoreClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateCustomer(Customer, FieldMask, CallSettings)
    
    
    public virtual Customer UpdateCustomer(Customer customer, FieldMask updateMask, CallSettings callSettings = null)

Update details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`customer` | `[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)`  
Required. The customer to update Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    Customer customer = new Customer();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Customer response = cloudControlsPartnerCoreClient.UpdateCustomer(customer, updateMask);
    

### UpdateCustomer(UpdateCustomerRequest, CallSettings)
    
    
    public virtual Customer UpdateCustomer(UpdateCustomerRequest request, CallSettings callSettings = null)

Update details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.UpdateCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = CloudControlsPartnerCoreClient.Create();
    // Initialize request argument(s)
    UpdateCustomerRequest request = new UpdateCustomerRequest
    {
        Customer = new Customer(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Customer response = cloudControlsPartnerCoreClient.UpdateCustomer(request);
    

### UpdateCustomerAsync(Customer, FieldMask, CallSettings)
    
    
    public virtual Task<Customer> UpdateCustomerAsync(Customer customer, FieldMask updateMask, CallSettings callSettings = null)

Update details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`customer` | `[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)`  
Required. The customer to update Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    Customer customer = new Customer();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.UpdateCustomerAsync(customer, updateMask);
    

### UpdateCustomerAsync(Customer, FieldMask, CancellationToken)
    
    
    public virtual Task<Customer> UpdateCustomerAsync(Customer customer, FieldMask updateMask, CancellationToken cancellationToken)

Update details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`customer` | `[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)`  
Required. The customer to update Format: `organizations/{organization}/locations/{location}/customers/{customer}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    Customer customer = new Customer();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.UpdateCustomerAsync(customer, updateMask);
    

### UpdateCustomerAsync(UpdateCustomerRequest, CallSettings)
    
    
    public virtual Task<Customer> UpdateCustomerAsync(UpdateCustomerRequest request, CallSettings callSettings = null)

Update details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.UpdateCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCustomerRequest request = new UpdateCustomerRequest
    {
        Customer = new Customer(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.UpdateCustomerAsync(request);
    

### UpdateCustomerAsync(UpdateCustomerRequest, CancellationToken)
    
    
    public virtual Task<Customer> UpdateCustomerAsync(UpdateCustomerRequest request, CancellationToken cancellationToken)

Update details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.UpdateCustomerRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Customer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1Beta/latest/Google.Cloud.CloudControlsPartner.V1Beta.Customer)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudControlsPartnerCoreClient cloudControlsPartnerCoreClient = await CloudControlsPartnerCoreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCustomerRequest request = new UpdateCustomerRequest
    {
        Customer = new Customer(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Customer response = await cloudControlsPartnerCoreClient.UpdateCustomerAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
