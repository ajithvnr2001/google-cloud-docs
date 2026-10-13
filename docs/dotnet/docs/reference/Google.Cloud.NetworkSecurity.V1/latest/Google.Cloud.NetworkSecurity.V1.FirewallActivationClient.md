---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient
title: Network Security v1 API - Class FirewallActivationClient (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:43.765168+00:00
---

# Network Security v1 API - Class FirewallActivationClient (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Security v1 API - Class FirewallActivationClient (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract class FirewallActivationClient

Reference documentation and code samples for the Network Security v1 API class FirewallActivationClient.

FirewallActivation client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FirewallActivationClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[FirewallActivationClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClientImpl)

## Namespace

[Google.Cloud.NetworkSecurity.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1)

## Assembly

Google.Cloud.NetworkSecurity.V1.dll

## Remarks

Service for managing Firewall Endpoints and Associations.

## Properties 

### CreateFirewallEndpointAssociationOperationsClient
    
    
    public virtual OperationsClient CreateFirewallEndpointAssociationOperationsClient { get; }

The long-running operations client for `CreateFirewallEndpointAssociation`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateFirewallEndpointOperationsClient
    
    
    public virtual OperationsClient CreateFirewallEndpointOperationsClient { get; }

The long-running operations client for `CreateFirewallEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateProjectFirewallEndpointOperationsClient
    
    
    public virtual OperationsClient CreateProjectFirewallEndpointOperationsClient { get; }

The long-running operations client for `CreateProjectFirewallEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the FirewallActivation service, which is a host of "networksecurity.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default FirewallActivation scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default FirewallActivation scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteFirewallEndpointAssociationOperationsClient
    
    
    public virtual OperationsClient DeleteFirewallEndpointAssociationOperationsClient { get; }

The long-running operations client for `DeleteFirewallEndpointAssociation`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteFirewallEndpointOperationsClient
    
    
    public virtual OperationsClient DeleteFirewallEndpointOperationsClient { get; }

The long-running operations client for `DeleteFirewallEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteProjectFirewallEndpointOperationsClient
    
    
    public virtual OperationsClient DeleteProjectFirewallEndpointOperationsClient { get; }

The long-running operations client for `DeleteProjectFirewallEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual FirewallActivation.FirewallActivationClient GrpcClient { get; }

The underlying gRPC FirewallActivation client

**Property Value**  
---  
**Type** | **Description**  
`[FirewallActivation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivation)[FirewallActivationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivation.FirewallActivationClient)` |   
  
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
  
### UpdateFirewallEndpointAssociationOperationsClient
    
    
    public virtual OperationsClient UpdateFirewallEndpointAssociationOperationsClient { get; }

The long-running operations client for `UpdateFirewallEndpointAssociation`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateFirewallEndpointOperationsClient
    
    
    public virtual OperationsClient UpdateFirewallEndpointOperationsClient { get; }

The long-running operations client for `UpdateFirewallEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateProjectFirewallEndpointOperationsClient
    
    
    public virtual OperationsClient UpdateProjectFirewallEndpointOperationsClient { get; }

The long-running operations client for `UpdateProjectFirewallEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static FirewallActivationClient Create()

Synchronously creates a [FirewallActivationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [FirewallActivationClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClientBuilder) .

**Returns**  
---  
**Type** | **Description**  
`[FirewallActivationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient)` | The created [FirewallActivationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<FirewallActivationClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [FirewallActivationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [FirewallActivationClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClientBuilder) .

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallActivationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient)` | The task representing the created [FirewallActivationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient).  
  
### CreateFirewallEndpoint(LocationName, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> CreateFirewallEndpoint(LocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.CreateFirewallEndpoint(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpoint(CreateFirewallEndpointRequest, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> CreateFirewallEndpoint(CreateFirewallEndpointRequest request, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    CreateFirewallEndpointRequest request = new CreateFirewallEndpointRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        FirewallEndpointId = "",
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.CreateFirewallEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpoint(OrganizationLocationName, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> CreateFirewallEndpoint(OrganizationLocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.CreateFirewallEndpoint(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpoint(string, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> CreateFirewallEndpoint(string parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.CreateFirewallEndpoint(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAssociation(LocationName, FirewallEndpointAssociation, string, CallSettings)
    
    
    public virtual Operation<FirewallEndpointAssociation, OperationMetadata> CreateFirewallEndpointAssociation(LocationName parent, FirewallEndpointAssociation firewallEndpointAssociation, string firewallEndpointAssociationId, CallSettings callSettings = null)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`firewallEndpointAssociation` | `[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)`  
Required. The resource being created  
`firewallEndpointAssociationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FirewallEndpointAssociation firewallEndpointAssociation = new FirewallEndpointAssociation();
    string firewallEndpointAssociationId = "";
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = firewallActivationClient.CreateFirewallEndpointAssociation(parent, firewallEndpointAssociation, firewallEndpointAssociationId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateFirewallEndpointAssociation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAssociation(CreateFirewallEndpointAssociationRequest, CallSettings)
    
    
    public virtual Operation<FirewallEndpointAssociation, OperationMetadata> CreateFirewallEndpointAssociation(CreateFirewallEndpointAssociationRequest request, CallSettings callSettings = null)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    CreateFirewallEndpointAssociationRequest request = new CreateFirewallEndpointAssociationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FirewallEndpointAssociationId = "",
        FirewallEndpointAssociation = new FirewallEndpointAssociation(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = firewallActivationClient.CreateFirewallEndpointAssociation(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateFirewallEndpointAssociation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAssociation(string, FirewallEndpointAssociation, string, CallSettings)
    
    
    public virtual Operation<FirewallEndpointAssociation, OperationMetadata> CreateFirewallEndpointAssociation(string parent, FirewallEndpointAssociation firewallEndpointAssociation, string firewallEndpointAssociationId, CallSettings callSettings = null)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`firewallEndpointAssociation` | `[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)`  
Required. The resource being created  
`firewallEndpointAssociationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    FirewallEndpointAssociation firewallEndpointAssociation = new FirewallEndpointAssociation();
    string firewallEndpointAssociationId = "";
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = firewallActivationClient.CreateFirewallEndpointAssociation(parent, firewallEndpointAssociation, firewallEndpointAssociationId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateFirewallEndpointAssociation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAssociationAsync(LocationName, FirewallEndpointAssociation, string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> CreateFirewallEndpointAssociationAsync(LocationName parent, FirewallEndpointAssociation firewallEndpointAssociation, string firewallEndpointAssociationId, CallSettings callSettings = null)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`firewallEndpointAssociation` | `[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)`  
Required. The resource being created  
`firewallEndpointAssociationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FirewallEndpointAssociation firewallEndpointAssociation = new FirewallEndpointAssociation();
    string firewallEndpointAssociationId = "";
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAssociationAsync(parent, firewallEndpointAssociation, firewallEndpointAssociationId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAssociationAsync(LocationName, FirewallEndpointAssociation, string, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> CreateFirewallEndpointAssociationAsync(LocationName parent, FirewallEndpointAssociation firewallEndpointAssociation, string firewallEndpointAssociationId, CancellationToken cancellationToken)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`firewallEndpointAssociation` | `[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)`  
Required. The resource being created  
`firewallEndpointAssociationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FirewallEndpointAssociation firewallEndpointAssociation = new FirewallEndpointAssociation();
    string firewallEndpointAssociationId = "";
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAssociationAsync(parent, firewallEndpointAssociation, firewallEndpointAssociationId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAssociationAsync(CreateFirewallEndpointAssociationRequest, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> CreateFirewallEndpointAssociationAsync(CreateFirewallEndpointAssociationRequest request, CallSettings callSettings = null)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    CreateFirewallEndpointAssociationRequest request = new CreateFirewallEndpointAssociationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FirewallEndpointAssociationId = "",
        FirewallEndpointAssociation = new FirewallEndpointAssociation(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAssociationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAssociationAsync(CreateFirewallEndpointAssociationRequest, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> CreateFirewallEndpointAssociationAsync(CreateFirewallEndpointAssociationRequest request, CancellationToken cancellationToken)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    CreateFirewallEndpointAssociationRequest request = new CreateFirewallEndpointAssociationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FirewallEndpointAssociationId = "",
        FirewallEndpointAssociation = new FirewallEndpointAssociation(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAssociationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAssociationAsync(string, FirewallEndpointAssociation, string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> CreateFirewallEndpointAssociationAsync(string parent, FirewallEndpointAssociation firewallEndpointAssociation, string firewallEndpointAssociationId, CallSettings callSettings = null)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`firewallEndpointAssociation` | `[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)`  
Required. The resource being created  
`firewallEndpointAssociationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    FirewallEndpointAssociation firewallEndpointAssociation = new FirewallEndpointAssociation();
    string firewallEndpointAssociationId = "";
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAssociationAsync(parent, firewallEndpointAssociation, firewallEndpointAssociationId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAssociationAsync(string, FirewallEndpointAssociation, string, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> CreateFirewallEndpointAssociationAsync(string parent, FirewallEndpointAssociation firewallEndpointAssociation, string firewallEndpointAssociationId, CancellationToken cancellationToken)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`firewallEndpointAssociation` | `[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)`  
Required. The resource being created  
`firewallEndpointAssociationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    FirewallEndpointAssociation firewallEndpointAssociation = new FirewallEndpointAssociation();
    string firewallEndpointAssociationId = "";
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAssociationAsync(parent, firewallEndpointAssociation, firewallEndpointAssociationId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAsync(LocationName, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateFirewallEndpointAsync(LocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAsync(LocationName, FirewallEndpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateFirewallEndpointAsync(LocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CancellationToken cancellationToken)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAsync(CreateFirewallEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateFirewallEndpointAsync(CreateFirewallEndpointRequest request, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    CreateFirewallEndpointRequest request = new CreateFirewallEndpointRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        FirewallEndpointId = "",
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAsync(CreateFirewallEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateFirewallEndpointAsync(CreateFirewallEndpointRequest request, CancellationToken cancellationToken)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    CreateFirewallEndpointRequest request = new CreateFirewallEndpointRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        FirewallEndpointId = "",
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAsync(OrganizationLocationName, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateFirewallEndpointAsync(OrganizationLocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAsync(OrganizationLocationName, FirewallEndpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateFirewallEndpointAsync(OrganizationLocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CancellationToken cancellationToken)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAsync(string, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateFirewallEndpointAsync(string parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateFirewallEndpointAsync(string, FirewallEndpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateFirewallEndpointAsync(string parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CancellationToken cancellationToken)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpoint(LocationName, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> CreateProjectFirewallEndpoint(LocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.CreateProjectFirewallEndpoint(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateProjectFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpoint(CreateFirewallEndpointRequest, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> CreateProjectFirewallEndpoint(CreateFirewallEndpointRequest request, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    CreateFirewallEndpointRequest request = new CreateFirewallEndpointRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        FirewallEndpointId = "",
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.CreateProjectFirewallEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateProjectFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpoint(OrganizationLocationName, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> CreateProjectFirewallEndpoint(OrganizationLocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.CreateProjectFirewallEndpoint(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateProjectFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpoint(string, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> CreateProjectFirewallEndpoint(string parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.CreateProjectFirewallEndpoint(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceCreateProjectFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpointAsync(LocationName, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateProjectFirewallEndpointAsync(LocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateProjectFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpointAsync(LocationName, FirewallEndpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateProjectFirewallEndpointAsync(LocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CancellationToken cancellationToken)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateProjectFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpointAsync(CreateFirewallEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateProjectFirewallEndpointAsync(CreateFirewallEndpointRequest request, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    CreateFirewallEndpointRequest request = new CreateFirewallEndpointRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        FirewallEndpointId = "",
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateProjectFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpointAsync(CreateFirewallEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateProjectFirewallEndpointAsync(CreateFirewallEndpointRequest request, CancellationToken cancellationToken)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    CreateFirewallEndpointRequest request = new CreateFirewallEndpointRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        FirewallEndpointId = "",
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateProjectFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpointAsync(OrganizationLocationName, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateProjectFirewallEndpointAsync(OrganizationLocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateProjectFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpointAsync(OrganizationLocationName, FirewallEndpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateProjectFirewallEndpointAsync(OrganizationLocationName parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CancellationToken cancellationToken)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateProjectFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpointAsync(string, FirewallEndpoint, string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateProjectFirewallEndpointAsync(string parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CallSettings callSettings = null)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateProjectFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateProjectFirewallEndpointAsync(string, FirewallEndpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> CreateProjectFirewallEndpointAsync(string parent, FirewallEndpoint firewallEndpoint, string firewallEndpointId, CancellationToken cancellationToken)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being created  
`firewallEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_id from the method_signature of Create RPC.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    string firewallEndpointId = "";
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.CreateProjectFirewallEndpointAsync(parent, firewallEndpoint, firewallEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceCreateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpoint(DeleteFirewallEndpointRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFirewallEndpoint(DeleteFirewallEndpointRequest request, CallSettings callSettings = null)

Deletes a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    DeleteFirewallEndpointRequest request = new DeleteFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = firewallActivationClient.DeleteFirewallEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceDeleteFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpoint(FirewallEndpointName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFirewallEndpoint(FirewallEndpointName name, CallSettings callSettings = null)

Deletes a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = firewallActivationClient.DeleteFirewallEndpoint(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceDeleteFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpoint(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFirewallEndpoint(string name, CallSettings callSettings = null)

Deletes a single org Endpoint.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = firewallActivationClient.DeleteFirewallEndpoint(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceDeleteFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAssociation(DeleteFirewallEndpointAssociationRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFirewallEndpointAssociation(DeleteFirewallEndpointAssociationRequest request, CallSettings callSettings = null)

Deletes a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    DeleteFirewallEndpointAssociationRequest request = new DeleteFirewallEndpointAssociationRequest
    {
        FirewallEndpointAssociationName = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = firewallActivationClient.DeleteFirewallEndpointAssociation(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceDeleteFirewallEndpointAssociation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAssociation(FirewallEndpointAssociationName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFirewallEndpointAssociation(FirewallEndpointAssociationName name, CallSettings callSettings = null)

Deletes a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointAssociationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociationName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    FirewallEndpointAssociationName name = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = firewallActivationClient.DeleteFirewallEndpointAssociation(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceDeleteFirewallEndpointAssociation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAssociation(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFirewallEndpointAssociation(string name, CallSettings callSettings = null)

Deletes a single FirewallEndpointAssociation.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/firewallEndpointAssociations/[FIREWALL_ENDPOINT_ASSOCIATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = firewallActivationClient.DeleteFirewallEndpointAssociation(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceDeleteFirewallEndpointAssociation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAssociationAsync(DeleteFirewallEndpointAssociationRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAssociationAsync(DeleteFirewallEndpointAssociationRequest request, CallSettings callSettings = null)

Deletes a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFirewallEndpointAssociationRequest request = new DeleteFirewallEndpointAssociationRequest
    {
        FirewallEndpointAssociationName = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAssociationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAssociationAsync(DeleteFirewallEndpointAssociationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAssociationAsync(DeleteFirewallEndpointAssociationRequest request, CancellationToken cancellationToken)

Deletes a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFirewallEndpointAssociationRequest request = new DeleteFirewallEndpointAssociationRequest
    {
        FirewallEndpointAssociationName = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAssociationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAssociationAsync(FirewallEndpointAssociationName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAssociationAsync(FirewallEndpointAssociationName name, CallSettings callSettings = null)

Deletes a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointAssociationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociationName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointAssociationName name = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAssociationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAssociationAsync(FirewallEndpointAssociationName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAssociationAsync(FirewallEndpointAssociationName name, CancellationToken cancellationToken)

Deletes a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointAssociationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociationName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointAssociationName name = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAssociationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAssociationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAssociationAsync(string name, CallSettings callSettings = null)

Deletes a single FirewallEndpointAssociation.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/firewallEndpointAssociations/[FIREWALL_ENDPOINT_ASSOCIATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAssociationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAssociationAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAssociationAsync(string name, CancellationToken cancellationToken)

Deletes a single FirewallEndpointAssociation.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/firewallEndpointAssociations/[FIREWALL_ENDPOINT_ASSOCIATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAssociationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAsync(DeleteFirewallEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAsync(DeleteFirewallEndpointRequest request, CallSettings callSettings = null)

Deletes a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFirewallEndpointRequest request = new DeleteFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAsync(DeleteFirewallEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAsync(DeleteFirewallEndpointRequest request, CancellationToken cancellationToken)

Deletes a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFirewallEndpointRequest request = new DeleteFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAsync(FirewallEndpointName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAsync(FirewallEndpointName name, CallSettings callSettings = null)

Deletes a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAsync(FirewallEndpointName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAsync(FirewallEndpointName name, CancellationToken cancellationToken)

Deletes a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAsync(string name, CallSettings callSettings = null)

Deletes a single org Endpoint.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFirewallEndpointAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFirewallEndpointAsync(string name, CancellationToken cancellationToken)

Deletes a single org Endpoint.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteFirewallEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProjectFirewallEndpoint(DeleteFirewallEndpointRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteProjectFirewallEndpoint(DeleteFirewallEndpointRequest request, CallSettings callSettings = null)

Deletes a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    DeleteFirewallEndpointRequest request = new DeleteFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = firewallActivationClient.DeleteProjectFirewallEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceDeleteProjectFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProjectFirewallEndpoint(FirewallEndpointName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteProjectFirewallEndpoint(FirewallEndpointName name, CallSettings callSettings = null)

Deletes a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = firewallActivationClient.DeleteProjectFirewallEndpoint(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceDeleteProjectFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProjectFirewallEndpoint(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteProjectFirewallEndpoint(string name, CallSettings callSettings = null)

Deletes a single project Endpoint.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = firewallActivationClient.DeleteProjectFirewallEndpoint(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceDeleteProjectFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProjectFirewallEndpointAsync(DeleteFirewallEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProjectFirewallEndpointAsync(DeleteFirewallEndpointRequest request, CallSettings callSettings = null)

Deletes a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFirewallEndpointRequest request = new DeleteFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteProjectFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProjectFirewallEndpointAsync(DeleteFirewallEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProjectFirewallEndpointAsync(DeleteFirewallEndpointRequest request, CancellationToken cancellationToken)

Deletes a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFirewallEndpointRequest request = new DeleteFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteProjectFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProjectFirewallEndpointAsync(FirewallEndpointName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProjectFirewallEndpointAsync(FirewallEndpointName name, CallSettings callSettings = null)

Deletes a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteProjectFirewallEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProjectFirewallEndpointAsync(FirewallEndpointName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProjectFirewallEndpointAsync(FirewallEndpointName name, CancellationToken cancellationToken)

Deletes a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteProjectFirewallEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProjectFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProjectFirewallEndpointAsync(string name, CallSettings callSettings = null)

Deletes a single project Endpoint.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteProjectFirewallEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProjectFirewallEndpointAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProjectFirewallEndpointAsync(string name, CancellationToken cancellationToken)

Deletes a single project Endpoint.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await firewallActivationClient.DeleteProjectFirewallEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceDeleteProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetFirewallEndpoint(FirewallEndpointName, CallSettings)
    
    
    public virtual FirewallEndpoint GetFirewallEndpoint(FirewallEndpointName name, CallSettings callSettings = null)

Gets details of a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    FirewallEndpoint response = firewallActivationClient.GetFirewallEndpoint(name);
    

### GetFirewallEndpoint(GetFirewallEndpointRequest, CallSettings)
    
    
    public virtual FirewallEndpoint GetFirewallEndpoint(GetFirewallEndpointRequest request, CallSettings callSettings = null)

Gets details of a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    GetFirewallEndpointRequest request = new GetFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
    };
    // Make the request
    FirewallEndpoint response = firewallActivationClient.GetFirewallEndpoint(request);
    

### GetFirewallEndpoint(string, CallSettings)
    
    
    public virtual FirewallEndpoint GetFirewallEndpoint(string name, CallSettings callSettings = null)

Gets details of a single org Endpoint.

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
`[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    FirewallEndpoint response = firewallActivationClient.GetFirewallEndpoint(name);
    

### GetFirewallEndpointAssociation(FirewallEndpointAssociationName, CallSettings)
    
    
    public virtual FirewallEndpointAssociation GetFirewallEndpointAssociation(FirewallEndpointAssociationName name, CallSettings callSettings = null)

Gets details of a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointAssociationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociationName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    FirewallEndpointAssociationName name = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]");
    // Make the request
    FirewallEndpointAssociation response = firewallActivationClient.GetFirewallEndpointAssociation(name);
    

### GetFirewallEndpointAssociation(GetFirewallEndpointAssociationRequest, CallSettings)
    
    
    public virtual FirewallEndpointAssociation GetFirewallEndpointAssociation(GetFirewallEndpointAssociationRequest request, CallSettings callSettings = null)

Gets details of a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    GetFirewallEndpointAssociationRequest request = new GetFirewallEndpointAssociationRequest
    {
        FirewallEndpointAssociationName = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]"),
    };
    // Make the request
    FirewallEndpointAssociation response = firewallActivationClient.GetFirewallEndpointAssociation(request);
    

### GetFirewallEndpointAssociation(string, CallSettings)
    
    
    public virtual FirewallEndpointAssociation GetFirewallEndpointAssociation(string name, CallSettings callSettings = null)

Gets details of a single FirewallEndpointAssociation.

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
`[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/firewallEndpointAssociations/[FIREWALL_ENDPOINT_ASSOCIATION]";
    // Make the request
    FirewallEndpointAssociation response = firewallActivationClient.GetFirewallEndpointAssociation(name);
    

### GetFirewallEndpointAssociationAsync(FirewallEndpointAssociationName, CallSettings)
    
    
    public virtual Task<FirewallEndpointAssociation> GetFirewallEndpointAssociationAsync(FirewallEndpointAssociationName name, CallSettings callSettings = null)

Gets details of a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointAssociationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociationName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointAssociationName name = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]");
    // Make the request
    FirewallEndpointAssociation response = await firewallActivationClient.GetFirewallEndpointAssociationAsync(name);
    

### GetFirewallEndpointAssociationAsync(FirewallEndpointAssociationName, CancellationToken)
    
    
    public virtual Task<FirewallEndpointAssociation> GetFirewallEndpointAssociationAsync(FirewallEndpointAssociationName name, CancellationToken cancellationToken)

Gets details of a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointAssociationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociationName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointAssociationName name = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]");
    // Make the request
    FirewallEndpointAssociation response = await firewallActivationClient.GetFirewallEndpointAssociationAsync(name);
    

### GetFirewallEndpointAssociationAsync(GetFirewallEndpointAssociationRequest, CallSettings)
    
    
    public virtual Task<FirewallEndpointAssociation> GetFirewallEndpointAssociationAsync(GetFirewallEndpointAssociationRequest request, CallSettings callSettings = null)

Gets details of a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    GetFirewallEndpointAssociationRequest request = new GetFirewallEndpointAssociationRequest
    {
        FirewallEndpointAssociationName = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]"),
    };
    // Make the request
    FirewallEndpointAssociation response = await firewallActivationClient.GetFirewallEndpointAssociationAsync(request);
    

### GetFirewallEndpointAssociationAsync(GetFirewallEndpointAssociationRequest, CancellationToken)
    
    
    public virtual Task<FirewallEndpointAssociation> GetFirewallEndpointAssociationAsync(GetFirewallEndpointAssociationRequest request, CancellationToken cancellationToken)

Gets details of a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    GetFirewallEndpointAssociationRequest request = new GetFirewallEndpointAssociationRequest
    {
        FirewallEndpointAssociationName = FirewallEndpointAssociationName.FromProjectLocationFirewallEndpointAssociation("[PROJECT]", "[LOCATION]", "[FIREWALL_ENDPOINT_ASSOCIATION]"),
    };
    // Make the request
    FirewallEndpointAssociation response = await firewallActivationClient.GetFirewallEndpointAssociationAsync(request);
    

### GetFirewallEndpointAssociationAsync(string, CallSettings)
    
    
    public virtual Task<FirewallEndpointAssociation> GetFirewallEndpointAssociationAsync(string name, CallSettings callSettings = null)

Gets details of a single FirewallEndpointAssociation.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/firewallEndpointAssociations/[FIREWALL_ENDPOINT_ASSOCIATION]";
    // Make the request
    FirewallEndpointAssociation response = await firewallActivationClient.GetFirewallEndpointAssociationAsync(name);
    

### GetFirewallEndpointAssociationAsync(string, CancellationToken)
    
    
    public virtual Task<FirewallEndpointAssociation> GetFirewallEndpointAssociationAsync(string name, CancellationToken cancellationToken)

Gets details of a single FirewallEndpointAssociation.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/firewallEndpointAssociations/[FIREWALL_ENDPOINT_ASSOCIATION]";
    // Make the request
    FirewallEndpointAssociation response = await firewallActivationClient.GetFirewallEndpointAssociationAsync(name);
    

### GetFirewallEndpointAsync(FirewallEndpointName, CallSettings)
    
    
    public virtual Task<FirewallEndpoint> GetFirewallEndpointAsync(FirewallEndpointName name, CallSettings callSettings = null)

Gets details of a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetFirewallEndpointAsync(name);
    

### GetFirewallEndpointAsync(FirewallEndpointName, CancellationToken)
    
    
    public virtual Task<FirewallEndpoint> GetFirewallEndpointAsync(FirewallEndpointName name, CancellationToken cancellationToken)

Gets details of a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetFirewallEndpointAsync(name);
    

### GetFirewallEndpointAsync(GetFirewallEndpointRequest, CallSettings)
    
    
    public virtual Task<FirewallEndpoint> GetFirewallEndpointAsync(GetFirewallEndpointRequest request, CallSettings callSettings = null)

Gets details of a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    GetFirewallEndpointRequest request = new GetFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
    };
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetFirewallEndpointAsync(request);
    

### GetFirewallEndpointAsync(GetFirewallEndpointRequest, CancellationToken)
    
    
    public virtual Task<FirewallEndpoint> GetFirewallEndpointAsync(GetFirewallEndpointRequest request, CancellationToken cancellationToken)

Gets details of a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    GetFirewallEndpointRequest request = new GetFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
    };
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetFirewallEndpointAsync(request);
    

### GetFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<FirewallEndpoint> GetFirewallEndpointAsync(string name, CallSettings callSettings = null)

Gets details of a single org Endpoint.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetFirewallEndpointAsync(name);
    

### GetFirewallEndpointAsync(string, CancellationToken)
    
    
    public virtual Task<FirewallEndpoint> GetFirewallEndpointAsync(string name, CancellationToken cancellationToken)

Gets details of a single org Endpoint.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetFirewallEndpointAsync(name);
    

### GetProjectFirewallEndpoint(FirewallEndpointName, CallSettings)
    
    
    public virtual FirewallEndpoint GetProjectFirewallEndpoint(FirewallEndpointName name, CallSettings callSettings = null)

Gets details of a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    FirewallEndpoint response = firewallActivationClient.GetProjectFirewallEndpoint(name);
    

### GetProjectFirewallEndpoint(GetFirewallEndpointRequest, CallSettings)
    
    
    public virtual FirewallEndpoint GetProjectFirewallEndpoint(GetFirewallEndpointRequest request, CallSettings callSettings = null)

Gets details of a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    GetFirewallEndpointRequest request = new GetFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
    };
    // Make the request
    FirewallEndpoint response = firewallActivationClient.GetProjectFirewallEndpoint(request);
    

### GetProjectFirewallEndpoint(string, CallSettings)
    
    
    public virtual FirewallEndpoint GetProjectFirewallEndpoint(string name, CallSettings callSettings = null)

Gets details of a single project Endpoint.

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
`[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    FirewallEndpoint response = firewallActivationClient.GetProjectFirewallEndpoint(name);
    

### GetProjectFirewallEndpointAsync(FirewallEndpointName, CallSettings)
    
    
    public virtual Task<FirewallEndpoint> GetProjectFirewallEndpointAsync(FirewallEndpointName name, CallSettings callSettings = null)

Gets details of a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetProjectFirewallEndpointAsync(name);
    

### GetProjectFirewallEndpointAsync(FirewallEndpointName, CancellationToken)
    
    
    public virtual Task<FirewallEndpoint> GetProjectFirewallEndpointAsync(FirewallEndpointName name, CancellationToken cancellationToken)

Gets details of a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FirewallEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointName name = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]");
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetProjectFirewallEndpointAsync(name);
    

### GetProjectFirewallEndpointAsync(GetFirewallEndpointRequest, CallSettings)
    
    
    public virtual Task<FirewallEndpoint> GetProjectFirewallEndpointAsync(GetFirewallEndpointRequest request, CallSettings callSettings = null)

Gets details of a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    GetFirewallEndpointRequest request = new GetFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
    };
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetProjectFirewallEndpointAsync(request);
    

### GetProjectFirewallEndpointAsync(GetFirewallEndpointRequest, CancellationToken)
    
    
    public virtual Task<FirewallEndpoint> GetProjectFirewallEndpointAsync(GetFirewallEndpointRequest request, CancellationToken cancellationToken)

Gets details of a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    GetFirewallEndpointRequest request = new GetFirewallEndpointRequest
    {
        FirewallEndpointName = FirewallEndpointName.FromOrganizationLocationFirewallEndpoint("[ORGANIZATION]", "[LOCATION]", "[FIREWALL_ENDPOINT]"),
    };
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetProjectFirewallEndpointAsync(request);
    

### GetProjectFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<FirewallEndpoint> GetProjectFirewallEndpointAsync(string name, CallSettings callSettings = null)

Gets details of a single project Endpoint.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetProjectFirewallEndpointAsync(name);
    

### GetProjectFirewallEndpointAsync(string, CancellationToken)
    
    
    public virtual Task<FirewallEndpoint> GetProjectFirewallEndpointAsync(string name, CancellationToken cancellationToken)

Gets details of a single project Endpoint.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "organizations/[ORGANIZATION]/locations/[LOCATION]/firewallEndpoints/[FIREWALL_ENDPOINT]";
    // Make the request
    FirewallEndpoint response = await firewallActivationClient.GetProjectFirewallEndpointAsync(name);
    

### ListFirewallEndpointAssociations(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> ListFirewallEndpointAssociations(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Associations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListAssociationsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointAssociationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointAssociationsResponse)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A pageable sequence of [FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> response = firewallActivationClient.ListFirewallEndpointAssociations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpointAssociation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointAssociationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpointAssociation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpointAssociation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpointAssociation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpointAssociations(ListFirewallEndpointAssociationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> ListFirewallEndpointAssociations(ListFirewallEndpointAssociationsRequest request, CallSettings callSettings = null)

Lists Associations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFirewallEndpointAssociationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointAssociationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointAssociationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointAssociationsResponse)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A pageable sequence of [FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    ListFirewallEndpointAssociationsRequest request = new ListFirewallEndpointAssociationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> response = firewallActivationClient.ListFirewallEndpointAssociations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpointAssociation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointAssociationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpointAssociation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpointAssociation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpointAssociation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpointAssociations(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> ListFirewallEndpointAssociations(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Associations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListAssociationsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointAssociationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointAssociationsResponse)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A pageable sequence of [FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> response = firewallActivationClient.ListFirewallEndpointAssociations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpointAssociation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointAssociationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpointAssociation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpointAssociation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpointAssociation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpointAssociationsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> ListFirewallEndpointAssociationsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Associations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListAssociationsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointAssociationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointAssociationsResponse)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A pageable asynchronous sequence of [FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> response = firewallActivationClient.ListFirewallEndpointAssociationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpointAssociation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointAssociationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpointAssociation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpointAssociation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpointAssociation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpointAssociationsAsync(ListFirewallEndpointAssociationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> ListFirewallEndpointAssociationsAsync(ListFirewallEndpointAssociationsRequest request, CallSettings callSettings = null)

Lists Associations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFirewallEndpointAssociationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointAssociationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointAssociationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointAssociationsResponse)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A pageable asynchronous sequence of [FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    ListFirewallEndpointAssociationsRequest request = new ListFirewallEndpointAssociationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> response = firewallActivationClient.ListFirewallEndpointAssociationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpointAssociation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointAssociationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpointAssociation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpointAssociation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpointAssociation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpointAssociationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> ListFirewallEndpointAssociationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Associations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListAssociationsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointAssociationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointAssociationsResponse)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)` | A pageable asynchronous sequence of [FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointAssociationsResponse, FirewallEndpointAssociation> response = firewallActivationClient.ListFirewallEndpointAssociationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpointAssociation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointAssociationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpointAssociation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpointAssociation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpointAssociation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpoints(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListFirewallEndpoints(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListFirewallEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpoints(ListFirewallEndpointsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListFirewallEndpoints(ListFirewallEndpointsRequest request, CallSettings callSettings = null)

Lists FirewallEndpoints in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFirewallEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    ListFirewallEndpointsRequest request = new ListFirewallEndpointsRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListFirewallEndpoints(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpoints(OrganizationLocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListFirewallEndpoints(OrganizationLocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListFirewallEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpoints(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListFirewallEndpoints(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListFirewallEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpointsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListFirewallEndpointsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable asynchronous sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListFirewallEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpointsAsync(ListFirewallEndpointsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListFirewallEndpointsAsync(ListFirewallEndpointsRequest request, CallSettings callSettings = null)

Lists FirewallEndpoints in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFirewallEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable asynchronous sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    ListFirewallEndpointsRequest request = new ListFirewallEndpointsRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListFirewallEndpointsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpointsAsync(OrganizationLocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListFirewallEndpointsAsync(OrganizationLocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable asynchronous sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListFirewallEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFirewallEndpointsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListFirewallEndpointsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable asynchronous sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListFirewallEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProjectFirewallEndpoints(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListProjectFirewallEndpoints(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListProjectFirewallEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProjectFirewallEndpoints(ListFirewallEndpointsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListProjectFirewallEndpoints(ListFirewallEndpointsRequest request, CallSettings callSettings = null)

Lists FirewallEndpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFirewallEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    ListFirewallEndpointsRequest request = new ListFirewallEndpointsRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListProjectFirewallEndpoints(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProjectFirewallEndpoints(OrganizationLocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListProjectFirewallEndpoints(OrganizationLocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListProjectFirewallEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProjectFirewallEndpoints(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListProjectFirewallEndpoints(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListProjectFirewallEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProjectFirewallEndpointsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListProjectFirewallEndpointsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable asynchronous sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListProjectFirewallEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProjectFirewallEndpointsAsync(ListFirewallEndpointsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListProjectFirewallEndpointsAsync(ListFirewallEndpointsRequest request, CallSettings callSettings = null)

Lists FirewallEndpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFirewallEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable asynchronous sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    ListFirewallEndpointsRequest request = new ListFirewallEndpointsRequest
    {
        ParentAsOrganizationLocationName = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListProjectFirewallEndpointsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProjectFirewallEndpointsAsync(OrganizationLocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListProjectFirewallEndpointsAsync(OrganizationLocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OrganizationLocationName)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable asynchronous sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    OrganizationLocationName parent = OrganizationLocationName.FromOrganizationLocation("[ORGANIZATION]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListProjectFirewallEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProjectFirewallEndpointsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> ListProjectFirewallEndpointsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FirewallEndpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListEndpointsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFirewallEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListFirewallEndpointsResponse)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)` | A pageable asynchronous sequence of [FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint) resources.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "organizations/[ORGANIZATION]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListFirewallEndpointsResponse, FirewallEndpoint> response = firewallActivationClient.ListProjectFirewallEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FirewallEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFirewallEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FirewallEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FirewallEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FirewallEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateFirewallEndpoint(string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> PollOnceCreateFirewallEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateFirewallEndpoint`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateFirewallEndpointAssociation(string, CallSettings)
    
    
    public virtual Operation<FirewallEndpointAssociation, OperationMetadata> PollOnceCreateFirewallEndpointAssociation(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateFirewallEndpointAssociation`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateFirewallEndpointAssociationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> PollOnceCreateFirewallEndpointAssociationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateFirewallEndpointAssociation`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> PollOnceCreateFirewallEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateFirewallEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateProjectFirewallEndpoint(string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> PollOnceCreateProjectFirewallEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateProjectFirewallEndpoint`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateProjectFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> PollOnceCreateProjectFirewallEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateProjectFirewallEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFirewallEndpoint(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteFirewallEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFirewallEndpoint`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteFirewallEndpointAssociation(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteFirewallEndpointAssociation(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFirewallEndpointAssociation`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteFirewallEndpointAssociationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteFirewallEndpointAssociationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFirewallEndpointAssociation`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteFirewallEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFirewallEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteProjectFirewallEndpoint(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteProjectFirewallEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteProjectFirewallEndpoint`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteProjectFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteProjectFirewallEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteProjectFirewallEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateFirewallEndpoint(string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> PollOnceUpdateFirewallEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateFirewallEndpoint`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateFirewallEndpointAssociation(string, CallSettings)
    
    
    public virtual Operation<FirewallEndpointAssociation, OperationMetadata> PollOnceUpdateFirewallEndpointAssociation(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateFirewallEndpointAssociation`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateFirewallEndpointAssociationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> PollOnceUpdateFirewallEndpointAssociationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateFirewallEndpointAssociation`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> PollOnceUpdateFirewallEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateFirewallEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateProjectFirewallEndpoint(string, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> PollOnceUpdateProjectFirewallEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateProjectFirewallEndpoint`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateProjectFirewallEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> PollOnceUpdateProjectFirewallEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateProjectFirewallEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient#Google_Cloud_NetworkSecurity_V1_FirewallActivationClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient#Google_Cloud_NetworkSecurity_V1_FirewallActivationClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient#Google_Cloud_NetworkSecurity_V1_FirewallActivationClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallActivationClient#Google_Cloud_NetworkSecurity_V1_FirewallActivationClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateFirewallEndpoint(FirewallEndpoint, FieldMask, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> UpdateFirewallEndpoint(FirewallEndpoint firewallEndpoint, FieldMask updateMask, CallSettings callSettings = null)

Update a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Endpoint resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.UpdateFirewallEndpoint(firewallEndpoint, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceUpdateFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpoint(UpdateFirewallEndpointRequest, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> UpdateFirewallEndpoint(UpdateFirewallEndpointRequest request, CallSettings callSettings = null)

Update a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    UpdateFirewallEndpointRequest request = new UpdateFirewallEndpointRequest
    {
        UpdateMask = new FieldMask(),
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.UpdateFirewallEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceUpdateFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAssociation(FirewallEndpointAssociation, FieldMask, CallSettings)
    
    
    public virtual Operation<FirewallEndpointAssociation, OperationMetadata> UpdateFirewallEndpointAssociation(FirewallEndpointAssociation firewallEndpointAssociation, FieldMask updateMask, CallSettings callSettings = null)

Update a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`firewallEndpointAssociation` | `[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Association resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    FirewallEndpointAssociation firewallEndpointAssociation = new FirewallEndpointAssociation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = firewallActivationClient.UpdateFirewallEndpointAssociation(firewallEndpointAssociation, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceUpdateFirewallEndpointAssociation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAssociation(UpdateFirewallEndpointAssociationRequest, CallSettings)
    
    
    public virtual Operation<FirewallEndpointAssociation, OperationMetadata> UpdateFirewallEndpointAssociation(UpdateFirewallEndpointAssociationRequest request, CallSettings callSettings = null)

Update a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    UpdateFirewallEndpointAssociationRequest request = new UpdateFirewallEndpointAssociationRequest
    {
        UpdateMask = new FieldMask(),
        FirewallEndpointAssociation = new FirewallEndpointAssociation(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = firewallActivationClient.UpdateFirewallEndpointAssociation(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceUpdateFirewallEndpointAssociation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAssociationAsync(FirewallEndpointAssociation, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> UpdateFirewallEndpointAssociationAsync(FirewallEndpointAssociation firewallEndpointAssociation, FieldMask updateMask, CallSettings callSettings = null)

Update a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`firewallEndpointAssociation` | `[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Association resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointAssociation firewallEndpointAssociation = new FirewallEndpointAssociation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.UpdateFirewallEndpointAssociationAsync(firewallEndpointAssociation, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAssociationAsync(FirewallEndpointAssociation, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> UpdateFirewallEndpointAssociationAsync(FirewallEndpointAssociation firewallEndpointAssociation, FieldMask updateMask, CancellationToken cancellationToken)

Update a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`firewallEndpointAssociation` | `[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Association resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpointAssociation firewallEndpointAssociation = new FirewallEndpointAssociation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.UpdateFirewallEndpointAssociationAsync(firewallEndpointAssociation, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAssociationAsync(UpdateFirewallEndpointAssociationRequest, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> UpdateFirewallEndpointAssociationAsync(UpdateFirewallEndpointAssociationRequest request, CallSettings callSettings = null)

Update a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFirewallEndpointAssociationRequest request = new UpdateFirewallEndpointAssociationRequest
    {
        UpdateMask = new FieldMask(),
        FirewallEndpointAssociation = new FirewallEndpointAssociation(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.UpdateFirewallEndpointAssociationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAssociationAsync(UpdateFirewallEndpointAssociationRequest, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpointAssociation, OperationMetadata>> UpdateFirewallEndpointAssociationAsync(UpdateFirewallEndpointAssociationRequest request, CancellationToken cancellationToken)

Update a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointAssociationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateFirewallEndpointAssociationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpointAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpointAssociation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFirewallEndpointAssociationRequest request = new UpdateFirewallEndpointAssociationRequest
    {
        UpdateMask = new FieldMask(),
        FirewallEndpointAssociation = new FirewallEndpointAssociation(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpointAssociation, OperationMetadata> response = await firewallActivationClient.UpdateFirewallEndpointAssociationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpointAssociation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpointAssociation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpointAssociation, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateFirewallEndpointAssociationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpointAssociation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAsync(FirewallEndpoint, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> UpdateFirewallEndpointAsync(FirewallEndpoint firewallEndpoint, FieldMask updateMask, CallSettings callSettings = null)

Update a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Endpoint resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.UpdateFirewallEndpointAsync(firewallEndpoint, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAsync(FirewallEndpoint, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> UpdateFirewallEndpointAsync(FirewallEndpoint firewallEndpoint, FieldMask updateMask, CancellationToken cancellationToken)

Update a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Endpoint resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.UpdateFirewallEndpointAsync(firewallEndpoint, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAsync(UpdateFirewallEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> UpdateFirewallEndpointAsync(UpdateFirewallEndpointRequest request, CallSettings callSettings = null)

Update a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFirewallEndpointRequest request = new UpdateFirewallEndpointRequest
    {
        UpdateMask = new FieldMask(),
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.UpdateFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFirewallEndpointAsync(UpdateFirewallEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> UpdateFirewallEndpointAsync(UpdateFirewallEndpointRequest request, CancellationToken cancellationToken)

Update a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFirewallEndpointRequest request = new UpdateFirewallEndpointRequest
    {
        UpdateMask = new FieldMask(),
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.UpdateFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProjectFirewallEndpoint(FirewallEndpoint, FieldMask, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> UpdateProjectFirewallEndpoint(FirewallEndpoint firewallEndpoint, FieldMask updateMask, CallSettings callSettings = null)

Update a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Endpoint resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.UpdateProjectFirewallEndpoint(firewallEndpoint, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceUpdateProjectFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProjectFirewallEndpoint(UpdateFirewallEndpointRequest, CallSettings)
    
    
    public virtual Operation<FirewallEndpoint, OperationMetadata> UpdateProjectFirewallEndpoint(UpdateFirewallEndpointRequest request, CallSettings callSettings = null)

Update a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = FirewallActivationClient.Create();
    // Initialize request argument(s)
    UpdateFirewallEndpointRequest request = new UpdateFirewallEndpointRequest
    {
        UpdateMask = new FieldMask(),
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = firewallActivationClient.UpdateProjectFirewallEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = firewallActivationClient.PollOnceUpdateProjectFirewallEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProjectFirewallEndpointAsync(FirewallEndpoint, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> UpdateProjectFirewallEndpointAsync(FirewallEndpoint firewallEndpoint, FieldMask updateMask, CallSettings callSettings = null)

Update a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Endpoint resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.UpdateProjectFirewallEndpointAsync(firewallEndpoint, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProjectFirewallEndpointAsync(FirewallEndpoint, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> UpdateProjectFirewallEndpointAsync(FirewallEndpoint firewallEndpoint, FieldMask updateMask, CancellationToken cancellationToken)

Update a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`firewallEndpoint` | `[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Endpoint resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    FirewallEndpoint firewallEndpoint = new FirewallEndpoint();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.UpdateProjectFirewallEndpointAsync(firewallEndpoint, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProjectFirewallEndpointAsync(UpdateFirewallEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> UpdateProjectFirewallEndpointAsync(UpdateFirewallEndpointRequest request, CallSettings callSettings = null)

Update a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFirewallEndpointRequest request = new UpdateFirewallEndpointRequest
    {
        UpdateMask = new FieldMask(),
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.UpdateProjectFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProjectFirewallEndpointAsync(UpdateFirewallEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<FirewallEndpoint, OperationMetadata>> UpdateProjectFirewallEndpointAsync(UpdateFirewallEndpointRequest request, CancellationToken cancellationToken)

Update a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateFirewallEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FirewallEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.FirewallEndpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FirewallActivationClient firewallActivationClient = await FirewallActivationClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFirewallEndpointRequest request = new UpdateFirewallEndpointRequest
    {
        UpdateMask = new FieldMask(),
        FirewallEndpoint = new FirewallEndpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<FirewallEndpoint, OperationMetadata> response = await firewallActivationClient.UpdateProjectFirewallEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FirewallEndpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FirewallEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FirewallEndpoint, OperationMetadata> retrievedResponse = await firewallActivationClient.PollOnceUpdateProjectFirewallEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FirewallEndpoint retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-01 UTC."],[],[]] 
