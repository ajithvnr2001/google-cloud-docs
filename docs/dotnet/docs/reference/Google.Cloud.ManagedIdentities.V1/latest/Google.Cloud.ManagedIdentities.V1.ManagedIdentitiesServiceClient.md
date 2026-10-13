---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient
title: Managed Service for Microsoft Active Directory v1 API - Class ManagedIdentitiesServiceClient (3.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:46.547692+00:00
---

# Managed Service for Microsoft Active Directory v1 API - Class ManagedIdentitiesServiceClient (3.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Microsoft Active Directory v1 API - Class ManagedIdentitiesServiceClient (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/3.3.0/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/3.2.0/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/3.1.0/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/3.0.0/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/2.3.0/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/2.2.0/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient)


    
    
    public abstract class ManagedIdentitiesServiceClient

Reference documentation and code samples for the Managed Service for Microsoft Active Directory v1 API class ManagedIdentitiesServiceClient.

ManagedIdentitiesService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ManagedIdentitiesServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ManagedIdentitiesServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClientImpl)

## Namespace

[Google.Cloud.ManagedIdentities.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1)

## Assembly

Google.Cloud.ManagedIdentities.V1.dll

## Remarks

API Overview

The `managedidentites.googleapis.com` service implements the Google Cloud Managed Identites API for identity services (e.g. Microsoft Active Directory).

The Managed Identities service provides methods to manage (create/read/update/delete) domains, reset managed identities admin password, add/remove domain controllers in GCP regions and add/remove VPC peering.

Data Model

The Managed Identities service exposes the following resources:

  * Locations as global, named as follows: `projects/{project_id}/locations/global`.

  * Domains, named as follows: `/projects/{project_id}/locations/global/domain/{domain_name}`.




The `{domain_name}` refers to fully qualified domain name in the customer project e.g. mydomain.myorganization.com, with the following restrictions:

  * Must contain only lowercase letters, numbers, periods and hyphens.
  * Must start with a letter.
  * Must contain between 2-64 characters.
  * Must end with a number or a letter.
  * Must not start with period.
  * First segement length (mydomain form example above) shouldn't exceed 15 chars.
  * The last segment cannot be fully numeric.
  * Must be unique within the customer project.



## Properties 

### AttachTrustOperationsClient
    
    
    public virtual OperationsClient AttachTrustOperationsClient { get; }

The long-running operations client for `AttachTrust`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateMicrosoftAdDomainOperationsClient
    
    
    public virtual OperationsClient CreateMicrosoftAdDomainOperationsClient { get; }

The long-running operations client for `CreateMicrosoftAdDomain`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ManagedIdentitiesService service, which is a host of "managedidentities.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ManagedIdentitiesService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ManagedIdentitiesService scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteDomainOperationsClient
    
    
    public virtual OperationsClient DeleteDomainOperationsClient { get; }

The long-running operations client for `DeleteDomain`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DetachTrustOperationsClient
    
    
    public virtual OperationsClient DetachTrustOperationsClient { get; }

The long-running operations client for `DetachTrust`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual ManagedIdentitiesService.ManagedIdentitiesServiceClient GrpcClient { get; }

The underlying gRPC ManagedIdentitiesService client

**Property Value**  
---  
**Type** | **Description**  
`[ManagedIdentitiesService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesService)[ManagedIdentitiesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesService.ManagedIdentitiesServiceClient)` |   
  
### ReconfigureTrustOperationsClient
    
    
    public virtual OperationsClient ReconfigureTrustOperationsClient { get; }

The long-running operations client for `ReconfigureTrust`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
### UpdateDomainOperationsClient
    
    
    public virtual OperationsClient UpdateDomainOperationsClient { get; }

The long-running operations client for `UpdateDomain`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ValidateTrustOperationsClient
    
    
    public virtual OperationsClient ValidateTrustOperationsClient { get; }

The long-running operations client for `ValidateTrust`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### AttachTrust(AttachTrustRequest, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> AttachTrust(AttachTrustRequest request, CallSettings callSettings = null)

Adds an AD trust to a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AttachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    AttachTrustRequest request = new AttachTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        Trust = new Trust(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.AttachTrust(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceAttachTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### AttachTrust(DomainName, Trust, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> AttachTrust(DomainName name, Trust trust, CallSettings callSettings = null)

Adds an AD trust to a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.AttachTrust(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceAttachTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### AttachTrust(string, Trust, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> AttachTrust(string name, Trust trust, CallSettings callSettings = null)

Adds an AD trust to a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.AttachTrust(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceAttachTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### AttachTrustAsync(AttachTrustRequest, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> AttachTrustAsync(AttachTrustRequest request, CallSettings callSettings = null)

Adds an AD trust to a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AttachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    AttachTrustRequest request = new AttachTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        Trust = new Trust(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.AttachTrustAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceAttachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### AttachTrustAsync(AttachTrustRequest, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> AttachTrustAsync(AttachTrustRequest request, CancellationToken cancellationToken)

Adds an AD trust to a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AttachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    AttachTrustRequest request = new AttachTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        Trust = new Trust(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.AttachTrustAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceAttachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### AttachTrustAsync(DomainName, Trust, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> AttachTrustAsync(DomainName name, Trust trust, CallSettings callSettings = null)

Adds an AD trust to a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.AttachTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceAttachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### AttachTrustAsync(DomainName, Trust, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> AttachTrustAsync(DomainName name, Trust trust, CancellationToken cancellationToken)

Adds an AD trust to a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.AttachTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceAttachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### AttachTrustAsync(string, Trust, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> AttachTrustAsync(string name, Trust trust, CallSettings callSettings = null)

Adds an AD trust to a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.AttachTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceAttachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### AttachTrustAsync(string, Trust, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> AttachTrustAsync(string name, Trust trust, CancellationToken cancellationToken)

Adds an AD trust to a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.AttachTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceAttachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static ManagedIdentitiesServiceClient Create()

Synchronously creates a [ManagedIdentitiesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ManagedIdentitiesServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ManagedIdentitiesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient)` | The created [ManagedIdentitiesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ManagedIdentitiesServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ManagedIdentitiesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ManagedIdentitiesServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedIdentitiesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient)` | The task representing the created [ManagedIdentitiesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient).  
  
### CreateMicrosoftAdDomain(LocationName, string, Domain, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> CreateMicrosoftAdDomain(LocationName parent, string domainName, Domain domain, CallSettings callSettings = null)

Creates a Microsoft AD domain.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource project name and location using the form: `projects/{project_id}/locations/global`  
`domainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully qualified domain name. e.g. mydomain.myorganization.com, with the following restrictions:

  * Must contain only lowercase letters, numbers, periods and hyphens.
  * Must start with a letter.
  * Must contain between 2-64 characters.
  * Must end with a number or a letter.
  * Must not start with period.
  * First segement length (mydomain form example above) shouldn't exceed 15 chars.
  * The last segment cannot be fully numeric.
  * Must be unique within the customer project.

  
`domain` | `[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)`  
Required. A Managed Identity domain resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string domainName = "";
    Domain domain = new Domain();
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.CreateMicrosoftAdDomain(parent, domainName, domain);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceCreateMicrosoftAdDomain(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### CreateMicrosoftAdDomain(CreateMicrosoftAdDomainRequest, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> CreateMicrosoftAdDomain(CreateMicrosoftAdDomainRequest request, CallSettings callSettings = null)

Creates a Microsoft AD domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMicrosoftAdDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.CreateMicrosoftAdDomainRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    CreateMicrosoftAdDomainRequest request = new CreateMicrosoftAdDomainRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        DomainName = "",
        Domain = new Domain(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.CreateMicrosoftAdDomain(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceCreateMicrosoftAdDomain(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### CreateMicrosoftAdDomain(string, string, Domain, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> CreateMicrosoftAdDomain(string parent, string domainName, Domain domain, CallSettings callSettings = null)

Creates a Microsoft AD domain.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource project name and location using the form: `projects/{project_id}/locations/global`  
`domainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully qualified domain name. e.g. mydomain.myorganization.com, with the following restrictions:

  * Must contain only lowercase letters, numbers, periods and hyphens.
  * Must start with a letter.
  * Must contain between 2-64 characters.
  * Must end with a number or a letter.
  * Must not start with period.
  * First segement length (mydomain form example above) shouldn't exceed 15 chars.
  * The last segment cannot be fully numeric.
  * Must be unique within the customer project.

  
`domain` | `[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)`  
Required. A Managed Identity domain resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string domainName = "";
    Domain domain = new Domain();
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.CreateMicrosoftAdDomain(parent, domainName, domain);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceCreateMicrosoftAdDomain(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### CreateMicrosoftAdDomainAsync(LocationName, string, Domain, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> CreateMicrosoftAdDomainAsync(LocationName parent, string domainName, Domain domain, CallSettings callSettings = null)

Creates a Microsoft AD domain.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource project name and location using the form: `projects/{project_id}/locations/global`  
`domainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully qualified domain name. e.g. mydomain.myorganization.com, with the following restrictions:

  * Must contain only lowercase letters, numbers, periods and hyphens.
  * Must start with a letter.
  * Must contain between 2-64 characters.
  * Must end with a number or a letter.
  * Must not start with period.
  * First segement length (mydomain form example above) shouldn't exceed 15 chars.
  * The last segment cannot be fully numeric.
  * Must be unique within the customer project.

  
`domain` | `[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)`  
Required. A Managed Identity domain resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string domainName = "";
    Domain domain = new Domain();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.CreateMicrosoftAdDomainAsync(parent, domainName, domain);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceCreateMicrosoftAdDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### CreateMicrosoftAdDomainAsync(LocationName, string, Domain, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> CreateMicrosoftAdDomainAsync(LocationName parent, string domainName, Domain domain, CancellationToken cancellationToken)

Creates a Microsoft AD domain.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource project name and location using the form: `projects/{project_id}/locations/global`  
`domainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully qualified domain name. e.g. mydomain.myorganization.com, with the following restrictions:

  * Must contain only lowercase letters, numbers, periods and hyphens.
  * Must start with a letter.
  * Must contain between 2-64 characters.
  * Must end with a number or a letter.
  * Must not start with period.
  * First segement length (mydomain form example above) shouldn't exceed 15 chars.
  * The last segment cannot be fully numeric.
  * Must be unique within the customer project.

  
`domain` | `[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)`  
Required. A Managed Identity domain resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string domainName = "";
    Domain domain = new Domain();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.CreateMicrosoftAdDomainAsync(parent, domainName, domain);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceCreateMicrosoftAdDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### CreateMicrosoftAdDomainAsync(CreateMicrosoftAdDomainRequest, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> CreateMicrosoftAdDomainAsync(CreateMicrosoftAdDomainRequest request, CallSettings callSettings = null)

Creates a Microsoft AD domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMicrosoftAdDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.CreateMicrosoftAdDomainRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateMicrosoftAdDomainRequest request = new CreateMicrosoftAdDomainRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        DomainName = "",
        Domain = new Domain(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.CreateMicrosoftAdDomainAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceCreateMicrosoftAdDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### CreateMicrosoftAdDomainAsync(CreateMicrosoftAdDomainRequest, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> CreateMicrosoftAdDomainAsync(CreateMicrosoftAdDomainRequest request, CancellationToken cancellationToken)

Creates a Microsoft AD domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMicrosoftAdDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.CreateMicrosoftAdDomainRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateMicrosoftAdDomainRequest request = new CreateMicrosoftAdDomainRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        DomainName = "",
        Domain = new Domain(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.CreateMicrosoftAdDomainAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceCreateMicrosoftAdDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### CreateMicrosoftAdDomainAsync(string, string, Domain, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> CreateMicrosoftAdDomainAsync(string parent, string domainName, Domain domain, CallSettings callSettings = null)

Creates a Microsoft AD domain.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource project name and location using the form: `projects/{project_id}/locations/global`  
`domainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully qualified domain name. e.g. mydomain.myorganization.com, with the following restrictions:

  * Must contain only lowercase letters, numbers, periods and hyphens.
  * Must start with a letter.
  * Must contain between 2-64 characters.
  * Must end with a number or a letter.
  * Must not start with period.
  * First segement length (mydomain form example above) shouldn't exceed 15 chars.
  * The last segment cannot be fully numeric.
  * Must be unique within the customer project.

  
`domain` | `[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)`  
Required. A Managed Identity domain resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string domainName = "";
    Domain domain = new Domain();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.CreateMicrosoftAdDomainAsync(parent, domainName, domain);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceCreateMicrosoftAdDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### CreateMicrosoftAdDomainAsync(string, string, Domain, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> CreateMicrosoftAdDomainAsync(string parent, string domainName, Domain domain, CancellationToken cancellationToken)

Creates a Microsoft AD domain.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource project name and location using the form: `projects/{project_id}/locations/global`  
`domainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully qualified domain name. e.g. mydomain.myorganization.com, with the following restrictions:

  * Must contain only lowercase letters, numbers, periods and hyphens.
  * Must start with a letter.
  * Must contain between 2-64 characters.
  * Must end with a number or a letter.
  * Must not start with period.
  * First segement length (mydomain form example above) shouldn't exceed 15 chars.
  * The last segment cannot be fully numeric.
  * Must be unique within the customer project.

  
`domain` | `[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)`  
Required. A Managed Identity domain resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string domainName = "";
    Domain domain = new Domain();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.CreateMicrosoftAdDomainAsync(parent, domainName, domain);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceCreateMicrosoftAdDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDomain(DeleteDomainRequest, CallSettings)
    
    
    public virtual Operation<Empty, OpMetadata> DeleteDomain(DeleteDomainRequest request, CallSettings callSettings = null)

Deletes a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DeleteDomainRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    DeleteDomainRequest request = new DeleteDomainRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
    };
    // Make the request
    Operation<Empty, OpMetadata> response = managedIdentitiesServiceClient.DeleteDomain(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceDeleteDomain(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDomain(DomainName, CallSettings)
    
    
    public virtual Operation<Empty, OpMetadata> DeleteDomain(DomainName name, CallSettings callSettings = null)

Deletes a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    // Make the request
    Operation<Empty, OpMetadata> response = managedIdentitiesServiceClient.DeleteDomain(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceDeleteDomain(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDomain(string, CallSettings)
    
    
    public virtual Operation<Empty, OpMetadata> DeleteDomain(string name, CallSettings callSettings = null)

Deletes a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    // Make the request
    Operation<Empty, OpMetadata> response = managedIdentitiesServiceClient.DeleteDomain(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceDeleteDomain(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDomainAsync(DeleteDomainRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OpMetadata>> DeleteDomainAsync(DeleteDomainRequest request, CallSettings callSettings = null)

Deletes a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DeleteDomainRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDomainRequest request = new DeleteDomainRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
    };
    // Make the request
    Operation<Empty, OpMetadata> response = await managedIdentitiesServiceClient.DeleteDomainAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDeleteDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDomainAsync(DeleteDomainRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OpMetadata>> DeleteDomainAsync(DeleteDomainRequest request, CancellationToken cancellationToken)

Deletes a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DeleteDomainRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDomainRequest request = new DeleteDomainRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
    };
    // Make the request
    Operation<Empty, OpMetadata> response = await managedIdentitiesServiceClient.DeleteDomainAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDeleteDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDomainAsync(DomainName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OpMetadata>> DeleteDomainAsync(DomainName name, CallSettings callSettings = null)

Deletes a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    // Make the request
    Operation<Empty, OpMetadata> response = await managedIdentitiesServiceClient.DeleteDomainAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDeleteDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDomainAsync(DomainName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OpMetadata>> DeleteDomainAsync(DomainName name, CancellationToken cancellationToken)

Deletes a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    // Make the request
    Operation<Empty, OpMetadata> response = await managedIdentitiesServiceClient.DeleteDomainAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDeleteDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDomainAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OpMetadata>> DeleteDomainAsync(string name, CallSettings callSettings = null)

Deletes a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    // Make the request
    Operation<Empty, OpMetadata> response = await managedIdentitiesServiceClient.DeleteDomainAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDeleteDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDomainAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OpMetadata>> DeleteDomainAsync(string name, CancellationToken cancellationToken)

Deletes a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    // Make the request
    Operation<Empty, OpMetadata> response = await managedIdentitiesServiceClient.DeleteDomainAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDeleteDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DetachTrust(DetachTrustRequest, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> DetachTrust(DetachTrustRequest request, CallSettings callSettings = null)

Removes an AD trust.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DetachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DetachTrustRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    DetachTrustRequest request = new DetachTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        Trust = new Trust(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.DetachTrust(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceDetachTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### DetachTrust(DomainName, Trust, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> DetachTrust(DomainName name, Trust trust, CallSettings callSettings = null)

Removes an AD trust.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource to removed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.DetachTrust(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceDetachTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### DetachTrust(string, Trust, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> DetachTrust(string name, Trust trust, CallSettings callSettings = null)

Removes an AD trust.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource to removed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.DetachTrust(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceDetachTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### DetachTrustAsync(DetachTrustRequest, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> DetachTrustAsync(DetachTrustRequest request, CallSettings callSettings = null)

Removes an AD trust.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DetachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DetachTrustRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DetachTrustRequest request = new DetachTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        Trust = new Trust(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.DetachTrustAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDetachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### DetachTrustAsync(DetachTrustRequest, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> DetachTrustAsync(DetachTrustRequest request, CancellationToken cancellationToken)

Removes an AD trust.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DetachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DetachTrustRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DetachTrustRequest request = new DetachTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        Trust = new Trust(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.DetachTrustAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDetachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### DetachTrustAsync(DomainName, Trust, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> DetachTrustAsync(DomainName name, Trust trust, CallSettings callSettings = null)

Removes an AD trust.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource to removed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.DetachTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDetachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### DetachTrustAsync(DomainName, Trust, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> DetachTrustAsync(DomainName name, Trust trust, CancellationToken cancellationToken)

Removes an AD trust.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource to removed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.DetachTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDetachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### DetachTrustAsync(string, Trust, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> DetachTrustAsync(string name, Trust trust, CallSettings callSettings = null)

Removes an AD trust.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource to removed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.DetachTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDetachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### DetachTrustAsync(string, Trust, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> DetachTrustAsync(string name, Trust trust, CancellationToken cancellationToken)

Removes an AD trust.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust resource to removed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.DetachTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceDetachTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### GetDomain(DomainName, CallSettings)
    
    
    public virtual Domain GetDomain(DomainName name, CallSettings callSettings = null)

Gets information about a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    // Make the request
    Domain response = managedIdentitiesServiceClient.GetDomain(name);
    

### GetDomain(GetDomainRequest, CallSettings)
    
    
    public virtual Domain GetDomain(GetDomainRequest request, CallSettings callSettings = null)

Gets information about a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.GetDomainRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    GetDomainRequest request = new GetDomainRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
    };
    // Make the request
    Domain response = managedIdentitiesServiceClient.GetDomain(request);
    

### GetDomain(string, CallSettings)
    
    
    public virtual Domain GetDomain(string name, CallSettings callSettings = null)

Gets information about a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    // Make the request
    Domain response = managedIdentitiesServiceClient.GetDomain(name);
    

### GetDomainAsync(DomainName, CallSettings)
    
    
    public virtual Task<Domain> GetDomainAsync(DomainName name, CallSettings callSettings = null)

Gets information about a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    // Make the request
    Domain response = await managedIdentitiesServiceClient.GetDomainAsync(name);
    

### GetDomainAsync(DomainName, CancellationToken)
    
    
    public virtual Task<Domain> GetDomainAsync(DomainName name, CancellationToken cancellationToken)

Gets information about a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    // Make the request
    Domain response = await managedIdentitiesServiceClient.GetDomainAsync(name);
    

### GetDomainAsync(GetDomainRequest, CallSettings)
    
    
    public virtual Task<Domain> GetDomainAsync(GetDomainRequest request, CallSettings callSettings = null)

Gets information about a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.GetDomainRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDomainRequest request = new GetDomainRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
    };
    // Make the request
    Domain response = await managedIdentitiesServiceClient.GetDomainAsync(request);
    

### GetDomainAsync(GetDomainRequest, CancellationToken)
    
    
    public virtual Task<Domain> GetDomainAsync(GetDomainRequest request, CancellationToken cancellationToken)

Gets information about a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.GetDomainRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDomainRequest request = new GetDomainRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
    };
    // Make the request
    Domain response = await managedIdentitiesServiceClient.GetDomainAsync(request);
    

### GetDomainAsync(string, CallSettings)
    
    
    public virtual Task<Domain> GetDomainAsync(string name, CallSettings callSettings = null)

Gets information about a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    // Make the request
    Domain response = await managedIdentitiesServiceClient.GetDomainAsync(name);
    

### GetDomainAsync(string, CancellationToken)
    
    
    public virtual Task<Domain> GetDomainAsync(string name, CancellationToken cancellationToken)

Gets information about a domain.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    // Make the request
    Domain response = await managedIdentitiesServiceClient.GetDomainAsync(name);
    

### ListDomains(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDomainsResponse, Domain> ListDomains(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists domains in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the domain location using the form: `projects/{project_id}/locations/global`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDomainsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ListDomainsResponse)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A pageable sequence of [Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain) resources.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListDomainsResponse, Domain> response = managedIdentitiesServiceClient.ListDomains(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Domain item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDomainsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Domain item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Domain> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Domain item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDomains(ListDomainsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDomainsResponse, Domain> ListDomains(ListDomainsRequest request, CallSettings callSettings = null)

Lists domains in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDomainsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ListDomainsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDomainsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ListDomainsResponse)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A pageable sequence of [Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain) resources.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    ListDomainsRequest request = new ListDomainsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListDomainsResponse, Domain> response = managedIdentitiesServiceClient.ListDomains(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Domain item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDomainsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Domain item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Domain> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Domain item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDomains(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDomainsResponse, Domain> ListDomains(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists domains in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the domain location using the form: `projects/{project_id}/locations/global`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDomainsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ListDomainsResponse)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A pageable sequence of [Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain) resources.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListDomainsResponse, Domain> response = managedIdentitiesServiceClient.ListDomains(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Domain item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDomainsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Domain item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Domain> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Domain item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDomainsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDomainsResponse, Domain> ListDomainsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists domains in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the domain location using the form: `projects/{project_id}/locations/global`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDomainsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ListDomainsResponse)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A pageable asynchronous sequence of [Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain) resources.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListDomainsResponse, Domain> response = managedIdentitiesServiceClient.ListDomainsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Domain item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListDomainsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Domain item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Domain> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Domain item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDomainsAsync(ListDomainsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDomainsResponse, Domain> ListDomainsAsync(ListDomainsRequest request, CallSettings callSettings = null)

Lists domains in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDomainsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ListDomainsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDomainsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ListDomainsResponse)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A pageable asynchronous sequence of [Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain) resources.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListDomainsRequest request = new ListDomainsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListDomainsResponse, Domain> response = managedIdentitiesServiceClient.ListDomainsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Domain item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListDomainsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Domain item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Domain> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Domain item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDomainsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDomainsResponse, Domain> ListDomainsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists domains in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the domain location using the form: `projects/{project_id}/locations/global`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDomainsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ListDomainsResponse)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)` | A pageable asynchronous sequence of [Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain) resources.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListDomainsResponse, Domain> response = managedIdentitiesServiceClient.ListDomainsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Domain item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListDomainsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Domain item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Domain> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Domain item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceAttachTrust(string, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> PollOnceAttachTrust(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `AttachTrust`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The result of polling the operation.  
  
### PollOnceAttachTrustAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> PollOnceAttachTrustAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `AttachTrust`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateMicrosoftAdDomain(string, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> PollOnceCreateMicrosoftAdDomain(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateMicrosoftAdDomain`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The result of polling the operation.  
  
### PollOnceCreateMicrosoftAdDomainAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> PollOnceCreateMicrosoftAdDomainAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateMicrosoftAdDomain`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteDomain(string, CallSettings)
    
    
    public virtual Operation<Empty, OpMetadata> PollOnceDeleteDomain(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteDomain`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteDomainAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OpMetadata>> PollOnceDeleteDomainAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteDomain`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDetachTrust(string, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> PollOnceDetachTrust(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DetachTrust`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The result of polling the operation.  
  
### PollOnceDetachTrustAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> PollOnceDetachTrustAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DetachTrust`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceReconfigureTrust(string, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> PollOnceReconfigureTrust(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ReconfigureTrust`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The result of polling the operation.  
  
### PollOnceReconfigureTrustAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> PollOnceReconfigureTrustAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ReconfigureTrust`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateDomain(string, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> PollOnceUpdateDomain(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateDomain`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateDomainAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> PollOnceUpdateDomainAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateDomain`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceValidateTrust(string, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> PollOnceValidateTrust(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ValidateTrust`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The result of polling the operation.  
  
### PollOnceValidateTrustAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> PollOnceValidateTrustAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ValidateTrust`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A task representing the result of polling the operation.  
  
### ReconfigureTrust(DomainName, string, IEnumerable<string>, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> ReconfigureTrust(DomainName name, string targetDomainName, IEnumerable<string> targetDnsIpAddresses, CallSettings callSettings = null)

Updates the DNS conditional forwarder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`targetDomainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully-qualified target domain name which will be in trust with current domain.  
`targetDnsIpAddresses` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The target DNS server IP addresses to resolve the remote domain involved in the trust.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    string targetDomainName = "";
    IEnumerable<string> targetDnsIpAddresses = new string[] { "", };
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.ReconfigureTrust(name, targetDomainName, targetDnsIpAddresses);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceReconfigureTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ReconfigureTrust(ReconfigureTrustRequest, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> ReconfigureTrust(ReconfigureTrustRequest request, CallSettings callSettings = null)

Updates the DNS conditional forwarder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReconfigureTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ReconfigureTrustRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    ReconfigureTrustRequest request = new ReconfigureTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        TargetDomainName = "",
        TargetDnsIpAddresses = { "", },
    };
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.ReconfigureTrust(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceReconfigureTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ReconfigureTrust(string, string, IEnumerable<string>, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> ReconfigureTrust(string name, string targetDomainName, IEnumerable<string> targetDnsIpAddresses, CallSettings callSettings = null)

Updates the DNS conditional forwarder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`targetDomainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully-qualified target domain name which will be in trust with current domain.  
`targetDnsIpAddresses` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The target DNS server IP addresses to resolve the remote domain involved in the trust.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    string targetDomainName = "";
    IEnumerable<string> targetDnsIpAddresses = new string[] { "", };
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.ReconfigureTrust(name, targetDomainName, targetDnsIpAddresses);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceReconfigureTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ReconfigureTrustAsync(DomainName, string, IEnumerable<string>, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ReconfigureTrustAsync(DomainName name, string targetDomainName, IEnumerable<string> targetDnsIpAddresses, CallSettings callSettings = null)

Updates the DNS conditional forwarder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`targetDomainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully-qualified target domain name which will be in trust with current domain.  
`targetDnsIpAddresses` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The target DNS server IP addresses to resolve the remote domain involved in the trust.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    string targetDomainName = "";
    IEnumerable<string> targetDnsIpAddresses = new string[] { "", };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ReconfigureTrustAsync(name, targetDomainName, targetDnsIpAddresses);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceReconfigureTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ReconfigureTrustAsync(DomainName, string, IEnumerable<string>, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ReconfigureTrustAsync(DomainName name, string targetDomainName, IEnumerable<string> targetDnsIpAddresses, CancellationToken cancellationToken)

Updates the DNS conditional forwarder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`targetDomainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully-qualified target domain name which will be in trust with current domain.  
`targetDnsIpAddresses` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The target DNS server IP addresses to resolve the remote domain involved in the trust.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    string targetDomainName = "";
    IEnumerable<string> targetDnsIpAddresses = new string[] { "", };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ReconfigureTrustAsync(name, targetDomainName, targetDnsIpAddresses);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceReconfigureTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ReconfigureTrustAsync(ReconfigureTrustRequest, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ReconfigureTrustAsync(ReconfigureTrustRequest request, CallSettings callSettings = null)

Updates the DNS conditional forwarder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReconfigureTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ReconfigureTrustRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    ReconfigureTrustRequest request = new ReconfigureTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        TargetDomainName = "",
        TargetDnsIpAddresses = { "", },
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ReconfigureTrustAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceReconfigureTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ReconfigureTrustAsync(ReconfigureTrustRequest, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ReconfigureTrustAsync(ReconfigureTrustRequest request, CancellationToken cancellationToken)

Updates the DNS conditional forwarder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReconfigureTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ReconfigureTrustRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    ReconfigureTrustRequest request = new ReconfigureTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        TargetDomainName = "",
        TargetDnsIpAddresses = { "", },
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ReconfigureTrustAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceReconfigureTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ReconfigureTrustAsync(string, string, IEnumerable<string>, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ReconfigureTrustAsync(string name, string targetDomainName, IEnumerable<string> targetDnsIpAddresses, CallSettings callSettings = null)

Updates the DNS conditional forwarder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`targetDomainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully-qualified target domain name which will be in trust with current domain.  
`targetDnsIpAddresses` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The target DNS server IP addresses to resolve the remote domain involved in the trust.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    string targetDomainName = "";
    IEnumerable<string> targetDnsIpAddresses = new string[] { "", };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ReconfigureTrustAsync(name, targetDomainName, targetDnsIpAddresses);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceReconfigureTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ReconfigureTrustAsync(string, string, IEnumerable<string>, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ReconfigureTrustAsync(string name, string targetDomainName, IEnumerable<string> targetDnsIpAddresses, CancellationToken cancellationToken)

Updates the DNS conditional forwarder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`targetDomainName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The fully-qualified target domain name which will be in trust with current domain.  
`targetDnsIpAddresses` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The target DNS server IP addresses to resolve the remote domain involved in the trust.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    string targetDomainName = "";
    IEnumerable<string> targetDnsIpAddresses = new string[] { "", };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ReconfigureTrustAsync(name, targetDomainName, targetDnsIpAddresses);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceReconfigureTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ResetAdminPassword(DomainName, CallSettings)
    
    
    public virtual ResetAdminPasswordResponse ResetAdminPassword(DomainName name, CallSettings callSettings = null)

Resets a domain's administrator password.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ResetAdminPasswordResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    // Make the request
    ResetAdminPasswordResponse response = managedIdentitiesServiceClient.ResetAdminPassword(name);
    

### ResetAdminPassword(ResetAdminPasswordRequest, CallSettings)
    
    
    public virtual ResetAdminPasswordResponse ResetAdminPassword(ResetAdminPasswordRequest request, CallSettings callSettings = null)

Resets a domain's administrator password.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetAdminPasswordRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ResetAdminPasswordResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    ResetAdminPasswordRequest request = new ResetAdminPasswordRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
    };
    // Make the request
    ResetAdminPasswordResponse response = managedIdentitiesServiceClient.ResetAdminPassword(request);
    

### ResetAdminPassword(string, CallSettings)
    
    
    public virtual ResetAdminPasswordResponse ResetAdminPassword(string name, CallSettings callSettings = null)

Resets a domain's administrator password.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ResetAdminPasswordResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    // Make the request
    ResetAdminPasswordResponse response = managedIdentitiesServiceClient.ResetAdminPassword(name);
    

### ResetAdminPasswordAsync(DomainName, CallSettings)
    
    
    public virtual Task<ResetAdminPasswordResponse> ResetAdminPasswordAsync(DomainName name, CallSettings callSettings = null)

Resets a domain's administrator password.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResetAdminPasswordResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    // Make the request
    ResetAdminPasswordResponse response = await managedIdentitiesServiceClient.ResetAdminPasswordAsync(name);
    

### ResetAdminPasswordAsync(DomainName, CancellationToken)
    
    
    public virtual Task<ResetAdminPasswordResponse> ResetAdminPasswordAsync(DomainName name, CancellationToken cancellationToken)

Resets a domain's administrator password.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResetAdminPasswordResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    // Make the request
    ResetAdminPasswordResponse response = await managedIdentitiesServiceClient.ResetAdminPasswordAsync(name);
    

### ResetAdminPasswordAsync(ResetAdminPasswordRequest, CallSettings)
    
    
    public virtual Task<ResetAdminPasswordResponse> ResetAdminPasswordAsync(ResetAdminPasswordRequest request, CallSettings callSettings = null)

Resets a domain's administrator password.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetAdminPasswordRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResetAdminPasswordResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    ResetAdminPasswordRequest request = new ResetAdminPasswordRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
    };
    // Make the request
    ResetAdminPasswordResponse response = await managedIdentitiesServiceClient.ResetAdminPasswordAsync(request);
    

### ResetAdminPasswordAsync(ResetAdminPasswordRequest, CancellationToken)
    
    
    public virtual Task<ResetAdminPasswordResponse> ResetAdminPasswordAsync(ResetAdminPasswordRequest request, CancellationToken cancellationToken)

Resets a domain's administrator password.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetAdminPasswordRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResetAdminPasswordResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    ResetAdminPasswordRequest request = new ResetAdminPasswordRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
    };
    // Make the request
    ResetAdminPasswordResponse response = await managedIdentitiesServiceClient.ResetAdminPasswordAsync(request);
    

### ResetAdminPasswordAsync(string, CallSettings)
    
    
    public virtual Task<ResetAdminPasswordResponse> ResetAdminPasswordAsync(string name, CallSettings callSettings = null)

Resets a domain's administrator password.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResetAdminPasswordResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    // Make the request
    ResetAdminPasswordResponse response = await managedIdentitiesServiceClient.ResetAdminPasswordAsync(name);
    

### ResetAdminPasswordAsync(string, CancellationToken)
    
    
    public virtual Task<ResetAdminPasswordResponse> ResetAdminPasswordAsync(string name, CancellationToken cancellationToken)

Resets a domain's administrator password.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The domain resource name using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResetAdminPasswordResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ResetAdminPasswordResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    // Make the request
    ResetAdminPasswordResponse response = await managedIdentitiesServiceClient.ResetAdminPasswordAsync(name);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient#Google_Cloud_ManagedIdentities_V1_ManagedIdentitiesServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient#Google_Cloud_ManagedIdentities_V1_ManagedIdentitiesServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient#Google_Cloud_ManagedIdentities_V1_ManagedIdentitiesServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ManagedIdentitiesServiceClient#Google_Cloud_ManagedIdentities_V1_ManagedIdentitiesServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateDomain(Domain, FieldMask, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> UpdateDomain(Domain domain, FieldMask updateMask, CallSettings callSettings = null)

Updates the metadata and configuration of a domain.

**Parameters**  
---  
**Name** | **Description**  
`domain` | `[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)`  
Required. Domain message with updated fields. Only supported fields specified in update_mask are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include fields from [Domain][google.cloud.managedidentities.v1.Domain]:

  * `labels`
  * `locations`
  * `authorized_networks`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    Domain domain = new Domain();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.UpdateDomain(domain, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceUpdateDomain(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDomain(UpdateDomainRequest, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> UpdateDomain(UpdateDomainRequest request, CallSettings callSettings = null)

Updates the metadata and configuration of a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.UpdateDomainRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    UpdateDomainRequest request = new UpdateDomainRequest
    {
        UpdateMask = new FieldMask(),
        Domain = new Domain(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.UpdateDomain(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceUpdateDomain(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDomainAsync(Domain, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> UpdateDomainAsync(Domain domain, FieldMask updateMask, CallSettings callSettings = null)

Updates the metadata and configuration of a domain.

**Parameters**  
---  
**Name** | **Description**  
`domain` | `[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)`  
Required. Domain message with updated fields. Only supported fields specified in update_mask are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include fields from [Domain][google.cloud.managedidentities.v1.Domain]:

  * `labels`
  * `locations`
  * `authorized_networks`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    Domain domain = new Domain();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.UpdateDomainAsync(domain, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceUpdateDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDomainAsync(Domain, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> UpdateDomainAsync(Domain domain, FieldMask updateMask, CancellationToken cancellationToken)

Updates the metadata and configuration of a domain.

**Parameters**  
---  
**Name** | **Description**  
`domain` | `[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)`  
Required. Domain message with updated fields. Only supported fields specified in update_mask are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include fields from [Domain][google.cloud.managedidentities.v1.Domain]:

  * `labels`
  * `locations`
  * `authorized_networks`

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    Domain domain = new Domain();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.UpdateDomainAsync(domain, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceUpdateDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDomainAsync(UpdateDomainRequest, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> UpdateDomainAsync(UpdateDomainRequest request, CallSettings callSettings = null)

Updates the metadata and configuration of a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.UpdateDomainRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDomainRequest request = new UpdateDomainRequest
    {
        UpdateMask = new FieldMask(),
        Domain = new Domain(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.UpdateDomainAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceUpdateDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDomainAsync(UpdateDomainRequest, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> UpdateDomainAsync(UpdateDomainRequest request, CancellationToken cancellationToken)

Updates the metadata and configuration of a domain.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDomainRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.UpdateDomainRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDomainRequest request = new UpdateDomainRequest
    {
        UpdateMask = new FieldMask(),
        Domain = new Domain(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.UpdateDomainAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceUpdateDomainAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ValidateTrust(DomainName, Trust, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> ValidateTrust(DomainName name, Trust trust, CallSettings callSettings = null)

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust to validate trust state for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.ValidateTrust(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceValidateTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ValidateTrust(ValidateTrustRequest, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> ValidateTrust(ValidateTrustRequest request, CallSettings callSettings = null)

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ValidateTrustRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    ValidateTrustRequest request = new ValidateTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        Trust = new Trust(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.ValidateTrust(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceValidateTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ValidateTrust(string, Trust, CallSettings)
    
    
    public virtual Operation<Domain, OpMetadata> ValidateTrust(string name, Trust trust, CallSettings callSettings = null)

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust to validate trust state for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = ManagedIdentitiesServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = managedIdentitiesServiceClient.ValidateTrust(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = managedIdentitiesServiceClient.PollOnceValidateTrust(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ValidateTrustAsync(DomainName, Trust, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ValidateTrustAsync(DomainName name, Trust trust, CallSettings callSettings = null)

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust to validate trust state for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ValidateTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceValidateTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ValidateTrustAsync(DomainName, Trust, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ValidateTrustAsync(DomainName name, Trust trust, CancellationToken cancellationToken)

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust to validate trust state for.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    DomainName name = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]");
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ValidateTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceValidateTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ValidateTrustAsync(ValidateTrustRequest, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ValidateTrustAsync(ValidateTrustRequest request, CallSettings callSettings = null)

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ValidateTrustRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    ValidateTrustRequest request = new ValidateTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        Trust = new Trust(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ValidateTrustAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceValidateTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ValidateTrustAsync(ValidateTrustRequest, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ValidateTrustAsync(ValidateTrustRequest request, CancellationToken cancellationToken)

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.ValidateTrustRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    ValidateTrustRequest request = new ValidateTrustRequest
    {
        DomainName = DomainName.FromProjectLocationDomain("[PROJECT]", "[LOCATION]", "[DOMAIN]"),
        Trust = new Trust(),
    };
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ValidateTrustAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceValidateTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ValidateTrustAsync(string, Trust, CallSettings)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ValidateTrustAsync(string name, Trust trust, CallSettings callSettings = null)

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust to validate trust state for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ValidateTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceValidateTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

### ValidateTrustAsync(string, Trust, CancellationToken)
    
    
    public virtual Task<Operation<Domain, OpMetadata>> ValidateTrustAsync(string name, Trust trust, CancellationToken cancellationToken)

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` | `[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)`  
Required. The domain trust to validate trust state for.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Domain)[OpMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.OpMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedIdentitiesServiceClient managedIdentitiesServiceClient = await ManagedIdentitiesServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/domains/[DOMAIN]";
    Trust trust = new Trust();
    // Make the request
    Operation<Domain, OpMetadata> response = await managedIdentitiesServiceClient.ValidateTrustAsync(name, trust);
    
    // Poll until the returned long-running operation is complete
    Operation<Domain, OpMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Domain result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Domain, OpMetadata> retrievedResponse = await managedIdentitiesServiceClient.PollOnceValidateTrustAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Domain retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
